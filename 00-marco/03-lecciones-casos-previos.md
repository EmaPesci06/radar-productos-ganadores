# Lecciones de casos previos

Lo que ya nos pasó. Cada línea de acá es un criterio que ganamos pagando.

> **Nota de alcance.** Este archivo está armado con el caso real documentado en la
> skill `importacion-alibaba-ar` (primera importación de la academia, sep-oct 2026)
> y con la lógica operativa del `radar-adlibrary-ar`. **No incluye los casos de la
> carpeta `Ecommerce Curso`**, que no se pudo leer desde esta sesión (ver `GAPS.md`).
> Cuando esos casos entren, este archivo es donde van.

---

## Caso 1 — Primera importación real (bijouterie, sep-oct 2026)

**Pedido:** 2 modelos de collar de acero inoxidable, 100 unidades cada uno, con cajita
individual. Courier DHL, DAP.

| Concepto | USD |
|---|---|
| Collar modelo 1: 100 × 1,38 | 138 |
| Collar modelo 2: 100 × 1,00 | 100 |
| Cajitas: 200 × 0,35 | 70 |
| **FOB** | **308** |
| Flete DHL (DAP) | 170 |
| **Orden de Alibaba** | **478** |
| Cobrado con DolarApp (+5% del medio de pago) | **~503** |

**Impuestos reales pagados a DHL** (courier comercial, sin franquicia):

| Concepto | ARS |
|---|---|
| Valor en aduana | 496.377 (~USD 327 al dólar ~$1.520 — **menos** que lo pagado) |
| Derecho (35%, bijouterie) | 173.732 |
| Estadística (3%) | 14.894 |
| Honorarios DHL (fijo) | 22.868 |
| IVA (21% sobre valor + derecho + estadística + honorarios) | 148.654 |
| **Total a DHL** | **360.148** (~USD 237) |

**Resultado:**

| | Con cajita (real) | Sin cajita (estimado) |
|---|---|---|
| Costo total | USD 740 | ~USD 516 |
| Costo por collar | **USD 3,70** | ~USD 2,58 |
| Multiplicador sobre Alibaba (prom. USD 1,19) | **×3,1** | ×2,2 |

Desglose por collar con cajita: producto 1,19 + flete 0,85 + cajita 0,35 + recargo de
pago 0,13 + impuestos y honorarios 1,18 = **USD 3,70**.

---

## Las 13 lecciones, convertidas en criterio

| # | Qué pasó | Criterio que queda |
|---|---|---|
| 1 | El packaging llevó el flete de USD 75 → 170 y pagó impuestos. La cajita costó ×3 su precio de lista (USD 1,10 por unidad). | **Pedir siempre flete con y sin packaging** y comparar contra comprarlo acá. |
| 2 | USD 1,19 de Alibaba → USD 3,70 puesto. | En productos baratos por courier, **calcular ×3**. Nunca usar el precio de Alibaba en la tabla de markup. |
| 3 | Orden de USD 478, cobrados USD 503. | **Sumar ~5%** por el medio de pago. |
| 4 | Pagó derecho completo con valor declarado < USD 400. | Con **100+ unidades iguales, asumir courier comercial**: no hay franquicia. |
| 5 | Bijouterie paga 35% de derecho — casi la mitad de los impuestos. | **Buscar el derecho de la posición arancelaria antes** de decidir el producto. No es un detalle, es un eje de decisión. |
| 6 | Dijeron 3 días, la orden decía 10, salió a los 6. | **Confiar en la orden de Alibaba, no en el chat.** |
| 7 | La proforma vino con CUIT en campo "CNPJ" (Brasil), campos vacíos, cajitas con el código arancelario del producto, total mezclado. | Checklist de proforma campo por campo **antes de pagar**. |
| 8 | El tracking llegó una semana después del pago, y solo tras reclamar. | **Pedir fecha concreta y reclamar al día siguiente.** |
| 9 | Negociar consiguió USD 10 de descuento, armado gratis y caja más barata. | **Preguntar siempre por algo más económico.** Funciona. |
| 10 | Mencionar 30 mil seguidores consiguió muestras gratis. | **Mostrar volumen al inicio del contacto.** |
| 11 | El primer modelo que ofrecieron no era el pedido. | **Comparar siempre contra la foto de referencia.** Los proveedores ofrecen "algo parecido". |
| 12 | Envío retenido 2 días por no pagar los impuestos al toque. | **Tener la plata lista** y pagar el mismo día del aviso. |
| 13 | Se pagó 1,7 kg de "aire" (volumétrico 11,48 vs real 9,8). | Chequear **peso volumétrico = L×A×H/5.000** antes de cerrar el packaging. |

---

## Criterio operativo que sale del caso

**Antes de enamorarse de un producto, resolver estas cuatro en este orden:**

1. ¿Está en la lista de permitidos? (si no → muere acá, ver `02-costos/reglas-y-exclusiones.md`)
2. ¿Cuál es el derecho de importación de su posición arancelaria? (35% vs 20% cambia todo)
3. ¿Cuánto pesa y cuánto vuela? (volumétrico vs real)
4. ¿Cuál es el costo puesto en AR, no el de Alibaba? (`02-costos/costo-puesto-ar.py`)

Un producto que falla la 1 no merece research. Un producto que falla la 4 no merece
un Doc A.

---

## Lecciones del radar (operativas, no de producto)

Del `radar-adlibrary-ar`, cosas que arruinan un relevamiento si no se saben:

| Error | Consecuencia | Qué hacer |
|---|---|---|
| Clickear el CTA de un anuncio de la competencia | Le cobrás el clic al competidor y ensuciás sus datos | El destino real está en el `href` del DOM (`l.facebook.com/l.php?u=`). Se lee, se decodifica, se navega escribiendo la URL. |
| Asumir el orden del ranking | Todo el análisis queda mal ordenado | **Verificar en cada página** que esté en "Impresiones: de más a menos" |
| No scrollear antes de extraer | Los `<video>` no están en el DOM: todo sale como "imagen" y los destinos vacíos | Scroll 10 ticks → 3s → 10 ticks → 4s |
| Medir foco sobre 5 anuncios | Muestra chica, conclusión falsa | Medir foco sobre **20-30** anuncios |
| Leer el dominio en mayúsculas de la tarjeta como destino | Dos ads que muestran `MARCA.COM` pueden ir a productos distintos | Usar el `href` real |
| Confiar en el precio que promete el anuncio | El creativo miente más que el checkout | Precios de la **landing real** |
| Contar páginas en vez de marcas | Una marca con una página por producto parece dispersa cuando está enfocada | Mirar el **dominio**, no la página |
| Benchmarks de precio en ARS sin fecha | Con la inflación, un benchmark vence en semanas | **Anotar la fecha de la corrida** junto a toda tabla de precios |
