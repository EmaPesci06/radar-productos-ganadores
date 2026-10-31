#!/usr/bin/env python3
"""
Estimador de costo de fabricacion local — productos fisicos de descanso.

NO reemplaza una cotizacion. Sirve para lo que se necesita antes de cotizar:
tener un costo con el que calcular el precio de venta, el markup y el CPA
breakeven, y para saber si una cotizacion que llega es razonable o un afano.

Metodo: doble estimacion y bracket.
  1. BOTTOM-UP por insumos (espuma, vellon, tela, confeccion, cierre, etiqueta)
  2. TOP-DOWN desde el precio de retail en MELI (el mayorista de un producto
     terminado ronda el 45-55% del precio al publico)
Si las dos no se cruzan, se dice.

Precios de insumos: relevados por web el 2026-10-31. Con la inflacion argentina
vencen en semanas: estan todos en PRECIOS y se actualizan ahi.

Uso:
    python3 02-costos/estimar-costo-fabricacion.py                      # todos
    python3 02-costos/estimar-costo-fabricacion.py --producto lumbar
    python3 02-costos/estimar-costo-fabricacion.py --producto lumbar --margen-fabricante 35
"""

import argparse
import sys

FECHA_PRECIOS = "2026-10-31"

# --- Precios de insumos en ARS. Rango (bajo, alto). Ver fuentes en el .md ---
PRECIOS = {
    # Espuma viscoelastica, por m3. El rango es enorme a proposito: depende de si
    # el proveedor FABRICA su propia espuma (Dubeflex, Jomaro) o corta planchas
    # compradas. Es el lever mas grande del costo del rodillo.
    "espuma_m3_fabrica":  (450_000, 650_000),    # proveedor que hace su espuma
    "espuma_m3_comprada": (900_000, 1_200_000),  # corta plancha comprada al por mayor
    "espuma_m3_retail":   (1_774_000, 2_650_000),  # plancha al publico en MELI (referencia)

    "vellon_kg":   (6_800, 10_000),   # siliconado nacional, mayorista
    "tela_tusor_m": (5_930, 7_750),   # 100% algodon, 1,50 m de ancho, mayorista
    "tela_micro_m": (3_000, 4_500),   # microfibra / poliester, mas barata
    "cierre_u":     (600, 1_200),
    "etiqueta_u":   (200, 500),
}

# Mano de obra de confeccion por pieza, segun complejidad.
CONFECCION = {
    "simple":   (2_500, 4_500),    # funda tubular con cierre
    "media":    (4_000, 7_000),    # forma con costuras curvas
    "compleja": (7_000, 13_000),   # U de cuerpo entero, forro + funda
}

# Margen del fabricante sobre su costo, por defecto.
MARGEN_FABRICANTE_DEFAULT = 40.0


def rango(clave):
    return PRECIOS[clave]


def cil_m3(largo_cm, diam_cm):
    """Volumen de un cilindro en m3."""
    r = (diam_cm / 2) / 100.0
    return 3.14159 * r * r * (largo_cm / 100.0)


# --- Recetas. Cada item: (etiqueta, (costo_bajo, costo_alto), detalle) ---
def receta_lumbar(espuma="comprada"):
    # Rodillo con forma de hueso: ~55 cm de largo, 13-16 cm de diametro.
    # Se modela como cilindro de 14 cm promedio + 10% por las puntas mas gruesas.
    vol = cil_m3(55, 14) * 1.10
    eb, ea = rango(f"espuma_m3_{espuma}")
    tela_m = 0.65   # circunferencia ~44 cm + costura, largo 55 cm + tapas
    tb, ta = rango("tela_tusor_m")
    cb, ca = CONFECCION["simple"]
    zb, za = rango("cierre_u")
    lb, la = rango("etiqueta_u")
    return [
        (f"Espuma viscoelastica ({vol*1000:.1f} L, fuente: {espuma})", (vol * eb, vol * ea),
         f"{vol:.4f} m3 x ${eb:,.0f}-${ea:,.0f}/m3"),
        ("Tela de la funda (tusor)", (tela_m * tb, tela_m * ta), f"{tela_m} m x ${tb:,.0f}-${ta:,.0f}/m"),
        ("Confeccion de la funda", (cb, ca), "funda tubular con cierre"),
        ("Cierre", (zb, za), ""),
        ("Etiqueta", (lb, la), ""),
    ]


