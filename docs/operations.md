# Operação

## Comandos seguros

Todos os comandos abaixo retornam JSON sem raw, transcript, inbox absoluta ou API key.

```bash
~/.context-kit/bin/agent-context-kit status
~/.context-kit/bin/agent-context-kit doctor --runtime-wrapper ~/.context-kit/bin/agent-context-kit
~/.context-kit/bin/agent-context-kit sync --source files
~/.context-kit/bin/agent-context-kit sync --source fathom
~/.context-kit/bin/agent-context-kit rebuild-ledger
hermes mcp test agent-context-kit
```

## Rotina normal

Não existe cron, daemon ou watcher no v0.1. O MCP tenta uma sincronização lazy no boot e antes de uma busca após cache de 60 segundos. Isso evita infraestrutura invisível e faz uma reunião nova aparecer na próxima pergunta útil.

## Entenda `status`

`status` traz somente:

- versão;
- se `files`/Fathom estão habilitados;
- contagem por fonte e primeira/última captura;
- total do Ledger;
- últimos recibos com operação, status, contagem e código seguro de falha.

Ele não mostra conteúdo, arquivo, caminho raw, cursor, ID de fornecedor ou segredo. “No change” significa que o conector rodou e nada novo entrou; uma falha tem `error_code` separado.

## Recibos

Cada `sync`, seed, rebuild, connect/desconnect grava um JSON local em `~/.context-kit/vault/receipts/`. O recibo é prova operacional, não evidência de trabalho: contém fonte, instante, versão de schema, adicionados, deduplicados, ignorados e cursor avançado — nunca payload.

## Reparar Ledger

O Ledger é projeção reconstruível do SQLite. Se o `doctor` ou uma auditoria indicar divergência:

```bash
~/.context-kit/bin/agent-context-kit rebuild-ledger
```

Isso não chama fonte externa nem modifica evidência raw. Reconstrói somente as seis colunas compactas a partir do SQLite local.

## Remover explicitamente uma fonte

Primeiro desconecte Fathom se aplicável:

```bash
~/.context-kit/bin/agent-context-kit disconnect-fathom
```

Depois remova a evidência daquela fonte somente se essa for a intenção:

```bash
~/.context-kit/bin/agent-context-kit purge-source --source fathom --yes-delete-source
```

O comando apaga itens normalizados, FTS e raw da fonte e reconstrói o Ledger sem ela. Não há purge implícito no uninstall.

## Backup

O Kit não faz backup automático. Se quiser durabilidade extra, pare o acesso ao vault, faça backup **criptografado** de `~/.context-kit/vault` para destino que você controla e valide restauração. Não use sync de cloud por default para raw de reuniões.

## Atualização

Reexecutar um instalador de versão revisada cria backup de app, wrapper, skill e config Hermes antes de tocar no runtime. Depois valide:

```bash
~/.context-kit/bin/agent-context-kit doctor --runtime-wrapper ~/.context-kit/bin/agent-context-kit
hermes mcp test agent-context-kit
```

## Onde olhar sem vazar dado

1. `doctor` para pré-requisito/permissão/integridade;
2. `status` para cobertura e recibos;
3. `hermes mcp test agent-context-kit` para handshake e tools reais;
4. logs locais do Hermes para falha de transporte, sem copiar transcript ou chave em issue/chat.
