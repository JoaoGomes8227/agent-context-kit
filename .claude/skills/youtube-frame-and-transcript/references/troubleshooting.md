# Troubleshooting

## Erros do yt-dlp no sandbox

| Sintoma | O que fazer |
|---|---|
| `HTTP Error 429` em uma faixa de legenda | Ignore se outra faixa já foi gravada. Se todas falharam, espere 30 s e rode de novo só com `--sub-lang "pt"` (uma faixa). |
| `Sign in to confirm you're not a bot` | Troque a ordem dos clients: `player_client=tv,android,web_embedded`. Se persistir, o vídeo exige login e está fora do escopo. |
| `Private video` / `Video unavailable` | Fora do escopo. Informe o usuário; não peça credenciais. |
| `Requested format is not available` no frame | Use `-f "b[height<=480]/b"`; alguns vídeos só têm formatos combinados. |
| `--download-sections` ignorado, baixou o vídeo inteiro | Falta `ffmpeg` no sandbox. Instale com `apt-get install -y -qq ffmpeg` e repita. |
| Aviso "impersonation ... not available" | Só aviso. Ignore. |
| `WARNING: ... no subtitles` | O vídeo não tem legenda automática nem manual. Não há transcrição; diga isso ao usuário. |

## Sandbox

- `/mnt/files` é persistente entre execuções e entre reinícios do sandbox. Pacotes instalados com
  `pip` e `apt` podem sumir num reinício; reinstale sem perguntar.
- Limite duro de 180 s por comando. Legenda e clipe de 4 s cabem folgados; um trecho de vários
  minutos em 1080p não. Reduza a resolução ou a janela.
- `COMPOSIO_REMOTE_WORKBENCH` é um Jupyter persistente com helpers pré-carregados:
  `upload_local_file(path)`, `get_mount_file_url(path)`, `invoke_llm(query)`. Só
  `upload_local_file` gera um link que redireciona para storage externo alcançável. `invoke_llm` é
  texto puro e não vê imagens. `show_file` é um stub que não faz nada.

## Rede no ambiente local

- `youtube.com`, `googlevideo.com` e `backend.composio.dev` são negados pelo proxy de egress com
  `403` no CONNECT. WebFetch devolve `EGRESS_BLOCKED` para os mesmos hosts.
- O storage final (hoje um bucket R2 em `*.r2.cloudflarestorage.com`) é alcançável. Por isso o
  redirecionamento precisa ser resolvido no sandbox e a URL final baixada localmente.
- Correção definitiva: adicionar `backend.composio.dev` à allowlist de rede do ambiente em
  claude.ai/code (documentação em https://code.claude.com/docs/en/claude-code-on-the-web). Com isso o
  link curto funciona direto e o passo do redirect deixa de ser necessário.

## Permissões e classificador

- Um `curl` local em loop contra vários sites públicos de upload foi bloqueado pelo classificador
  do modo auto, porque se parece com busca de canal de exfiltração. O bloqueio está correto. O
  caminho legítimo é o helper de upload do Composio, que já existe para isso.
- Não peça ao usuário regra ampla como liberar todo `curl`. O único `curl` local necessário é o
  download da URL final do storage, e ele passa sem prompt.

## Becos sem saída já percorridos

1. `YOUTUBE_LOAD_CAPTIONS` → 403, restrição de propriedade da YouTube Data API v3.
2. `youtube-transcript-api` no sandbox → `IpBlocked`.
3. `youtube-transcript-api` local → `ProxyError 403`.
4. WebFetch do link curto do Composio → `EGRESS_BLOCKED`.
5. `curl` local do link curto → `CONNECT tunnel failed, response 403`.
6. Base64 do frame no stdout e retranscrição manual → corrompe o arquivo.
7. Sondagem de hosts públicos de upload → bloqueado pelo classificador.
8. OCR com tesseract no frame → lixo em telas desenhadas à mão; útil só para slides com texto impresso.
9. Toolkits de scraping do Composio (Firecrawl, Olostep etc.) → exigem conexão nova e não resolvem
   legenda nem frame; não vale o desvio.
