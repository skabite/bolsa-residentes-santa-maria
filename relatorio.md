# Bolsa de residência médica em Santa Maria/RS — documentos, fluxo do dinheiro e dados reais

Levantamento feito em 13/10/2026 a partir dos dois documentos da pasta e de bases públicas oficiais
(Portal da Transparência de Santa Maria, FNS, DOU/BVS MS). Números extras estão em `dados/`.

> **Revisão de 15/10/2026 — o que mudou:**
> - **Média por residente.** R$ 8.000 é o valor por residente *contado* pelo Ministério, não por residente
>   pago pela prefeitura. Dividindo o incentivo que de fato entrou pelos residentes pagos, a média foi
>   **R$ 4.189** em mar–jun/2026, **R$ 0** em jul/2026 e **R$ 3.434** de nov/2024 a jul/2026 — abaixo da bolsa
>   em todos os meses, menos fev/2026 (`dados/incentivo_federal_media_por_residente.csv`).
> - **Todos os empenhos da bolsa são da prefeitura.** "Recurso federal" e "recurso municipal" são a *fonte*
>   que ela declara em cada empenho, e a divisão 11 + 11 não acompanha a contagem do Ministério.
> - **eAP:** o CNES de jun/2026 mostra **1** médico residente em equipe eAP (não 2); os outros 25 estão em eSF.
> - A estimativa da seção 5.3 (11 credenciados) foi **superada** pelo dado oficial da seção 5.4
>   (18 credenciados, 12 contados).
> - **Onde trava a contagem** (investigação em andamento, com o texto da portaria transcrito do DOU):
>   ver [`investigacao.md`](investigacao.md).

---

## 1. O que diz cada documento

**Lei municipal 6.516, de 29/12/2020 (Santa Maria)** — institui a “Bolsa Auxílio” aos médicos residentes
em Medicina Geral de Família e Comunidade (MFC) dos programas da UFSM e da UFN que atuam na rede municipal.
- Valor: **R$ 4.500,00/mês** para R1 e R2 (art. 7º), “corrigido anualmente conforme critérios do Ministério da Saúde” (art. 3º, §1º).
- Quem paga: **o Município, diretamente ao profissional** (art. 3º, §2º).
- Condição: pagamento **vinculado à existência do repasse federal**; o Município não é responsável solidário se o repasse não vier.
- Sem vínculo empregatício; sem 13º, férias ou adicionais; exige cadastro no CNES (art. 8º).
- Dotação: projeto/atividade **2.113000 – Manutenção dos Serviços Básicos de Saúde**, elemento **3.3.90.48 – Outros Auxílios a Pessoa Física**.

**Portaria GM/MS nº 10.193, de 29/01/2026 (publicada no DOU em 02/02/2026)** — altera as Portarias de
Consolidação GM/MS nº 6/2017 (arts. 172-E a 172-I-A) e nº 2/2017 (arts. 50 a 58) e **atualiza o incentivo
federal de custeio** para municípios com equipes da APS integradas a programas de residência em saúde.
- Valores mensais por residente (art. 172-E, §5º):
  - **R$ 8.000,00** — residente de medicina;
  - **R$ 4.000,00** — enfermagem e odontologia;
  - **R$ 3.000,00** — demais categorias do PRAPS (inciso II do §1º).
- Equipes elegíveis: eSF, eSB, eMulti, eSFF/UBSF, eSFR, eCR, eAPP, com limites por equipe (§6º: ex. eSF = até 2 de medicina + 2 de enfermagem).
- Exige: profissional regular na CNRM/CNRAPS, cursando 1º, 2º ou ano adicional, cadastro no SCNES com “05 – Residência” e “01 – Residente”, vínculo a equipe por INE, 40h semanais.
- **Credenciamento** do município pelo e-Gestor APS + portaria no DOU (art. 172-F). Sem credenciamento, não há repasse.
- **Transferência fundo a fundo**, Bloco de Manutenção; Programa de Trabalho 20.36.901.10.301.5119.219A – PO 0004 (art. 172-G).
- Suspensão após 3 competências sem produção no SIAPS ou sem cadastro regular no SCNES; cancelamento automático em hipóteses do art. 172-I.
- Antecedentes: Portaria GM/MS nº 3.510/2019 (criou o incentivo) e **Portaria GM/MS nº 4.411/2022**
  (valores anteriores: R$ 4.500 medicina; R$ 1.500 enfermagem/odontologia).

