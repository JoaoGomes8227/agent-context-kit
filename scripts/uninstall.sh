#!/usr/bin/env bash
# Remove a integração Hermes sem apagar vault, banco, raw ou recibos.
set -euo pipefail

if [[ "${1:-}" != "--yes" ]]; then
  printf '%s\n' 'Confirmação necessária: rode uninstall-agent-context-kit --yes.' >&2
  exit 2
fi

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
INSTALLED_HOME="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)"
if [[ -f "$INSTALLED_HOME/app/src/agent_context_kit/cli.py" ]]; then
  DEFAULT_HOME="$INSTALLED_HOME"
else
  DEFAULT_HOME="$HOME/.context-kit"
fi
KIT_HOME="${ACK_HOME:-$DEFAULT_HOME}"
BACKUP_DIR="$KIT_HOME/backups/uninstall-$(date -u +%Y%m%dT%H%M%SZ)"
SKILL_DIR="$HOME/.hermes/skills/agent-context-kit"
CONFIG_PATH="$(hermes config path)"

mkdir -p "$BACKUP_DIR"
chmod 700 "$KIT_HOME" "$KIT_HOME/backups" "$BACKUP_DIR"

if [[ -f "$CONFIG_PATH" ]]; then
  cp -p "$CONFIG_PATH" "$BACKUP_DIR/hermes-config.yaml"
  chmod 600 "$BACKUP_DIR/hermes-config.yaml"
fi

# O remove só altera a configuração Hermes; nenhum dado do vault é apagado.
printf '\n' | hermes mcp remove agent-context-kit >/dev/null || true

if [[ -d "$SKILL_DIR" ]]; then
  mv "$SKILL_DIR" "$BACKUP_DIR/agent-context-kit-skill"
fi

printf '%s\n' 'Integração MCP removida. Seus dados privados continuam preservados no vault.'
