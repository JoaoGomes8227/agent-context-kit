# Extração estruturada — Grupo A (canal Bruno Okamoto)

Fonte: legendas automáticas em PT-BR dos três vídeos abaixo. Nomes corrigidos (Okamoto, OpenClaw, Hostinger, GBrain, Grok, Claude/Claude Code). Tudo o que está aqui foi dito nas transcrições; minutagens em [mm:ss] (vídeo 2 passa de 60 min e usa [mm:ss] contínuo, ex. [65:22]).

---

## TSimMWwR6to | Abri o jogo: meu setup de agentes de IA em negócios, conteúdo e casa (2026-08-30)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel Educação | empresa que ele constrói desde 2026, "crescendo absurdamente" com múltiplos agentes | preço não dito | [01:25]
- Instalador de Hermes da Pixel Educação | deploy completo do Hermes na VPS, com Telegram ligado e agente configurado; feito para alunos, aberto a todos | R$ 30 | [10:00]
- Link/cupom de VPS Hostinger (afiliado) | VPS KVM2 no plano de 24 meses com cupom | R$ 39/mês | [08:50], [09:04]
- SaaS de WhatsApp | SaaS próprio só de WhatsApp, ~25 números | preço não dito | [07:16]
- Curadoria de trilhas no Startup Summit | responsável por duas trilhas inteiras (MicroSaaS e IA) no maior evento de startups do Brasil | não é venda direta | [27:46]
- Publis e palestras | contratos de publi (uso de imagem), cachê, hotel, viagens gerenciados pela Amora | preço não dito | [44:37], [46:26]
- Conteúdo futuro sob demanda | vídeo dedicado do Dexter e vídeo sobre arquitetura de cérebros "se comentar" | gratuito (YouTube) | [15:56], [25:53]

### Ferramentas e stack citados
- Hermes | chassi principal dos agentes, self-hosted; migrou do OpenClaw por volta de maio/junho; nunca precisou de manutenção | [02:06], [04:22], [06:57]
- OpenClaw | usado antes; incomodava: atualizações quebravam, memória "falhada", respostas em fila (não conectava mensagens seguidas) | [02:44], [03:06], [03:22]
- Roncho + GBrain | duas camadas extras de memória: Roncho injeta personalidade/contexto em toda sessão; GBrain faz pesquisa semântica e indexa arquivos | [05:02], [16:46], [16:56]
- Hostinger VPS KVM2 | hospeda todos os agentes; 8 GB RAM, 100 GB; ~2 GB por agente; tem mais de 15 VPS lá | [08:43], [09:11], [09:50]
- GitHub | segundo cérebro (não usa Obsidian); "feito para agentes" e funciona para equipes; aceita Claude, Codex, Antigravity, ChatGPT, Grok Bot no mesmo cérebro | [10:48], [11:16]
- Grok 4.6 | LLM favorita no Hermes (muito rápida); limite acaba rápido, por isso duas contas do plano 300 | [19:03], [19:38], [19:59]
- Codex (ChatGPT) | ~8 agentes rodando; cota generosa; gera imagem final dos carrosséis; Amora pessoal roda em GPT 5.6 | [21:51], [24:51], [27:15]
- Composio.dev | plugar 1500 ferramentas numa única chave API (X, Instagram, YouTube, LinkedIn, e-mail, calendário) | [22:54], [23:07]
- OpenRouter (Qwen 3.8 e Gemini 3 Flash) | Qwen como segunda LLM no app do Hermes; Gemini para o Dexter "assistir" vídeos | [40:05], [41:18]
- Higgsfield, Hotmart API, Omie, Autentique, banco via MCP, Slack, Figma, Tailscale | geração de vídeo; gestão de alunos; financeiro/NF; assinatura de contratos; finanças pessoais; equipe no Slack; mockup de carrossel; SSH remoto do app na VPS | [41:37], [42:37], [44:04], [45:05], [47:01], [22:14], [24:47], [38:05]

