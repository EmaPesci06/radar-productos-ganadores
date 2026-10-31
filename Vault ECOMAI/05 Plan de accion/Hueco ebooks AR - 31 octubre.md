---
tags: [ecomai, ebooks, plan-de-accion, radar-ar]
fecha: 2026-10-31
estado: investigando
---
# Hueco de ebooks en Argentina (31/10/2026)

> [!summary] En 30 segundos
> - **El hueco real no es un tema, es una forma de vender:** casi todas las ofertas de ebooks que le llegan a Argentina son de operadores de LATAM, Brasil o Europa que cobran **en USD, en español neutro y sin Mercado Pago**. Muy pocas cobran en **pesos, con voseo y Mercado Pago**. Las pocas locales que lo hacen (Jazmín Cocina, Nutri de Confianza, Pilates en la Pared con Caro) tienen 3 a 5 anuncios: están probando, nadie escaló.
> - **Temas con ganador afuera y poco o nada en AR:** 1) **ciática y dolor lumbar** (encaja con la Marca de la almohada lumbar), 2) **ejercicios somáticos** (afuera crece, en AR solo hay operadores brasileños), 3) **dejar el pañal** (cero ofertas digitales en AR).
> - **Saturados en AR, no entrar:** yoga en silla, menopausia/cortisol, drenaje linfático, hígado graso.
> - **Rentabilidad:** a $19.900 con un order bump, el CPA de equilibrio ronda **$20.000**. Con CPA de $10.000 y $30.000/día de pauta deja unos **$800.000 por mes**; con CPA de $15.000, unos $200.000. Sin stock ni envío.
> - **Recomendación de Claude:** arrancar por el **ebook de ciática y lumbar**, porque además de venderse solo trae compradores para la almohada lumbar (backend físico de $49.900). En paralelo, testear **somáticos** como ebook puro.

Reglas que sigo: [[Modulo 8 - Ebooks]] (validación de ofertas, precio, landing, upsells) y [[_Reglas - criterios vault ECOMAI]] (ganador afuera + poca competencia enfocada en AR + demanda probada).

---

## 1. Cómo lo medí y sus límites

- **Fuente:** Meta Ad Library vía API, anuncios **activos** al 31/10/2026, país **AR** (términos en español rioplatense) contra **US** (términos en inglés). Después conté los anuncios activos de cada anunciante clave.
- **Criterio del Módulo 8 (M8-02/M8-03):** una oferta está validada si tiene **20 anuncios o más** corriendo hace más de 3-4 días, **sin marca personal** y con **un solo producto**.
- **Límites (importantes):**
  - El "total estimado" de cada búsqueda cuenta **todo anuncio que menciona la palabra**, no solo ebooks (por ejemplo, "ojo seco" trae novelas románticas). Lo uso como termómetro, no como dato duro.
  - La API devuelve los anuncios **más nuevos primero**: no puedo ver cuánto tiempo lleva corriendo cada creativo ni ordenar por impresiones. Por eso falta la validación de **run time ≥30 días en GetHookd / Espiad** (paso 1 del plan).
  - Mercado Libre no sirve de termómetro para ebooks. La demanda se mide por quién pauta.

## 2. Afuera vs Argentina, tema por tema

