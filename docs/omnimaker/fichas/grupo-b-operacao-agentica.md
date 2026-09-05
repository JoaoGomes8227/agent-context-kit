# Extração estruturada — Grupo B (canal Bruno Okamoto)

Fonte: legendas automáticas em português (nomes corrigidos: Okamoto, OpenClaw, Hostinger, Supabase, GBrain, Grok, Claude/Claude Code, human in the loop). Só consta o que está dito nas transcrições.

---

## Zzkl7cYP8q8 | 6 Agentes de IA que Fazem Minha Empresa Faturar 1,5 Milhão por Mês (com 5 pessoas) (2026-07-21)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel Educação | startup que ensina a criar e implementar agentes e empresas agênticas com estrutura de segundo cérebro | não dito | [00:54]
- Ecossistema MicroSaaS | "maior ecossistema de microSaaS do Brasil", +20.000 empreendedores | não dito | [00:50]
- Instalador de agente Hermes | ferramenta que conecta VPS + Telegram + assinatura ChatGPT e instala o Hermes "em 3 cliques / 5 passos"; mesmo instalador dado aos alunos | link na descrição | [16:19] [22:47]
- Hostinger VPS (parceira oficial) | VPS onde ficam todos os agentes dele e dos 20.000 alunos; link + cupom | R$ 44/mês no plano anual com cupom (arredondou para ~R$ 40–47) | [15:44] [17:09]
- Suporte automatizado a alunos | Openclawzinho, Brainzinho e Hubzinho atendem +20.000 alunos no WhatsApp/Telegram | incluso nos cursos | [13:36]
- Hubzinho | novo agente em construção: tutor privado no WhatsApp para cada aluno, vai substituir Openclawzinho e Brainzinho | não dito | [14:41]
- Palestras | trilhas do Startup Summit (27 de agosto) preparadas pela Amora | não dito | [04:15]

### Ferramentas e stack citados
- Claude Code (Fable / Sonnet) | "estação de trabalho" da equipe; sessões com skills; brainstorm e planejamento | [02:35] [05:08] [11:22]
- Hermes | os 6 agentes autônomos da empresa rodam em Hermes | [07:05] [22:07]
- Telegram | interface para manipular múltiplos agentes por áudio/texto | [02:45] [11:22]
- Slack | equipe manipula agentes dentro do Slack ou do Claude Code | [09:21]
- Hostinger VPS (KVM2) | hospeda agentes 24/7; até 3 agentes por KVM2 | [15:42] [16:12]
- ChatGPT (assinatura), Gemini, Qwen | Dexter roda na assinatura do ChatGPT; Gemini para ver vídeo; Qwen para transcrição | [12:23]
- Higgsfield, Notion, ElevenLabs | ferramentas plugadas na operação | [20:45]
- Assinaturas GPT, Claude e Grok | múltiplas LLMs pagas porque "a estrutura se paga" | [20:55]
- Meta Ads | campanhas geridas pelo Léo | [10:45] [15:07]
- iCloud | causa do bug: pasta sincronizada por agente e por iCloud ao mesmo tempo | [01:32]

### Arquitetura de agentes e segundo cérebro
- Dois cérebros | cérebro pessoal da Amora e cérebro da Pixel Educação; Amora orquestra os dois | [03:41] [04:44]
- Skill "cérebro" | ao sentar para trabalhar, o membro roda a skill que faz pull do cérebro e atualiza a estação de trabalho com o contexto mais recente | [05:19] [05:43]
- Arquivos base do cérebro | Daily Notes, Projects, People carregados toda vez que o Claude inicia | [06:07]
- Skill "salve" | ao terminar, joga todo o contexto de volta para o segundo cérebro (arquitetura híbrida) | [06:25]
- Human in the loop | agentes executam tarefas pontuais o dia inteiro, caem para uma pessoa decidir, agente refatora e cruza dados de novo | [07:32] [08:09]
- Sub-cérebros | cérebro "wik" (conteúdo) e outros; cada cérebro é um nível de permissionamento por área/grupo | [08:44] [09:05]
- Léo (orquestrador) | checa diariamente se cérebro está atualizado, faz backup de agentes e cérebro, verifica vazamento de CPF, cartão, token, senha | [09:37] [09:52]
- Dexter multi-LLM | ChatGPT + Gemini (vídeo) + Qwen (transcrição); transcreve concorrentes, extrai hooks, pautas, ângulos; `/wik` abre o cérebro de conteúdo no Claude Code | [12:23] [13:03]
- Agentes de suporte | Openclawzinho (ajuda a construir agentes), Brainzinho (segundo cérebro) no WhatsApp/Telegram; recebem foto, áudio, vídeo | [13:29] [14:29]
- Amora Boss vs Amora Devil | Boss: gestora universal de contexto de todos os negócios, alerta urgências, metas, caixa; Devil: assistente pessoal usada pela família | [10:11] [11:39]

