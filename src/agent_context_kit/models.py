"""Contrato mínimo, validações e limites do Agent Context Kit."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
import hashlib
import json
import re
from typing import Any, Mapping

from .errors import ValidationError

SOURCE_RE = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")
ITEM_ID_RE = re.compile(r"^ctx_[0-9a-f]{64}$")
WHO_KINDS = frozenset({"pessoa", "ferramenta", "transacional", "desconhecido"})
MAX_TEXT_CHARS = 200_000
MAX_TITLE_CHARS = 500
MAX_PROVENANCE_CHARS = 1_000
MAX_EXCERPT_CHARS = 200
MAX_QUERY_CHARS = 200
MAX_LIMIT = 10
MAX_SINCE_DAYS = 90


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def normalize_timestamp(value: str | None, *, fallback: str | None = None) -> str:
    """Normaliza timestamps para UTC ISO-8601; rejeita formatos ambíguos."""
    raw = value or fallback or now_iso()
    if not isinstance(raw, str) or not raw.strip():
        raise ValidationError("Timestamp ausente ou inválido.")
    try:
        parsed = datetime.fromisoformat(raw.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError("Timestamp inválido; use ISO-8601.") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_since(value: str | None, *, default_days: int) -> str:
    """Converte uma janela curta em timestamp UTC para consultas parametrizadas."""
    if value is None or not str(value).strip():
        return (datetime.now(timezone.utc) - timedelta(days=default_days)).isoformat(
            timespec="seconds"
        ).replace("+00:00", "Z")
    raw = str(value).strip()
    match = re.fullmatch(r"(\d{1,3})d", raw)
    if match:
        days = int(match.group(1))
        if not 1 <= days <= MAX_SINCE_DAYS:
            raise ValidationError(f"A janela deve ficar entre 1d e {MAX_SINCE_DAYS}d.")
        return (datetime.now(timezone.utc) - timedelta(days=days)).isoformat(
            timespec="seconds"
        ).replace("+00:00", "Z")
    return normalize_timestamp(raw)


def validate_source(value: str | None) -> str | None:
    if value is None:
        return None
    source = str(value).strip().lower()
    if not SOURCE_RE.fullmatch(source):
        raise ValidationError("Fonte inválida.")
    return source


def safe_excerpt(text: str, *, limit: int = MAX_EXCERPT_CHARS) -> str:
    normalized = re.sub(r"\s+", " ", text or "").strip()
    return normalized[:limit] + ("…" if len(normalized) > limit else "")


def truncate(text: str, limit: int) -> tuple[str, bool]:
    if len(text) <= limit:
        return text, False
    return text[:limit] + "…", True


def fts_query(query: str) -> str:
    """Produz uma expressão FTS literal, sem operadores fornecidos pelo usuário."""
    if not isinstance(query, str) or not query.strip() or len(query) > MAX_QUERY_CHARS:
        raise ValidationError(f"A busca deve ter entre 1 e {MAX_QUERY_CHARS} caracteres.")
    terms = re.findall(r"[\wÀ-ÿ'-]+", query.lower(), flags=re.UNICODE)[:12]
    if not terms:
        raise ValidationError("A busca não contém termos pesquisáveis.")
    # Os termos vêm de regex fechada, mas mantemos a citação FTS para não aceitar sintaxe.
    return " AND ".join(f'"{term}"' for term in terms)


def stable_item_id(source: str, account: str | None, source_item_id: str) -> str:
    material = "\x00".join((source, account or "", source_item_id)).encode("utf-8")
    return "ctx_" + hashlib.sha256(material).hexdigest()


@dataclass(frozen=True)
class ContextItem:
    """Envelope rico da evidência. O Ledger guarda apenas sua projeção compacta."""

    source: str
    source_item_id: str
    account: str | None
    occurred_at: str | None
    text: str
    title: str | None
    thread_id: str | None
    provenance: str
    who: str = ""
    who_kind: str = "desconhecido"
    raw: Mapping[str, Any] | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        source = validate_source(self.source)
        if source is None:
            raise ValidationError("Fonte obrigatória.")
        object.__setattr__(self, "source", source)
        item_id = str(self.source_item_id or "").strip()
        if not item_id or len(item_id) > 512:
            raise ValidationError("Identificador de origem inválido.")
        object.__setattr__(self, "source_item_id", item_id)
        account = str(self.account or "").strip()
        if len(account) > 256:
            raise ValidationError("Conta inválida.")
        object.__setattr__(self, "account", account or None)
        text = str(self.text or "").strip()
        title = str(self.title or "").strip()
        if not text and not title:
            raise ValidationError("O item precisa de texto ou título.")
        if len(text) > MAX_TEXT_CHARS:
            raise ValidationError("O item excede o limite local de texto.")
        if len(title) > MAX_TITLE_CHARS:
            raise ValidationError("Título excede o limite permitido.")
        object.__setattr__(self, "text", text)
        object.__setattr__(self, "title", title or None)
        provenance = str(self.provenance or "").strip()
        if not provenance or len(provenance) > MAX_PROVENANCE_CHARS:
            raise ValidationError("Proveniência inválida.")
        object.__setattr__(self, "provenance", provenance)
        thread_id = str(self.thread_id or "").strip()
        if len(thread_id) > 512:
            raise ValidationError("Thread inválida.")
        object.__setattr__(self, "thread_id", thread_id or None)
        who = str(self.who or title or source).strip()
        if len(who) > 500:
            who = who[:500]
        object.__setattr__(self, "who", who)
        if self.who_kind not in WHO_KINDS:
            raise ValidationError("Classificação de autor inválida.")
        object.__setattr__(self, "occurred_at", normalize_timestamp(self.occurred_at))
        if self.raw is not None:
            try:
                json.dumps(self.raw, ensure_ascii=False)
            except (TypeError, ValueError) as exc:
                raise ValidationError("O payload bruto não é serializável.") from exc

    @property
    def item_id(self) -> str:
        return stable_item_id(self.source, self.account, self.source_item_id)

    @property
    def ref(self) -> str:
        return self.item_id

    def raw_document(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "captured_at": now_iso(),
            "item": {
                "id": self.item_id,
                "source": self.source,
                "source_item_id": self.source_item_id,
                "account": self.account,
                "occurred_at": self.occurred_at,
                "title": self.title,
                "thread_id": self.thread_id,
                "who": self.who,
                "who_kind": self.who_kind,
                "provenance": self.provenance,
                "text": self.text,
            },
            "raw": self.raw if self.raw is not None else {},
        }
