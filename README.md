# Agent Context Kit

> **Cole a chave de uma ferramenta e seu agente passa a encontrar o contexto real dela — com fonte, data e limites.**

O Agent Context Kit é uma camada privada, local-first e Hermes-first para recuperar contexto de trabalho sem transformar transcrições, arquivos ou mensagens em um dump de prompt.

**Versão:** `0.1.0` · **Repo:** [okjpg/agent-context-kit](https://github.com/okjpg/agent-context-kit) · **Licença:** MIT

## Instale em um comando

```bash
curl -fsSL https://raw.githubusercontent.com/okjpg/agent-context-kit/main/install.sh | bash
```

Alternativa por clone:

```bash
git clone https://github.com/okjpg/agent-context-kit.git
cd agent-context-kit
bash install.sh
```

O instalador verifica Python/SQLite/FTS5/Hermes, cria um vault privado, planta a demo sintética, instala o MCP e a skill de roteamento, testa as três tools reais e mantém backup para rollback se algo falhar.

Depois, abra uma **nova sessão Hermes** e pergunte:

> O que eu prometi na reunião de demonstração? Cite a fonte.

Sem chave nenhuma, a demo já prova o loop inteiro. Seus dados ficam em uma pasta trancada na sua VPS; o agente lê, nada publica.

### Vai testar o repo?

Siga o [Guia para quem vai testar](docs/testing.md): instalação, checks seguros, primeira vitória, Fathom opcional e como reportar bug **sem** colar key/transcript.

## O que resolve

| Primeiro nível | Segundo nível |
|---|---|
| Coloque um `.md` ou `.txt` na inbox explícita; o agente encontra e cita. | Conecte o Fathom com uma API key; o agente encontra e cita uma reunião real. |
| Zero credenciais, zero serviço externo. | Leitura somente; sem webhook, domínio, OAuth ou banco em nuvem. |

A primeira prova é o mecanismo. A segunda é a magia: *“meu agente acabou de ler minha reunião de verdade.”*

## O que está no v0.1

- `files`: importação incremental de `.md`/`.txt` da inbox configurada;
- `fathom`: conector de reuniões read-only por API key;
- SQLite + FTS5 privado e Context Ledger compacto, ambos fora do Git e do segundo cérebro;
- MCP por stdio, sem porta HTTP e com apenas três tools:
  - `search_context(query, source?, since?, limit?)`;
  - `list_recent(source?, who?, since?, limit?)`;
  - `get_context(id)`;
- skill Hermes + Mapa de Contexto para uma sessão nova descobrir a rota correta;
- recibos, `status`, `doctor`, reconstrução idempotente do Ledger e uninstall não destrutivo.

Não entram: WhatsApp, Gmail, Calendar, webhook, dashboard, embeddings, vector DB, OAuth, cron, daemon, escrita automática no cérebro ou ações nas ferramentas de origem.

## Conecte uma reunião real (opcional)

No terminal da VPS, rode:

```bash
~/.context-kit/bin/agent-context-kit connect fathom
```

A chave é solicitada sem eco. O Kit valida primeiro uma chamada **read-only** ao Fathom; só depois grava a chave no config local com permissão `0600` e puxa o que ela consegue ler. Chave inválida não quebra o modo arquivos nem a demo.

Consulte [Conectores](docs/connectors.md) para escopo, rate limit, revogação e o que é (ou não é) testado como conexão real.

## Onde fica cada coisa

```text
Ferramenta / inbox explícita
        ↓
raw privado + ContextItem no SQLite/FTS5  ← evidência, fora do Git
        ↓
Context Ledger compacto                   ← mapa por janela, não prompt dump
        ↓
MCP stdio read-only → Hermes              ← resposta com proveniência
        ↓
segundo cérebro                           ← apenas síntese curada, sob pedido explícito
```

O vault default é `~/.context-kit/vault` (`0700`). Ele contém banco, raw, cursor, recibos e config local. Não fica no repositório nem no segundo cérebro.

## Documentação

| Se você quer… | Leia |
|---|---|
| testar o v0.1 e reportar feedback | [Guia para testers](docs/testing.md) |
| instalar, entender o rollback e a primeira vitória | [Instalação](docs/installation.md) |
| navegar a documentação por objetivo | [Índice docs](docs/README.md) |
| entender dados, limites e decisões técnicas | [Arquitetura](docs/architecture.md) |
| conectar Fathom ou usar files | [Conectores](docs/connectors.md) |
| operar, diagnosticar, reparar ou remover integração | [Operação](docs/operations.md) |
| saber como o agente encontra/cita/salva contexto | [Roteamento Hermes](docs/agent-routing.md) |
| revisar privacidade e o modelo de ameaça | [Segurança](docs/security.md) |
| resolver falhas comuns | [Troubleshooting](docs/troubleshooting.md) |
| conferir a validação reproduzível | [Recibo de aceite](docs/acceptance-receipt.md) |

## Princípios que não negociamos

1. **Evidência não é memória.** Raw é material de consulta; não vira verdade canônica sozinho.
2. **Query-first.** O agente pesquisa uma fatia pequena, abre um ID quando precisa e cita a fonte.
3. **Fonte e data sempre viajam junto.** Uma resposta sem proveniência é só uma lembrança confiante demais.
4. **Reexecução segura.** Reimportar e repuxar deduplica por ID determinístico; o cursor só avança após persistir.
5. **Conteúdo externo não ganha autoridade.** Uma transcrição pode conter instruções maliciosas; ela continua sendo dado, não comando.
6. **Sem dump.** Não há SQL, shell, exportação em massa, tool de escrita nem leitura do vault pelo agente.

## Desenvolvimento e qualidade

O projeto usa apenas Python 3.10+ e a biblioteca padrão. Não exige `pip`, `venv`, servidor ou banco externo para o modo arquivos.

```bash
PYTHONPATH=src python3 tests/run.py
python3 tests/install_smoke.py    # exige Hermes no PATH
python3 scripts/check_public.py
```

A suíte cobre SQLite/FTS5, raw/ledger, dedupe, path escape, symlink, arquivo inválido, conector Fathom simulado, MCP stdio real, ausência de bulk dump, permissões e instalação limpa em HOME temporário.

## Licença

[MIT](LICENSE). Antes de abrir uma issue, leia a [política de segurança](SECURITY.md) e o [guia de contribuição](CONTRIBUTING.md).