def receta_embarazo_u():
    # U de cuerpo entero, ~130 cm de alto. Relleno de vellon, no espuma.
    vellon_kg = (2.0, 2.8)
    vb, va = rango("vellon_kg")
    tela_m = (3.2, 4.5)   # funda exterior + forro interno
    tb, ta = rango("tela_micro_m")
    cb, ca = CONFECCION["compleja"]
    zb, za = rango("cierre_u")
    lb, la = rango("etiqueta_u")
    return [
        ("Vellon siliconado", (vellon_kg[0] * vb, vellon_kg[1] * va),
         f"{vellon_kg[0]}-{vellon_kg[1]} kg x ${vb:,.0f}-${va:,.0f}/kg"),
        ("Tela (funda + forro)", (tela_m[0] * tb, tela_m[1] * ta),
         f"{tela_m[0]}-{tela_m[1]} m x ${tb:,.0f}-${ta:,.0f}/m"),
        ("Confeccion", (cb, ca), "forma en U, costuras curvas, forro + funda desmontable"),
        ("Cierre regulable", (zb, za), ""),
        ("Etiqueta", (lb, la), ""),
    ]


def receta_brazo_lactancia():
    # Almohadita de brazo (referencia CozyArm): chica, relleno de vellon.
    vellon_kg = (0.35, 0.6)
    vb, va = rango("vellon_kg")
    tela_m = (0.5, 0.8)
    tb, ta = rango("tela_tusor_m")
    cb, ca = CONFECCION["media"]
    lb, la = rango("etiqueta_u")
    return [
        ("Vellon siliconado", (vellon_kg[0] * vb, vellon_kg[1] * va),
         f"{vellon_kg[0]}-{vellon_kg[1]} kg x ${vb:,.0f}-${va:,.0f}/kg"),
        ("Tela", (tela_m[0] * tb, tela_m[1] * ta), f"{tela_m[0]}-{tela_m[1]} m"),
        ("Confeccion", (cb, ca), "forma curva chica"),
        ("Etiqueta", (lb, la), ""),
    ]


def receta_rodillas():
    # Separador de piernas / almohada de rodillas (Marca 1, ya activa).
    vol = cil_m3(25, 15) * 0.75   # forma de reloj de arena, menos volumen que el cilindro
    eb, ea = rango("espuma_m3_comprada")
    tela_m = 0.45
    tb, ta = rango("tela_tusor_m")
    cb, ca = CONFECCION["simple"]
    zb, za = rango("cierre_u")
    lb, la = rango("etiqueta_u")
    return [
        (f"Espuma viscoelastica ({vol*1000:.1f} L)", (vol * eb, vol * ea), f"{vol:.4f} m3"),
        ("Tela de la funda", (tela_m * tb, tela_m * ta), f"{tela_m} m"),
        ("Confeccion", (cb, ca), ""),
        ("Cierre", (zb, za), ""),
        ("Etiqueta", (lb, la), ""),
    ]


PRODUCTOS = {
    "lumbar": {
        "nombre": "Almohada lumbar hueso (ciatica)",
        "receta": receta_lumbar,
        "objetivo_vault": 12_000,
        "precio_venta_plan": 49_900,
        # Anclas de retail en MELI, del relevamiento del vault (30/10/2026)
        "anclas": [("Cilindro viscoelastico Schwartz 48x16", 24_500),
                   ("Almohada ortopedica gel memory foam", 29_999),
                   ("Almohada lumbar MTL viscoelastica", 31_989)],
    },
    "embarazo": {
        "nombre": "Almohada de embarazo en U",
        "receta": receta_embarazo_u,
        "objetivo_vault": 22_000,
        "precio_venta_plan": 79_900,
        "anclas": [("Almohada embarazo MELI, piso", 54_990),
                   ("Almohada embarazo MELI, techo", 95_000)],
    },
    "brazo": {
        "nombre": "Almohadita de brazo para lactancia",
        "receta": receta_brazo_lactancia,
        "objetivo_vault": None,
        "precio_venta_plan": 20_000,   # va dentro del Kit Maternidad de $99.900
        "anclas": [("Almohadon de lactancia AR, tipico", 25_000)],
    },
    "rodillas": {
        "nombre": "Almohada de rodillas / separador (Marca 1)",
        "receta": receta_rodillas,
        "objetivo_vault": None,
        "precio_venta_plan": 34_900,
        "anclas": [("Separador de piernas ciatica MELI", 32_999)],
    },
}