### Arquitetura de agentes e segundo cérebro
- Squad de 3 agentes principais | Amora Boss (chefona dos negócios), Dexter (conteúdo), Amora Devil (pessoal); Amora Boss tem subagentes on demand | [07:27], [07:44], [08:07]
- VPS fatiada em três | uma "casa" com um quarto por agente: Amora, Dexter, Amora pessoal | [10:22], [14:48]
- Um cérebro por agente e um por empresa | Dexter tem o cérebro "Content"; Pixel Works e Pixel Educação têm cérebros próprios; Amora faz commits em todos | [11:44], [13:13], [14:07], [14:22]
- Interseção entre cérebros | pastas compartilhadas entre Amora pessoal e profissional (viagens, palestras, brainstorm/produtos) | [12:06], [12:32]
- mapa.md | arquivo-índice que explica cada cérebro: Amora é Master Brain com acesso a "irmãos" (Content, Pixel etc.), pasta agents, palestras | [12:55], [13:09], [13:41]
- Ledger | sumário/índice de contexto captado de WhatsApp, transcrições de reuniões, Slack, e-mails, calendário; dá contexto rápido à Amora | [16:10], [16:28]
- Permissionamento define fatiamento | fatiar VPS/cérebro só quando há níveis de acesso diferentes (ex.: cérebro dos sócios vs cérebro da equipe) | [14:33], [15:39]
- Bots do Hermes | agentes independentes que dividem o mesmo cérebro, mas com ferramentas, skills, MCPs e soul diferentes (Amora Crítica, Amora Designer); invocados por @ na sessão principal e "voltam a dormir" | [32:50], [33:19], [37:05], [37:26]
- Loop extra de autoaprendizado | ao fim de cada skill, uma linha de prompt manda reanalisar o output e sugerir melhoria na skill | [26:11], [26:31]
- Memória do Hermes | 3 camadas nativas; skills não usadas ficam em standby aos 30 dias e vão para pasta Archive aos 90 | [04:56], [05:34]

### Frameworks, regras e princípios
- Tríade Skills + Contexto + Rotinas | tudo que você faz vira skill; contexto é rei; rotinas automatizam (última etapa) | [48:26], [49:12], [49:53]
- "Tudo que você pede é uma skill" | criar skill conscientemente, mesmo o Hermes criando sozinho; fatiar skills longas e orquestrar | [48:14], [06:05]
- Mapa de skills | criar mapa do que faz cada skill e pedir ao agente para manter atualizado; dashboard de skills | [48:55], [51:58]
- Contexto é rei | guardar contexto no próprio cérebro, não entregar à Anthropic/Codex; gravar até consulta médica | [49:25], [50:39], [50:54]
- Menos é mais | menos agentes = menos manutenção; um super agente que chama outros por @ | [51:10], [51:34]
- Criatividade > técnica | não-técnico vai do 0 ao 2; precisa de técnicos do 2 ao 5 | [52:07], [52:39]
- Não seja fã de empresa | Codex se usa muito (limite grande), Grok se tem grana, Claude para trabalhar no desktop | [52:59], [53:23]
- Hermes é chassi, LLM é cérebro | sem LLM boa o app não funciona bem | [18:19], [39:43]
- Soul cirúrgico | define o que o agente NÃO faz, quando bloquear, onde trabalha; "TDAH: três coisas por vez, priorizar receita, risco e prazo" | [34:19], [34:50], [35:15]
- Não gaste sem saber ganhar | só compre IA para ganhar dinheiro ou tempo; aprende-se pondo a mão na massa | [20:59], [54:31]

