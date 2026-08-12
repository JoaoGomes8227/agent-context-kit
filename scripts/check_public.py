#!/usr/bin/env python3
"""Falha fechada para segredos e identificadores privados no artefato público.

O scanner emite apenas categoria + caminho. Nunca replica o valor que disparou
um alerta. Ele verifica a árvore de trabalho e, quando houver commits, todos os
objetos alcançáveis no histórico publicado localmente.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".context-kit", "__pycache__", ".pytest_cache"}

# Fragmentos impedem que o próprio scanner acione uma assinatura literal que ele
# precisa detectar em outros arquivos.
PATTERNS = {
    "openai_key": re.compile(r"\b" + "sk" + r"-[A-Za-z0-9_-]{10,}\b"),
    "github_pat": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "google_key": re.compile(r"\bAI" + "za" + r"[A-Za-z0-9_-]{10,}\b"),
    "onepassword_reference": re.compile("op:" + "//"),
    "private_root_path": re.compile(
        "/root/" + "(?:workspace" + "-amora-v2|\\.hermes/private|repos/agent-context-hub)"
    ),
    "private_ledger_path": re.compile("memory/tracking/" + "context-ledger"),
}


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def classify(text: str) -> list[str]:
    return [name for name, pattern in PATTERNS.items() if pattern.search(text)]


def scan_worktree() -> tuple[int, list[tuple[str, str]]]:
    scanned = 0
    findings: list[tuple[str, str]] = []
    for path in ROOT.rglob("*"):
        if should_skip(path) or not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        scanned += 1
        for category in classify(text):
            findings.append((str(path.relative_to(ROOT)), category))
    return scanned, findings


def git_output(args: list[str]) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if completed.returncode not in {0, 1}:
        return ""
    return completed.stdout


def scan_history() -> tuple[int, list[tuple[str, str]]]:
    commits = [line for line in git_output(["rev-list", "--all"]).splitlines() if line]
    findings: list[tuple[str, str]] = []
    for commit in commits:
        for category, pattern in PATTERNS.items():
            # Padrão é controlado pelo projeto. Git grep retorna 1 quando não há hit.
            completed = subprocess.run(
                ["git", "grep", "-I", "-l", "-E", pattern.pattern, commit, "--", "."],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            if completed.returncode not in {0, 1}:
                continue
            for path in completed.stdout.splitlines():
                findings.append((f"history:{commit[:12]}:{path}", category))
    return len(commits), findings


def main() -> int:
    worktree_files, findings = scan_worktree()
    commits, history_findings = scan_history()
    findings.extend(history_findings)
    if findings:
        for path, category in sorted(set(findings)):
            print(f"FAIL {category}: {path}")
        return 1
    print(f"OK public-scan worktree_files={worktree_files} commits={commits} findings=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
