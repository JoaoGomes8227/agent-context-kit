# Segurança e privacidade

## Modelo de ameaça v0.1

O Kit protege uma instalação local de uma pessoa em uma VPS. Não é um produto multi-tenant nem um cofre de credenciais compartilhado. A regra central é simples:

> Texto recuperado é evidência não confiável; nunca autoriza um comando, ação ou acesso.

## Controles implementados

| Risco | Controle |
|---|---|
| agente recebe contexto demais | FTS por termo, janela, limite ≤10, snippet; detalhe apenas por ID |
| dump de banco/Ledger | não há tool de SQL, shell, raw, exportação ou listagem total |
| porta exposta | MCP é stdio; nenhum listener HTTP é aberto |
| Git captura dados | vault default está fora do repo; `.gitignore` cobre runtime local |
| key em log/config público | config local `0600`; status/doctor/recibo não exibem segredo |
| fonte recebe escrita | conectores v0.1 usam apenas GET |
| symlink/path escape | inbox e vault rejeitam symlink; arquivos precisam permanecer sob inbox resolvida |
| arquivo malicioso | tamanho, UTF-8, extensão e NUL são validados; texto não é executado |
| repetição ou queda | ID determinístico, raw atômico, SQLite transacional, Ledger com lock e cursor pós-commit |
| remoção acidental | uninstall preserva dados; purge exige flag explícita |

## Permissões esperadas

```text
~/.context-kit/                 0700
~/.context-kit/vault/           0700
~/.context-kit/vault/config.json 0600
~/.context-kit/vault/raw/**     0600
~/.context-kit/vault/receipts/** 0600
```

Rode `doctor` para detectar desvio. Em filesystem que não respeita `chmod`, trate o resultado como sinal para mover o vault a um volume local apropriado.

## O que ainda pode sair da VPS

Quando Hermes responde, o trecho recuperado pode ser incluído na conversa enviada ao provedor de modelo que você configurou. O Kit não adiciona telemetria, mas não consegue mudar a política do seu provedor de LLM. Use a mesma classificação que aplicaria ao conteúdo do seu segundo cérebro.

## Dados que não entram no segundo cérebro automaticamente

- transcript completo;
- raw de API;
- Context Ledger inteiro;
- API key, cursor, recibos técnicos ou caminho do banco;
- qualquer texto só porque apareceu numa fonte.

Uma promoção é explícita: o agente escreve apenas uma síntese curta, data e ponteiros de evidência no local canônico do cérebro do usuário.

## Retenção e exclusão

- `uninstall` tira MCP e skill, mas mantém o vault.
- `purge-source --source files --yes-delete-source` ou `--source fathom` remove explicitamente evidência, FTS, raw daquela fonte e reconstrói o Ledger restante.
- Faça backup criptografado do vault somente se você controlar o destino. Backup em cloud-sync não é default do Kit.

## Reportar vulnerabilidade

Não abra issue pública com key, arquivo real, transcript, ID de conta ou reprodução que exponha dados. Siga [SECURITY.md](../SECURITY.md).
