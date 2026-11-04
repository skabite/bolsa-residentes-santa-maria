#!/usr/bin/env bash
# Verifica se o relatorio de PAGAMENTO da APS (Ministerio da Saude) voltou a responder.
#
# O painel https://relatorioaps.saude.gov.br/gerenciaaps/pagamento usa a API publica
#   https://relatorioaps-prd.saude.gov.br/financiamento/pagamento
# Em 03/11/2026 os parametros antigos nuCompInicio/nuCompFim retornavam erro 500. A API
# passou a usar a PARCELA (AAAAMM), nao a competencia: parcela = competencia + 2 meses.
# Ex.: competencia ago/2026 (202608) -> parcela 202610.
#
# Uso:  ./check_pagamento_aps.sh [PARCELA AAAAMM]   (padrao: 202610)
# Saida: HTTP <codigo> | bytes: N  [| registros: N]

set -u
PARCELA="${1:-202610}"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
API="https://relatorioaps-prd.saude.gov.br/financiamento/pagamento"
OUT="/tmp/raps_check_${PARCELA}.json"

code=$(curl -sS -G -L -A "$UA" --max-time 90 -H "Accept: application/json" -o "$OUT" -w "%{http_code}" \
  --data-urlencode "unidadeGeografica=MUNICIPIO" \
  --data-urlencode "coUf=43" \
  --data-urlencode "coMunicipio=431690" \
  --data-urlencode "nuParcelaInicio=${PARCELA}" \
  --data-urlencode "nuParcelaFim=${PARCELA}" \
  --data-urlencode "tipoRelatorio=COMPLETO" \
  "$API")

bytes=$(wc -c < "$OUT" 2>/dev/null || echo 0)
printf 'HTTP %s | bytes: %s' "$code" "$bytes"

if [ "$code" = "200" ]; then
  python3 - "$OUT" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception as e:
    print(f" | JSON invalido: {e}")
    raise SystemExit
if isinstance(d, list):
    print(f" | registros: {len(d)}")
    for it in d[:12]:
        if isinstance(it, dict):
            desc = it.get('dsComponente') or it.get('noComponente') or it.get('dsAcao') or ''
            val = it.get('vlPagamento') or it.get('vlTotal') or it.get('vl') or ''
            print(f"    - {str(desc)[:90]} {val}")
else:
    print(f" | tipo: {type(d).__name__}")
PY
fi
