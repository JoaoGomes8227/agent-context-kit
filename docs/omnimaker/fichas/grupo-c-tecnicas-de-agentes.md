# Extração estruturada — Grupo C (canal Bruno Okamoto)

Fonte: legendas automáticas em português (nomes corrigidos: Okamoto, OpenClaw, Hostinger, Supabase, GBrain, Grok, Claude/Claude Code). Só consta o que foi dito nos vídeos; minutos em [mm:ss].

---

## FtRSGEm4gKQ | Meus agentes aprendem sozinhos. Eu só gravo a lição. (2026-08-16)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel Educação | empresa que faz deploy de agentes de IA em empresas e ensina empresários a criar estrutura agêntica | preço não dito | [01:36]
- Pixel AI Hub | curso/comunidade: criar agente, aplicar em todas as áreas, time + agentes, segundo cérebro da empresa | link na descrição; +25.000 alunos em 4 meses | [11:37]
- Agentes Léo da 20 e Dexter prontos | serão liberados dentro do AI Hub para os alunos | incluso no AI Hub | [21:04]
- Skill "wick" (radar de pautas) | liberada dentro do AI Hub | incluso | [21:01]
- Hostinger VPS KVM2 (afiliado) | hospedagem dos agentes | ~R$40/mês, 12 meses, 30 dias de reembolso, cupom "Bruno Okamoto" +10% | [25:28]
- Instalador | ferramenta para instalar agente na VPS | link na descrição | [26:59]
- Vídeo passo a passo de instalação de agente | tutorial no YouTube | gratuito | [26:52]

### Ferramentas e stack citados
- Claude Code | /loop; CLAUDE.md como lugar do lessons learned; roda a skill "wick" | [03:15]
- Hermes | motor por trás da Amora; /goal; cria skills por padrão a partir de loops | [08:44]
- OpenClaw e Codex | outros lugares onde criar o lessonslearned.md | [29:49]
- Telegram | interface da Amora, Léo e Dexter; Dexter também no Slack | [07:17]
- Meta Ads API (graph token) | Léo da 20 cria e gerencia campanhas | [13:16]
- Excel + Google Drive | lista de criativos apontando para a pasta de vídeos | [15:17]
- OpenRouter + Gemini 2.5 Flash | fazer o agente "assistir" o criativo em vídeo | [15:46]
- Grok (x search) | Dexter busca trending no X por palavra-chave | [19:55]
- YouTube (métricas) | Dexter tira snapshot diário dos vídeos por 7 dias | [23:14]
- Hostinger KVM2 (Ubuntu 24) | hospeda todos os agentes, ~2 GB RAM por agente | [25:35]

### Arquitetura de agentes e segundo cérebro
- Amora = chief of staff | agente geral que manipula todos os agentes e a agente pessoal; roda no Telegram via Hermes | [07:56]
- Quatro tipos de loop | turno (checklist), objetivo (/goal, /loop), tempo (schedule) e autoaprendizado | [02:56]
- Nível 1 (Amora) | humano dá feedback negativo → arquivo lessons learned; lição que reincide 3x vira lei no Soul | [09:17]
- Onde salvar | CLAUDE.md (podar sempre) ou lessonslearned.md carregado por padrão no Soul/Tools/agents a cada sessão | [09:38]
- Nível 2 (Léo da 20) | analisa campanhas e criativos no Meta; extrai ângulo, formato, tempo de visualização, hook, cliques; salva lesson por criativo em markdown | [13:07]
- Fábrica de criativos | 1x/semana cria 50-90 criativos em cima do que funciona (15 variações de hook, estático ou copy) | [16:56]
- Nível 3 (Dexter) | stalkeia benchmarks no YouTube e X, extrai hook/ângulo/formato/modelo; snapshot diário 7 dias dos vídeos do Bruno (retenção, cliques, engajamento, comentários) → lessons de conteúdo → cria com a estrutura que funciona | [19:13]
- Skill "wick" | carrega benchmarks das últimas 24h + segundo cérebro de conteúdo → pautas quentes e ideias de carrossel | [20:37]
- Dexter produtor | gera carrosséis (estilo paper draw etc.), transforma podcast/vídeo em carrossel automaticamente | [22:09]
- Case Untangle (Ryan Carson) | paralegal "Grace", 5 VMs Claude em paralelo, self-improvement loop sobre conversas vira backlog + production watchdog | [28:14]

