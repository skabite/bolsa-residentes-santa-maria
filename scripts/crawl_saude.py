#!/usr/bin/env python3
"""Baixa todos os empenhos da Secretaria de Municipio da Saude de Santa Maria/RS.

Uso: python3 crawl_saude.py 2021 2022 2023 ...
Gera /tmp/bolsa-work/empenhos_saude_<ano>.csv
"""
import csv
import os
import re
import sys
import time

sys.path.insert(0, "/tmp/bolsa-work")
from empenho import EmpenhoClient

UNIDADE = "Secretaria de Município da Saúde"
POR_PAGINA = 100


def maxpage(h):
    pgs = [int(x) for x in re.findall(r"gotoPage\((\d+)\)", h)]
    return max(pgs) if pgs else 1


def crawl(ano):
    c = EmpenhoClient()
    c.load()
    h = c.call(updates={"ano": str(ano), "nomeUnidade": UNIDADE,
                        "quantidadePorPagina": POR_PAGINA}, method="filtrar")
    total = maxpage(h)
    rows = c.rows_from(h)
    print(f"[{ano}] total paginas: {total} | pagina 1: {len(rows)} linhas", flush=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"empenhos_saude_{ano}.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["nrEmpenho", "fornecedor", "valor", "data", "link"])
        for r in rows:
            if len(r) >= 5:
                w.writerow([r[1], r[2], r[3], r[4], ""])
    for p in range(2, total + 1):
        for tent in range(3):
            try:
                h = c.call(method="gotoPage", params=[p])
                rows = c.rows_from(h)
                break
            except Exception as e:
                print(f"[{ano}] pag {p} erro {e}; retry {tent+1}", flush=True)
                time.sleep(3)
                c = EmpenhoClient()
                c.load()
                c.call(updates={"ano": str(ano), "nomeUnidade": UNIDADE,
                                "quantidadePorPagina": POR_PAGINA}, method="filtrar")
                for q in range(2, p):
                    c.call(method="gotoPage", params=[q])
        else:
            rows = []
        with open(out, "a", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            for r in rows:
                if len(r) >= 5:
                    w.writerow([r[1], r[2], r[3], r[4], ""])
        if p % 10 == 0:
            print(f"[{ano}] pagina {p}/{total}", flush=True)
        time.sleep(0.35)
    print(f"[{ano}] concluido -> {out}", flush=True)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        crawl(int(a))
