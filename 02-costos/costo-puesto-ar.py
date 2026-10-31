#!/usr/bin/env python3
"""
Costo puesto en Argentina — calculadora de importacion por courier.

Formulas validadas contra el desglose real de DHL de la primera importacion
(bijouteria, sep-oct 2026). Ver 00-marco/03-lecciones-casos-previos.md.

TERMINA en el costo por unidad puesto en Argentina. No calcula precio de venta,
margen ni comisiones: eso lo hace el scorecard con la tabla de markup.

Uso:
    # Caso real de referencia (reproduce el numero conocido: USD 3,70/unidad)
    python3 02-costos/costo-puesto-ar.py --caso-real

    # Caso propio
    python3 02-costos/costo-puesto-ar.py \
        --unidades 200 --precio-unitario 1.19 \
        --packaging-precio 0.35 --packaging-unidades 200 \
        --flete 170 --caja 58x30x33 --peso-real 9.8 \
        --derecho 35 --dolar 1520

    # Comparar con y sin packaging, y al doble de cantidad
    python3 02-costos/costo-puesto-ar.py ... --escenarios
"""

import argparse
import math
import sys

# --- Parametros de referencia, oct 2026. VERIFICAR antes de decidir con esto. ---
ESTADISTICA = 0.03
IVA = 0.21
HONORARIOS_COURIER_ARS = 22_900.0     # cargo fijo DHL
RECARGO_MEDIO_PAGO = 0.05             # ~5% (DolarApp/ARQ, caso real)
FRANQUICIA_USD = 400.0
DIVISOR_VOLUMETRICO_COURIER = 5_000
FLETE_REF_USD_KG = 14.8               # caso real DHL China-Argentina

DERECHOS_RUBRO = {
    "bijouteria": 35.0,
    "indumentaria": 20.0,
    "calzado": 20.0,
    "telas": 18.0,
}


def peso_cobrado(peso_real_kg, caja_cm):
    """Se cobra el mayor entre real y volumetrico, redondeado hacia arriba a 0,5 kg."""
    volumetrico = 0.0
    if caja_cm:
        largo, ancho, alto = caja_cm
        volumetrico = (largo * ancho * alto) / DIVISOR_VOLUMETRICO_COURIER
    mayor = max(peso_real_kg or 0.0, volumetrico)
    cobrado = math.ceil(mayor * 2) / 2 if mayor else 0.0
    return cobrado, volumetrico


def impuestos_courier_comercial(valor_aduana_ars, derecho_pct):
    derecho = valor_aduana_ars * (derecho_pct / 100.0)
    estadistica = valor_aduana_ars * ESTADISTICA
    honorarios = HONORARIOS_COURIER_ARS
    base_iva = valor_aduana_ars + derecho + estadistica + honorarios
    iva = base_iva * IVA
    return {
        "derecho": derecho,
        "estadistica": estadistica,
        "honorarios": honorarios,
        "iva": iva,
        "total": derecho + estadistica + honorarios + iva,
    }


def impuestos_courier_personal(fob_usd, valor_aduana_ars, derecho_pct, dolar):
    excedente_usd = max(0.0, fob_usd - FRANQUICIA_USD)
    excedente_ars = excedente_usd * dolar
    derecho = excedente_ars * (derecho_pct / 100.0)
    estadistica = excedente_ars * ESTADISTICA
    honorarios = HONORARIOS_COURIER_ARS
    iva = (valor_aduana_ars + derecho + estadistica) * IVA
    return {
        "derecho": derecho,
        "estadistica": estadistica,
        "honorarios": honorarios,
        "iva": iva,
        "total": derecho + estadistica + honorarios + iva,
    }


def calcular(unidades, precio_unitario, flete_usd, derecho_pct, dolar,
             packaging_precio=0.0, packaging_unidades=0,
             peso_real=0.0, caja=None, via=None, recargo=RECARGO_MEDIO_PAGO):

    fob_producto = unidades * precio_unitario
    fob_packaging = packaging_unidades * packaging_precio
    fob = fob_producto + fob_packaging

    cobrado, volumetrico = peso_cobrado(peso_real, caja)
    flete_estimado = flete_usd is None
    if flete_estimado:
        flete_usd = cobrado * FLETE_REF_USD_KG

    orden_alibaba = fob + flete_usd
    pago_real = orden_alibaba * (1 + recargo)

    # Via: con 100+ unidades iguales se asume courier comercial (sin franquicia).
    if via is None:
        via = "comercial" if unidades >= 100 else "personal"

    # El valor en aduana depende de lo que declare el remitente. Dos escenarios.
    escenarios_aduana = {
        "bajo (FOB)": fob,
        "alto (FOB + flete)": fob + flete_usd,
    }

    resultados = {}
    for nombre, valor_usd in escenarios_aduana.items():
        valor_ars = valor_usd * dolar
        if via == "comercial":
            imp = impuestos_courier_comercial(valor_ars, derecho_pct)
        else:
            imp = impuestos_courier_personal(fob, valor_ars, derecho_pct, dolar)
        imp_usd = imp["total"] / dolar
        total_usd = pago_real + imp_usd
        resultados[nombre] = {
            "valor_aduana_usd": valor_usd,
            "valor_aduana_ars": valor_ars,
            "impuestos_ars": imp,
            "impuestos_usd": imp_usd,
            "total_usd": total_usd,
            "costo_unidad_usd": total_usd / unidades,
            "costo_unidad_ars": (total_usd / unidades) * dolar,
            "multiplicador": (total_usd / unidades) / precio_unitario,
        }

    return {
        "unidades": unidades,
        "precio_unitario": precio_unitario,
        "fob_producto": fob_producto,
        "fob_packaging": fob_packaging,
        "fob": fob,
        "flete": flete_usd,
        "flete_estimado": flete_estimado,
        "orden_alibaba": orden_alibaba,
        "pago_real": pago_real,
        "peso_real": peso_real,
        "peso_volumetrico": volumetrico,
        "peso_cobrado": cobrado,
        "via": via,
        "derecho_pct": derecho_pct,
        "dolar": dolar,
        "escenarios": resultados,
    }


