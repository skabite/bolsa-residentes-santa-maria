# Caderno de investigação — onde trava o incentivo federal

Estado em **03/11/2026**. Este arquivo é a memória de trabalho entre sessões: o que já foi
estabelecido, o que é hipótese, o que foi descartado e o que falta. O site público (as páginas `.html`)
só recebe o que estiver confirmado. **Este arquivo também é público** (o GitHub Pages publica o
repositório): sem nomes e sem atributo individual (carga horária, origem, saída, gênero, licença) de quem
possa ser identificado. Grupo com menos de 3 pessoas por papel ou por equipe aparece só como número.
Detalhes individuais vão à gestão e às COREMEs por canal privado.

## A pergunta

Santa Maria tem **18 vagas credenciadas** e paga bolsa a **22–23 residentes** de MFC, mas o Ministério
da Saúde contou **12** residentes em mar–jun/2026 e **0** em jul e ago/2026 (planilha e API do painel de pagamentos
da APS, aba "Residência"). Onde trava? O objetivo do usuário é entender o mecanismo para **ensinar a
gestão municipal**, sem tom acusatório: cada residente não contado são R$ 8.000/mês que a própria
prefeitura deixa de receber, e ela paga a bolsa de qualquer jeito.

## O que a norma exige (texto verificado no DOU)

Transcrição em [`dados/portaria_10193_2026_arts_172E_172IA.md`](dados/portaria_10193_2026_arts_172E_172IA.md).

Para um residente entrar na conta (art. 172-E § 4º, art. 172-F § 6º, art. 172-E § 6º):

| Requisito | Onde se vê | Quem resolve |
|---|---|---|
| Situação regular na **CNRM** e cursando 1º, 2º ou ano adicional | não é público (SisCNRM) | COREME de cada programa |
| SCNES com "05 – Residência" / "01 – Residente" | ficha do CNES | gestão municipal (§ 5º do 172-F) |
| Vinculado a equipe elegível (eSF etc.) por INE | ficha do CNES | gestão municipal |
| **Carga horária mínima de 40h semanais** na composição da equipe | ficha do CNES | gestão municipal |
| No máximo **2 residentes de medicina por eSF** | ficha do CNES | gestão municipal |
| Teto de vagas credenciadas (hoje 18) | planilha do MS / e-Gestor | gestão municipal (pedir ampliação no e-Gestor) |

**Suspensão (art. 172-H):** o MS suspende a transferência quando, por **3 competências consecutivas**,
falta produção no SIAPS das equipes com residentes (I), falta cadastro regular dos residentes no SCNES
"observados os requisitos dos arts. 172-E e 172-F" (II), ou falta cadastro de novo residente depois de
uma saída (III). A suspensão "será mantida até a adequação das irregularidades".

## O que já está estabelecido

- **Contagem do MS** (planilha oficial): 2025 — turma entrou em mar/2025, MS passou de 8 (mar) para 14
  (abr): **reconheceu a turma nova em ~1 mês**. Out/2025–fev/2026: 17 contados de 19 pagos (teto 18).
  2026 — caiu para 12 em mar/2026 e parou; 0 em jul e ago/2026. Set/2026 ainda não foi publicado.
- **Repasse federal não é retroativo**: em todas as competências o valor = contados × valor unitário;
  nenhum acerto posterior aparece. Mês não contado = dinheiro perdido. A bolsa municipal, sim, é paga
  com retroativo.
- **Zero registrado, não dado ausente (jul e ago/2026)**: na API, a competência ago/2026 traz
  `qtResidenteMedicoCredenciado=18`, `qtResidenteMedicoPagamento=0` e `vlPagamentoResidencia=0`, com os campos
  preenchidos. O resumo do plano "Demais programas, serviços e equipes da APS" traz `vlIntegral=0`,
  `vlDesconto=0` e `vlEfetivoRepasse=0`: a rubrica nasceu zerada, não houve desconto nem glosa. As outras 22
  rubricas do mês vieram com valor. Jul/2026 já era zero; set/2026 não foi publicado.
- **FNS (03/11/2026)**: a ação 69166 (Demais programas) teve 8 créditos em 2026, **R$ 749.500**, o último em
  **14/08/2026** (parcela 08, competência jun/2026). Não há parcelas 09 (set) e 10 (out) nessa ação. Não é atraso
  do FNS: a ação 69182 (eSF/eAP) recebeu a 09 em 10/09/2026 (R$ 931.126) e a 10 em 14/10/2026 (R$ 952.126). O
  total de R$ 749.500 bate com a soma das parcelas 2026 do Ministério, inclusive as duas zeradas.