### Ideias aplicáveis a uma agência agêntica B2B
- Radar em grupos de WhatsApp | agente lê grupos de suporte/vendas/mentoria, identifica pautas para o dono se manifestar e extrai dados (tópicos, volume de mensagens) — vendável como "inteligência de comunidade" | [29:11], [29:42], [30:01]
- Follow-up operacional em grupo | agente cobra stakeholders diariamente e marca quem já entregou — aplicável a onboarding e coleta de materiais de clientes | [28:08], [28:50]
- Agente crítico ("diretoria virtual") | soul que sabatina ideias, revisa PRDs e decisões caras — oferta de revisão estratégica automatizada | [34:05], [34:41]
- Agente designer com branding pack | soul carrega sistema visual, fontes, cores, exemplos de capas — replicável por cliente | [35:32], [35:49]
- Pipeline de conteúdo ponta a ponta | benchmark viral, mapear formatos/hooks/CTAs, métricas em tempo real, carrossel via Figma + Codex, vídeo via Higgsfield | [40:40], [41:10], [42:06]
- Backoffice agêntico | NF, cobrança, fluxo de caixa, faturas ao contador, skill de análise de contrato com red/yellow flags e envio ao Autentique | [43:44], [44:53], [45:05]
- Jornada de clientes via API da plataforma | medir % de avanço por etapa e onde alunos se perdem (Hotmart) — serviço de retenção | [43:15], [43:33]
- Argumento de ROI | R$ 3.200/mês em LLM equivale a 3–4 pessoas; 3 pessoas a R$ 5.000 = R$ 15.000 + encargos | [20:10], [20:38], [20:50]
- Produtizar o deploy | instalador one-click por R$ 30 — modelo de setup pago e replicável | [10:00]
- Segurança prática | dar e-mail e calendário próprios ao agente em vez de acesso total; modelo por tarefa (Grok rápido, Codex pesado, Gemini vídeo) | [23:55], [19:00], [41:18]

### Números citados
- Trajetória | startup vendida em 2022; 4 anos de ecossistema MicroSaaS; agentes desde 2026 | [01:11], [01:20]
- Migração OpenClaw → Hermes | ~2 meses antes (maio/junho) | [02:16], [02:25]
- VPS KVM2 | 40 reais/mês; 24 meses; R$ 39 com cupom; 8 GB RAM; 2 GB/agente; 3–4 agentes; 100 GB | [08:37], [09:04], [09:14], [09:30]
- Frota | mais de 15 VPS Hostinger; SaaS com ~25 números de WhatsApp | [09:50], [07:19]
- Instalador | R$ 30 | [10:10]
- Uso de Claude | menos de 30% do limite semanal usado | [17:50]
- Lentidão do Codex | 40 min para tarefa boba; carrossel de 10 etapas leva até 3 horas | [18:37], [18:50]
- Grok | 88% do limite semanal com 5 dias faltando; 2 contas do plano 300 = R$ 3.200 | [19:21], [19:31], [20:11]
- Assinaturas | Claude plano 1K, Codex plano 1K, 2× Grok 3,2K; ~8 agentes rodando no Codex | [21:23], [21:51]
- Composio | 1500 ferramentas | [22:58]
- Startup Summit | 2 trilhas; prazo 20/07; palestras dias 27 e 28 | [27:51], [28:37], [28:43]
- Skills | standby 30 dias, arquivo 90 dias | [05:34]

---

## mU06NTyBsS8 | 7 passos obrigatórios para usar o Hermes e criar agentes que trabalham por você (guia completo) (2026-06-02)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel AI Hub / Pixel Educação | hub que ensina criar agente, segundo cérebro, permissionamento, governança e segurança para empresa agêntica; +500 alunos em menos de um mês | link nos comentários; preço não dito | [29:27], [29:40], [29:48]
- Marketing OS | estrutura que faz marketing ponta a ponta (criativos, anúncios, orgânico); "versão do Dexter" exclusiva para alunos do Hub | incluso no Hub | [29:59], [30:08]
- Minicurso de Claude | dentro do Hub | incluso | [30:17]
- Minicurso de OpenClaw (openclaw.pixeleducacao) | templates, starter kit, compact agendado por cron, memory flush ativado em 70% | "de graça" | [37:52], [38:05], [38:22]
- Soul 4.0 da Amora | arquivo do soul para download e adaptação | grátis na descrição | [46:25], [46:41]
- Template de apresentação HTML feito com Claude Code | usado como template dos vídeos; material disponibilizado | grátis | [10:46], [46:42], [74:47]
- Cupom Hostinger "Bruno Okamoto" | 10% de desconto na VPS KVM2 | afiliado | [54:55], [55:26]
- Vídeo "zero a R$ 1,3 milhão em 45 dias" | case da operação com OpenClaw | gratuito | [02:01]

