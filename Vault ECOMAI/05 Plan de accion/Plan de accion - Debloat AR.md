---
tags: [ecomai, plan-de-accion]
fecha: 2026-09-23
---
# Plan de acción: producto → landing Shopify → Meta Ads (Argentina)

> [!abstract] Decisión
> **Producto:** cápsulas o gomitas "debloat" (probióticos + enzimas digestivas) para la **hinchazón después de comer**. Es nicho laboratorio y se fabrica en Argentina.
> **Por qué:** es el puntaje más alto de Jev (70,5/100) y tiene la mejor evidencia en el exterior y en LATAM. En Argentina es el único hueco real: el dolor "panza hinchada" está caliente (~1.400 anuncios), pero todos lo atacan con "drenaje linfático". No hay ninguna marca de respuesta directa enfocada en la hinchazón digestiva.
> **Ángulo diferencial:** *"No es grasa ni es retención: es lo que comiste que tu panza no termina de digerir."*

Precios en ARS relevados el 23/09/2026. Con la inflación, vencen en semanas.

---

## 0. Cómo se tomó la decisión (trazabilidad)

| Paso | Herramienta | Regla del vault aplicada | Resultado |
|---|---|---|---|
| 1. Búsqueda | Gethookd (tu cuenta) | [[M2-02 Búsqueda con herramienta espía (recomendado)\|M2-02]] y [[M2-08 Elegir creativos ganadores con los filtros de Gethookd\|M2-08]]: buscar por **problema**, *Most impressions*, runtime ≥30 días y marcas con 100 a 600 anuncios | 176 marcas en 6 problemas: bloating, cortisol, sleep, hair loss, joint pain y menopause |
| 2. Cómo venden en otros países | Gethookd, búsquedas en español | M2-02: validar en países parecidos a Argentina (Colombia, Chile, España) | Cortisol en DE, FR, ES, PT, CL, UY y CO. Hinchazón en CL (Cáscara, 595 anuncios), MX (NUVI+) y ES (Sonvital) |
| 3. Ganador | **Jev** (TypeSafe), `jev_ranking.py` | Doc-A: MUSTs como vetos y NICEs ponderados. Nicho laboratorio (M2-11), promesa tiempo-resultado (M2-03) y advertencia ética (M2-08) | ver tabla abajo |
| 4. Saturación AR | Skill **radar-adlibrary-ar** | Semáforo y plan de entrada | 🟡 Caliente, con hueco en el mecanismo digestivo |

### Ranking de Jev (top 6 de 14)

| # | Candidato | Puntaje | Qué lo frenó |
|---|---|---|---|
| 🥇 | **Debloat probióticos + enzimas** | **70,5** | Riesgo regulatorio medio-alto (se controla con los claims) |
| 2 | Gotas de drenaje linfático | 66,7 | Espacio en AR 0,28. Riesgo ético y regulatorio |
| 3 | Cápsulas "cortisol belly" | 64,8 | **Promesa de tiempo 0,27** (tarda semanas). Claims de adelgazamiento (riesgo 1,0) |
| 4 | Magnesio complejo | 63,2 | Espacio en AR 0,01 (commodity de farmacia) y mecanismo débil |
| 5 | Hierro para caída de pelo | 48,1 | Sin evidencia LATAM y resultados lentos |
| 6 | Barra shampoo coreana | 47,8 | Sin evidencia LATAM |

Las señales crudas y la confianza de cada pregunta están en `jev_resultados.json`. Los pesos están en `combinar_puntaje()` de `jev_ranking.py`: cambialos y volvé a correr el script.

---

## 1. Radar Argentina (skill radar-adlibrary-ar)

### Marcas relevadas (Ad Library AR, activas, orden por impresiones)