- **Empenhos de out/2026**: 22817/2026 (R$ 49.500, 11 residentes) e 22818/2026 (R$ 45.000, 10 residentes)
  estão pagos integralmente: R$ 94.500, 21 residentes. Empenhos de nov/2026 ainda não existiam em 03/11/2026
  (saem por volta do dia 25). Em set e out, os dois empenhos de 11 residentes declaram a fonte "Transferências
  Fundo a Fundo ... Governo Federal" mesmo com o incentivo de residência zerado: a fonte declarada é o bloco de
  manutenção federal em geral, que continua recebendo outros repasses.
- **Lei 6.516/2020, art. 3º, §2º**: a bolsa é vinculada à pré-existência do repasse federal, sem
  responsabilidade solidária do município quando o repasse não vem. Com o incentivo de residência zerado desde a
  competência jul/2026 e sem crédito em set e out/2026, isso é um risco concreto para a continuidade da bolsa.
- **Composição real** (informação de residentes do programa, não oficial; UFN R2 = 4 confere com o
  resultado publicado da seleção):

  | Grupo | Quantos |
  |---|---|
  | Matrícula anterior a mar/2026 | **12** |
  | Matrícula iniciada em mar/2026 | **11** |
  | Total abr–jun/2026 (bate com os 23 pagos pela prefeitura) | 23 |
  | Ago/2026 (bate com os 22 pagos) | 22 |

  A divisão por programa e por ano fica fora deste arquivo: com grupos de 1 pessoa ela permitiria
  deduzir quem saiu e quando.

- **CNES de 03/11/2026 (15 unidades, contagem agregada, sem nomes)**: **23** médicos residentes (eram 26 em
  jun/2026); São José caiu de 5 para 3, São João de 1 para 0, as demais unidades ficaram iguais. Todos os 23
  estão em alguma equipe (22 em eSF e 1 em eAP). **4 cadastros** estão abaixo de 40 h na cidade (só o total
  agregado; não registrar unidade nem equipe). **Uma equipe tem 3** residentes de medicina: São Francisco, INE
  0001662821; em São José, a equipe que tinha 3 passou a 2.
  - **Estimativa (hipótese, premissa escrita):** aplicando 40 h e até 2 por eSF ao cadastro atual, cerca de
    **18** dos 23 se encaixariam (23 − 4 − 1), igual às 18 vagas. Premissa: é o cadastro de hoje, não o das
    competências jul/ago/2026; não prova que o cadastro de jul/ago estivesse regular. O cadastro atual, sozinho,
    não explica o zero de jul/ago.
- **CNES de 15/10/2026 (3 unidades, fichas) — histórico:** todos os R1 tinham cadastro correto (CBO 2231F9,
  vínculo Residência/Residente, 40h, eSF, entrada em 10/03/2026); dois registros abaixo de 40h; duas equipes com
  3 (São José INE 0000433012 e São Francisco INE 0001662821); pelo menos um registro ativo de quem já saiu. São
  José constava como "UNIDADE SEM ATIVIDADE DE ENSINO" e São Francisco como "UNIDADE AUXILIAR DE ENSINO"; não se
  sabe se o MS confere isso. Parte desse quadro foi superada pela contagem de nov/2026.
- **Todos os empenhos da bolsa são da prefeitura**; "federal" × "municipal" é só a fonte declarada
  (1600 – Bloco de Manutenção × 1500 – impostos). A divisão 11 + 11 não acompanha a contagem do MS.
- **Média federal de fato por residente pago**: R$ 4.189 (mar–jun/2026), R$ 0 (jul e ago/2026), R$ 3.259
  (nov/2024–ago/2026; R$ 3.434 até jul/2026) — abaixo da bolsa em todos os meses menos fev/2026.

## Hipóteses, em ordem

1. **Matrícula da turma de 2026 não reconhecida (CNRM)** — principal. Os 12 contados batem em número com
   quem tinha matrícula antes de mar/2026; os 11 que começaram em mar/2026 não aparecem. A planilha só traz o
   total, então a correspondência um a um não está provada. A contagem de nov/2026 mostra todos os 23 em alguma
   equipe, mas é o cadastro de hoje: não diz como estava em jul/ago. O requisito individual que sobra é o § 4º,
   I–II do 172-E (situação regular na CNRM). Contra: exigiria falha simultânea de programas diferentes; pode ser
   também a forma como o MS passou a ler o CNRM com a portaria nova (fev/2026).