### Frameworks, regras e princípios
- Regra 1: Contexto acima de tudo | "contexto é rei"; cérebro tem que ser vivo; equipe tem hábito de salvar no cérebro senão contexto sai com o funcionário | [17:34] [18:08]
- Regra 2: Autonomia é a escada | agente entra na área para ler → recomendar → agir; humano sempre ajudando a decidir | [18:17] [18:39]
- Regra 3: Skill não testada | agente opera por skills pré-determinadas; não deixar o time montar skills solto | [19:58] [20:13]
- Regra 4: Mínimo de agentes | quanto mais agentes, mais governança, contexto e higienização | [20:26] [15:26]
- Regra 5: Todo agente se paga | tem que gerar economia/produtividade desde o dia 1; se não sabe usar, dá prejuízo | [20:41] [21:19]
- Regra 6: Cuidado com perfeccionismo | "perfeição é o inimigo da operação"; over-engineering custou 2–3 meses | [21:23] [21:50]
- Bônus: menos é mais | poucos agentes superpoderosos | [15:22]
- Cultura vem de cima | sócios usam primeiro | [22:02]
- Agente de verdade toca a operação | não lê e-mail nem cuida de agenda | [02:20] [03:00]
- Não ficar refém de ferramenta | segredo é orquestrar múltiplas ferramentas | [11:32]

### Ideias aplicáveis a uma agência agêntica B2B
- Um cérebro por cliente/área | usar cérebros como unidade de permissionamento para isolar contexto de cada conta | [09:05]
- Agente orquestrador de governança | oferecer "Léo" como serviço: backup, higiene do cérebro, DLP (CPF/cartão/token) diário | [09:37]
- Skills cérebro/salve para onboarding | padronizar entrada e saída de contexto da equipe do cliente para não perder conhecimento | [05:19] [06:25]
- Escada ler → recomendar → agir | metodologia de implantação em empresa que já opera, reduz risco | [18:17]
- Agente de suporte treinado em base de conhecimento | replicar Openclawzinho para clientes com muitos usuários/alunos (20.000 alunos sem 20 pessoas) | [13:36] [14:06]
- Agente de inteligência de conteúdo | Dexter monitorando benchmarks e extraindo hooks para clientes | [12:13]
- Instalador produtizado | setup de agente em 3 cliques como produto de entrada | [16:19]
- Custo mínimo como argumento de venda | VPS ~R$ 44 + ChatGPT ~R$ 100/mês roda um agente | [17:09] [17:23]
- Lição de infra | nunca sincronizar pasta do agente com outra cloud (iCloud) | [01:36]
- Human in the loop como desenho de processo | agente operacional, humano aprova; vender isso como modelo de operação | [07:32]

### Números citados
- Arquivos deletados pelo agente | 2.047 arquivos, 12 projetos em uma noite | [00:00]
- Faturamento | R$ 1,5 milhão/mês | [00:19]
- Equipe | 6 agentes, 5 pessoas (contrataram uma depois) | [07:13] [22:14]
- Crescimento | de R$ 15.000/mês para R$ 1,5 milhão/mês em menos de 4 meses | [22:21]
- Alunos atendidos por agentes | +20.000; precisaria de equipe de 20 pessoas | [13:36] [14:06]
- Ecossistema MicroSaaS | +20.000 empreendedores | [00:50]
- Capacidade VPS | até 3 agentes numa KVM2 | [16:12]
- Custos | VPS R$ 44/mês (anual + cupom); ChatGPT ~R$ 100/mês | [17:09] [17:23]
- Tempo perdido em perfeccionismo | 2–3 primeiros meses | [21:33]
- Evento | Startup Summit em 27 de agosto | [04:15]

---

## _1hZ3WVqoNw | Como escalamos pra R$ 1.3M/mês em 45 dias com uma empresa gerida por agentes (2026-04-03)