| Marca | Anuncios | Foco | Longevidad | Producto / ángulo | Precio |
|---|---|---|---|---|---|
| **Pureza** | ~240 | 100% (1 ficha) | 78 anuncios con 60+ días, top de **335 días** 🏆 | Gotas de drenaje, "40.000+ mujeres ya dejaron de sentirse hinchadas" | $47.900 (tachado $65.000) |
| **Drenova** | ~220 | 98% | 17 nuevos, casi todos de 40 a 60 días 📈 | Gotas de drenaje, "tu cuerpo tiene un sistema de limpieza interno", 2x1 + envío gratis | $49.990 |
| **Lympha** | ~190 | 94% | Todos con menos de 45 días 📈 | Gotas de drenaje, "a veces no es grasa, es retención". Order bumps: gua sha, ebook, seguro de envío | 2x1 con +1 al 70% OFF ($19.990) |
| **Dr. Karol Green / Linfozen** | ~120 | 100% | **Todos con 10-11 días** 🧪 (marca recién lanzada) | Clon de Pureza | 1: $49.960 · 2: $59.950 · **3: $69.940 ($23.313/u)** |
| **Restora Labs** | ~220 | 98% | 13 con 60+ días, top de 87 días | Limpieza intestinal, "caca de piedra" / constipación | $95.980 |
| **Cortizen / Cortizzen** | ~150 en 4+ tiendas clon | 57% | 41 nuevos con menos de 15 días | "Cápsulas adelgazantes" de cortisol | $59.990 |
| **Bell Esencia** | ~130 | 52% | 3 con 60+ días | Detox de hígado (cardo mariano), advertorial de storytelling | — |
| **Diabla** | ~190 | ~15% en su probiótico | Marca de catálogo | Probiótico "Super Flora" dentro de un catálogo de proteína y greens. Suscripción -20% | $95.999 en MELI |

### Semáforo

| Eje | Lectura | Color |
|---|---|---|
| Marcas DTC con el mismo dolor ("hinchazón") | 8+ (casi todas de drenaje) | 🔴 |
| Marcas DTC con el **mismo mecanismo** (probiótico/enzima para la hinchazón post-comida) | 0 enfocadas (Diabla es de catálogo) | 🟢 |
| Anuncios activos del líder | Pureza ~240 | 🔴 |
| Marcas nuevas en los últimos 15 días | Linfozen, Cortizen y Lympha | 🔴 (en drenaje) |
| Ángulos tomados | "no es grasa, es retención" (4 marcas) y "+40.000 mujeres" (Pureza y su clon) | 🔴 si copiás el drenaje |
| Demanda MELI | Digecaps (enzimas) **+10 mil vendidos** a $62.500. Probióticos +10 mil. Pureza +5 mil | 🟢 demanda probada |

**Veredicto: 🟡 CALIENTE.** El dolor está validado y hay plata peleando. Se entra con **mecanismo propio (digestivo)**, nunca clonando el drenaje linfático.

**Línea de flotación:** $23.313 por unidad (Linfozen x3) y 2x1 con envío gratis (Drenova, Lympha).