---

## 2. Fluxo do dinheiro — três trilhas

| # | Quem paga | Quanto | Para quem | Caminho |
|---|---|---|---|---|
| A | União (MEC/MS — Portaria Interministerial MEC/MS nº 9/2021) | **R$ 4.106,09/mês** (bruto, congelado desde jan/2022) | diretamente ao residente | instituição formadora (COREME/UFSM/UFN) paga a bolsa de residência |
| B | União (MS — Portaria 10.193/2026) | **R$ 8.000/mês** por residente de medicina (R$ 4.000 enfermagem/odonto; R$ 3.000 demais) | **ao Fundo Municipal de Saúde** (não ao residente) | transferência fundo a fundo, Bloco de Manutenção, após credenciamento no e-Gestor APS |
| C | Município (Lei 6.516/2020) | **R$ 4.500/mês** por residente | diretamente ao residente | empenho da Secretaria de Saúde, projeto “Manutenção dos Serviços Básicos de Saúde” |

Ponto-chave: **a trilha C é paga com o dinheiro da trilha B.** Nos empenhos municipais a fonte de recurso
declarada é “Transferências Fundo a Fundo de Recursos do SUS provenientes do Governo Federal – Bloco de
Manutenção das Ações e Serviços Públicos de Saúde” (código de recurso 1600.4500). Ou seja, o município
recebe o incentivo federal e repassa parte dele ao residente como bolsa; a lei municipal, inclusive,
condiciona o pagamento à existência desse repasse.

---

## 3. Valores exatos (e o que mudou em 2026)

| | 2020–2021 | 2022–2025 | 2026 |
|---|---|---|---|
| Incentivo federal por residente de **medicina** (pago ao município) | R$ 4.500 (Portaria 3.510/2019) | R$ 4.500 (Portaria 4.411/2022) | **R$ 8.000** (Portaria 10.193/2026) |
| Bolsa municipal paga **ao residente** | R$ 4.500 | R$ 4.500 | **R$ 4.500 (não mudou)** |
| Bolsa federal de residência (MEC, paga ao residente) | R$ 4.106,09 | R$ 4.106,09 | R$ 4.106,09 |

Em 2026 o incentivo federal por residente de medicina **quase dobrou**, mas o valor da bolsa municipal
permaneceu em R$ 4.500 — a diferença fica no Fundo Municipal de Saúde.

---

## 4. Onde conferir os dados reais

| O que | Onde | URL |
|---|---|---|
| Credenciamentos do município na APS e relatórios de pagamento da APS (painel oficial do MS) | Relatórios Públicos da APS | https://relatorioaps.saude.gov.br/gerenciaaps/pagamento · API: `relatorioaps-prd.saude.gov.br` (`/credenciamento/solicitacoes-adesao/gerencia` funciona; `/financiamento/pagamento` está retornando erro 500) |
| Empenhos pagos pela prefeitura (buscar “FOLHA PGTO COLETIVA”, “MÉDICOS RESIDENTES” ou o próprio nome) | Portal da Transparência → Despesa → Empenho | https://www.santamaria.rs.gov.br/transparencia/despesa/empenho |
| Detalhe de um empenho (natureza, fonte, projeto, credor, descrição) | idem, clicar na lupa | https://www.santamaria.rs.gov.br/transparencia/despesa/empenho/{nº}/{ano} |
| Execução por natureza da despesa (TRD mensal, PDF) | Despesa por Categoria | https://www.santamaria.rs.gov.br/transparencia/despesa/despesa-por-categoria |
| API de dados abertos da prefeitura | Swagger (Despesas **quebrado** no servidor; Receitas funciona) | https://gestaodepessoal.santamaria.rs.gov.br/DADOSABERTOS/swagger/v1/swagger.json |
| Repasses federais ao município (fundo a fundo) | FNS – Consulta Detalhada de Pagamento (filtrar município + PT 20.36.901.10.301.5119.219A) | https://consultafns.saude.gov.br/#/detalhada |
| Equipes credenciadas e repasses da APS | e-Gestor APS (Relatórios Públicos) | https://egestoraps.saude.gov.br (antigo egestorab.saude.gov.br) |
| Execução orçamentária municipal em saúde (o que o município declara) | SIOPS/DATASUS | http://siops.datasus.gov.br |
| Se o residente está cadastrado na equipe (código 05 – Residência / 01 – Residente) | CNES | https://cnes.datasus.gov.br |
| Portarias de credenciamento e o texto oficial das normas | DOU / BVS MS Saúde Legis | https://www.in.gov.br · https://bvsms.saude.gov.br/bvs/saudelegis/ |

