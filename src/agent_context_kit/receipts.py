"""Recibos locais sem conteúdo privado para operação e diagnóstico."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import __version__
from .models import now_iso, validate_source
from .paths import VaultPaths, atomic_write_json


def write_receipt(
    paths: VaultPaths,
    *,
    operation: str,
    status: str,
    source: str | None = None,
    added: int = 0,
    deduplicated: int = 0,
    ignored: int = 0,
    error_code: str | None = None,
    cursor_advanced: bool | None = None,
    window: str | None = None,
) -> Path:
    """Escreve metadados operacionais, nunca payload, path raw ou chave."""
    timestamp = now_iso()
    safe_source = validate_source(source) if source else None
    document: dict[str, Any] = {
        "schema_version": 1,
        "kit_version": __version__,
        "timestamp": timestamp,
        "operation": operation,
        "status": status,
        "source": safe_source,
        "added": int(added),
        "deduplicated": int(deduplicated),
        "ignored": int(ignored),
    }
    if error_code:
        document["error_code"] = error_code
    if cursor_advanced is not None:
        document["cursor_advanced"] = bool(cursor_advanced)
    if window:
        document["window"] = window
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    destination = paths.receipts_dir / f"{stamp}-{operation}.json"
    atomic_write_json(destination, document)
    return destination


def latest_receipts(paths: VaultPaths, *, limit: int = 8) -> list[dict[str, Any]]:
    """Retorna somente metadados de recibos recentes, em ordem reversa."""
    if not paths.receipts_dir.exists():
        return []
    results: list[dict[str, Any]] = []
    for path in sorted(paths.receipts_dir.glob("*.json"), reverse=True)[:limit]:
        try:
            import json

            item = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(item, dict):
            results.append(item)
    return results
