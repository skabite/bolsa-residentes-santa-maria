# Caderno de investigação — onde trava o incentivo federal

Estado em **15/10/2026**. Este arquivo é a memória de trabalho entre sessões: o que já foi
estabelecido, o que é hipótese, o que foi descartado e o que falta. A página pública (`index.html`)
só recebe o que estiver confirmado. Sem nomes de pessoas — residentes aparecem por papel (R1/R2/R3) e unidade.

## A pergunta

Santa Maria tem **18 vagas credenciadas** e paga bolsa a **22–23 residentes** de MFC, mas o Ministério
da Saúde contou **12** residentes em mar–jun/2026 e **0** em jul/2026 (planilha do painel de pagamentos
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
  2026 — caiu para 12 em mar/2026 e parou; 0 em jul/2026.
- **Repasse federal não é retroativo**: em todas as competências o valor = contados × valor unitário;
  nenhum acerto posterior aparece. Mês não contado = dinheiro perdido. A bolsa municipal, sim, é paga
  com retroativo.
- **Composição real** (informada pelo usuário, que é residente do programa; UFN R2 = 4 confere com o
  resultado publicado da seleção):

  | Grupo | Quantos |
  |---|---|
  | Matrícula anterior a mar/2026: 7 R2 UFSM + 4 R2 UFN + 1 R2 que ficou até ago/2026 | **12** |
  | Matrícula iniciada em mar/2026: 7 R1 UFSM + 3 R1 UFN + 1 R3 (ano adicional, vinda de outro programa) | **11** |
  | Total abr–jun/2026 (bate com os 23 pagos pela prefeitura) | 23 |
  | Hoje (depois da saída de ago/2026): 15 UFSM + 7 UFN | 22 |

- **CNES de 15/10/2026** (fichas públicas de São José, São Francisco e Victor Hoffmann; resumo agregado):
  - Todos os R1 têm cadastro **correto**: CBO 2231F9, vínculo Residência/Residente, 40h, equipe eSF,
    entrada em **10/03/2026** (a turma de 2025 entrou em 07/03/2025 com o mesmo cadastro e foi reconhecida).
  - A maioria dos R2 está com 40h. **Dois residentes estão abaixo de 40h** (um R2 e o R3).
  - **Duas equipes têm 3 residentes de medicina** (limite 2): São José equipe 16 (INE 0000433012) e São
    Francisco equipe 30 (INE 0001662821).
  - Um **registro de residente que já saiu do programa (ago/2026) continua ativo** na São José equipe 16,
    ocupando uma das 2 vagas da equipe.
  - Caracterização: São José consta como "UNIDADE SEM ATIVIDADE DE ENSINO"; São Francisco como "UNIDADE
    AUXILIAR DE ENSINO". Não se sabe se o MS confere isso.
- **Todos os empenhos da bolsa são da prefeitura**; "federal" × "municipal" é só a fonte declarada
  (1600 – Bloco de Manutenção × 1500 – impostos). A divisão 11 + 11 não acompanha a contagem do MS.
- **Média federal de fato por residente pago**: R$ 4.189 (mar–jun/2026), R$ 0 (jul/2026), R$ 3.434
  (nov/2024–jul/2026) — abaixo da bolsa em todos os meses menos fev/2026.

## Hipóteses, em ordem

1. **Matrícula da turma de 2026 não reconhecida (CNRM)** — principal. Os 12 contados são exatamente quem
   tinha matrícula antes de mar/2026; os 11 que começaram em mar/2026 (UFSM, UFN e a R3) não aparecem.
   O cadastro CNES dos R1 está correto, então o único requisito individual que sobra é o § 4º, I–II do
   172-E (situação regular na CNRM). Contra: exigiria falha simultânea de programas diferentes; pode
   ser também a forma como o MS passou a ler o CNRM com a portaria nova (fev/2026).
2. **Carga horária < 40h** (art. 172-F § 6º) — real, mas explica no máximo 2 pessoas.
3. **Limite de 2 por eSF** — explica 2 (um R1 na São José 16, um na São Francisco 30), e o registro de
   quem já saiu agrava o caso da São José.
4. **Zero de jul/2026 = suspensão do art. 172-H** depois de 3 competências com residentes "irregulares"
   (mar/abr/mai ou abr/mai/jun). Se for isso, regularizar os cadastros destrava (sem retroativo).
   Não confirmado: o texto não diz se a suspensão é do incentivo inteiro ou por vaga.

**Descartadas**: cadastro ausente; INE ausente; equipe não homologada (os 17 INEs com residentes estão
homologados); modalidade eAP como causa principal (só 1 residente em eAP); vínculo errado nos R1;
carga horária como causa geral (R2 de outras unidades têm 40h); "R3 era R2 interna" (ela é externa);
"residente que saiu continuava no CNES em julho" (ela saiu em agosto — julho estava certo; corrigido
na página).

## Próximos passos

- **Gestor (e-Gestor APS)**: quais residentes foram validados em cada competência e o motivo dos não
  validados; motivo do zero de jul/2026; se o credenciamento (18) precisa ser ampliado/atualizado.
  Correções que não dependem de nada: dar baixa do registro de quem saiu em ago/2026; resolver as duas equipes
  com 3 residentes (art. 172-F § 4º permite mudar de equipe homologada); alinhar a carga horária dos
  dois residentes abaixo de 40h com a dos colegas.
- **COREMEs (UFSM e UFN)**: situação da turma de 2026 (R1 e R3) no SisCNRM e desde quando. Perguntar
  também se aderiram ao **Edital SGTES/MS nº 10/2026 (Mais Residências)**: bolsa-formação de
  R$ 4.000/mês paga pelo MS direto ao residente que fizer o curso de preceptoria em MFC, se o programa
  tiver aderido (residentes matriculados em abr/2026; Portaria GM/MS 8.403/2025).
- **LAI**: pedido ao Ministério já protocolado pelo usuário no Fala.BR (antes de 15/10/2026; prazo
  20 + 10 dias). Ao chegar a resposta, comparar com as hipóteses acima.
- **Dados a atualizar quando houver acesso**: empenho de set/out/2026 (`scripts/check_empenho_residentes.py`);
  planilha do MS com ago/set/2026; fichas CNES das outras 12 unidades com residentes (lista de CNES em
  `dados/cnes_medicos_residentes_por_unidade.csv`) para fechar o 26 × 22.

## Perguntas em aberto ao usuário

- A folha de jul/2026 teve 22, mas havia 23 pessoas no programa. Quem ficou sem a bolsa de julho?
- Por que um R2 está abaixo de 40h no CNES se os outros R2, com o mesmo rodízio, estão com 40h?

## Registro das sessões

- **13/10/2026** — dossiê, empenhos, planilha do MS, CNES (26 registrados), homologação dos INEs, LAI.
- **15/10/2026** — revisão: gráfico por residente refeito com a média real; manchete corrigida
  ("R$ 8.000 por residente que o Ministério conta"); empenhos explicados como todos municipais; caso
  do CNES de julho retirado; texto da Portaria 10.193/2026 transcrito; padrão "matrículas de 2026 não
  contadas" identificado; fichas CNES de 3 unidades analisadas.
