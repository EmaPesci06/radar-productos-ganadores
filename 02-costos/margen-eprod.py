#!/usr/bin/env python3
"""
Unit economics de un eprod.

En digital el margen bruto es ~90% y no discrimina entre candidatos. Lo que
discrimina es CAC/ticket y LTV/CAC. Este script calcula eso, aplica los umbrales
de 00-marco/02-producto-ganador-eprod.md y dice si el negocio cierra.

Uso:
    python3 02-costos/margen-eprod.py --ticket 50000 --cac 12000
    python3 02-costos/margen-eprod.py --ticket 50000 --cac 12000 \
        --reembolsos 12 --plataforma hotmart --escalera 50000 150000 400000
    python3 02-costos/margen-eprod.py --ticket 50000 --breakeven
"""

import argparse
import sys

# Comisiones de referencia, oct 2026. VERIFICAR: el dato de Hotmart viene de un
# comparador de software, no de la fuente oficial.
PLATAFORMAS = {
    "hotmart":      (0.099, 0.50, "9,9% + USD 0,50 por venta (verificar)"),
    "gumroad":      (0.10,  0.0,  "~10% (verificar plan)"),
    "mercadopago":  (0.0599, 0.0, "~5,99% checkout (verificar)"),
    "stripe":       (0.029, 0.30, "2,9% + USD 0,30"),
    "propia":       (0.0,   0.0,  "venta directa, sin plataforma"),
}

UMBRALES = {
    "cac_ticket":  [(0.30, "VERDE"), (0.50, "AMARILLO"), (float("inf"), "ROJO")],
    "reembolsos":  [(0.08, "VERDE"), (0.15, "AMARILLO"), (float("inf"), "ROJO")],
}
COLOR = {"VERDE": "\033[92m", "AMARILLO": "\033[93m", "ROJO": "\033[91m"}
RESET = "\033[0m"


def clasificar(valor, tabla):
    for techo, etiqueta in tabla:
        if valor <= techo:
            return etiqueta
    return "ROJO"


def clasificar_ltv_cac(ratio):
    if ratio >= 3:
        return "VERDE"
    if ratio >= 2:
        return "AMARILLO"
    return "ROJO"


def calcular(ticket, cac, plataforma, reembolsos_pct, impuestos_pct, usd_ars, escalera):
    pct, fijo_usd, _ = PLATAFORMAS[plataforma]
    fijo = fijo_usd * usd_ars

    comision = ticket * pct + fijo
    impuestos = ticket * (impuestos_pct / 100.0)
    bruto = ticket - comision - impuestos

    # Los reembolsos se descuentan del ingreso esperado por venta bruta: de cada 100
    # ventas, N se devuelven y se pierde el ingreso (la comision suele devolverse).
    tasa = reembolsos_pct / 100.0
    neto = bruto * (1 - tasa)

    contribucion = neto - cac
    cac_ticket = cac / ticket if ticket else float("inf")

    # LTV: la escalera son pares (ticket, tasa de conversion a ese escalon).
    # La tasa es la fraccion de compradores del escalon 1 que llega a ese escalon:
    # sin esto el LTV asume que el 100% sube toda la escalera, que es la mentira
    # mas comun del modelado de infoproductos.
    if escalera:
        neto_escalera = sum(
            (t - (t * pct + fijo) - t * (impuestos_pct / 100.0)) * (1 - tasa) * conv
            for t, conv in escalera
        )
    else:
        neto_escalera = neto
    ltv_cac = neto_escalera / cac if cac else float("inf")

    return {
        "ticket": ticket, "comision": comision, "impuestos": impuestos,
        "bruto": bruto, "tasa_reembolso": tasa, "neto": neto,
        "cac": cac, "contribucion": contribucion, "cac_ticket": cac_ticket,
        "ltv": neto_escalera, "ltv_cac": ltv_cac,
        "margen_bruto_pct": bruto / ticket if ticket else 0,
        "plataforma": plataforma, "escalera": escalera,
    }