| Tema (búsqueda por el dolor) | US activos | AR activos | Quién pauta en AR | Lectura |
|---|---|---|---|---|
| Ciática / lumbar ("sciatica exercises" / "ciática ejercicios", "dolor lumbar ejercicios guía") | 1.172 | 19 / 12 | **Vida Sin Ciática** (47 anuncios, voseo, USD, producto "Ciatiflex®", sin confirmar si es digital) y **Olga Sanchez** (12, mismo copy: el mismo operador con dos páginas) | 🟢🟡 Un solo operador enfocado. Nadie cobra en pesos. **Sinergia directa con la almohada lumbar** |
| Ejercicios somáticos ("somatic exercises" / "ejercicios somáticos") | 182 | 20 | **Isabel Navarro** (65 anuncios, BRL, "+90 Protocolos Somáticos" y "+120 Actividades del Nervio Vago", en español, italiano, etc.), Ana Rosa y Fernanda Domínguez (BRL) | 🟢 Ganador validado afuera (operador brasileño multipaís). **Ningún argentino** |
| Nervio vago | 4.015 | 366 | **Patricia Vega MD** (33 anuncios, voseo: "Reseteá tu nervio vago en 28 días", USD), osteópatas locales | 🟡 Ya hay un jugador argentinizado. Mejor como bono del somático |
| Dejar el pañal ("potty training" / "dejar el pañal") | ruido* | 62 | Ninguna oferta digital: solo pañales (UltraDries) y dramas | 🟢 Hueco total en AR. **Falta confirmar el ganador afuera** |
| Rodilla ("knee pain exercises guide" / "dolor de rodilla ejercicios") | 110 | 181 | **PuntoDigital** (10, voseo: "10 minutos por día para tus rodillas"), Pablo Gutiérrez | 🟡 Hay gente probando, nadie escaló. Encaja con la almohada de rodillas (Marca 1) |
| Cuidador de Alzheimer / demencia | 97 (casi todo servicios) | 7 | **Neurocuidadores** (6) | 🟡 Poca competencia y mucho dolor emocional, pero falta un ganador ebook afuera |
| Pilates en pared | 1.423 | 98 | LinkaCash ("Pilates 21 días en casa", USD), Pilates en la Pared con Caro (3, ARS), Axa/Natura Pilates | 🟡 Locales chicos, pero compite contra apps con quiz |
| Yoga facial | — | 119 | Varónica Navarro, Emily Parker (USD), Flor Gao y Profe Lore Torti (locales) | 🟡 Con marcas personales locales |
| Dieta antiinflamatoria / recetas argentinas | — | 165 | **Jazmín Cocina** (4, ARS, "100 Recetas Antiinflamatorias Argentinas") | 🟡 El ángulo "argentinas" existe pero está en prueba |
| Recetas para diabéticos | — | 226 | **Nutri de Confianza** (5, ARS, "+400 personas lo adquirió") | 🟡 Igual que arriba |
| Adiestramiento de perros | 7.374* | 295 | Woofz y Good Dogs (apps, USD), Gabriel Porcario (local) | 🔴 Apps grandes |
| TDAH adultos | 758 ("ADHD women") | 89 | Psicólogos y operadores para chicos (Mia Clark) | 🟡 Tema sensible de salud mental |
| Yoga en silla | 4.789 | 690 | Emma Taylor (EUR, decenas de anuncios por día), quiz funnels | 🔴 Saturado por apps |
| Menopausia / cortisol | — | 3.162 | Muscle Transformation Challenge, Emma Taylor | 🔴 Saturado |
| Drenaje linfático | 35.770 | 3.007 | Mayoría producto físico (FemLab) | 🔴 |
| Hígado graso | — | 1.174 | Operadores por WhatsApp (Bolivia, Brasil) | 🔴 |

*"Potty training" en US trae también entrenamiento de perros y otros anuncios; el número no sirve.

**El patrón general:** al buscar "ebook" en AR hay 5.791 anuncios activos, y la mayoría cobran en USD o BRL (Esencia Femenina Digital "Ebook + 3 bonos por USD 9,90", Relaciones Modo Dios "Kit USD 17", Raíz Saludable "sin TACC" en USD). Cobrar **en pesos con Mercado Pago, voseo y ejemplos locales** es la ventaja que el Módulo 8 ya da por hecha (M8-12: Shopify + Mercado Pago, $14.990 a $25.000) y que casi nadie aplica.

## 3. Los 3 candidatos

### 🥇 Ebook "Ciática y lumbar: plan de 21 días"
- **Ganador afuera:** Thomas W. Brenner (93 anuncios activos, EUR, en inglés: "My Sciatica Surgery Failed After 4 Months…"), con advertorial largo, el formato que el vault recomienda para +50 (M2-04).
- **AR:** un solo operador enfocado (Vida Sin Ciática + Olga Sanchez, ~59 anuncios en dos páginas, USD). Valida que hay quien pague por pautar el dolor en voseo, y deja espacio para una oferta en pesos.
- **Por qué primero:** cumple el **Bloque 3 del doc-A (ecosistema)**. El mismo comprador es el cliente de la almohada lumbar ([[Producto - Almohada lumbar ciatica]]):
  - El ebook se vende solo a $19.900 y **trae compradores** a los que después se les ofrece la almohada ($49.900).
  - Al revés: el ebook va **de bono** con la almohada y sube el valor percibido sin costo de stock.
