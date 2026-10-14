# Pedido de informação ao Ministério da Saúde (Fala.BR) — incentivo de residência na APS

**Canal:** https://falabr.cgu.gov.br → "Registrar manifestação" → **Acesso à Informação** →
órgão: **Ministério da Saúde** · **Base legal:** Lei nº 12.527/2011 — resposta em 20 dias, prorrogáveis por mais 10.
**Assunto:** incentivo financeiro adicional de custeio a equipes de saúde integradas a programas de
residência em saúde na APS (art. 172-E da Portaria de Consolidação GM/MS nº 6/2017, com a redação da
Portaria GM/MS nº 10.193/2026) — **Município de Santa Maria/RS (IBGE 431690)**.

**Motivação.** Documentos públicos mostram divergência entre a base cadastral e o valor pago: em junho e
julho de 2026 o CNES registra **26 médicos residentes** no Município, dos quais **25 vinculados a equipes
eSF** cujos **INEs estão homologados** (arquivo público de INEs homologados), ao passo que a planilha de
pagamento da APS registra **12 residentes pagos** (mar–jun/2026) e **zero** na competência jul/2026, com
**18 residentes credenciados**. O relatório público de pagamento da APS
(`relatorioaps.saude.gov.br/gerenciaaps/pagamento`) está com a API indisponível (erro 500 em todos os
filtros), o que impede a conferência pela via ordinária.

## Pedidos

**1. Valores por competência.** Relação das competências de **nov/2024 até a mais recente disponível**, com:
valor calculado e valor efetivamente transferido ao Município de Santa Maria/RS a título do incentivo do
art. 172-E, por categoria profissional (medicina; enfermagem; odontologia; demais categorias), número da
parcela e data da transferência.

**2. Memória de cálculo da contagem.** Para cada uma dessas competências, informe:
   a) o **quantitativo de residentes considerados** no cálculo, por tipo de equipe (eSF, eSB, eMulti,
      eSFF, eSFR, eCR, eAPP), com os respectivos **INEs**;
   b) o **quantitativo de residentes credenciados** para o Município e **como se apura esse teto**
      (qual ato o fixou);
   c) **quais residentes registrados no SCNES deixaram de ser computados** e por qual motivo, indicado
      item a item em relação aos requisitos do art. 172-E, §4º (situação regular na CNRM/CNRAPS;
      ano do programa; código “05 – Residência”/“01 – Residente”; vínculo a equipe por INE) e do §6º
      (limite por equipe).

**3. Queda da contagem em mar/2026 e zeramento em jul/2026.** Esclarecer especificamente:
   a) por que a contagem passou de **17 residentes** (nov/2025 a fev/2026) para **12** a partir de
      **mar/2026** — mês em que ocorreu a troca de turma dos programas;
   b) por que a competência **jul/2026** foi calculada com **valor zero**, enquanto os demais componentes
      da APS na mesma competência tiveram valores normais;
   c) se houve **suspensão total ou parcial** da transferência (art. 172-H) ou **cancelamento**
      (art. 172-I), com a motivação, as equipes (INE) afetadas, as competências e as providências
      exigidas para restabelecimento.

**4. Fonte dos dados da contagem.** Informar qual base o Ministério utiliza para apurar o quantitativo de
residentes por competência (SCNES de qual competência; registro da CNRM/CNRAPS; produção no SIAPS) e qual
desses requisitos faltou, no caso de Santa Maria/RS, para os residentes não computados em mar–jul/2026.

**5. Regularidade dos programas.** Informar se os programas de residência em Medicina de Família e
Comunidade das instituições formadoras que atuam no Município (**UFSM** e **UFN — Universidade Franciscana**)
estão com situação regular na CNRM/CNRAPS e, em caso negativo, qual a pendência e sua implicação no
incentivo.

**6. Credenciamento.** Número e data da portaria de credenciamento do Município publicada no **DOU**
(art. 172-F), quantitativo de residentes credenciados, eventuais alterações posteriores e a
disponibilidade orçamentária considerada (art. 172-F, §1º).

**7. Efeitos financeiros do novo valor.** Confirmação da data de início dos efeitos financeiros do valor de
**R$ 8.000,00** por residente de medicina (Portaria GM/MS nº 10.193/2026) e o total transferido ao
Município a esse título desde então.

## Observações

- Os dados pedidos são **de execução orçamentária e de cadastro público**, não envolvendo dados pessoais
  sensíveis; quando a resposta envolver nome de profissional, admite-se a apresentação **sem nome**,
  mantendo-se CNS/matrícula anonimizados, INE, categoria, competência e datas.
- Resposta preferencialmente em **planilha (CSV/XLSX)**, ou com indicação de link direto ao relatório.
- Registre-se que o painel público de pagamentos da APS apresentou **erro HTTP 500** no endpoint
  `/financiamento/pagamento` em consultas realizadas em 13 e 14/10/2026, para todos os filtros (inclusive
  Brasil), enquanto os módulos de cobertura respondiam normalmente — razão pela qual o pedido é formulado
  por este canal.
