---
name: youtube-frame-and-transcript
description: "Extrai de qualquer vídeo público do YouTube a transcrição/legenda, os metadados e frames exatos (captura de tela em um minuto específico, ex.: 4:40) usando o Composio (toolkit YouTube + sandbox remoto com yt-dlp e ffmpeg), e traz o frame de volta para o Claude ver e descrever. Use SEMPRE que o usuário colar um link ou ID do YouTube (youtu.be/..., watch?v=..., shorts/...) e pedir para resumir, extrair pontos principais, transcrever, pegar legendas, dizer 'o que aparece na tela' ou 'o que ele mostra' em um minuto, capturar/printar um frame, ou relacionar o conteúdo do vídeo com um projeto, mesmo sem mencionar Composio, transcript ou screenshot. Também use quando uma tentativa direta de ler o YouTube falhou por bloqueio de rede ou 403 de legenda."
---

# YouTube: transcrição, metadados e frame por minuto

Procedimento fechado, validado em sessão real, para ler um vídeo público do YouTube a partir de um
ambiente Claude Code (web, celular ou desktop) onde o acesso direto a `youtube.com` costuma ser
bloqueado. O trabalho pesado roda no **sandbox remoto do Composio**, que tem rede livre; o
ambiente local só recebe o resultado final.

## Por que este caminho e não o óbvio

Cada atalho abaixo já foi tentado e falha. Não repita:

| Tentativa | Resultado | Motivo |
|---|---|---|
| `YOUTUBE_LOAD_CAPTIONS` | 403 | A API oficial só entrega legendas de vídeos que a conta conectada possui |
| `youtube-transcript-api` no sandbox | `IpBlocked` | YouTube bloqueia IPs de nuvem para esse endpoint |
| `curl`/`pip` para `youtube.com` no ambiente local | 403 do proxy | Política de egress do ambiente Claude Code |
| `curl`/WebFetch para `backend.composio.dev` | 403 do proxy | Mesmo motivo; só o storage final é alcançável |
| Copiar base64 da imagem à mão | Corrompe | 20 KB de base64 não sobrevivem à transcrição manual |
| Sondar hosts públicos de upload (0x0.st, transfer.sh...) | Bloqueado pelo classificador | Parece exfiltração; use o helper de upload do Composio |

O que funciona: `yt-dlp` dentro do sandbox do Composio com `player_client=android,web_embedded,tv`,
`ffmpeg` para o frame, e o helper `upload_local_file` do workbench para exportar o arquivo por um link
de storage assinado.

## Pré-requisitos

- Tools MCP do Composio disponíveis: `COMPOSIO_SEARCH_TOOLS`, `COMPOSIO_MULTI_EXECUTE_TOOL`,
  `COMPOSIO_REMOTE_BASH_TOOL`, `COMPOSIO_REMOTE_WORKBENCH`. Se estiverem deferidas, carregue com
  `ToolSearch` usando `select:mcp__Composio__COMPOSIO_SEARCH_TOOLS,...`.
- Toolkit `youtube` conectado no Composio. `COMPOSIO_SEARCH_TOOLS` informa; se não estiver,
  chame `COMPOSIO_MANAGE_CONNECTIONS` e mostre o link ao usuário.
- Aviso único ao usuário, na primeira vez na conversa: o `yt-dlp` acessa o YouTube fora da API
  oficial. Só funciona em vídeos públicos ou não listados, e é responsabilidade do usuário aceitar
  esse uso.

## Passo 0: extrair o ID do vídeo

Aceite qualquer forma: `youtu.be/ID?si=...`, `youtube.com/watch?v=ID`, `youtube.com/shorts/ID`,
`youtube.com/live/ID`, ou o ID cru de 11 caracteres. Descarte tudo depois de `?` ou `&`.
Timestamps do pedido do usuário ("minuto 4:40", "aos 12min50") viram segundos inteiros.

## Passo 1: metadados e faixas de legenda (Composio, API oficial)

Chame `COMPOSIO_SEARCH_TOOLS` com `session: {generate_id: true}` e um use_case como
"get YouTube video details by video id". Depois execute em paralelo com `COMPOSIO_MULTI_EXECUTE_TOOL`:

- `YOUTUBE_GET_VIDEO_DETAILS_BATCH` com `id: ["<ID>"]`, `parts: ["snippet","contentDetails","statistics"]`
  → título, canal, data, duração, descrição, idioma padrão.