### Frameworks, regras e princípios
- Loop de autoaprendizado | executa tarefa, aprende com o resultado, automelhora o loop | [00:35]
- Loops "frios" | turno/objetivo/tempo rodam até sucesso ou X tentativas, mas não ficam mais inteligentes | [03:54]
- "Lição que reincide três vezes vira lei" | entra no Soul como regra inegociável | [10:37]
- Cérebro entulhado ignora regras | lições antigas vão para arquivo morto | [10:33]
- Aprendizado → contexto → regra → outputs melhores | cadeia do quarto loop | [25:07]
- "O ativo não é o agente, é o histórico de lições" | dado proprietário que ninguém copia | [30:21]
- Comece pelo loop manualmente | erro repetido duas vezes sem lição escrita é uma escolha | [30:29]
- Criatividade > técnica | barreira técnica não existe mais | [04:33]
- Pergunta prática | qual processo repetitivo eu preciso aprovar todo dia? Vire lição aprendida | [29:09]
- Regra final | crie lessonslearned.md em qualquer ferramenta e peça para salvar o que aprendeu | [29:44]

### Ideias aplicáveis a uma agência agêntica B2B
- Loop nível 1 como entregável | feedback do gestor do cliente vira regra no Soul do agente dele | [09:17]
- Gestor de tráfego agêntico | relatório por criativo com receita, gasto, ROAS, tendência e ação (pré-escala/monitorar/manter/cancelar) | [13:44]
- Fábrica semanal de criativos | 50-90 variações derivadas do que já performa | [16:56]
- Loop nível 2 em outras áreas | propostas comerciais, transcrições de vendedores, suporte | [17:57]
- Agente que assiste vídeo | Gemini via OpenRouter para extrair hook/ângulo dos criativos do cliente | [15:46]
- Snapshot diário de métricas do cliente | 7 dias por peça → lições editoriais | [23:14]
- Vender dado proprietário | histórico de lições como ativo defensável do cliente | [30:21]
- Hospedagem de agentes | 3 agentes por VPS de R$40 | [25:41]
- Modelo Untangle | nicho vertical + dado proprietário + fluxo completo; conversas alimentam backlog | [27:55]
- Radar diário de benchmarks | skill tipo "wick" para marketing do cliente | [20:37]

### Números citados
- Startup ERD vendida após 8 anos | [01:24]
- Ecossistema microSaaS | +25.000 empreendedores | [01:30]
- Pixel AI | +20.000 alunos | [01:52]
- AI Hub | +25.000 alunos em 4 meses | [12:06]
- Criativos novos por semana | 50 a 90; 15 variações por tipo | [16:58]
- Copy do Léo | 6 agentes 24/7, 11 agentes, 35 tarefas, montar em 3 horas | [16:33]
- Snapshot Dexter | 1x/dia por 7 dias | [23:12]
- VPS | 2 GB RAM/agente, R$40/mês, 3 (até 4) agentes, cupom 10% | [25:38]
- Ryan Carson | 110 funcionários → 1; Treehouse 1 milhão de alunos; 50x output; 5 VMs; receita 4x/mês | [27:15]
- Gemini | 2.5 Flash | [15:53]

---

## HaDJONsfua0 | O que é Graph Engineering? A técnica por trás do funcionário digital (2026-08-09)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel Educação | empresa agêntica; ensina criar agentes autônomos e fazer deploy em empresas | preço não dito | [01:28]
- Masterclass Hermes | vídeo de 1h no YouTube para criar agente autônomo | gratuito | [11:39]
- Conteúdo do canal como formação | "estude os conteúdos no meu canal" para virar profissional de IA | gratuito | [22:56]

### Ferramentas e stack citados
- Hermes | agente autônomo; /goal; crons; subagentes; roda com Codex | [06:15]
- Claude Code | /loop; rotinas; executar processo passo a passo (nível 2) | [13:07]
- Codex | executor em paralelo com Claude | [06:07]
- Claude Opus / Fable | agente "cético" que avalia o trabalho | [06:25]
- Kimi, GLM | LLMs alternativas para paralelizar até 5 LLMs | [07:21]
- n8n, Make, Zapier | processos lineares; orquestração externa no nível 3 | [02:13]
- Hotmart API | loop diário de receita, alunos, faturamento e reembolso → Excel de fluxo de caixa | [14:49]
- Excalidraw | desenhar o processo (nível 1) | [18:29]
- Slack | interface do Dexter para criação de roteiros | [13:52]
- OpenClaw | agente autônomo recomendado junto com Hermes | [20:31]

