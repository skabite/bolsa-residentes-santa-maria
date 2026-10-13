# Pedido de informação ao Ministério da Saúde (Fala.BR) — incentivo federal de residência na APS

**Canal:** https://falabr.cgu.gov.br (Plataforma Integrada de Ouvidoria e Acesso à Informação)
→ "Registrar manifestação" → **Acesso à Informação** → órgão: **Ministério da Saúde**
**Base legal:** Lei nº 12.527/2011 (LAI) — resposta em 20 dias, prorrogáveis por mais 10.
**Por que este pedido:** o painel oficial de pagamentos da APS
(https://relatorioaps.saude.gov.br/gerenciaaps/pagamento) está com o relatório de pagamento
fora do ar (a API responde erro 500 para qualquer filtro), e o e-Gestor legado foi desativado.
Este pedido obtém os mesmos dados por outra via, independentemente do painel voltar.

---

Assunto: **Valores do incentivo financeiro adicional de custeio a equipes de saúde integradas a
programas de residência em saúde na Atenção Primária (art. 172-E da Portaria de Consolidação GM/MS
nº 6/2017, com a redação da Portaria GM/MS nº 10.193/2026) — Município de Santa Maria/RS
(IBGE 431690)**

Solicito, com fundamento na Lei nº 12.527/2011:

1. **Valores transferidos**, por competência (parcela), de janeiro de 2025 até a competência mais
   recente disponível, ao Município de Santa Maria/RS (código IBGE 431690), a título do incentivo
   financeiro adicional de custeio de que trata o art. 172-E da Portaria de Consolidação GM/MS
   nº 6/2017 — indicando o valor por categoria profissional (medicina; enfermagem; odontologia;
   demais categorias) e o total da competência.

2. **Quantitativo de profissionais residentes** considerado no cálculo do incentivo para esse
   Município, por competência e por tipo de equipe (eSF, eSB, eMulti, eSFF da UBSF, eSFR, eCR, eAPP),
   com os respectivos códigos INE, se possível.

3. **Portaria de credenciamento** do Município (art. 172-F): número, data de publicação no DOU e
   eventuais alterações ou cancelamentos, com indicação do quantitativo de vagas credenciadas.

4. **Suspensões ou cancelamentos** da transferência relativos a esse Município (arts. 172-H e 172-I),
   com a motivação e o período, em 2025 e 2026.

5. **Valores de referência** do incentivo antes e depois da Portaria GM/MS nº 10.193/2026
   (R$ 4.500 e R$ 8.000 por residente de medicina, respectivamente), confirmando a data de início
   dos efeitos financeiros do novo valor.

Caso parte da informação esteja disponível em relatório público cujo acesso esteja indisponível por
falha técnica, peço que seja informado o caminho alternativo de consulta ou que os dados sejam
fornecidos por este canal.

---

### Observações para quem for protocolar
- Anexe/descreva a falha do painel: em 13/10/2026 o endpoint
  `https://relatorioaps-prd.saude.gov.br/financiamento/pagamento` responde **HTTP 500** para todos os
  filtros (inclusive Brasil), enquanto `.../cobertura/ab` responde normalmente — evidência de problema
  no serviço, não de uso incorreto.
- Peça o retorno em **planilha** (CSV/XLSX) para facilitar a conferência.
- O mesmo pedido pode ser feito por um grupo de residentes; nesse caso, indique que se trata de
  solicitação de dados públicos de execução orçamentária federal (não envolve dados pessoais).
