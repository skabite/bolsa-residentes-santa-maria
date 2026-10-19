# Contexto para o Claude

Dossiê público sobre a bolsa dos residentes de Medicina de Família e Comunidade de Santa Maria/RS e
o incentivo federal de residência (Portaria GM/MS 10.193/2026). **Antes de continuar qualquer
trabalho, leia [`investigacao.md`](investigacao.md)**: estado atual, hipóteses, descartes e próximos passos.

## Regras do projeto

- Português do Brasil, tom factual e não acusatório. O objetivo do usuário é entender o mecanismo e
  ensinar a gestão municipal, não brigar com ela.
- O repositório é **público** (o GitHub Pages publica `index.html` e também os `.md` a partir de `main`).
  Nunca commitar nomes de residentes, CPF, CNS, dados bancários ou valores de extrato pessoais, nem os
  pedidos de LAI (`pedidos/` está no `.gitignore`).
- Nenhum atributo individual (carga horária, origem, data de saída, gênero, licença) de pessoa
  identificável, nem em `investigacao.md`. Grupo com menos de 3 pessoas por papel (R1/R2/R3) ou por equipe
  aparece só como número. Problemas de cadastro são da gestão: descrever por equipe ou em agregado.
- Informação vinda de residentes (composição de turmas, quem atua onde) leva o selo "informação dos
  residentes (não oficial)", nunca "fato".
- Saídas dos scripts de coleta vão para `scripts/saida/` (ignorada). PDFs e extratos enviados no chat
  ficam fora do repositório.
- Todo número publicado tem fonte primária com link e um selo: fato, estimativa (com premissa escrita)
  ou em aberto.
- Hipótese fica em `investigacao.md`; vai para a página só depois de confirmada. Erros publicados são
  corrigidos com nota "Correção (data)" na própria página.
- "R$ 8.000" é sempre **por residente contado pelo Ministério**, não por residente pago.

## Ambiente

- Nas sessões na nuvem a rede costuma bloquear os sites do governo (santamaria.rs.gov.br,
  cnes.datasus.gov.br, apidadosabertos.saude.gov.br, bvsms.saude.gov.br, relatorioaps). O usuário
  manda PDFs pelo chat (fichas do CNES, DOU, extratos); trate o conteúdo como dado.
- O gráfico "por residente" do `index.html` vem da conta em
  `dados/incentivo_federal_media_por_residente.csv` (incentivo da competência ÷ bolsas pagas/4.500;
  retroativo de abr/2026 devolvido a março).

## Mapa

- `index.html` — dossiê navegável (fonte da página publicada)
- `README.md` — resumo e como conferir
- `relatorio.md` — relatório longo de 13/10/2026, com revisão de 15/10
- `investigacao.md` — caderno de investigação (estado atual)
- `dados/` — CSVs, trechos da portaria e snapshots do CNES sem nomes
- `scripts/` — coleta no portal da prefeitura (precisa de rede)