### Ferramentas e stack citados
- Hermes (Nous Research) | agente "que cresce com você"; self-hosted na VPS via Docker one-click da Hostinger | [14:32], [14:57], [56:26]
- Apify + Grok Premium (assinatura do X) | Apify puxa YouTube/Instagram/Reddit via API; Grok Premium para scraping do Twitter | [04:29], [04:35], [71:39]
- Granola | transcrição de reuniões enviada ao Dexter para virar ideias de conteúdo | [11:08], [11:15]
- Claude Code CLI dentro do Dexter | instalado num canal para brainstorm de pauta e para gerar apresentações HTML | [10:32], [71:04]
- Telegram (tópicos) + Bot Father | canal recomendado; tópicos trending/inbox/ideias/hot ideas/AI news/config; criação do bot | [03:43], [53:21], [63:19]
- GitHub vs Obsidian | GitHub "feito para agentes" e B2B; Obsidian mais bonito, "para humanos" | [24:29], [24:40]
- OpenRouter | ranking de apps: Hermes em 1º, 3–4× o uso do OpenClaw | [17:30], [18:00]
- Tailscale + Hostinger MCP | acesso seguro à VPS e gestão de agentes; MCP faz cópia/backup diário da VPS | [47:52], [57:10], [57:36], [57:52]
- 1Password / Bitwarden | senhas, tokens, ENV e dados sensíveis fora do agente; universal entre Hermes, OpenClaw, Claude | [67:10], [67:22], [67:42]
- Firecrawl, Perplexity, transcripts, scrapers, OpenClaw como auditor | Firecrawl transforma site em Markdown (grátis); OpenClaw audita o Dexter | [71:27], [71:29], [71:57]

### Arquitetura de agentes e segundo cérebro
- Dexter = camada operacional de conteúdo | canal trending (X, Reddit, YouTube, Instagram, filtrado por viralidade), Inbox com score 0–100, Ideias (75–85), Hot Ideas (>85), AI News | [02:43], [04:13], [05:15], [05:37], [05:48]
- Score de fit | cada pauta recebe nota, tier (Tier B = roteiro antes), qualidade do radar, fontes e fit com Bruno/Pixel | [06:59], [07:06], [07:21]
- Tópicos por pessoa | Dexter Bruno, Dexter Beatriz (social media), canal de configuração | [08:39], [08:45], [09:03]
- Loop de feedback com nota | equipe avalia report; automação diária trabalha as notas até mínimo 8,5; score por fonte | [09:14], [09:43], [09:59]
- Skill master "Bruno Content OS" | arquivo core que dita a governança inteira do Dexter | [11:37], [11:48]
- Segundo cérebro corporativo | conteúdo, pautas, tickets, decisões, faturamento; inbox por agente/pessoa; agente Léo audita o inbox diariamente, distribui em pastas e pergunta quando não sabe | [23:14], [23:41], [25:58], [26:08]
- Cérebro pessoal da Amora | contexto, projetos, sessões, integrações, track, skills categorizadas; opera em Claude, VPS, "todos os lugares" | [23:51], [24:08]
- Skill "cérebro" no Claude | lê Notion, e-mails e carrega o segundo cérebro ("cérebro ligado, vamos trabalhar"); contexto universal entre Claude e Dexter | [27:43], [28:06], [29:15]
- Memória 4 camadas do Hermes | daily notes em Markdown, peer cards (memória social por pessoa: tom, preferências), fuzzy index (busca), prompt cache de 1h (−40% tokens) | [30:36], [31:35], [32:12], [32:30]
- Worker memory review + compactação | lê a conversa e decide o que guardar; threshold 0.5 compacta cedo, 0.9 arrisca context overflow; recomenda 0.8; Amora compactou com 136–140k de 272k | [34:45], [35:11], [36:19], [36:50], [37:16]
- Self-evolving skills | tudo vira skill automaticamente e é atualizada com correções; preocupação com milhares de skills em 12–18 meses | [41:13], [42:57], [43:28]
- Soul em 4 camadas | identidade (quem é, o que faz, para quem), contrato de runtime (onde vive, fonte de verdade, dono), como pensa, tom de voz | [45:49], [46:03], [46:16]
- Gateway/dashboard | sessões, modelo por tarefa (ex.: Opus só para skill de alta qualidade), logs, crons, skills, plugins via repo GitHub, perfis, chaves, Kanban | [48:33], [48:48], [49:38], [50:45], [51:26]
- Sem heartbeat; crons em linguagem natural | Hermes não tem heartbeat do OpenClaw (60 min); rotinas criadas por comando natural; rotinas: varredura de fontes com score, digest operacional, checagem de conectores, social matrix, newsletter capture, daily notes, weekly | [68:49], [69:18], [69:49], [70:12]
- Agente de governança | um OpenClaw via Hostinger MCP + Tailscale audita ~8 agentes: crons rodando, skills funcionando | [68:06], [68:23], [68:33]