### Serviços e produtos que o Bruno vende ou oferece
- Minicurso OpenClaw | 2h (depois 3h) ensinando a montar, configurar e implementar OpenClaw; prompts prontos, "nem precisa assistir" | R$ 97 | [00:15] [13:01] [25:30]
- Imersão OpenClaw para Negócios | 2 dias ao vivo: cérebro, skills, criadora de skills, crons, segurança, multiagentes por área, agente de marketing, Openclawzinho | R$ 397; 450 unidades | [29:29] [30:13] [30:26]
- Mentoria 90 dias | 6 encontros ao vivo com os 3 sócios, diagnóstico, plano de ação, acompanhamento individual, grupo de WhatsApp com sócios/funcionários do cliente | R$ 30.000; 10 vagas | [37:00] [37:35]
- E-book "20 cases de aplicação prática de OpenClaw" | oferecido na página de upsell em troca de respostas de pesquisa | grátis mediante formulário | [25:44]
- MicroSaaS Pro | comunidade paga (primeiro produto, 2023) | lançada a ~R$ 250/ano | [06:30]
- Curso Do Zero ao MicroSaaS | primeiro infoproduto (2024) | não dito | [06:44]
- MyGroupMetrics (MGM) | SaaS de data analytics para grupos de WhatsApp | não dito | [08:31]
- Metricaas | SaaS de gestão de MRR e dados financeiros de SaaS | não dito | [08:37]
- Landing page da imersão | 100% feita pelo OpenClaw | 22% de conversão | [29:41] [29:53]

### Ferramentas e stack citados
- OpenClaw | agentes 24/7 no Telegram com memória persistente; base de toda a empresa | [10:41] [26:07]
- Claude / Claude Code | estação de trabalho; mesmo cérebro roda nos dois | [09:35] [40:01]
- Supabase | script diário salva histórico de conversas do Openclawzinho para medir dúvidas | [19:03]
- GitHub | cérebro é um repositório no GitHub | [32:32]
- PostHog, Notion, GoHighLevel, GA, Google Search Console | fontes cruzadas pela Amora em relatórios do SaaS | [12:11] [12:19]
- Meta API | OpenClaw monitora criativos e campanhas | [20:28]
- Telegram | grupo de alunos (migrado do WhatsApp) e grupo dos sócios com o Léo | [19:40] [24:25]
- WhatsApp | 4 grupos lotados em 2 semanas; não escalou | [19:48]
- Claude Max | R$ 1.000 por sócio (x3) + 1 para o Léo; R$ 500 pessoal como fallback | [35:16] [35:36]
- OpenAI plano R$ 1.000 (GPT 5.1 Mini Codex) | roda o Openclawzinho | [35:53]

### Arquitetura de agentes e segundo cérebro
- Amora HQ e Amora pessoal | duas Amoras: chief of staff profissional e pessoal | [11:28] [11:33]
- Openclawzinho treinado no workspace da Amora | usa transcrições de aula como verdade, memória do agente do Bruno como base | [18:15] [18:36]
- Base de conhecimento autoatualizável | conversas salvas no Supabase → dúvidas principais → base atualiza materiais do curso a cada release do OpenClaw | [19:03] [19:16]
- Loop de marketing | Meta API → criativos convertidos em Markdown → mapa de ângulos/hooks/formatos → testes A/B → campanhas "normal" vs "foguete" → skills geram banners → reports ao gestor de tráfego | [20:28] [21:20] [22:55]
- Human in the loop deliberado | não automatizaram 100% (risco de ban da Meta e gestor de tráfego bom) | [23:35]
- Leonardo da Vinci (Léo) | nasceu agente de marketing/copy e virou agente da empresa no grupo dos sócios | [23:59] [24:25]
- OpenClaw dos diretores | cada sócio tem seu OpenClaw + um OpenClaw com permissão geral para debater projetos | [26:34] [27:05]
- Cérebro = repo GitHub com memória persistente | guarda contexto, processos, resultados, base de conhecimento e rotinas; mapa de como agentes leem e guardam | [32:32] [32:43]
- Evolução em 4 estágios | agente pessoal por sócio → agente geral → agente por área (3–4 áreas) → agente por área + master (Léo) | [28:06] [28:28]
- Criadora de skills, crons e camada de segurança | agentes trabalham de madrugada via crons | [30:40] [30:46]

### Frameworks, regras e princípios
- Contexto, rotinas, skills | única coisa que importa; ferramenta é irrelevante | [41:34]
- Segundo cérebro = independência de ferramenta | ferramentas lançam feature por semana; cérebro roda em qualquer uma | [27:18] [39:56]
- Empresa OpenClaw-first / agent-first | agentes em suporte, marketing, administração, operação | [26:07] [28:44]
- Agente como armadura | júnior vira sênior em uma semana com skills | [38:29] [38:46]
- Não cair no hype de "agentes de madrugada" | ganho real é o superpoder da equipe | [38:04]
- IA faz e lembra | conhecimento acumula como juros compostos | [40:41] [40:51]
- Fazer primeiro, vender depois | implementaram na Pixel antes de virar produto | [29:03] [35:02]
- Building public | vídeo freestyle, honesto | [00:37]
- Pesquisa de persona embutida no funil | upsell com e-book em troca de respostas | [25:44]
- "Toda empresa precisa de estratégia OpenClaw" | citação de Jensen Huang (Nvidia) | [41:53]

