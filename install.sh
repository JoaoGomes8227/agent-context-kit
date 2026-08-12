#!/usr/bin/env bash
# Bootstrap de um comando. Em clone local, usa a árvore atual; por curl|bash, baixa uma cópia limpa.
set -euo pipefail

REPO_URL="${ACK_REPO_URL:-https://github.com/okjpg/agent-context-kit.git}"

# Quando o script é piped (`curl | bash`), não há arquivo local — BASH_SOURCE pode ficar vazio.
SOURCE_PATH="${BASH_SOURCE[0]:-}"
if [[ -n "$SOURCE_PATH" && -f "$SOURCE_PATH" ]]; then
  SELF_DIR="$(CDPATH= cd -- "$(dirname -- "$SOURCE_PATH")" && pwd)"
  if [[ -f "$SELF_DIR/scripts/install.sh" ]]; then
    exec "$SELF_DIR/scripts/install.sh" --source "$SELF_DIR" "$@"
  fi
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
