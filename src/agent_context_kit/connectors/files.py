"""Conector `files`: somente .md/.txt dentro da inbox explícita do Kit."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
from pathlib import Path
from typing import Iterator

from ..config import load_config
from ..models import ContextItem
from ..paths import VaultPaths
from ..receipts import write_receipt
from ..store import ContextStore

SUPPORTED_SUFFIXES = frozenset({".md", ".txt"})


@dataclass(frozen=True)
class SyncReport:
    source: str
    status: str
    added: int = 0
    deduplicated: int = 0
    ignored: int = 0
    cursor_advanced: bool = False

    def public(self) -> dict[str, object]:
        return {
            "source": self.source,
            "status": self.status,
            "added": self.added,
            "deduplicated": self.deduplicated,
            "ignored": self.ignored,
            "cursor_advanced": self.cursor_advanced,
        }


def _iter_candidate_files(inbox: Path) -> Iterator[Path]:
    root = inbox.resolve(strict=True)
    for candidate in sorted(root.rglob("*")):
        # is_file() seguiria symlinks; rejeitar antes é a trava importante.
        if candidate.is_symlink() or not candidate.is_file():
            continue
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(root)
        except (OSError, ValueError):
            continue
        if resolved.suffix.lower() in SUPPORTED_SUFFIXES:
            yield resolved


def _item_from_file(path: Path, *, inbox: Path, max_bytes: int) -> ContextItem | None:
    try:
        details = path.stat()
    except OSError:
        return None
    if details.st_size < 1 or details.st_size > max_bytes:
        return None
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if "\x00" in text:
        return None
    try:
        relative = path.relative_to(inbox).as_posix()
    except ValueError:
        return None
    digest = hashlib.sha256(raw).hexdigest()
    occurred_at = datetime.fromtimestamp(details.st_mtime, tz=timezone.utc).isoformat(
        timespec="seconds"
    ).replace("+00:00", "Z")
    return ContextItem(
        source="files",
        source_item_id=f"{relative}:{digest}",
        account=None,
        occurred_at=occurred_at,
        text=text,
        title=path.stem,
        thread_id=None,
        provenance=f"files:{relative}",
        who=f"Arquivo: {relative}",
        who_kind="ferramenta",
        raw={"relative_path": relative, "sha256": digest, "bytes": len(raw)},
    )


def sync_files(paths: VaultPaths, store: ContextStore | None = None) -> SyncReport:
    """Indexa incrementalmente somente a inbox configurada e segura."""
    config = load_config(paths)
    inbox = Path(config["files"]["inbox"])
    max_bytes = int(config["files"]["max_file_bytes"])
    store = store or ContextStore(paths)
    added = deduplicated = ignored = 0
    for path in _iter_candidate_files(inbox):
        item = _item_from_file(path, inbox=inbox, max_bytes=max_bytes)
        if item is None:
            ignored += 1
            continue
        result = store.ingest(item)
        if result.added:
            added += 1
        else:
            deduplicated += 1
    status = "ok" if added else "no_change"
    report = SyncReport("files", status, added, deduplicated, ignored)
    write_receipt(
        paths,
        operation="sync-files",
        status=status,
        source="files",
        added=added,
        deduplicated=deduplicated,
        ignored=ignored,
        cursor_advanced=False,
    )
    return report
