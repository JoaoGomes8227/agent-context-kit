# Conectores

## Regra de entrada v0.1

Um conector entra se fizer:

```text
uma chave simples → probe read-only → pull → ContextItem → dedupe → citação
```

Nada de webhook, endpoint público, OAuth, domínio ou processo sempre ligado. Toda fonte é opcional: o Kit continua útil com `files` apenas.

## `files` — zero chave

| Item | Regra |
|---|---|
| Escopo | somente a inbox explícita do Kit |
| Tipos | `.md` e `.txt` UTF-8 |
| Limite | 1 MB por arquivo por default, configurável até 10 MB |
| Dedupe | caminho relativo + SHA-256 do conteúdo |
| Atualização | lazy: no início do MCP e antes de busca após cache curta |
| Exclusões | symlink, path escape, binário, vazio, extensão não suportada, oversized |

Arquivos alterados geram nova evidência; o histórico não é sobrescrito silenciosamente.

## Fathom — reuniões reais, opcional

### O que o Kit lê

O conector usa `GET /external/v1/meetings`, com `X-Api-Key`, `include_transcript=true` e paginação por `next_cursor`. Ele nunca cria, edita, apaga, compartilha ou envia nada no Fathom.

### Como conectar

```bash
~/.context-kit/bin/agent-context-kit connect fathom
```

1. a chave é pedida em prompt sem eco;
2. o Kit faz uma chamada read-only de probe;
3. só se o probe funcionar a chave é gravada em `vault/config.json` (`0600`);
4. a primeira carga roda e gera recibo seguro;
5. pull posterior é lazy e deduplicado.

Chave inválida gera erro amigável e não afeta `files`, banco existente ou demo.

### Escopo e revogação

A chave vê somente reuniões visíveis para o usuário Fathom dela. Para interromper acesso local:

```bash
~/.context-kit/bin/agent-context-kit disconnect-fathom
```

Para revogar no fornecedor, remova a API key em **Fathom → User Settings → API Access**. Depois rode `disconnect-fathom` localmente.

### Limites conhecidos

O Fathom documenta limite de 60 chamadas/minuto por usuário. O Kit limita a cinco páginas por sync lazy, usa cache curta entre buscas repetidas e nunca inicia daemon/cron. Para um backfill muito grande, repita consultas naturais; o cursor é salvo apenas após a página persistir.

### O que significa “conectado”

A chave só é marcada conectada após probe read-only no endpoint real. Ter conta, login, plano ou uma chave armazenada não é prova. `status` mostra apenas `enabled` e `credential_stored`; não imprime a chave, o nome da conta, reunião ou transcript.

## Próximas categorias (fora de v0.1)

| Categoria | Por que não entra agora |
|---|---|
| WhatsApp | precisa QR/gateway e regras de escopo próprias |
| Gmail/Calendar | OAuth/IMAP precisam onboarding separado |
| Granola | API é alternativa paga e só entra quando houver segundo conector de reuniões real |

A interface se organiza por categoria (`meetings`, `files`), mas não existe plugin framework antes de necessidade provada por múltiplas implementações.
