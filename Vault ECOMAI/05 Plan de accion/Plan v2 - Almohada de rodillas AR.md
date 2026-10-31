---
tags: [ecomai, plan-de-accion, producto-fisico]
fecha: 2026-09-23
---
# Plan v2: producto físico no químico, importable o local

> [!abstract] Decisión
> **Producto:** almohada de rodillas ergonómica para dormir de costado (espuma viscoelástica, con correa y funda lavable).
> **Nicho:** Salud y bienestar → **Descanso ortopédico: alivio de ciática y dolor lumbar nocturno**. No se cruza con los nichos que ya usó la tienda (cocina y mascotas/gatos).
> **Por qué:**
> - Es el puntaje más alto de Jev entre 12 productos físicos (64,6).
> - Tiene el creativo más longevo de la búsqueda: Revoget lleva **509 días al aire** con 231 anuncios.
> - En Meta Argentina está **🟢 libre**: "almohada para rodillas" tiene ~90 resultados y ninguno es del producto.
> - La demanda local está probada: en MELI hay publicaciones con **+1.000 vendidos**.
> - Se consigue **local** (fábricas de espuma) **o en Alibaba** (USD 3-7, MOQ desde 10 unidades).

Datos relevados el 23/09/2026. Los precios en ARS vencen rápido.

---

## 1. Búsqueda en Gethookd con los filtros del curso

**Filtros aplicados** (tal cual el vault):

| Filtro | Valor | Fuente |
|---|---|---|
| Performance score | Winning + Optimized ("performance validado") | [[M2-02 Búsqueda con herramienta espía (recomendado)\|M2-02]] |
| Run time | 30 días o más | M2-02 y [[M2-08 Elegir creativos ganadores con los filtros de Gethookd\|M2-08]] |
| Brand active ads | **200 a 500** (con más de 500 suelen ser multiproducto) | M2-02 |
| Orden | **Most impressions** (no solo el score de performance) | M2-08 |
| Búsqueda | Por **problema**, no por producto | [[M2-03 Validar productos por la calidad del embudo de ventas\|M2-03]] y M2-08 |
| Límite por marca | 1 anuncio (para ver marcas distintas) | — |

**Problemas buscados:** back pain, snoring, neck pain, foot pain, posture, knee pain, dog pulling, baby sleep y car cleaning. En total 139 marcas. Después profundicé por producto: plantar fasciitis, knee pillow, y en español "fascitis plantar" y "almohada".

**Descartes:**
- Todo lo químico: cremas, parches herbales, suplementos, tés.
- Tiendas de catálogo: Mattress Firm, Naaptol y similares.
- Servicios y clínicas.
- Productos caros o electrónicos: sillas, colchones, fajas LED.
- **Mascotas**, aunque los arneses antitirones para perro tienen buena evidencia en Alemania e Italia, porque la tienda ya usó mascotas.

### Mejores anuncios del nicho (para modelar)

| Marca | Anuncios | Días | Formato | Ángulo / hook |
|---|---|---|---|---|
| **Revoget** 🏆 | 231 | **509** | Video 2:29 | *"Most side sleepers are surprised they never knew this…"* (curiosidad + alineación de columna) |
| **Coop Sleep Goods** | 463 | 37 | Imagen | Almohada de rodilla ajustable (relleno a gusto) |
| **Nourial** | 236 | 46 | **Advertorial** | *"If you're a side sleeper, read this"*: la técnica de posicionamiento que usan los kinesiólogos con cada paciente de lumbalgia |
| **SnugWell** (Australia) | 112 | 200 | Imagen | *"Mucha gente con ciática no sabe que su posición al dormir lo empeora"* |
| **Doctor Trigger** | 198 | 65 | Imagen | *"Dormí 120 noches sin riesgo"* (garantía como ángulo) |
| **Fossflakes** (Dinamarca) | 337 | 176 | Video 0:27 | *"La almohada perfecta para entre las piernas"*: ¿te despertás con las rodillas doloridas y la espalda torcida? |

