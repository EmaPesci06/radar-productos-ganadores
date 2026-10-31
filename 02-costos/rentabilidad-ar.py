#!/usr/bin/env python3
"""
Rentabilidad real por venta en Argentina — CPA y ROAS de breakeven.

Replica la logica de la Calculadora de costos AcademAI (M2-12) con los costos
reales del curso. Es el numero que gobierna la decision: el scorecard dice que
testear, esto dice si el precio cierra.

Variables del curso (M2-12, oct 2026 — verificar antes de decidir):
    fulfillment  $1.200-1.500 por pedido
    envio        ~$7.000 por pedido
    CPA objetivo ~$15.000 (unos USD 10)
    comisiones   Tiendanube/Shopify 1% + comision de cuotas, mas Mercado Pago
    IIBB         3% para inscriptos en ARCA

Uso:
    # Una unidad
    python3 02-costos/rentabilidad-ar.py --precio 49900 --costo 12000

    # Con bundles (el precio por unidad BAJA al subir la cantidad)
    python3 02-costos/rentabilidad-ar.py --costo 12000 \
        --bundle 1:49900 --bundle 2:84900 --bundle 3:109900

    # Ebook: sin envio ni fulfillment, con order bump
    python3 02-costos/rentabilidad-ar.py --precio 19900 --costo 0 \
        --digital --bump 9900 --bump-take 20

    # Monotributo (sin IIBB)
    python3 02-costos/rentabilidad-ar.py --precio 49900 --costo 12000 --monotributo
"""

import argparse
import sys

# --- Costos de referencia del curso (M2-12), oct 2026 ---
FULFILLMENT = 1_350.0       # promedio del rango 1.200-1.500
ENVIO = 7_000.0
CPA_OBJETIVO = 15_000.0
COM_PLATAFORMA = 0.01       # Tiendanube / Shopify
COM_PASARELA = 0.0599       # Mercado Pago, aprox
COM_CUOTAS = 0.0            # se suma si se ofrecen cuotas sin interes
IIBB = 0.03                 # solo inscriptos en ARCA

# Pisos de realidad en Meta AR (del vault): por debajo de esto no se compra trafico.
CPA_PISO_COMPRABLE = 10_000.0
ROAS_SANO = 2.5
VENTAS_MINIMAS_TEST = 5
USD_TEST_FISICO = 100
USD_TEST_DIGITAL = 50


def unit_economics(precio, costo_unitario, unidades, digital, monotributo,
                   com_cuotas, fulfillment, envio):
    """Rentabilidad de UNA venta (que puede incluir N unidades)."""
    costo_producto = costo_unitario * unidades
    log = 0.0 if digital else (fulfillment + envio)

    com = precio * (COM_PLATAFORMA + COM_PASARELA + com_cuotas)
    iibb = 0.0 if monotributo else precio * IIBB

    # Margen de contribucion ANTES de publicidad. Esto es el CPA de breakeven:
    # lo maximo que se puede pagar por una venta sin perder plata.
    contribucion = precio - costo_producto - log - com - iibb

    return {
        "precio": precio, "unidades": unidades,
        "precio_unidad": precio / unidades,
        "costo_producto": costo_producto,
        "logistica": log,
        "comisiones": com,
        "iibb": iibb,
        "cpa_breakeven": contribucion,
        "roas_breakeven": precio / contribucion if contribucion > 0 else float("inf"),
        "margen_sobre_venta": contribucion / precio if precio else 0,
    }


def con_cpa(e, cpa):
    """Resultado neto si la venta cuesta `cpa` de publicidad."""
    neto = e["cpa_breakeven"] - cpa
    return {
        "cpa": cpa,
        "neto": neto,
        "margen_neto": neto / e["precio"] if e["precio"] else 0,
        "roas_real": e["precio"] / cpa if cpa else float("inf"),
    }