def imprimir(r, reembolsos_pct):
    m = "ARS"
    print()
    print("=" * 70)
    print("UNIT ECONOMICS — EPROD")
    print("=" * 70)
    print(f"  Plataforma              {r['plataforma']}  ({PLATAFORMAS[r['plataforma']][2]})")
    print()
    print(f"  Ticket                  {m} {r['ticket']:>12,.0f}")
    print(f"  - Comision plataforma   {m} {r['comision']:>12,.0f}")
    print(f"  - Impuestos             {m} {r['impuestos']:>12,.0f}")
    print(f"  = Bruto por venta       {m} {r['bruto']:>12,.0f}   ({r['margen_bruto_pct']*100:.0f}% del ticket)")
    print(f"  - Reembolsos ({reembolsos_pct:.0f}%)       {m} {r['bruto']*r['tasa_reembolso']:>12,.0f}")
    print(f"  = NETO por venta        {m} {r['neto']:>12,.0f}")
    print()
    print(f"  CAC                     {m} {r['cac']:>12,.0f}")
    print(f"  = CONTRIBUCION          {m} {r['contribucion']:>12,.0f}")
    print()
    print("-" * 70)
    print("  RATIOS CONTRA NUESTROS UMBRALES")
    print("-" * 70)

    e = clasificar(r["cac_ticket"], UMBRALES["cac_ticket"])
    print(f"  CAC / Ticket            {r['cac_ticket']*100:>6.1f}%   "
          f"{COLOR[e]}{e}{RESET}   (verde <30%, amarillo 30-50%, rojo >50%)")

    e2 = clasificar(r["tasa_reembolso"], UMBRALES["reembolsos"])
    print(f"  Reembolsos              {r['tasa_reembolso']*100:>6.1f}%   "
          f"{COLOR[e2]}{e2}{RESET}   (verde <8%, amarillo 8-15%, rojo >15%)")

    if r["escalera"]:
        print(f"  LTV (escalera ponderada) {m} {r['ltv']:,.0f}")
        for t, conv in r["escalera"]:
            print(f"    {m} {t:>10,.0f}  x {conv*100:>5.1f}% de conversion")
    else:
        print(f"  LTV (sin escalera)      {m} {r['ltv']:,.0f}   [= una sola compra]")
    e3 = clasificar_ltv_cac(r["ltv_cac"])
    print(f"  LTV / CAC               {r['ltv_cac']:>6.1f}x   "
          f"{COLOR[e3]}{e3}{RESET}   (verde >=3, amarillo 2-3, rojo <2)")
    print("-" * 70)

    print()
    gates = []
    if r["cac_ticket"] > 0.50 and not r["escalera"]:
        gates.append("CAC > 50% del ticket y NO hay escalera de valor cargada.")
    if r["contribucion"] <= 0:
        gates.append("Contribucion negativa o cero: cada venta pierde plata en la primera compra.")
    if r["ltv_cac"] < 2:
        gates.append("LTV/CAC < 2: el negocio no paga su propia adquisicion.")

    if gates:
        print(f"  {COLOR['ROJO']}GATE FALLADO — NO-GO de unit economics{RESET}")
        for g in gates:
            print(f"    x {g}")
    elif r["contribucion"] > 0 and r["ltv_cac"] >= 3:
        print(f"  {COLOR['VERDE']}Unit economics sanas.{RESET} Rentable desde la primera compra")
        print("  y la escalera paga la adquisicion con margen.")
    else:
        print(f"  {COLOR['AMARILLO']}Unit economics ajustadas.{RESET} Cierra, pero sin colchon:")
        print("  depende de que la escalera funcione. Resolver antes de escalar el gasto.")

    if r["contribucion"] < 0 and r["ltv_cac"] >= 3:
        print()
        print("  Nota: breakeven negativo en front-end con LTV/CAC sano es una decision")
        print("  valida (el heroe es la puerta de entrada, no donde se maximiza margen),")
        print("  pero exige caja para financiar el hueco. No es gratis.")
    print()


