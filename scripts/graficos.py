#!/usr/bin/env python3
"""Gera os graficos SVG do dossie a partir dos CSVs em dados/ e os injeta no index.html.

Uso:  python3 scripts/graficos.py            (atualiza index.html no lugar)
      python3 scripts/graficos.py --mostrar  (so imprime os nomes e tamanhos)

Cada grafico fica entre os marcadores <!--g:nome--> e <!--/g:nome--> no index.html.
Os SVGs usam viewBox de 360 de largura (pensados para o celular) e classes CSS da pagina
(.g-grid, .g-axis, .g-tick, .g-s1, .g-s2, .g-ref, .g-bar, .g-hit, .g-lab), entao as cores
seguem o tema claro/escuro. Sem dependencias alem da biblioteca padrao.
"""
import csv
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(RAIZ, "dados")
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
W = 360


def brl(v, casas=0):
    s = f"{v:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + s


def num(v):
    s = f"{v:.1f}".replace(".", ",")
    return s[:-2] if s.endswith(",0") else s


def ler(nome):
    with open(os.path.join(DADOS, nome), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def escala(v0, v1, p0, p1):
    return lambda v: p0 + (p1 - p0) * (v - v0) / (v1 - v0)


def svg_abre(h, rotulo):
    return (f'<svg viewBox="0 0 {W} {h}" class="g" role="img" aria-label="{rotulo}">')


# ---------------------------------------------------------------- pagos x contados
def pagos_contados():
    linhas = ler("incentivo_federal_media_por_residente.csv")
    n = len(linhas)
    H, X0, X1, Y0, Y1 = 250, 30, 268, 214, 22
    x = lambda i: X0 + (X1 - X0) * i / (n - 1)
    y = escala(0, 25, Y0, Y1)
    p = [svg_abre(H, "Residentes pagos pela prefeitura e residentes contados pelo Ministerio da Saude, "
                     "por competencia, de novembro de 2024 a julho de 2026.")]
    for v in (0, 5, 10, 15, 20, 25):
        p.append(f'<line class="g-grid" x1="{X0}" x2="{X1}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>'
                 f'<text class="g-tick" x="{X0 - 6}" y="{y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    # teto credenciado
    p.append(f'<path class="g-ref" d="M {X0} {y(18):.1f} H {X1}"/>')
    p.append(f'<text class="g-lab" x="{X1 + 6}" y="{y(18) + 4:.1f}">18 vagas</text>')
    # marca da turma nova
    i_mar = [l["competencia"] for l in linhas].index("MAR/2026")
    p.append(f'<path class="g-mark" d="M {x(i_mar):.1f} {Y1} V {Y0}"/>')
    p.append(f'<text class="g-tick" x="{x(i_mar) - 4:.1f}" y="{Y1 + 2}" text-anchor="end">turma nova →</text>')
    pag = [float(l["residentes_pagos_prefeitura"]) for l in linhas]
    con = [int(l["residentes_contados_ms"]) for l in linhas]
    for serie, cls in ((pag, "g-s2"), (con, "g-s1")):
        d = " ".join(f"{'M' if i == 0 else 'L'} {x(i):.1f} {y(v):.1f}" for i, v in enumerate(serie))
        p.append(f'<path class="g-line {cls}" d="{d}"/>')
        p.append(f'<circle class="g-dot {cls}" cx="{x(n - 1):.1f}" cy="{y(serie[-1]):.1f}" r="4"/>')
    p.append(f'<text class="g-lab g-strong" x="{X1 + 6}" y="{y(pag[-1]) + 4:.1f}">{num(pag[-1])} pagos</text>')
    p.append(f'<text class="g-lab g-strong" x="{X1 + 6}" y="{y(con[-1]) + 4:.1f}">{con[-1]} contados</text>')
    for i, lab in ((0, "nov/24"), (n - 1, "jul/26")):
        p.append(f'<text class="g-tick" x="{x(i):.1f}" y="{Y0 + 18}" text-anchor="middle">{lab}</text>')
    i_jan = [l["competencia"] for l in linhas].index("JAN/2026")
    p.append(f'<text class="g-tick" x="{x(i_jan):.1f}" y="{Y0 + 18}" text-anchor="middle">jan/26</text>')
    passo = (X1 - X0) / (n - 1)
    for i, l in enumerate(linhas):
        comp = l["competencia"].lower()
        tip = f"{comp} · prefeitura pagou {num(pag[i])} · Ministério contou {con[i]}"
        p.append(f'<rect class="g-hit" data-tip="{tip}" x="{x(i) - passo / 2:.1f}" y="{Y1}" '
                 f'width="{passo:.1f}" height="{Y0 - Y1}"><title>{tip}</title></rect>')
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- media por residente
def media_residente():
    linhas = ler("incentivo_federal_media_por_residente.csv")
    n = len(linhas)
    H, X0, X1, Y0, Y1 = 250, 34, 352, 214, 26
    y = escala(0, 9000, Y0, Y1)
    passo = (X1 - X0) / n
    bw = max(6.0, passo * 0.62)
    p = [svg_abre(H, "Media do incentivo federal por residente pago pela prefeitura, por competencia, "
                     "comparada com a bolsa de 4.500 reais e com o valor de 8.000 reais por residente contado.")]
    for v in (0, 2000, 4000, 6000, 8000):
        p.append(f'<line class="g-grid" x1="{X0}" x2="{X1}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>'
                 f'<text class="g-tick" x="{X0 - 6}" y="{y(v) + 4:.1f}" text-anchor="end">{v // 1000 if v else 0}{"k" if v else ""}</text>')
    for i, l in enumerate(linhas):
        m = float(l["media_federal_por_residente_pago"])
        cx = X0 + passo * (i + 0.5)
        if m > 0:
            top = y(m)
            r = min(3, (Y0 - top) / 2)
            p.append(f'<path class="g-bar" d="M {cx - bw / 2:.1f} {Y0} V {top + r:.1f} '
                     f'Q {cx - bw / 2:.1f} {top:.1f} {cx - bw / 2 + r:.1f} {top:.1f} H {cx + bw / 2 - r:.1f} '
                     f'Q {cx + bw / 2:.1f} {top:.1f} {cx + bw / 2:.1f} {top + r:.1f} V {Y0} Z"/>')
    p.append(f'<line class="g-axis" x1="{X0}" x2="{X1}" y1="{Y0}" y2="{Y0}"/>')
    p.append(f'<path class="g-line g-s2" d="M {X0} {y(4500):.1f} H {X1}"/>')
    p.append(f'<text class="g-lab" x="{X0 + 4}" y="{y(4500) - 7:.1f}">bolsa: R$ 4.500</text>')
    i_fev = [l["competencia"] for l in linhas].index("FEV/2026")
    p.append(f'<path class="g-ref" d="M {X0 + passo * i_fev:.1f} {y(8000):.1f} H {X1}"/>')
    p.append(f'<text class="g-lab" x="{X1}" y="{y(8000) - 7:.1f}" text-anchor="end">R$ 8.000 por residente contado</text>')
    fev = float(linhas[i_fev]["media_federal_por_residente_pago"])
    p.append(f'<text class="g-lab g-strong" x="{X0 + passo * (i_fev + 0.5):.1f}" y="{y(fev) - 6:.1f}" '
             f'text-anchor="middle">{brl(fev)[3:]}</text>')
    p.append(f'<text class="g-lab g-strong" x="{X0 + passo * (n - 0.5):.1f}" y="{Y0 - 6}" '
             f'text-anchor="middle">0</text>')
    for comp, lab in (("NOV/2024", "nov/24"), ("JAN/2026", "jan/26"), ("JUL/2026", "jul/26")):
        i = [l["competencia"] for l in linhas].index(comp)
        p.append(f'<text class="g-tick" x="{X0 + passo * (i + 0.5):.1f}" y="{Y0 + 18}" text-anchor="middle">{lab}</text>')
    for i, l in enumerate(linhas):
        tip = (f'{l["competencia"].lower()} · {brl(float(l["incentivo_federal"]))} do Ministério ÷ '
               f'{num(float(l["residentes_pagos_prefeitura"]))} residentes pagos = '
               f'{brl(float(l["media_federal_por_residente_pago"]))} por residente')
        p.append(f'<rect class="g-hit" data-tip="{tip}" x="{X0 + passo * i:.1f}" y="{Y1}" '
                 f'width="{passo:.1f}" height="{Y0 - Y1}"><title>{tip}</title></rect>')
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- bolsa por mes
def bolsa_mes():
    linhas = ler("bolsa_residentes_por_mes.csv")
    por = {(int(l["ano"]), int(l["mes"])): l for l in linhas}
    meses = []
    a, m = 2021, 4
    while (a, m) <= (int(linhas[-1]["ano"]), int(linhas[-1]["mes"])):
        meses.append((a, m))
        a, m = (a + 1, 1) if m == 12 else (a, m + 1)
    n = len(meses)
    H, X0, X1, Y0, Y1 = 230, 38, 352, 196, 16
    y = escala(0, 180000, Y0, Y1)
    passo = (X1 - X0) / n
    bw = max(2.6, passo * 0.68)
    p = [svg_abre(H, "Valor mensal empenhado em bolsas de residencia, de abril de 2021 a agosto de 2026. "
                     "Toque numa barra para ver os empenhos do mes.")]
    for v in (0, 60000, 120000, 180000):
        p.append(f'<line class="g-grid" x1="{X0}" x2="{X1}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>'
                 f'<text class="g-tick" x="{X0 - 6}" y="{y(v) + 4:.1f}" text-anchor="end">{v // 1000}{"k" if v else ""}</text>')
    for i, (a, m) in enumerate(meses):
        l = por.get((a, m))
        v = float(l["valor_bolsas"]) if l else 0.0
        if v <= 0:
            continue
        cx = X0 + passo * (i + 0.5)
        p.append(f'<rect class="g-bar" x="{cx - bw / 2:.1f}" y="{y(v):.1f}" width="{bw:.1f}" '
                 f'height="{Y0 - y(v):.1f}" rx="1.2"/>')
    p.append(f'<line class="g-axis" x1="{X0}" x2="{X1}" y1="{Y0}" y2="{Y0}"/>')
    for ano in range(2021, meses[-1][0] + 1):
        idx = [i for i, (a, _) in enumerate(meses) if a == ano]
        cx = X0 + passo * (idx[0] + idx[-1] + 1) / 2
        p.append(f'<text class="g-tick" x="{cx:.1f}" y="{Y0 + 18}" text-anchor="middle">{ano}</text>')
    for i, (a, m) in enumerate(meses):
        l = por.get((a, m))
        v = float(l["valor_bolsas"]) if l else 0.0
        eq = v / 4500
        tip = f"{MESES[m - 1]}/{a} · {brl(v, 2)}" + (f" · ≈{num(eq)} bolsas" if v else " · sem empenho no mês")
        p.append(f'<rect class="g-hit g-mes" tabindex="0" role="button" data-ano="{a}" data-mes="{m}" '
                 f'data-tip="{tip}" x="{X0 + passo * i:.1f}" y="{Y1}" width="{passo:.1f}" '
                 f'height="{Y0 - Y1}"><title>{tip}</title></rect>')
    p.append("</svg>")
    return "".join(p)


GRAFICOS = {"pagos-contados": pagos_contados, "media-residente": media_residente, "bolsa-mes": bolsa_mes}


def main():
    if "--mostrar" in sys.argv:
        for nome, f in GRAFICOS.items():
            print(nome, len(f()))
        return
    caminho = os.path.join(RAIZ, "index.html")
    html = open(caminho, encoding="utf-8").read()
    for nome, f in GRAFICOS.items():
        padrao = re.compile(r"(<!--g:%s-->).*?(<!--/g:%s-->)" % (nome, nome), re.S)
        if not padrao.search(html):
            print(f"aviso: marcador <!--g:{nome}--> nao encontrado")
            continue
        html = padrao.sub(lambda mo: mo.group(1) + f() + mo.group(2), html)
    open(caminho, "w", encoding="utf-8").write(html)
    print("graficos atualizados em index.html")


if __name__ == "__main__":
    main()