### Ideias aplicáveis a uma agência agêntica B2B
- Case Walter (aluno Eric Pontes) | agente com 30 endpoints, 8 automações, monitora produção, comercial, financeiro, estoque, RH em 2 semanas — modelo de agente operacional para PME | [13:53] [14:17]
- Mentoria com diagnóstico + plano + acompanhamento | formato de serviço de implantação (R$ 30k / 90 dias) | [37:15]
- Loop de marketing com humano no final | oferecer performance agêntica que entrega reports ao gestor de tráfego do cliente | [23:22]
- Agente de suporte que aprende das conversas | Supabase + base autoatualizável para clientes com muitos usuários | [19:03]
- OpenClaw dos diretores | agente compartilhado do C-level do cliente com visão da empresa inteira | [27:05]
- Cérebro em repo GitHub | entregável padrão: contexto, processos, resultados, base, rotinas | [32:32]
- Vender serviços de IA para empresas | Bruno diz explicitamente que empresas vão precisar dessa estrutura e há oportunidade | [42:38]
- Aplicabilidade até 100 funcionários | já aplicou em empresa de 100; acima disso há compliance extra | [41:05]
- ROI como argumento | R$ 5–6k/mês de IA para R$ 1,3M de receita | [36:06]
- Migração de canal por escala | WhatsApp não escala em grupos; Telegram sim | [19:48]

### Números citados
- Faturamento | R$ 0 → R$ 1,3 milhão em 45 dias (19/02 a 31/03) | [00:27] [02:36]
- Alunos | +7.000 em 45 dias | [00:23]
- Equipe | 5 pessoas: 3 sócios, 2 funcionários | [00:41]
- NPS minicurso | 83; 88 respostas; 88% nota 9–10; 5 detratores | [15:10] [15:19]
- Reel do Rony Meisler | 12.000 comentários, 7.000 likes; R$ 250.000 em 48h; pico ~R$ 90–100k/dia | [16:00] [16:11] [16:54]
- Criativos | 95 em uma semana | [21:46]
- Vendas/dia | R$ 2.000 → 5k → 8k → 10k → 14k → pico R$ 50.000 | [21:55] [22:01]
- Persona | 88% empresários; 3.000 respostas | [25:40] [25:51]
- Imersão | R$ 397; 450 unidades; base de ~5.000; NPS 78 (dia 1) e 71 (dia 2) | [29:36] [30:13] [31:17]
- Mentoria | R$ 30.000; 10 vagas; R$ 240.000 em um dia | [37:00] [37:41]
- Custo de IA | R$ 5–6 mil/mês; Claude Max R$ 1.000 x4 + R$ 500 fallback; OpenAI R$ 1.000 | [35:16] [36:06]
- Receita por headcount | ~R$ 280.000 (1,4M / 5) | [39:00]
- Boca a boca | >30% das vendas; Instagram +30.000 seguidores/mês | [34:24] [34:44]

---

## r7jOicSsUwk | Construí o PAINEL DE CONTROLE da minha empresa inteira com IA (passo a passo). Pt 1. (2026-03-23)

### Serviços e produtos que o Bruno vende ou oferece
- Minicurso OpenClaw | prompts + PRD para jogar no OpenClaw e configurar tudo | R$ 97 | [05:43] [05:51]
- Hostinger VPS (parceria) | link com cupom de desconto | não dito | [06:00]
- MyGroupMetrics (MGM) | SaaS gerido por agente dedicado | não dito | [27:38]
- Mission Control (não vendido) | previsão: todo mundo com agente vai construir seu próprio SaaS de controle | — | [04:01]