### Frameworks, regras e princípios
- Tríade Contexto + Skills + Rotina | contexto = dados (reuniões, WhatsApp, e-mail, ERP, CRM); skills = processos repetitivos precisos; rotina = automações | [25:04], [25:29], [26:52]
- Agente entra em estrutura que já funciona | "se a estrutura é bagunçada, ele automatiza bagunça" | [12:03], [12:14]
- 4 etapas de implantação | ler → revisar (relatório do que melhorar) → relatórios cruzando ferramentas e áreas → pequenas automações com skills | [12:30], [12:46], [13:00], [13:15], [13:28]
- Gamification para agentes | nota e score em tudo para que se autoavaliem e autoevoluam | [09:32], [10:19]
- Ferramenta não importa; o jogo é arquitetura | funcionalidade é commodity; não trocar de agente por hype | [18:39], [19:26], [21:22]
- Papéis | OpenClaw acelera execução; Hermes estabiliza continuidade; Claude Code aprofunda técnico; segundo cérebro preserva contexto | [19:34], [21:32]
- Memória é infraestrutura de continuidade | "IA sem memória é um estagiário novo todo dia" | [40:09], [40:20]
- Regra no Soul: repetiu, virou skill | tarefa repetitiva (2–3 vezes) vira skill automaticamente | [44:03], [45:30]
- Tratar o agente como funcionário | 1 agente por VPS, Docker, e-mail e calendário próprios, acesso granular (Drive, CRM, Stripe, Slack; nunca admin) | [65:22], [65:29], [65:51], [66:17], [66:45]
- Autonomia sem governança é risco automatizado | segredos no 1Password, não no agente | [68:02], [67:01]
- Comece com um agente útil | ambiente, VPS, canal, base, duas skills; "sem visibilidade não tem operação, tem suspense" | [74:36], [53:33]