---

## 5. O que os dados municipais mostram (extraído e conferido empenho por empenho)

Empenhos da Secretaria de Município da Saúde com descrição “BOLSA AUXÍLIO, AO MÉDICO RESIDENTE…”
(2021–2022, um empenho por residente) e “BOLSAS / AUXÍLIOS AOS MÉDICOS RESIDENTES” em “folha de
pagamento coletiva” (2023–2026). Categoria contábil: “RESIDÊNCIA MÉDICA”.

| Ano | Total empenhado (bolsas) | Nº de residentes (variação no ano) |
|---|---|---|
| 2021 (abr–dez) | R$ 139.500,00 | 1 a 10 |
| 2022 | R$ 616.500,00 | 5 a 13 |
| 2023 | R$ 774.000,00 | 11 a 18 |
| 2024 | R$ 897.450,00 | 15 a 19 |
| 2025 | R$ 1.016.550,00 | 14 a 20 |
| 2026 (jan–ago) | R$ 781.500,00 | 13 a 23 |

- O valor **por residente é R$ 4.500,00 do começo ao fim** — nunca houve reajuste, apesar do art. 3º, §1º da lei e do aumento do incentivo federal em 2026.
- Desde 2025 há **dois empenhos** por mês, ambos da prefeitura: 11 residentes com fonte declarada federal (1600.4500 — dinheiro do SUS já no Fundo Municipal) e 2–12 com fonte municipal (1500 – impostos). Total 13–23 residentes/mês em 2026.
- Sobre INSS: a prefeitura paga **20% patronal sobre as bolsas** em empenho separado (ex.: R$ 13.500 em dez/2023, sobre R$ 67.500 de bolsas — descrição “VALOR REF. OBRIGAÇÃO PATRONAL (20%) SOBRE AS BOLSAS / AUXÍLIOS AOS MÉDICOS RESIDENTES”).
- Em 2021 a classificação contábil era “AUXÍLIO A PESSOAS FÍSICAS” (o 3.3.90.48 previsto na lei); depois passou a “OUTROS SERVIÇOS DE TERCEIROS – PESSOA FÍSICA” (3.3.90.36), o que faz o elemento 3.3.90.48 aparecer como R$ 0,00 nos relatórios anuais recentes.

Dados completos: `dados/bolsa_empenhos_coletivos_2023_2026.csv` (empenho por empenho, com link do detalhe)
e `dados/bolsa_residentes_por_mes.csv` (agregado mensal).

---

### 5.1 Quantos residentes existem (UFSM e UFN)

| Instituição | Vagas por ano (R1) | Observação |
|---|---|---|
| UFSM — MFC (2 anos) | 7 | edital 034/2025 (ingresso 2026); R1+R2 = até 14 |
| UFSM — ano adicional (R3) | 1 | idem |
| UFN — MFC (2 anos) | 4 | **a turma atual está menor que o edital** |
| **Pagos pela prefeitura (fato, dos empenhos)** | | **23 em mai–jun/2026 e 22 em ago/2026** |

As vagas por ano vêm dos editais; o número factual é o de pagamentos por competência (acima).
Como a turma atual da UFN está menor que o edital, convém confirmar com as COREMEs quem compõe o total
pago (R1, R2, ano adicional e eventuais prorrogações).

### 5.2 Residentes em eAP ficam fora do incentivo federal

A Portaria GM/MS 10.193/2026 (art. 172-E, §3º) admite o cadastro de residentes, para fins do incentivo,
**apenas** nas equipes **eSF, eSB, eMulti, eSFF da UBSF, eSFR, eCR e eAPP**. A **equipe de Atenção Primária
(eAP) não está na lista** — o residente do município cadastrado em equipe eAP (1, segundo o CNES de jun/2026), portanto, não gera o repasse
federal de R$ 8.000/mês. Como a lei municipal (art. 3º, §2º) condiciona a bolsa à existência do repasse
federal, esse é o grupo mais exposto. Conferir no CNES (cnes.datasus.gov.br) em qual equipe/INE cada
residente está cadastrado e levar o caso à Secretaria de Saúde e à coordenação do programa.

### 5.3 O que entra para o município