TABLA_MARKUP = [
    (0, 2_000, 10, "x10"),
    (2_000, 5_000, 10, "x10"),
    (5_000, 10_000, 7, "x7"),
    (10_000, 20_000, 5, "x5"),
    (20_000, 35_000, 4, "x4"),
    (35_000, 50_000, 3, "x3"),
]


def markup_de(costo):
    for piso, techo, m, et in TABLA_MARKUP:
        if piso <= costo < techo:
            return m, et
    return 3, "x3 (fuera de tabla por arriba)"


def estimar(clave, margen_fab, espuma):
    p = PRODUCTOS[clave]
    items = p["receta"](espuma) if clave == "lumbar" else p["receta"]()

    sub_b = sum(i[1][0] for i in items)
    sub_a = sum(i[1][1] for i in items)
    # El fabricante vende con margen sobre SU costo.
    cost_b = sub_b * (1 + margen_fab / 100.0)
    cost_a = sub_a * (1 + margen_fab / 100.0)

    # Top-down: el mayorista de un terminado ronda 45-55% del retail.
    td = [(n, v * 0.45, v * 0.55) for n, v in p["anclas"]]

    return items, (sub_b, sub_a), (cost_b, cost_a), td


def imprimir(clave, margen_fab, espuma):
    p = PRODUCTOS[clave]
    items, (sub_b, sub_a), (cost_b, cost_a), td = estimar(clave, margen_fab, espuma)

    print()
    print("=" * 78)
    print(p["nombre"].upper())
    print("=" * 78)
    print("\n--- BOTTOM-UP: insumos + confeccion ---\n")
    print(f"{'Item':<42} {'Bajo':>11} {'Alto':>11}")
    print("-" * 78)
    for nombre, (b, a), detalle in items:
        print(f"{nombre[:41]:<42} {b:>11,.0f} {a:>11,.0f}")
        if detalle:
            print(f"  \033[90m{detalle}\033[0m")
    print("-" * 78)
    print(f"{'Subtotal (costo del fabricante)':<42} {sub_b:>11,.0f} {sub_a:>11,.0f}")
    print(f"{f'+ margen del fabricante ({margen_fab:.0f}%)':<42} "
          f"{cost_b-sub_b:>11,.0f} {cost_a-sub_a:>11,.0f}")
    print("-" * 78)
    print(f"\033[1m{'= COSTO ESTIMADO PARA NOSOTROS':<42} {cost_b:>11,.0f} {cost_a:>11,.0f}\033[0m")

    print("\n--- TOP-DOWN: desde el retail de MELI (mayorista ~45-55%) ---\n")
    print(f"{'Ancla de retail':<42} {'Precio':>11} {'Mayorista estimado':>22}")
    print("-" * 78)
    for nombre, b, a in td:
        print(f"{nombre[:41]:<42} {nombre and '':>0}{b/0.45:>11,.0f}   ${b:,.0f} - ${a:,.0f}")
    td_b = min(x[1] for x in td)
    td_a = max(x[2] for x in td)
    print("-" * 78)
    print(f"{'Rango top-down':<42} {'':>11} {f'${td_b:,.0f} - ${td_a:,.0f}':>22}")

    # Cruce de los dos metodos
    print("\n--- CRUCE ---\n")
    solapan = not (cost_a < td_b or cost_b > td_a)
    if solapan:
        lo = max(cost_b, td_b)
        hi = min(cost_a, td_a)
        print(f"  Los dos metodos se cruzan en \033[1m${lo:,.0f} - ${hi:,.0f}\033[0m.")
        print("  Ese es el rango con el que conviene trabajar.")
        usar_b, usar_a = lo, hi
    else:
        print(f"  \033[93mNO se cruzan.\033[0m Bottom-up: ${cost_b:,.0f}-${cost_a:,.0f}. "
              f"Top-down: ${td_b:,.0f}-${td_a:,.0f}.")
        if cost_b > td_a:
            print("  El bottom-up sale MAS CARO que lo que implica el retail. Dos lecturas:")
            print("  los que venden en MELI compran insumos mas baratos o a mas volumen,")
            print("  o estan vendiendo con margen muy fino. Usar el rango amplio y cotizar.")
        else:
            print("  El bottom-up sale MAS BARATO que el retail. Hay margen de sobra,")
            print("  o el retail esta inflado.")
        usar_b, usar_a = min(cost_b, td_b), max(cost_a, td_a)

    # Contra el objetivo del plan
    obj = p.get("objetivo_vault")
    if obj:
        print(f"\n  Objetivo del plan: \033[1m<= ${obj:,.0f}\033[0m")
        if usar_b > obj:
            print(f"  \033[91mEl piso de la estimacion (${usar_b:,.0f}) ya supera el objetivo.\033[0m")
            print(f"  Diferencia: ${usar_b-obj:,.0f}. Revisar el precio de venta del plan.")
        elif usar_a > obj:
            print(f"  \033[93mAlcanzable solo en el extremo bajo del rango.\033[0m "
                  f"Hay que negociar o subir volumen.")
        else:
            print(f"  \033[92mEl objetivo es alcanzable en todo el rango.\033[0m")

    # Precio de venta
    print("\n--- PRECIO DE VENTA SUGERIDO (tabla de markup del Doc A) ---\n")
    for etiqueta, costo in (("piso del rango", usar_b), ("techo del rango", usar_a)):
        m, et = markup_de(costo)
        print(f"  Costo ${costo:>9,.0f} ({etiqueta:<15}) -> markup {et:<4} -> "
              f"precio minimo \033[1m${costo*m:,.0f}\033[0m")
    plan = p.get("precio_venta_plan")
    if plan:
        m_a, _ = markup_de(usar_a)
        minimo = usar_a * m_a
        print(f"\n  Precio del plan: \033[1m${plan:,.0f}\033[0m")
        if plan < minimo:
            print(f"  \033[91mQueda ${minimo-plan:,.0f} POR DEBAJO del minimo de la tabla "
                  f"(${minimo:,.0f}) en el escenario de costo alto.\033[0m")
            print(f"  Markup real a ese precio: x{plan/usar_a:.1f} contra x{m_a} que pide la tabla.")
        else:
            print(f"  \033[92mPasa la tabla incluso con el costo alto\033[0m "
                  f"(markup x{plan/usar_a:.1f}).")

    print(f"\n  Siguiente paso: python3 02-costos/rentabilidad-ar.py "
          f"--costo {int(usar_a)} --precio {plan or int(usar_a*4)}")
    print()
    return usar_b, usar_a


def main():
    ap = argparse.ArgumentParser(description="Estimador de costo de fabricacion local")
    ap.add_argument("--producto", choices=sorted(PRODUCTOS), help="omitir para todos")
    ap.add_argument("--margen-fabricante", type=float, default=MARGEN_FABRICANTE_DEFAULT,
                    help=f"%% de margen del fabricante sobre su costo (default {MARGEN_FABRICANTE_DEFAULT:.0f})")
    ap.add_argument("--espuma", choices=["fabrica", "comprada", "retail"], default="comprada",
                    help="solo para el rodillo lumbar: si el proveedor hace su espuma o corta plancha comprada")
    args = ap.parse_args()

    print(f"\n{'#'*78}")
    print(f"# Precios de insumos relevados el {FECHA_PRECIOS}. Con la inflacion vencen")
    print(f"# en semanas: actualizar el dict PRECIOS antes de decidir con esto.")
    print(f"# Margen del fabricante asumido: {args.margen_fabricante:.0f}%")
    print(f"{'#'*78}")

    claves = [args.producto] if args.producto else list(PRODUCTOS)
    for c in claves:
        imprimir(c, args.margen_fabricante, args.espuma)


if __name__ == "__main__":
    main()