### Ideias aplicáveis a uma agência agêntica B2B
- Radar de tendências com score de fit | Inbox 0–100 cruzando trending, timing, evergreen e fit com a marca — serviço de inteligência de conteúdo por cliente | [04:13], [05:15], [06:33]
- Loop de qualidade com nota | equipe do cliente avalia entregas; automação força nota mínima 8,5 e ajusta o processo | [09:14], [09:55]
- Segundo cérebro por área/diretoria | cérebros de marketing, suporte, logística e diretoria com permissionamento — arquitetura vendável | [27:08], [27:17], [27:31]
- Agente bibliotecário (Léo) | audita o inbox corporativo, arquiva e escala dúvidas — mantém o cérebro do cliente organizado | [26:08], [26:16]
- Metodologia de implantação em 4 etapas | ler, revisar, cruzar, automatizar — roteiro de consultoria de baixo risco | [12:30]
- Agente de governança de frota | monitora crons e skills de todos os agentes — base de um SLA de operação | [68:06], [68:33]
- Marketing OS como produto | Dexter generalizado (criativos, anúncios, orgânico) replicável para clientes | [29:59]
- Modelo por tarefa | GPT 5.5 como padrão, Opus para alta qualidade, Haiku para tarefas específicas — otimização de custo | [48:48], [70:48]
- Segurança/compliance como entregável | VPS por agente, Docker, 1Password, roles específicos, backup diário via MCP | [65:29], [67:10], [57:52]
- Peer cards | memória social por pessoa (tom, preferências) — personalização por stakeholder do cliente | [31:35], [32:04]

### Números citados
- Uso | mais de 100 horas de Hermes | [00:05]
- Ecossistema | 20.000 empreendedores MicroSaaS; 40.000 alunos; equipe de 4 pessoas | [01:24], [02:08], [02:11]
- Case | zero a R$ 1,3 milhão em 45 dias | [02:03]
- Conteúdo | mais de 40% das vendas | [04:03]
- Score | 100 pontos; Ideias 75–85; Hot >85; pauta exemplo 88; 31 fontes do YouTube | [05:15], [05:37], [06:59], [07:48]
- Qualidade | nota mínima 8,5; fontes 5 Twitter / 2 Reddit / 3 YouTube / 6 Instagram | [09:59], [09:43]
- OpenRouter | Hermes 1º, 3–4× o OpenClaw; OpenClaw lançado nov/2025 | [18:00], [15:58]
- Memória | 4 camadas vs 2 do OpenClaw; cache 1h reduz até 40% de tokens | [19:14], [32:33]
- Compactação | threshold 0.5/0.8/0.9; Amora 136–140k de 272k (Codex 5.5); OpenClaw memory flush em 70% | [35:11], [36:21], [36:52], [37:16], [38:30]
- Hub | +500 alunos em menos de 1 mês | [29:40]
- Escala | ~8 agentes rodando; 2 agentes por VPS; preocupação com 2.000–3.000 skills em 12–18 meses | [68:17], [65:34], [43:28]
- Hostinger | cupom 10%; KVM2; 12 meses; latência 134 ms; heartbeat OpenClaw 60 min | [54:55], [55:17], [56:08], [68:56]

---

## W7KqfZPep5o | GROKBOT vs HERMESBOT: qual agente de IA vale a pena em 2026 (2026-09-03)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel Educação | startup onde ensina empreendedores a fazer deploy de agentes Hermes + segundo cérebro e transformar operações em agênticas | preço não dito | [01:09], [01:15]
- Comunidade | "nossa comunidade" onde todos perguntam sobre Grok Bot | não detalhado | [00:08]
- Cupom Hostinger "Bruno Okamoto" | VPS Ubuntu 24.04 no Brasil, plano 12/24 meses | "R$ 950" (período não claro na legenda) | [17:05], [17:13], [17:25]
- Vídeos do canal | vídeo do setup atual e vídeos sobre segundo cérebro (links na descrição) | gratuito | [02:22], [21:23]

