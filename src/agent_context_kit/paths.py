"""Filesystem privado, atômico e contido no vault do Agent Context Kit."""
from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import stat
import tempfile
from typing import Any

from .errors import ValidationError

DIR_MODE = 0o700
FILE_MODE = 0o600
VAULT_MARKER = ".agent-context-kit-vault"


def _chmod(path: Path, mode: int) -> None:
    try:
        os.chmod(path, mode)
    except OSError:
        # Filesystems sem chmod ainda podem funcionar; doctor sinaliza o desvio.
        pass


def ensure_private_dir(path: Path) -> Path:
    """Cria/corrige um diretório privado sem seguir um leaf symlink."""
    if path.exists() and path.is_symlink():
        raise ValidationError("Um diretório privado do Kit não pode ser symlink.")
    path.mkdir(parents=True, exist_ok=True, mode=DIR_MODE)
    _chmod(path, DIR_MODE)
    return path


def ensure_private_file(path: Path) -> Path:
    """Impede que config/raw/estado sejam lidos por meio de um symlink."""
    if path.exists() and path.is_symlink():
        raise ValidationError("Um arquivo privado do Kit não pode ser symlink.")
    if path.exists():
        _chmod(path, FILE_MODE)
    return path


def atomic_write_bytes(path: Path, data: bytes, *, mode: int = FILE_MODE) -> None:
    ensure_private_dir(path.parent)
    ensure_private_file(path)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        _chmod(Path(temporary_name), mode)
        os.replace(temporary_name, path)
        _chmod(path, mode)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)


def atomic_write_text(path: Path, text: str, *, mode: int = FILE_MODE) -> None:
    atomic_write_bytes(path, text.encode("utf-8"), mode=mode)


def atomic_write_json(path: Path, data: Any, *, mode: int = FILE_MODE) -> None:
    encoded = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write_text(path, encoded, mode=mode)


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    ensure_private_file(path)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError("Um arquivo local de estado está inválido.") from exc


def is_private_mode(path: Path, expected: int) -> bool:
    try:
        return stat.S_IMODE(path.stat().st_mode) == expected
    except OSError:
        return False


def normalize_vault_root(value: str | Path | None) -> Path:
    root = Path(value or "~/.context-kit/vault").expanduser()
    if root == Path("/") or root == Path.home():
        raise ValidationError("O vault não pode ser a raiz do sistema ou sua HOME.")
    if root.exists() and root.is_symlink():
        raise ValidationError("O diretório do vault não pode ser um symlink.")
    return root.resolve(strict=False)


def normalize_inbox(value: str | Path, *, vault_root: Path) -> Path:
    candidate = Path(value).expanduser()
    if candidate == Path("/") or candidate == Path.home():
        raise ValidationError("A inbox não pode ser a raiz do sistema ou sua HOME.")
    if candidate.exists() and candidate.is_symlink():
        raise ValidationError("A inbox não pode ser um symlink.")
    ensure_private_dir(candidate)
    resolved = candidate.resolve(strict=True)
    if resolved == Path("/") or resolved == Path.home().resolve():
        raise ValidationError("Inbox insegura.")
    return resolved


@dataclass(frozen=True)
class VaultPaths:
    root: Path

    @classmethod
    def from_value(cls, value: str | Path | None = None) -> "VaultPaths":
        return cls(normalize_vault_root(value))

    @property
    def db(self) -> Path:
        return self.root / "context.sqlite3"

    @property
    def raw_dir(self) -> Path:
        return self.root / "raw"

    @property
    def state_dir(self) -> Path:
        return self.root / "state"

    @property
    def receipts_dir(self) -> Path:
        return self.root / "receipts"

    @property
    def backups_dir(self) -> Path:
        return self.root / "backups"

    @property
    def inbox_dir(self) -> Path:
        return self.root / "inbox"

    @property
    def ledger(self) -> Path:
        return self.root / "context-ledger.jsonl"

    @property
    def config(self) -> Path:
        return self.root / "config.json"

    @property
    def marker(self) -> Path:
        return self.root / VAULT_MARKER

    @property
    def kit_home(self) -> Path:
        return self.root.parent

    @property
    def context_map(self) -> Path:
        return self.kit_home / "MAPA-DE-CONTEXTO.md"

    def ensure_layout(self) -> None:
        ensure_private_dir(self.kit_home)
        ensure_private_dir(self.root)
        for directory in (
            self.raw_dir,
            self.state_dir,
            self.receipts_dir,
            self.backups_dir,
            self.inbox_dir,
        ):
            ensure_private_dir(directory)
        if not self.marker.exists():
            atomic_write_text(self.marker, "Agent Context Kit vault — private runtime data.\n")
        ensure_private_file(self.marker)

    def raw_path_for(self, source: str, item_id: str) -> Path:
        source_dir = ensure_private_dir(self.raw_dir / source)
        return source_dir / f"{item_id}.json"
