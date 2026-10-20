#!/usr/bin/env python3
"""Extrator de empenhos do Portal da Transparencia de Santa Maria/RS.

A tela /transparencia/despesa/empenho e um componente Livewire
(transparencia.lista-empenho). A pagina tambem expoe a API publica
DadosAbertos (parcialmente quebrada no lado do servidor).
"""
import base64
import html
import json
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

BASE = "https://www.santamaria.rs.gov.br"
URL = f"{BASE}/transparencia/despesa/empenho"
UPDATE_URI = "/livewire/update"


class EmpenhoClient:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({
            # identifica o projeto, em vez de se passar por navegador
            "User-Agent": "Mozilla/5.0 (compatible; bolsa-residentes-sm/1.0; +https://github.com/skabite/bolsa-residentes-santa-maria)",
            "Accept-Language": "pt-BR,pt;q=0.9",
        })
        self.snapshot = None
        self.csrf = None

    def load(self):
        r = self.s.get(URL, timeout=60)
        r.raise_for_status()
        raw = r.text
        m = re.search(r'data-csrf="([^"]+)"', raw)
        if not m:
            raise RuntimeError("csrf nao encontrado na pagina")
        self.csrf = m.group(1)
        snaps = re.findall(r'wire:snapshot="([^"]+)"', raw)
        for s in snaps:
            j = json.loads(html.unescape(s))
            if j.get("memo", {}).get("name") == "transparencia.lista-empenho":
                self.snapshot = j
                return
        raise RuntimeError("componente lista-empenho nao encontrado")

    def call(self, updates=None, method=None, params=None):
        comp = {
            "snapshot": json.dumps(self.snapshot, ensure_ascii=False, separators=(",", ":")),
            "updates": updates or {},
            "calls": ([{"path": "", "method": method, "params": params or []}]
                      if method else []),
        }
        payload = {"_token": self.csrf, "components": [comp]}
        headers = {
            "Content-Type": "application/json",
            "X-Livewire": "",
            "X-CSRF-TOKEN": self.csrf,
            "Accept": "application/json, text/plain, */*",
            "Origin": BASE,
            "Referer": URL,
        }
        r = self.s.post(BASE + UPDATE_URI, json=payload, headers=headers, timeout=90)
        r.raise_for_status()
        data = r.json()
        out = data["components"][0]
        # atualiza o snapshot local (o servidor devolve o novo)
        if "snapshot" in out:
            try:
                self.snapshot = json.loads(out["snapshot"])
            except (TypeError, json.JSONDecodeError):
                pass
        return out.get("effects", {}).get("html", "")

    def rows_from(self, html_chunk):
        soup = BeautifulSoup(html_chunk, "html.parser")
        rows = []
        for tr in soup.select("table tbody tr"):
            tds = [td.get_text(" ", strip=True) for td in tr.find_all("td")]
            if tds:
                rows.append(tds)
        return rows


def main():
    year = sys.argv[1] if len(sys.argv) > 1 else "2026"
    pages = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    c = EmpenhoClient()
    c.load()
    print(f"snapshot carregado; ano atual = {c.snapshot['data'].get('ano')}")
    print("CSRF:", c.csrf[:12], "...")
    h = c.call(updates={"ano": year}, method="filtrar")
    print("html devolvido:", len(h), "bytes")
    rows = c.rows_from(h)
    print("linhas na pagina 1:", len(rows))
    for r in rows[:5]:
        print("   ", r)
    # tenta paginar
    for p in range(2, pages + 1):
        time.sleep(1)
        h = c.call(method="gotoPage", params=[p])
        rows = c.rows_from(h)
        print(f"pagina {p}: {len(rows)} linhas")
        for r in rows[:2]:
            print("   ", r)


if __name__ == "__main__":
    main()