**Oferta del ganador (Revoget):** 1 almohada a USD 34,95 (tachado USD 69,90) · pack doble USD 89,90 · **upsells**: funda extra USD 19,95, faja para ciática USD 39,95, parches y un masajeador. Es exactamente el "ecosistema" del doc-A: el producto héroe más productos para el mismo dolor.

---

## 2. Ranking con Jev (12 productos físicos)

`jev_ranking_fisico.py`: 12 juicios por candidato, incluidos efecto wow, facilidad de importación, margen x5, riesgo de commodity en MELI y si el nicho ya se usó en la tienda.

| # | Candidato | Puntaje | Lectura |
|---|---|---|---|
| 🥇 | **Almohada de rodillas** | **64,6** | Espacio en AR 0,99 · importación 1,0 · promesa rápida 0,93 · sin evidencia LATAM (0,01) |
| 🥈 | Manga de compresión para fascitis plantar | 63,9 | Evidencia LATAM 0,56, pero el dolor en AR ya lo pelean 5 marcas de plantillas |
| 3 | Manija de apoyo para puerta de auto | 61,8 | Muy wow (0,79), pero el dolor es poco masivo (0,38) |
| 4 | Almohada cervical mariposa | 58,8 | Importación difícil por volumen (0,28) y competencia en AR (Zen Sleep, Irishome) |
| 5 | Portabebé de cadera | 58,0 | Poca evidencia |
| 6 | Estirador cervical | 53,9 | Mecanismo débil y commodity |
| 7-12 | Tiras nasales, soporte de celular, paño de microfibra, faja LED, rodillera, corrector de postura | 36-47 | Commodity en MELI o importación complicada |

Resultados completos en `jev_resultados_fisicos.json`.

---

## 3. Radar en Argentina (Ad Library AR + Mercado Libre)

| Búsqueda en Ad Library AR | Resultados | Quiénes |
|---|---|---|
| "almohada para rodillas" | ~90 | **Ninguna marca del producto** (el resto son novelas, apps y cremas) → 🟢 |
| "fascitis plantar" | ~500 | Balox, Nubia, SereniVida AR y PieNube: **plantillas** (dolor tomado) → 🔴 para el dolor de pie |
| "dolor de talón" | ~700 | SereniVida AR (56 anuncios a su ficha), Balox y Nubia → 🔴 |

**Mercado Libre, "almohada para piernas":** 2.294 publicaciones. Varias con **+1.000 vendidos** a **$16.200-$31.499**, y una premium a $49.999 con +100 vendidos. Todas son genéricas, sin marca ni embudo.

**Semáforo: 🟢 ABIERTO en Meta / 🟡 cuidado con el precio.** Hay demanda y no hay ninguna marca de respuesta directa. El riesgo es que el cliente compare con MELI. Mitigación:
1. Diseño diferencial: **con correa** que no se sale de noche y **funda refrigerante de bambú**, lavable. Es el diseño de Revoget.
2. **Advertorial** que vende la solución a la ciática, no "una almohada".
3. Garantía de **30 noches**.
4. Bundle **x2 "para vos y tu pareja"**.

---

## 4. Proveedores

### 🇦🇷 Opción A: local (recomendada para **testear**, como el "nicho laboratorio" de M2-11: poco stock y sin importar)
Pedí cotización mayorista (MOQ, precio por 50 y 100 unidades, si pueden agregar la **correa** y una funda con tu logo, y plazo):

