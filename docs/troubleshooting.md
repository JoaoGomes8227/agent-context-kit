# Troubleshooting

## Instalação por `curl` falhou ao clonar

Confirme rede, `git` no PATH e que o repositório público responde:

```bash
git ls-remote https://github.com/okjpg/agent-context-kit.git HEAD
curl -fsI https://raw.githubusercontent.com/okjpg/agent-context-kit/main/install.sh
```

Se o clone falhar, use o [Caminho B do guia de teste](testing.md) a partir de um zip/clone já baixado.

## `hermes mcp test agent-context-kit` falha

1. Rode:

   ```bash
   ~/.context-kit/bin/agent-context-kit doctor --runtime-wrapper ~/.context-kit/bin/agent-context-kit
   ```

2. Confirme que o wrapper existe e está executável (`doctor` faz a comparação de versão).
3. Não edite `~/.hermes/config.yaml` manualmente antes de olhar o backup em `~/.context-kit/backups/`.
4. Se a instalação foi interrompida, reexecute o instalador da mesma versão; ele faz backup e tenta uma instalação limpa.
5. Confirme `command -v hermes` e que uma sessão Hermes normal já funciona nesta máquina.

## As tools não aparecem na conversa

`hermes mcp test` valida o transporte, mas sessões abertas antes da instalação mantêm o catálogo anterior. Abra uma nova sessão Hermes. Verifique também se a skill existe:

```bash
test -f ~/.hermes/skills/agent-context-kit/SKILL.md && echo ok
```

## Meu arquivo não apareceu

- Ele precisa estar na inbox configurada, não no cérebro inteiro.
- Só `.md` e `.txt` UTF-8 entram no v0.1.
- Symlinks, arquivo vazio, binário ou maior que o limite são ignorados.
- Rode `sync --source files` e consulte `status`; ambos mostram contagem/recibo sem imprimir conteúdo.

## Fathom recusou a chave

O Kit não grava uma chave antes do probe. Confirme que você copiou uma API key de **User Settings → API Access**, não uma URL ou token de outro produto. Tente novamente:

```bash
~/.context-kit/bin/agent-context-kit connect fathom
```

Se a fonte estiver rate-limited ou indisponível, o modo arquivos continua operando. O recibo registra um código seguro; não cole chave nem resposta HTTP em chat/issue.

## Ledger e banco parecem divergentes

O SQLite é a autoridade. Reconstrua apenas o mapa compacto:

```bash
~/.context-kit/bin/agent-context-kit rebuild-ledger
```

## Quero apagar tudo

O uninstall preserva seu vault. Para excluir dado, remova cada fonte explicitamente com `purge-source --yes-delete-source`, valide `status` e então apague o vault manualmente apenas depois de confirmar que não precisa de backup. Não existe opção “limpar tudo” escondida no Kit.

## Permissões aparecem como inválidas

Mova o vault para filesystem local Linux que suporte `chmod`, ou instale com `ACK_HOME=/caminho-seguro` antes do comando. Depois rode `doctor` de novo. Não contorne isso tornando o diretório público.