# --- Tabla de markup del Doc A: costo puesto en AR -> markup minimo ---
TABLA_MARKUP = [
    (2_000,  5_000,  10, "$20.000 - $50.000"),
    (5_000,  10_000,  7, "$35.000 - $70.000"),
    (10_000, 20_000,  5, "$50.000 - $100.000"),
    (20_000, 35_000,  4, "$80.000 - $140.000"),
    (35_000, 50_000,  3, "$105.000 - $150.000"),
]


def markup_sugerido(costo_ars):
    for piso, techo, mult, rango in TABLA_MARKUP:
        if piso <= costo_ars < techo:
            return mult, rango
    if costo_ars < 2_000:
        return 10, "fuera de tabla por abajo: usar x10 como piso"
    return 3, "fuera de tabla por arriba: x3 es el piso, revisar si el ticket cierra en AR"


def imprimir(r):
    u = r["unidades"]
    print()
    print("=" * 72)
    print("COSTO PUESTO EN ARGENTINA")
    print("=" * 72)
    print(f"  Unidades                {u}")
    print(f"  Precio unitario         USD {r['precio_unitario']:.2f}")
    print(f"  FOB producto            USD {r['fob_producto']:.2f}")
    if r["fob_packaging"]:
        print(f"  FOB packaging           USD {r['fob_packaging']:.2f}")
    print(f"  FOB total               USD {r['fob']:.2f}")
    est = "  [ESTIMADO]" if r["flete_estimado"] else ""
    print(f"  Flete                   USD {r['flete']:.2f}{est}")
    print(f"  Orden Alibaba           USD {r['orden_alibaba']:.2f}")
    print(f"  Pago real (+{RECARGO_MEDIO_PAGO*100:.0f}% medio de pago)  USD {r['pago_real']:.2f}")
    print()
    if r["peso_cobrado"]:
        aire = r["peso_cobrado"] - (r["peso_real"] or 0)
        print(f"  Peso real               {r['peso_real']:.2f} kg")
        print(f"  Peso volumetrico        {r['peso_volumetrico']:.2f} kg  (L*A*H/5000)")
        print(f"  Peso cobrado            {r['peso_cobrado']:.2f} kg")
        if aire > 0.2:
            print(f"  >> Pagas {aire:.2f} kg de AIRE. Revisar packaging o armado de la caja.")
        print()
    print(f"  Via                     courier {r['via']}" +
          ("  (100+ unidades iguales: sin franquicia)" if r["via"] == "comercial" else ""))
    print(f"  Derecho                 {r['derecho_pct']:.0f}%")
    print(f"  Dolar                   ARS {r['dolar']:,.0f}")
    print()
    print("-" * 72)
    print(f"{'Escenario de valor en aduana':<26} {'Impuestos':>12} {'Total':>11} {'USD/u':>8} {'x Alibaba':>10}")
    print("-" * 72)
    for nombre, e in r["escenarios"].items():
        print(f"{nombre:<26} {e['impuestos_usd']:>11.0f}  {e['total_usd']:>10.0f} "
              f"{e['costo_unidad_usd']:>8.2f} {e['multiplicador']:>9.1f}x")
    print("-" * 72)

    bajo = min(e["costo_unidad_usd"] for e in r["escenarios"].values())
    alto = max(e["costo_unidad_usd"] for e in r["escenarios"].values())
    bajo_ars = bajo * r["dolar"]
    alto_ars = alto * r["dolar"]
    print()
    print(f"  COSTO POR UNIDAD:  USD {bajo:.2f} - {alto:.2f}")
    print(f"                     ARS {bajo_ars:,.0f} - {alto_ars:,.0f}")
    print()
    mult_b, rango_b = markup_sugerido(bajo_ars)
    mult_a, rango_a = markup_sugerido(alto_ars)
    print("  TABLA DE MARKUP (Doc A), aplicada al costo PUESTO:")
    print(f"    Escenario bajo:  markup minimo x{mult_b}  ->  precio {rango_b}")
    if (mult_a, rango_a) != (mult_b, rango_b):
        print(f"    Escenario alto:  markup minimo x{mult_a}  ->  precio {rango_a}")
    print(f"    Precio piso (x{mult_a} sobre el costo alto): ARS {alto_ars*mult_a:,.0f}")
    print()
    print("  >> Comparar ese precio piso contra lo que se vende HOY en MELI AR.")
    print("     Si queda muy por encima del mercado, es NO-GO de margen.")
    print()
    print("  Que puede mover el resultado: el valor que declare el remitente,")
    print("  el tipo de cambio del dia de nacionalizacion, y la posicion arancelaria.")
    print()


