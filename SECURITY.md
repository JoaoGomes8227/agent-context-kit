# Política de segurança

Não publique API keys, transcrições, arquivos privados, IDs de conta, caminhos de vault, logs com payload ou qualquer reprodução que exponha o mesmo.

Para relatar vulnerabilidade, use um canal privado com os mantenedores do repositório `okjpg/agent-context-kit` (issue privada, security advisory ou contato direto do maintainer). Descreva impacto, versão (`VERSION` / tag), passos mínimos **sintéticos** e mitigação sugerida.

Se um segredo já vazou, **revogue primeiro** e só depois relate o incidente sem repetir o valor.

O Kit é local-first e single-user na VPS. Achados sobre multi-tenant, webhook ou OAuth devem deixar claro que estão fora do v0.1, salvo se afetarem a superfície já instalada (MCP stdio, vault, conectores files/Fathom).
