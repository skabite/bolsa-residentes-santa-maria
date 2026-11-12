# Caderno de investigação — onde trava o incentivo federal

Estado em **12/11/2026**. Este arquivo é a memória de trabalho entre sessões: o que já foi
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

## Achado de 12/11/2026: o código de ocupação (CBO)

Resumo: **o zero de jul–set/2026 coincide com uma mudança na forma de o Ministério ler o cadastro, não com uma mudança
no cadastro de Santa Maria.** Tudo abaixo vem de fonte oficial (API do painel de pagamentos e serviços do CNES, que
aceitam `?competencia=AAAAMM`); a ligação entre as duas coisas é leitura nossa, ainda sem confirmação do Ministério.

- **Set/2026 publicado (fato):** parcela 202611, 18 credenciados, 0 contados, R$ 0. Terceiro zero seguido.
- **CBO de Santa Maria, mês a mês (fato):** de nov/2024 a set/2026, **todos** os médicos com vínculo de residência nas 15
  unidades estavam com o CBO **2231F9** (Médico residente): 16–17 (nov/2024–fev/2025), 20 (mar/2025–fev/2026), 26
  (mar–ago/2026), 25 (set/2026). No cadastro consultado em 12/11/2026, os 23 estão no **225130** (Médico de família e
  comunidade). As fichas de 15/10 ainda tinham 2231F9 e a contagem de 03/11 já usava o filtro 225: a troca foi feita
  entre meados de outubro e o início de novembro. As competências 202610 e 202611 ainda não têm histórico no serviço,
  então não se sabe em qual delas a troca entrou. `dados/cnes_cbo_medicos_residentes_por_competencia.csv`.
- **Junho × julho (fato):** o cadastro era igual nos dois meses (26 registros, todos em equipe, 25 em eSF, 23 com 40 h
  na equipe, 1 em eAP). A contagem foi de 12 para 0. Não houve mudança local que explique.
- **Outros municípios (fato):** na soma de 29 municípios consultados na API, os médicos contados foram 605 (fev), 416
  (mar), 361 (abr), 339 (mai), 321 (jun), **666 (jul)**, 689 (ago), 689 (set), de ~816 vagas. A queda de março e o salto
  de julho foram gerais. `dados/residencia_outros_municipios_2026.csv`.
- **CBO × contagem em 12 municípios (fato):** onde os residentes estão em 225142 (Pelotas, Rio Grande, Passo Fundo,
  Palmas, Santa Rosa), 225130 (São Leopoldo) ou 225170 (Florianópolis), a contagem chegou ao teto em jul–set sem mudança
  no cadastro. Onde estão em 2231F9, ficou em zero (Porto Alegre, 81 residentes; Fortaleza, 67; Ijuí, 9) ou igual ao
  número de residentes em outro código (Canoas, 2; Santos, 1). Em Porto Alegre os enfermeiros residentes seguiram
  contados. Nenhum município da amostra teve médico em 2231F9 contado depois de junho.
  `dados/cnes_cbo_comparacao_municipios_2026.csv`.
- **A norma (fato):** a Portaria 10.193/2026 não cita CBO. Exige o vínculo "05 – Residência / 01 – Residente", equipe
  por INE e 40 h; o art. 58 da PRC nº 2 (na redação dela) manda a SAPS regulamentar "os meios para identificação dos
  residentes" no SCNES. Não localizamos esse ato (busca em 12/11/2026). O art. 50, §2º, pede o preceptor registrado na
  equipe ou na unidade do residente: a conferir pela gestão.
- **Regras visíveis no cadastro de cada mês (estimativa):** eSF + 40 h na equipe + até 2 por eSF → passavam 18
  (fev/2026), 22 (jun e jul/2026), 21 (set/2026) e **17** no cadastro atual (23 − 1 em eAP − 4 abaixo de 40 h − 1
  excedente). Corrige a estimativa anterior de "cerca de 18", que não descontava a eAP.