def main():
    ap = argparse.ArgumentParser(description="Costo puesto en Argentina (courier)")
    ap.add_argument("--caso-real", action="store_true",
                    help="reproduce el caso real documentado (bijouteria, oct 2026)")
    ap.add_argument("--unidades", type=int)
    ap.add_argument("--precio-unitario", type=float, help="USD por unidad (FOB)")
    ap.add_argument("--packaging-precio", type=float, default=0.0)
    ap.add_argument("--packaging-unidades", type=int, default=0)
    ap.add_argument("--flete", type=float, default=None,
                    help="USD cotizados. Si se omite, se estima a USD %.1f/kg" % FLETE_REF_USD_KG)
    ap.add_argument("--peso-real", type=float, default=0.0, help="kg del envio completo")
    ap.add_argument("--caja", type=str, default=None, help="LxAxH en cm, ej 58x30x33")
    ap.add_argument("--derecho", type=float, default=None, help="%% de derecho de importacion")
    ap.add_argument("--rubro", choices=sorted(DERECHOS_RUBRO), default=None)
    ap.add_argument("--dolar", type=float, default=1520.0, help="ARS por USD, oficial del dia")
    ap.add_argument("--via", choices=["comercial", "personal"], default=None)
    ap.add_argument("--escenarios", action="store_true",
                    help="comparar sin packaging y al doble de cantidad")
    args = ap.parse_args()

    if args.caso_real:
        print("\n### CASO REAL DE REFERENCIA — bijouteria, sep-oct 2026")
        print("### Esperado: ~USD 3,70 por collar con cajita (x3,1 sobre Alibaba)")
        r = calcular(unidades=200, precio_unitario=1.19, flete_usd=170.0,
                     derecho_pct=35.0, dolar=1520.0,
                     packaging_precio=0.35, packaging_unidades=200,
                     peso_real=9.8, caja=(58, 30, 33), via="comercial")
        imprimir(r)
        print("### Sin cajitas (flete cotizado era USD 75) — esperado ~USD 2,58")
        r2 = calcular(unidades=200, precio_unitario=1.19, flete_usd=75.0,
                      derecho_pct=35.0, dolar=1520.0,
                      peso_real=8.0, caja=(50, 28, 25), via="comercial")
        imprimir(r2)
        return

    faltan = [n for n, v in (("--unidades", args.unidades),
                             ("--precio-unitario", args.precio_unitario)) if v is None]
    if faltan:
        sys.exit(f"Faltan argumentos: {', '.join(faltan)}. Usa --caso-real para ver un ejemplo.")

    derecho = args.derecho
    if derecho is None and args.rubro:
        derecho = DERECHOS_RUBRO[args.rubro]
    if derecho is None:
        print("\n[!] Sin --derecho ni --rubro: se muestra el RANGO 20%% - 35%%,")
        print("    como indica la regla cuando no se encuentra la posicion arancelaria.\n")
        for d in (20.0, 35.0):
            print(f"\n{'#'*72}\n### DERECHO {d:.0f}%\n{'#'*72}")
            caja = tuple(int(x) for x in args.caja.lower().split("x")) if args.caja else None
            imprimir(calcular(args.unidades, args.precio_unitario, args.flete, d, args.dolar,
                              args.packaging_precio, args.packaging_unidades,
                              args.peso_real, caja, args.via))
        return

    caja = tuple(int(x) for x in args.caja.lower().split("x")) if args.caja else None
    base = dict(unidades=args.unidades, precio_unitario=args.precio_unitario,
                flete_usd=args.flete, derecho_pct=derecho, dolar=args.dolar,
                packaging_precio=args.packaging_precio,
                packaging_unidades=args.packaging_unidades,
                peso_real=args.peso_real, caja=caja, via=args.via)
    imprimir(calcular(**base))

    if args.escenarios:
        if args.packaging_unidades:
            print(f"\n{'#'*72}\n### ESCENARIO: SIN PACKAGING\n{'#'*72}")
            sin_pack = dict(base, packaging_precio=0.0, packaging_unidades=0, flete_usd=None)
            print("    (flete re-estimado: pedir al proveedor la cotizacion sin packaging)")
            imprimir(calcular(**sin_pack))
        print(f"\n{'#'*72}\n### ESCENARIO: DOBLE DE CANTIDAD (dilucion del flete)\n{'#'*72}")
        doble = dict(base, unidades=args.unidades * 2,
                     packaging_unidades=args.packaging_unidades * 2, flete_usd=None,
                     peso_real=(args.peso_real or 0) * 2,
                     caja=None)
        imprimir(calcular(**doble))


if __name__ == "__main__":
    main()
