# Conta médicos residentes por unidade e equipe no CNES. Nunca imprime nomes nem CNS.
import csv, json, sys, time, urllib.request, collections
B = "https://cnes.datasus.gov.br/services/"
H = {"User-Agent": "Mozilla/5.0", "Referer": "https://cnes.datasus.gov.br/"}
def get(u):
    for i in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(B + u, headers=H), timeout=60))
        except Exception as e:
            err = e; time.sleep(2)
    raise err
src, out_unid, out_eq = sys.argv[1:4]
unid = list(csv.DictReader(open(src)))
ru, re_ = [], []
for u in unid:
    cnes = u["cnes_estabelecimento"]; co = "431690" + cnes
    profs = get("estabelecimentos-profissionais/" + co)
    res = {}
    for p in profs:
        if p.get("vinculacao") == "RESIDENCIA" and str(p.get("cbo", "")).startswith("225"):
            res.setdefault(p["cns"], 0); res[p["cns"]] += (p.get("chAmb") or 0) + (p.get("chOutros") or 0) + (p.get("chHosp") or 0)
    em_equipe = set()
    for e in get("estabelecimentos-equipes/" + co):
        if e.get("dtDesativacao"): continue
        mem = get(f"estabelecimentos-equipes/profissionais/{co}?coMun=431690&coArea={e['coArea']}&coEquipe={e['coEquipe']}")
        r = [m for m in mem if m["cns"] in res and not m.get("dtDesligamento")]
        if not r: continue
        for m in r: em_equipe.add(m["cns"])
        ent = sorted(m.get("dtEntrada") or "" for m in r)
        re_.append({"unidade": u["unidade"], "cnes": cnes, "ine": e["coEquipe"], "tipo_equipe": e["tpEquipe"] + " " + e["dsEquipe"][:30],
                    "medicos_residentes": len(r),
                    "ch_na_equipe_abaixo_40h": sum(1 for m in r if (m.get("chAmb") or 0) + (m.get("chOutros") or 0) < 40),
                    "entrada_antes_de_mar_2024": sum(1 for m in r if m.get("dtEntrada") and m["dtEntrada"][6:] + m["dtEntrada"][3:5] < "202403")})
    ru.append({"unidade": u["unidade"], "cnes": cnes, "medicos_residentes_nov_2026": len(res),
               "ch_total_abaixo_40h": sum(1 for v in res.values() if v < 40),
               "sem_equipe": len(set(res) - em_equipe), "fev_2026": u["medicos_residentes_fev_2026"], "jun_2026": u["medicos_residentes_jun_2026"]})
    print(ru[-1], flush=True)
for path, rows in ((out_unid, ru), (out_eq, re_)):
    w = csv.DictWriter(open(path, "w", newline=""), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
