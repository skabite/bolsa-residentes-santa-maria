#!/usr/bin/env python3
"""Monta as páginas do dossiê: partes comuns, gráficos, tabelas e listas tirados de dados/.

Uso:  python3 scripts/montar_site.py              atualiza as páginas no lugar
      python3 scripts/montar_site.py --verificar  só confere, sem gravar (erro se algo faltar ou estiver velho)

As páginas .html da raiz são escritas à mão. O script só reescreve o que fica entre os marcadores
<!--tipo:nome--> e <!--/tipo:nome--> e gera assets/fontes.js (fontes e termos para os balões):

  b:cabeca b:topo b:rodape b:pager b:toc b:data b:cartoes   partes comuns às páginas
  g:pagos-contados g:media-residente g:bolsa-mes             gráficos (scripts/graficos.py)
  t:federal t:cnes t:situacao b:situacao-curta               tabelas tiradas dos CSVs
  d:dados                                                    dados da tabela de empenhos
  b:lista-fontes b:lista-termos                              dados/fontes.json e dados/glossario.json

Antes de gravar, confere que cada data-ref existe em dados/fontes.json e cada data-termo em
dados/glossario.json, que o link de cada trecho com fonte aponta para a primeira fonte citada, e que
cada link interno (pagina.html#id, #id, dados/...) leva a algo que existe.
Só usa a biblioteca padrão.
"""
import html
import json
import os
import re
import sys
import unicodedata
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graficos  # noqa: E402

RAIZ, DADOS = graficos.RAIZ, graficos.DADOS
ATUALIZADO = "29/10/2026"
REPO = "https://github.com/skabite/bolsa-residentes-santa-maria"
ESTADO = {"primaria": "Conferida na fonte primária", "parcial": "Conferida em parte", "conferir": "A conferir"}
esc = html.escape

# arquivo, nome curto (barra e mapa), título (menu e cartões), descrição, aparece na barra do computador
PAGINAS = [
    ("index.html", "Início", "Início", "A situação em 2 minutos, com os quatro pontos principais.", True),
    ("reajuste.html", "Reajuste", "Dá para pedir reajuste?", "O pedido, quanto seria e como outras cidades fazem.", True),
    ("contagem.html", "Contagem", "Onde trava a contagem", "Os requisitos do Ministério, um a um, e o estágio externo.", True),
    ("numeros.html", "Números", "Os números", "Gráficos, tabelas, cada empenho e até quando vão os dados.", True),
    ("fazer.html", "O que fazer", "O que fazer", "Para residentes, gestão municipal e COREMEs, com os canais.", True),
    ("linha-do-tempo.html", "Linha do tempo", "Linha do tempo", "Do incentivo de 2019 ao zero de julho de 2026.", False),
    ("fontes.html", "Fontes", "Fontes", "As referências, com o que cada uma prova e onde é citada.", True),
    ("glossario.html", "Glossário", "Glossário", "CNES, CNRM, competência, empenho e outros termos.", False),
    ("sobre.html", "Sobre", "Sobre o dossiê", "Método, correções, privacidade e como reutilizar.", False),
]
NOME = {p[0]: p[1] for p in PAGINAS}

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
           "<rect width='32' height='32' rx='8' fill='%231d5fae'/><path d='M8 23V9h4l4 7 4-7h4v14' fill='none' "
           "stroke='white' stroke-width='3' stroke-linejoin='round'/></svg>")


# ---------------------------------------------------------------- registros
def carrega_fontes():
    with open(os.path.join(DADOS, "fontes.json"), encoding="utf-8") as fh:
        return json.load(fh)


def carrega_termos():
    with open(os.path.join(DADOS, "glossario.json"), encoding="utf-8") as fh:
        return json.load(fh)["termos"]


