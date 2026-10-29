/* Dossiê da bolsa dos residentes de MFC de Santa Maria: comportamento comum a todas as páginas.
   Sem dependências e sem envio de dados. Sem JavaScript tudo continua legível: os trechos com fonte
   levam à lista de fontes, os termos ao glossário, e as tabelas montadas aqui estão nos CSVs de dados/. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");
  var MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];
  function brl(v) { return "R$ " + v.toLocaleString("pt-BR", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  var temDialog = typeof HTMLDialogElement === "function";

  /* ---- links da antiga página única (#reajuste, #ref-5...) levam à página nova ---- */
  if (document.body.getAttribute("data-pagina") === "index.html" && location.hash) {
    var ANTIGOS = {
      reajuste: "reajuste.html", contagem: "contagem.html", fazer: "fazer.html", numeros: "numeros.html",
      detalhes: "numeros.html", "d-federal": "numeros.html#federal", "d-equipes": "contagem.html#cnes",
      "d-tempo": "linha-do-tempo.html", "d-empenhos": "numeros.html#empenhos", "d-metodo": "sobre.html#metodo",
      "d-aberto": "sobre.html#em-aberto", "d-glossario": "glossario.html", "d-correcoes": "sobre.html#correcoes",
      fontes: "fontes.html"
    };
    var antigo = location.hash.slice(1);
    var novo = ANTIGOS[antigo] || (/^ref-\d+$/.test(antigo) ? "fontes.html#" + antigo : "");
    if (novo) { location.replace(novo); return; }
  }

  /* ---- tema ---- */
  function aplicaTema(t) {
    if (t === "light" || t === "dark") doc.setAttribute("data-theme", t); else doc.removeAttribute("data-theme");
    $$("[data-tema]").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.tema === (t || "auto"))); });
  }
  var temaSalvo = null;
  try { temaSalvo = localStorage.getItem("dossie-tema"); } catch (e) {}
  aplicaTema(temaSalvo);
  $$("[data-tema]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.dataset.tema === "auto" ? null : b.dataset.tema;
      aplicaTema(t);
      try { if (t) localStorage.setItem("dossie-tema", t); else localStorage.removeItem("dossie-tema"); } catch (e) {}
    });
  });

  /* ---- menu ---- */
  $$("dialog [data-fechar]").forEach(function (b) { b.addEventListener("click", function () { var d = b.closest("dialog"); if (d.close) d.close(); }); });
  $$("dialog.folha").forEach(function (d) { d.addEventListener("click", function (e) { if (e.target === d) d.close(); }); });
  var menu = $("#menu"), abreMenu = $("#abre-menu");
  if (menu && abreMenu) {
    abreMenu.addEventListener("click", function (e) {
      if (!temDialog || !menu.showModal) return;   /* sem <dialog>, o link leva ao mapa no rodapé */
      e.preventDefault(); menu.showModal();
    });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { menu.close(); }); });
  }

  /* ---- balões: trecho com fonte (data-ref) e termo do glossário (data-termo) ----
     Mouse: o balão aparece ao passar por cima e continua aberto enquanto o ponteiro estiver nele,
     para dar tempo de clicar nos links; clicar no trecho abre a fonte na lista de fontes.
     Toque: o primeiro toque abre o balão (com botão de fechar); tocar fora fecha.
     Teclado: o balão aparece com o foco; Esc fecha; Enter segue o link. */
  var DADOS = window.DOSSIE || { fontes: {}, termos: {} };
  var ESTADO = { primaria: "Conferida na fonte primária", parcial: "Conferida em parte", conferir: "A conferir" };
  var balao = $("#balao");
  var atual = null, fixo = false, tAbre = 0, tFecha = 0, ponteiro = "", ultimoXY = null;

  function cria(tag, cls, txt) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (txt != null) e.textContent = txt;
    return e;
  }
  function itemFonte(n) {
    var f = DADOS.fontes[n]; if (!f) return null;
    var item = cria("div", "b-item"), cab = cria("p", "b-cab");
    cab.appendChild(cria("span", "f-num", n));
    cab.appendChild(cria("span", null, f.grupo));
    if (f.estado) cab.appendChild(cria("span", "estado " + f.estado, ESTADO[f.estado]));
    item.appendChild(cab);
    item.appendChild(cria("p", "b-tit", f.titulo));
    item.appendChild(cria("p", "b-prova", f.prova));
    var ls = cria("div", "b-links");
    f.links.forEach(function (l) {
      var a = cria("a", l.secundaria ? "sec" : null, l.rotulo + (l.secundaria ? " (secundária)" : "") + " ↗");
      a.href = l.url; a.target = "_blank"; a.rel = "noopener";
      ls.appendChild(a);
    });
    item.appendChild(ls);
    return item;
  }
  function itemTermo(id) {
    var t = DADOS.termos[id]; if (!t) return null;
    var item = cria("div", "b-item");
    item.appendChild(cria("p", "b-tit", t.termo));
    item.appendChild(cria("p", "b-prova", t.def));
    var mais = cria("a", "b-mais", "Ver no glossário →"); mais.href = "glossario.html#t-" + id;
    item.appendChild(mais);
    return item;
  }
  function preenche(alvo, fixar) {
    var itens = [];
    if (alvo.dataset.termo) {
      var t = itemTermo(alvo.dataset.termo); if (t) itens.push(t);
    } else {
      var ns = (alvo.dataset.ref || "").split(/\s+/).filter(Boolean);
      ns.forEach(function (n) { var f = itemFonte(n); if (f) itens.push(f); });
      if (itens.length) {
        var mais = cria("a", "b-mais", "Ver na lista de fontes →");
        mais.href = "fontes.html#ref-" + ns[0];
        itens[itens.length - 1].appendChild(mais);
      }
    }
    if (!itens.length) return false;
    balao.textContent = "";
    itens.forEach(function (i) { balao.appendChild(i); });
    if (fixar) {
      var x = cria("button", "b-fechar", "×");
      x.type = "button"; x.setAttribute("aria-label", "Fechar");
      x.addEventListener("click", function () { fecha(true); });
      balao.appendChild(x);
    }
    return true;
  }
  function posiciona() {
    if (!atual) return;
    /* na vertical o balão fica fora do trecho inteiro, para não cobrir o texto; na horizontal, centrado na
       linha do ponteiro quando o trecho quebra em várias linhas */
    var todo = atual.getBoundingClientRect(), rs = atual.getClientRects(), r = rs[0] || todo;
    if (rs.length > 1 && ultimoXY) {
      for (var i = 0; i < rs.length; i++) if (ultimoXY[1] >= rs[i].top - 2 && ultimoXY[1] <= rs[i].bottom + 2) { r = rs[i]; break; }
    }
    var vw = doc.clientWidth, vh = window.innerHeight;
    if (todo.bottom < 0 || todo.top > vh) { fecha(false); return; }
    balao.style.left = "0px"; balao.style.top = "0px";
    var bw = balao.offsetWidth, bh = balao.offsetHeight;
    var cx = Math.min(Math.max(r.left + r.width / 2, 14), vw - 14);
    var x = Math.round(Math.min(Math.max(8, cx - bw / 2), vw - bw - 8));
    var abaixo = todo.bottom + 10 + bh <= vh - 8 || todo.top - 10 - bh < 8;
    var y = Math.round(abaixo ? todo.bottom + 10 : todo.top - 10 - bh);
    balao.style.left = x + "px"; balao.style.top = y + "px";
    balao.classList.toggle("acima", !abaixo);
  }
  function abre(alvo, fixar) {
    clearTimeout(tAbre); clearTimeout(tFecha);
    if (atual && atual !== alvo) atual.removeAttribute("aria-describedby");
    if (!preenche(alvo, fixar)) return;
    atual = alvo; fixo = !!fixar;
    balao.classList.toggle("fixo", fixo);
    balao.hidden = false;
    alvo.setAttribute("aria-describedby", "balao");
    posiciona();
  }
  function fecha(devolveFoco) {
    clearTimeout(tAbre); clearTimeout(tFecha);
    if (!atual) return;
    var era = atual, focoDentro = balao.contains(document.activeElement);
    balao.hidden = true; era.removeAttribute("aria-describedby");
    atual = null; fixo = false;
    if (devolveFoco && focoDentro) era.focus({ preventScroll: true });
  }
  function fechaDepois() { clearTimeout(tFecha); tFecha = setTimeout(function () { fecha(false); }, 300); }

  if (balao) {
    document.addEventListener("pointerdown", function (e) {
      ponteiro = e.pointerType || "mouse"; ultimoXY = [e.clientX, e.clientY];
      if (atual && !balao.contains(e.target) && !atual.contains(e.target)) fecha(false);
    }, true);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && atual) { fecha(true); return; }
      ponteiro = "";
    });
    $$("a.cita, a.ref, a.termo").forEach(function (a) {
      a.addEventListener("pointerenter", function (e) {
        if (e.pointerType !== "mouse") return;
        ultimoXY = [e.clientX, e.clientY];
        clearTimeout(tFecha);
        if (atual === a) return;
        clearTimeout(tAbre);
        tAbre = setTimeout(function () { abre(a, false); }, atual ? 60 : 160);
      });
      a.addEventListener("pointerleave", function (e) {
        if (e.pointerType !== "mouse") return;
        clearTimeout(tAbre);
        if (atual === a && !fixo) fechaDepois();
      });
      a.addEventListener("focus", function () {
        var teclado = true;
        try { teclado = a.matches(":focus-visible"); } catch (x) {}
        if (teclado && atual !== a) { ultimoXY = null; abre(a, false); }
      });
      a.addEventListener("blur", function (e) {
        if (atual === a && !fixo && !(e.relatedTarget && balao.contains(e.relatedTarget))) fechaDepois();
      });
      a.addEventListener("click", function (e) {
        if (ponteiro !== "touch" && ponteiro !== "pen") return;   /* mouse e teclado seguem o link */
        e.preventDefault();
        if (atual === a && fixo) { fecha(false); return; }
        abre(a, true);
      });
    });
    balao.addEventListener("pointerenter", function (e) { if (e.pointerType === "mouse") clearTimeout(tFecha); });
    balao.addEventListener("pointerleave", function (e) { if (e.pointerType === "mouse" && !fixo) fechaDepois(); });
    var pendente = false;
    function acompanha() {
      if (pendente || !atual) return;
      pendente = true;
      requestAnimationFrame(function () { pendente = false; if (!atual) return; if (fixo) posiciona(); else fecha(false); });
    }
    addEventListener("scroll", acompanha, { passive: true });
    addEventListener("resize", acompanha);
  }

  /* ---- gráficos: dica no mouse, leitura no toque ---- */
  var tip = $("#tip");
  function mostraTip(e, t) {
    if (!tip) return;
    tip.textContent = t; tip.style.opacity = "1";
    var r = tip.getBoundingClientRect(), x = e.clientX + 14, y = e.clientY + 14;
    if (x + r.width > innerWidth - 8) x = e.clientX - r.width - 12;
    if (y + r.height > innerHeight - 8) y = e.clientY - r.height - 12;
    tip.style.left = x + "px"; tip.style.top = y + "px";
  }
  function escondeTip() { if (tip) tip.style.opacity = "0"; }
  addEventListener("scroll", escondeTip, { passive: true });
  function leitura(alvo, texto) {
    var painel = alvo.closest(".painel"); if (!painel) return;
    var l = $(".leitura", painel); if (l) l.textContent = texto;
    $$(".g-hit.sel", painel).forEach(function (h) { h.classList.remove("sel"); });
    alvo.classList.add("sel");
  }
  $$(".g-hit").forEach(function (h) {
    var t = h.getAttribute("data-tip");
    var tt = h.querySelector("title"); if (tt) tt.remove();  /* evita a dica nativa por cima da .tip */
    h.addEventListener("pointermove", function (e) { if (e.pointerType === "mouse") mostraTip(e, t); });
    h.addEventListener("pointerleave", escondeTip);
    h.addEventListener("click", function () { escondeTip(); leitura(h, t); if (h.dataset.mes) abreMes(+h.dataset.ano, +h.dataset.mes); });
  });

  /* arrastar o dedo sobre o gráfico percorre os meses; botões andam um mês por vez */
  $$("svg.g").forEach(function (svg) {
    var hits = $$(".g-hit", svg); if (!hits.length) return;
    var painel = svg.closest(".painel");
    svg.style.touchAction = "pan-y";
    function noPonto(e) {
      var pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY;
      var ctm = svg.getScreenCTM(); if (!ctm) return;
      var x = pt.matrixTransform(ctm.inverse()).x, alvo = hits[0];
      hits.forEach(function (h) { if (x >= +h.getAttribute("x")) alvo = h; });
      if (!alvo.classList.contains("sel")) alvo.dispatchEvent(new Event("click"));
    }
    svg.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse") noPonto(e); });
    svg.addEventListener("pointermove", function (e) { if (e.pointerType !== "mouse" && e.buttons) noPonto(e); });
    var l = painel && $(".leitura", painel); if (!l) return;
    var passos = document.createElement("div"); passos.className = "passos";
    passos.innerHTML = '<button type="button" data-passo="-1">‹ mês anterior</button><button type="button" data-passo="1">próximo mês ›</button>';
    l.parentNode.insertBefore(passos, l.nextSibling);
    $$("button", passos).forEach(function (b) {
      b.addEventListener("click", function () {
        var i = hits.indexOf($(".g-hit.sel", svg));
        var j = i < 0 ? hits.length - 1 : Math.min(hits.length - 1, Math.max(0, i + +b.dataset.passo));
        hits[j].dispatchEvent(new Event("click"));
      });
    });
  });

  /* ---- empenhos (dados embutidos em numeros.html) ---- */
  var D = { emp: [], agg: [], mes: {} };
  var bloco = $("#dados");
  if (bloco) { try { var bruto = JSON.parse(bloco.textContent); D = { emp: bruto.emp || [], agg: bruto.agg || [], mes: bruto.mes || {} }; } catch (e) {} }
  var chavesMes = Object.keys(D.mes).map(function (k) { var p = k.split("-"); return +p[0] * 12 + (+p[1] - 1); });
  var iniMes = chavesMes.length ? Math.min.apply(null, chavesMes) : 0, fimMes = chavesMes.length ? Math.max.apply(null, chavesMes) : -1;
  function plural(n, um, varios) { return n === 1 ? um : varios; }

  function tabelaMes(a, m) {
    var col = D.emp.filter(function (e) { return e.a === a && e.m === m; });
    var ag = D.agg.filter(function (e) { return e.a === a && e.m === m; })[0];
    if (col.length) {
      return '<div class="tabela"><table><thead><tr><th>Empenho</th><th class="n">Valor</th><th class="n">Resid.</th></tr></thead><tbody>' +
        col.map(function (e) {
          return '<tr><td><a href="' + e.u + '" target="_blank" rel="noopener">' + e.nr + "/" + e.a + ' ↗</a><br><span class="mini">' + e.d +
            " · " + e.f + '</span></td><td class="n">' + brl(e.v) + '</td><td class="n">' + (e.n || "—") + "</td></tr>";
        }).join("") + "</tbody></table></div>";
    }
    if (ag) {
      var bq = Math.round(ag.v / 4500);
      return '<p class="nota">' + ag.q + plural(ag.q, " empenho individual", " empenhos individuais") + ", somando " + brl(ag.v) +
        " (≈ " + bq + plural(bq, " bolsa", " bolsas") + "). Os nomes não são reproduzidos; a consulta nominal está no portal oficial.</p>";
    }
    return '<p class="nota">Sem empenho específico neste mês; o pagamento saiu acumulado em outro mês.</p>';
  }
  function abreMes(a, m) {
    var alvo = $("#mes-detalhe"); if (!alvo) return;
    if (!chavesMes.length) { alvo.innerHTML = '<p class="nota">Os dados dos empenhos não carregaram. Veja as tabelas em dados/ no repositório.</p>'; return; }
    alvo.innerHTML = "<h3>" + MESES[m - 1] + "/" + a + " · " + brl(D.mes[a + "-" + m] || 0) + "</h3>" + tabelaMes(a, m);
  }

  var anos = $("#anos"), caixa = $("#empenhos-tabela");
  function mostraAno(ano) {
    $$("button", anos).forEach(function (b) { b.setAttribute("aria-pressed", String(+b.textContent === ano)); });
    var linhas = [];
    for (var m = 1; m <= 12; m++) {
      var idx = ano * 12 + m - 1;
      if (idx < iniMes || idx > fimMes) continue;
      var v = D.mes[ano + "-" + m] || 0;
      var col = D.emp.filter(function (e) { return e.a === ano && e.m === m; });
      var ag = D.agg.filter(function (e) { return e.a === ano && e.m === m; })[0];
      if (col.length) {
        col.forEach(function (e) {
          linhas.push("<tr><td>" + MESES[m - 1] + '</td><td><a href="' + e.u + '" target="_blank" rel="noopener">' + e.nr + ' ↗</a><br><span class="mini">' + e.f +
            '</span></td><td class="n">' + brl(e.v) + '</td><td class="n">' + (e.n || "—") + "</td></tr>");
        });
      } else if (ag) {
        linhas.push("<tr><td>" + MESES[m - 1] + "</td><td>" + ag.q + plural(ag.q, " individual", " individuais") + '</td><td class="n">' + brl(ag.v) + '</td><td class="n">≈ ' + Math.round(ag.v / 4500) + "</td></tr>");
      } else if (v === 0) {
        linhas.push("<tr><td>" + MESES[m - 1] + '</td><td>sem empenho no mês</td><td class="n">—</td><td class="n">—</td></tr>');
      }
    }
    caixa.innerHTML = '<div class="tabela"><table><thead><tr><th>Mês</th><th>Empenho</th><th class="n">Valor</th><th class="n">Resid.</th></tr></thead><tbody>' +
      linhas.join("") + "</tbody></table></div>";
  }
  if (anos && caixa && chavesMes.length) {
    var lista = [];
    Object.keys(D.mes).forEach(function (k) { var a = +k.split("-")[0]; if (lista.indexOf(a) < 0) lista.push(a); });
    lista.sort().forEach(function (a) {
      var b = document.createElement("button"); b.type = "button"; b.textContent = a;
      b.addEventListener("click", function () { mostraAno(a); }); anos.appendChild(b);
    });
    mostraAno(lista[lista.length - 1]);
  }

  /* ---- busca na lista de fontes ---- */
  var busca = $("#busca-fonte"), limpaFiltro = null;
  if (busca) {
    var filtro = busca.closest(".filtro"), chips = $$(".chips button", filtro);
    var itens = $$("ol.fontes > li"), grupoAtual = "", total = $("#busca-total");
    var normal = function (s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    var textos = itens.map(function (li) { return normal(li.textContent); });
    var aplica = function () {
      var q = normal(busca.value.trim()), n = 0;
      itens.forEach(function (li, i) {
        var ok = (!q || textos[i].indexOf(q) >= 0) && (!grupoAtual || li.getAttribute("data-grupo") === grupoAtual);
        li.hidden = !ok; if (ok) n++;
      });
      $$(".grupo-fontes").forEach(function (g) { g.hidden = !$$("ol.fontes > li", g).some(function (li) { return !li.hidden; }); });
      total.textContent = n === itens.length ? "" : n ? n + plural(n, " fonte encontrada", " fontes encontradas") : "Nenhuma fonte encontrada.";
    };
    var escolheGrupo = function (b) {
      grupoAtual = (b && b.dataset.grupo) || "";
      chips.forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
    };
    filtro.hidden = false;
    busca.addEventListener("input", aplica);
    chips.forEach(function (b) { b.addEventListener("click", function () { escolheGrupo(b); aplica(); }); });
    limpaFiltro = function () { busca.value = ""; escolheGrupo(chips[0]); aplica(); };
  }

  /* ---- abrir o acordeão (ou limpar a busca) quando o link aponta para algo escondido ---- */
  function abreAlvo() {
    var id = location.hash.slice(1); if (!id) return;
    var el = document.getElementById(id); if (!el) return;
    if (limpaFiltro && el.closest("[hidden]")) { limpaFiltro(); el.scrollIntoView(); }
    var d = el.closest("details");
    if (d && !d.open) { d.open = true; el.scrollIntoView(); }
  }
  addEventListener("hashchange", abreAlvo); abreAlvo();

  /* ---- copiar link ---- */
  var copiar = $("#copiar");
  if (copiar) copiar.addEventListener("click", function () {
    var url = location.href.split(/[?#]/)[0].replace(/[^/]*$/, ""), aviso = $("#copiado");
    function avisa(t) { if (aviso) aviso.textContent = t; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () { avisa("Link copiado."); }, function () { avisa("Não deu para copiar. Endereço: " + url); });
    } else avisa("Endereço: " + url);
  });
})();