2. **Carga horária < 40h** (art. 172-F § 6º) — real, mas explica no máximo 4 pessoas (os 4 cadastros abaixo de
   40h em nov/2026). Não é exigência nova de 2026: a Portaria 4.411/2022 (art. 172-E, § 10) já exigia a carga
   horária mínima da composição; o "40 (quarenta) horas" literal só aparecia para eSB (§ 9º). Ver a seção sobre
   estágio externo abaixo.
3. **Limite de 2 por eSF** — uma equipe com 3 em nov/2026 (São Francisco, INE 0001662821); explica no máximo 1
   excedente. Em São José, a equipe que tinha 3 passou a 2. Registros de quem já saiu também precisam de baixa.
4. **Zeros de jul e ago/2026 = suspensão do art. 172-H** depois de 3 competências com residentes "irregulares"
   (mar/abr/mai ou abr/mai/jun). Se for isso, regularizar os cadastros destrava (sem retroativo).
   Não confirmado: o texto não diz se a suspensão é do incentivo inteiro ou por vaga.
5. **O cadastro atual sozinho não explica o zero (estimativa).** Aplicando 40 h e até 2 por eSF ao cadastro de
   nov/2026, cerca de 18 dos 23 se encaixariam, igual às vagas. Premissa: é o cadastro de hoje, não o das
   competências jul/ago/2026; não prova que o cadastro de jul/ago estivesse regular. É hipótese, não fato.

**Descartadas**: cadastro ausente; INE ausente; equipe não homologada (as 16 equipes com residentes em
nov/2026 estão homologadas); modalidade eAP como causa principal (só 1 residente em eAP); vínculo errado nos
R1; carga horária como causa geral (quase todos os registros têm 40h, só 4 abaixo); dado ausente ou glosa em
jul/ago (o zero é registrado, com os campos preenchidos); o caso de "registro desatualizado" citado em 13/10
(estava errado; corrigido na página com nota).

## Estágio externo e as 40 horas (pergunta de 29/10/2026)

Pergunta do usuário: o município pode manter no CNES o cadastro de 40h dos R2 durante os estágios externos,
já que muitos são na própria rede e outros programas fariam isso? Análise em termos gerais; **não registrar
quem está em estágio nem ligar isso aos 4 registros abaixo de 40h** (grupos pequenos, identificáveis).

- **Norma (fato, texto do DOU):** o residente "deverá cumprir a carga horária mínima, cumulativamente, de
  quarenta horas semanais na composição" das equipes listadas (art. 172-F § 6º); o cadastro no SCNES é da gestão
  (§ 5º); a conta usa residentes "atuantes" no município (172-E § 2º). O verbo é *cumprir*: o cadastro de 40h tem
  de corresponder a 40h reais na equipe.
- **As 40h antes de 2026 (conferido em 29/10/2026):** a Portaria GM/MS 4.411/2022 já mandava o profissional em
  formação cumprir "a carga horária semanal mínima exigida para a composição da eSF ou eSB" (art. 172-E, § 10).
  O número "40 (quarenta) horas" só aparece literalmente para eSB (§ 9º); para eSF, o mínimo de 40h vinha da
  carga horária exigida para a composição da equipe, não nasceu com a 10.193/2026.
- **Margem:** a residência médica pode ter até 60h semanais (Lei 6.932/1981, art. 5º; fonte 21, conferida no
  Planalto em 29/10/2026). Estágio externo em parte da semana, mantendo 40h na equipe, cumpre as duas regras. Estágio em tempo
  integral fora da equipe: manter 40h no CNES não reflete a realidade (risco para a gestão em auditoria; a
  Portaria SAS/MS 134/2011 trata da fidedignidade do SCNES, a conferir se está vigente).
- **"Na rede" não basta:** só contam horas na composição de eSF, eSB, eMulti, eSFF/UBSF, eSFR, eCR ou eAPP. CAPS,
  policlínica, hospital ou UPA não estão na lista.
- **Folga do teto (estimativa):** com 22 pagos e 18 vagas, até 4 residentes podem ficar abaixo de 40h no mesmo mês
  sem perda, se os outros 18 estiverem regulares (172-E § 2º). Escalonar os estágios protege o repasse. Hoje a
  folga não ajuda: em jul/ago a contagem está em 0 por outros motivos (hipótese 1).
- **A perguntar ao Ministério:** (a) se "cumulativamente" permite somar horas em mais de uma equipe elegível (ex.:
  eSF + eMulti); (b) como tratar o residente em estágio externo; (c) como aplica, na prática, a carga horária mínima
  que já vinha da 4.411/2022.