### Viabilidad
- **Regulatorio (el riesgo principal):** un suplemento dietario necesita RNPA (producto) y RNE (establecimiento), incluso para vender online. ANMAT prohíbe productos con registros vencidos. Según el Decreto 697/2026 el registro de alimentos pasó a SENASA: **confirmalo con el laboratorio**. Camino práctico: laboratorio **fasón / marca blanca** que ya tenga RNE y registre tu RNPA. En el rótulo **no pueden ir indicaciones terapéuticas**. Fuentes: [Instructivo registro de suplementos](https://www.assal.gov.ar/documentos/Instructivo%20Registro%20Suplementos%20dietarios.pdf), [BFood – RNPA](https://www.bfood.com.ar/registro-rnpa), [ANMAT prohibió 18 suplementos](https://dib.com.ar/sociedad/la-anmat-prohibio-la-elaboracion-y-venta-18-suplementos-dietarios-n48538).
- **Proveedor:** hay cadena local (Digecaps, Enzihelp y probióticos nacionales en MELI). Pedí cotización a 3 laboratorios con el método de [[M2-05 Búsqueda de productos con GPT y biblioteca|M2-05]] (captura + ChatGPT con investigación avanzada: "laboratorio fasón suplementos dietarios Argentina").
- **Logística:** frasco chico y liviano, entra en envío estándar de Andreani o Correo. Fulfillment con Senydrop ([[Modulo 10 - Logistica fullfilment|M10]]).
- **Veredicto: viable con fricción.** La fricción es el RNPA y los claims en Meta.

---

## 2. Plan de acción: 4 semanas

### Semana 0: Fundaciones (días 1 a 5)

**Producto y números**
- [ ] Cotizar con 3 laboratorios: fórmula de probióticos (Bacillus coagulans o multicepa) + enzimas (amilasa, proteasa, lipasa, lactasa) + jengibre o hinojo. Formato: **gomitas** si el MOQ lo permite (diferencial de formato contra las gotas y las cápsulas), si no, cápsulas. 60 u = 30 días.
- [ ] Confirmar RNE y RNPA con el laboratorio antes de pagar.
- [ ] Cargar costos en la [[Calculadora de costos AcademAI]] ([[M2-12 Aplicación calculadora de costos y rentabilidad|M2-12]]). Supuesto de trabajo, **reemplazalo con tu cotización**:

| Oferta | Precio | $/u | Costo prod. | Fulfill. + envío | Comisiones (~11%) | Margen antes de ads | **CPA breakeven** |
|---|---|---|---|---|---|---|---|
| 1 frasco | $44.900 | 44.900 | 7.000 | 8.500 | 4.940 | 24.460 | **~$24.400** |
| 2 frascos (pack empujado) | $59.900 | 29.950 | 14.000 | 8.500 | 6.590 | 30.810 | **~$30.800** |
| 3 frascos | $74.900 | 24.967 | 21.000 | 8.500 | 8.240 | 37.160 | **~$37.100** |

  El ROAS breakeven del pack x2 da ≈ 1,95. Regla del doc-A: si el costo es de $5.000 a $10.000, el markup es x7, y $44.900 está dentro del rango. Bundles calculados como en M2-12: baja el $/u y sube el margen total.
- [ ] Correr la skill **doc-b-builder** (Claude) sobre el producto para armar buyer persona, VOCC, objeciones y ángulos. Es el "documento madre" de [[M2-09 Validar productos ganadores con skills de Claude|M2-09]].

**Arreglar la tienda Shopify (errores detectados en "The Lazy Susan Co.")**
- [ ] 🔴 **Moneda de la tienda en USD:** el producto "Radio – Rascador" tiene precio 49.900 en USD, o sea que se muestra como **US$49.900**. Cambiar la moneda a ARS en Configuración → Mercados/Tienda **antes** de cargar productos y pauta.
- [ ] 🔴 **Zona horaria en EDT:** pasarla a Buenos Aires (GMT-3). Si no, los reportes por día no coinciden con los de Meta y las lecturas de "día 1 / día 2" del testeo quedan corridas.
- [ ] Nombre y dominio: "The Lazy Susan Co." y el `.myshopify.com` crudo no sirven. Comprar dominio propio en Hostinger y conectarlo ([[M3-10 Configuración completa de Shopify y dominio|M3-10]]). Un `.myshopify.com` es señal de "operación recién armada" y le resta confianza.
- [ ] Mercado Pago Checkout Pro + Cuotas sin Tarjeta ([[M3-02 Configuración inicial de Shopify pagos, píxel y envíos|M3-02]]). Envío gratis + express con costo.
- [ ] App de Facebook y píxel. Verificar AddToCart, InitiateCheckout y Purchase en "Probar eventos". Hacer una compra de testeo con el precio bajado.
- [ ] Idioma español. Checkout con logo y colores propios, pidiendo solo los datos necesarios.
- [ ] Desactivar el seguimiento de inventario en las variantes ([[M3-04 Cómo replicar una landing con IA en Shopify|M3-04]]).

### Semana 1: Landing (días 6 a 10)

**Referencias a replicar (método de [[M3-04 Cómo replicar una landing con IA en Shopify|M3-04]], con [[Prompt maestro - Replica de landings en Shopify]]):**
- Landing principal: `lemmelive.com/pages/debloat-lp-v2` (Lemme Debloat, 545 anuncios en EE.UU.).
- Referencia de mecanismo: `restartyourgut.com/pages/ryg-er-pdpfb/` (GetEmmaRelief, 238 días: "esto no es otro probiótico").
- Referencia de estructura local: la ficha de Pureza (qué oferta y garantía usa el líder de AR).

**Estructura (5 etapas de [[M3-03 Los cinco pasos para que una landing venda|M3-03]], en este orden):**
1. **Primer pantallazo:** qué es + beneficio + prueba + CTA. *"Panza liviana después de comer. Sin globo a la noche."* Estrellas, "envío gratis" y botón.
2. **Desear:** línea de tiempo honesta: *"Día 1: menos gases después del almuerzo. Semana 1: la panza de la noche se parece a la de la mañana. Semana 3: comés sin pensar en qué te va a caer mal."*
3. **Creer (mecanismo):** comparativa *"¿Gotas de drenaje, té detox o enzimas?"*. La hinchazón post-comida es fermentación, no agua. Ingredientes con su función. Tabla versus (idea de [[M4-03 Doce ideas de contenido creativo para testear anuncios|M4-03]]).
4. **Sentirse seguro:** garantía **30 días "panza liviana o te devolvemos"** (M2-03: no le tengas miedo a la garantía fuerte), reseñas y FAQ con las dudas más fuertes arriba ("¿Tiene RNPA?", "¿Sirve si ya tomé probióticos?", "¿Cuándo lo noto?").
5. **Actuar:** selector 1 / **2 (más elegido)** / 3, cuotas, envío gratis y botones de compra a lo largo de toda la página.

- [ ] Imágenes: ChatGPT + Higgsfield ([[M3-08 Cómo crear fotos y producto Shopify|M3-08]]). Carrusel de videos de creativos ([[M3-13 Creando Liquid y sección de producto|M3-13]]).
- [ ] Carrito en Liquid y variantes conectadas por ID.
- [ ] **Advertorial** para tráfico frío (M2-04, M4-14 "presentación"): *"Por qué las gotitas de drenaje no te bajaron la panza (y qué sí)"*. Estructura: camino fallido → mecanismo único → testimonio → cierre. Es fácil de armar (imagen + texto largo) y funciona con +50 años.
- [ ] Probar la velocidad desde el celular ([[Prompt - Mejorar la velocidad de carga (Lovable y Magic Patterns)]]).

**Claims (Meta + ANMAT):** decir "ayuda a una digestión más liviana", "menos sensación de hinchazón después de comer". **Nunca** decir "adelgaza", "cura", "elimina grasa", ni usar antes/después de cuerpo con cinta métrica (lo rechaza Meta y es la advertencia ética de M2-08).

### Semana 1: Creativos (en paralelo)

Mix del primer testeo según [[M2-08 Elegir creativos ganadores con los filtros de Gethookd|M2-08]] y [[M4-15 Niveles de conciencia del comprador|M4-15]]: **3 fríos, 3 tibios y 2 calientes**, un ángulo por creativo ([[M4-02 Los nueve ángulos de venta y cómo usarlos|M4-02]]), guiones de 25 a 30 s con hook + cuerpo + CTA ([[M4-04 Cómo pedirle a la IA los guiones|M4-04]]).

| # | Temperatura | Ángulo | Hook (listo para grabar) |
|---|---|---|---|
| 1 | Frío | Dolor | *"A la mañana tengo panza chata. A las 9 de la noche parezco embarazada de cuatro meses. Y no, no es grasa."* |
| 2 | Frío | Mecanismo | *"Si las gotitas de drenaje no te hicieron nada, es porque tu hinchazón no es agua: es comida que tu panza no termina de romper."* |
| 3 | Frío | Identidad | *"Soy de las que se desabrochan el jean después del asado. Esto es para nosotras."* |
| 4 | Tibio | Prueba (UGC real) | *"Me tomé dos antes del asado del domingo. Tres horas después pasó esto."* |
| 5 | Tibio | Autoridad | Nutricionista/b-roll: *"La hinchazón de la tarde tiene un nombre: fermentación. Y se ataca antes de comer, no después."* |
| 6 | Tibio | Versus | *"Gotas de drenaje, té detox o enzimas: probé las tres un mes."* |
| 7 | Caliente | Oferta | *"Pack x2 con envío gratis y 30 días de garantía: si tu panza no está más liviana, te devolvemos la plata."* |
| 8 | Caliente | Urgencia real | *"Último lote de septiembre: 3 frascos a $24.967 cada uno."* |

- [ ] Producción: UGC con IA y b-roll con Flow (Veo 3) + CapCut ([[M4-13 Proceso completo de creativos con IA|M4-13]]), voz con ElevenLabs ([[M4-05 Cómo generar la voz en off con IA|M4-05]]).
- [ ] Adaptar 1 o 2 réplicas de Lemme o Wild Dose a la jerga argentina ([[M4-06 Cómo adaptar un video réplica a la jerga argentina|M4-06]]), sacando toda mención de la marca original.
- [ ] Sumar 2 o 3 **imágenes** estáticas para evaluación y conversión ([[M5-03 Armado práctico de campaña CBO infinito|M5-03]]).
- [ ] **Pendiente del radar (Fase 3):** con "Download creative" de Gethookd, bajá los 3 creativos más longevos: el video de Pureza con 335 días ("40.000+ mujeres…"), el de Restora con 74 días ("¿Te limpiás más de 4 veces…") y el top de Lemme Debloat. Pasámelos para deconstruir los primeros 3 segundos con ffmpeg.

### Semana 2: Lanzamiento en Meta Ads (días 11 a 18)

**Estructura** ([[M5-01 Configuración de cuenta publicitaria y primera campaña|M5-01]], [[M5-03 Armado práctico de campaña CBO infinito|M5-03]]):
- Campaña de **Ventas "DEBLOAT – CBO infinito – fecha"**, presupuesto de **40 a 50 USD/día**, un conjunto, Advantage+ abierto (sin edad ni género), excluir Tierra del Fuego, conversión en sitio web y evento **Comprar**.
- Subir **18 anuncios** (8 guiones × variantes de copy e imagen), **activar 10 el día 1** y sumar 2 por día.
- 3 versiones de texto principal, título y descripción por anuncio. Nombre del anuncio = el hook.
- Destino: **ficha del producto**, nunca la home. Los fríos pueden ir al advertorial.
- Cargar la campaña **6 a 10 h antes** y que arranque a las 00:00 del día siguiente.
- Si el presupuesto es más ajustado, usar la alternativa ABO de [[M5-14 Cómo elegir entre campaña CBO y ABO|M5-14]]: presupuesto ÷ conjuntos. Si da menos de $10-15 mil por conjunto, máximo 3 anuncios por conjunto.

**Árbol de decisión día a día** ([[M5-02 Testeo, estabilización y renovación día a día|M5-02]], [[M4-17 Testeo de productos ganadores en Meta Ads|M4-17]]):

| Día | Si… | Entonces… |
|---|---|---|
| 1 | 0 carritos | Descartar el ángulo. Si el CTR es de 5-7%, primero revisar la landing o el pago |
| 1 | Menos de 3 ventas, CTR ≥3% y ATC ≥10% | **Día 2 = estabilizar**: no tocar nada |
| 1 | 5-6 ventas | Duplicar con creativos nuevos y +70% de presupuesto |
| 1 | Más de 6 ventas | Saltar la estabilización: nuevo conjunto con 6 anuncios y +15 USD |
| 3 | — | **Reemplazar** (no duplicar) los anuncios que no gastaron por iteraciones del ángulo ganador |
| 5+ | — | Campaña nueva de **renovación** con 6 videos distintos (nunca repetir creativos entre campañas) |
| 7+ | 3-4 anuncios estables con buen CPA y más de 60 USD gastados | Escalar por **Post ID**: ABO con 4 conjuntos, presupuesto de 2 × CPA BE ([[M5-04 Cómo usar el Post ID para escalar\|M5-04]]) |
| 10+ | 5-6 ganadores y margen >25% | BidCap: puja inicial de CPA promedio × 2 y +1 USD por conjunto ([[M5-08 Escalado agresivo con campañas BidCap\|M5-08]]) |

**Umbrales** ([[M5-05 Métricas del embudo de ventas en Meta Ads|M5-05]]): CPM de 7-10 USD · CTR ≥3% · CPC ≤0,5 USD · ATC ≥10% de los clics · pagos iniciados ≥60-65% de los carritos · compras ≥20% de los carritos · CPA ≤ CPA breakeven (~$30.800 en el pack x2) · ROAS ≥2.

### Semana 3-4: Escalar y renovar
- Escalado horizontal ([[M5-07 Escalado horizontal con un caso real|M5-07]]): testeo → duplicado con renovación → CBO de ganadores → campaña 100% nueva.
- RENO e iteración de hooks ([[M5-09 Escalado RENO con fragmentos del hook|M5-09]], [[M5-11 Iteración de creativos ganadores con hook y cuerpo|M5-11]]): cortes al 15%, 25% y 35-40%, y hook 1 + cuerpo 2, siempre en un conjunto aparte.
- Cada vez que subas presupuesto, sumá creativos en la misma proporción ([[M5-15 Cómo funciona Andrómeda y la renovación de creativos|M5-15]]).
- Ecosistema (doc-A bloque 3): suscripción mensual con -15% (Diabla lo hace), y como upsell un té digestivo o fibra prebiótica.

---

## 3. Auditoría de campañas: puntos erróneos a revisar

Checklist sacado del vault. Si en tu cuenta aparece cualquiera de estos, es un error:

**Configuración**
- [ ] Advantage+ de **catálogo activado**: Meta muestra fotos de producto en vez del video (M5-01).
- [ ] **"Enlaces al sitio" y "Productos"** activos en el contenido del anuncio: generan fuga hacia otro producto o página (M5-03).
- [ ] Mejora "**Mostrar productos**" o variantes de imagen IA de Meta activas (M5-01, M5-03).
- [ ] Evento de optimización distinto de **Comprar**, o conversión "sitio web y app" (M5-01).
- [ ] Destino a la **home** en vez de la ficha del producto (M5-13).
- [ ] Público restringido por edad o género con cuenta nueva (M5-13).
- [ ] **Dos productos en la misma campaña**: ensucia el píxel (M5-07).
- [ ] Campaña cargada a la noche o arrancando a media jornada (M5-03).
- [ ] Moneda o zona horaria de la tienda distinta de la cuenta publicitaria (detectado en tu Shopify).

**Decisiones**
- [ ] Apagar **campañas** por el CPA general en vez de apagar **anuncios** puntuales (M5-02).
- [ ] Decidir en menos de **48 h** (sin día de estabilización) (M5-02).
- [ ] Apagar un anuncio que no vendió pero trae buen CTR, carritos y costo por carrito: está prospectando (M5-05, M5-15).
- [ ] **Duplicar** un anuncio ganador en vez de usar su **Post ID**: pierde el historial (M5-04).
- [ ] Reutilizar el mismo creativo en campañas distintas (M5-02).
- [ ] Subir presupuesto sin sumar creativos, lo que se ve como frecuencia en aumento y fatiga (M5-15).
- [ ] BidCap con margen menor al 25% (M5-08).
- [ ] Juzgar por el ROAS de Meta sin descontar costos reales (M5-06: usar la calculadora o Escalafy).

**Cómo auditarlo con Claude** ([[M6-01 Meta Ads con Claude|M6-01]]): en Claude, Configuración → Conectores → conector personalizado con `mcp.facebook.com/ads`. Pasale tu CPA breakeven (~$30.800) y tu ROAS breakeven (~1,95) y pedile que marque campañas en pérdida y los puntos de este checklist.

---

## 4. Riesgo principal
**Regulatorio + política de Meta.** Sin RNPA vigente no se puede vender. Un claim de adelgazamiento o un antes/después de cuerpo puede desaprobar la cuenta publicitaria. Mitigación: laboratorio con registro, copy centrado en "digestión liviana" y cuenta publicitaria calentada con la tienda ya prolija.

## Archivos de esta corrida
- `candidatos_gethookd.json`: 14 candidatos con la evidencia de Gethookd por país.
- `jev_ranking.py` y `jev_resultados.json`: ranking de Jev con las reglas del vault.
- `radar_extract.js`: extractor de la Ad Library usado en el radar.
