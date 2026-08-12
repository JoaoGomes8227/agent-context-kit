# Documentação — Agent Context Kit

## Comece por aqui

| Situação | Documento | Resultado |
|---|---|---|
| Fui convidado para testar o repo | [Guia para testers](testing.md) | install → checks → primeira vitória → feedback seguro |
| Quero instalar sem depender de infraestrutura | [Instalação](installation.md) | primeira vitória sintética e MCP testado |
| Quero entender o que roda e por quê | [Arquitetura](architecture.md) | fronteiras entre raw, SQLite, Ledger, MCP e cérebro |
| Quero ligar uma fonte real | [Conectores](connectors.md) | escopo, probe read-only, revogação e limites |
| Quero saber o que meu agente deve fazer | [Roteamento Hermes](agent-routing.md) | busca primeiro, evidência citada, promoção explícita |
| Quero operar/diagnosticar/remover | [Operação](operations.md) | status, doctor, recibos, repair, purge e uninstall |
| Quero revisar privacidade | [Segurança](security.md) | modelo de ameaça, permissões, retenção e limites |
| Algo falhou | [Troubleshooting](troubleshooting.md) | caminhos de correção sem despejar conteúdo privado |
| Quero conferir a entrega | [Recibo de aceite](acceptance-receipt.md) | comandos e gates reproduzíveis |

## Ordem de leitura recomendada

1. **Tester externo:** [Guia para testers](testing.md) → Instalação → Troubleshooting.
2. **Aluno / operador:** Instalação → Roteamento Hermes → Conectores → Operação.
3. **Pessoa responsável por privacidade:** Arquitetura → Segurança → Recibo de aceite.
4. **Pessoa contribuindo com código:** Arquitetura → Conectores → [CONTRIBUTING.md](../CONTRIBUTING.md) → Recibo de aceite.

## Contrato de documentação

A documentação descreve somente o que o v0.1 realmente executa. Cada afirmação operacional importante precisa ter um recibo ou teste correspondente:

| Afirmação | Evidência no repo |
|---|---|
| instala em clone/HOME limpo | `tests/install_smoke.py` |
| MCP expõe só três tools | `tests/run.py` + `hermes mcp test` no smoke |
| busca não vira dump | testes de limite/ausência de tool de bulk dump em `tests/run.py` |
| files e Fathom repetem sem duplicar | testes de conector/dedupe em `tests/run.py` |
| dados não vão para Git público | `.gitignore` + `scripts/check_public.py` |
| uninstall não apaga vault | `tests/install_smoke.py` |

Se um comportamento mudar, atualize **código, teste, recibo de aceite e documento de operação na mesma alteração**. Não use documentação para prometer conectores, automações ou proteção que o runtime ainda não provou.
