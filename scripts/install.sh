#!/usr/bin/env bash
# Instalador canônico: preflight → backup → runtime → MCP real → recibo.
# O script nunca recebe chave, nunca toca em fonte externa e preserva o vault
# caso precise desfazer a integração Hermes.
set -Eeuo pipefail
umask 077

SOURCE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --source)
      SOURCE="${2:?--source requer um caminho}"
      shift 2
      ;;
    *)
      printf 'Argumento desconhecido: %s\n' "$1" >&2
      exit 2
      ;;
  esac
done

[[ -n "$SOURCE" && -f "$SOURCE/src/agent_context_kit/cli.py" ]] || {
  printf '%s\n' 'Instalação interrompida: fonte canônica do Kit não encontrada.' >&2
  exit 2
}
command -v python3 >/dev/null 2>&1 || {
  printf '%s\n' 'Instalação interrompida: python3 não encontrado.' >&2
  exit 2
}
command -v hermes >/dev/null 2>&1 || {
  printf '%s\n' 'Instalação interrompida: Hermes não encontrado.' >&2
  exit 2
}

python3 - <<'PY'
import sqlite3
import sys

if sys.version_info < (3, 10):
    raise SystemExit('Python 3.10+ é necessário.')
connection = sqlite3.connect(':memory:')
try:
    connection.execute('CREATE VIRTUAL TABLE probe USING fts5(text)')
except sqlite3.OperationalError as error:
    raise SystemExit('SQLite com FTS5 é necessário.') from error
finally:
    connection.close()
PY

KIT_HOME="${ACK_HOME:-$HOME/.context-kit}"
APP_ROOT="$KIT_HOME/app"
VAULT="$KIT_HOME/vault"
BIN_DIR="$KIT_HOME/bin"
WRAPPER="$BIN_DIR/agent-context-kit"
UNINSTALLER="$BIN_DIR/uninstall-agent-context-kit"
BACKUP_DIR="$KIT_HOME/backups/install-$(date -u +%Y%m%dT%H%M%SZ)"
SKILL_DIR="$HOME/.hermes/skills/agent-context-kit"
CONFIG_PATH="$(hermes config path)"
STAGE_ROOT=""
CONFIG_EXISTED=0
APP_BACKUP=""
WRAPPER_BACKUP=""
UNINSTALLER_BACKUP=""
SKILL_BACKUP=""
SUCCESS=0

mkdir -p "$KIT_HOME" "$BIN_DIR" "$KIT_HOME/backups" "$BACKUP_DIR"
chmod 700 "$KIT_HOME" "$BIN_DIR" "$KIT_HOME/backups" "$BACKUP_DIR"

rollback() {
  local status="$1"
  trap - ERR EXIT
  if [[ "$SUCCESS" -ne 1 ]]; then
    printf '%s\n' 'Instalação falhou; restaurando a integração Hermes anterior.' >&2
    if [[ "$CONFIG_EXISTED" -eq 1 && -f "$BACKUP_DIR/hermes-config.yaml" ]]; then
      cp -p "$BACKUP_DIR/hermes-config.yaml" "$CONFIG_PATH"
    elif [[ -f "$CONFIG_PATH" ]]; then
      mv "$CONFIG_PATH" "$BACKUP_DIR/failed-hermes-config.yaml"
    fi
    if [[ -d "$APP_ROOT" ]]; then mv "$APP_ROOT" "$BACKUP_DIR/failed-app"; fi
    if [[ -n "$APP_BACKUP" && -d "$APP_BACKUP" ]]; then mv "$APP_BACKUP" "$APP_ROOT"; fi
    if [[ -f "$WRAPPER" ]]; then mv "$WRAPPER" "$BACKUP_DIR/failed-wrapper"; fi
    if [[ -n "$WRAPPER_BACKUP" && -f "$WRAPPER_BACKUP" ]]; then mv "$WRAPPER_BACKUP" "$WRAPPER"; fi
    if [[ -f "$UNINSTALLER" ]]; then mv "$UNINSTALLER" "$BACKUP_DIR/failed-uninstaller"; fi
    if [[ -n "$UNINSTALLER_BACKUP" && -f "$UNINSTALLER_BACKUP" ]]; then mv "$UNINSTALLER_BACKUP" "$UNINSTALLER"; fi
    if [[ -d "$SKILL_DIR" ]]; then mv "$SKILL_DIR" "$BACKUP_DIR/failed-skill"; fi
    if [[ -n "$SKILL_BACKUP" && -d "$SKILL_BACKUP" ]]; then mv "$SKILL_BACKUP" "$SKILL_DIR"; fi
  fi
  if [[ -n "$STAGE_ROOT" && -d "$STAGE_ROOT" ]]; then rm -rf "$STAGE_ROOT"; fi
  exit "$status"
}
trap 'rollback $?' ERR
trap 'rollback $?' EXIT

