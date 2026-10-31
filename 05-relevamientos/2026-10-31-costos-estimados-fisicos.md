# Costos estimados de fabricación local y precio de venta

| | |
|---|---|
| **Fecha** | 2026-10-31 |
| **Para qué** | Tener un costo con el que calcular precio de venta, markup y CPA breakeven **antes** de cotizar |
| **Herramienta** | `02-costos/estimar-costo-fabricacion.py` + `02-costos/rentabilidad-ar.py` |
| **Qué NO es** | Una cotización. Es una estimación para ordenar el pricing y para detectar si una cotización que llega es razonable |

---

## El método

Doble estimación, y se cruzan:

1. **Bottom-up** por insumos: espuma o vellón + tela + confección + cierre + etiqueta,
   más el margen del fabricante sobre su costo (40% por defecto).
2. **Top-down** desde el precio de retail en MELI: el mayorista de un producto terminado
   ronda el **45-55%** del precio al público.

Donde los dos rangos se cruzan, ese es el rango de trabajo. Si no se cruzan, se dice y
se usa el rango amplio.

### Precios de insumos relevados (2026-10-31)

| Insumo | Rango mayorista | Nota |
|---|---|---|
| Espuma viscoelástica, **proveedor que la fabrica** | $450.000 – $650.000 / m³ | Estimado. Dubeflex y Jomaro hacen su propia espuma |
| Espuma viscoelástica, **plancha comprada** | $900.000 – $1.200.000 / m³ | Mayorista |
| Espuma viscoelástica, **retail MELI** | $1.774.000 – $2.650.000 / m³ | Plancha 140×190×6 a $283.100; 100×70×3 a $55.670 |
| Vellón siliconado | $6.800 – $10.000 / kg | Roma Blanquería $6.800/kg · Mercería del Litoral $9.971/kg · bolsón 5 kg $32.750 |
| Tela tusor 100% algodón, 1,50 m | $5.930 – $7.750 / m | Telas.com.ar desde $5.930 a 100 m · Trapitos $6.200 mayorista |
| Tela microfibra / poliéster | $3.000 – $4.500 / m | Estimado |
| Cierre | $600 – $1.200 | Estimado |
| Etiqueta | $200 – $500 | Estimado |
| Confección | $2.500 (simple) – $13.000 (U de cuerpo) | Estimado por complejidad |

> ⚠️ Los marcados "estimado" son mi estimación, no un precio relevado. Y **todos vencen
> en semanas** por inflación: están en el dict `PRECIOS` del script, se actualizan ahí.

---

## El hallazgo estructural: la tabla de markup no aplica a fabricación local

Los **cuatro** productos fallan la tabla de markup del Doc A:

| Producto | Costo estimado | Markup que pide la tabla | Precio del plan | Markup real |
|---|---|---|---|---|
| Almohada lumbar hueso | $15.884 – $17.594 | ×5 → $88.000 | $49.900 | **×2,8** |
| Almohada de embarazo U | $43.400 – $52.250 | ×3 → $157.000 | $79.900 | **×1,5** |
| Almohadita de brazo | $13.363 – $13.750 | ×5 → $69.000 | $20.000 | **×1,5** |
| Almohada de rodillas | $14.850 – $18.149 | ×5 → $91.000 | $34.900 | **×1,9** |

Cuatro de cuatro no es casualidad: **es un desajuste estructural.**

La tabla de markup se construyó para **importar**. Ahí el costo base es bajísimo (el
caso real: collar a USD 1,19, puesto en AR USD 3,70 ≈ $5.600), y sobre eso un ×10 da
$56.000, que es un precio de mercado razonable.

Fabricando en Argentina el costo base es 3-4 veces más alto, porque se paga mano de obra
y materiales locales. Pedirle ×5 a un costo de $15.000 da $75.000 — que es **2 a 3 veces
el ancla de MELI** ($24.500 el cilindro Schwartz, $32.999 el separador). A ese precio no
se vende.

**Qué usar en su lugar:** el **CPA de breakeven**, que es lo que dice el propio M2-12
("el CPA breakeven manda"). La tabla de markup sirve para importación; para fabricación
local el filtro es si se puede comprar tráfico.

---

## Los números con el CPA breakeven

Corrido con `rentabilidad-ar.py`, Responsable Inscripto, envío $7.000 + fulfillment $1.350.

| Producto / oferta | Precio | Costo estimado | CPA breakeven | Margen pre-ads | Lectura |
|---|---|---|---|---|---|
| **Lumbar 1u** | $49.900 | $17.594 | **$18.971** | 38,0% | 🟢 sobre el objetivo de $15.000 |
| **Lumbar pack x2** | $84.900 | $35.188 | **$32.880** | 38,7% | 🟢 cómodo |
| **Embarazo 1u** | $79.900 | $52.250 | **$11.318** | 14,2% | 🟡 apenas sobre el piso de $10.000 |
| **Kit Maternidad** | $99.900 | ~$71.000 | **$10.570** | 10,6% | 🟡 al borde |
| **Rodillas 1u** | $34.900 | $18.149 | **$4.914** | 14,1% | 🔴 **bajo el piso comprable** |

### Qué significa cada uno

