# Canal Bruno Okamoto: catálogo de serviços e ideias para a Omnimaker

> Análise do canal [@obrunookamoto](https://youtube.com/@obrunookamoto) feita em 2026-09-05 para orientar a Omnimaker, agência agêntica que opera com agentes de IA e atende clientes B2B. O objetivo é listar tudo que o canal oferece de aproveitável, separando o que fortalece a própria Omnimaker do que pode virar oferta para clientes, para a equipe escolher por onde começar.

## Como a análise foi feita

| Etapa | Fonte | Volume |
|---|---|---|
| Catálogo do canal via API oficial do YouTube (Composio) | 321 vídeos, títulos, datas e descrições | 2022-09 a 2026-09 |
| Links recorrentes nas descrições | produtos, afiliados e comunidades | 20 destinos com 2 ou mais ocorrências |
| Transcrição integral de 19 vídeos de 2025-2026 | legenda automática via `yt-dlp` no sandbox do Composio | ~700 mil caracteres |
| Extração estruturada por vídeo | 4 subagentes, fichas com minuto | 6 seções por vídeo |

Os vídeos transcritos estão listados no fim. Toda afirmação atribuída ao canal tem vídeo e minuto de origem, no formato `[id mm:ss]`.

## Quem é a referência

Bruno Okamoto vendeu uma startup em 2022, construiu o ecossistema MicroSaaS (mais de 20 mil empreendedores) e hoje toca a Pixel Educação, edtech agêntica. Números que ele mesmo declara:

| Indicador | Valor declarado | Fonte |
|---|---|---|
| Faturamento | R$ 1,3 a 1,5 milhão por mês | `[Zzkl7cYP8q8 00:19]` |
| Equipe | 5 pessoas e 6 agentes | `[Zzkl7cYP8q8 07:13]` |
| Crescimento | de R$ 15 mil a R$ 1,5 milhão por mês em menos de 4 meses | `[Zzkl7cYP8q8 22:21]` |
| Custo de IA | R$ 5 a 6 mil por mês | `[_1hZ3WVqoNw 36:06]` |
| Alunos atendidos por agentes | mais de 20 mil, sem equipe de suporte | `[Zzkl7cYP8q8 13:36]` |
| Canal | 143 mil inscritos, 321 vídeos, 2,2 milhões de views | API do YouTube |

A tese que atravessa o canal: **contexto é rei, ferramenta é commodity, e o valor migra para o sistema operacional do agente (memória, skills, rotinas e governança)**.

## Parte 1. O que o Bruno vende hoje

Serve como benchmark da escada de ofertas e dos canais de monetização.

| Produto | O que é | Preço ou modelo | Fonte |
|---|---|---|---|
| Minicurso OpenClaw | 2 a 3 horas, prompts e PRD prontos; mais de 12 mil alunos no primeiro mês | R$ 97 | `[_1hZ3WVqoNw 13:01]` `[xjHXUjyMZps 05:06]` |
| Imersão Agentes de IA para Negócios | 2 dias ao vivo: cérebro, skills, crons, segurança, multiagentes | R$ 397, 450 unidades, landing com 22% de conversão | `[_1hZ3WVqoNw 29:29]` |
| Mentoria 90 dias | 6 encontros com os 3 sócios, diagnóstico, plano, acompanhamento | R$ 30 mil, 10 vagas, R$ 240 mil em um dia | `[_1hZ3WVqoNw 37:00]` |
| Pixel AI Hub | comunidade e trilhas: primeiro agente, segundo cérebro, empresa agêntica; mais de 25 mil alunos em 4 meses | assinatura | `[FtRSGEm4gKQ 11:37]` |
| Marketing OS | Dexter e Léo empacotados: criativos, anúncios, orgânico | incluso no Hub | `[mU06NTyBsS8 29:59]` |
| Instalador de Hermes | deploy one-click na VPS com Telegram | R$ 30 | `[TSimMWwR6to 10:00]` |
| Soul 4.0 da Amora, skill "wick", Sinal WhatsApp | arquivos e repositórios abertos | grátis | `[mU06NTyBsS8 46:25]` `[tXAH78b0Sms 18:20]` |
| Afiliados | Hostinger VPS, Replit, Crisp, Hotmart | comissão sobre infra que os agentes consomem | `[xjHXUjyMZps 11:09]` |
| SaaS próprios | Metricaas (MRR), MyGroupMetrics (grupos de WhatsApp), SaaS de WhatsApp com 25 números | não dito | `[_1hZ3WVqoNw 08:31]` `[TSimMWwR6to 07:16]` |
| Comunidade MicroSaaS | portal com 15 mil pessoas, MicroSaaS Pro, curso Do Zero ao MicroSaaS, newsletter | R$ 250 por ano no lançamento | `[Px18BOPAKhA 09:26]` |

Padrão: **implementa internamente, prova com números, depois vende o que já roda**. Cada agente interno vira produto ou trilha.

## Parte 2. Catálogo de serviços para clientes B2B da Omnimaker

Numerados para facilitar a escolha. Cada item traz o que é, de onde veio, o modelo de cobrança sugerido pelo próprio canal e o que precisa existir antes.

### Entrada e diagnóstico

**1. Diagnóstico de maturidade agêntica.** Posicionar o cliente nos 5 degraus (chatbot, agente pessoal, empresa agêntica, agent loops, maestro) e aplicar o teste dos 6 pontos para decidir o que merece automação. Projeto de 3 meses para levar do degrau 1 ou 2 ao 3. Cobrança por projeto. `[ND4ck6N7c3s 02:10, 08:40]` `[HaDJONsfua0 08:25]`

**2. Auditoria de segurança de templates, repositórios e agentes.** Verificar prompt injection e malware antes de qualquer deploy, e endurecer a operação: VPS por agente, Docker, Tailscale, 1Password, e-mail e calendário próprios do agente, acesso granular, sem chave de API dentro do agente. Cobrança por auditoria ou como parte do onboarding. `[r7jOicSsUwk 06:40]` `[mU06NTyBsS8 65:22, 67:10]` `[sNKRYUip4zA 14:42]`

### Fundação

**3. Implantação do Segundo Cérebro corporativo.** Repositório GitHub por cliente com `mapa.md`, Ledger de contexto, pastas por área e projeto, skills `cérebro` e `salve` para a equipe, arquivos vivos de pessoas, pendências, deadlines e decisões. Um cérebro por cliente é a unidade de permissionamento. É exatamente a camada que o `agent-context-kit` implementa. Cobrança por implantação mais mensalidade de curadoria. `[TSimMWwR6to 10:48, 12:55]` `[Zzkl7cYP8q8 05:19, 09:05]` `[kbR8goTbJS0]`

**4. Agente chief of staff para o C-level.** Uma "Amora" por cliente: visão 360 dos negócios, alertas de urgência, meta, caixa e prazos, heartbeat que acorda a cada hora e só fala quando há algo, fila de decisões que só traz o que exige humano. Cobrança por assento executivo mensal. `[Zzkl7cYP8q8 10:11]` `[iRc6QwYmHDI 06:49, 08:43]` `[ND4ck6N7c3s 15:19]`

**5. Agente de governança de frota.** Um "Léo" que audita diariamente crons, skills e saúde dos agentes, faz backup do cérebro e detecta vazamento de CPF, cartão, token e senha. Base de um SLA de operação. Cobrança mensal por frota. `[Zzkl7cYP8q8 09:37]` `[mU06NTyBsS8 68:06]`

**6. Camada única de integrações.** Composio como chave única para mais de 1.500 apps, válida para Hermes, OpenClaw, Codex e Claude, mais o padrão "leia a documentação desta API e instale" com a chave do cliente. Reduz horas de integração e evita reconectar OAuth a cada troca de agente. Cobrança embutida na implantação. `[1uiVsGUutBk 14:28, 15:36]` `[sNKRYUip4zA 20:36]`

### Operação por área

**7. Marketing OS e gestor de tráfego agêntico.** Meta Ads via API, lição salva por criativo (ângulo, hook, formato, tempo de visualização), fábrica de 50 a 90 criativos por semana derivados do que performa, relatório diário com receita, gasto, ROAS, tendência e recomendação, humano do cliente decidindo no final. Caso interno: ROAS 5,67 e custo de lançamento de R$ 25 mil para R$ 5 mil. Cobrança por retainer mais performance. `[FtRSGEm4gKQ 13:07, 16:56]` `[1uiVsGUutBk 20:09, 21:31]` `[_1hZ3WVqoNw 20:28]` `[xjHXUjyMZps 39:35]`

**8. Inteligência de conteúdo.** Um "Dexter" por cliente: radar de benchmarks em X, YouTube, Instagram e Reddit, score de fit 0 a 100, inbox de pautas, pipeline fontes → evidências → ideia → backlog → produção → performance → aprendizado → wiki, snapshot diário de métricas por 7 dias, carrossel e newsletter gerados automaticamente, gates humanos definidos. Cobrança por retainer. `[mU06NTyBsS8 02:43, 05:15]` `[HaDJONsfua0 17:13, 17:51]` `[FtRSGEm4gKQ 19:13]`

**9. Suporte e tutoria com memória por usuário.** Agente no WhatsApp ou Telegram restrito ao conteúdo do cliente, memória por número, recebe foto, áudio e vídeo, base de conhecimento que se autoatualiza a partir das conversas salvas em Supabase. Caso interno: 20 mil alunos sem equipe de 20 pessoas. Cobrança por volume ou por usuário ativo. `[Zzkl7cYP8q8 13:36, 14:06]` `[_1hZ3WVqoNw 19:03]` `[xjHXUjyMZps 01:12]`

**10. Sinal WhatsApp: social listening e mini CRM.** Pipeline WhatsApp → n8n → Supabase → dashboard e agente diário: volume, tempo médio de resposta, pendências 7/14/30 dias, pautas que cruzam grupos, menções de marca e tag de elogio, tasks por contato, aprovação humana de quem entra no cérebro. Repositório aberto como base. MVP de 1 hora de integração e cerca de US$ 250. Cobrança por implantação mais mensalidade. `[tXAH78b0Sms 03:16, 13:49, 16:36]`

**11. Backoffice agêntico.** Nota fiscal, cobrança, fluxo de caixa, faturas ao contador, loop diário via API do gateway (Hotmart, Stripe) alimentando dashboards, análise de contratos com red flags e envio para assinatura. Cobrança mensal por área. `[TSimMWwR6to 43:44, 45:05]` `[HaDJONsfua0 14:49]`

**12. Agente especialista setorial.** Leitura diária de notícias e fontes do setor do cliente com memória persistente; em um ano vira especialista do nicho e gera apresentações para o time. Cobrança mensal. `[sNKRYUip4zA 04:39, 17:44]`

### Qualidade e autonomia

**13. Camada de QA por agente cético e cross-check entre LLMs.** Uma LLM diferente avalia o trabalho da outra com rubrica 0 a 10; "quem faz não avalia, quem avalia não assina, quem assina é o humano". Semáforo verde, amarelo e vermelho como cláusula contratual de autonomia. Cobrança embutida nos retainers. `[HaDJONsfua0 05:17, 07:41]` `[sNKRYUip4zA 15:38]` `[ND4ck6N7c3s 17:22]`

**14. Loops de autoaprendizado como entregável.** Arquivo de lições aprendidas carregado a cada sessão; lição que reincide 3 vezes vira lei no Soul do agente. O histórico de lições é o ativo proprietário do cliente. `[FtRSGEm4gKQ 09:17, 10:37, 30:21]`

**15. Mission Control: painel de frota para o cliente.** Kanban de tarefas dos agentes, conteúdo e publicação, métricas de redes e de negócio, trends e sinais, feito a partir de template auditado, PRD e Claude Code na VPS. Um PRD bem feito entregou 85% em um prompt. Cobrança por projeto. `[r7jOicSsUwk 00:56, 07:56, 18:02]`

### Modelos de receita e aquisição

**16. FDE e results delivery: vender resultado, não software.** Um engenheiro dedicado à operação do cliente executa dentro do CRM dele, a tecnologia fica invisível e a cobrança é por uso, por sucesso ou por performance, com prova conta a conta e foto das métricas antes e depois. Disposição a pagar: menos de 10% para assinatura, 20 a 25% para resultado. Captura o budget de pessoas, não só o de software. `[YK4GQdwWG2Y 17:54, 24:22, 25:00]` `[WpojqC0CJ28 24:06, 25:35, 30:33]` `[Wip1eQTxtW0 01:49]`

**17. Vibe marketing: ferramentas gratuitas como ímã de leads.** Mini-SaaS construído com IA para o nicho do cliente, SEO programático com páginas por palavra-chave, pipeline bug → Notion → PRD → IA. Cobrança por projeto ou como parte do marketing. `[q0vFKBAjhJk 00:33, 19:41, 20:50]`

**18. Produto agêntico para edtechs e infoprodutores.** Curso em GitHub ou Drive "leia-me IA", primeira aula humana e o agente estuda o resto, order bump de agente por R$ 49, área do aluno via API e MCP, cron semanal que atualiza o agente do aluno. `[xjHXUjyMZps 05:17, 12:50, 24:33, 34:43]`

**19. Setup produtizado e hospedagem gerenciada.** Instalador one-click de agente na VPS como produto de entrada (R$ 30 no canal), 3 agentes por VPS de R$ 40, mais hospedagem e monitoramento gerenciados. Cobrança por setup mais mensalidade de infra. `[TSimMWwR6to 10:00, 09:04]` `[Zzkl7cYP8q8 16:19]`

**20. Escada educacional para clientes.** Workshop de entrada, imersão de 2 dias e mentoria de 90 dias com diagnóstico, plano e acompanhamento, replicando a escada R$ 97 → R$ 397 → R$ 30 mil. `[_1hZ3WVqoNw 25:30, 29:29, 37:00]`

**21. CCO-as-a-service.** Operar com agentes os 5 pilares do Chief Content Officer para o fundador do cliente: conteúdo, comunidade, comunicação, relacionamento com parceiros e representação institucional. No canal, o cargo responde por 90% do faturamento. `[Px18BOPAKhA 00:52, 04:13]`

**22. Máquina que constrói agentes e golden path.** Em vez de construir agente por agente, entregar ao cliente a "máquina" com dev container, padrões de segurança e MCPs próprios, e rodar hackathon de uma semana com toda a empresa. Modelo Arvo, com 82 agentes em produção. `[WpojqC0CJ28 39:42, 47:10, 49:23]`

## Parte 3. Capacidades para a própria Omnimaker

O que o canal mostra que a Omnimaker deve ter internamente antes de vender.

| Capacidade | Como o canal faz | Fonte |
|---|---|---|
| Segundo cérebro da agência e um por cliente | GitHub, `mapa.md`, Ledger, permissionamento por cérebro; o `agent-context-kit` é a camada de evidência | `[TSimMWwR6to 14:33]` |
| Squad enxuto | chief of staff, conteúdo, orquestrador e governança; subagentes sob demanda que "voltam a dormir"; menos agentes, menos manutenção | `[TSimMWwR6to 07:27, 51:10]` |
| Estação de trabalho da equipe | Claude Code com skill `cérebro` na entrada e `salve` na saída; agentes autônomos em Hermes ou OpenClaw na VPS; comando por Telegram e Slack | `[Zzkl7cYP8q8 05:08, 06:25]` |
| Tríade contexto, skills e rotinas | toda repetição vira skill; skill longa é fatiada; rotinas em linguagem natural | `[mU06NTyBsS8 25:04, 44:03]` |
| Soul em 4 camadas | identidade, contrato de runtime, como pensa, tom de voz, e o que não faz; prioridades: receita, risco, prazo, caos, alavancagem | `[mU06NTyBsS8 45:49]` `[iRc6QwYmHDI 25:43]` |
| Loops de autoaprendizado | lessons learned por sessão, lição 3x vira lei | `[FtRSGEm4gKQ 09:17]` |
| Heartbeat minimalista | acorda a cada hora, silencia se não há nada, lista do que não fazer para poupar tokens | `[iRc6QwYmHDI 06:49, 11:31]` |
| Multi-LLM por tarefa | Grok para velocidade, Codex para cota e tarefas pesadas, Claude para técnico, Gemini para vídeo; não ser fã de fornecedor | `[TSimMWwR6to 52:59]` |
| Infra padrão | Hostinger KVM2 a R$ 40 por mês com 3 agentes, Docker, Tailscale, 1Password, backup diário via MCP | `[mU06NTyBsS8 56:26, 57:52]` |
| Founder-led growth | conteúdo do fundador responde por 40 a 90% das vendas; comunidade pequena e engajada antes de plataforma | `[mU06NTyBsS8 04:03]` `[Px18BOPAKhA 20:04]` |
| Dogfooding | implementar na própria empresa, medir, depois vender; cada agente interno vira produto | `[_1hZ3WVqoNw 29:03]` |
| Métricas de ROI | horas devolvidas ao time, custo de IA de R$ 2 a 6 mil por mês contra headcount, run rate em vez de ARR | `[1uiVsGUutBk 24:10]` `[Wip1eQTxtW0 13:17]` |

## Parte 4. Regras de governança que se repetem

Seis regras do vídeo dos 6 agentes `[Zzkl7cYP8q8 17:34 a 21:50]`, complementadas pelos demais:

1. **Contexto acima de tudo.** O cérebro tem que ser vivo; o time salva tudo nele, senão o contexto sai com o funcionário.
2. **Autonomia é uma escada.** O agente entra para ler, depois recomenda, só então age. Humano decide no meio.
3. **Skill não testada não entra em produção.** O agente opera por skills predefinidas; o time não monta skill solta.
4. **Mínimo de agentes.** Mais agentes exigem mais governança, contexto e higienização.
5. **Todo agente se paga.** Tem de gerar economia ou produtividade desde o primeiro dia.
6. **Cuidado com perfeccionismo.** Over-engineering custou 2 a 3 meses; perfeição é inimiga da operação.

Adições: agente entra em processo que já funciona, senão automatiza bagunça `[mU06NTyBsS8 12:03]`; cultura vem de cima, sócios usam primeiro `[Zzkl7cYP8q8 22:02]`; todo loop precisa de objetivo, contexto, ferramentas, critério de pronto, limite e escalada `[ND4ck6N7c3s 12:40]`; nunca sincronizar a pasta do agente com outra nuvem `[Zzkl7cYP8q8 01:36]`.

## Parte 5. Como escolher por onde começar

Critérios sugeridos: esforço de implantação, dependência de outros itens, tempo até receita e aderência ao que a Omnimaker já tem (o `agent-context-kit` e a skill de YouTube).

| # | Serviço | Esforço | Depende de | Tempo até receita | Aderência ao que já existe |
|---|---|---|---|---|---|
| 1 | Diagnóstico de maturidade | baixo | nada | imediato | alta |
| 3 | Segundo Cérebro corporativo | médio | 2 | curto | muito alta |
| 4 | Chief of staff | médio | 3 | curto | alta |
| 5 | Governança de frota | médio | 3, 4 | médio | alta |
| 7 | Marketing OS | alto | 3, 6 | médio | média |
| 8 | Inteligência de conteúdo | médio | 3, 6 | médio | alta |
| 9 | Suporte com memória | médio | 3 | médio | média |
| 10 | Sinal WhatsApp | baixo | nada | curto | alta |
| 13 | QA por agente cético | baixo | qualquer retainer | embutido | alta |
| 16 | FDE e cobrança por resultado | alto | 3 a 8 | longo | média |
| 19 | Setup produtizado | baixo | nada | imediato | alta |

Três combinações que o próprio canal valida como sequência:

- **Trilha fundação:** 1 → 3 → 4 → 5. É a ordem em que a Pixel construiu a própria operação e é onde o `agent-context-kit` entra como diferencial técnico.
- **Trilha receita rápida:** 19 → 10 → 9. Produtos de baixo esforço com prova visível em dias, bons para os primeiros clientes.
- **Trilha performance:** 3 → 6 → 7 → 16. Mais longa, mas é a que permite cobrar por resultado.

A escolha fica para a reunião de decisão. O que não recomendo é começar por 16 sem a fundação, porque cobrar por resultado exige o cérebro do cliente e a governança prontos.

## Anexo. Vídeos transcritos

| ID | Título | Data |
|---|---|---|
| W7KqfZPep5o | GROKBOT vs HERMESBOT: qual agente de IA vale a pena em 2026 | 2026-09-03 |
| TSimMWwR6to | Abri o jogo: meu setup de agentes de IA em negócios, conteúdo e casa | 2026-08-30 |
| YK4GQdwWG2Y | O próximo mercado de US$ 1 trilhão não é software: é serviço | 2026-08-25 |
| kbR8goTbJS0 | As 3 camadas que deixam o Segundo Cérebro da sua IA mais inteligente | 2026-08-20 |
| FtRSGEm4gKQ | Meus agentes aprendem sozinhos. Eu só gravo a lição. | 2026-08-16 |
| HaDJONsfua0 | O que é Graph Engineering? A técnica por trás do funcionário digital | 2026-08-09 |
| ND4ck6N7c3s | O uso mais avançado de agentes de IA que eu já vi | 2026-07-23 |
| Zzkl7cYP8q8 | 6 Agentes de IA que Fazem Minha Empresa Faturar 1,5 Milhão por Mês | 2026-07-21 |
| sNKRYUip4zA | Qual IA usar pra cada tarefa? Essa pergunta tá errada | 2026-07-02 |
| xjHXUjyMZps | Criar infoproduto com IA não é o futuro. O produto agêntico é | 2026-06-29 |
| tXAH78b0Sms | A IA que organiza o caos do WhatsApp: 85.000 msg viraram um dashboard | 2026-06-26 |
| WpojqC0CJ28 | O fim do SaaS como conhecemos: empresas de IA vão vender resultado | 2026-06-23 |
| 1uiVsGUutBk | Pare de testar toda ferramenta de IA: use este combo | 2026-06-18 |
| mU06NTyBsS8 | 7 passos obrigatórios para usar o Hermes | 2026-06-02 |
| iRc6QwYmHDI | Heartbeat em agentes de IA | 2026-05-10 |
| _1hZ3WVqoNw | Como escalamos pra R$ 1.3M/mês em 45 dias com uma empresa gerida por agentes | 2026-04-03 |
| r7jOicSsUwk | Construí o PAINEL DE CONTROLE da minha empresa inteira com IA | 2026-03-23 |
| q0vFKBAjhJk | Vibe Marketing | 2026-02-26 |
| Px18BOPAKhA | Criamos um novo cargo (CCO) que toda Startup deveria ter | 2025-09-30 |
| Wip1eQTxtW0 | A tríade do momento: SaaS + IA + Serviços | 2025-04-08 |

As fichas de extração por vídeo, com todas as minutagens, ficaram no workspace da sessão e podem ser incorporadas a este diretório se a equipe quiser o detalhe completo.
