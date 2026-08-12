"""Orquestração lazy dos conectores locais; falhas externas não derrubam busca local."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .config import load_config
from .errors import ContextKitError, safe_error_code
from .paths import VaultPaths
from .store import ContextStore
from .connectors.files import SyncReport, sync_files
from .connectors.fathom import sync_fathom


@dataclass(frozen=True)
class SyncSummary:
    reports: tuple[SyncReport, ...]
    failures: tuple[dict[str, str], ...]

    def public(self) -> dict[str, Any]:
        return {
            "sources": [report.public() for report in self.reports],
            "failures": list(self.failures),
        }


def lazy_sync(paths: VaultPaths, store: ContextStore | None = None) -> SyncSummary:
    """Atualiza arquivos e, se conectado, Fathom; nenhum texto de erro é exposto."""
    store = store or ContextStore(paths)
    reports: list[SyncReport] = []
    failures: list[dict[str, str]] = []
    try:
        reports.append(sync_files(paths, store))
    except Exception as error:  # inbox pode conter erro local; busca ainda responde ao existente
        failures.append({"source": "files", "error_code": safe_error_code(error)})

    config = load_config(paths)
    fathom = config.get("fathom")
    if isinstance(fathom, dict) and fathom.get("enabled"):
        try:
            reports.append(sync_fathom(paths, store))
        except ContextKitError as error:
            failures.append({"source": "fathom", "error_code": error.code})
        except Exception as error:  # nunca passar corpo/resposta upstream ao agente
            failures.append({"source": "fathom", "error_code": safe_error_code(error)})
    return SyncSummary(tuple(reports), tuple(failures))
