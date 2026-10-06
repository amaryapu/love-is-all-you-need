#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere um REGISTRO DE DECISÃO contra o protocolo.

    python3 ferramentas/conferir_registro.py exemplos/*.json

Não basta o esquema validar. O protocolo tem exigências que são
substantivas, não formais — e são estas que o programa testa:

  C3  a pessoa recebeu o registro, e a cadeia não está vazia
  C4  a contestação suspende o efeito e obriga exame humano
  C5  as ausências estão declaradas
  C8  o custo do erro recai sobre o sistema, e examinar é mais barato
      do que o erro — senão o sistema vai categorizar, por economia

  ATRIBUIDO não pode ter peso. Circula amplamente e não se verificou:
  não entra como fato em hipótese nenhuma.

Sem dependência externa. CC BY-SA · AMARYAPU
"""
import json, sys, pathlib

OBRIGATORIOS = ["id","quando","sujeito","decisao","cadeia","criterio",
                "responsavel","fronteira","derrubar","ausencias","custo"]
ETIQUETAS = {"FATO","CALCULO","DECLARADO","DEMOGRAFICO","TRANSMITIDO",
             "ATRIBUIDO","INTERPRETATIVO","A_CONFERIR"}

def confere(r):
    f = []
    for c in OBRIGATORIOS:
        if c not in r: f.append(f"campo obrigatório ausente: {c}")
    if f: return f

    # ── C3 · procedência ────────────────────────────────────────────
    if not r["sujeito"].get("recebeu_copia"):
        f.append("C3 · a pessoa NÃO recebeu o registro")
    if not r["cadeia"]:
        f.append("C3 · cadeia vazia — a decisão não diz de onde veio")
    for i, e in enumerate(r["cadeia"]):
        et = e.get("etiqueta")
        if et not in ETIQUETAS:
            f.append(f"cadeia[{i}] · etiqueta inválida: {et!r}")
        if et == "ATRIBUIDO" and (e.get("peso") or 0) > 0:
            f.append(f"cadeia[{i}] · ATRIBUIDO com peso {e['peso']} — "
                     "circula amplamente e não se verificou; não entra como fato")
        if et == "FATO" and not e.get("fonte"):
            f.append(f"cadeia[{i}] · FATO sem fonte — cai se a fonte cair, "
                     "e não há fonte para cair")

    # ── critério publicado ANTES ────────────────────────────────────
    if not r["criterio"].get("regra_publicada"):
        f.append("a regra não está publicada — categoria sem critério legível "
                 "não é descrição: é sentença com outro nome")

    # ── C4 · derrubar enquanto está em uso ──────────────────────────
    d = r["derrubar"]
    if not d.get("suspende_efeito"):
        f.append("C4 · a contestação NÃO suspende o efeito — "
                 "revelação tardia não desfaz o que já foi vivido")
    if not d.get("obriga_exame"):
        f.append("C4 · a contestação não obriga exame humano")

    # ── a marca de fronteira ────────────────────────────────────────
    fr = r["fronteira"]
    if fr.get("e_caso_de_fronteira") and fr.get("margem") is None:
        f.append("fronteira · declarada sem margem — "
                 "a marca existe para ser lida, não para constar")

    # ── C5 · índice reverso ─────────────────────────────────────────
    if not r["ausencias"]:
        f.append("C5 · nenhuma ausência declarada — "
                 "ou o sistema tinha todos os campos, ou não olhou")

    # ── C8 · a assimetria ───────────────────────────────────────────
    c = r["custo"]
    if c.get("recai_sobre") != "sistema":
        f.append(f"C8 · custo do erro recai sobre {c.get('recai_sobre')!r} — "
                 "é a assimetria que sustenta o mecanismo")
    ce, cx = c.get("custo_erro_estimado"), c.get("custo_exame_estimado")
    if ce is not None and cx is not None and ce <= cx:
        f.append(f"C8 · errar ({ce}) custa menos que examinar ({cx}) — "
                 "sob pressão este sistema vai categorizar, e estará sendo eficiente")
    return f

def main(args):
    if not args:
        print(__doc__); return 2
    total = 0
    for a in args:
        p = pathlib.Path(a)
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"❌ {p.name}: não é JSON válido — {e}"); total += 1; continue
        f = confere(r)
        if f:
            print(f"❌ {p.name} — {len(f)} não-conformidades")
            for x in f: print(f"     · {x}")
            total += len(f)
        else:
            print(f"✅ {p.name} — conforme")
    print()
    if total:
        print(f"❌ {total} não-conformidades. O registro não cumpre o protocolo.")
        return 1
    print("✅ conforme ao protocolo.")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
