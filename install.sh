#!/usr/bin/env bash
# Bootstrap de um comando. Em clone local, usa a árvore atual; por curl, baixa uma cópia limpa.
set -euo pipefail

REPO_URL="${ACK_REPO_URL:-https://github.com/okjpg/agent-context-kit.git}"
SELF_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ -f "$SELF_DIR/scripts/install.sh" ]]; then
  exec "$SELF_DIR/scripts/install.sh" --source "$SELF_DIR" "$@"
fi

command -v git >/dev/null 2>&1 || {
  printf '%s\n' 'Instalação interrompida: git é necessário para baixar o Kit.' >&2
  exit 1
}

TEMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/agent-context-kit.XXXXXX")"
cleanup() { rm -rf "$TEMP_ROOT"; }
trap cleanup EXIT

git clone --depth 1 "$REPO_URL" "$TEMP_ROOT/repo" >/dev/null
exec "$TEMP_ROOT/repo/scripts/install.sh" --source "$TEMP_ROOT/repo" "$@"