### Ferramentas e stack citados
- OpenClaw | 6 agentes em tempo integral; interface por áudio no Telegram | [02:47] [04:38]
- Claude Code | fundação do painel via terminal; `claude --dangerously-skip-permissions` | [12:58] [18:30]
- Codex | alternativa ao Claude Code para conectar no terminal/VPS | [06:15] [32:24]
- Supabase | gestão do que o agente aprende e salva | [04:46]
- GitHub | backup de tudo; clone do Mission Control | [04:49] [16:27]
- Hostinger VPS | todos os agentes; acesso root | [14:10] [14:51]
- Tenacity OS (template de Carlos Azaustre) | base do Mission Control, com escritório 3D | [06:52] [07:14]
- Superpowers (skill) | brainstorm, writing plans, executing plans, subagentes; ativa por default | [09:28] [10:42]
- Tailscale | acesso direto à VPS; substituiu Cloudflare Tunnel | [08:54] [09:05]
- Apify | scraping de dados das redes sociais para tracking de conteúdo (~US$ 30–40/mês) | [21:52]
- Notion, CRM, fluxo de caixa | integrações pedidas ao painel e ao agente da empresa | [03:15] [19:53]

### Arquitetura de agentes e segundo cérebro
- 6 agentes OpenClaw | 4 para pilares profissionais, 1 pessoal (com a esposa), 1 da empresa (CRM, caixa, processos) | [02:47] [03:09]
- Cosa Amora | chefe geral, administra todos os negócios, braço direito | [27:05]
- FLG Amora | agente de conteúdo (50–60% do trabalho): relatórios, redes, repost, texto→carrossel, YouTube→newsletter; muitas skills e crons | [27:14] [27:34]
- MGM Amora | agente dedicado ao SaaS: backend, repo GitHub, bugs, suporte, funil, landing, conversão | [27:38] [27:55]
- Leonardo da Vinci | agente da equipe/sócios conectado a toda a empresa | [28:50]
- Openclawzinho | bot no grupo do minicurso; gerido no Telegram, interface no WhatsApp | [29:25] [29:39]
- Mission Control | kanban de tarefas de agentes, gestão/publicação de conteúdo, métricas de redes e negócios, trends/sinais/ideias | [00:56] [01:16]
- Fluxo de construção | Amora audita template (prompt injection/malware) → PRD → Superpowers brainstorm → Claude Code executa PRD na VPS em 4 chunks (segurança, branding, escritório, deploy) → self-review → Amora itera via áudio mandando prints | [06:35] [07:23] [15:45] [17:22] [20:43]
- Divisão de custo | fundação em Claude Code (menos tokens), continuação via OpenClaw | [12:27] [13:08]
- Backup e resiliência | se der problema, desliga a VPS; tudo salvo no GitHub | [14:20]

### Frameworks, regras e princípios
- PRD antes de construir | 85% do painel saiu de um único prompt por causa do PRD | [07:56] [18:02]
- Auditar template de terceiros | verificar prompt injection e malware antes de instalar | [06:40] [07:12]
- Double check por prompt | não técnico deve pedir ao agente revisar o próprio trabalho e apontar dúvidas | [07:41] [17:22]
- Front-end primeiro → PRD por sessão → backend | agente entende campos e rotas antes de conectar | [30:48] [31:16] [31:38]
- Jornada de agentes | 1 agente até dominar memória, skills, APIs → múltiplos agentes só quando: demanda intensa de uma área, equipe precisa usar, clientes externos | [25:27] [26:51] [28:27] [29:08]
- Usar o agente ao máximo | unificar financeiro, comercial e suporte com relatórios cruzados, não ler e-mail | [25:49]
- Superpowers força planejamento | IA pensa e planeja em vez de só executar | [10:20]
- Telegram para comandar, painel para visualizar | dois níveis complementares | [24:39] [25:06]

### Ideias aplicáveis a uma agência agêntica B2B
- Um agente por conta de cliente | Bruno cita explicitamente "você tem uma agência" como caso de múltiplos agentes | [29:13]
- Mission Control como painel para clientes | dashboard com kanban de agentes, conteúdo e métricas | [00:56]
- Auditoria de segurança de templates/repos | prompt injection e malware como serviço antes de deploy | [06:40]
- Metodologia PRD + Superpowers + Claude Code na VPS | entrega em ~1h30 com PRD bem feito | [15:29] [18:16]
- Tracking de conteúdo do cliente via Apify | performance de 7 dias por post | [21:41] [21:52]
- Acesso seguro à VPS do cliente via Tailscale | substitui tunnel público | [09:05]
- Agente dedicado a produto SaaS | modelo MGM Amora: repo, bugs, suporte, funil | [27:38]
- UX de entrega por áudio + prints | cliente não técnico acompanha e ajusta pelo Telegram | [20:43] [24:55]