def imprimir(e, cpa_objetivo, digital):
    print()
    print("=" * 74)
    etiqueta = f"PACK x{e['unidades']}" if e["unidades"] > 1 else "UNIDAD SUELTA"
    print(f"{etiqueta}  —  precio ${e['precio']:,.0f}"
          + (f"  (${e['precio_unidad']:,.0f} por unidad)" if e["unidades"] > 1 else ""))
    print("=" * 74)
    print(f"  Precio de venta                   $ {e['precio']:>12,.0f}")
    print(f"  - Costo del producto x{e['unidades']}            $ {e['costo_producto']:>12,.0f}")
    if not digital:
        print(f"  - Envio + fulfillment             $ {e['logistica']:>12,.0f}")
    print(f"  - Comisiones (plataforma+pago)    $ {e['comisiones']:>12,.0f}")
    if e["iibb"]:
        print(f"  - IIBB 3%                         $ {e['iibb']:>12,.0f}")
    print("  " + "-" * 48)
    print(f"  = CPA DE BREAKEVEN                $ {e['cpa_breakeven']:>12,.0f}")
    print(f"    (lo maximo que podes pagar por una venta sin perder plata)")
    print()
    print(f"  ROAS de breakeven                   {e['roas_breakeven']:>10.2f}x")
    print(f"  Margen sobre venta (pre-ads)        {e['margen_sobre_venta']*100:>9.1f}%")

    # Semaforo contra el piso de realidad de Meta AR
    be = e["cpa_breakeven"]
    print()
    if be <= 0:
        print("  \033[91mPIERDE PLATA ANTES DE PAUTAR.\033[0m El precio no cubre ni los costos fijos.")
    elif be < CPA_PISO_COMPRABLE:
        print(f"  \033[91mCPA breakeven ${be:,.0f} < ${CPA_PISO_COMPRABLE:,.0f}: NO SE PUEDE COMPRAR TRAFICO\033[0m")
        print("  a ese precio en Meta AR. Es el gate que mato al antifaz suelto ($7.353).")
        print("  Subir el precio, armar pack, o descartar.")
    elif be < CPA_OBJETIVO:
        print(f"  \033[93mCPA breakeven ${be:,.0f} por debajo del CPA objetivo del curso (${CPA_OBJETIVO:,.0f}).\033[0m")
        print("  Cierra, pero sin colchon: cualquier suba del CPA te pone en rojo.")
    else:
        print(f"  \033[92mCPA breakeven ${be:,.0f}, por encima del objetivo de ${CPA_OBJETIVO:,.0f}.\033[0m Hay aire.")

    if be > 0:
        r = con_cpa(e, cpa_objetivo)
        print()
        print(f"  Con un CPA real de ${cpa_objetivo:,.0f}:")
        c = "\033[92m" if r["neto"] > 0 else "\033[91m"
        print(f"    Neto por venta      {c}$ {r['neto']:>10,.0f}\033[0m   ({r['margen_neto']*100:.1f}% sobre venta)")
        print(f"    ROAS real             {r['roas_real']:>10.2f}x" +
              ("  OK" if r["roas_real"] >= ROAS_SANO else f"  (por debajo de {ROAS_SANO}x)"))
    print()


def imprimir_test(precio, digital, dolar):
    usd = USD_TEST_DIGITAL if digital else USD_TEST_FISICO
    presupuesto = usd * dolar
    print("=" * 74)
    print("REGLA DE CORTE DEL TEST (disciplina de capital del vault)")
    print("=" * 74)
    print(f"  Presupuesto de test       USD {usd}  (~$ {presupuesto:,.0f})")
    print(f"  GO si salen               >= {VENTAS_MINIMAS_TEST} ventas")
    print(f"  CPA implicito en el corte $ {presupuesto/VENTAS_MINIMAS_TEST:,.0f}")
    print(f"  Facturacion del test      $ {precio*VENTAS_MINIMAS_TEST:,.0f} con {VENTAS_MINIMAS_TEST} ventas")
    print(f"  ROAS del test             {precio*VENTAS_MINIMAS_TEST/presupuesto:.2f}x")
    print()
    if digital:
        print("  STOP: < 3 ventas con USD 50 -> cambiar hook/angulo.")
        print("        Dos giros sin mejora -> pasar al siguiente ebook.")
    else:
        print("  STOP: si el CTR del video es < 1,2%, rehacer los primeros 3 segundos.")
    print()


