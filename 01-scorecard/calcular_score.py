#!/usr/bin/env python3
"""
Calculadora del scorecard de productos ganadores.

Lee las fichas JSON de 03-candidatos/, aplica los gates de NO-GO, pondera los ejes
segun el tipo (fisico o eprod) y devuelve el ranking.

Uso:
    python3 01-scorecard/calcular_score.py
    python3 01-scorecard/calcular_score.py --detalle <slug>

Formato de ficha: ver 03-candidatos/_plantilla-candidato.json
"""

import argparse
import glob
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_CANDIDATOS = os.path.join(RAIZ, "03-candidatos")

# Pesos por tipo. Deben sumar 1.0 — se verifica al arrancar.
PESOS = {
    "fisico": {
        "market_fit":   (0.30, "Market Fit"),
        "unit_economics": (0.25, "Unit economics"),
        "saturacion":   (0.15, "Saturacion / espacio"),
        "operativa":    (0.15, "Operativa y regulatorio"),
        "ecosistema":   (0.15, "Ecosistema (AOV/LTV)"),
    },
    "eprod": {
        "demanda_pagada": (0.25, "Demanda pagada"),
        "canal_cac":      (0.20, "Canal y CAC"),
        "autoridad":      (0.20, "Autoridad / ventaja injusta"),
        "escalera_ltv":   (0.20, "Escalera de valor / LTV"),
        "entregabilidad": (0.15, "Entregabilidad"),
    },
}

UMBRALES = [
    (75, "GO claro",     "\033[92m"),
    (60, "GO con flags", "\033[93m"),
    (45, "Standby",      "\033[33m"),
    (0,  "NO-GO",        "\033[91m"),
]
RESET = "\033[0m"


def validar_pesos():
    for tipo, ejes in PESOS.items():
        total = sum(p for p, _ in ejes.values())
        if abs(total - 1.0) > 1e-9:
            sys.exit(f"ERROR de configuracion: los pesos de '{tipo}' suman {total}, deben sumar 1.0")


def cargar_candidatos():
    fichas = []
    patron = os.path.join(DIR_CANDIDATOS, "*.json")
    for ruta in sorted(glob.glob(patron)):
        nombre = os.path.basename(ruta)
        if nombre.startswith("_"):       # _plantilla-candidato.json y similares
            continue
        try:
            with open(ruta, encoding="utf-8") as f:
                ficha = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  [!] {nombre}: JSON invalido ({e}). Se omite.", file=sys.stderr)
            continue
        ficha["_archivo"] = nombre
        ficha.setdefault("slug", os.path.splitext(nombre)[0])
        fichas.append(ficha)
    return fichas


def evaluar(ficha):
    """Devuelve (score, veredicto, gates_fallados, detalle_por_eje, musts_fallados)."""
    tipo = ficha.get("tipo")
    if tipo not in PESOS:
        return None, "TIPO INVALIDO", [f"tipo '{tipo}' no es 'fisico' ni 'eprod'"], [], []

    ejes = PESOS[tipo]
    scores = ficha.get("scores", {})

    # --- Gates ---
    gates = [g for g in ficha.get("gates_fallados", []) if g]

    # Gate estructural: 2+ MUSTs fallados (score 0-2 en un eje marcado como must)
    musts_fallados = []
    for clave in ejes:
        item = scores.get(clave, {})
        valor = item.get("score")
        if valor is None:
            musts_fallados.append(f"{clave}: sin calificar")
        elif valor <= 2 and item.get("es_must", True):
            musts_fallados.append(f"{clave}: {valor}/5")
    if len(musts_fallados) >= 2:
        gates.append(f"2+ MUSTs fallados ({len(musts_fallados)})")

    # --- Score ponderado ---
    detalle, acumulado, peso_calificado = [], 0.0, 0.0
    for clave, (peso, etiqueta) in ejes.items():
        item = scores.get(clave, {})
        valor = item.get("score")
        if valor is None:
            detalle.append((etiqueta, peso, None, 0.0, item.get("evidencia", "")))
            continue
        valor = max(0, min(5, float(valor)))
        aporte = (valor / 5.0) * peso * 100
        acumulado += aporte
        peso_calificado += peso
        detalle.append((etiqueta, peso, valor, aporte, item.get("evidencia", "")))

    if gates:
        return 0.0, "NO-GO (gate)", gates, detalle, musts_fallados

    if peso_calificado == 0:
        return None, "SIN CALIFICAR", [], detalle, musts_fallados

    # Si falta calificar ejes, se informa el score sobre lo calificado y se marca.
    score = round(acumulado, 1)
    veredicto = next(nombre for piso, nombre, _ in UMBRALES if score >= piso)
    if musts_fallados and veredicto == "GO claro":
        veredicto = "GO con flags"
    if peso_calificado < 0.999:
        veredicto += f" (parcial: {peso_calificado*100:.0f}% del peso calificado)"
    return score, veredicto, gates, detalle, musts_fallados


