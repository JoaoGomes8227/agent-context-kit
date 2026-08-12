# Arquitetura

## Limite do produto

O Kit não é uma memória, RAG genérico ou banco de dados do seu negócio. Ele é a fronteira privada entre fontes externas e um agente: captura evidência, mantém proveniência e devolve pequenas fatias consultáveis.

```text
files inbox ─┐
             ├─→ ContextItem → raw durável + SQLite/FTS5 → MCP stdio → Hermes
Fathom API ──┘                       │                         │
                                     └→ Context Ledger          └→ citação
                                        (6 campos, janela)          ↓
                                                                  síntese curada
                                                                  só sob pedido
```

## Camadas e contratos

| Camada | Responsabilidade | Não faz |
|---|---|---|
| Fonte | produz sinal externo | não dita permissões do agente |
| Conector | valida, normaliza, deduplica e persiste | não interpreta com LLM nem altera a fonte |
| Raw | conserva payload reprocessável no vault | não entra em Git ou segundo cérebro |
| SQLite/FTS5 | descobre e abre evidência por ID | não vira contexto inteiro do prompt |
| Context Ledger | responde “o que chegou, de quem e quando?” | não guarda o payload completo |
| MCP | entrega três leituras limitadas | não expõe SQL, shell, exportação ou escrita |
| Skill Hermes | força consulta e citação | não promove memória automaticamente |
| Segundo cérebro | guarda decisão/síntese aceita | não recebe raw por default |

## ContextItem

O envelope mínimo de evidência é:

```yaml
source: string
source_item_id: string
account: string | null
occurred_at: ISO-8601 UTC
text: string
title: string | null
thread_id: string | null
provenance: string
```

Campos locais para recuperação (`who`, `who_kind`) não alteram a fonte. O ID é determinístico: `sha256(source + account + source_item_id)`. Portanto, replay, restart e backfill são seguros.

## Context Ledger

O Ledger é JSONL append-only, reconstruível a partir do SQLite e deliberadamente pequeno:

| Campo | Função |
|---|---|
| `ts` | timestamp da evidência |
| `source` | produtor (`files`, `fathom`) |
| `who` | autor/remetente como chegou |
| `who_kind` | pessoa, ferramenta, transacional ou desconhecido |
| `excerpt` | trecho bruto normalizado, máximo ~200 caracteres |
| `ref` | ID estável da evidência |

`list_recent` lê o Ledger do fim para o começo, aplica janela/filtros e para no limite. Ele não carrega JSONL inteiro na conversa.

## Escrita e consistência

A ordem é intencional:

1. raw atômico;
2. linha normalizada + FTS no SQLite, em transação;
3. linha compacta no Ledger com lock local e `fsync`;
4. cursor do conector, somente depois de todas as três camadas.

Uma queda deixa, no pior caso, raw sem projeção. Reexecutar usa o mesmo ID e fecha a lacuna sem duplicar. O cursor não avança se uma página falhar.

## Recuperação

1. `search_context` monta termos literais FTS e retorna no máximo 10 snippets com ID, fonte, data e proveniência.
2. `list_recent` retorna no máximo 10 linhas compactas da janela curta.
3. `get_context(id)` abre um item já identificado e limita texto a 6.000 caracteres; possui limite de taxa.

A expansão só acontece por ID. A ausência de uma tool `list_all`, SQL, shell, raw ou exportação é uma decisão de segurança, não uma lacuna acidental.

## Por que SQLite/FTS5

Para uma pessoa em uma VPS, o contexto já está local. Colocar isso em um banco remoto acrescentaria trânsito, chaves e infraestrutura antes do primeiro valor. FTS5 é determinístico, auditável, offline e instalado com Python/SQLite comuns. Embeddings só entram depois de avaliações mostrarem perda material de recuperação; raw e Ledger continuam fora desse índice futuro.

## Runtime canônico

O código canônico é a cópia versionada em `~/.context-kit/app/src`. O wrapper em `~/.context-kit/bin/agent-context-kit` só ajusta `PYTHONPATH` e chama `python3 -m agent_context_kit.cli`. `doctor --runtime-wrapper …` compara a versão desse caminho com a versão canônica; não há cópia de regra de negócio dentro do Hermes.
