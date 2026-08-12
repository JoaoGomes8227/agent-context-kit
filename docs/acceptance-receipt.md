# Recibo de aceite reproduzível

Este documento define como provar o v0.1 sem depender de uma conta ou transcrição privada.

## Gate A — clone e instalação limpa

```bash
git clone https://github.com/okjpg/agent-context-kit.git agent-context-kit
cd agent-context-kit
HOME="$(mktemp -d)" ACK_HOME="$HOME/.context-kit" bash scripts/install.sh --source "$PWD"
```

Esperado:

- exit `0`;
- vault `0700`, config `0600`;
- skill instalada;
- `hermes mcp test agent-context-kit` descobre exatamente três tools;
- `doctor --runtime-wrapper …` responde `status=ok`;
- nenhum banco/raw entra no clone.

O harness automatizado em `tests/install_smoke.py` executa essa sequência em HOME temporário (exige `hermes` no PATH). A suíte comportamental em `tests/run.py` cobre storage, conectores simulados, MCP e limites anti-dump sem precisar de install completo.

## Gate B — primeira vitória local

1. seed sintético cria um `.md` e uma reunião `account=demo`;
2. `search_context("proposta revisada")` retorna snippet com fonte/data/proveniência;
3. `get_context(id)` abre somente o item escolhido;
4. a segunda execução do seed/sync adiciona zero e informa dedupe;
5. restart do processo MCP preserva banco, config e busca.

## Gate C — conector Fathom

A suíte usa transporte HTTP simulado para cobrir: header `X-Api-Key`, páginas, transcript, dedupe, cursor pós-commit, chave inválida e erro de rede seguro. Isso prova o contrato sem credencial.

A conexão de uma pessoa só é declarada real quando `connect fathom` faz probe read-only no endpoint real, vê a conta/escopo daquela chave e grava recibo `ok`. Sem uma key voluntariamente fornecida, este repositório não pode afirmar que uma conta real foi conectada — e não finge isso.

## Gate D — limites negativos

Os testes devem provar:

- `list_recent` respeita janela e máximo 10;
- `search_context` rejeita query longa/sintaxe não controlada;
- `get_context` exige ID explícito e limita resposta;
- não existe tool `list_all`, `raw`, SQL, shell ou mutação;
- symlink, traversal, binário, extensão errada e oversized são rejeitados/ignorados;
- conteúdo de prompt injection permanece resultado de texto, sem tool adicional;
- logs/recibos/status não incluem segredo ou payload.

## Gate E — release sanitizado

```bash
python3 scripts/check_public.py
git diff --check
git status --short
```

O scanner verifica padrões comuns de segredo e caminhos/identificadores privados proibidos. A inspeção humana continua obrigatória: scanner não torna conteúdo real seguro automaticamente.