def color_de(veredicto):
    for _, nombre, c in UMBRALES:
        if veredicto.startswith(nombre):
            return c
    return ""


def imprimir_ranking(fichas):
    filas = []
    for ficha in fichas:
        score, veredicto, gates, _, musts = evaluar(ficha)
        filas.append((score, veredicto, gates, musts, ficha))

    filas.sort(key=lambda r: (r[0] is None, -(r[0] or 0)))

    print()
    print("=" * 78)
    print("RANKING DE CANDIDATOS")
    print("=" * 78)
    if not filas:
        print("\n  No hay fichas cargadas en 03-candidatos/.")
        print("  Copia 03-candidatos/_plantilla-candidato.json y llenala.\n")
        return

    print(f"\n{'#':<3} {'Candidato':<30} {'Tipo':<8} {'Score':>7}  Veredicto")
    print("-" * 78)
    for i, (score, veredicto, gates, musts, ficha) in enumerate(filas, 1):
        s = f"{score:.1f}" if score is not None else "  -"
        c = color_de(veredicto)
        nombre = ficha.get("nombre", ficha["slug"])[:29]
        print(f"{i:<3} {nombre:<30} {ficha.get('tipo','?'):<8} {s:>7}  {c}{veredicto}{RESET}")
        for g in gates:
            print(f"    \033[91m[gate]\033[0m {g}")
        for m in musts:
            if not gates:
                print(f"    \033[93m[must]\033[0m {m}")
    print("-" * 78)

    ganadores = [f for f in filas if f[0] is not None and f[0] >= 60]
    print()
    if not ganadores:
        print("  Ningun candidato alcanza el piso de 60 (GO con flags).")
        print("  No hay winner que declarar todavia.")
    elif len(ganadores) == 1:
        print(f"  Unico candidato sobre el piso: {ganadores[0][4].get('nombre')}")
        print("  Un winner sin competencia en el ranking no esta comparado: cargar mas candidatos.")
    else:
        top, segundo = ganadores[0], ganadores[1]
        margen = top[0] - segundo[0]
        print(f"  Lider: {top[4].get('nombre')} ({top[0]:.1f})")
        print(f"  Segundo: {segundo[4].get('nombre')} ({segundo[0]:.1f})  —  margen {margen:.1f} pts")
        if margen < 5:
            print("  Margen < 5 pts: empate tecnico. Decidir por el eje que mas importa hoy,")
            print("  no por el score. Dejarlo escrito en 04-decision/decision-final.md.")
    print()


def imprimir_detalle(fichas, slug):
    ficha = next((f for f in fichas if f["slug"] == slug or f.get("nombre") == slug), None)
    if not ficha:
        disponibles = ", ".join(f["slug"] for f in fichas) or "(ninguno)"
        sys.exit(f"No encontre '{slug}'. Disponibles: {disponibles}")

    score, veredicto, gates, detalle, musts = evaluar(ficha)
    print()
    print("=" * 78)
    print(f"{ficha.get('nombre', slug)}  [{ficha.get('tipo')}]")
    print("=" * 78)
    for campo in ("nicho", "mercado", "dolor", "mecanismo_unico", "ticket_objetivo"):
        if ficha.get(campo):
            print(f"  {campo.replace('_',' ').capitalize():<18} {ficha[campo]}")
    print()
    print(f"{'Eje':<30} {'Peso':>6} {'Score':>7} {'Aporte':>8}")
    print("-" * 78)
    for etiqueta, peso, valor, aporte, evidencia in detalle:
        v = f"{valor:.0f}/5" if valor is not None else "   -"
        print(f"{etiqueta:<30} {peso*100:>5.0f}% {v:>7} {aporte:>7.1f}")
        if evidencia:
            print(f"    \033[90m{evidencia[:70]}\033[0m")
    print("-" * 78)
    s = f"{score:.1f}" if score is not None else "-"
    print(f"{'TOTAL':<30} {'100%':>6} {'':>7} {s:>7}  →  {color_de(veredicto)}{veredicto}{RESET}")
    if gates:
        print("\n  GATES FALLADOS:")
        for g in gates:
            print(f"    \033[91m×\033[0m {g}")
    if musts:
        print("\n  MUSTs POR RESOLVER:")
        for m in musts:
            print(f"    \033[93m!\033[0m {m}")
    if ficha.get("flags"):
        print("\n  FLAGS:")
        for f in ficha["flags"]:
            print(f"    - {f}")
    if ficha.get("pendientes"):
        print("\n  PENDIENTES:")
        for p in ficha["pendientes"]:
            print(f"    - {p}")
    print()


def main():
    validar_pesos()
    ap = argparse.ArgumentParser(description="Scorecard de productos ganadores")
    ap.add_argument("--detalle", metavar="SLUG", help="desglose eje por eje de un candidato")
    args = ap.parse_args()

    fichas = cargar_candidatos()
    if args.detalle:
        imprimir_detalle(fichas, args.detalle)
    else:
        imprimir_ranking(fichas)


if __name__ == "__main__":
    main()
