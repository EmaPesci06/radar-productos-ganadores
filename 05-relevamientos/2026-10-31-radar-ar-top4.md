# Radar AR — verificación independiente de los 4 candidatos top

| | |
|---|---|
| **Fecha** | 2026-10-31 |
| **Herramienta** | Meta Ad Library AR, país Argentina, anuncios activos, vía `scripts/radar-extract.js` |
| **Queries** | ciatica · almohada lumbar · almohada embarazo · dolor de cintura · nervio vago · ejercicios somaticos · dejar el pañal · control de esfinteres |
| **Qué es** | Medición **independiente y del mismo día** que la del vault, con otra herramienta (Ad Library directa, no GetHookd) |

> ## ⚠️ Esto son OBJECIONES, no correcciones
>
> El vault hizo su relevamiento el **30-31/10** y este es del **31/10**: mismo día.
> Entonces lo que sigue **no es "el mercado cambió"** — es una medición que **no
> coincide** con la del vault en tres de los cuatro candidatos.
>
> Por el flujo de `06 Analisis compartido/README.md`, las discrepancias van como
> **objeción en la tabla de revisión cruzada, y decide Emanuel**. Así que
> **no cambié ningún score**. Abajo está el recálculo propuesto para que lo veas,
> pero los números del scorecard siguen como los dejó el vault hasta que resuelvas.
>
> Posibles causas de la discrepancia, además de que yo esté equivocado: el vault
> usó GetHookd (que indexa distinto) y yo la Ad Library directa; y los términos de
> búsqueda pueden no ser los mismos.

---

## Resumen

| Candidato | Hueco según vault | Lo que mido hoy | Objeción |
|---|---|---|---|
| **#1 Almohada Lumbar** (95) | 19/20 | El rodillo hueso **sigue sin competencia**. Pero la categoría de almohada ortopédica tiene 4 probados y **5 marcas arrancadas en 10 días** | 🟡 menor |
| **#2 Almohada Embarazo** (94) | 20/20 — "0 marcas DTC" | **Micolecho: 716 días al aire**, copy al público, tienda propia. Y figura en el plan como *proveedor* | 🔴 fuerte |
| **#3 Ebook Somáticos** (93) | 19/20 — "nadie cobra en ARS" | **Cursa Virtual: 169 días**, tienda `.com.ar`. Isabel Navarro escalando con 14 ads. **5 marcas en 15 días**, una clonando su dominio | 🔴 fuerte |
| **#4 Ebook Chau Pañal** (92) | 20/20 | **Confirmado exacto.** ~75 resultados, 18 marcas, **todas producto físico**. Cero digital | ✅ se sostiene |

---

## 1. Almohada Lumbar / Ciática — 🟡 aguanta, con nota

### "ciatica" — ~350 resultados, 27 anuncios, 16 marcas

| Ads | Días | Marca | Destino |
|---|---|---|---|
| **10** | 166 | **María Elena Vargas** (10 advertorials) | `es.groundingwell.com/products/...` |
| 2 | 225 | Punto Quiropráctico | `chiro-sphere.com` |
| 1 | 166 | GroundingWell | `es.groundingwell.com/products/...` |
| 1 | 78 | **Vida Sin Ciática** | `nervialabs.site/productos/ciatiflex-...` |
| 1 | 40 | Enerflex Argentina | `tupedidoaqui.com/enerflex-verde/` |

De 16 marcas, **ninguna vende almohada ni espuma**. Son quiroprácticos y masajistas
(servicio), colchonetas de grounding y una crema tópica.

✅ **Confirma el vault:** *Vida Sin Ciática* con Ciatiflex, tal cual lo describía.

🔍 **Hallazgo nuevo — la operación más escalada del nicho:** *María Elena Vargas* no es
una marca, es una **página-persona con 10 advertorials y 166 días al aire**, todos a
GroundingWell, que además aparece aparte con un solo anuncio. Copys en primera persona:
*"Manejo un Airbnb, una huésped me llamó llorando"*, *"Soy sobadora desde hace años"*.
Es exactamente el patrón de advertorial para +50 del M2-04. **Vale estudiarla como
referencia de formato**, no de producto.

### "almohada lumbar" — solo ~15 resultados, 15 anuncios, 12 marcas

| Ads | Días | Marca | Destino |
|---|---|---|---|
| 2 | 121 | Fisicaline | `fisicaline.com/.../duo-aliv...` |
| 2 | 60 | Nuvia comfort | `nuviacomfort.shop` |
| 1 | 95 | Calm es simple | `calmessimple.com.ar/producto/colchon-...` |
| 1 | 77 | Nómada | `bynomada.com/productos/almohada-intelige...` |
| 2 | 5 | Blanco & Deco | sin destino |
| 1 | 2 | Ortho bed | `7e1yqp-uk.myshopify.com/products/orthobe...` |
| 1 | 2 | Solvex | `solvexarg.shop/products/almohadon-ortope...` |
| 1 | 10 | Matcor / Que Baratooo | sin destino |

✅ **El producto específico sigue libre:** ninguna vende el **rodillo hueso lumbar**.

