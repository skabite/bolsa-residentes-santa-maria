# Como verificar cada afirmação, de forma independente

Guia para quem quer conferir o dossiê sem confiar nele: cada afirmação central, a fonte primária
pública, o caminho para chegar lá e o estado da verificação em **03/11/2026**. Na página, cada fonte da
[lista de fontes](https://skabite.github.io/bolsa-residentes-santa-maria/fontes.html) mostra o mesmo estado
(registro em `dados/fontes.json`).

Estados:
- **Conferido na fonte primária:** documento oficial lido, com link ou código de autenticidade.
- **Conferido em reprodução:** o texto foi lido numa cópia fiel (site de terceiro, PDF hospedado
  por outro), não no site do órgão.
- **A conferir:** ainda falta abrir o documento original. Não usar em ofício antes disso.

Os sites do governo podem não abrir no ambiente onde o dossiê é montado. A coleta de 03/11/2026 usou a API
do painel de pagamentos e os serviços públicos do CNES; as respostas brutas estão em `dados/brutos/2026-11-03/`.
Quem preferir pode refazer o caminho num navegador comum; são poucos passos, descritos abaixo.

---

## 1. O núcleo do pedido (conferir antes de qualquer ofício)

| # | Afirmação | Fonte primária e caminho | Estado |
|---|---|---|---|
| 1 | A lei municipal prevê **correção anual** da bolsa (art. 3º, §1º) e liga o pagamento ao repasse federal | Lei municipal 6.516, de 29/12/2020. Site da Câmara (camara-sm.rs.gov.br) → Atividades legislativas → Legislação → Lei → buscar "6516" (página: <https://camara-sm.rs.gov.br/atividades-legislativas/legislacao/lei/70865/lei-n--6516-2020>) | Conferido na fonte primária (site da Câmara, 29/10/2026; texto integral e .doc oficial). Art. 3º, §1º: "O valor da Complementação será corrigido anualmente conforme critérios formalizados pelo Ministério da Saúde." O §2º vincula o pagamento à pré-existência do repasse federal |
| 2 | A bolsa está em **R$ 4.500 desde 2021**, sem correção | Portal da Transparência de Santa Maria → Despesa → Empenho → unidade Secretaria de Município da Saúde → buscar "FOLHA PGTO COLETIVA". Cada empenho em `dados/bolsa_empenhos_coletivos_2023_2026.csv` tem o link oficial (coluna `link_detalhe`) | Conferido na fonte primária (empenhos de abr/2021 a out/2026; valor ÷ residentes declarados = R$ 4.500) |
| 3 | O Ministério repassa **R$ 8.000 por residente de medicina contado** desde fev/2026 | Portaria GM/MS 10.193/2026, DOU nº 22 de 02/02/2026, Seção 1, p. 104. Autenticidade: código **05152026020200104** em in.gov.br/autenticidade.html | Conferido na fonte primária (página do DOU). Transcrição em `dados/portaria_10193_2026_arts_172E_172IA.md` |
| 4 | Requisitos para contar: CNRM regular, CNES "Residência/Residente", equipe elegível, 40 h, até 2 por eSF; cadastro é responsabilidade da gestão (172-F, §5º); suspensão após 3 competências (172-H) | Mesma portaria, arts. 172-E a 172-H | Conferido na fonte primária |
| 5 | **18 vagas credenciadas**; contados: 17 (out/2025–fev/2026), **12** (mar–jun/2026), **0** (jul e ago/2026); set/2026 ainda não publicado | Painel de pagamentos da APS (relatorioaps.saude.gov.br/gerenciaaps/pagamento) → município Santa Maria/RS → planilha → aba **Residência**; API com `nuParcelaInicio`/`nuParcelaFim` (parcela AAAAMM = competência + 2 meses) | Conferido na fonte primária (planilha em 13/10/2026; API em 03/11/2026). Ago/2026: 18 credenciados, 0 pagos e R$ 0 |
| 6 | O dinheiro entra no Fundo Municipal entre os dias 13 e 17, cerca de dois meses depois; as competências jul e ago/2026 não tiveram crédito (parcelas 09 e 10 não emitidas na ação 69166) | Portal da prefeitura → Contas públicas → Recursos recebidos (Lei 9.452/97); conferência independente no FNS (consultafns.saude.gov.br) → 2026 → Fundo a Fundo → bloco Manutenção → ação 69166 | Conferido no FNS em 03/11/2026: 8 créditos, R$ 749.500, o último em 14/08/2026. O relatório "Recursos recebidos" da prefeitura só traz o total da APS, sem separar a residência; não serve para esta conferência |
| 7 | Folha de **R$ 118.800/mês** = 22 × R$ 4.500 + 20% de INSS patronal | Empenhos da bolsa de ago/2026 (dois de R$ 49.500) e empenho do INSS **18203/2026** (R$ 19.800,01), no Portal da Transparência | Conferido na fonte primária |

## 2. Referências de valor

| # | Afirmação | Fonte e caminho | Estado |
|---|---|---|---|
| 8 | Bolsa federal: R$ 3.330,43 → **R$ 4.106,09** (+23,29%) a partir de jan/2022 | Portaria Interministerial MEC/MS nº 9, de 13/10/2021, DOU de 15/10/2021. Buscar em in.gov.br pelo título | Conferido em reprodução (ABMES) e em edital vigente (Fiocruz 2026). **A conferir** no DOU |
| 9 | Inflação (IPCA) de jan/2021 a set/2026: cerca de +38,4% → **≈ R$ 6.228** | Calculadora do Cidadão do Banco Central (bcb.gov.br → Calculadora do Cidadão → Correção de valores → IPCA, 12/2020 a 09/2026, valor 4.500) | Estimativa feita com as taxas anuais do IBGE. **Conferir o valor exato** na calculadora (a diferença deve ser de poucos reais) |
| 10 | Com 18 contados, o incentivo cobre bolsa de **R$ 5.454** para 22 residentes (ago/2026; com 21, R$ 5.714) | Conta: 18 × 8.000 = 144.000; 144.000 ÷ (22 × 1,2) = 5.454,55; com 21, 144.000 ÷ (21 × 1,2) = 5.714,29 | Conta sobre os itens 3, 5 e 7 |
| 11 | Mais Residências: bolsa-formação de **R$ 4.000/mês** paga pelo Ministério ao residente que faz o curso de preceptoria, se o programa aderiu | Edital SGTES/MS nº 10/2026 e comunicado aos residentes de MFC (gov.br/saude → Chamamentos públicos 2026) | Conferido na página do edital |

## 3. O que trava a contagem

| # | Afirmação | Fonte e caminho | Estado |
|---|---|---|---|
| 12 | 23 médicos residentes registrados no CNES em nov/2026 (26 em jun/2026): 22 em eSF e 1 em eAP | CNES (cnes.datasus.gov.br) → Consultas → Estabelecimentos → cada unidade → abas Profissionais e Equipes; ou serviços `estabelecimentos-profissionais` e `estabelecimentos-equipes` | Conferido em contagem agregada (15 unidades, 03/11/2026) |
| 13 | Uma equipe com 3 residentes (São Francisco, INE 0001662821); em São José, a equipe que tinha 3 passou a 2; quatro registros abaixo de 40 h; todos os 23 em alguma equipe | Contagem agregada dos serviços do CNES, sem nomes | Conferido em **15 de 15 unidades** (03/11/2026), em contagem agregada |
| 14 | A queda de 17 para 12 coincide com a entrada da turma de mar/2026 (12 matrículas anteriores + 11 novas) | Planilha do item 5 (a queda). A composição das turmas é **informação dos residentes, não oficial**; só as COREMEs podem confirmar | Fato: a queda. **Não oficial:** a composição. Causa **em aberto** (pedido ao Ministério via Fala.BR em andamento) |
| 15 | O residente precisa *cumprir* 40 h semanais "na composição" da equipe (eSF e as outras listadas); o cadastro no CNES é da gestão | Portaria 10.193/2026, art. 172-F, §§ 5º e 6º; Portaria 4.411/2022, art. 172-E, §§ 9º e 10 (<https://bvsms.saude.gov.br/bvs/saudelegis/gm/2022/prt4411_22_12_2022.html>) | Conferido na fonte primária. A exigência não nasceu em 2026: a Portaria 4.411/2022 (art. 172-E, §10) já exigia a carga horária mínima da composição; o "40 (quarenta) horas" literal só aparecia para eSB (§9º) |
| 16 | A residência médica tem no máximo 60 h semanais (por isso cabe estágio externo em parte da semana com 40 h na equipe) | Lei 6.932/1981, art. 5º: planalto.gov.br/ccivil_03/leis/l6932.htm | Conferido na fonte primária (Planalto, 29/10/2026): "máximo de 60 (sessenta) horas semanais", com "um máximo de 24 (vinte e quatro) horas de plantão" |
| 17 | Com 22 pagos (ago/2026) e 18 vagas, até 4 residentes podiam ficar fora da conta no mesmo mês sem perda de repasse; com 21 (set–out/2026), até 3 | Conta sobre os itens 5 e 7 e o art. 172-E, § 2º | Estimativa |
| 18 | Jul e ago/2026 com **zero registrado**: 18 credenciados, 0 pagos e R$ 0; o plano "Demais programas, serviços e equipes da APS" veio com integral 0, desconto 0 e repasse 0 | API do painel de pagamentos da APS: `nuParcelaInicio=202609&nuParcelaFim=202610` | Conferido na fonte primária em 03/11/2026; não é dado ausente nem glosa |

## 4. Comparação com outros municípios

São contexto, não base do pedido. No ofício, citar no máximo os conferidos.

| Município | Valor | Estado |
|---|---|---|
| Porto Alegre | R$ 3.619,57 + R$ 550 (editais de 2022 a 2025) | Conferido em editais da prefeitura. O edital para 2027 pode ter mudado o valor: abrir antes de citar |
| Rio de Janeiro | até R$ 8.260,41 (teto, Resolução SMS 5.297/2022) | Conferido em resumo do PDF oficial; quanto se paga de fato é desconhecido |
| Cachoeiro de Itapemirim | até o total de R$ 10.000 (Lei 8.203/2025) | Conferido em resumo do PDF do Diário Oficial; abrir o PDF para a redação exata |
| Ijuí | R$ 6.000 (Lei 6.745/2019, alterada em 2023) | **A conferir** no PDF consolidado; houve outra alteração em 2025 não localizada |
| Santos | R$ 5.227,32 (edital de 2024) | Conferido em cópia do edital; em 2026 uma lei nova pode ter substituído a bolsa |
| Remígio, Distrito Federal | R$ 5.000; R$ 7.536 | **A conferir** (verificação independente não concluída) |

---

## Antes de enviar um ofício, o mínimo

1. Usar o texto literal do art. 3º da Lei 6.516/2020, já conferido (item 1).
2. Conferir o IPCA exato na Calculadora do Cidadão (item 9).
3. Baixar de novo a planilha/API do Ministério para ver set/2026 (item 5); ago/2026 já foi conferido em 03/11/2026.
4. Não afirmar a composição das turmas nem a causa da queda: perguntar.
5. O art. 5º da Lei 6.932/1981 já está conferido (item 16).

---

## Atualizar os dados

**Estado em 03/11/2026.** Os itens 1 a 4 foram resolvidos nesta data; o que ainda falta está marcado.

1. **Planilha de pagamentos da APS (Ministério) — resolvido em 03/11/2026.** A API voltou a responder com os
   parâmetros novos, que usam a **parcela** (AAAAMM = competência + 2 meses), não a competência:
   `https://relatorioaps-prd.saude.gov.br/financiamento/pagamento?unidadeGeografica=MUNICIPIO&coUf=43&coMunicipio=431690&nuParcelaInicio=202601&nuParcelaFim=202610&tipoRelatorio=COMPLETO`
   Resultado: **ago/2026** com 18 credenciados, **0 pagos** e R$ 0; **set/2026 ainda não publicado**. A planilha do
   painel continua sendo a via alternativa. Os parâmetros antigos `nuCompInicio`/`nuCompFim` dão erro 500.
2. **Créditos na conta do município — resolvido em 03/11/2026.** A
   [consulta detalhada do FNS](https://consultafns.saude.gov.br/#/detalhada) (ano 2026, Fundo a Fundo, bloco
   Manutenção, CNPJ 12.964.512/0001-57, ação 69166) mostra **8 créditos, R$ 749.500**, o último em **14/08/2026**.
   Não há parcelas 09 e 10 nessa ação; não é atraso do FNS, porque a ação 69182 (eSF/eAP) recebeu a 09 em
   10/09/2026 (R$ 931.126) e a 10 em 14/10/2026 (R$ 952.126). O relatório mensal "Recursos Recebidos" da
   prefeitura só traz o total da Atenção Primária, sem separar a residência; **não serve para esta conferência**.
   O FNS serve.
3. **Empenhos da bolsa de set e out/2026 — resolvido em 03/11/2026.** Em outubro, os empenhos 22817/2026
   (R$ 49.500, 11 residentes) e 22818/2026 (R$ 45.000, 10 residentes) estão **pagos integralmente**: R$ 94.500,
   21 residentes. Empenhos de nov/2026 ainda não existiam nessa data (saem por volta do dia 25).
4. **CNES das 15 unidades — resolvido em 03/11/2026, em contagem agregada.** Total de **23** médicos residentes
   (eram 26 em jun/2026); São José caiu de 5 para 3 e São João de 1 para 0; todos estão em alguma equipe; 4
   cadastros abaixo de 40 h (só o total agregado, sem unidade); uma equipe com 3 (São Francisco, INE 0001662821).
   A contagem não traz nomes e não substitui a ficha individual. Arquivos:
   `dados/cnes_residentes_por_unidade_nov_2026.csv` e `dados/cnes_residentes_por_equipe_nov_2026.csv`.
5. **Texto da Lei 6.516/2020** (item 1) — [Câmara de Vereadores](https://camara-sm.rs.gov.br/atividades-legislativas?tipo=legislacao&subtipo=lei&ano=0)
   → buscar 6516 → PDF da lei.
6. **Para a questão das 40 horas — ainda em aberto.**
   [Portaria GM/MS 4.411/2022](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2022/prt4411_22_12_2022.html) (a regra
   de horas já existia antes de 2026?),
   [nota técnica do Ministério sobre o recurso de residência na APS, 2023](https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2023/sei_ms-0024042088-nota-tecnica.pdf)
   e [PNAB 2017](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2017/prt2436_22_09_2017.html) (procurar "8 (oito)
   horas" e "residência"). A regra já existia antes de 2026; falta a resposta do Ministério sobre estágio externo
   e soma de horas em mais de uma equipe elegível.

Depois de incluir os dados nos CSVs, atualizar `dados/situacao_dos_dados.csv` (período coberto e data da coleta) e
rodar `python3 scripts/montar_site.py`, que refaz gráficos e tabelas em todas as páginas.