### Arquitetura de agentes e segundo cérebro
- Graph engineering | plano com etapas paralelas + agente cético (outra LLM) refuta → loop refaz → gate humano | [05:17]
- Escada de uso | prompt → chat → loop → graph | [11:54]
- Um agente com subagentes | preferível a muitos agentes: mais agente = mais manutenção | [05:43]
- Cético com "norte" | sabe o que é bom/ruim sem ditar output exato | [06:45]
- Dexter: rotinas | +30 cadastradas, 17 pausadas, 13 ativas; captação (X, notícias, Instagram, métricas), transformadores, auditores, manutenção, relatórios | [15:52]
- Destilação da wiki | time joga pautas, agente analisa, dá veredito e nota | [16:21]
- Fluxo do Dexter | fontes → evidências → ideia → score → backlog → produção → publicação → performance → aprendizado → wiki | [17:13]
- Gates humanos no Dexter | seleção editorial, copy, direção visual, peça final, divulgação, mudança estrutural, refutação, incidente externo | [17:51]
- Loop Hotmart | diário via API, alimenta relatórios de múltiplas áreas | [15:31]
- Agente autônomo + graph | memória persistente e autoaprendizado dão autonomia real ao "funcionário" | [20:42]

### Frameworks, regras e princípios
- Prompt vs contexto vs graph | pedir com contexto / contexto alimentado automaticamente / trabalho que se move ponta a ponta | [03:38]
- "Quem faz não avalia, quem avalia não assina, quem assina é você" | separação de papéis | [07:41]
- Teste dos 6 pontos | múltiplos passos, múltiplas fontes, paralelo, checks 0-10, risco, etapa do humano | [08:25]
- Sem clareza nos 6 → back to basics | prompt + contexto + rotinas + skills | [10:17]
- Skill / rotina / contexto | atividade predeterminada; execução no horário; insumo para decidir | [10:48]
- Três níveis de construção | desenhar processo; rodar na mão com Claude/Codex dando notas; orquestrar com automações e checkpoint | [18:25]
- "Dexter opera sozinho dentro dos trilhos" | humano define intenção, aceita risco, autoriza consequências externas | [18:00]
- Ferramenta não é o foco | criatividade dos fluxos | [07:31]
- Papel do empresário | sair do operacional para tático/estratégico; orquestrador de agentes | [21:33]
- Empoderar, não demitir | tirar equipe do Excel e realocar horas | [22:24]

### Ideias aplicáveis a uma agência agêntica B2B
- Camada "cético" como QA | LLM diferente avaliando output do agente do cliente com rubrica 0-10 | [06:05]
- Teste dos 6 pontos como diagnóstico | decidir se processo do cliente merece graph ou prompt+rotina | [08:25]
- Oferta em 3 níveis | mapear processo → piloto manual com IA → orquestração | [18:25]
- Loop financeiro | API do gateway alimenta dashboards diários do cliente | [14:49]
- Pipeline editorial com score e backlog | modelo Dexter para marketing de clientes | [17:13]
- Gates humanos explícitos no contrato | o que o cliente aprova e o que o agente decide | [17:51]
- Um agente + subagentes | menor custo de manutenção na operação do cliente | [05:43]
- Posicionamento | devolver 5h/dia de Excel à equipe do cliente | [22:38]
- Revisão de contratos por agente | insights do que não faz sentido | [21:49]
- Consultoria em graph engineering | conhecimento vendável como profissão do futuro | [23:27]

### Números citados
- MicroSaaS | +25.000 empreendedores | [01:25]
- Anthropic | +80% do código feito por IA (Boris) | [02:48]
- Uso de IA como chat | 95% a >99% da população | [12:26]
- Dexter | +30 rotinas, 17 pausadas, 13 ativas | [15:52]
- LLMs em paralelo | até 5 | [07:25]
- Escala de avaliação | 0 a 10 | [09:27]
- Horizonte de mudança | ~2 anos | [21:22]
- Tempo em Excel | 5 horas/dia | [22:38]
- Masterclass Hermes | 1 hora | [11:39]

---

## iRc6QwYmHDI | Heartbeat em agentes de IA: pare de brincar com prompts e construa sistemas (2026-05-10)

### Serviços e produtos que o Bruno vende ou oferece
- Minicurso de OpenClaw | ensina heartbeat, soul, arquivo hot, montar agente | "preço de dois cafés" | [29:14]
- Crisp (patrocinador) | plataforma que centraliza redes e suporte; Magic Reply com base de conhecimento | usa há +1 ano | [05:57]
- Canal | conteúdo sobre SaaS, microSaaS, IA e agentes | gratuito | [01:01]