- **"Outros programas fazem isso":** não achamos orientação pública do Ministério. A busca de 29/10 mostrou
  programas que fixam um mínimo de horas na unidade (João Pessoa, Portaria 18/2016 da RMFC: 32h; regulamento
  da ESP/SC: 45h em serviço na atenção básica, de 60h) — vistos só em resumo de busca, a conferir. Perguntar às
  COREMEs como outros programas organizam a semana durante estágios.
- **Para conferir (links):** Portaria GM/MS 4.411/2022 (conferida em 29/10/2026)
  (https://bvsms.saude.gov.br/bvs/saudelegis/gm/2022/prt4411_22_12_2022.html); nota técnica do Ministério sobre o
  recurso adicional para residência na APS, 2023
  (https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2023/sei_ms-0024042088-nota-tecnica.pdf);
  PNAB 2017 (Portaria GM/MS 2.436/2017), sobre as "até 8 horas" para residência que existiam na PNAB de 2011;
  Resolução CNRM nº 1/2015 (requisitos mínimos do PRM em MFC, alterada pela Resolução CNRM nº 35/2018).
- **Na página:** contagem.html, seção "Estágio externo conta para as 40 horas?" (regras, margem, folga, em aberto)
  e a estimativa dos ~18 no cadastro de nov/2026; um item em fazer.html para gestão e COREMEs.

## Próximos passos

- **Gestor (e-Gestor APS)**: quais residentes foram validados em cada competência e o motivo dos não
  validados; motivo dos zeros de jul e ago/2026; se o credenciamento (18) precisa ser ampliado/atualizado.
  Correções que não dependem de nada: dar baixa dos registros de quem já saiu; resolver a equipe com 3
  residentes (São Francisco, INE 0001662821; o art. 172-F § 4º permite mudar de equipe homologada); alinhar a
  carga horária dos 4 residentes abaixo de 40h com a dos colegas.
- **COREMEs (UFSM e UFN)**: situação da turma de 2026 (R1 e ano adicional) no SisCNRM e desde quando. Perguntar
  também se aderiram ao **Edital SGTES/MS nº 10/2026 (Mais Residências)**: bolsa-formação de
  R$ 4.000/mês paga pelo MS direto ao residente que fizer o curso de preceptoria em MFC, se o programa
  tiver aderido (residentes matriculados em abr/2026; Portaria GM/MS 8.403/2025).
- **LAI**: pedido ao Ministério já protocolado pelo usuário no Fala.BR (antes de 15/10/2026; prazo
  20 + 10 dias). Ao chegar a resposta, comparar com as hipóteses acima.
- **Dados a atualizar**: competência **set/2026** do Ministério (a mais importante: diz se o zero continua);
  empenhos de **nov/2026** (saem por volta do dia 25); resposta do Ministério sobre estágio externo e 40h. A
  contagem do CNES de nov/2026 já foi feita nas 15 unidades, mas é agregada: para conciliar os 23 registros com
  os 21–22 pagos, a gestão precisa conferir ficha a ficha (sem nomes no repositório). Depois de mudar os CSVs:
  `dados/situacao_dos_dados.csv` (período e data da coleta) e `python3 scripts/montar_site.py`.
- **Pista conferida (29/10/2026)**: a Portaria GM/MS 10.345/2026 (DOU de 05/05/2026, ed. 82, seção 1, p. 131)
  credencia equipes da APS e, no Anexo XXI, "novas vagas" de residência. Santa Maria (IBGE 431690) **não está**
  no Anexo XXI: não ganhou vagas novas de residência por essa portaria. Aparece só no Anexo VII, com 3 INEs
  (0002044692, 0002105403, 0002044471) para eSF em substituição a equipes homologadas — sem relação com residência.
  Link: <https://in.gov.br/web/dou/-/portaria-gm/ms-n-10.345-de-13-de-marco-de-2026-*-703189310>.

## Privacidade e histórico

- Versões anteriores a 19/10/2026 deste caderno e da página (commits até 62d1598) traziam detalhes
  individuais que hoje não aparecem mais. Decisão em 19/10/2026: **não reescrever o histórico do git** por
  iniciativa própria (risco baixo, custo alto); reescrever só se alguém citado pedir (LGPD art. 18), sabendo
  que clones já feitos não são alcançados.
- Saídas dos scripts de coleta (com nomes de credores) ficam em `scripts/saida/`, que é ignorada pelo git.
  PDFs e extratos enviados no chat nunca entram no repositório.

## Registro das sessões

- **13/10/2026** — dossiê, empenhos, planilha do MS, CNES (26 registrados), homologação dos INEs, LAI.
- **15/10/2026** — revisão: gráfico por residente refeito com a média real; manchete corrigida
  ("R$ 8.000 por residente que o Ministério conta"); empenhos explicados como todos municipais; caso
  do CNES de julho retirado; texto da Portaria 10.193/2026 transcrito; padrão "matrículas de 2026 não
  contadas" identificado; fichas CNES de 3 unidades analisadas.
- **19/10/2026** — revisão de conformidade legal (LGPD, honra, direitos autorais, ética do residente):
  caderno reescrito sem atributos individuais; correções datadas no relatorio.md; saídas dos scripts
  protegidas; página redesenhada para celular. Revisão adversarial da página nova (fatos e regras):
  hipótese de julho e atribuição da contagem reescritas sem afirmar causa (CNES da gestão, CNRM das
  COREMEs, credenciamento do Ministério); alcance do CNES explicitado (3 de 15 unidades); premissa do
  retroativo de março escrita; vagas do gráfico em degraus (15 em mar–set/2025); empenho do INSS
  patronal (18203/2026) nos dados; tabela de composição reduzida aos totais; comparações com Ijuí
  (R$ 6.000 desde 2023) e Santos.
- **20/10/2026** — revisões de UX, acessibilidade, texto e código aplicadas: fontes em grupos
  recolhidos (página de 18,9 para 13,7 telas a 360 px), tabelas que cabem no celular (a federal com
  coluna fixa), contraste AA, "repassa" (Ministério → município) × "paga" (prefeitura → residente),
  glossário ampliado, gráficos navegáveis por arrasto e botões, página legível sem JavaScript,
  `scripts/graficos.py` com rótulos tirados dos dados e erro se faltar marcador. Próximo passo
  sugerido: ofício à Secretaria e às COREMEs antes de divulgar mais.
- **29/10/2026** — a página única virou um site de 9 páginas (Início, Reajuste, Contagem, Números, O que
  fazer, Linha do tempo, Fontes, Glossário, Sobre), com CSS e JS em `assets/`. Trechos com fonte abrem um
  balão (mouse, teclado e toque) com a referência e os links; termos técnicos, a definição. Fontes e termos
  saem de `dados/fontes.json` e `dados/glossario.json`; fonte 21 nova (Lei 6.932/1981, a conferir). Tabela
  "Até quando vão os dados" (`dados/situacao_dos_dados.csv`). `scripts/montar_site.py` monta as partes comuns,
  gráficos e tabelas e confere fontes, termos e links. Análise do estágio externo e das 40h (seção acima). Rede
  da sessão bloqueou todos os sites do governo: dados não atualizados; lista do que baixar passada ao usuário.
- **29/10/2026 (dados)** — empenhos de setembro e outubro/2026 incluídos: 11 + 10 residentes,
  R$ 94.500 de bolsas por mês e R$ 18.900 de INSS patronal (empenhos 20440/20441 e 22817/22818;
  INSS 20447 e 22835), conferidos no portal. Os créditos de ago–out/2026 ainda não foram publicados
  (o relatório de outubro só lista créditos até 09/10). A API do painel do Ministério segue com erro
  500 em todas as competências: ago/set não foram baixados; julho foi validado na planilha de 13/10.
  Fontes 1 e 21 conferidas (Lei 6.516/2020 e Lei 6.932/1981); a Portaria 10.345/2026 não deu vagas
  novas de residência a Santa Maria (só 3 INEs de substituição); a 4.411/2022 já exigia a carga
  horária mínima da composição. A folha caiu de 22 (ago) para 21 residentes (set–out) nos empenhos.
- **03/11/2026** — coleta nova: a API do painel voltou com `nuParcelaInicio`/`nuParcelaFim` e mostrou ago/2026
  com 18 credenciados, 0 pagos e R$ 0 (zero registrado, não dado ausente); o FNS registra 8 créditos da ação
  69166, R$ 749.500, último em 14/08/2026, sem parcelas 09 e 10 nessa ação (a 69182 recebeu as duas); os
  empenhos de outubro estão pagos integralmente (R$ 94.500, 21 residentes). CNES das 15 unidades em contagem
  agregada: 23 residentes (26 em junho), São José 5→3, São João 1→0, 4 abaixo de 40h, uma equipe com 3. A lei
  6.516/2020, art. 3º, §2º, passa a ser risco concreto para a bolsa. Site e CSVs atualizados; fonte 22 nova
  (FNS).
