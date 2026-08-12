"""CLI operacional do Agent Context Kit.

A CLI administra somente o vault local. A interface que o agente recebe é o MCP
read-only; esta separação impede que uma conversa obtenha SQL, exportação,
credenciais ou comandos de manutenção por acidente.
"""
from __future__ import annotations

import argparse
import getpass
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
from typing import Any

from . import __version__
from .config import (
    connect_fathom,
    disconnect_fathom,
    initialize_config,
    load_config,
    safe_config_status,
)
from .connectors.fathom import probe_fathom, sync_fathom
from .connectors.files import sync_files
from .context_map import write_context_map
from .errors import ContextKitError, ValidationError, safe_error_code
from .ledger import count_entries
from .mcp_server import run_stdio
from .models import ContextItem, now_iso
from .paths import DIR_MODE, FILE_MODE, VaultPaths, atomic_write_text, is_private_mode
from .receipts import latest_receipts, write_receipt
from .store import ContextStore
from .sync import lazy_sync


def _paths(args: argparse.Namespace) -> VaultPaths:
    return VaultPaths.from_value(getattr(args, "vault", None))


def _emit(payload: dict[str, Any], *, code: int = 0) -> int:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return code


def _safe_failure(error: Exception) -> int:
    message = (
        error.public_message
        if isinstance(error, ContextKitError)
        else "O Kit não conseguiu concluir esta operação."
    )
    return _emit(
        {"status": "error", "error_code": safe_error_code(error), "message": message},
        code=2,
    )


def command_version(_args: argparse.Namespace) -> int:
    return _emit({"version": __version__})


def command_init(args: argparse.Namespace) -> int:
    paths = _paths(args)
    config = initialize_config(paths, inbox=args.inbox)
    ContextStore(paths).initialize()
    write_context_map(paths)
    return _emit(
        {
            "status": "ok",
            "operation": "init",
            "config": safe_config_status(config),
            "context_map_created": paths.context_map.exists(),
        }
    )


def command_seed_demo(args: argparse.Namespace) -> int:
    """Cria duas provas estritamente sintéticas: arquivo e reunião."""
    paths = _paths(args)
    config = initialize_config(paths, inbox=args.inbox)
    store = ContextStore(paths)
    store.initialize()
    write_context_map(paths)

    inbox = Path(config["files"]["inbox"])
    demo_file = inbox / "demo-promessa-reuniao.md"
    if not demo_file.exists():
        atomic_write_text(
            demo_file,
            "# Reunião de demonstração\n\n"
            "Eu prometi enviar a proposta revisada até sexta-feira.\n",
        )
    file_report = sync_files(paths, store)

    demo_meeting = ContextItem(
        source="fathom",
        source_item_id="demo-meeting-001",
        account="demo",
        # A demo deve cair na janela padrão de uma instalação recém-criada.
        occurred_at=now_iso(),
        text=(
            "Reunião sintética de demonstração. A pessoa responsável prometeu "
            "enviar a proposta revisada até sexta-feira."
        ),
        title="Demo — reunião com promessa",
        thread_id=None,
        provenance="demo:fathom:demo-meeting-001",
        who="Fathom: Demo — reunião com promessa",
        who_kind="ferramenta",
        raw={"synthetic": True, "fixture": "demo-meeting-001"},
    )
    meeting_result = store.ingest(demo_meeting)
    write_receipt(
        paths,
        operation="seed-demo",
        status="ok",
        source="fathom",
        added=int(meeting_result.added),
        deduplicated=int(not meeting_result.added),
    )
    return _emit(
        {
            "status": "ok",
            "operation": "seed-demo",
            "files": file_report.public(),
            "meeting_added": meeting_result.added,
            "note": "Dados sintéticos; nenhuma chave ou fonte externa foi usada.",
        }
    )


def command_sync(args: argparse.Namespace) -> int:
    paths = _paths(args)
    initialize_config(paths)
    store = ContextStore(paths)
    if args.source == "files":
        report = sync_files(paths, store)
        return _emit({"status": "ok", "sync": report.public()})
    if args.source == "fathom":
        report = sync_fathom(paths, store)
        return _emit({"status": "ok", "sync": report.public()})
    return _emit({"status": "ok", "sync": lazy_sync(paths, store).public()})


def _read_fathom_key(args: argparse.Namespace) -> str:
    if args.api_key_stdin:
        return sys.stdin.read().strip()
    return getpass.getpass("Cole a API key do Fathom (não será exibida): ").strip()


def command_connect_fathom(args: argparse.Namespace) -> int:
    paths = _paths(args)
    initialize_config(paths)
    api_key = _read_fathom_key(args)
    # A prova read-only vem antes de qualquer escrita da credencial.
    proof = probe_fathom(api_key)
    connect_fathom(paths, api_key)
    report = sync_fathom(paths, ContextStore(paths))
    return _emit(
        {
            "status": "ok",
            "operation": "connect-fathom",
            "probe": proof,
            "sync": report.public(),
            "scope": (
                "Leitura de reuniões visíveis para a chave. "
                "O Kit nunca altera o Fathom."
            ),
        }
    )


def command_connect(args: argparse.Namespace) -> int:
    """Rota de UX extensível: `connect fathom` no v0.1."""
    if args.service != "fathom":  # argparse protege hoje; mantém contrato futuro.
        raise ValidationError("Esta ferramenta ainda não é suportada.")
    return command_connect_fathom(args)


def command_disconnect_fathom(args: argparse.Namespace) -> int:
    paths = _paths(args)
    initialize_config(paths)
    disconnect_fathom(paths)
    write_receipt(paths, operation="disconnect-fathom", status="ok", source="fathom")
    return _emit({"status": "ok", "operation": "disconnect-fathom"})