### Ferramentas e stack citados
- OpenClaw | roda a Amora; heartbeat e soul | [05:43]
- Hermes | roda o Dexter | [14:28]
- Claude Code (computador) | segunda área de trabalho; skill "sync pessoal" | [14:19]
- Antigravity | editor para abrir o arquivo heartbeat | [08:11]
- Notion | tarefas, deadlines; tudo vira registro | [09:19]
- E-mail e calendário | Amora tem visão 360 da vida digital | [09:21]
- Telegram e Slack | inbox da Amora; gatilho "salva isso" | [22:47]
- Crisp | suporte e redes sociais unificadas com IA | [06:20]
- Git (bash git) | sincronização do cérebro sob demanda | [23:37]
- Session spawn (OpenClaw) | dispara até 6 subagentes | [23:49]

### Arquitetura de agentes e segundo cérebro
- Agente = modelos + ferramentas + orquestração | com três características: contexto, skills, rotina | [01:26]
- Heartbeat | arquivo markdown; agente acorda a cada 1h; sensor de urgência; silêncio se nada a fazer | [06:49]
- Heartbeat da Amora | lê heartbeat state (JSON) + deadlines; alerta prazos 24/48h, reunião externa em 2h, falha crítica, tarefa bloqueando dinheiro, material em risco (Projects) | [08:43]
- "O que não fazer" | não auditar 80 automações, não revisar projetos inteiros, sem fire and forget, sem histórico longo, sem resumo repetido | [11:31]
- Arquivos Pending, Hot, Projects, People | markdown alimentados por skill de save ao fim da sessão | [13:32]
- Skill "sync pessoal" | propaga sessão do Claude para pendências, decisões, pessoas, projetos, métricas, skills, mapas; mesma lógica na Amora | [14:40]
- Delegação via arquivo Hot | back-end atualiza hot → front-end acorda e lê → QA; agentes se comunicam pelo mesmo arquivo | [16:57]
- Soul da Amora | toda atividade recorrente vira skill; checa skill antes de executar; inbox wiki ingest (URL/"salva isso") auditada de madrugada | [22:02]
- Subagentes | session spawn até 6; usam skills existentes; sem skill, escalam ao humano | [23:41]
- Ao acordar | lê identidade, alma, memória → arquivos enxutos para poupar tokens; rodapé mostra modelo e % de contexto | [20:44]

### Frameworks, regras e princípios
- Contexto + skills + rotina = agente | [05:06]
- Deixar a IA perguntar | gera contexto melhor do que ditar o que fazer | [02:59]
- Skill | passos em markdown para o mesmo output; "transforma tudo que aprendeu numa skill" | [04:11]
- "Funcionário 24/7 é lorota" | agente acorda a cada 1h | [07:00]
- Heartbeat minimalista | tarefa concluída sai do hot; menos tokens, menos interrupção | [28:30]
- Alma rasa = trabalho mediano | detalhar tom, comportamento, regras e limites | [21:11]
- Como ela pensa | viés para ação, discordar antes de construir errado, certeza calibrada, get shit done: plano → execução verificada → confirmar resultado | [24:34]
- Mudanças cirúrgicas | não melhorar código adjacente, não inventar documentação, não refatorar o que funciona; lê → checa → pesquisa → pergunta só se travar | [25:13]
- Regras de prioridade | destrava receita > evita risco > protege prazo > reduz caos > aumenta alavancagem | [25:43]
- Tom de voz | nunca abrir com "great question", nunca fechar com "precisa de mais algo", brevidade, opiniões fortes, sem emoji | [26:04]

### Ideias aplicáveis a uma agência agêntica B2B
- Heartbeat como monitor de gargalos | avisa o gestor do cliente: prazos, reuniões, bloqueios de receita | [09:30]
- Follow-up automático de key accounts | sem contato há 7 dias → agente age na batida | [16:30]
- Pipeline multiagente com handoff por arquivo | dev → design → QA dentro da própria agência | [16:57]
- Soul padronizada como entregável | tom, regras e prioridades de cada agente do cliente | [21:52]
- Inbox wiki ingest | cliente joga links/áudios; auditoria noturna categoriza no segundo cérebro | [22:42]
- Suporte omnicanal com IA + base de conhecimento | modelo Crisp Magic Reply | [06:20]
- Skill de sync de sessão | continuidade entre Claude Code e agente operacional | [14:40]
- Lista de "o que não fazer" | controle de custo de tokens em agentes de clientes | [11:31]
- Alerta de falha crítica de infra | agentes monitoram a própria saúde | [10:05]
- Rodapé de modelo/contexto | transparência operacional para o cliente | [27:27]

