# Contribuindo

## Escopo v0.1

Antes de abrir código, confirme que melhora uma destas três coisas: instalação, recuperação limitada ou um conector real. Não introduza dashboard, webhook, OAuth, embeddings, banco remoto, plugin loader, cron, watcher, WhatsApp, Gmail ou escrita automática no cérebro por conveniência.

## Convenções

- Python 3.10+, biblioteca padrão no core;
- novo conector precisa de fixture sintética, testes de dedupe/cursor e documentação de revogação;
- `ContextItem` só ganha campo depois de dois conectores reais justificarem;
- raw/cache/config nunca entram no Git;
- todo resultado público preserva fonte, data e proveniência;
- nenhum diagnóstico imprime conteúdo privado ou segredo.

## Antes do PR

```bash
PYTHONPATH=src python3 tests/run.py
python3 scripts/check_public.py
git diff --check
```

Rode também os comandos documentados que você alterou. Se mexer em instalador, teste em HOME temporário e prove rollback/uninstall.