def command_rebuild_ledger(args: argparse.Namespace) -> int:
    paths = _paths(args)
    initialize_config(paths)
    count = ContextStore(paths).rebuild_ledger()
    write_receipt(paths, operation="rebuild-ledger", status="ok", added=count)
    return _emit({"status": "ok", "operation": "rebuild-ledger", "entries": count})


def command_status(args: argparse.Namespace) -> int:
    paths = _paths(args)
    config = initialize_config(paths)
    store = ContextStore(paths)
    return _emit(
        {
            "status": "ok",
            "version": __version__,
            "config": safe_config_status(config),
            "items": store.count(),
            "ledger_entries": count_entries(paths),
            "sources": store.source_summary(),
            "receipts": latest_receipts(paths),
            "raw_content_excluded": True,
        }
    )


def _fts_available() -> bool:
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE VIRTUAL TABLE probe USING fts5(text)")
        return True
    except sqlite3.OperationalError:
        return False
    finally:
        connection.close()


def _wrapper_matches(wrapper: str | None, paths: VaultPaths) -> bool | None:
    if not wrapper:
        return None
    candidate = Path(wrapper)
    if not candidate.is_file() or candidate.is_symlink():
        return False
    try:
        completed = subprocess.run(
            [str(candidate), "version"],
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
            env={
                "PATH": "/usr/bin:/bin",
                "HOME": str(Path.home()),
                "ACK_HOME": str(paths.kit_home),
            },
        )
        parsed = json.loads(completed.stdout)
        return completed.returncode == 0 and parsed.get("version") == __version__
    except (OSError, subprocess.SubprocessError, ValueError):
        return False


def command_doctor(args: argparse.Namespace) -> int:
    paths = _paths(args)
    config = initialize_config(paths)
    store = ContextStore(paths)
    write_context_map(paths)
    fathom_config = config.get("fathom")
    checks: dict[str, bool | str | None] = {
        "python_supported": sys.version_info >= (3, 10),
        "sqlite_fts5": _fts_available(),
        "sqlite_integrity": store.integrity(),
        "vault_dir_0700": is_private_mode(paths.root, DIR_MODE),
        "config_0600": is_private_mode(paths.config, FILE_MODE),
        "context_map_present": paths.context_map.is_file(),
        "runtime_wrapper_matches_canonical": _wrapper_matches(args.runtime_wrapper, paths),
        "fathom_enabled": (
            bool(fathom_config.get("enabled"))
            if isinstance(fathom_config, dict)
            else False
        ),
    }
    # Fathom é opcional: instalação saudável com somente `files` deve passar.
    required_check_names = {
        "python_supported",
        "sqlite_fts5",
        "sqlite_integrity",
        "vault_dir_0700",
        "config_0600",
        "context_map_present",
        "runtime_wrapper_matches_canonical",
    }
    healthy = all(checks[name] in {True, "ok", None} for name in required_check_names)
    return _emit(
        {
            "status": "ok" if healthy else "needs_attention",
            "checks": checks,
            "note": "Doctor não lê nem imprime conteúdo, paths de evidência ou credenciais.",
        },
        code=0 if healthy else 1,
    )


def command_purge_source(args: argparse.Namespace) -> int:
    if not args.yes_delete_source:
        return _emit(
            {
                "status": "confirmation_required",
                "message": "Use --yes-delete-source para remover explicitamente uma fonte do vault.",
            },
            code=2,
        )
    paths = _paths(args)
    removed = ContextStore(paths).purge_source(args.source)
    write_receipt(paths, operation="purge-source", status="ok", source=args.source)
    return _emit(
        {
            "status": "ok",
            "operation": "purge-source",
            "source": args.source,
            "removed": removed,
        }
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-context-kit")
    parser.add_argument("--vault", help="Vault privado; default: ~/.context-kit/vault")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("version")

    init = sub.add_parser("init")
    init.add_argument("--inbox", help="Inbox explícita para .md/.txt")

    seed = sub.add_parser("seed-demo")
    seed.add_argument("--inbox", help="Inbox explícita para .md/.txt")

    sync = sub.add_parser("sync")
    sync.add_argument("--source", choices=("all", "files", "fathom"), default="all")

    connect = sub.add_parser("connect")
    connect.add_argument("service", choices=("fathom",))
    connect.add_argument(
        "--api-key-stdin",
        action="store_true",
        help="Lê a chave por stdin; para automação segura.",
    )
    # Compatibilidade curta para quem adotou a instrução pré-release.
    connect_legacy = sub.add_parser("connect-fathom", help=argparse.SUPPRESS)
    connect_legacy.add_argument("--api-key-stdin", action="store_true", help=argparse.SUPPRESS)

    sub.add_parser("disconnect-fathom")
    sub.add_parser("rebuild-ledger")
    sub.add_parser("status")

    doctor = sub.add_parser("doctor")
    doctor.add_argument(
        "--runtime-wrapper",
        help="Wrapper que Hermes executa; compara a versão canônica.",
    )

    purge = sub.add_parser("purge-source")
    purge.add_argument("--source", required=True)
    purge.add_argument("--yes-delete-source", action="store_true")

    sub.add_parser("mcp")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "mcp":
        return run_stdio(args.vault)
    try:
        commands = {
            "version": command_version,
            "init": command_init,
            "seed-demo": command_seed_demo,
            "sync": command_sync,
            "connect": command_connect,
            "connect-fathom": command_connect_fathom,
            "disconnect-fathom": command_disconnect_fathom,
            "rebuild-ledger": command_rebuild_ledger,
            "status": command_status,
            "doctor": command_doctor,
            "purge-source": command_purge_source,
        }
        return commands[args.command](args)
    except Exception as error:
        return _safe_failure(error)


if __name__ == "__main__":
    raise SystemExit(main())