### Números citados
- Heartbeat | a cada 1 hora | [00:04]
- Deadlines | próximas 24/48h; reuniões nas próximas 2h | [09:47]
- Automações do Bruno | +80 | [11:46]
- Subagentes simultâneos | até 6 | [23:50]
- Key account sem follow-up | +7 dias | [16:46]
- Crisp | uso há +1 ano | [06:03]
- Minicurso OpenClaw | preço de dois cafés | [29:16]
- Inbox wiki | ~15 itens/dia (exemplo) | [23:10]
- Alma da Amora | alguns meses para construir | [27:47]

---

## 1uiVsGUutBk | Pare de testar toda ferramenta de IA: use este combo (2026-06-18)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel Educação (edtech) | alunos com dúvidas recorrentes; empresa AI first | preço não dito | [02:03]
- AI Hub | comunidade/produtos: primeiro agente, segundo cérebro, empresa agêntica, agentes top-down | link na descrição | [07:20]
- Masterclass Hermes | vídeo de 1h15 para montar agente Hermes | gratuito | [07:08]
- Composio como padrão do Pixel AI Hub | recomendação oficial para alunos | [14:57]

### Ferramentas e stack citados
- Claude / Claude Code / Claude agents | orquestrador no app e no terminal; skill "cérebro"; conectores MCP | [09:55]
- Hermes | roda a Amora; Claude CLI instalado dentro | [19:04]
- OpenClaw | Guilherme despacha agentes OpenClaw e Hermes via Claude por SSH na VPS | [11:41]
- GitHub | segundo cérebro sincronizado | [10:16]
- Codex | assinatura principal de cognição | [22:44]
- Composio | uma conexão (API/CLI/MCP) para todas as ferramentas; SDKs Vercel AI, Claude Agents | [14:28]
- HubSpot API | exemplo: "leia a documentação desta API e instale" | [13:25]
- Meta Ads, Google Ads, Analytics via CLI/API | report de campanhas | [20:44]
- Canva, Figma, Higgsfield, Perplexity, Grok, Crisp | design, vídeo, pesquisa, X, suporte | [21:50]
- GitHub, Vercel, Supabase, Notion | desenvolvimento e SaaS de apoio | [22:13]

### Arquitetura de agentes e segundo cérebro
- Trio | tools (mãos), cognition (cérebro), skills (procedimentos) | [00:44]
- Três degraus | chat → agentes com mãos (Telegram) → empresa agêntica AI first onde organograma desaparece | [05:04]
- Segundo cérebro no GitHub | backup inteligente em camadas para agentes, humanos e qualquer IA; skill "cérebro" carrega tudo | [09:58]
- Fluxo bidirecional | tudo do Claude vai para a Amora e vice-versa; workstation + celular | [11:18]
- Forma B (Guilherme) | Claude via SSH na VPS despacha agentes usando assinatura ChatGPT | [11:39]
- "Claude Code constrói a frota; agentes operam a frota" | construção e operação são coisas diferentes | [12:07]
- Ferramenta = API, CLI ou MCP | API crua, CLI transparente no terminal, MCP padroniza mas servidor quebra | [12:20]
- Skill orquestradora "nave mãe" | campanhas ativa skills filhas de pesquisa, copy, design, ajuste | [18:49]
- Hermes + Claude CLI | agente usa assinatura Claude para planejar campanhas; report com receita, gasto, CPA, ROAS, tendência, recomendação | [20:09]
- Frota | Amora (chief of staff controla cognition/tools/skills), Dexter (conteúdo), Guilherme (Claude na VPS) | [26:13]

### Frameworks, regras e princípios
- "Cérebro decide, mãos executam, skill repete. Só muda a peça" | [19:51]
- Erro comum | apostar tudo em uma ou duas ferramentas; fanboy | [03:12]
- Problema não é falta de ferramenta | é não saber montar as que existem | [04:30]
- Prefira API ou CLI a MCP | performa melhor | [14:18]
- Criar skill | "pega tudo dessa sessão e transforma numa skill chamada report financeiro" | [18:19]
- Fatiar skills | skill longa vira várias menores; ter 8 skills é ok | [18:37]
- Verificação de sucesso explícita | números batem, design certo, e-mail enviado | [17:43]
- ROI em horas compradas de volta | não em custo | [24:10]
- Comece com um combo, não 20 agentes | 20 carros exigem 20 manutenções | [27:27]
- "Não converso com a frota, rejo a frota" | [26:09]