> *Superada pela seção 5.4 (dado oficial do MS: 18 credenciados, 12 contados em mar–jun/2026). Mantida como registro.*

O relatório “Recursos Recebidos” da prefeitura (https://www.santamaria.rs.gov.br/transparencia/contas-publicas/rr)
mostra o bloco federal da Atenção Primária — **R$ 1.338.156,11 em ago/2026** e **R$ 13.486.692,62 no ano** —
mas **não abre o incentivo de residência em linha separada**. Estimativa, supondo 11 residentes credenciados
(os pagos com recurso federal 1600.4500): entra ≈ R$ 88.000/mês (11 × R$ 8.000) e saem R$ 99.000 em bolsas
para 22 residentes → o município ainda cobre ≈ R$ 11.000/mês com recursos próprios. Antes do aumento (2025),
entravam ≈ R$ 49.500 e a cobertura municipal era de ≈ R$ 36.000–40.500/mês. Ou seja: o aumento federal
aliviou o caixa do programa, mas não o bolso do residente. O número exato de credenciados precisa ser
confirmado no e-Gestor APS e no DOU (ou via LAI).

### 5.4 O incentivo federal efetivamente recebido (dado oficial — planilha do MS)

Fonte: planilhas do painel público de pagamentos da APS (aba “Residência”), baixadas em 13/10/2026 —
arquivos `Excell relatorioaps saude gov/download-pagamento-*.xlsx`.

| Competência | Residentes credenciados | Residentes pagos | Incentivo federal recebido | Bolsa paga pela prefeitura | Diferença |
|---|---|---|---|---|---|
| NOV/2024 | 18 | 11 | R$ 49.500,00 | R$ 72.000,00 | −22.500,00 |
| DEZ/2024 | 18 | 10 | R$ 45.000,00 | R$ 72.000,00 | −27.000,00 |
| JAN/2025 | 18 | 10 | R$ 45.000,00 | R$ 74.700,00 | −29.700,00 |
| FEV/2025 | 18 | 6 | R$ 27.000,00 | R$ 63.000,00 | −36.000,00 |
| MAR/2025 | 15 | 8 | R$ 36.000,00 | R$ 82.350,00 | −46.350,00 |
| ABR–SET/2025 | 15 | 14 | R$ 63.000,00 (cada) | R$ 90.000,00 (cada) | −27.000,00 (cada) |
| OUT/2025–JAN/2026 | 18 | 17 | R$ 76.500,00 (cada) | R$ 85.500,00 (cada) | −9.000,00 (cada) |
| **FEV/2026** | 18 | 17 | **R$ 136.000,00** (17 × R$ 8.000) | R$ 85.500,00 | **+50.500,00** |
| MAR/2026 | 18 | 12 | R$ 96.000,00 | R$ 58.500,00 | +37.500,00 |
| ABR/2026 | 18 | 12 | R$ 96.000,00 | R$ 147.000,00 | −51.000,00 |
| MAI/2026 | 18 | 12 | R$ 96.000,00 | R$ 103.500,00 | −7.500,00 |
| JUN/2026 | 18 | 12 | R$ 96.000,00 | R$ 103.500,00 | −7.500,00 |
| **JUL/2026** | 18 | **0** | **R$ 0,00** | R$ 99.000,00 | −99.000,00 |
| **Total** | | | **R$ 1.406.500,00** | **R$ 1.843.050,00** | **−436.550,00** |

Três leituras importantes:

1. **O valor de R$ 8.000 por residente entrou em fev/2026** (R$ 136.000 = 17 × R$ 8.000) — confirma os
   efeitos financeiros da Portaria GM/MS 10.193/2026.
2. **Entre mar e jun/2026 só 12 residentes geraram incentivo**, embora a prefeitura tenha pago bolsa a
   22–23 no período: cerca de 10 residentes são custeados com recursos próprios do município. É aqui que
   os residentes fora de equipe elegível (ex.: eAP) aparecem no orçamento.
3. **Jul/2026: incentivo zerado.** O plano orçamentário “Demais programas, serviços e equipes da Atenção
   Primária” foi transferido com R$ 0,00, enquanto todos os outros planos da APS seguiram normais no mesmo
   mês (eSF+eAP R$ 931.126,00; saúde bucal R$ 72.387,49; eMulti R$ 15.000,00; ACS R$ 343.652,00; per capita
   R$ 140.020,85). Como a planilha foi baixada em 13/10/2026, não se trata de atraso da mesma semana.
   Hipóteses previstas no art. 172-H (3 competências sem produção no SIAPS; cadastro irregular no SCNES;
   ausência de cadastro de novo residente) precisam ser apuradas com a gestão.

No acumulado (nov/2024 a jul/2026) o município recebeu R$ 1.406.500,00 de incentivo e pagou R$ 1.843.050,00
em bolsas — desembolsando R$ 436.550,00 a mais do que recebeu. Ou seja: **o aumento federal de 2026 melhorou
o caixa do programa, mas não cobriu toda a folha** — e não houve repasse do aumento aos residentes.

## 6. Dúvidas e pontos que os documentos não esclarecem

1. **Reajuste**: o art. 3º, §1º manda corrigir “conforme critérios do MS”, mas nenhum ato municipal aplicou correção — o valor está em R$ 4.500 desde 2020, mesmo com o incentivo federal por residente em R$ 8.000 (2026). Quais “critérios do MS” seriam esses e por que não foram aplicados?
2. **Destinação do aumento federal**: a lei não diz que o valor recebido a mais deve ser repassado ao residente. Com o incentivo em R$ 8.000 e a bolsa em R$ 4.500 por residente credenciado, o excedente de até R$ 3.500/residente/mês fica no Fundo Municipal de Saúde — na prática, ajudando a cobrir a parcela da folha que hoje sai de recursos próprios (ver 5.3). Não há, na lei, vinculação desse aumento ao profissional.
3. **Credenciamento**: não localizei portaria de credenciamento de Santa Maria especificamente para o incentivo de residência (art. 172-E). O município usa recursos “fundo a fundo – Bloco de Manutenção” para pagar as bolsas, mas quantos residentes estão efetivamente credenciados precisa ser conferido no e-Gestor APS e no DOU.
4. **Elemento de despesa**: a lei fixou 3.3.90.48, a execução usa 3.3.90.36 (“Outros serviços de terceiros – pessoa física”). Isso muda a natureza jurídica do gasto (bolsa x serviço) e dificulta o rastreamento pelo elemento previsto na própria lei.
5. **Previdenciário**: a prefeitura paga 20% patronal sobre as bolsas (tratando como remuneração), mas não há clareza sobre desconto de 11% no valor do residente nem sobre o tratamento tributário — o §3º da lei diz que não há parcelas trabalhistas, o que não resolve a questão previdenciária.
6. **Paralisação do repasse**: como o pagamento municipal é condicionado ao repasse federal, uma suspensão do incentivo (art. 172-H: 3 competências sem produção no SIAPS ou sem cadastro no SCNES) pode interromper a bolsa dos residentes sem que a lei defina o que acontece nesse caso.
7. **Quem entra e quem fica de fora**: em 2026 foram pagos 19–23 residentes; a lei fala apenas em R1 e R2 dos programas da UFSM e da UFN. Residentes de ano adicional (R3), de outras especialidades ou de outros programas não estão claramente contemplados.
8. **INSS de 11%**: como saber o que foi descontado. Ver seção 7.

---

## 7. Como verificar o INSS da bolsa

1. **Contracheque / recibo de pagamento** do órgão pagador (prefeitura ou COREME/UFSM/UFN): mostra o bruto, o desconto e o líquido.
2. **Meu INSS** — https://meu.inss.gov.br → “Extrato de Contribuição (CNIS)”: lista mês a mês as contribuições feitas em seu nome (empregador e valor). Se a bolsa tiver contribuição, aparece ali.
3. **Informe de Rendimentos** do ano (fornecido pelo pagador da bolsa).
4. **Prefeitura**: e-mail/telefone do Fundo Municipal de Saúde / Gestão de Pessoas (a folha é paga como “folha de pagamento coletiva”, então o setor responsável é a Secretaria de Município da Saúde junto com a Fazenda).

Tratamento esperado (checar com os comprovantes): residente é contribuinte individual — a bolsa de
residência é **isenta de imposto de renda**, mas costuma haver contribuição previdenciária; de
R$ 4.106,09 o desconto de 11% resultaria em ≈ R$ 3.654,42 líquidos. Se você recebe ~R$ 4 mil “e
quebrados”, vale identificar se é o valor bruto de R$ 4.106,09 (bolsa federal paga pela instituição),
a bolsa municipal de R$ 4.500,00 com algum desconto, ou a soma de dois pagamentos.
