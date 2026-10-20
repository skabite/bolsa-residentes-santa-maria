#!/usr/bin/env python3
"""Checa se o Portal da Transparencia de Santa Maria publicou novos empenhos de
bolsa dos medicos residentes (Secretaria de Municipio da Saude).

Como funciona: a tela /transparencia/despesa/empenho e um componente Livewire.
O script faz o handshake (pega o data-csrf e o wire:snapshot) e envia os filtros
por POST em /livewire/update. Usa a tela publica de listagem; nao usa a exportacao
nem resolve captcha (acesso automatizado previsto na Lei 12.527/2011, art. 8o, par. 3o, III).

Uso:  python3 check_empenho_residentes.py [ano]
Saida (uma linha por achado):
  ULTIMO_EMPENHO <data>            - empenho mais recente da Saude no portal
  BOLSA <data> <nr> <valor> <desc> - empenho de bolsa de residente encontrado
  NOVO <data>                      - bolsa com data posterior a ULTIMA_CONHECIDA
  ERRO <mensagem>                  - falha de acesso
Exit code 0 sempre (o cron decide pelo texto).
"""
import json
import re
import sys
from html import unescape

import requests

BASE = "https://www.santamaria.rs.gov.br"
URL = f"{BASE}/transparencia/despesa/empenho"
UNIDADE = "Secretaria de Município da Saúde"
# ultima competencia de bolsa ja conhecida (26/08/2026, empenhos 18085/18088)
ULTIMA_CONHECIDA = "26/08/2026"
RUIDO = re.compile(r"(?i)(rm-?40|hospital|assistencial|moradia|mais m[ée]dicos|residencial)")


def main():
    ano = sys.argv[1] if len(sys.argv) > 1 else "2026"
    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0 (compatible; bolsa-residentes-sm/1.0; +https://github.com/skabite/bolsa-residentes-santa-maria)"})
    try:
        raw = s.get(URL, timeout=90).text
    except Exception as e:
        print(f"ERRO nao consegui abrir o portal: {e}")
        return
    m = re.search(r'data-csrf="([^"]+)"', raw)
    snap = None
    for x in re.findall(r'wire:snapshot="([^"]+)"', raw):
        j = json.loads(unescape(x))
        if j.get("memo", {}).get("name") == "transparencia.lista-empenho":
            snap = j
            break
    if not m or not snap:
        print("ERRO pagina do portal mudou (sem csrf/snapshot) - avisar o Claude")
        return
    payload = {"_token": m.group(1), "components": [{
        "snapshot": json.dumps(snap, ensure_ascii=False, separators=(",", ":")),
        "updates": {"ano": ano, "nomeUnidade": UNIDADE, "quantidadePorPagina": 100},
        "calls": [{"path": "", "method": "filtrar", "params": []}]}]}
    try:
        r = s.post(BASE + "/livewire/update", json=payload, timeout=120, headers={
            "Content-Type": "application/json", "X-Livewire": "", "X-CSRF-TOKEN": m.group(1),
            "Accept": "application/json", "Referer": URL, "Origin": BASE})
        html = r.json()["components"][0]["effects"]["html"]
    except Exception as e:
        print(f"ERRO na consulta ao portal: {e}")
        return

    linhas = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S)
    achados, ultimo = [], None
    for tr in linhas:
        tds = [re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if len(tds) < 5:
            continue
        nr, forn, valor, data = tds[1], tds[2], tds[3], tds[4]
        if re.match(r"\d{2}/\d{2}/\d{4}", data):
            if ultimo is None or (data[6:], data[3:5], data[:2]) > (ultimo[6:], ultimo[3:5], ultimo[:2]):
                ultimo = data
        if re.search(r"(?i)folha\s*pgto\s*coletiva|m[ée]dicos\s*residentes", forn) and not RUIDO.search(forn):
            achados.append((data, nr, valor, forn))
    if ultimo:
        print(f"ULTIMO_EMPENHO {ultimo}")
    for data, nr, valor, forn in sorted(achados, reverse=True)[:6]:
        d, mo, a = data[:2], data[3:5], data[6:]
        marca = "NOVO " if (a, mo, d) > (ULTIMA_CONHECIDA[6:], ULTIMA_CONHECIDA[3:5], ULTIMA_CONHECIDA[:2]) else ""
        print(f"{marca}BOLSA {data} emp {nr} R$ {valor} :: {forn[:60]}")
    if not achados:
        print("(nenhum empenho de bolsa de residente na primeira pagina)")


if __name__ == "__main__":
    main()
