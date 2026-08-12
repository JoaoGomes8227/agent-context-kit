# Instalação

## Antes de começar

Você precisa de uma VPS Linux com:

- Hermes Agent instalado e respondendo normalmente;
- `python3` 3.10 ou superior;
- SQLite compilado com FTS5;
- acesso de escrita à sua HOME;
- `git` (para o caminho de um comando via curl).

Não precisa de: domínio, Docker, Supabase, banco em nuvem, webhook, OAuth, `pip`, `venv` ou API key.

## O único comando de instalação

```bash
curl -fsSL https://raw.githubusercontent.com/okjpg/agent-context-kit/main/install.sh | bash
```

Se preferir inspecionar o código antes:

```bash
git clone https://github.com/okjpg/agent-context-kit.git
cd agent-context-kit
bash install.sh
```

Quem foi convidado só para validar o produto: use o [Guia para testers](testing.md).

O instalador toma defaults seguros e não pede decisões técnicas:

1. valida Python, FTS5 e Hermes;
2. copia o código canônico para `~/.context-kit/app`;
3. cria `~/.context-kit/vault` com permissão `0700`;
4. cria a inbox `~/.context-kit/vault/inbox` e a demo sintética;
5. instala o wrapper fino em `~/.context-kit/bin/agent-context-kit`;
6. instala a skill `agent-context-kit` no discovery do Hermes;
7. faz backup de `~/.hermes/config.yaml` antes de alterá-lo;
8. registra o MCP por stdio, descobre as tools e executa `hermes mcp test agent-context-kit`;
9. roda `doctor` usando o mesmo wrapper que o Hermes vai executar.

Se uma etapa falhar, o instalador restaura a configuração Hermes anterior e preserva o vault. O backup fica em `~/.context-kit/backups/install-<UTC>/`.

## Primeira vitória, sem chave

Abra uma **nova sessão Hermes** para ele recarregar a skill e as tools MCP. Pergunte:

> O que eu prometi na reunião de demonstração? Cite a fonte.

O resultado deve apontar a demo sintética. Ela inclui uma reunião e um arquivo; isso prova as duas superfícies sem acessar uma conta externa.

Depois, coloque um arquivo pessoal `.md` ou `.txt` na inbox configurada. Por default:

```text
~/.context-kit/vault/inbox/
```

Na próxima consulta (a cache lazy é curta), o Kit indexa esse arquivo. Não use a pasta inteira do seu segundo cérebro como inbox: ela é deliberadamente uma área explícita e limitada.

## Se seu cérebro já tem uma inbox

A instalação padrão não reorganiza o workspace. Para escolher uma inbox existente, faça a configuração local explícita:

```bash
~/.context-kit/bin/agent-context-kit init --inbox "$HOME/seu-cerebro/inbox/context"
```

Isso não indexa o cérebro todo — só `.md` e `.txt` abaixo desse caminho específico.

## O que o instalador não faz

- não lê seus arquivos existentes fora da inbox;
- não envia dados para nuvem;
- não pede nem salva API key;
- não cria cron, watcher ou daemon;
- não edita o segundo cérebro;
- não apaga dados se você remover a integração.

## Comprovantes

Após instalar, estes comandos não expõem conteúdo ou chave:

```bash
~/.context-kit/bin/agent-context-kit status
~/.context-kit/bin/agent-context-kit doctor --runtime-wrapper ~/.context-kit/bin/agent-context-kit
hermes mcp test agent-context-kit
```

`status` mostra fontes, contagem e recibos; `doctor` verifica pré-requisitos, permissão, FTS5, integridade e se o wrapper efetivo corresponde ao código canônico.

## Atualizar

O v0.1 não possui auto-update. Baixe uma versão revisada e rode novamente o instalador; ele cria backup antes de substituir o runtime. Revise o [CHANGELOG](../CHANGELOG.md) antes.

## Desinstalar sem apagar o que é seu

```bash
~/.context-kit/bin/uninstall-agent-context-kit --yes
```

Ele remove somente a integração MCP e a skill, guarda backup da configuração Hermes e **preserva o vault**. Se você estiver rodando de um clone ainda não instalado, o equivalente é:

```bash
bash scripts/uninstall.sh --yes
```

Para remover uma fonte de forma destrutiva, use o fluxo explícito em [Operação](operations.md).