### Números citados
- Agentes | 6 em tempo integral | [02:47]
- Tempo com OpenClaw | 40–50 dias; beta tester | [02:05] [05:19]
- Minicurso | R$ 97 | [05:51]
- Execução do PRD | ~1h–1h30 (estimativa da IA: 9h); 4 chunks | [15:29] [15:48]
- Um prompt | 85% do painel | [18:02]
- Consumo | 39% do limite semanal; usou ~15–20%; plano Claude 20x de R$ 1.000 | [23:49] [23:55]
- Apify | ~US$ 30–40/mês | [21:56]
- Alunos no grupo | 3–4.000 | [29:29]
- Conteúdo | 50–60% do trabalho do Bruno | [27:18]

---

## Px18BOPAKhA | Criamos um novo cargo (CCO) que toda Startup deveria ter (passo a passo) (2025-09-30)

### Serviços e produtos que o Bruno vende ou oferece
- MicroSaaS Pro | comunidade paga com +1.000 alunos: curso Do Zero ao MicroSaaS, WhatsApp do Bruno, workshops mão na massa | não dito | [01:30] [07:53]
- Comunidade MicroSaaS (portal) | portal com +15.000 pessoas para feedback de ideias/MVPs, achar sócios | acesso pelo site da comunidade | [09:26] [09:34]
- MyGroupMetrics | microSaaS que mede engajamento de grupos de WhatsApp | não dito | [15:24] [22:09]
- Portfólio de infoprodutos | 3–4: e-book, MicroSaaS Pro, curso, comunidade privada; imersão nova em montagem | não dito | [15:28]
- Conteúdo como canal | YouTube 3x/semana, newsletter 1x, LinkedIn diário | orgânico | [21:41]

### Ferramentas e stack citados
- WhatsApp | grupo pequeno como primeira comunidade + formulário de entrada | [20:26] [20:37]
- LinkedIn, Instagram, YouTube, newsletter | canais do Founder Led Growth | [19:31] [21:41]
- MyGroupMetrics | medir engajamento, não alcance | [22:09]
- (Sem stack de agentes neste vídeo — foco organizacional) | — | —

### Arquitetura de agentes e segundo cérebro
- Sem agentes de IA neste vídeo | estrutura é humana: Caio CEO (estratégia, OKRs, produto, marketing, engenharia), Mateus COO (processos, KPIs, financeiro, jurídico, RH), Bruno CCO | [05:15] [05:26] [05:41]
- Tripé de sócios | CEO / COO / CCO definido em 2025 | [02:37] [03:18]

### Frameworks, regras e princípios
- CCO (Chief Content Officer) | cargo responsável por 90% do faturamento | [00:52] [03:22]
- CCCRR | Conteúdo, Comunidade, Comunicação, Relacionamento com parceiros, Representação institucional | [04:13] [04:26]
- Processo linear de venda | conteúdo → visibilidade → autoridade do fundador → posicionamento → relacionamento → vendas | [14:31]
- Funil ACP | Awareness (histórias/dados) → Community (sonhar junto) → Product | [14:54] [15:02]
- Founder Led Growth (FLG) | storytelling do fundador como motor; case Rony Meisler | [18:33] [19:17]
- 4 razões do CCO vender | visibilidade gera oportunidade; autoridade constrói confiança; relacionamento supera transação; comunidade cria defensores | [13:56] [14:04]
- 4 passos para começar | fundadores primeiro; FLG; comunidade pequena engajada; estratégia consistente | [18:00] [18:33] [19:53] [21:20]
- Estratégia de conteúdo | nicho definido, calendário editorial, autenticidade/building public, medir engajamento | [21:28] [22:01]
- 100 engajados > 10.000 passivos | qualidade das conexões | [20:04]
- Pessoas compram transformações (output) | não produtos | [10:25]
- Confiança é o maior ativo | IA democratizou tecnologia; diferenciação técnica cai | [17:22] [17:34]

### Ideias aplicáveis a uma agência agêntica B2B
- Fundador da agência como CCO | conteúdo do fundador como principal canal de vendas B2B | [03:56] [13:50]
- CCO-as-a-service | oferecer os 5 pilares CCCRR operados com agentes para clientes B2B | [04:13]
- Comunidade pequena no WhatsApp + formulário | captar dados de persona antes de escalar plataforma | [20:26] [20:37]
- Medir engajamento de comunidades de clientes | MyGroupMetrics como ferramenta de prova | [22:09]
- Benchmarks B2B com FLG | Marpin (Ivan Cordeiro), GetDemo (Mateus), Humper (Ricardo Correa) — SaaS B2B vendendo via LinkedIn + comunidade | [16:19] [16:39] [16:56]
- Funil ACP para agência | awareness → comunidade → serviço | [14:54]
- Parcerias estratégicas abrem portas | alguém dedicado a filtrar oportunidades e construir canais | [12:03] [12:17]
- Não montar time comercial de 100 pessoas | autoridade e presença substituem força de vendas | [23:35]

