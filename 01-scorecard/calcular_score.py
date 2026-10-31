#!/usr/bin/env python3
"""
Scorecard de productos ganadores — vault ECOMAI.

Cinco ejes de 20 puntos, los mismos para fisicos y para ebooks, que es lo que
permite que compitan en un solo ranking. Replica el scorecard usado en
05 Plan de accion/Comparativa integral AR y Planificacion - 31 octubre.md.

Uso:
    python3 01-scorecard/calcular_score.py
    python3 01-scorecard/calcular_score.py --detalle <slug>
    python3 01-scorecard/calcular_score.py --tipo digital
"""

import argparse
import glob
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_CANDIDATOS = os.path.join(RAIZ, "03-candidatos")

# Los 5 ejes del vault. 20 puntos cada uno, 100 en total.
EJES = [
    ("afuera",     "Evidencia afuera",      20),
    ("dolor_ar",   "Demanda y dolor en AR",  20),
    ("hueco_meta", "Hueco en Meta AR",       20),
    ("operativa",  "Facilidad operativa",    20),
    ("margen",     "Margen y ecosistema",    20),
]

# Un eje en 0-5 es bloqueante, pase lo que pase con el total.
PISO_BLOQUEANTE = 5

UMBRALES = [
    (88, "EJECUTAR YA",          "\033[92m"),
    (80, "SEGUNDA OLA",          "\033[93m"),
    (60, "SOLO BUMP O BONO",     "\033[33m"),
    (0,  "DESCARTADO",           "\033[91m"),
]
RESET = "\033[0m"
GRIS = "\033[90m"

TIPOS = ("fisico-local", "fisico-courier", "fisico-lab", "digital")


def cargar_candidatos():
    fichas = []
    for ruta in sorted(glob.glob(os.path.join(DIR_CANDIDATOS, "*.json"))):
        nombre = os.path.basename(ruta)
        if nombre.startswith("_"):
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


def evaluar(ficha, usar_propuesto=False):
    """Devuelve (total, veredicto, gates, bloqueantes, detalle).

    usar_propuesto=True usa `score_propuesto` donde exista: son objeciones de un
    relevamiento posterior que todavia no acepto Emanuel. El oficial no se toca.
    """
    scores = ficha.get("scores", {})
    gates = [g for g in ficha.get("gates_fallados", []) if g]

    detalle, total, sin_calificar = [], 0, []
    bloqueantes = []
    for clave, etiqueta, tope in EJES:
        item = scores.get(clave, {})
        valor = item.get("score")
        if usar_propuesto and item.get("score_propuesto") is not None:
            valor = item["score_propuesto"]
        if valor is None:
            sin_calificar.append(etiqueta)
            detalle.append((etiqueta, tope, None, item.get("evidencia", "")))
            continue
        valor = max(0, min(tope, int(valor)))
        total += valor
        if valor <= PISO_BLOQUEANTE:
            bloqueantes.append(f"{etiqueta}: {valor}/{tope}")
        detalle.append((etiqueta, tope, valor, item.get("evidencia", "")))

    if gates:
        return total, "DESCARTADO (gate)", gates, bloqueantes, detalle
    if sin_calificar:
        return total, f"PARCIAL (falta: {', '.join(sin_calificar)})", gates, bloqueantes, detalle

    veredicto = next(n for piso, n, _ in UMBRALES if total >= piso)
    if bloqueantes and veredicto in ("EJECUTAR YA", "SEGUNDA OLA"):
        veredicto = "FRENADO (eje bloqueante)"
    return total, veredicto, gates, bloqueantes, detalle


def color_de(veredicto):
    for _, nombre, c in UMBRALES:
        if veredicto.startswith(nombre):
            return c
    if veredicto.startswith("FRENADO"):
        return "\033[91m"
    return GRIS