### Ferramentas e stack citados
- Grok Bot (xAI) | interface minimalista, agentes conversam entre si, computador na nuvem por agente, app mobile, templates (diretor de marketing, chief of staff), rotinas simples | [03:51], [04:41], [15:30], [18:36], [21:47]
- Hermes Bot | bots com soul próprio, provider/modelo por agente (Codex, OpenRouter, Grok), profiles clonáveis, capabilities (ferramentas, skills, MCPs) | [07:05], [07:23], [07:44], [09:58]
- Hostinger VPS | casa dos agentes: 100 GB, 3 agentes por 40/mês, 24/7 | [16:44], [16:54], [17:02]
- Composio | 1500 ferramentas numa chave API usada no Codex, Claude, Hermes e Grok; sem afiliação | [28:20], [28:32], [28:42]
- GitHub | segundo cérebro; no Grok Bot é preciso especificar pastas por agente | [09:39], [31:05]
- Telegram e Slack | Telegram substitui o mobile; equipe usa Dexter no Slack | [22:07], [35:01]
- Grok (LLM) | favorita do momento, plano de 300; SuperGrok de 30 | [14:14], [21:20], [21:26]
- Claude para Slack (Anthropic) | crítica: salva o contexto do Slack na Anthropic e gera lock-in | [36:48], [36:59]
- Beehiiv + X + Gmail | stack do case Arlington no Grok Bot | [23:21]

### Arquitetura de agentes e segundo cérebro
- Segundo cérebro como camada independente | permite navegar entre Grok Bot, Hermes, OpenClaw, Claude, Codex com o mesmo contexto | [02:14], [03:02], [03:12]
- Soul da Amora Anxiety (redes sociais) | define cérebro, mapa, pastas, arquivos icônicos, "ideia não é roteiro", tom de voz por canal, métricas, doutrina | [07:54], [08:12], [08:26], [08:53]
- Memória | Hermes: mesmo cérebro ou cérebros separados por agente (escolha); Grok Bot: tudo no mesmo cérebro, contexto vaza entre bots | [09:27], [09:34], [23:38], [23:53]
- Capabilities enxutas | desabilitar ferramentas para não encher contexto (500 conectadas → 1–2 para falar de Instagram) | [10:23], [10:35]
- Invocação por demanda | Amora Planner chamada dentro da sessão da Amora principal para organizar viagem/palestra no RJ | [20:05], [20:49], [21:01]
- Bot profile pronto | Grok cria agente conversando; a partir do contexto do dono sugere agentes (radar, lupa, forja, caixa, cortes, orelha, tesouraria) | [12:37], [12:52], [19:08]
- Boss bot | um bot no Grok que cria os outros bots | [24:57]
- Onde mora o contexto | Grok: VM na nuvem que você não controla; Hermes: VPS sua, contexto no profile, skills e GitHub | [15:30], [18:02], [24:37], [31:33]
- Sessões paralelas | Hermes permite abrir várias sessões; Grok Bot é um agente por coisa | [06:07], [06:11]

### Frameworks, regras e princípios
- Contexto é rei / ferramenta vai e vem | segundo cérebro é o que dá flexibilidade | [02:02], [02:35]
- Código é commodity | ganha quem tem distribuição e executa melhor | [05:11]
- Bot sobre processo existente | mais fácil criar bot em cima de processo que já existe do que criar bot para criar processo | [13:00], [13:14]
- Menos agentes | um super agente + @ por demanda; 8 bots conversando é "engenharia adicional sem necessidade" | [34:26], [34:31]
- Não entregue seu contexto | contra ficar refém de fornecedor; lock-in de preço e modelo | [31:43], [36:33], [37:05]
- Um projeto por vez no Grok Bot | limite acaba rápido e contexto mistura | [15:01], [24:15]
- Segmentação | iniciante/resultado rápido → Grok Bot; aprender sistemas ou empresa com time → Hermes | [32:46], [33:34], [34:56]
- Empresários nunca são uma pessoa | multiplayer é obrigatório | [35:45]
- Ferramenta se adapta a você | não você a ela | [37:29]