### Números citados
- Startup anterior | ideia em 2014; 35.000 técnicos; CEO ~7 anos; +R$ 4 milhões/ano; saída em 2022 | [00:00] [00:17] [00:27] [00:43]
- CCO | 90% do faturamento | [00:55] [13:50]
- MicroSaaS Pro | +1.000 alunos | [01:36]
- Bolha microSaaS | 80% do conteúdo do Brasil; teto em janeiro/2025 | [02:08] [02:15]
- Portal da comunidade | +15.000 pessoas | [09:34]
- Comunidade | 100 engajados > 10.000 passivos; migrar plataforma com ~1.000 | [20:04] [20:48]
- Cadência | YouTube 3x/semana, newsletter 1x, LinkedIn diário | [21:41]
- Tempo empreendendo | +12 anos | [05:57]

---

## ND4ck6N7c3s | O uso mais avançado de agentes de IA que eu já vi (e como chegar lá) (2026-07-23)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel Educação | ensina empreendedores e executivos a construir e implementar agentes | não dito | [01:25]
- Pixel Hub | hub onde alunos aprendem a implementar agentes; área de aluno na Hotmart via API | não dito | [04:18] [04:29]

### Ferramentas e stack citados
- OpenClaw | onde começou a jornada com a Amora | [03:34]
- Hermes e OpenClaw | agentes autônomos no segundo cérebro; Hermes tem comando `go` | [06:40] [12:09]
- Claude / Claude Code | estação de trabalho; comando `/loop` | [06:40] [12:16]
- Codex / ChatGPT | inteligência alocada ao contexto do negócio | [07:19]
- Hotmart API | agente lê onde alunos estão, aulas assistidas, faturamento, onde travam | [04:32] [04:46]
- Telegram | comandar agente por áudio; agendar relatório às 9h | [04:05] [05:08]
- E-mail, WhatsApp e ferramentas | agente plugável em qualquer lugar | [05:12]
- LLMs citadas | Kimi 3, Minimax, GLM, ChatGPT — tokens cada vez mais baratos | [15:37]
- GitHub | exemplo: Claude faz deploy, outro agente revisa o repositório | [17:36]

### Arquitetura de agentes e segundo cérebro
- 5 degraus | chatbot → agente assistente pessoal → empresa agêntica (segundo cérebro) → agent loops → maestro das IAs | [02:10] [03:15] [05:40] [09:14] [13:22]
- Segundo cérebro | contexto de toda a empresa: decisões, tickets, reuniões, ferramentas; onde múltiplos agentes operam | [06:12] [06:31]
- Agentes por área num só cérebro | financeiro, comercial, jurídico, suporte, todos conectados | [08:00] [08:12]
- Human in the loop | agente constrói → humano revisa → aprova/reprova → agente continua | [09:48] [10:11]
- Agent loop | mesmo ciclo, mas quem revisa é outro agente; precisa de muitos exemplos do resultado esperado | [10:18] [11:16]
- Loop precisa de 6 coisas | objetivo, contexto, ferramentas, critério de pronto, limite, quando escalar ao humano | [12:40] [12:54]
- Semáforo de atenção | verde: agente executa e registra; amarelo: outro agente revisa e aprova; vermelho: humano obrigatório | [17:22] [17:40]
- Maestro | agentes pesquisando, construindo, revisando, orquestrando e monitorando outros agentes/skills/automações em paralelo | [13:39] [13:52]
- Relatório agendado | dado da Hotmart todo dia às 9h | [05:06]

### Frameworks, regras e princípios
- Gargalo de cada degrau | nível 1: prompts; nível 2: manutenção/governança; nível 5: atenção | [03:00] [05:24] [14:32]
- "Gargalo virou token, agora é atenção" | Peter Steinberger (criador do OpenClaw) | [14:32]
- Humano não sai do loop | só muda onde intervém | [16:30]
- Maestro não toca todos os instrumentos | define onde coloca atenção; não pode revisar tudo | [17:07] [17:11]
- Loop bem instruído | "corrija todos os testes da pasta; não altere a API pública" em vez de "arruma meu projeto" | [12:22]
- Sem critério de pronto agente declara vitória cedo; sem escalada toma decisão irreversível | [12:57]
- 5 passos para subir de nível | processo recorrente; tirar contexto da cabeça para uma pasta; definir "pronto" (artefato, teste, o que não pode quebrar); escolher autonomia (verde/amarelo/vermelho); multiplicar agentes | [18:29] [18:54] [19:11] [19:33]
- Jornada do empreendedor | 1 pergunta; 2 delega; 3 contexto compartilhado; 4 objetivos e provas; 5 administra frota e protege atenção | [19:45]
- Novo papel do humano | decidir produto, aprovar código, criar contexto, arquitetura, restrições, guardrails | [17:51] [18:05]
- Empresa pequena surfa melhor | até ~100 funcionários com flexibilidade | [08:57]