- **Dinheiro (estimativa):** com o teto de 18 contado em jul, ago e set, teriam entrado 3 × R$ 144.000 = **R$ 432.000**.
  Com o cadastro atual, 17 × R$ 8.000 = R$ 136.000/mês (folha de set–out: R$ 113.400 com INSS).
- **Quando volta (estimativa):** parcela = competência + 2 meses. Troca no CNES de out/2026 → parcela 12/2026, crédito em
  meados de dezembro. Troca só em nov/2026 → out/2026 também zerado e volta na parcela 01/2027.
- **Informação recebida (não oficial, 12/11/2026):** o usuário ouviu que "um problema era o CBO, e não a carga
  horária". Bate com os dados acima; não é documento.
- **Limites:** amostra escolhida (capitais e municípios gaúchos), não o país; correlação, não regra publicada; em
  municípios grandes a varredura do CNES pega as unidades de atenção primária achadas pelo nome. O CBO pode ser o
  critério direto ou acompanhar outro (por exemplo, a forma de compor a equipe mínima).

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

**Revisão de 12/11/2026.** A ordem abaixo é a de 03/11. Com o achado do CBO: a hipótese nova (0) passa a ser a
principal para os zeros; a 1 perde força para Santa Maria, porque a queda de março foi geral na amostra; a 4 segue
possível, mas o zero começou no mês em que a contagem mudou em outros municípios; a 5 foi respondida (o cadastro de
jul–set foi lido no histórico do CNES e era regular nas regras visíveis).

0. **CBO 2231F9 deixou de ser contado a partir da competência jul/2026** — principal para os zeros. Ver a seção
   "Achado de 12/11/2026". Falta: confirmação escrita do Ministério e o ato da SAPS.
1. **Matrícula da turma de 2026 não reconhecida (CNRM)** — era a principal. Os 12 contados batem em número com
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

- **Mais importante agora**: (a) olhar a **parcela 12/2026** (competência out/2026) quando o Ministério publicar, por
  volta de 10/12: diz se a troca do CBO entrou em outubro; (b) quando o serviço do CNES tiver o histórico de 202610,
  rodar `python3 scripts/cnes_cbo.py santa-maria 202610`; (c) pedir ao Ministério, por escrito, qual CBO é aceito, desde
  quando e em que ato, e o reprocessamento de jul–set/2026; (d) gestão: os 4 cadastros abaixo de 40 h e a equipe com 3
  seguram a contagem em 17 de 18.
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
- **Dados a atualizar**: competência **out/2026** do Ministério (parcela 12/2026); empenhos de **nov/2026** (saem por
  volta do dia 25; não existiam em 12/11); resposta do Ministério sobre estágio externo e 40h. A
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
- **12/11/2026** — coleta feita de uma máquina com acesso aos sites do governo. Set/2026 publicado e zerado; FNS sem
  crédito da ação 69166 desde 14/08 (parcela 11 ainda não emitida em nenhuma ação); sem empenho de novembro; CNES igual ao
  de 03/11. Descoberto que os serviços do CNES aceitam `?competencia=AAAAMM`: histórico do CBO de Santa Maria (2231F9 até
  set/2026; 225130 hoje) e de 12 municípios, cruzado com a contagem de 29 municípios na API. Leitura: o Ministério deixou
  de contar o 2231F9 em jul/2026 (em aberto). Estimativa corrigida para 17 de 23 nas regras visíveis. Fontes conferidas
  no documento oficial: IPCA (série 433 do BC: 38,40%, R$ 6.227,96), Ijuí, Remígio, DF, Rio e Cachoeiro; DOU da Portaria
  Interministerial 9/2021 localizado (ed. 195, seção 1, p. 42). Fontes novas 23 e 24; script `scripts/cnes_cbo.py`.
  Site redesenhado em tons pastéis (CSS refeito, tema claro e escuro, tabelas que cabem no celular, `defer` nos
  scripts, metadados de compartilhamento).