### Ideias aplicáveis a uma agência agêntica B2B
- Diagnóstico do degrau do cliente (1-2-3) | ponto de entrada da venda | [05:04]
- Composio como camada única de integrações | evita reconectar auth a cada troca de agente | [15:36]
- Skills documentadas como receita vendável | report financeiro, campanhas | [18:19]
- Report de mídia paga por agente | ROAS, tendência, recomendação manter/monitorar/escalar | [20:49]
- Padrão de integração | "leia a documentação desta API e instale" com chave do cliente | [13:41]
- Separar build e run | Claude Code constrói, agentes operam; dois contratos | [12:07]
- Segundo cérebro em GitHub para o cliente | camadas para humanos e agentes | [10:16]
- Precificar em horas devolvidas | ROI em tempo do time do cliente | [24:19]
- Empresa agêntica | suporte, operação e comercial na mesma equipe | [06:20]
- Orçamento de referência | R$3-4 mil/mês em cognição + ferramentas vs ~40h devolvidas | [25:02]

### Números citados
- Empreendedor | +15 anos | [01:36]
- Codex | R$1.000/mês; Claude R$500 (era R$1.000) | [22:44]
- Higgsfield R$700; Anthropic R$500; OpenAI R$1.000; APIs de scraping R$200-300/mês | [22:58]
- Report Meta | R$31.000 receita ontem, R$15.000 gasto | [20:56]
- ROAS | 5,67 (R$1 → R$5,67) | [21:31]
- Etapas para acertar | 3 ou 4 | [17:05]
- Gasto total em cognition + tools | R$3-4 mil/mês | [25:02]
- Tempo devolvido | ~40 horas (exemplo com hora a R$1.000) | [24:25]
- Masterclass Hermes | 1h15 | [19:19]

---

## sNKRYUip4zA | Qual IA usar pra cada tarefa? Essa pergunta tá errada (2026-07-02)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel AI Hub | curso/comunidade: criar agente, aplicar em áreas, time + agentes, segundo cérebro | +25.000 alunos em 4 meses; link na descrição | [20:52]
- Hostinger VPS (afiliado) | VPS para rodar Hermes | R$43/mês; ~R$44/mês em 12 meses com cupom | [12:45]
- Composio como recomendação oficial da trilha do AI Hub | [21:30]

### Ferramentas e stack citados
- Hermes | maestro; 4 camadas de memória; skills que se autoatualizam; /goal | [01:29]
- Claude Code (Claude CLI) | instalado dentro do Hermes/Dexter; apresentações; revisar código | [13:55]
- Codex | motor da Amora; código; cruza com output do Claude | [11:13]
- Grok CLI | leitura em tempo real do X; subagentes Researcher, Code Reviewer, Critic, Builder | [16:00]
- Agent Browser (CLI) | acessar o X sem Grok | [16:25]
- Antigravity CLI | Gemini para sites/landing/protótipos; rodar Opus | [18:20]
- NotebookLM CLI (repo do Jacob) | estudar links, PDFs e vídeos | [19:00]
- Composio (composio.dev) | 1000+ apps numa única chave API; CLI; free tier | [20:36]
- Hostinger VPS Ubuntu | terminal sem interface onde o Hermes roda | [12:26]
- Telegram | áudios para o agente no Uber | [11:01]

### Arquitetura de agentes e segundo cérebro
- Maestro | Hermes orquestra ferramentas; Claude como orquestrador do Hermes em paralelo | [01:29]
- IA = funcionário super inteligente | contexto traz o "sabe tudo" para a bolha do negócio | [03:37]
- Self learning loop | curadoria ("sonhar") + memória persistente; agente que lê notícias vira especialista em 1 ano | [04:39]
- Hermes | 4 layers de memória / 4 sistemas de busca cruzando dados | [05:57]
- Skills autoatualizáveis | Hermes salva sozinho; OpenClaw exigia pedir | [07:27]
- Human in the loop → agents in the loop | agente usa Claude, revisa o resultado, /goal até satisfatório | [08:24]
- Amora orquestradora | usa Codex e Claude debaixo do capô | [11:08]
- Instalar Claude CLI no agente | pedir link de auth e remover chave API | [14:31]
- Cross-check | Codex bate com o que o Claude criou: duas LLMs, duas visões | [15:38]
- Subagentes por função | apresentação, brainstorm, conselheiro; cada um com CLI específica | [22:43]