### Ideias aplicáveis a uma agência agêntica B2B
- Agência como dona do segundo cérebro do cliente | contexto no GitHub do cliente, ferramenta intercambiável — evita lock-in | [02:14], [31:05]
- Segmentar oferta por perfil | Grok Bot para PME simples ("minha mãe, meu tio"); Hermes para empresa com time | [33:06], [34:56]
- Soul completo como entregável | ferramentas, pautas, skills, pastas, doutrina por agente | [08:46], [09:01]
- Case chief of staff de newsletter | 6.000 leitores; pesquisa, vendas e rotinas; substituiu funcionário que saiu | [22:25], [22:36], [22:50]
- Cases x.com/bot | suporte e reembolsos, office manager para pequenos negócios, prospecção de vendas, bot em reuniões, resumo de podcasts, limpeza de e-mails | [26:27], [26:56], [27:22], [27:31]
- Fluxo completo de redes sociais | ideias → lapidar → draft → postar → medir → aprender | [29:23], [29:38], [29:47]
- Outros fluxos | inbox de produto/triagem, diretório, onboarding de clientes | [30:00], [30:07]
- Composio como camada única de integrações | uma chave para todas as LLMs | [28:20]
- Precificação | R$ 300 no Hermes gerencia 3 empresas vs 1 projeto no Grok | [30:25], [30:36]
- Barreira do dólar | Grok Bot sem pagamento em real fecha o cerco às empresas brasileiras — oportunidade para oferta local | [36:22], [36:26]

### Números citados
- Grok | SuperGrok 30; plano de 300 (dólar) | [14:14], [14:26]
- VPS | 100 GB; 3 agentes; 40/mês; "R$ 950" | [16:54], [17:25]
- Composio | mais de 1500 ferramentas | [28:32]
- Ferramentas conectadas do Bruno | 500 | [10:27]
- Post x.com/bot de 19/08 | 33 milhões de visualizações | [25:41]
- Case Arlington | 6.000 leitores, e-mail toda quinta | [22:36]
- Data da análise | 24 de agosto | [12:16]
- Grok Bot | 1–2 projetos por vez ("um, sendo honesto"); "três botões" | [15:01], [33:52]
- Trajetória | startup vendida em 2022 após 9 anos; 4 anos até 2026 | [00:54], [01:01]

---

## Síntese do grupo A
- Tríade repetida nos três vídeos: Contexto (rei) + Skills (tudo vira skill, conscientemente) + Rotinas/crons.
- Segundo cérebro em GitHub, versionado, um por agente e um por empresa/área, com mapa.md, Ledger e permissionamento como critério de fatiamento (VPS e cérebro).
- Squad enxuto: Amora Boss orquestra, Dexter produz conteúdo, Léo audita o cérebro; subagentes/bots com soul próprio invocados por @ e "voltam a dormir" — "menos agentes, menos manutenção".
- Soul é o arquivo mais importante: identidade, contrato de runtime, como pensa, tom de voz, o que NÃO faz.
- Governança como produto: agente entra em processo que já funciona; implantação em 4 etapas (ler → revisar → cruzar → automatizar); agente de governança monitora a frota; segredos em 1Password; e-mail/calendário próprios; acesso granular.
- Loops de autoavaliação: score 0–100 nas pautas, nota mínima 8,5 nos reports, revisão da skill ao fim de cada execução.
- Infra padrão: Hostinger KVM2 (~R$ 40/mês, 3 agentes), Docker, Tailscale, Hostinger MCP para backup; nunca local.
- Multi-LLM por tarefa: Grok 4.6 (velocidade), Codex/GPT 5.5 (cota, tarefas pesadas), Claude (desktop/técnico), Gemini (vídeo); "não seja fã".
- Composio como camada única de 1500 integrações para todas as LLMs.
- Anti lock-in: recusa entregar contexto a Anthropic/xAI; ferramenta é commodity, arquitetura é o diferencial.
- ROI explícito: R$ 3.200/mês em LLM substitui 3–4 pessoas (R$ 15k+); R$ 300 no Hermes gerencia 3 empresas.
- Monetização do Bruno: Pixel AI Hub (+500 alunos), Marketing OS, instalador R$ 30, minicursos, soul grátis e cupom Hostinger.