| Proveedor | Qué es | Link |
|---|---|---|
| **Jomaro SRL** | Fábrica de poliuretano integral: almohadas viscoelásticas y **separadores de piernas** | [jomaro.com.ar](https://www.jomaro.com.ar/fabrica/almohadas-viscoelasticas) |
| **Tapitel** (Lanús Oeste) | Fábrica y mayorista de colchones y almohadas | [tapitel.com.ar](https://www.tapitel.com.ar/mayoristas-de-colchones.asp?idioma=colchones-y-tapiceria&es=ALMOHADAS) |
| **SleepTime** | Fabricante de viscoelástica (materia prima Bayer/Basf). Ya vende un combo almohada + separador | [sleeptime.com.ar](https://www.sleeptime.com.ar/productos/combo-almohada-separador-rodillas/) |
| Referencias minoristas (para comparar calidad y precio) | Love & Home, White Salud (marca D.E.M.A.), Ortopedia Centro, Casabella, Ortopedia Libertad | [loveandhome](https://loveandhome.com.ar/productos/separador-rodillas-piernas-almohadon-almohada-viscoelastica/) · [whitesalud](https://whitesalud.com.ar/productos/almohada-para-piernas-rodillas/) · [ortopediacentro](https://www.ortopediacentro.com/productos/almohada-separador-de-piernas-y-rodillas-con-funda-viscoelastica/) · [casabella](https://www.colchonescasabella.com/productos/almohada-casabella-separador-de-rodillas-viscoelastico/) · [ortopedialibertad](https://www.ortopedialibertad.com.ar/productos/almohada-cojin-separador-de-rodillas-anatomico-viscoelastico/) |

También aplicá M2-07: Google Lens sobre la foto de Revoget + la palabra "mayorista", y M2-05: captura a ChatGPT con investigación avanzada pidiendo "mayoristas de almohadas separadoras de rodillas en Argentina".

### 🇨🇳 Opción B: Alibaba (para **escalar** una vez validado)
Criterios de [[M2-10 Explicación de importación con Alibaba|M2-10]]: antigüedad, reseñas, tasa de recompra, MOQ y **Trade Assurance**. Negociar por chat, nunca con "comprar ahora". Pedir envío **DDP** o courier y calcular el costo final (producto + envío + impuestos).

| Proveedor | Años | Recompra | MOQ | Precio (ARS ref.) | Por qué |
|---|---|---|---|---|---|
| **Nanjing Yosta Textile Technology** | 7 | — | 200 | ~9.372 | ⭐ Modelo **con correa** (el diseño de Revoget). 5.0/5 |
| **Jiangsu Yizhen Textile Technology** | 8 | **66%** | 200 | 4.448-5.718 | La tasa de recompra más alta de la búsqueda. Logo personalizado |
| **Nantong Shule Sponge Production** | — (certificado) | — | **99** | 4.511-5.480 | Proveedor verificado. MOQ bajo. Forma de U |
| **Ningbo Kaiweida Household** | **12** | 28% | 1.000 | 6.338-6.671 | El más antiguo, 5.0/5 (MOQ alto: para la etapa de escala) |
| Siyang (proveedor de "almohada para piernas al por mayor") | — | 16% | **10** | 5.718-6.354 | Sirve para una **orden de muestra** chica |

Producto de referencia en Alibaba: IDs 1600084049965 (Yosta, con correa), 1601022372248 (Yizhen), 1601008208373 (Shule) y 1601802261374 (Siyang, MOQ 10).

**Mensaje para el chat del proveedor** (mandalo vos):
> Hi! I'm interested in your memory-foam knee pillow for side sleepers (with elastic strap and removable bamboo cooling cover). Could you share: price for 200 / 500 pcs, custom logo on cover + custom box, vacuum-compressed packing size and weight, sample cost + DDP shipping to Buenos Aires, Argentina, and lead time? We'll pay through Trade Assurance. Thanks!

**Plan de abastecimiento:** testear con **stock local** (50-100 u), porque llega en días y no hay aduana. Pedir en paralelo **muestras** a Yosta y Yizhen. Si el testeo da el día 1 del árbol de M4-17, pasar a una orden de Alibaba de 200 u para mejorar el margen.

---

## 5. Números (supuesto de trabajo: reemplazar con las cotizaciones)

| Oferta | Precio | Costo prod. (local est.) | Fulfill. + envío (bulto voluminoso) | Comisiones ~11% | **Margen antes de ads = CPA breakeven** |
|---|---|---|---|---|---|
| 1 almohada | **$44.900** (tachado $79.900) | 10.000 | 10.000 | 4.940 | **~$20.000** |
| **2 almohadas "para vos y tu pareja"** (empujado) | **$64.900** | 20.000 | 11.500 | 7.140 | **~$26.300** |
| + Funda extra (order bump) | $9.900 | 2.500 | — | 1.090 | +$6.300 |

- Regla del doc-A: con costo de $10.000-$20.000 el markup es **x5**. $44.900 es x4,5, justo en el borde, así que empujá el pack x2.
- Cuidado: el precio queda **por encima de MELI ($16-31k)**. Lo justifican la correa, la funda, la garantía, el advertorial y el bundle. Si el CTR es bueno pero no hay ventas, el precio es lo primero a revisar ([[M5-05 Métricas del embudo de ventas en Meta Ads|M5-05]]).
- Con la importación de Alibaba el costo baja a ~USD 4-7 más flete e impuestos. Calculalo con la [[Calculadora de costos AcademAI]] ([[M2-12 Aplicación calculadora de costos y rentabilidad|M2-12]]).

---

## 6. Landing (Shopify) y creativos

**Landing:** replicar Revoget con el [[Prompt maestro - Replica de landings en Shopify]] ([[M3-04 Cómo replicar una landing con IA en Shopify|M3-04]]), más un **advertorial** que modele a Nourial (M2-04):
- *"Si dormís de costado, leé esto: la posición que los kinesiólogos usan con cada paciente de lumbalgia"*.
- Estructura: camino fallido (colchón nuevo, pastillas) → mecanismo (la rodilla de arriba tuerce la cadera y la columna toda la noche) → testimonio → oferta.

Aplicá las 5 etapas de [[M3-03 Los cinco pasos para que una landing venda|M3-03]]. Garantía de 30 noches. FAQ arriba: "¿Se sale de noche?" (no, tiene correa) y "¿Se puede lavar?".

**8 creativos (3 fríos, 3 tibios y 2 calientes, según M2-08):**

| # | Temp. | Hook |
|---|---|---|
| 1 | Frío | *"Si te despertás con la cadera dolorida y dormís de costado, tu problema no es el colchón."* |
| 2 | Frío | *"Mirá lo que le pasa a tu columna cuando dormís de costado sin nada entre las rodillas."* (demo con línea de columna, b-roll IA) |
| 3 | Frío | *"Los kinesiólogos hacen esto con cada paciente con ciática. Nadie te lo dice para tu casa."* |
| 4 | Tibio | UGC: *"Dormí tres semanas con esto. Así me levanto ahora."* |
| 5 | Tibio | Versus: *"Almohada común entre las piernas vs. esta: por qué la común se cae a las 2 de la mañana."* |
| 6 | Tibio | Pareja: *"Mi marido me la robó la segunda noche. Ahora tenemos dos."* |
| 7 | Caliente | *"30 noches de prueba: si no te levantás mejor, te devolvemos la plata."* |
| 8 | Caliente | *"Pack x2 para vos y tu pareja, con envío gratis, solo esta semana."* |

Meta Ads: la misma estructura que el plan v1 (CBO infinito de 40-50 USD/día, 10 de 18 anuncios activos el día 1, árbol día a día de [[M5-02 Testeo, estabilización y renovación día a día|M5-02]] y auditoría de 17 errores). Ver [[Plan de accion - Debloat AR]] sección 2-3.

## 7. Riesgo principal
**Que el cliente compare con MELI ($16-31k).** Si el diferencial (correa + funda + garantía + advertorial) no se comunica en los primeros 3 segundos, va a buscar la genérica. Segundo riesgo: flete voluminoso, así que conviene comprimido al vacío. Plan B si falla: la **manga de compresión para fascitis plantar** (#2 de Jev). Es el mismo nicho de "dolor que no te deja dormir", con importación todavía más barata, y en Meta AR el mecanismo de la manga está libre (solo pelean con plantillas).
