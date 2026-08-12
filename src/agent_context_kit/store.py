"""SQLite/FTS5 privado: persistência da evidência e recuperação limitada."""
from __future__ import annotations

from dataclasses import dataclass
import json
import sqlite3
from typing import Any, Iterator, Mapping

from .errors import ValidationError
from .ledger import append_entry, replace_entries
from .models import ContextItem, ITEM_ID_RE, MAX_LIMIT, fts_query, parse_since, truncate, validate_source
from .paths import VaultPaths, atomic_write_json


SCHEMA_VERSION = 1
MAX_GET_TEXT_CHARS = 6_000


@dataclass(frozen=True)
class IngestResult:
    item_id: str
    added: bool
    ledger_added: bool


class ContextStore:
    """Autoridade para evidência normalizada; raw e Ledger são camadas separadas."""

    def __init__(self, paths: VaultPaths) -> None:
        self.paths = paths

    def _connect(self) -> sqlite3.Connection:
        self.paths.ensure_layout()
        connection = sqlite3.connect(self.paths.db, timeout=10, isolation_level=None)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA synchronous = FULL")
        return connection

    def initialize(self) -> None:
        connection = self._connect()
        try:
            # executescript controla sua própria fronteira transacional no
            # sqlite3; um BEGIN anterior gera um falso "no transaction active".
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS meta (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS items (
                    id TEXT PRIMARY KEY,
                    source TEXT NOT NULL,
                    source_item_id TEXT NOT NULL,
                    account TEXT NOT NULL DEFAULT '',
                    occurred_at TEXT NOT NULL,
                    title TEXT,
                    text TEXT NOT NULL,
                    thread_id TEXT,
                    provenance TEXT NOT NULL,
                    who TEXT NOT NULL,
                    who_kind TEXT NOT NULL,
                    raw_path TEXT NOT NULL,
                    captured_at TEXT NOT NULL,
                    UNIQUE(source, account, source_item_id)
                );

                CREATE INDEX IF NOT EXISTS idx_items_recent
                    ON items(occurred_at DESC);
                CREATE INDEX IF NOT EXISTS idx_items_source_recent
                    ON items(source, occurred_at DESC);

                CREATE VIRTUAL TABLE IF NOT EXISTS item_fts USING fts5(
                    item_id UNINDEXED,
                    title,
                    text,
                    tokenize = 'unicode61 remove_diacritics 2'
                );
                """
            )
            connection.execute(
                "INSERT OR REPLACE INTO meta(key, value) VALUES ('schema_version', ?)",
                (str(SCHEMA_VERSION),),
            )
        finally:
            connection.close()

    @staticmethod
    def _row_to_public(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "source": row["source"],
            "source_item_id": row["source_item_id"],
            "account": row["account"] or None,
            "occurred_at": row["occurred_at"],
            "title": row["title"],
            "text": row["text"],
            "thread_id": row["thread_id"],
            "provenance": row["provenance"],
            "who": row["who"],
            "who_kind": row["who_kind"],
        }

    def ingest(self, item: ContextItem) -> IngestResult:
        """Persiste raw → SQLite → Ledger; replays corrigem projeção ausente.

        O cursor de conectores deve ser gravado somente depois deste método
        retornar: se houver queda entre as camadas, a reexecução reaproveita o
        mesmo ID determinístico e fecha a lacuna sem duplicar dados.
        """
        self.initialize()
        raw_path = self.paths.raw_path_for(item.source, item.item_id)
        if raw_path.exists() and raw_path.is_symlink():
            raise ValidationError("Evidência raw em caminho inseguro.")
        raw_document = item.raw_document()
        if not raw_path.exists():
            atomic_write_json(raw_path, raw_document)

        connection = self._connect()
        inserted = False
        try:
            connection.execute("BEGIN IMMEDIATE")
            cursor = connection.execute(
                """
                INSERT OR IGNORE INTO items (
                    id, source, source_item_id, account, occurred_at, title,
                    text, thread_id, provenance, who, who_kind, raw_path, captured_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item.item_id,
                    item.source,
                    item.source_item_id,
                    item.account or "",
                    item.occurred_at,
                    item.title,
                    item.text,
                    item.thread_id,
                    item.provenance,
                    item.who,
                    item.who_kind,
                    str(raw_path.relative_to(self.paths.root)),
                    raw_document["captured_at"],
                ),
            )
            inserted = cursor.rowcount == 1
            if inserted:
                connection.execute(
                    "INSERT INTO item_fts(item_id, title, text) VALUES (?, ?, ?)",
                    (item.item_id, item.title or "", item.text),
                )
            row = connection.execute("SELECT * FROM items WHERE id = ?", (item.item_id,)).fetchone()
            if row is None:  # pragma: no cover - assertion against a SQLite invariant
                raise RuntimeError("Item não persistiu após o commit local.")
            connection.execute("COMMIT")
        except Exception:
            connection.execute("ROLLBACK")
            raise
        finally:
            connection.close()

        ledger_added = append_entry(self.paths, self._row_to_public(row))
        return IngestResult(item_id=item.item_id, added=inserted, ledger_added=ledger_added)

    def search(
        self,
        query: str,
        *,
        source: str | None = None,
        since: str | None = None,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        """Pesquisa FTS parametrizada e devolve somente citações compactas."""
        self.initialize()
        chosen_source = validate_source(source)
        chosen_limit = min(max(int(limit or 5), 1), MAX_LIMIT)
        since_at = parse_since(since, default_days=30)
        match = fts_query(query)
        connection = self._connect()
        try:
            sql = """
                SELECT i.id, i.source, i.occurred_at, i.title, i.who, i.provenance,
                       snippet(item_fts, 2, '', '', '…', 28) AS snippet
                FROM item_fts
                JOIN items AS i ON item_fts.item_id = i.id
                WHERE item_fts MATCH ?
                  AND i.occurred_at >= ?
            """
            parameters: list[object] = [match, since_at]
            if chosen_source is not None:
                sql += " AND i.source = ?"
                parameters.append(chosen_source)
            sql += " ORDER BY bm25(item_fts), i.occurred_at DESC LIMIT ?"
            parameters.append(chosen_limit)
            rows = connection.execute(sql, parameters).fetchall()
        finally:
            connection.close()
        results: list[dict[str, Any]] = []
        for row in rows:
            snippet, was_truncated = truncate(str(row["snippet"] or ""), 500)
            results.append(
                {
                    "id": row["id"],
                    "source": row["source"],
                    "occurred_at": row["occurred_at"],
                    "title": row["title"],
                    "who": row["who"],
                    "provenance": row["provenance"],
                    "snippet": snippet,
                    "snippet_truncated": was_truncated,
                }
            )
        return results

    def get(self, item_id: str, *, text_limit: int = MAX_GET_TEXT_CHARS) -> dict[str, Any] | None:
        """Abre um item por ID explícito sem retornar raw, paths ou credenciais."""
        if not isinstance(item_id, str) or not ITEM_ID_RE.fullmatch(item_id):
            raise ValidationError("ID de contexto inválido.")
        self.initialize()
        connection = self._connect()
        try:
            row = connection.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
        finally:
            connection.close()
        if row is None:
            return None
        public = self._row_to_public(row)
        text, was_truncated = truncate(str(public["text"]), text_limit)
        return {
            "id": public["id"],
            "source": public["source"],
            "occurred_at": public["occurred_at"],
            "title": public["title"],
            "who": public["who"],
            "provenance": public["provenance"],
            "text": text,
            "text_truncated": was_truncated,
            "total_text_chars": len(str(public["text"])),
        }

    def iter_items(self) -> Iterator[dict[str, Any]]:
        self.initialize()
        connection = self._connect()
        try:
            rows = connection.execute("SELECT * FROM items ORDER BY occurred_at, id").fetchall()
            for row in rows:
                yield self._row_to_public(row)
        finally:
            connection.close()

    def rebuild_ledger(self) -> int:
        return replace_entries(self.paths, self.iter_items())

    def source_summary(self) -> list[dict[str, Any]]:
        self.initialize()
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT source, COUNT(*) AS items, MIN(occurred_at) AS first_capture,
                       MAX(occurred_at) AS last_capture
                FROM items GROUP BY source ORDER BY source
                """
            ).fetchall()
        finally:
            connection.close()
        return [dict(row) for row in rows]

    def count(self) -> int:
        self.initialize()
        connection = self._connect()
        try:
            return int(connection.execute("SELECT COUNT(*) FROM items").fetchone()[0])
        finally:
            connection.close()

    def integrity(self) -> str:
        self.initialize()
        connection = self._connect()
        try:
            return str(connection.execute("PRAGMA quick_check").fetchone()[0])
        finally:
            connection.close()

    def purge_source(self, source: str) -> int:
        """Remove explicitamente uma fonte e reconstrói o Ledger restante."""
        chosen_source = validate_source(source)
        assert chosen_source is not None
        self.initialize()
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT id FROM items WHERE source = ?", (chosen_source,)
            ).fetchall()
            connection.execute("BEGIN IMMEDIATE")
            for row in rows:
                connection.execute("DELETE FROM item_fts WHERE item_id = ?", (row["id"],))
            connection.execute("DELETE FROM items WHERE source = ?", (chosen_source,))
            connection.execute("COMMIT")
        except Exception:
            connection.execute("ROLLBACK")
            raise
        finally:
            connection.close()
        for row in rows:
            raw_path = self.paths.raw_path_for(chosen_source, row["id"])
            if raw_path.exists() and not raw_path.is_symlink():
                raw_path.unlink()
        self.rebuild_ledger()
        return len(rows)