def confere_registros(reg, termos):
    erros, grupos, vistos = [], {g["id"] for g in reg["grupos"]}, set()
    for f in reg["fontes"]:
        quem = f"dados/fontes.json: fonte {f.get('n')}"
        if f.get("n") in vistos:
            erros.append(f"{quem}: número repetido")
        vistos.add(f.get("n"))
        if f.get("grupo") not in grupos:
            erros.append(f"{quem}: grupo desconhecido {f.get('grupo')!r}")
        if f.get("estado") and f["estado"] not in ESTADO:
            erros.append(f"{quem}: estado desconhecido {f['estado']!r}")
        for campo in ("titulo", "prova"):
            if not f.get(campo):
                erros.append(f"{quem}: falta {campo}")
        if not f.get("links") or any(not l.get("rotulo") or not l.get("url", "").startswith("https://") for l in f["links"]):
            erros.append(f"{quem}: cada link precisa de rotulo e de url https://")
    ids = [t["id"] for t in termos]
    for i in sorted({i for i in ids if ids.count(i) > 1}):
        erros.append(f"dados/glossario.json: id repetido {i}")
    for i in ids:
        if not re.fullmatch(r"[a-z0-9-]+", i):
            erros.append(f"dados/glossario.json: id inválido {i!r} (só minúsculas, números e hífen)")
    return erros


