# Plano de implementação — Agent Context Kit v0.1

> **Status:** entregue em código (0.1.0)  
> **Fonte de produto:** PRD canônico em `projects/agent-context-hub/PRD.md` no segundo cérebro do projeto  
> **Repositório público de entrega:** https://github.com/okjpg/agent-context-kit  
> **Escopo travado:** `files` + Fathom, SQLite/FTS5, MCP por stdio, instalação Hermes e documentação operacional.

## Objetivo

Entregar um kit local-first que guarda evidência privada fora do Git, a recupera por consultas pequenas e rastreáveis e deixa uma rota explícita para que um agente Hermes encontre o contexto sem varrer diretórios ou receber um dump de memória.

## Decisões de implementação

| Decisão | Implementação | Motivo |
|---|---|---|
| Runtime | Python 3.10+ e biblioteca padrão | instalação sem `pip`, venv, banco ou serviço extra |
| Evidência | SQLite privado com FTS5 + cópia raw no vault | busca lexical auditável; evidência durável e reconstruível |
| Mapa compacto | JSONL append-only de seis campos | perguntas recentes sem carregar conteúdo completo |
| Interface do agente | MCP stdio com 3 tools | zero porta HTTP; superfície mínima e read-only |
| Conectores v0.1 | `files` e Fathom | primeira vitória sem chave + prova de uma ferramenta real |
| Instalação | script auditável que chama `hermes mcp add` | usa o mecanismo real do runtime, com backup e rollback |

## Gates do v0.1

1. **Core privado:** modelos, paths seguros, SQLite/FTS5, raw, ledger e recibos.
2. **Conectores:** inbox files + Fathom com cursor pós-commit e dedupe.
3. **MCP:** três tools limitadas; sem SQL, shell, raw, export ou escrita.
4. **Instalação Hermes:** wrapper, skill, mapa, demo, doctor, uninstall.
5. **Documentação e release:** quickstart, guia de teste, aceite reproduzível, scan sanitário.

## Fora de escopo (de propósito)

Webhook, dashboard, OAuth, embeddings, banco remoto, cron, watcher, plugins, WhatsApp, Gmail/Calendar e escrita automática no cérebro.

## Honestidade de validação

- Install limpo + MCP + demo + scan: cobertos por testes/smoke no repo.
- Fathom real: o contrato é testado com transporte simulado; conexão de conta real só é “ok” quando o tester cola a própria key e o probe passa.