- `YOUTUBE_LIST_CAPTION_TRACK` com `video_id` → idiomas de legenda existentes e se são `asr`
  (automáticas). Use isso só para escolher o `--sub-lang`; não chame `YOUTUBE_LOAD_CAPTIONS`.

Guarde o `session_id` retornado e passe-o em todas as chamadas seguintes.

## Passo 2: transcrição (sandbox do Composio)

Rode em `COMPOSIO_REMOTE_BASH_TOOL`. Troque `VID` e os idiomas conforme o Passo 1
(ex.: `"pt.*,en.*"`). O limite de execução é 180 s; este bloco costuma levar menos de 30 s.

```bash
cd /mnt/files && VID=kbR8goTbJS0 && pip install -q -U yt-dlp 2>&1 | grep -v notice | tail -1
timeout 150 yt-dlp -q --no-warnings --skip-download --write-auto-sub --write-sub \
  --sub-lang "pt.*,en.*" --sub-format vtt \
  --extractor-args "youtube:player_client=android,web_embedded,tv" \
  -o "tx_%(id)s" "https://www.youtube.com/watch?v=$VID" 2>&1 | grep -iE "error|writing" | head -5
ls tx_${VID}*.vtt
python3 - "$VID" <<'EOF'
import re, sys, glob
vid = sys.argv[1]
files = sorted(glob.glob(f"/mnt/files/tx_{vid}*.vtt"))
raw = open(files[0], encoding="utf-8").read()
out, prev = [], ""
for block in re.split(r"\n\n+", raw):
    m = re.match(r"(\d\d):(\d\d):(\d\d)\.\d+ --> ", block)
    if not m:
        continue
    text = " ".join(l for l in block.split("\n")[1:] if l and "-->" not in l)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text).replace("&nbsp;", " ")).strip()
    if not text or text in prev:
        continue
    out.append(f"[{int(m.group(1))*60+int(m.group(2)):02d}:{int(m.group(3)):02d}] {text}")
    prev = text
open(f"/mnt/files/transcript_{vid}.txt", "w").write("\n".join(out))
print(len(out), "linhas;", sum(len(x) for x in out), "chars")
EOF
cat /mnt/files/transcript_${VID}.txt
```

Um `429` em uma das faixas de idioma é normal quando há várias; a primeira faixa gravada basta.
Se nenhum `.vtt` aparecer, tente `--sub-lang "all"` e leia o erro impresso; se o vídeo não tiver
legenda automática, avise o usuário que a transcrição não existe em vez de inventar.

Vídeos longos geram texto acima do limite do tool result. Nesse caso, leia em fatias com
`sed -n '1,300p'` ou filtre por minuto com `grep '^\[1[0-9]:'`.

## Passo 3: frame em um minuto exato (sandbox do Composio)

Baixe só uma janela de poucos segundos em 720p e extraia o quadro com `ffmpeg`. `T` é o timestamp
em segundos. Vários timestamps: uma janela por timestamp, mesmo comando em loop.

Use `player_client=default` aqui, não a lista `android,web_embedded,tv` da transcrição: esses
clients só expõem o formato 18 (640x360), e em 360p o texto de uma IDE ou slide fica ilegível.
O bloco confere a resolução e cai para os outros clients só se o `default` falhar.

```bash
cd /mnt/files && VID=kbR8goTbJS0 && T=280 && which ffmpeg >/dev/null || apt-get install -y -qq ffmpeg >/dev/null 2>&1
S=$((T-2)); E=$((T+2)); URL="https://www.youtube.com/watch?v=$VID"
timeout 150 yt-dlp -q --no-warnings -f "bv*[height<=720][ext=mp4]/bv*[height<=720]/b[height<=720]" \
  --download-sections "*${S}-${E}" --force-keyframes-at-cuts \
  --extractor-args "youtube:player_client=default" \
  -o "clip_${VID}_${T}.%(ext)s" "$URL" 2>&1 | grep -i error
ls clip_${VID}_${T}.* >/dev/null 2>&1 || timeout 150 yt-dlp -q --no-warnings -f "b[height<=720]/b" \
  --download-sections "*${S}-${E}" --force-keyframes-at-cuts \
  --extractor-args "youtube:player_client=android,web_embedded,tv" \
  -o "clip_${VID}_${T}.%(ext)s" "$URL" 2>&1 | grep -i error
CLIP=$(ls clip_${VID}_${T}.* | head -1)
ffmpeg -loglevel error -y -ss 2 -i "$CLIP" -frames:v 1 frame_${VID}_${T}.png
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 frame_${VID}_${T}.png
```