### Frameworks, regras e princípios
- "Maestro não toca cada instrumento; sabe quem chamar, quando e para quê" | [03:02]
- Problema = excesso sem coordenação | não falta ferramenta | [02:01]
- Amor pelo resultado, não pela ferramenta | [09:50]
- Por que agente tem mais autonomia | labs vendem para corporações e não podem liberar autonomia | [09:55]
- Skill | atividades repetitivas que exigem o mesmo resultado | [06:15]
- "Um prompt, três especialistas" | [23:22]
- Criatividade e orquestração > conhecimento técnico | [23:15]
- 3 passos | mapeie cada peça antes de plugar; use só onde há ROI claro; humano é o critério final | [25:43]
- Evite orquestrar por hype | maestro não faz mágica; só monte se trouxer dinheiro | [25:54]
- Budget mensal para testar ferramentas | assina, testa, cancela | [25:29]

### Ideias aplicáveis a uma agência agêntica B2B
- Vender o "maestro" | agente que orquestra CLIs em vez de vender ferramenta | [02:52]
- Cross-check entre LLMs | Codex revisando Claude como QA de entregas | [15:38]
- Radar de mercado via Grok | trending do X → apresentação automática para o time do cliente | [17:44]
- Subagentes especializados | researcher, critic, reviewer, builder como time virtual | [16:59]
- NotebookLM CLI | estudar materiais do cliente e gerar apresentação | [19:25]
- Composio | reduzir horas de integração; funciona em Hermes, OpenClaw, Codex e Claude | [20:40]
- Agente especialista do setor | leitura diária de notícias com memória persistente | [05:18]
- Argumento de venda | ~R$2.700/mês equivale a cinco sêniores | [26:27]
- Agents in the loop | camada filtrada que reduz decisões do humano | [15:31]
- Segurança | auth por link, remover chaves API dos agentes | [14:42]

### Números citados
- Operação | 7 dígitos em <4 meses com equipe "de duas pizzas" | [01:03]
- Ferramentas conectáveis | +1.500 | [07:50]
- Hermes | 4 camadas de memória | [06:00]
- VPS Hostinger | R$43/mês; ~R$44/mês em 12 meses | [12:45]
- Grok | plano ~R$100 | [16:53]
- Composio | +1.000 apps | [20:42]
- AI Hub | 25.000 alunos em 4 meses | [21:24]
- Higgsfield | R$1.000 por 2 meses (teste) | [25:31]
- Gasto mensal | R$2.000-2.700 | [26:27]
- Hipótese | 10-20 clientes = 80% do faturamento dos labs | [10:08]

---

## tXAH78b0Sms | A IA que organiza o caos do WhatsApp: 85.000 msg viraram um dashboard (open source) (2026-06-26)

### Serviços e produtos que o Bruno vende ou oferece
- Pixel AI Hub | carro-chefe; ensina empreendedores a colocar agentes nas empresas | link na descrição | [04:23]
- Okamoto Sinal WhatsApp | dashboard open source no GitHub | gratuito | [18:20]
- Replit (afiliado/recomendação) | ferramenta usada para construir | plano de US$20 | [19:41]
- Controle de missão (interno) | painel para administrar os agentes da empresa, feito no Replit | [02:52]

### Ferramentas e stack citados
- Replit | construir dashboard; agent multi-agente; até 4 pessoas simultâneas | [01:38]
- n8n | recebe WhatsApp via API não oficial e joga no Supabase; MCP do n8n | [14:10]
- W-API (API não oficial do WhatsApp) | conexão do número | [14:22]
- Supabase | tabelas de contatos, grupos, convites, mídias, login Google; API e MCP | [14:38]
- Claude | criou tabelas e estrutura; MCP do Claude conectável ao dashboard | [15:10]
- Hermes (Amora) | processa mensagens diariamente e salva no segundo cérebro | [15:37]
- GitHub | repositório e documentação | [13:22]
- Conector Google | não testado/funcionando | [12:55]

### Arquitetura de agentes e segundo cérebro
- Fluxo | WhatsApp → n8n → Supabase → dashboard (front-end) e Hermes/Amora diário → segundo cérebro | [13:49]
- Overview | msgs privadas em 7 dias, enviadas, áudios, tarefas, volumetria, busca, top pautas, temas em grupos, VIPs | [03:16]
- Privado | volume/dia, tempo médio de resposta (break às 20h, fim de semana não conta), convites, pendências 7/14/30 dias | [05:35]
- Kanban | triagem de convites e pendências | [06:52]
- Grupos | pautas que cruzam grupos, score por pauta, grupos ativos, excluir grupos de suporte/oferta | [07:18]
- Menções | palavra-chave de pessoa/produto/outros; tag de elogio | [09:11]
- Mini CRM | contato equipe/VIP, métricas, primeira/última interação, pautas, análise IA, links, tasks com due date | [10:38]
- Amora | processa 51 conversas/dia, match com "people" do segundo cérebro; aprovação manual de novos | [15:57]
- Dashboard só front-end | Supabase é a fonte única; enriquece contatos e monta cockpit | [16:57]
- Montagem | MCP do n8n + API em 20-30 min; Supabase em 30 min; total ~1h | [18:54]

