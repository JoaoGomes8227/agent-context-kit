"""Context Ledger compacto, append-only e consultado por janela.

O Ledger é uma projeção navegável da evidência; não é uma segunda memória nem
uma forma de despejar contexto inteiro no agente. A evidência completa segue no
SQLite/raw privado e só é aberta pelo ID explícito retornado numa busca.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Iterator, Mapping, TextIO

from .errors import ValidationError
from .models import MAX_LIMIT, parse_since, safe_excerpt, validate_source
from .paths import (
    FILE_MODE,
    VaultPaths,
    atomic_write_text,
    ensure_private_dir,
    ensure_private_file,
)

try:  # Linux é o alvo inicial; fallback preserva funcionalidade em outros SOs.
    import fcntl
except ImportError:  # pragma: no cover - Windows future profile
    fcntl = None  # type: ignore[assignment]


LEDGER_FIELDS = ("ts", "source", "who", "who_kind", "excerpt", "ref")


def _parse_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def entry_from_mapping(item: Mapping[str, object]) -> dict[str, str]:
    """Projeta um item rico nos seis campos estáveis do Ledger."""
    text = str(item.get("text") or item.get("title") or "")
    return {
        "ts": str(item["occurred_at"]),
        "source": str(item["source"]),
        "who": str(item.get("who") or item.get("title") or item["source"]),
        "who_kind": str(item.get("who_kind") or "desconhecido"),
        "excerpt": safe_excerpt(text),
        "ref": str(item["id"]),
    }


@contextmanager
def _locked_ledger(path: Path) -> Iterator[TextIO]:
    ensure_private_dir(path.parent)
    ensure_private_file(path)
    handle = path.open("a+", encoding="utf-8")
    try:
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield handle
        handle.flush()
    finally:
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def append_entry(paths: VaultPaths, item: Mapping[str, object]) -> bool:
    """Apende uma projeção uma única vez por ``ref``.

    A deduplicação é deliberadamente local e simples: um item já persistido
    pode ser reprocessado com segurança após queda ou backfill. O SQLite é a
    autoridade para a evidência; este scan reduz a superfície de falha entre a
    projeção JSONL e o banco sem expor o arquivo ao agente.
    """
    entry = entry_from_mapping(item)
    with _locked_ledger(paths.ledger) as handle:
        handle.seek(0)
        for line in handle:
            try:
                existing = json.loads(line)
            except json.JSONDecodeError:
                continue
            if existing.get("ref") == entry["ref"]:
                return False
        handle.seek(0, 2)
        handle.write(json.dumps(entry, ensure_ascii=False, separators=(",", ":")) + "\n")
        handle.flush()
        # O fsync é importante: o cursor de um conector só avança depois disso.
        import os

        os.fsync(handle.fileno())
    try:
        paths.ledger.chmod(FILE_MODE)
    except OSError:
        pass
    return True


def _reverse_lines(path: Path, *, block_size: int = 8192) -> Iterator[str]:
    """Itera JSONL do fim para o começo sem materializar o arquivo inteiro."""
    ensure_private_file(path)
    with path.open("rb") as handle:
        handle.seek(0, 2)
        position = handle.tell()
        remainder = b""
        while position > 0:
            size = min(block_size, position)
            position -= size
            handle.seek(position)
            block = handle.read(size)
            pieces = (block + remainder).split(b"\n")
            remainder = pieces[0]
            for piece in reversed(pieces[1:]):
                if piece:
                    yield piece.decode("utf-8", "replace")
        if remainder:
            yield remainder.decode("utf-8", "replace")


def list_recent(
    paths: VaultPaths,
    *,
    source: str | None = None,
    who: str | None = None,
    since: str | None = None,
    limit: int | None = None,
) -> list[dict[str, str]]:
    """Lê somente uma janela compacta; nunca devolve o Ledger inteiro."""
    chosen_source = validate_source(source)
    chosen_limit = min(max(int(limit or 5), 1), MAX_LIMIT)
    since_at = _parse_timestamp(parse_since(since, default_days=7))
    assert since_at is not None
    who_query = str(who or "").strip().lower()
    if len(who_query) > 128:
        raise ValidationError("O filtro de pessoa é longo demais.")
    if not paths.ledger.exists():
        return []

    rows: list[dict[str, str]] = []
    for line in _reverse_lines(paths.ledger):
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(row, dict) or set(row) != set(LEDGER_FIELDS):
            continue
        timestamp = _parse_timestamp(row.get("ts"))
        if timestamp is None or timestamp < since_at:
            continue
        if chosen_source is not None and row.get("source") != chosen_source:
            continue
        haystack = f"{row.get('who', '')} {row.get('excerpt', '')}".lower()
        if who_query and who_query not in haystack:
            continue
        rows.append({field: str(row[field]) for field in LEDGER_FIELDS})
        if len(rows) >= chosen_limit:
            break
    return rows


def count_entries(paths: VaultPaths) -> int:
    if not paths.ledger.exists():
        return 0
    ensure_private_file(paths.ledger)
    count = 0
    with paths.ledger.open("r", encoding="utf-8") as handle:
        for line in handle:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict) and set(row) == set(LEDGER_FIELDS):
                count += 1
    return count


def replace_entries(paths: VaultPaths, entries: Iterator[Mapping[str, object]]) -> int:
    """Reconstrói explicitamente o Ledger a partir do SQLite, com troca atômica."""
    lines: list[str] = []
    seen: set[str] = set()
    for item in entries:
        entry = entry_from_mapping(item)
        if entry["ref"] in seen:
            continue
        seen.add(entry["ref"])
        lines.append(json.dumps(entry, ensure_ascii=False, separators=(",", ":")))
    atomic_write_text(paths.ledger, "\n".join(lines) + ("\n" if lines else ""))
    return len(lines)