`-ss 2` porque o clipe começa em `T-2`. Se o `ffprobe` mostrar largura abaixo de 1280, avise na
resposta que o vídeo só oferece baixa resolução para esse trecho.

Quando o quadro tiver texto pequeno (terminal, IDE, planilha), gere recortes ampliados ainda no
sandbox antes de exportar. O ambiente local não tem PIL, ffmpeg nem ImageMagick, então isso só
funciona lá:

```bash
cd /mnt/files && python3 - frame_${VID}_${T}.png <<'EOF'
import sys
from PIL import Image
im = Image.open(sys.argv[1]); w, h = im.size
for name, box in {"left": (0, 0, w//2, h), "right": (w//2, 0, w, h), "center": (w//4, h//8, 3*w//4, 7*h//8)}.items():
    im.crop(box).resize(((box[2]-box[0])*2, (box[3]-box[1])*2), Image.LANCZOS).save(sys.argv[1].replace(".png", f"_zoom_{name}.png"))
print("ok")
EOF
```

Não use OCR para "ver" o quadro: em telas desenhadas à mão ele devolve lixo. O frame precisa chegar
aos seus olhos, e é isso que o Passo 4 faz.

## Passo 4: trazer o frame para o ambiente local e olhar

1. No `COMPOSIO_REMOTE_WORKBENCH`, exporte com o helper pré-carregado. Vários arquivos, um
   `upload_local_file` por arquivo, na mesma célula:

   ```python
   for f in ["/mnt/files/frame_kbR8goTbJS0_280.png", "/mnt/files/frame_kbR8goTbJS0_280_zoom_center.png"]:
       data, err = upload_local_file(f)
       print(f, "->", err or data["s3_url"])
   ```

   O mesmo helper serve para trazer a transcrição limpa (`transcript_<VID>.txt`) como arquivo exato,
   em vez de copiá-la do stdout.

   O link devolvido é curto, em `backend.composio.dev`, e redireciona para um storage assinado que
   expira em 1 hora.

2. Resolva o redirecionamento **dentro do sandbox**, porque o ambiente local não alcança o host
   curto:

   ```bash
   curl -sS -o /dev/null -w "%{redirect_url}\n" "<s3_url>"
   ```

3. No ambiente local, baixe a URL final para o scratchpad e visualize com a ferramenta de leitura
   de arquivos, que renderiza imagens:

   ```bash
   curl -sS -m 30 -o <scratchpad>/frame_<VID>_<T>.png "<url_final_do_storage>"
   ```

4. Entregue o arquivo ao usuário com a ferramenta de envio de arquivos, com `display: render`, e
   descreva o que está na tela: layout, textos legíveis, desenhos, pessoas, elementos de interface.

Se o passo 3 falhar com 403 do proxy também para o storage, pare e explique: o usuário precisa
adicionar `backend.composio.dev` e o host do storage à allowlist de rede do ambiente em
claude.ai/code. Não procure hosts alternativos de upload.

## Formato da resposta

Comece pelo que foi pedido. Depois, nesta ordem, só o que se aplica:

- **Vídeo:** título, canal, data de publicação, duração. Uma linha.
- **Pontos principais:** lista com marcação de minuto `[mm:ss]` para cada ponto, extraída da
  transcrição, na ordem do vídeo. Cite frases do autor quando a palavra exata importa.
- **Tela em mm:ss:** descrição objetiva do frame enviado, separando texto legível de interpretação.
- **Relação com o projeto do usuário** quando pedida: tabela "ideia do vídeo → estado no projeto →
  lacuna", não parágrafos soltos.
- **Como foi obtido:** uma frase dizendo que a legenda e o frame vieram por `yt-dlp` no sandbox do
  Composio, e o que falhou se algo falhou.

## Quando algo sair do roteiro

Leia `references/troubleshooting.md` para erros de `yt-dlp` (429, "Sign in to confirm", vídeo
privado), sandbox reiniciado (arquivos em `/mnt/files` persistem; instalações não), e a lista
completa de becos sem saída com o motivo de cada um.
