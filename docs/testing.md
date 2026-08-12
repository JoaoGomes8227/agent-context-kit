# Guia para quem vai testar

Este documento é o caminho curto para validar o Agent Context Kit v0.1 em uma VPS com Hermes, sem depender de conta Fathom e sem vazar dado privado.

## O que você está testando

O Kit responde a esta pergunta:

> Depois de instalar, uma sessão Hermes nova consegue achar contexto privado com fonte, data e limites — sem dump de memória e sem banco em nuvem?

Há dois níveis:

1. **Sem chave (obrigatório):** demo sintética + inbox de arquivos.
2. **Com Fathom (opcional):** API key real do tester; read-only.

## Pré-requisitos

- Linux com HOME gravável
- Hermes Agent instalado (`hermes` no `PATH`)
- Python 3.10+
- SQLite com FTS5
- `git` (o instalador de um comando clona o repo)

Não precisa de Docker, domínio, `pip`, venv, Supabase, webhook ou OAuth.

## Caminho A — instalação em um comando (recomendado)

```bash
curl -fsSL https://raw.githubusercontent.com/okjpg/agent-context-kit/main/install.sh | bash
```

Esperado no final:

```text
Agent Context Kit instalado e validado: 3 tools MCP read-only, demo seed e Mapa de Contexto prontos.
```

Se falhar, o instalador tenta restaurar a config Hermes anterior e **não apaga** um vault já existente. Backup em `~/.context-kit/backups/`.

## Caminho B — clone e instalação local

Útil se você já baixou o repo ou quer inspecionar o código antes:

```bash
git clone https://github.com/okjpg/agent-context-kit.git
cd agent-context-kit
bash install.sh
# equivalente explícito:
# bash scripts/install.sh --source "$PWD"
```

## Depois de instalar

### 1. Comprovantes no terminal

```bash
~/.context-kit/bin/agent-context-kit status
~/.context-kit/bin/agent-context-kit doctor --runtime-wrapper ~/.context-kit/bin/agent-context-kit
hermes mcp test agent-context-kit
hermes mcp list
```

Checklist mínimo:

| Check | Esperado |
|---|---|
| `status` | JSON com `items >= 2`, `raw_content_excluded: true` |
| `doctor` | `"status": "ok"` |
| `hermes mcp test` | conecta e descobre **exatamente 3** tools |
| `status` / `doctor` | **não** imprimem API key, transcript, path raw ou texto da evidência |

### 2. Primeira vitória no Hermes

Abra uma **nova sessão** Hermes (sessões antigas não recarregam MCP/skill sozinhas) e pergunte:

> O que eu prometi na reunião de demonstração? Cite a fonte.

A resposta deve apontar a demo sintética (reunião e/ou arquivo) com fonte/data/proveniência.
Não peça ao agente para abrir `~/.context-kit`, SQLite ou JSONL.

### 3. Inbox de arquivo real (ainda sem chave)

```bash
printf '%s\n' '# Nota de teste

Eu preciso enviar o resumo da mentoria até segunda-feira.' \
  > ~/.context-kit/vault/inbox/nota-teste.md

~/.context-kit/bin/agent-context-kit sync --source files
~/.context-kit/bin/agent-context-kit status
```

Na sessão Hermes:

> O que eu preciso enviar até segunda? Cite a fonte.

### 4. Fathom opcional

Só se você quiser testar reunião real **com a sua** API key:

```bash
~/.context-kit/bin/agent-context-kit connect fathom
```

A chave:

- é pedida sem eco;
- só é gravada depois do probe read-only;
- fica em `~/.context-kit/vault/config.json` com permissão `0600`;
- **nunca** deve ser colada em issue, chat de grupo ou print.

Para sair:

```bash
~/.context-kit/bin/agent-context-kit disconnect-fathom
```

Revogue também a key no painel do Fathom se ela era só para o teste.

## O que NÃO é bug do Kit

- Sessão Hermes aberta **antes** da instalação não vê as tools → abra outra.
- Arquivo fora da inbox não entra → a inbox default é `~/.context-kit/vault/inbox`.
- Só `.md`/`.txt` UTF-8 no v0.1.
- Sem cron/daemon: sync é lazy (no boot do MCP e antes de busca, com cache curta).
- `uninstall` **preserva** o vault de propósito.

## Como reportar problema (sem vazar dado)

Envie:

1. comando exato e exit code;
2. saída de `doctor` e `status` (já são seguros);
3. trecho de `hermes mcp test agent-context-kit` **sem** conteúdo de reunião;
4. SO, versão do Python (`python3 -V`) e se Hermes responde em terminal;
5. se usou Caminho A ou B.

**Não envie:**

- API key / token;
- transcript ou arquivo real;
- `config.json` completo;
- dump de SQLite/JSONL/raw;
- print do vault inteiro.

Modelo curto:

```text
Ambiente: Ubuntu … / Python 3.x / Hermes ok
Caminho: curl | bash   OU   clone + install.sh
Falhou em: install | doctor | mcp test | busca na sessão | fathom
Comando:
Saída segura (doctor/status/mcp test):
Esperado:
Observado:
```

## Desinstalar a integração (mantém seus dados)

```bash
~/.context-kit/bin/uninstall-agent-context-kit --yes
```

O vault permanece em `~/.context-kit/vault`. Só apague manualmente se tiver certeza e backup.

## Validação local do código (mantenedores / CI)

No clone:

```bash
PYTHONPATH=src python3 tests/run.py
python3 tests/install_smoke.py   # exige hermes no PATH
python3 scripts/check_public.py
```

## Links úteis

- [Instalação](installation.md)
- [Operação](operations.md)
- [Conectores](connectors.md)
- [Troubleshooting](troubleshooting.md)
- [Recibo de aceite](acceptance-receipt.md)
- [Segurança](security.md)