### Frameworks, regras e princípios
- "Jogue repositório + transcrição no Claude e peça um PRD" | forma de replicar | [18:27]
- Fonte de dados única | dashboard e agente consomem a mesma base | [00:21]
- Gestão do que devo às pessoas | pendências viram tasks associadas a contatos | [12:11]
- Excluir ruído das métricas | grupos de suporte/oferta fora | [08:51]
- Aprovação humana | quem entra no segundo cérebro é aprovado pelo Bruno | [16:36]
- Open source colaborativo | convite a commits e perspectiva externa | [13:22]
- Não técnico constrói com IA | integração feita via Claude e MCP | [18:49]

### Ideias aplicáveis a uma agência agêntica B2B
- "Sinal WhatsApp" como produto | para comerciantes e lojistas que fazem suporte no WhatsApp | [20:16]
- Social listening em grupos | menções de marca, tag de elogio, trending → pautas de conteúdo | [09:11]
- Mini CRM automático | gerado a partir do WhatsApp com tasks e pendências | [10:38]
- Métrica de SLA | tempo médio de resposta para equipes de atendimento | [05:41]
- Pipeline n8n → Supabase → agente | replicável para qualquer canal do cliente | [13:49]
- Resumo diário no segundo cérebro | agente registra contexto de cada contato | [15:37]
- Controle de missão | painel de frota de agentes construído com a equipe | [02:52]
- MVP rápido | ~US$251 no Replit + 1h de integração | [20:02]
- Recomendações de venda a partir das conversas | feature ainda a evoluir | [09:53]
- Build colaborativo | até 4 pessoas no mesmo projeto Replit | [02:41]

### Números citados
- Mensagens processadas | 85.000 | [13:34]
- Enriquecidas com IA | ~1.000 das 85.000; custo baixo | [17:29]
- Mensagens por semana | 1.090 | [12:20]
- Grupos | 1.800 mensagens resumidas; 1.200 por pauta | [07:49]
- Conversas processadas em 18/06 | 51 | [16:04]
- Replit | plano US$20; gasto total US$251 (~R$1.000) | [19:57]
- Uso do Replit | +1 ano | [01:49]
- Tempo de montagem | 20-30 min n8n; 30 min Supabase; 1h total | [19:00]
- Filtros | 7/14/30 dias | [06:11]
- Pessoas simultâneas no Replit | até 4 | [02:41]

---

## Síntese do grupo C
- Stack recorrente: Hermes como "maestro" (Amora), OpenClaw, Claude Code/CLI e Codex como executores, Grok para o X, tudo na VPS Hostinger; Composio surge em 2 vídeos como camada única de integrações.
- Tríade repetida em todos os vídeos: contexto (segundo cérebro em GitHub), skills (markdown que garante o mesmo output) e rotina/heartbeat (autonomia).
- Toda repetição vira skill; toda correção vira lição; lição reincidente vira lei no Soul — o ativo é o histórico de lições, não o agente.
- Loops evoluem: prompt → chat → loop (/goal, /loop) → graph com agente "cético" e gate humano; use só se passar no teste dos 6 pontos.
- Humano define intenção, aceita risco e assina; agente opera "dentro dos trilhos" e escala quando falta skill.
- Preferência por API e CLI sobre MCP; instalar ferramenta é "leia a documentação e instale"; auth por link, sem chave API no agente.
- Um agente com subagentes (até 6) em vez de muitos agentes; começar com um combo, não 20 agentes.
- Custo é tema constante: tokens do heartbeat, assinaturas (R$2-4 mil/mês), ROI medido em horas devolvidas.
- Casos internos servem de vitrine de produto: Léo da 20 (tráfego), Dexter (conteúdo), Sinal WhatsApp (dados), depois liberados no AI Hub.
- Dados proprietários alimentam o segundo cérebro: WhatsApp, Hotmart, Meta, YouTube, X — fonte única para dashboard e agente.
- Monetização: Pixel AI Hub (25.000 alunos em 4 meses), minicurso OpenClaw, afiliados Hostinger/Replit/Crisp, Composio como recomendação oficial.
- Discurso: criatividade e orquestração valem mais que técnica; empresário sai do operacional e empodera a equipe em vez de demitir.