- **Riesgo:** es salud. Nada de "curar la ciática". Promesa como experiencia ("10 minutos por día para moverte con menos dolor"), aviso de consultar al médico, y conviene que un **kinesiólogo argentino** revise el contenido (le da autoridad real, que el vault pide no inventar).

### 🥈 Ebook "Ejercicios somáticos: 28 días para soltar la tensión"
- **Ganador afuera:** Isabel Navarro (65 anuncios, opera en BRL y en varios idiomas) con "+90 protocolos somáticos" y un segundo producto de nervio vago. Es exactamente la oferta a **modelar** (M8-03): tomarla y hacerla más irresistible, no copiarla.
- **AR:** solo operadores brasileños en USD/BRL. Nadie local.
- **Para quién:** mujeres de 35 a 60 con estrés, ansiedad y contracturas. Bonos naturales: nervio vago, respiración, sueño.
- **Riesgo:** Patricia Vega MD ya pauta nervio vago en voseo (33 anuncios). Entrar por "somático" y dejar el nervio vago como bono.

### 🥉 Ebook "Chau pañal en 3 días" (o 7)
- **AR:** 62 anuncios con esas palabras y **ninguno vende un método**. Hueco total.
- **Falta:** confirmar el ganador afuera (en US el método "3 días" es un clásico, pero la búsqueda de la API trae ruido). Se valida en GetHookd / Espiad con "potty training" y en Brasil con "desfralde".
- **Ventaja:** público de mamás muy activo en Meta, compra emocional, ticket bajo y escalera a otros ebooks (sueño del bebé, berrinches, alimentación).

## 4. Rentabilidad (por qué un ebook puede rendir)

Supuestos: precio de **$19.900** (dentro del rango del M8-12), **order bump o upsell de $9.900** que toma el 30% de los compradores (M8-16), costos variables de alrededor del **12%** (Mercado Pago, 1% de Shopify con pasarela externa y 3% de IIBB; es una estimación), **$100.000/mes** de costos fijos (Shopify y apps) y **$30.000/día** de pauta.

| CPA real | Ventas/mes | Facturación | Neto después de comisiones | Pauta | Ganancia/mes |
|---|---|---|---|---|---|
| $10.000 | 90 | $2.058.300 | $1.811.300 | $900.000 | **≈ $811.000** |
| $15.000 | 60 | $1.372.200 | $1.207.500 | $900.000 | **≈ $207.000** |
| $20.000 | 45 | $1.029.150 | $905.700 | $900.000 | **≈ −$94.000** |

- **CPA de equilibrio ≈ $20.000.** El costo de producir el ebook es casi cero (Claude + Gamma + Canva, M8-06/07/09), así que no hay que recuperar stock.
- **Regla de corte del vault:** con USD 50 de campaña tienen que salir **5 ventas o más**. Si no, se cambia el ángulo o el tema.
- **El plus del ciática:** si apenas el 5% de los compradores del ebook se lleva después la almohada lumbar, son ~4 almohadas más por mes **sin pagar adquisición**.
- **Ojo:** el escenario de $10.000 es optimista para un primer mes. El realista para arrancar es el de $15.000, y la ganancia grande aparece cuando se suma el upsell y se escala.

## 5. "Proveedores" de un ebook

No hay fábrica: el "proveedor" es la cadena para producir, cobrar y entregar.

| Pieza | Opción del vault | Nota |
|---|---|---|
| Contenido | Claude con prompts encadenados (M8-07) o la skill con Higgsfield para ilustraciones (M8-06) | Pedir ejercicios con ilustración paso a paso |
| Revisión profesional | Kinesiólogo o fisiatra argentino (ciática, somáticos) | Le da autoridad real a la landing. Presupuesto: a cotizar |
| Diseño | Gamma (maquetado) + Canva (portada y mockups, M8-09) | |
| Tienda y cobro | Shopify plan Grow + Mercado Pago Checkout Pro + Digital Downloads (M8-12), o Impultienda (M8-11) | Impuestos en 0%, sin envío |
| Upsells | Sell Easy (M8-16) | Precio del upsell al doble con 50% off |
| Ofertas a modelar (exterior) | Thomas W. Brenner (ciática), Isabel Navarro (somáticos) | Modelar, no copiar (M8-03) |
| Espía | Espiad (plan gratis: 2 ofertas por día, M8-05) y GetHookd | Para validar run time |