if [[ -f "$CONFIG_PATH" ]]; then
  CONFIG_EXISTED=1
  cp -p "$CONFIG_PATH" "$BACKUP_DIR/hermes-config.yaml"
  chmod 600 "$BACKUP_DIR/hermes-config.yaml"
fi

STAGE_ROOT="$(mktemp -d "$KIT_HOME/.stage.XXXXXX")"
mkdir -p "$STAGE_ROOT/src"
cp -a "$SOURCE/src/agent_context_kit" "$STAGE_ROOT/src/agent_context_kit"
cp "$SOURCE/VERSION" "$STAGE_ROOT/VERSION"
chmod -R go-rwx "$STAGE_ROOT"

if [[ -d "$APP_ROOT" ]]; then
  APP_BACKUP="$BACKUP_DIR/previous-app"
  mv "$APP_ROOT" "$APP_BACKUP"
fi
mv "$STAGE_ROOT" "$APP_ROOT"
STAGE_ROOT=""

if [[ -f "$WRAPPER" ]]; then
  WRAPPER_BACKUP="$BACKUP_DIR/previous-wrapper"
  mv "$WRAPPER" "$WRAPPER_BACKUP"
fi
cp "$SOURCE/scripts/agent-context-kit" "$WRAPPER"
chmod 700 "$WRAPPER"

if [[ -f "$UNINSTALLER" ]]; then
  UNINSTALLER_BACKUP="$BACKUP_DIR/previous-uninstaller"
  mv "$UNINSTALLER" "$UNINSTALLER_BACKUP"
fi
cp "$SOURCE/scripts/uninstall.sh" "$UNINSTALLER"
chmod 700 "$UNINSTALLER"

if [[ -d "$SKILL_DIR" ]]; then
  SKILL_BACKUP="$BACKUP_DIR/previous-skill"
  mv "$SKILL_DIR" "$SKILL_BACKUP"
fi
mkdir -p "$SKILL_DIR"
cp "$SOURCE/integrations/hermes/skills/agent-context-kit/SKILL.md" "$SKILL_DIR/SKILL.md"
chmod 700 "$SKILL_DIR"
chmod 600 "$SKILL_DIR/SKILL.md"

"$WRAPPER" --vault "$VAULT" init >/dev/null
"$WRAPPER" --vault "$VAULT" seed-demo >/dev/null

# `mcp add` descobre tools no processo que Hermes realmente executa. Em
# reinstalação, o primeiro "y" confirma overwrite; em instalação nova, confirma
# as três tools. O backup de config torna a mudança reversível.
printf 'y\n\n' | hermes mcp add agent-context-kit --command "$WRAPPER" --args --vault "$VAULT" mcp >/dev/null
hermes mcp test agent-context-kit >/dev/null
"$WRAPPER" --vault "$VAULT" doctor --runtime-wrapper "$WRAPPER" >/dev/null

SUCCESS=1
trap - ERR EXIT
printf '%s\n' 'Agent Context Kit instalado e validado: 3 tools MCP read-only, demo seed e Mapa de Contexto prontos.'
