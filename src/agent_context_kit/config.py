"""Configuração privada do Kit — permissões 0600, sem saída de segredos."""
from __future__ import annotations

import hashlib
from typing import Any, cast

from .errors import NotConnectedError, ValidationError
from .paths import VaultPaths, atomic_write_json, normalize_inbox, read_json


CONFIG_VERSION = 1
DEFAULT_MAX_FILE_BYTES = 1_000_000


def _defaults(paths: VaultPaths) -> dict[str, Any]:
    return {
        "schema_version": CONFIG_VERSION,
        "files": {
            "inbox": str(paths.inbox_dir),
            "max_file_bytes": DEFAULT_MAX_FILE_BYTES,
        },
        "fathom": {"enabled": False},
    }


def load_config(paths: VaultPaths) -> dict[str, Any]:
    paths.ensure_layout()
    config = read_json(paths.config, _defaults(paths))
    if not isinstance(config, dict) or config.get("schema_version") != CONFIG_VERSION:
        raise ValidationError("A configuração local do Kit é incompatível.")
    files = config.get("files")
    if not isinstance(files, dict):
        raise ValidationError("A configuração de arquivos está inválida.")
    inbox = normalize_inbox(files.get("inbox") or paths.inbox_dir, vault_root=paths.root)
    files["inbox"] = str(inbox)
    limit = files.get("max_file_bytes", DEFAULT_MAX_FILE_BYTES)
    if not isinstance(limit, int) or not 1 <= limit <= 10_000_000:
        raise ValidationError("O limite da inbox está inválido.")
    files["max_file_bytes"] = limit
    fathom = config.get("fathom", {"enabled": False})
    if not isinstance(fathom, dict):
        raise ValidationError("A configuração Fathom está inválida.")
    config["fathom"] = fathom
    return config


def save_config(paths: VaultPaths, config: dict[str, Any]) -> None:
    if not isinstance(config, dict):
        raise ValidationError("Configuração inválida.")
    config["schema_version"] = CONFIG_VERSION
    atomic_write_json(paths.config, config)


def initialize_config(paths: VaultPaths, *, inbox: str | None = None) -> dict[str, Any]:
    paths.ensure_layout()
    config = _defaults(paths)
    if paths.config.exists():
        config = load_config(paths)
    if inbox:
        config["files"]["inbox"] = str(normalize_inbox(inbox, vault_root=paths.root))
    save_config(paths, config)
    return config


def connect_fathom(paths: VaultPaths, api_key: str) -> dict[str, Any]:
    """Armazena uma chave já validada com uma identidade local estável.

    O ``account_id`` é fingerprint não reversível da chave. Ele evita que uma
    reconexão com a mesma credencial quebre dedupe ou crie uma conta aleatória,
    sem expor a chave em status, recibos ou MCP.
    """
    key = str(api_key or "").strip()
    if not key or len(key) > 1024:
        raise ValidationError("A chave Fathom é inválida.")
    config = load_config(paths)
    config["fathom"] = {
        "enabled": True,
        "api_key": key,
        "account_id": "key-" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:16],
    }
    save_config(paths, config)
    return config


def disconnect_fathom(paths: VaultPaths) -> None:
    config = load_config(paths)
    config["fathom"] = {"enabled": False}
    save_config(paths, config)


def fathom_credentials(config: dict[str, Any]) -> tuple[str, str]:
    fathom = config.get("fathom")
    if not isinstance(fathom, dict) or not fathom.get("enabled"):
        raise NotConnectedError("Fathom ainda não está conectado.")
    key = fathom.get("api_key")
    account_id = fathom.get("account_id")
    if not isinstance(key, str) or not key or not isinstance(account_id, str) or not account_id:
        raise NotConnectedError("A conexão Fathom está incompleta. Conecte novamente.")
    return key, account_id


def safe_config_status(config: dict[str, Any]) -> dict[str, Any]:
    """Projeção que jamais inclui a chave, inbox absoluta ou outros segredos."""
    files = (
        cast(dict[str, Any], config.get("files"))
        if isinstance(config.get("files"), dict)
        else {}
    )
    fathom = (
        cast(dict[str, Any], config.get("fathom"))
        if isinstance(config.get("fathom"), dict)
        else {}
    )
    return {
        "schema_version": config.get("schema_version"),
        "files": {"enabled": True, "max_file_bytes": files.get("max_file_bytes")},
        "fathom": {
            "enabled": bool(fathom.get("enabled")),
            "credential_stored": bool(fathom.get("api_key")),
        },
    }
