#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O símbolo — desenhado por fórmula, não escolhido por gosto.

    python3 ferramentas/simbolo.py     # gera flor.svg

Três camadas, todas computadas, nenhuma decorativa:

  1. FLOR DA VIDA — 19 círculos de raio r, centros em retículo hexagonal
     com distância r entre vizinhos. É a figura que aparece em pedra,
     em templo e em caderno de geometria em culturas que nunca se
     encontraram, porque é a consequência mais simples de uma única
     regra: circunferências de mesmo raio passando pelo centro umas das
     outras.

  2. ESPIRAL ÁUREA — espiral logarítmica r(θ) = a·e^(bθ), com b tal que
     o raio multiplica por φ a cada quarto de volta: b = ln(φ)/(π/2).

  3. FILOTAXIA — 89 sementes no ÂNGULO ÁUREO de 137,507764°, raio √n.
     89 é número de Fibonacci. É a mesma constante que posiciona as
     estrelas da constelação do AMARYAPU.

φ = (1+√5)/2 não foi escolhido por ser bonito. É a única razão que
resolve a/b = (a+b)/a — a proporção que se repete em toda escala.
"""
import math, pathlib

PHI   = (1 + 5 ** 0.5) / 2
AUREO = 137.507764                 # graus — o mesmo da constelação
R     = 100.0                      # raio do círculo unitário da flor
OURO  = "#D4A94A"
S     = 420                        # lado do quadro

def flor_da_vida():
    """19 círculos: 1 central + 6 + 12, retículo hexagonal de passo R."""
    cs, vistos = [], set()
    for i in range(-2, 3):
        for j in range(-2, 3):
            x = R * (i + j * 0.5)
            y = R * (j * math.sqrt(3) / 2)
            if math.hypot(x, y) > 2 * R + 1e-6:      # só os 19 de dentro
                continue
            k = (round(x, 4), round(y, 4))
            if k in vistos: continue
            vistos.add(k); cs.append((x, y))
    return cs

def espiral_aurea(voltas=3.0, passos=720):
    """r(θ) = a·e^(bθ), b = ln(φ)/(π/2): φ a cada quarto de volta."""
    b = math.log(PHI) / (math.pi / 2)
    th_f = voltas * 2 * math.pi
    a = (3 * R) / math.exp(b * th_f)                  # termina na borda
    return [(a * math.exp(b * t) * math.cos(t),
             a * math.exp(b * t) * math.sin(t))
            for t in (th_f * i / passos for i in range(passos + 1))]

def sementes(n=89):
    """Filotaxia: ângulo áureo, raio √n. 89 é Fibonacci."""
    a = math.radians(AUREO)
    return [(math.sqrt(k / n) * 3 * R * math.cos(k * a),
             math.sqrt(k / n) * 3 * R * math.sin(k * a),
             1.1 + 2.0 * math.sqrt(k / n))
            for k in range(1, n + 1)]

def main():
    # os 19 círculos alcançam 3R a partir do centro (centro a 2R + raio R).
    # O quadro precisa contê-los: cortar por acidente é desenhar à mão
    # aquilo que se disse ter sido calculado.
    v = 3 * R * 1.05
    cab = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" '
           f'viewBox="{-v} {-v} {2*v} {2*v}" role="img" '
           f'aria-label="Flor da vida com espiral áurea e filotaxia no ângulo áureo">')
    out = [cab,
           '<title>φ — a proporção que se repete em toda escala</title>',
           '<desc>Flor da vida: 19 círculos de raio igual em retículo hexagonal. '
           'Espiral logarítmica com crescimento φ por quarto de volta. '
           '89 sementes no ângulo áureo de 137,507764°. '
           'Gerado por ferramentas/simbolo.py — nada aqui foi desenhado à mão.</desc>',
           '<g fill="none" stroke-linecap="round">']

    for x, y in flor_da_vida():
        out.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{R:.3f}" '
                   f'stroke="{OURO}" stroke-opacity=".34" stroke-width="2.1"/>')
    out.append(f'<circle cx="0" cy="0" r="{3*R:.3f}" stroke="{OURO}" '
               f'stroke-opacity=".7" stroke-width="2.8"/>')
    out.append(f'<circle cx="0" cy="0" r="{2*R:.3f}" stroke="{OURO}" '
               f'stroke-opacity=".3" stroke-width="1.6"/>')

    d = " ".join(("M" if i == 0 else "L") + f"{x:.3f} {y:.3f}"
                 for i, (x, y) in enumerate(espiral_aurea()))
    out.append(f'<path d="{d}" stroke="{OURO}" stroke-opacity=".9" stroke-width="3"/>')
    out.append('</g><g fill="' + OURO + '">')
    for x, y, r in sementes():
        out.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r:.2f}" fill-opacity=".85"/>')
    out.append('</g></svg>')

    svg = "\n".join(out)
    pathlib.Path("flor.svg").write_text(svg, encoding="utf-8")
    print(f"flor.svg · {len(flor_da_vida())} círculos · 89 sementes · "
          f"φ={PHI:.9f} · ângulo áureo {AUREO}° · {len(svg)//1024} KB")

if __name__ == "__main__":
    main()
