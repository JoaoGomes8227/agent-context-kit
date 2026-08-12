"""Conector Fathom read-only: valida chave, puxa páginas e só avança cursor após commit."""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping
import urllib.error
import urllib.parse
import urllib.request

from ..config import fathom_credentials, load_config
from ..errors import ConnectorError, ValidationError
from ..models import ContextItem, now_iso
from ..paths import VaultPaths, atomic_write_json, read_json
from ..receipts import write_receipt
from ..store import ContextStore
from .files import SyncReport

API_BASE = "https://api.fathom.ai/external/v1"
STATE_VERSION = 1
MAX_PAGES_PER_SYNC = 5


def _request_json(api_key: str, path: str, params: Mapping[str, str] | None = None) -> dict[str, Any]:
    query = urllib.parse.urlencode(params or {})
    url = API_BASE + path + (f"?{query}" if query else "")
    request = urllib.request.Request(
        url,
        headers={"X-Api-Key": api_key, "Accept": "application/json"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            raise ConnectorError("invalid_credentials", "A chave Fathom foi recusada.") from exc
        if exc.code == 429:
            raise ConnectorError("rate_limited", "O Fathom pediu uma pausa antes da próxima leitura.") from exc
        raise ConnectorError("upstream_error", "O Fathom não respondeu como esperado.") from exc
    except urllib.error.URLError as exc:
        raise ConnectorError("network_error", "Não foi possível alcançar o Fathom agora.") from exc
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ConnectorError("invalid_upstream_response", "O Fathom devolveu uma resposta inválida.") from exc
    if not isinstance(payload, dict):
        raise ConnectorError("invalid_upstream_response", "O Fathom devolveu uma resposta inválida.")
    return payload


def list_meetings_page(api_key: str, *, cursor: str | None, include_transcript: bool) -> dict[str, Any]:
    params = {
        "include_transcript": "true" if include_transcript else "false",
        "include_summary": "true" if include_transcript else "false",
        "include_action_items": "true" if include_transcript else "false",
    }
    if cursor:
        params["cursor"] = cursor
    page = _request_json(api_key, "/meetings", params)
    if not isinstance(page.get("items") or [], list):
        raise ConnectorError("invalid_upstream_response", "O Fathom não devolveu uma lista de reuniões válida.")
    return page


def probe_fathom(api_key: str) -> dict[str, int]:
    """Prova read-only mínima; não persiste nem imprime nomes ou conteúdo."""
    page = list_meetings_page(api_key, cursor=None, include_transcript=False)
    return {"meetings_visible": len(page.get("items") or [])}


def _transcript_text(meeting: Mapping[str, Any]) -> str:
    transcript = meeting.get("transcript")
    if isinstance(transcript, str):
        return transcript.strip()
    if isinstance(transcript, list):
        parts: list[str] = []
        for entry in transcript:
            if isinstance(entry, Mapping):
                value = entry.get("text") or entry.get("content") or ""
            else:
                value = str(entry)
            if value:
                parts.append(str(value).strip())
        if parts:
            return "\n".join(parts)
    if isinstance(transcript, Mapping):
        nested = transcript.get("text") or transcript.get("content") or transcript.get("segments")
        if isinstance(nested, str):
            return nested.strip()
        if isinstance(nested, list):
            return "\n".join(
                str(part.get("text") if isinstance(part, Mapping) else part).strip()
                for part in nested
                if part
            )
    for fallback_key in ("summary", "summary_text", "action_items"):
        value = meeting.get(fallback_key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, list):
            joined = "\n".join(str(x) for x in value if x)
            if joined.strip():
                return joined.strip()
    return ""


def _meeting_item(meeting: Mapping[str, Any], *, account_id: str) -> ContextItem | None:
    external_id = meeting.get("recording_id") or meeting.get("id") or meeting.get("meeting_id")
    if external_id is None:
        return None
    title = str(meeting.get("name") or meeting.get("title") or "Reunião Fathom").strip()
    text = _transcript_text(meeting) or title
    occurred_at = None
    for key in ("recorded_at", "recording_started_at", "created_at", "start_time", "date"):
        value = meeting.get(key)
        if isinstance(value, str) and value.strip():
            occurred_at = value
            break
    return ContextItem(
        source="fathom",
        source_item_id=str(external_id),
        account=account_id,
        occurred_at=occurred_at,
        text=text,
        title=title,
        thread_id=str(meeting.get("thread_id") or "") or None,
        provenance=f"fathom:meeting:{external_id}",
        who=f"Fathom: {title}",
        who_kind="ferramenta",
        raw={"meeting": dict(meeting)},
    )


def _state_path(paths: VaultPaths) -> Path:
    return paths.state_dir / "fathom.json"


def _load_state(paths: VaultPaths) -> dict[str, Any]:
    state = read_json(_state_path(paths), {"schema_version": STATE_VERSION, "cursor": None})
    if not isinstance(state, dict) or state.get("schema_version") != STATE_VERSION:
        raise ValidationError("O cursor Fathom local está inválido.")
    cursor = state.get("cursor")
    if cursor is not None and not isinstance(cursor, str):
        raise ValidationError("O cursor Fathom local está inválido.")
    return state


def _save_state(paths: VaultPaths, *, cursor: str | None) -> None:
    atomic_write_json(
        _state_path(paths),
        {"schema_version": STATE_VERSION, "cursor": cursor, "updated_at": now_iso()},
    )


def sync_fathom(paths: VaultPaths, store: ContextStore | None = None) -> SyncReport:
    """Faz pull limitado. Cursor só muda depois de raw + SQLite + Ledger."""
    config = load_config(paths)
    api_key, account_id = fathom_credentials(config)
    store = store or ContextStore(paths)
    state = _load_state(paths)
    cursor = state.get("cursor")
    added = deduplicated = ignored = 0
    cursor_advanced = False
    pages_seen = 0

    for _ in range(MAX_PAGES_PER_SYNC):
        page = list_meetings_page(api_key, cursor=cursor, include_transcript=True)
        items = page.get("items") or []
        assert isinstance(items, list)
        for meeting in items:
            if not isinstance(meeting, Mapping):
                ignored += 1
                continue
            item = _meeting_item(meeting, account_id=account_id)
            if item is None:
                ignored += 1
                continue
            result = store.ingest(item)
            if result.added:
                added += 1
            else:
                deduplicated += 1
        next_cursor_raw = page.get("next_cursor")
        next_cursor = str(next_cursor_raw) if next_cursor_raw else None
        # O commit de todos os itens desta página terminou; agora pode avançar.
        _save_state(paths, cursor=next_cursor)
        cursor_advanced = cursor_advanced or next_cursor != cursor
        cursor = next_cursor
        pages_seen += 1
        if not cursor or not items:
            break

    status = "ok" if added else "no_change"
    report = SyncReport("fathom", status, added, deduplicated, ignored, cursor_advanced)
    write_receipt(
        paths,
        operation="sync-fathom",
        status=status,
        source="fathom",
        added=added,
        deduplicated=deduplicated,
        ignored=ignored,
        cursor_advanced=cursor_advanced,
        window=f"pages:{pages_seen}",
    )
    return report