### Ideias aplicáveis a uma agência agêntica B2B
- Diagnóstico por degrau | vender migração do nível 1–2 para o 3 como projeto de ~3 meses | [08:40]
- Segundo cérebro por cliente com agente por área | financeiro, comercial, jurídico, suporte no mesmo contexto | [08:00]
- Semáforo como governança contratual | definir com o cliente o que é verde, amarelo e vermelho | [17:22]
- Critério de pronto + escalada como escopo | especificar artefato, teste, o que não pode quebrar | [18:54] [19:02]
- Agente revisor como controle de qualidade | nível amarelo: um agente revisa o trabalho de outro antes do cliente | [17:32]
- Integrar plataforma do cliente via API | exemplo Hotmart → relatório diário automático | [04:41] [05:06]
- Loop de 6 elementos como template | objetivo, contexto, ferramentas, pronto, limite, escalada | [12:40]
- Vender proteção da atenção do CEO | filas de decisão que só trazem o que exige humano | [00:43] [15:19]
- Usar `go` (Hermes) e `/loop` (Claude) | mecanismos concretos de execução autônoma | [12:09]

### Números citados
- Código da Anthropic feito por IA | 80% | [00:00] [17:49]
- Degraus | 5 | [00:31]
- Tempo para chegar ao degrau 3 | ~3 meses (6 a 12 conforme tamanho) | [08:40] [08:49]
- Tamanho de empresa ideal | até 100 funcionários | [09:01]
- Elementos do loop | 6 | [12:40]
- Níveis de atenção | 3 (verde, amarelo, vermelho) | [17:22]
- Passos práticos | 5 | [18:26]
- Relatório diário | 9h da manhã | [05:08]

---

## Síntese do grupo B

1. O ativo central é sempre o **segundo cérebro** (repositório GitHub com contexto, processos, resultados, base de conhecimento e rotinas), não a ferramenta — "contexto, rotinas, skills" repete em 4 dos 5 vídeos.
2. Arquitetura recorrente: agente pessoal/chief of staff (Amora) → agentes por área → agente master/orquestrador (Léo) que faz governança, backup e checagem de vazamento.
3. **Human in the loop** é desenho deliberado: agentes fazem o operacional, humano aprova; evolução natural é agente revisando agente (semáforo verde/amarelo/vermelho).
4. Implantação sempre gradual: ler → recomendar → agir; 1 agente até dominar, múltiplos só com demanda, equipe ou clientes externos.
5. Stack fixa: Hostinger VPS 24/7 + Telegram como interface por áudio + Claude Code como estação de trabalho + OpenClaw/Hermes como agentes autônomos + Supabase/GitHub para memória e backup.
6. Skills padronizadas (cérebro, salve, Superpowers) e PRD antes de construir são o mecanismo de qualidade; "skill não testada" e over-engineering são os riscos nomeados.
7. Modelo de negócio em escada: minicurso R$ 97 → imersão R$ 397 → mentoria R$ 30.000, todos vendendo o que a própria empresa já implementou (dogfooding).
8. Custo de IA baixo (R$ 5–6k/mês, VPS R$ 44) frente a receita de R$ 1,3–1,5M/mês com 5 pessoas — ROI é o argumento comercial recorrente.
9. Suporte a milhares de alunos por agentes treinados em transcrições, com base de conhecimento que se autoatualiza via Supabase.
10. Marketing como loop de dados: monitorar Meta API → extrair padrões de criativos → gerar variações por skills → humano (gestor de tráfego) decide.
11. Conteúdo do fundador (CCO, Founder Led Growth, funil ACP, comunidade pequena e engajada) é o motor de vendas mesmo antes dos agentes — e depois vira agente (Dexter/FLG Amora).
12. Gargalo evolui de prompts → manutenção/governança → tokens → **atenção humana**; o papel do humano passa a ser decidir, definir "pronto", limites e guardrails.