⚠️ **Pero la categoría se está activando.** Cinco marcas arrancaron en los últimos 10
días (Blanco & Deco 5d, Que Baratooo 10d, Matcor 10d, Ortho bed 2d, Solvex 2d). Por el
semáforo del vault, el eje "marcas que arrancaron en los últimos 15 días" con 4+ es
🔴. Dos de ellas venden almohadón ortopédico, que es vecino directo.

Detalle operativo: *Ortho bed* apunta a un `myshopify.com` crudo sin dominio propio —
señal de operación recién armada, de las que suele apagarse rápido.

### "dolor de cintura" — ~2.100 resultados, 28 anuncios, 24 marcas

Casi todo servicio (fisios, pilates, estética, rehabilitación) y ruido de apps de
drama. **Ninguna marca de almohada.** Refuerza que el ángulo de dolor lumbar como
producto físico está libre.

---

## 2. Almohada de Embarazo — 🔴 objeción fuerte

### "almohada embarazo" — ~330 resultados, 26 anuncios, 15 marcas

La query está casi toda contaminada con anuncios de apps de drama de Google Play. De
las 15 marcas, **solo una es real del nicho**:

| Ads | Días | Marca | Destino | Copy |
|---|---|---|---|---|
| 2 | **716** | **Micolechoargentina** | `micolecho.com.ar` | "Mejora tu sueño con nuestra almohada maternal es perfecta pa..." |

**716 días al aire es el anuncio más longevo de todo el relevamiento.**

### La objeción

El vault puntuó el hueco **20/20** con el fundamento *"0 marcas DTC con embudo de dolor
en Meta AR"*, y listó **micolecho** entre los **proveedores** a contactar para fabricar
la almohada de embarazo (junto a MTL, Hola Luisina, Jomaro/Tapitel).

Las dos cosas no pueden ser ciertas a la vez. Micolecho corre publicidad con copy de
venta al público, a su propia tienda, desde hace casi dos años. **En la subasta de Meta
es competencia**, le compremos o no.

⚠️ **No pude confirmar si además fabrican a terceros:** `micolecho.com.ar` está
bloqueado en esta sesión. Es posible que sean fabricante **y** marca DTC, que es el peor
caso: nos venderían el producto y después nos compiten con ventaja de costo.

**Qué verificar antes de cotizarles:** si tienen línea mayorista / façon, y si aceptan
que un cliente les compite en Meta con el mismo producto.

---

## 3. Ebook #1 Somáticos / Nervio Vago — 🔴 objeción fuerte

### "nervio vago" — ~380 resultados, 28 anuncios, 13 marcas

| Ads | Días | Marca | Destino |
|---|---|---|---|
| 4 | **169** | **Cursa Virtual** | `cursavirtualtienda.com.ar/productos/cuer...` |
| 4 | 67 | Isabel Navarro | `herramientas-somaticas.netlify.app` |
| 4 | **11** | Camila con C | `reset-linfatico-ar.impultienda.ar/q/rese...` |
| 3 | 24 | Nuropod (3 advertorials) | `nuropod.com/es/pages/11-reasons-why-tens...` |
| 3 | **10** | Auralis Solutions | `nervio-vago.impultienda.ar` |
| 2 | 75 | Tienda Yapita | `tiendayapita.myshopify.com/products/masa...` |
| 2 | 239 | Carolina Cancio | `instagram.com/carolina.cancio` |
| 1 | **10** | **Patricia Vega MD** | `nervio-vago.impultienda.ar` |
| 1 | 8 | Liviana | `liviana.lat` |
| 1 | 6 | Dra. Florencia Sanabria | `instagram.com/dra.florencia.sanabria` |

### "ejercicios somaticos" — ~22 resultados, 21 anuncios, 8 marcas

| Ads | Días | Marca | Destino |
|---|---|---|---|
| **14** | 43 | **Isabel Navarro** | `herramientas-somaticas.netlify.app` |
| 1 | 25 | El Alma Sabe Más | `elalmasabemas.com/products/curso-sanacio...` |
| 1 | **1** | **Ana Rosa** | `herramientasomaticas.site` |
| 1 | 3 | Somatico Art | `somaticoart.com/registroesencial` |
| 1 | 3 | anandapsicologia | sin destino |
| 1 | 1 | Fernanda Dominguez | `kitpausayequilibrio.shop` |

### Las tres objeciones

**a) El "hueco de cobro en pesos" no se sostiene.** El fundamento del 19/20 era que
*ningún operador local cobra en ARS con Mercado Pago*. Hoy encuentro:

- **Cursa Virtual con 169 días al aire** y destino a una tienda `.com.ar`
- **Tres operadores en `impultienda.ar`** — que es el constructor de tiendas del M8-11,
  con checkout en pesos. Uno tiene el subdominio literal `nervio-vago`
- **Patricia Vega MD**, que el vault tenía como "cobra en USD", apuntando hoy a
  `nervio-vago.impultienda.ar`

**b) Cinco marcas arrancaron en los últimos 15 días.** Camila con C (11d), Auralis (10d),
Patricia Vega (10d), Liviana (8d), Dra. Sanabria (6d). En "ejercicios somáticos" hay
cuatro más de 1 a 3 días. Por el semáforo del vault, 4+ es 🔴 — y acá hay el doble.