def main():
    ap = argparse.ArgumentParser(description="Rentabilidad real por venta en AR")
    ap.add_argument("--precio", type=float, help="precio de venta en ARS (1 unidad)")
    ap.add_argument("--costo", type=float, required=True, help="costo por unidad puesto en ARS")
    ap.add_argument("--bundle", action="append", default=[], metavar="N:PRECIO",
                    help="pack de N unidades a PRECIO. Repetible: --bundle 2:84900")
    ap.add_argument("--digital", action="store_true", help="sin envio ni fulfillment")
    ap.add_argument("--monotributo", action="store_true", help="sin IIBB")
    ap.add_argument("--cuotas", type=float, default=0.0,
                    help="%% extra de comision por cuotas sin interes (ej 8)")
    ap.add_argument("--fulfillment", type=float, default=FULFILLMENT)
    ap.add_argument("--envio", type=float, default=ENVIO)
    ap.add_argument("--cpa", type=float, default=CPA_OBJETIVO, help="CPA real a evaluar")
    ap.add_argument("--bump", type=float, default=None, help="precio del order bump")
    ap.add_argument("--bump-take", type=float, default=20.0, help="%% de take rate del bump")
    ap.add_argument("--dolar", type=float, default=1560.0, help="ARS por USD")
    args = ap.parse_args()

    if not args.precio and not args.bundle:
        sys.exit("Pasa --precio o al menos un --bundle N:PRECIO")

    packs = []
    if args.precio:
        packs.append((1, args.precio))
    for b in args.bundle:
        try:
            n, p = b.split(":")
            packs.append((int(n), float(p)))
        except ValueError:
            sys.exit(f"--bundle mal formado: '{b}'. Se espera N:PRECIO, ej 2:84900")
    packs.sort()

    print()
    print("#" * 74)
    print(f"# Costo por unidad: ${args.costo:,.0f}" +
          ("  |  DIGITAL (sin envio ni fulfillment)" if args.digital else
           f"  |  envio ${args.envio:,.0f} + fulfillment ${args.fulfillment:,.0f}"))
    print(f"# Condicion: {'Monotributo (sin IIBB)' if args.monotributo else 'Responsable Inscripto (IIBB 3%)'}"
          + (f"  |  cuotas +{args.cuotas:.0f}%" if args.cuotas else ""))
    print("#" * 74)

    evaluados = []
    for n, p in packs:
        e = unit_economics(p, args.costo, n, args.digital, args.monotributo,
                           args.cuotas / 100.0, args.fulfillment, args.envio)
        imprimir(e, args.cpa, args.digital)
        evaluados.append(e)

    if len(evaluados) > 1:
        print("=" * 74)
        print("COMPARATIVA DE PACKS")
        print("=" * 74)
        print(f"{'Pack':<8} {'Precio':>11} {'$/unidad':>11} {'CPA breakeven':>15} {'Margen':>9}")
        print("-" * 74)
        for e in evaluados:
            print(f"x{e['unidades']:<7} {e['precio']:>11,.0f} {e['precio_unidad']:>11,.0f} "
                  f"{e['cpa_breakeven']:>15,.0f} {e['margen_sobre_venta']*100:>8.1f}%")
        print("-" * 74)
        mejor = max(evaluados, key=lambda e: e["margen_sobre_venta"])
        print(f"\n  Mejor margen: pack x{mejor['unidades']} ({mejor['margen_sobre_venta']*100:.1f}%)")
        print("  Regla del curso (M2-12): el precio por unidad BAJA al subir la cantidad")
        print("  y aun asi el margen SUBE, porque los costos fijos por pedido")
        print(f"  (envio + fulfillment + CPA) se reparten entre mas unidades.")
        print()

    if args.bump:
        e = evaluados[0]
        take = args.bump_take / 100.0
        # El bump no suma envio ni fulfillment: va en el mismo pedido.
        com_bump = args.bump * (COM_PLATAFORMA + COM_PASARELA)
        iibb_bump = 0.0 if args.monotributo else args.bump * IIBB
        neto_bump = args.bump - com_bump - iibb_bump
        aporte = neto_bump * take
        print("=" * 74)
        print(f"ORDER BUMP  —  ${args.bump:,.0f} con take rate del {args.bump_take:.0f}%")
        print("=" * 74)
        print(f"  Neto del bump cuando se vende     $ {neto_bump:>12,.0f}")
        print(f"  Aporte promedio por venta         $ {aporte:>12,.0f}")
        print(f"  CPA breakeven SIN bump            $ {e['cpa_breakeven']:>12,.0f}")
        print(f"  CPA breakeven CON bump            $ {e['cpa_breakeven']+aporte:>12,.0f}")
        print(f"  Mejora                            $ {aporte:>12,.0f}"
              f"   ({aporte/e['cpa_breakeven']*100:.0f}% mas de CPA tolerable)")
        print()
        if args.bump_take < 20:
            print("  El vault pide take rate del order bump >= 20% para dar GO a un ebook.")
            print()

    imprimir_test(packs[0][1], args.digital, args.dolar)


if __name__ == "__main__":
    main()