def imprimir_ranking(fichas, filtro_tipo=None, usar_propuesto=False):
    if filtro_tipo:
        fichas = [f for f in fichas if f.get("tipo") == filtro_tipo]

    filas = []
    for ficha in fichas:
        total, veredicto, gates, bloq, _ = evaluar(ficha, usar_propuesto)
        oficial = evaluar(ficha)[0]
        filas.append((total, veredicto, gates, bloq, ficha, oficial))
    filas.sort(key=lambda r: -r[0])

    print()
    print("=" * 96)
    print("RANKING MAESTRO DE CANDIDATOS" + (f"  [tipo: {filtro_tipo}]" if filtro_tipo else "")
          + ("   >>> CON OBJECIONES DEL RADAR APLICADAS (no oficial) <<<" if usar_propuesto else ""))
    print("=" * 96)
    if not filas:
        print("\n  No hay fichas cargadas en 03-candidatos/.\n")
        return

    cab = f"\n{'#':<3} {'Candidato':<40} {'Tipo':<16} {'Score':>6}"
    print(cab + (f" {'Oficial':>8}" if usar_propuesto else "") + "  Veredicto")
    print("-" * 96)
    for i, (total, veredicto, gates, bloq, ficha, oficial) in enumerate(filas, 1):
        c = color_de(veredicto)
        nombre = ficha.get("nombre", ficha["slug"])[:39]
        delta = ""
        if usar_propuesto:
            d = total - oficial
            delta = f" {oficial:>8}" + (f" ({d:+d})" if d else "      ")
        print(f"{i:<3} {nombre:<40} {ficha.get('tipo','?'):<16} {total:>5}{delta}   {c}{veredicto}{RESET}")
        for g in gates:
            print(f"    \033[91m[gate]\033[0m {g}")
        for b in bloq:
            print(f"    \033[91m[bloq]\033[0m {b}")
    print("-" * 96)

    ejecutar = [f for f in filas if f[0] >= 88 and not f[2] and not f[3]]
    print()
    if not ejecutar:
        print("  Ningun candidato en zona EJECUTAR YA (>=88 sin gates ni ejes bloqueantes).")
    else:
        print(f"  EJECUTAR YA ({len(ejecutar)}):")
        for total, _, _, _, ficha, _o in ejecutar:
            print(f"    {total:>3}  {ficha.get('nombre')}")
        if len(ejecutar) > 1:
            margen = ejecutar[0][0] - ejecutar[1][0]
            if margen <= 2:
                print()
                print(f"  Los dos primeros estan a {margen} punto(s): empate tecnico.")
                print("  No decide el score. Decide el eje que mas importa hoy, y queda escrito")
                print("  en 04-decision/decision-final.md.")
    print()

    # Resumen por tipo: sirve para ver si la cartera esta desbalanceada.
    por_tipo = {}
    for total, _, gates, bloq, ficha, _o in filas:
        t = ficha.get("tipo", "?")
        por_tipo.setdefault(t, []).append(total)
    if len(por_tipo) > 1 and not filtro_tipo:
        print("  Por tipo:")
        for t in sorted(por_tipo, key=lambda k: -max(por_tipo[k])):
            v = por_tipo[t]
            print(f"    {t:<16} {len(v):>2} candidato(s)   mejor {max(v):>3}   promedio {sum(v)/len(v):>5.1f}")
        print()


def imprimir_detalle(fichas, slug):
    ficha = next((f for f in fichas if f["slug"] == slug or f.get("nombre") == slug), None)
    if not ficha:
        disp = "\n    ".join(f["slug"] for f in fichas) or "(ninguno)"
        sys.exit(f"No encontre '{slug}'. Disponibles:\n    {disp}")

    total, veredicto, gates, bloq, detalle = evaluar(ficha)
    print()
    print("=" * 96)
    print(f"{ficha.get('nombre', slug)}   [{ficha.get('tipo')}]")
    print("=" * 96)
    for campo in ("nicho", "dolor", "referencia_afuera", "mecanismo_culpable",
                  "proveedor", "precio", "cpa_breakeven", "rol"):
        if ficha.get(campo):
            print(f"  {campo.replace('_',' ').capitalize():<20} {ficha[campo]}")
    print()
    print(f"{'Eje':<28} {'Tope':>5} {'Score':>7}")
    print("-" * 96)
    for etiqueta, tope, valor, evidencia in detalle:
        v = f"{valor}" if valor is not None else "-"
        marca = "  <- BLOQUEANTE" if valor is not None and valor <= PISO_BLOQUEANTE else ""
        print(f"{etiqueta:<28} {tope:>5} {v:>7}{marca}")
        if evidencia:
            for linea in [evidencia[i:i+88] for i in range(0, len(evidencia), 88)]:
                print(f"    {GRIS}{linea}{RESET}")
    print("-" * 96)
    print(f"{'TOTAL':<28} {'100':>5} {total:>7}   ->  {color_de(veredicto)}{veredicto}{RESET}")
    for seccion, clave in (("GATES FALLADOS", gates), ("FLAGS", ficha.get("flags", [])),
                           ("PENDIENTES", ficha.get("pendientes", []))):
        if clave:
            print(f"\n  {seccion}:")
            for x in clave:
                print(f"    - {x}")
    if ficha.get("fuente_vault"):
        print(f"\n  {GRIS}Fuente: {ficha['fuente_vault']}{RESET}")
    print()


def main():
    ap = argparse.ArgumentParser(description="Scorecard de productos ganadores (vault ECOMAI)")
    ap.add_argument("--detalle", metavar="SLUG", help="desglose eje por eje")
    ap.add_argument("--tipo", choices=TIPOS, help="filtrar el ranking por tipo")
    ap.add_argument("--propuesto", action="store_true",
                    help="aplicar los score_propuesto de los relevamientos (objeciones sin aceptar)")
    args = ap.parse_args()

    fichas = cargar_candidatos()
    if args.detalle:
        imprimir_detalle(fichas, args.detalle)
    else:
        imprimir_ranking(fichas, args.tipo, args.propuesto)


if __name__ == "__main__":
    main()