**🟢 La almohada lumbar sigue cerrando, con menos colchón.** El plan asumía costo
$12.000 y CPA breakeven de $24.565. Con costo $17.594 el breakeven baja a $18.971: el
colchón sobre el CPA objetivo de $15.000 **se reduce de $9.565 a $3.971, un 60% menos**.
Sigue siendo el mejor de la cartera, pero hay menos margen para que el CPA se vaya de
tema. El combo x2 es el que da aire de verdad ($32.880).

**🟡 La almohada de embarazo es mucho más ajustada de lo que supone el plan.** El
objetivo era costo ≤$22.000 y la estimación da **$43.400-$52.250: el doble**. A $79.900
el CPA breakeven queda en $11.318, apenas sobre el piso de $10.000 y muy por debajo del
objetivo de $15.000. El Kit a $99.900 no mejora: $10.570.

Esto es coherente con el ancla de MELI, que va de $54.990 a $95.000 — si el costo
mayorista fuera $22.000, los que venden a $54.990 estarían ganando ×2,5 y el techo de
$95.000 sería un robo. Lo más probable es que el costo real esté en mi rango y que el
mercado se venda con margen fino.

**🔴 La almohada de rodillas no cerraría a $34.900.** CPA breakeven $4.914, por debajo
del piso de ~$10.000 que se puede pagar en Meta AR. Es el mismo gate que mató al antifaz
($7.353).

---

## 🔴 Lo que necesito para saber si el estimador sirve

**La almohada de rodillas ya está lanzada desde el 08/10.** O sea: Emanuel tiene su
**costo real**, y es el único número con el que se puede calibrar todo esto.

| Si el costo real de la almohada de rodillas es… | Entonces |
|---|---|
| **cerca de $15.000-18.000** | El estimador está calibrado, y hay un problema real de pricing en toda la línea: los precios del plan son muy bajos para fabricación local |
| **muy por debajo, tipo $8.000-10.000** | El estimador corre **alto** y hay que recalibrarlo. Probablemente mi margen de fabricante del 40% o los precios de espuma estén sobrestimados. Y entonces los números del plan son correctos |

Con ese dato ajusto el script y vuelvo a correr los cuatro. **Sin él, estas cifras son
una referencia para discutir una cotización, no para fijar precio.**

---

## Cómo usarlo

```bash
# Un producto
python3 02-costos/estimar-costo-fabricacion.py --producto lumbar

# Si el proveedor fabrica su propia espuma (Dubeflex, Jomaro) — baja mucho el costo
python3 02-costos/estimar-costo-fabricacion.py --producto lumbar --espuma fabrica

# Si el fabricante trabaja con otro margen
python3 02-costos/estimar-costo-fabricacion.py --producto lumbar --margen-fabricante 25

# Y después, con el costo que salga:
python3 02-costos/rentabilidad-ar.py --costo 17594 --bundle 1:49900 --bundle 2:84900
```

### El lever más grande del rodillo lumbar

Si el proveedor **compra plancha** de espuma, el bottom-up da $21.751-$31.379 y **no se
cruza** con el top-down ($11.025-$17.594). Si **fabrica su propia espuma**, da
$15.884-$17.594 y sí se cruza.

Traducción práctica: **el costo del rodillo depende casi por completo de que el
proveedor haga su propia espuma.** Por eso Dubeflex y Jomaro son los dos que importan de
la lista de 9 — no por precio de lista, sino por integración vertical. A los que cortan
plancha comprada no vale la pena ni pedirles cotización para este producto.

---

## Fuentes

**Espuma**
- [Espuma viscoelástica por mayor (MELI AR)](https://listado.mercadolibre.com.ar/espuma-viscoelastica-por-mayor) — plancha 140×190×6 a $283.100, 100×70×3 a $55.670

**Vellón siliconado**
- [Roma Blanquería — vellón siliconado por kilo](https://www.romablanqueria.com.ar/productos/vellon-siliconado-por-kilo/) — $6.800/kg, bolsón 5 kg $32.750
- [Mercería del Litoral (mayorista)](https://www.merceriadellitoral.com.ar/productos/merceria-5160/vellon-siliconado-8851/) — $9.971,20/kg con IVA
- [Las Mil Telas](https://www.lasmiltelas.com.ar/producto/138-vellon-siliconado-x-kilo) — $13.300/kg
- [Milagres Textil SRL](https://milagrestextil.com/) — fabricante de vellón, guata y siliconado. Proveedor de materia prima

**Tela**
- [Telas.com.ar — tusor](https://www.telas.com.ar/telas/tusor/) — $6.900/m, $6.690 desde 10 m, $5.930 desde 100 m
- [Trapitos — tusor 100% algodón](https://www.trapitos.com.ar/tipos-de-telas-por-metro/tela-tusor/) — $7.200 menor, $6.200 mayor (+10 m)
- [Todotusor](https://www.todotusor.com.ar/productos/tela-tusor-100-algodon-por-metro-150-m-de-ancho-crudo-natural-tdxe9/) — crudo 1,50 m a $4.950
- [Telas Group (Once)](https://www.telasgroup.ar/telas-por-metro/) — tusor de color $9.000/m

**Anclas de retail**: del relevamiento del vault en
`05 Plan de accion/Proveedores AR - almohada lumbar ciatica.md` (30/10/2026).