# ---------------------------------------------------------------- leitura das páginas
class Leitor(HTMLParser):
    """Guarda ids, links, seções de <main> (para o "Nesta página") e os trechos com fonte ou termo."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.gatilhos, self.secoes = [], [], [], []
        self._secao, self._h2, self._main = None, None, 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        linha = self.getpos()[0]
        if a.get("id"):
            self.ids.append((a["id"], linha))
        if tag == "main":
            self._main += 1
        if tag == "section" and self._main and a.get("id"):
            self._secao = [a["id"], a.get("data-toc") or None]
            self.secoes.append(self._secao)
        elif tag == "h2" and self._secao is not None and self._secao[1] is None:
            self._h2 = []
        if tag == "a" and "href" in a:
            self.links.append((a["href"], linha))
        if "data-ref" in a or "data-termo" in a:
            self.gatilhos.append({"tag": tag, "classes": a.get("class", "").split(), "href": a.get("href", ""),
                                  "ref": a.get("data-ref", ""), "termo": a.get("data-termo", ""),
                                  "linha": linha, "secao": self._secao})

    def handle_endtag(self, tag):
        if tag == "h2" and self._h2 is not None:
            self._secao[1] = " ".join("".join(self._h2).split())
            self._h2 = None
        elif tag == "section":
            self._secao = None
        elif tag == "main":
            self._main -= 1

    def handle_data(self, data):
        if self._h2 is not None:
            self._h2.append(data)


def le(texto):
    leitor = Leitor()
    leitor.feed(texto)
    leitor.close()
    return leitor


# ---------------------------------------------------------------- partes comuns
def href_fonte(n, pag):
    return f"#ref-{n}" if pag == "fontes.html" else f"fontes.html#ref-{n}"


def chip(n, pag):
    return f'<a class="ref" href="{href_fonte(n, pag)}" data-ref="{n}">{n}</a>'


def atual(arq, pag):
    return ' aria-current="page"' if arq == pag else ""


def cabeca(pag, info):
    return ('\n<meta name="color-scheme" content="light dark">\n'
            f'<link rel="icon" href="{FAVICON}">\n'
            '<link rel="stylesheet" href="assets/dossie.css">\n'
            '<script>(function (d) { d.classList.add("js"); try { var t = localStorage.getItem("dossie-tema"); '
            'if (t === "light" || t === "dark") d.setAttribute("data-theme", t); } catch (e) {} })(document.documentElement);</script>\n')


def topo(pag, info):
    nav = "".join(f'<a href="{a}"{atual(a, pag)}>{esc(n)}</a>' for a, n, _, _, barra in PAGINAS if barra)
    return ('\n<a class="skip" href="#conteudo">Pular para o conteúdo</a>\n'
            '<header class="bar">\n'
            '  <a class="marca" href="index.html">Bolsa MFC <span>· Santa Maria</span></a>\n'
            f'  <nav class="nav-topo" aria-label="Páginas principais">{nav}</nav>\n'
            '  <div class="bar-acoes">\n'
            f'    <a class="bar-btn so-celular" href="fontes.html"{atual("fontes.html", pag)}>Fontes</a>\n'
            '    <a class="bar-btn primario" href="#mapa" id="abre-menu" aria-haspopup="dialog">Menu</a>\n'
            '  </div>\n'
            '</header>\n')


def rodape(pag, info):
    mapa = "".join(f'<li><a href="{a}"{atual(a, pag)}>{esc(n)}</a></li>' for a, n, _, _, _ in PAGINAS)
    menu = "\n".join(f'      <li><a href="{a}"{atual(a, pag)}><span><b>{esc(t)}</b><small>{esc(d)}</small></span></a></li>'
                     for a, _, t, d, _ in PAGINAS)
    return f'''
<footer>
  <nav id="mapa" aria-label="Todas as páginas"><ul>{mapa}</ul></nav>
  <p><strong>Iniciativa pessoal e independente.</strong> Não representa nem tem endosso da UFSM, da UFN ou da Prefeitura de
  Santa Maria; os nomes das instituições aparecem só para identificar as fontes.</p>
  <p><strong>Privacidade.</strong> Sem nomes, CPF, cartão SUS ou dados bancários. Residentes aparecem só em números
  agregados. Os dados vêm de fontes públicas oficiais, exceto a composição das turmas, informada por residentes (não
  oficial) e marcada como tal.</p>
  <p><strong>Correções e resposta.</strong> Pedidos de correção ou de retirada podem ser feitos por uma
  <a href="{REPO}/issues" target="_blank" rel="noopener">issue no GitHub</a>. Uma resposta da Secretaria de Saúde ou das
  COREMEs será publicada aqui com o mesmo destaque.</p>
  <p>Atualizado em {ATUALIZADO}. O site não usa rastreadores nem envia dados a nenhum servidor. Textos sob
  <a href="https://creativecommons.org/licenses/by/4.0/deed.pt-br" target="_blank" rel="noopener">CC BY 4.0</a>; código sob
  licença MIT. <a href="sobre.html">Sobre o dossiê</a>.</p>
</footer>

<dialog id="menu" class="folha" aria-labelledby="menu-tit">
  <div class="folha-topo"><h2 id="menu-tit">Páginas</h2><button class="fechar" type="button" data-fechar>Fechar</button></div>
  <div class="folha-corpo">
    <ul class="menu-lista">
{menu}
    </ul>
    <div class="tema" role="group" aria-label="Tema">
      <button type="button" data-tema="auto">Automático</button>
      <button type="button" data-tema="light">Claro</button>
      <button type="button" data-tema="dark">Escuro</button>
    </div>
  </div>
</dialog>
<div class="balao" id="balao" hidden></div>
<div class="tip" id="tip" aria-hidden="true"></div>
<script src="assets/fontes.js"></script>
<script src="assets/dossie.js"></script>
'''


def pager(pag, info):
    arqs = [p[0] for p in PAGINAS]
    i, partes = arqs.index(pag), []
    if i > 0:
        a, n = PAGINAS[i - 1][:2]
        partes.append(f'<li class="ant"><a href="{a}" rel="prev"><span>‹ Anterior</span><b>{esc(n)}</b></a></li>')
    if i < len(PAGINAS) - 1:
        a, n = PAGINAS[i + 1][:2]
        partes.append(f'<li class="prox"><a href="{a}" rel="next"><span>Próxima ›</span><b>{esc(n)}</b></a></li>')
    return f'<nav aria-label="Página anterior e próxima"><ul class="pager">{"".join(partes)}</ul></nav>'


def toc(pag, info):
    itens = "".join(f'<li><a href="#{sid}">{esc(rot)}</a></li>' for sid, rot in info.secoes if rot)
    if not itens:
        sys.exit(f"erro: {pag} tem <!--b:toc--> mas nenhuma <section id> com <h2> ou data-toc")
    return f'<nav class="toc" aria-label="Nesta página"><p>Nesta página</p><ol>{itens}</ol></nav>'


def data(pag, info):
    return ATUALIZADO


def cartoes(pag, info):
    lis = "".join(f'<li><a href="{a}"><b>{esc(t)}</b><span>{esc(d)}</span></a></li>'
                  for a, _, t, d, _ in PAGINAS if a != pag)
    return f'<ul class="cartoes">{lis}</ul>'


# ---------------------------------------------------------------- tabelas tiradas dos CSVs
def situacao(pag, info):
    corpo = "".join(
        f'<tr><td><b>{esc(l["base"])}</b><br><span class="mini">{esc(l["mostra"])}</span> {chip(l["fonte"], pag)}</td>'
        f'<td>{esc(l["periodo"])}</td><td>{esc(l["coletado_em"])}</td><td>{esc(l["falta"])}</td></tr>'
        for l in graficos.ler("situacao_dos_dados.csv"))
    return ('<div class="tabela"><table><thead><tr><th>Base</th><th>Cobre</th><th>Coletado em</th><th>Falta incluir</th>'
            f'</tr></thead><tbody>{corpo}</tbody></table></div>')


def situacao_curta(pag, info):
    partes = [esc(l["resumo"]) for l in graficos.ler("situacao_dos_dados.csv") if l["resumo"].strip()]
    return (f'<p class="dados-ate"><span>Dados até</span> {" · ".join(partes)}. '
            '<a href="numeros.html#situacao">O que falta incluir</a></p>')


def federal(pag, info):
    vagas = {l["competencia"]: int(l["medicos_credenciados"]) for l in graficos.ler("incentivo_federal_residencia.csv")}
    linhas = sorted(graficos.ler("incentivo_federal_media_por_residente.csv"), key=graficos.ordem)
    corpo, tot_inc, tot_pag = [], 0.0, 0.0
    for l in linhas:
        comp, contados = l["competencia"], int(l["residentes_contados_ms"])
        inc, pagos = float(l["incentivo_federal"]), float(l["residentes_pagos_prefeitura"])
        tot_inc, tot_pag = tot_inc + inc, tot_pag + pagos
        classe = ' class="destaque"' if contados == 0 else ""
        corpo.append(f'<tr{classe}><td>{comp.lower()}</td><td class="n">{vagas[comp]}</td><td class="n">{contados}</td>'
                     f'<td class="n">{graficos.num(pagos)}</td><td class="n">{graficos.brl(inc)}</td>'
                     f'<td class="n">{graficos.brl(float(l["media_federal_por_residente_pago"]))}</td></tr>')
    return ('<div class="tabela"><table><thead><tr><th>Mês</th><th class="n">Vagas</th><th class="n">Contados</th>'
            '<th class="n">Pagos</th><th class="n">Entrou</th><th class="n">Por pago</th></tr></thead>'
            f'<tbody>{"".join(corpo)}</tbody><tfoot><tr><td>Total</td><td></td><td></td><td></td>'
            f'<td class="n">{graficos.brl(tot_inc)}</td><td class="n">{graficos.brl(tot_inc / tot_pag)}</td></tr></tfoot>'
            '</table></div>')


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def cnes(pag, info):
    linhas = graficos.ler("cnes_medicos_residentes_por_unidade.csv")
    homolog = {l["ine"]: l for l in graficos.ler("ines_homologacao_equipes_com_residentes.csv")}
    col = [c for c in linhas[0] if re.fullmatch(r"medicos_residentes_[a-z]{3}_\d{4}", c)][-1]
    mes = "/".join(col.split("_")[2:])
    itens = []
    for l in linhas:
        ines = [i.strip() for i in l["ines"].split(",") if i.strip()]
        tipos = sorted({homolog[i]["tipo_de_equipe"] for i in ines})
        equipe = " e ".join(tipos) + (f" ({len(ines)} equipes)" if len(ines) > 1 else "")
        if tipos == ["eAP"]:
            equipe += " (não conta)"
        itens.append((int(l[col]), homolog[ines[0]]["unidade"], equipe, tipos))
    itens.sort(key=lambda t: (-t[0], "eAP" in t[3], sem_acento(t[1])))
    corpo = "".join(f'<tr><td>{esc(nome)}</td><td class="n">{n}</td><td>{esc(eq)}</td></tr>' for n, nome, eq, _ in itens)
    total, esf = sum(t[0] for t in itens), sum(t[0] for t in itens if t[3] == ["eSF"])
    return (f'<div class="tabela"><table><thead><tr><th>Unidade</th><th class="n">Residentes ({mes})</th><th>Equipe</th>'
            f'</tr></thead><tbody>{corpo}</tbody><tfoot><tr><td>Total</td><td class="n">{total}</td><td>{esf} em eSF</td>'
            '</tr></tfoot></table></div>')


# ---------------------------------------------------------------- listas
def citada_em(n, usos):
    """Onde a fonte n é citada, agrupado por página: Reajuste (Os argumentos, Dúvidas) · ..."""
    por_pagina = {}
    for pag, sec, rot in usos.get(str(n), []):
        lugares = por_pagina.setdefault(pag, [])
        if (sec, rot) not in lugares:
            lugares.append((sec, rot))
    partes = []
    for pag, lugares in por_pagina.items():
        if len(lugares) == 1 and not lugares[0][1]:  # página sem seções (ou só a abertura): o nome basta
            partes.append(f'<a href="{pag}">{esc(NOME[pag])}</a>')
            continue
        links = [f'<a href="{pag}#{sec}">{esc(rot)}</a>' if sec and rot else f'<a href="{pag}">abertura</a>'
                 for sec, rot in lugares]
        partes.append(f'{esc(NOME[pag])} ({", ".join(links)})')
    return f'<p class="f-citada">Citada em: {" · ".join(partes)}</p>' if partes else ""


def lista_fontes(usos):
    reg, partes = carrega_fontes(), []
    for g in reg["grupos"]:
        fs = sorted((f for f in reg["fontes"] if f["grupo"] == g["id"]), key=lambda f: f["n"])
        lis = []
        for f in fs:
            estado = f.get("estado")
            cab = (f'<p class="f-cab"><span class="f-num">{f["n"]}</span>'
                   + (f'<span class="estado {estado}">{ESTADO[estado]}</span>' if estado else "") + "</p>")
            links = "".join(f'<a href="{esc(l["url"])}" target="_blank" rel="noopener">{esc(l["rotulo"])}'
                            + (' <span class="f-tipo">(secundária)</span>' if l.get("secundaria") else "") + " ↗</a>"
                            for l in f["links"])
            nota = f'<p class="f-nota">{esc(f["nota"])}</p>' if f.get("nota") else ""
            lis.append(f'<li id="ref-{f["n"]}" data-grupo="{g["id"]}">{cab}<p class="f-tit">{esc(f["titulo"])}</p>'
                       f'<p class="f-prova">{esc(f["prova"])}</p>{nota}<div class="f-links">{links}</div>'
                       f'{citada_em(f["n"], usos)}</li>')
        rotulo = "fonte" if len(fs) == 1 else "fontes"
        partes.append(f'<section class="grupo-fontes" id="{g["id"]}"><h2>{esc(g["titulo"])} <span class="sub">'
                      f'{len(fs)} {rotulo}</span></h2><ol class="fontes">{"".join(lis)}</ol></section>')
    return "\n" + "\n".join(partes) + "\n"


def lista_termos(pag, info):
    itens = "".join(f'<div id="t-{t["id"]}"><dt>{esc(t["termo"])}</dt><dd>{esc(t["def"])}</dd></div>'
                    for t in carrega_termos())
    return f'<dl class="glossario">{itens}</dl>'


def fontes_js():
    reg = carrega_fontes()
    grupos = {g["id"]: g["titulo"] for g in reg["grupos"]}
    fontes = {str(f["n"]): {"titulo": f["titulo"], "prova": f["prova"], "grupo": grupos[f["grupo"]],
                            "estado": f.get("estado", ""),
                            "links": [{"rotulo": l["rotulo"], "url": l["url"], "secundaria": bool(l.get("secundaria"))}
                                      for l in f["links"]]}
              for f in reg["fontes"]}
    termos = {t["id"]: {"termo": t["termo"], "def": t["def"]} for t in carrega_termos()}
    corpo = json.dumps({"fontes": fontes, "termos": termos}, ensure_ascii=False, separators=(",", ":"))
    return ("/* Gerado por scripts/montar_site.py a partir de dados/fontes.json e dados/glossario.json. "
            "Não edite à mão. */\nwindow.DOSSIE = " + corpo + ";\n")


BLOCOS = {
    "b:cabeca": cabeca, "b:topo": topo, "b:rodape": rodape, "b:pager": pager, "b:toc": toc, "b:data": data,
    "b:cartoes": cartoes, "b:situacao-curta": situacao_curta,
    "t:situacao": situacao, "t:federal": federal, "t:cnes": cnes,
    "b:lista-termos": lista_termos,
    "d:dados": lambda pag, info: graficos.dados_js(),
    "g:pagos-contados": lambda pag, info: graficos.pagos_contados(),
    "g:media-residente": lambda pag, info: graficos.media_residente(),
    "g:bolsa-mes": lambda pag, info: graficos.bolsa_mes(),
    "b:lista-fontes": None,  # depende de onde cada fonte é citada: preenchido no segundo passo
}
MARCADOR = re.compile(r"<!--([a-z]):([a-z0-9-]+)-->(.*?)<!--/\1:\2-->", re.S)


def substitui(pag, texto, erros):
    info = le(texto)
    abertos = re.findall(r"<!--([a-z]:[a-z0-9-]+)-->", texto)
    fechados = [f"{a}:{b}" for a, b, _ in MARCADOR.findall(texto)]
    for m in sorted(set(abertos) - set(fechados)):
        erros.append(f"{pag}: marcador <!--{m}--> sem o <!--/{m}--> correspondente")

    def troca(mo):
        chave = f"{mo.group(1)}:{mo.group(2)}"
        if chave not in BLOCOS:
            erros.append(f"{pag}: marcador desconhecido <!--{chave}-->")
            return mo.group(0)
        f = BLOCOS[chave]
        return mo.group(0) if f is None else f"<!--{chave}-->{f(pag, info)}<!--/{chave}-->"
    return MARCADOR.sub(troca, texto)


def coleta_usos(paginas):
    usos = {}
    for pag, _, _, _, _ in PAGINAS:
        if pag == "fontes.html":
            continue
        for g in le(paginas[pag]).gatilhos:
            secao = g["secao"] or [None, None]
            for n in g["ref"].split():
                usos.setdefault(n, []).append((pag, secao[0], secao[1]))
    return usos


def confere(paginas, fontes, termos):
    erros, leitores = [], {pag: le(texto) for pag, texto in paginas.items()}
    ids = {pag: {i for i, _ in l.ids} for pag, l in leitores.items()}
    for pag, l in leitores.items():
        vistos = set()
        for i, linha in l.ids:
            if i in vistos:
                erros.append(f"{pag}:{linha}: id repetido {i!r}")
            vistos.add(i)
        for g in l.gatilhos:
            onde = f"{pag}:{g['linha']}"
            if g["ref"]:
                ns = g["ref"].split()
                erros += [f"{onde}: data-ref {n} não existe em dados/fontes.json" for n in ns if n not in fontes]
                if g["tag"] == "a" and g["href"] != href_fonte(ns[0], pag):
                    erros.append(f"{onde}: trecho com data-ref=\"{g['ref']}\" deveria ter href=\"{href_fonte(ns[0], pag)}\"")
                if g["tag"] == "a" and not {"cita", "ref"} & set(g["classes"]):
                    erros.append(f"{onde}: link com data-ref precisa da classe cita ou ref")
            if g["termo"]:
                if g["termo"] not in termos:
                    erros.append(f"{onde}: data-termo {g['termo']!r} não existe em dados/glossario.json")
                if g["href"] != f"glossario.html#t-{g['termo']}":
                    erros.append(f"{onde}: termo {g['termo']!r} deveria ter href=\"glossario.html#t-{g['termo']}\"")
                if "termo" not in g["classes"]:
                    erros.append(f"{onde}: link com data-termo precisa da classe termo")
        for href, linha in l.links:
            if re.match(r"(https?:|mailto:)", href):
                continue
            alvo, _, frag = href.partition("#")
            alvo = alvo or pag
            if alvo.startswith(("dados/", "assets/")):
                if not os.path.exists(os.path.join(RAIZ, alvo)):
                    erros.append(f"{pag}:{linha}: arquivo não existe: {href}")
            elif alvo not in ids:
                erros.append(f"{pag}:{linha}: página não existe: {href}")
            elif frag and frag not in ids[alvo]:
                erros.append(f"{pag}:{linha}: âncora não existe: {href}")
    return erros


def main():
    verificar = "--verificar" in sys.argv
    reg, termos_lista = carrega_fontes(), carrega_termos()
    erros = confere_registros(reg, termos_lista)
    fontes = {str(f["n"]): f for f in reg["fontes"]}
    termos = {t["id"]: t for t in termos_lista}

    originais = {}
    for pag, _, _, _, _ in PAGINAS:
        with open(os.path.join(RAIZ, pag), encoding="utf-8") as fh:
            originais[pag] = fh.read()
    paginas = {pag: substitui(pag, texto, erros) for pag, texto in originais.items()}
    usos = coleta_usos(paginas)
    lista = lista_fontes(usos)
    paginas["fontes.html"] = re.sub(r"(<!--b:lista-fontes-->).*?(<!--/b:lista-fontes-->)",
                                    lambda mo: mo.group(1) + lista + mo.group(2), paginas["fontes.html"], flags=re.S)
    erros += confere(paginas, fontes, termos)
    if erros:
        print("\n".join(erros))
        sys.exit(f"{len(erros)} problema(s); nada foi gravado")
    sem_uso = sorted((n for n in fontes if n not in usos), key=int)
    if sem_uso:
        print("aviso: fontes que nenhuma página cita (continuam na lista): " + ", ".join(sem_uso))

    saidas = dict(paginas)
    saidas[os.path.join("assets", "fontes.js")] = fontes_js()
    mudou = []
    for nome, texto in saidas.items():
        caminho = os.path.join(RAIZ, nome)
        antigo = open(caminho, encoding="utf-8").read() if os.path.exists(caminho) else None
        if antigo == texto:
            continue
        mudou.append(nome)
        if not verificar:
            with open(caminho + ".tmp", "w", encoding="utf-8") as fh:
                fh.write(texto)
            os.replace(caminho + ".tmp", caminho)
    if verificar:
        if mudou:
            sys.exit("desatualizado (rode python3 scripts/montar_site.py): " + ", ".join(mudou))
        print(f"ok: {len(PAGINAS)} páginas conferidas")
    else:
        print(("atualizado: " + ", ".join(mudou)) if mudou else "nada mudou")


if __name__ == "__main__":
    main()
