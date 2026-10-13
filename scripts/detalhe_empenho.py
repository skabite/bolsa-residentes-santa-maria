#!/usr/bin/env python3
"""Busca o detalhe de empenhos no Portal da Transparencia de Santa Maria/RS."""
import html
import json
import re
import sys

import requests

BASE = "https://www.santamaria.rs.gov.br"
URL = BASE + "/transparencia/despesa/empenho/{}/{}"


def detalhe(s, nr, ano):
    r = s.get(URL.format(nr, ano), timeout=90)
    raw = r.text
    for x in re.findall(r'wire:snapshot="([^"]+)"', raw):
        j = json.loads(html.unescape(x))
        if j.get("memo", {}).get("name") == "transparencia.ver-empenho":
            d = j["data"]
            dados = d.get("dadosEmpenho") or {}
            if isinstance(dados, list):
                dados = dados[0] if dados else {}
            itens = []
            raw_itens = d.get("itens") or []
            try:
                for it in raw_itens[0]:
                    itens.append(it[0])
            except (IndexError, KeyError, TypeError):
                pass
            return dados, itens
    return None, None


def main():
    pares = []
    for a in sys.argv[1:]:
        nr, ano = a.split("/")
        pares.append((nr, ano))
    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/126 Safari/537.36"})
    out = []
    for nr, ano in pares:
        dados, itens = detalhe(s, nr, ano)
        if not dados:
            print(f"{nr}/{ano}: NAO ENCONTRADO")
            continue
        print(f"===== Empenho {nr}/{ano} =====")
        for k in ("nmFornecedor", "dtemissaoempenhoc", "nmSecretaria", "nmUnidadeOrcamentaria",
                  "nmProjetoAtividade", "nmNaturezaDespesa", "dsSubElemento", "nmFonteRecurso",
                  "vlEmpenhado", "vlLiquidado", "vlPago", "dsTipoLicitacao"):
            if k in dados:
                print(f"   {k}: {dados[k]}")
        print("   chaves disponiveis:", ", ".join(dados.keys()))
        for it in itens[:3]:
            print("   ITEM:", {k: it[k] for k in list(it)[:12]})
        out.append({"nr": nr, "ano": ano, "dados": dados, "itens": itens})
    json.dump(out, open("/tmp/bolsa-work/detalhes.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