def breakeven(ticket, plataforma, reembolsos_pct, impuestos_pct, usd_ars):
    """CAC maximo que tolera este ticket en cada umbral."""
    pct, fijo_usd, _ = PLATAFORMAS[plataforma]
    neto = (ticket - (ticket * pct + fijo_usd * usd_ars) - ticket * (impuestos_pct / 100.0))
    neto *= (1 - reembolsos_pct / 100.0)
    print()
    print("=" * 70)
    print(f"CAC MAXIMO TOLERABLE — ticket ARS {ticket:,.0f}")
    print("=" * 70)
    print(f"  Neto por venta                      ARS {neto:,.0f}")
    print()
    print(f"  CAC de breakeven (contribucion 0)   ARS {neto:,.0f}")
    print(f"  CAC para LTV/CAC = 3 (1 compra)     ARS {neto/3:,.0f}")
    print(f"  CAC en umbral verde (30% ticket)    ARS {ticket*0.30:,.0f}")
    print(f"  CAC en techo amarillo (50% ticket)  ARS {ticket*0.50:,.0f}")
    print()
    print("  Si el CAC real de la categoria supera el ultimo numero, el eprod no")
    print("  cierra a este ticket: o sube el ticket, o se construye la escalera primero.")
    print()


def main():
    ap = argparse.ArgumentParser(description="Unit economics de un eprod")
    ap.add_argument("--ticket", type=float, required=True, help="precio de venta en ARS")
    ap.add_argument("--cac", type=float, help="costo de adquisicion por cliente en ARS")
    ap.add_argument("--plataforma", choices=sorted(PLATAFORMAS), default="hotmart")
    ap.add_argument("--reembolsos", type=float, default=12.0,
                    help="%% esperado (default 12, estimacion de industria)")
    ap.add_argument("--impuestos", type=float, default=0.0,
                    help="%% sobre el ticket. Consultar con el contador segun condicion")
    ap.add_argument("--dolar", type=float, default=1520.0, help="ARS por USD")
    ap.add_argument("--escalera", type=str, nargs="+", default=None,
                    metavar="TICKET:TASA",
                    help="escalones como ticket:tasa_de_conversion, ej: "
                         "50000:1 150000:0.15 400000:0.04. Sin ':tasa' se asume 1.0, "
                         "que casi nunca es cierto fuera del primer escalon.")
    ap.add_argument("--breakeven", action="store_true",
                    help="calcular el CAC maximo tolerable en vez de evaluar uno")
    args = ap.parse_args()

    if args.breakeven:
        breakeven(args.ticket, args.plataforma, args.reembolsos, args.impuestos, args.dolar)
        return

    if args.cac is None:
        sys.exit("Falta --cac (o usa --breakeven para ver el CAC maximo tolerable).")

    escalera = None
    if args.escalera:
        escalera = []
        for item in args.escalera:
            if ":" in item:
                t, c = item.split(":", 1)
                escalera.append((float(t), float(c)))
            else:
                escalera.append((float(item), 1.0))
        optimistas = [t for t, c in escalera[1:] if c >= 1.0]
        if optimistas:
            print("\n  [!] Hay escalones con 100% de conversion. Eso no pasa en la vida real:")
            print("      pasa tasas realistas (ej. 150000:0.15) o el LTV sale inflado.")

    r = calcular(args.ticket, args.cac, args.plataforma, args.reembolsos,
                 args.impuestos, args.dolar, escalera)
    imprimir(r, args.reembolsos)

    if not args.escalera:
        print("  Sugerencia: corre de nuevo con --escalera para ver el efecto del")
        print("  back-end. Un eprod de un solo SKU casi nunca cierra solo.")
        print()


if __name__ == "__main__":
    main()
