#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Benchmark do verificador de registros.

    python3 ferramentas/benchmark.py

Cada caso declara o que ESPERA que o verificador aponte. O executor
compara esperado contra obtido e separa dois tipos de falha, que são
exatamente os dois erros que o livro mede:

  FALSO NEGATIVO — a não-conformidade existe e o verificador NÃO viu.
                   É o mecanismo passando. É o pior dos dois.
  FALSO POSITIVO — o verificador apontou o que não havia.
                   É categorizar sem exame, cometido pela ferramenta.

Um verificador com falso positivo é uma máquina que faz M4. Por isso os
controles positivos existem, e por isso falham alto.

Sem dependência externa. CC BY-SA · AMARYAPU
"""
import json, pathlib, sys, datetime
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from conferir_registro import confere

B = pathlib.Path(__file__).resolve().parent.parent

def main():
    casos = json.loads((B/"benchmark/CASOS.json").read_text(encoding="utf-8"))
    linhas, fneg, fpos, ok = [], 0, 0, 0

    for c in casos:
        r = json.loads((B/c["arquivo"]).read_text(encoding="utf-8"))
        obtidas = confere(r)
        esperadas = c["espera"]

        faltou = [e for e in esperadas
                  if not any(e.lower() in o.lower() for o in obtidas)]
        sobrou = [o for o in obtidas
                  if not any(e.lower() in o.lower() for e in esperadas)]

        if faltou: fneg += len(faltou)
        if sobrou: fpos += len(sobrou)
        passou = not faltou and not sobrou
        if passou: ok += 1

        linhas.append({"id": pathlib.Path(c["arquivo"]).stem, "titulo": c["titulo"],
                       "mecanismo": c["mecanismo"], "passou": passou,
                       "esperadas": len(esperadas), "obtidas": len(obtidas),
                       "faltou": faltou, "sobrou": sobrou})

    # ── relatório ───────────────────────────────────────────────────
    print(f"BENCHMARK · {len(casos)} casos · {datetime.date.today():%d/%m/%Y}\n")
    print(f"{'caso':26} {'mecanismo':34} {'esp':>4} {'obt':>4}  resultado")
    print("─"*92)
    for l in linhas:
        marca = "✅" if l["passou"] else "❌"
        print(f"{l['id']:26} {l['mecanismo'][:34]:34} {l['esperadas']:4} "
              f"{l['obtidas']:4}  {marca}")
        for x in l["faltou"]: print(f"{'':26} ↳ FALSO NEGATIVO · não apontou: {x}")
        for x in l["sobrou"]: print(f"{'':26} ↳ FALSO POSITIVO · apontou a mais: {x[:60]}")
    print("─"*92)
    print(f"  {ok}/{len(casos)} casos corretos")
    print(f"  falsos negativos: {fneg}   (o mecanismo passou)")
    print(f"  falsos positivos: {fpos}   (a ferramenta categorizou sem exame)")

    rel = {"data": str(datetime.date.today()), "casos": len(casos), "corretos": ok,
           "falsos_negativos": fneg, "falsos_positivos": fpos, "detalhe": linhas}
    (B/"benchmark/RESULTADO.json").write_text(
        json.dumps(rel, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n  benchmark/RESULTADO.json")
    return 0 if (fneg == 0 and fpos == 0) else 1

if __name__ == "__main__":
    sys.exit(main())
