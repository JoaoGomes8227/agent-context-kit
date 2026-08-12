#!/usr/bin/env python3
"""Smoke real: HOME temporário + Hermes real + MCP stdio sob ambiente filtrado."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, env=env, timeout=120)


def main() -> int:
    hermes = shutil.which("hermes")
    if not hermes:
        raise SystemExit("hermes_not_found")

    with tempfile.TemporaryDirectory(prefix="ack-install-") as temp:
        home = Path(temp) / "home"
        home.mkdir()
        kit_home = home / ".context-kit"
        path = ":".join(dict.fromkeys([str(Path(hermes).parent), "/usr/local/bin", "/usr/bin", "/bin"]))
        env = dict(os.environ)
        env.update({
            "HOME": str(home),
            "ACK_HOME": str(kit_home),
            "PATH": path,
            "PYTHONDONTWRITEBYTECODE": "1",
        })
        for key in list(env):
            if key.startswith("HERMES_"):
                env.pop(key)

        installed = run(["bash", "scripts/install.sh", "--source", str(ROOT)], env)
        if installed.returncode != 0:
            raise SystemExit("install_failed\n" + installed.stdout + "\n" + installed.stderr)

        wrapper = kit_home / "bin" / "agent-context-kit"
        status = run([str(wrapper), "status"], env)
        if status.returncode != 0:
            raise SystemExit("status_failed\n" + status.stdout + "\n" + status.stderr)
        status_body = json.loads(status.stdout)
        if status_body["items"] < 2:
            raise SystemExit("demo_seed_missing")

        tested = run(["hermes", "mcp", "test", "agent-context-kit"], env)
        observed = tested.stdout + tested.stderr
        if tested.returncode != 0 or "Connected" not in observed or "Tools discovered: 3" not in observed:
            raise SystemExit("mcp_test_failed\n" + observed)

        doctor = run([str(wrapper), "doctor", "--runtime-wrapper", str(wrapper)], env)
        if doctor.returncode != 0 or json.loads(doctor.stdout).get("status") != "ok":
            raise SystemExit("doctor_failed\n" + doctor.stdout + "\n" + doctor.stderr)

        # MCP stdio recebe somente o baseline seguro do Hermes. Esta busca real
        # prova que o wrapper não depende de ACK_HOME/PYTHONPATH do shell pai.
        filtered_env = {
            "PATH": "/usr/bin:/bin",
            "HOME": str(home),
            "USER": "student",
            "SHELL": "/bin/bash",
            "LANG": "C.UTF-8",
        }
        process = subprocess.Popen(
            [str(wrapper), "--vault", str(kit_home / "vault"), "mcp"],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=filtered_env,
        )
        assert process.stdin is not None and process.stdout is not None
        try:
            process.stdin.write(json.dumps({
                "jsonrpc": "2.0", "id": 1, "method": "initialize",
                "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "smoke", "version": "1"}},
            }) + "\n")
            process.stdin.write(json.dumps({
                "jsonrpc": "2.0", "id": 2, "method": "tools/call",
                "params": {"name": "search_context", "arguments": {"query": "proposta revisada", "since": "30d"}},
            }) + "\n")
            process.stdin.flush()
            initialized = json.loads(process.stdout.readline())
            searched = json.loads(process.stdout.readline())
            if initialized["result"]["protocolVersion"] != "2025-11-25":
                raise SystemExit("mcp_protocol_version_failed")
            search_body = json.loads(searched["result"]["content"][0]["text"])
            if not search_body["results"]:
                raise SystemExit("filtered_env_search_failed")
        finally:
            if not process.stdin.closed:
                process.stdin.close()
            process.wait(timeout=10)
            stderr = process.stderr.read() if process.stderr else ""
            if process.stdout and not process.stdout.closed:
                process.stdout.close()
            if process.stderr and not process.stderr.closed:
                process.stderr.close()
            if process.returncode:
                raise SystemExit("filtered_env_mcp_failed\n" + stderr)

        uninstalled = run([str(kit_home / "bin" / "uninstall-agent-context-kit"), "--yes"], env)
        if uninstalled.returncode != 0:
            raise SystemExit("uninstall_failed\n" + uninstalled.stdout + "\n" + uninstalled.stderr)
        vault = kit_home / "vault"
        config = home / ".hermes" / "config.yaml"
        if not vault.is_dir() or not (vault / "context.sqlite3").is_file():
            raise SystemExit("vault_was_deleted")
        if config.exists() and "agent-context-kit" in config.read_text(encoding="utf-8"):
            raise SystemExit("mcp_was_not_removed")

        print(json.dumps({
            "status": "ok",
            "installer": "clean_home",
            "mcp_tools": 3,
            "demo_items": status_body["items"],
            "filtered_env_search": True,
            "uninstall_preserved_vault": True,
        }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