## 6. Planificación (4 semanas)

| Semana | Qué | Entregable | Criterio para seguir |
|---|---|---|---|
| **1 (3-9 nov)** | Validar los 3 temas en **GetHookd y Espiad** (run time ≥30 días, ≥20 anuncios, una oferta). Abrir las landings de Thomas W. Brenner, Isabel Navarro y Vida Sin Ciática y anotar promesa, bonos, precio y garantía. Mini doc-A del elegido | Ficha `Producto - Ebook ciatica.md` en `06 Analisis compartido` | Ganador afuera confirmado y menos de 3 jugadores enfocados en AR |
| **2 (10-16 nov)** | Escribir el ebook (25 a 40 páginas, plan día por día), **5 bonos** (M8-10), 1 order bump y 1 upsell. Revisión del kinesiólogo | PDF final + bonos en Drive (M8-08) | Contenido revisado |
| **3 (17-23 nov)** | Landing (promesa, dolores, beneficios, bonos, garantía de 7 días, prueba social, FAQ) con Claude (M8-14), tienda en Shopify con Mercado Pago, 5 a 8 creativos (advertorial para +50, video "editable") | Tienda online y campaña lista | Compra de prueba OK y la landing se ve bien en el celular |
| **4 (24-30 nov)** | Testear con **USD 50** (CBO, M5-03). Si da 5 ventas o más, escalar y probar el ebook **como bono de la almohada lumbar** | Reporte de CPA, conversión y take rate del upsell | ≥5 ventas con USD 50 → escalar; si no, cambiar ángulo o pasar al somático |

Después, la escalera: segundo ebook (somáticos), y un **pack** de los dos.

## 7. Lo que falta y quién lo hace
- **Run time real en GetHookd/Espiad:** necesita el Chrome de Emanuel (sesión remota, como el 30/10).
- **Qué vende "Ciatiflex®" (Vida Sin Ciática):** abrir uno de sus anuncios. Si es un dispositivo físico, también es competencia de la almohada lumbar.
- **Tendencia en Google Trends AR** de "ciática", "ejercicios somáticos" y "dejar el pañal": tarea para Antigravity.

## Links de evidencia (Ad Library)
- Thomas W. Brenner (ciática, 93 activos): https://www.facebook.com/ads/library/?id=1111039125249360
- Vida Sin Ciática (47 activos): https://www.facebook.com/ads/library/?id=2184725335805558
- Olga Sanchez (12 activos, mismo copy): https://www.facebook.com/ads/library/?id=1115052017899009
- Isabel Navarro (somáticos, 65 activos): https://www.facebook.com/ads/library/?id=1105377672410492
- Patricia Vega MD (nervio vago, 33 activos): https://www.facebook.com/ads/library/?id=1159455353408468
- PuntoDigital (rodilla, 10 activos): https://www.facebook.com/ads/library/?id=1483497130300084
- Neurocuidadores (cuidadores, 6 activos): https://www.facebook.com/ads/library/?id=29433583426245254
- Pilates en la Pared con Caro (3 activos, ARS): https://www.facebook.com/ads/library/?id=28915112861476249
- LinkaCash (pilates 21 días): https://www.facebook.com/ads/library/?id=1397554275751368
- Jazmín Cocina (recetas antiinflamatorias argentinas, ARS): https://www.facebook.com/ads/library/?id=1447410530912933
- Nutri de Confianza (diabéticos, ARS): https://www.facebook.com/ads/library/?id=959170140223166
- Emma Taylor (yoga en silla, saturado): https://www.facebook.com/ads/library/?id=29281847021499962
- Esencia Femenina Digital (ebook en USD hacia AR): https://www.facebook.com/ads/library/?id=1661704265341016