**c) Isabel Navarro ya no es un modelo a copiar: es el jugador dominante, y ya la están
clonando.** Tiene **14 de los 21 anuncios** visibles del nicho (foco ~67%), y los 14
comparten **el mismo copy con creativo distinto** — la señal exacta que describe la
skill: está testeando ángulos visuales sobre un texto ganador. Y *Ana Rosa*, con **1 día
al aire**, apunta a `herramientasomaticas.site`, un clon del dominio de Isabel Navarro.

El M8-03 es explícito sobre esto: copiar una oferta escalada beneficia al original,
porque tiene más anuncios, más tiempo y más presupuesto. Entrar hoy es entrar detrás de
ella **y** detrás de cinco que arrancaron esta semana.

---

## 4. Ebook #2 Chau Pañal — ✅ confirmado, el único que se sostiene

### "dejar el pañal" — ~75 resultados, 29 anuncios, 18 marcas

| Ads | Días | Marca | Qué vende |
|---|---|---|---|
| **7** | 16 | UltraDries Argentina (4 advertorials) | pañales de entrenamiento |
| 4 | 69 | Juguetear | juguetes |
| 3 | 18 | Nala Co | pañales de entrenamiento |
| 1 | 92 | Importbaires | pelela / asiento de inodoro |
| 1 | 78 | Bonitos Dreams | pañales ecológicos |
| 1 | 75 | Primer Luna | bombachas absorbentes |
| 1 | 4 | Clover | bombacha de entrenamiento |

**Las 18 marcas venden producto físico. Ninguna vende un método digital.**

✅ Confirma textualmente el vault: *"los anuncios en Meta AR son solo pañales y
bombachitas"*. Y la pediatra argentina que vende la guía grabada sigue sin pautar.

🔍 **Dato de formato:** *UltraDries* corre **4 advertorials** sobre pañales de
entrenamiento con 16 días. El formato advertorial ya está validado en este dolor y en
este país — es el que conviene usar, no el video de producto.

⚠️ **La ventana es ahora.** El pico es octubre-febrero (sacar el pañal con el calor,
antes del jardín en marzo). En el plan de 6 semanas está recién en la Semana 3.

---

## 5. Lo que no se pudo medir

| Query | Estado | Por qué |
|---|---|---|
| **control de esfinteres** | 🟡 **SIN_LEER** | La página no renderizó en 2 intentos (898 chars). **No es un hueco: no se midió.** Afecta al Ebook #3 (Control Pélvico, 88/100), que queda sin verificar |
| `micolecho.com.ar` | 🔴 dominio bloqueado | No pude confirmar si Micolecho vende mayorista además de DTC |
| Demanda en MELI | 🔴 bloqueado | MELI muestra pantalla de login a IPs de datacenter |
| Google Trends AR | 🔴 429 | Rate-limit a la IP del contenedor |

Para el Ebook #3 hay que correr de nuevo la query, o medirla desde una sesión local.

---

## 6. Recálculo propuesto (NO aplicado)

Si Emanuel acepta las objeciones, los ejes de hueco quedarían:

| Candidato | Hueco | Total | Antes | Veredicto |
|---|---|---|---|---|
| Almohada Lumbar Hueso | 19 → **17** | **93** | 95 | 🟢 EJECUTAR YA |
| **Ebook #2 Chau Pañal** | 20 → **20** | **92** | 92 | 🟢 EJECUTAR YA |
| Jabón de Caqui | sin medir | 90 | 90 | 🟢 EJECUTAR YA |
| Loción de Magnesio | sin medir | 89 | 89 | 🟢 EJECUTAR YA |
| Ebook #3 Control Pélvico | **sin verificar** | 88 | 88 | 🟢 pero a ciegas |
| Almohada de Embarazo | 20 → **12** | **86** | 94 | 🟡 SEGUNDA OLA |
| **Ebook #1 Somáticos** | 19 → **8** | **82** | 93 | 🟡 SEGUNDA OLA |

**Lo que cambia la decisión:** el Ebook #1, que era el winner digital, se cae de la zona
de ejecutar. Y el **Ebook #2 Chau Pañal pasa a ser el digital #1** — es el único cuyo
hueco verifiqué de forma independiente y dio exacto, **y su ventana estacional está
abierta ahora**.

La Almohada Lumbar sigue siendo el winner físico en los dos escenarios.

### Fundamento de cada cambio

| Eje | De → a | Por qué |
|---|---|---|
| Lumbar, hueco | 19 → 17 | El producto específico sigue libre, pero 5 marcas arrancaron en 10 días en la categoría vecina |
| Embarazo, hueco | 20 → 12 | Existe una DTC con 716 días al aire. No es "0 marcas". Queda hueco de **ángulo** (el copy de Micolecho es genérico, no de dolor), no de categoría |
| Somáticos, hueco | 19 → 8 | La premisa del puntaje era falsable y se falsó: hay quien cobra en ARS con 169 días. Más 5 arranques en 15 días y el dominante ya clonado |
