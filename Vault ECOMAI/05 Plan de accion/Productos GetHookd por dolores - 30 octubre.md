---
tags: [ecomai, producto-ganador, ranking, radar-ar, gethookd]
fecha: 2026-10-30
---
# Productos GetHookd por dolores (30/10/2026)

Relevado el 30/10/2026 con la cuenta Famecom. No repite productos del [[Top 10 productos ganadores]], del [[Top 15 productos ganadores - octubre]] ni de [[Productos nuevos GetHookd - 30 octubre]]. Cuando un producto se cruza con alguno de esos, lo aclaro.

## Cómo se buscó (lógica del vault)

| Paso | Regla del vault | Qué se hizo |
|---|---|---|
| 1. GetHookd | [[M2-02 Búsqueda con herramienta espía (recomendado)\|M2-02]] y [[M2-08 Elegir creativos ganadores con los filtros de Gethookd\|M2-08]]: buscar por **problema** y ordenar por **impresiones** | 10 problemas: constipation, bladder leaks, lower back pain, dry eyes, seniors mobility, swollen legs, acid reflux, noise sleep, sciatica y hot flashes. Filtros: **activos**, **100 a 500 anuncios por marca** (el piso laxo), Winning + Optimized, 1 anuncio por marca y orden "Most impressions". Después filtré a mano los de **30 días o más**. Salieron **724 resultados** (de 20 en seniors mobility a 130 en constipation); en cada búsqueda me quedé con los de 30 días o más y 100 anuncios o más |
| 2. Tienda de un solo producto | [[M2-03 Validar productos por la calidad del embudo de ventas\|M2-03]] | Saqué suplementos, cremas, parches, clínicas, cursos, electrónica (TENS, masajeadores, auriculares) y catálogos. En las ~25 candidatas que quedaron revisé la landing y el catálogo completo de la tienda |
| 3. Doc A rápido | [[Skill Claude - doc-a-validator]] | Dolor real y evergreen, efecto wow, margen, importación y que no sea commodity |
| 4. Semáforo AR | radar-adlibrary-ar, versión rápida | Meta Ad Library Argentina, anuncios activos, con términos en rioplatense |

> [!warning] Filtros que tuve que cambiar
> - **30 días como filtro de GetHookd** (`run-time=30`) junto con "1 anuncio por marca" devuelve **0 resultados**. Por eso los días se filtraron a mano: son los días del **anuncio más impreso** de cada marca.
> - **Sin el filtro de performance** la búsqueda se cuelga y devuelve 0. Por eso dejé Winning + Optimized, el estándar del vault.
> - **Variante "relief"**: la probé con "dry eye relief" y trajo 7 resultados, menos que "dry eyes". No sumó nada.
> - **Embudo**: no abrí 3-5 anuncios uno por uno en todas las marcas. Para confirmar que es una tienda de un producto revisé la **landing del anuncio y el catálogo completo de la tienda** (`/products.json`). Antes de comprar stock, abrir 3-5 anuncios del elegido.

> [!note] Cómo es la búsqueda
> Los 10 problemas traen sobre todo **suplementos**: de 724 resultados, unos 25 eran productos físicos de una tienda enfocada. Constipación, reflujo, sofocos y ojo seco son casi 100% cápsulas, tés y gotas. Lo que queda son **almohadas, soportes y accesorios de descanso**: es la misma familia que ya funcionó en los rankings anteriores.

---

## Ranking

Semáforo Meta AR: 🟢 casi sin anunciantes del producto · 🟡 algunos · 🔴 cancha ocupada. "Laxo" = la marca tiene entre 100 y 199 anuncios (debajo del rango ideal de 200 a 500).

| # | Producto | Problema | Marca afuera | Anuncios · días | Precio afuera | Wow | Meta AR | Semáforo |
|---|---|---|---|---|---|---|---|---|
| 1 | **Antifaz autocalentable para ojo seco** (descartable) | Ojo seco, vista cansada de pantalla | Lula Eye Mask (AU) | 144 (laxo) · 79 d | AUD 29,99 la caja de 5 · bundles AUD 72-93 | Medio: se abre y calienta solo | "antifaz térmico ojos": **1 anuncio** (una peluquería). "antifaz ojo seco": 0 | 🟢 |
| 2 | **Almohada para estenosis espinal / lumbar para dormir** | Lumbalgia, ciática, estenosis | Alignex Pro (DE/US) | 337 · 130 d | USD 59,90-60 · funda USD 14,95 · almohada de rodillas USD 27,95 | Medio: alivio al acostarse, se ve en el video | "almohada lumbar dormir": ~8 anuncios sueltos (Nuvia Comfort 2, Fisicaline 2) | 🟢 |
| 3 | **Sistema de cuña antirreflujo para adultos** | Reflujo y acidez de noche | MedCline (US) | 145 (laxo) · 71 d | USD 299-320 el sistema completo | Alto: cuña inclinada con hueco para el brazo, no te resbalás | "almohada reflujo adultos": **0**. "almohada reflujo": ~19, casi todo de bebé (Pequelú 7, FIRME 7) | 🟢 |
| 4 | **Respaldo lumbar para moto** | Dolor de espalda de motoqueros | MotoCush MotoSupport (AU) | 172 (laxo) · **214 d** | AUD 84,99 · upsells muñequera AUD 32 y cruise assist AUD 29 | Medio: se calza en el asiento y el piloto apoya la espalda | "respaldo moto": ~330, todo concesionarias y seguros. **Nadie vende el producto** | 🟢 |
| 5 | **Entrenador de piso pélvico para hombres** (sin electrodos ni inserción) | Pérdidas de orina en hombres (post-próstata) | Fortis Control Trainer (AU) | **374 · 176 d** (varias páginas al mismo landing) | AUD 79 (antes AUD 119) · caja discreta | Medio: "10 minutos por día" | "incontinencia hombre": 3 (un coach). "piso pélvico hombres": ~22, todo info o coaches, **ningún producto** | 🟢 |
| 6 | **Changuito de compras con estabilidad de andador** | Movilidad de adultos mayores | Strolee Stability Shopper (US) | 204 · **219 d** | USD 195 · accesorios USD 22-44 | Alto: changuito y andador en uno | "changuito andador": **0** | 🟢 |
| 7 | **Silla pelota ergonómica** (pelota con base y funda) | Lumbalgia por estar sentado | Bloon Paris (FR) | 370 · 170 d | USD 369-525 | Alto: diseño, se ve distinto en cualquier living | "silla pelota": ~88, ruido (novelas, ortopedias sueltas). **Ninguna marca DTC** | 🟢 |
| 8 | **Protector bucal antirronquidos** | Ronquidos / el ruido de la pareja al dormir | SnoreLessNow, Somnofit-S (US) | **451 · 124 d** | USD 149,99 · faja posicional USD 299 | Medio: se moldea a la boca | "antirronquidos": ~12 (Oxen Argentina 6, BRTH 2, una dental) | 🟡 |
| 9 | **Sábanas frescas para sofocos** (bambú) | Sofocos y sudor nocturno en la menopausia | CozyOnCozy (US) | **466 · 68 d** | USD 129,97 · fundas x2 USD 34,97 | Bajo-medio: tela fría al tacto | "sábanas frescas": ~140 de blanquerías. "sofocos": ~640, todo suplementos y médicos. **Nadie une las dos cosas** | 🟡 |
| 10 | **Faja lumbar magnética** | Lumbalgia y ciática | Sanatate Forte, "Centura Magnetica" (RO) · DealMate (US, 38 d) | 447 · 100 d (3 páginas) | RON 130 | Bajo | "faja magnética": ~6 | 🟢, pero tienda catálogo |
| 11 | **Asistente para levantarse** (manija de pie) | Movilidad de adultos mayores | MobilityPal Secure-Lift (US) | 143 (laxo) · 117 d | USD 69 | Medio | "ayuda para levantarse": ~740, todo ruido. **Ningún producto** | 🟢, pero tienda catálogo |
| 12 | **Aro de hula hula inteligente con peso** | Panza hinchada, constipación, movimiento | Infinity Hoop (US) | 154 (laxo) · 80 d | USD 49,99 · patas y estuche aparte | Alto | "aro inteligente": ~14, ruido | 🟡 (verificar MELI: es un producto muy visto) |
| 13 | **Corrector de postura** | Dolor de espalda alta | Corecare (US) | 107 (laxo) · 50 d | USD 64,90 | Bajo | "corrector de postura": ~87 (P G Shop 5, DEMA 3, Lummine 2, Farmacity) | 🔴 |

---

## Los 5 mejores

### 1. Antifaz autocalentable para ojo seco
- **Por qué**: Lula lleva 79 días escalando con una sola línea (antifaz de calor descartable, en cajas y bundles). Es un **consumible**: si funciona, vuelven a comprar. Es liviano, barato (Alibaba "steam eye mask" a centavos de dólar la unidad) y entra en courier.
- **Hueco AR**: en Meta **no lo vende nadie**. El ojo seco se lo trata con gotas; el ángulo *"20 minutos de calor y dejás de sentir arena en los ojos"* está libre.
- **Riesgo**: es descartable, así que el margen depende del pack (5, 10, 30). Chequear MELI antes (hay antifaces de gel genéricos).
- [Anuncio en GetHookd, 79 días](https://app.gethookd.ai/ads/143857316) · [landing](https://lulaeyemask.com.au/collections/all)

### 2. Almohada para estenosis / lumbar para dormir
- **Por qué**: Alignex le habla a un dolor muy puntual (estenosis espinal, espondilolistesis) con 337 anuncios y 130 días. Es una sola almohada con variantes por país (alemán e inglés).
- **Encaja** con la almohada de rodillas del [[Plan v2 - Almohada de rodillas AR]]: Alignex la vende como segundo producto (USD 27,95). Puede ser **la misma marca**.
- **Hueco AR**: unos 8 anuncios sueltos con "almohada lumbar". Fabricable en espuma local.
- [Anuncio en GetHookd, 130 días](https://app.gethookd.ai/ads/111350358) · [tienda](https://alignextechnology.com/)

### 3. Cuña antirreflujo para adultos
- **Por qué**: MedCline vende un "sistema" (cuña + almohada de cuerpo con hueco para el brazo) a **USD 299-320**. Es una sola línea de producto (reflujo y hombro).
- **Hueco AR**: con "almohada reflujo" solo aparecen **cuñas de bebé** (Pequelú). Para adultos: **0 anuncios**. El ángulo *"dormí sin que te suba el ácido, sin pastillas"* está libre.
- **Riesgo**: es voluminosa y cara de importar. Conviene **fabricarla en espuma en Argentina** (hay talleres de cuñas ortopédicas) y vender cuña + funda a un ticket alto.
- [Anuncio en GetHookd, 71 días](https://app.gethookd.ai/ads/151218439) · [landing](https://medcline.com/)

### 4. Respaldo lumbar para moto
- **Por qué**: es la marca **con más días al aire de toda la lista (214)**. Es una sola tienda con un producto y dos upsells.
- **Hueco AR**: Argentina tiene millones de motos y un ejército de **repartidores** (Rappi, PedidosYa, mensajería). En Meta "respaldo moto" solo trae concesionarias. **Nadie vende el producto.** Ángulo: *"8 horas arriba de la moto sin que te mate la cintura"*.
- **Opciones**: Alibaba "motorcycle driver backrest" (varios modelos universales) o un taller local de tapicería de motos.
- [Anuncio en GetHookd, 214 días](https://app.gethookd.ai/ads/136562017) · [landing](https://motocush.com/products/motosupport)

### 5. Entrenador de piso pélvico para hombres
- **Por qué**: Fortis pauta con **varias páginas distintas** (Fortis, David M, Susan, Pelvic Recovery) que llevan al mismo landing: 374 anuncios y 176 días. Es una tienda de un solo producto, con caja discreta y "sin electrodos, sin inserción, sin app".
- **Hueco AR**: con "piso pélvico hombres" solo aparecen coaches y médicos. **Ningún producto.** Es un dolor vergonzante: compra online sí o sí.
- **Riesgo**: confirmar qué mecanismo usa (parece un ejercitador de presión entre los muslos) y que no lo clasifiquen como producto médico. Copy sin promesas de cura.
- [Anuncio en GetHookd, 176 días](https://app.gethookd.ai/ads/132473201) · [landing](https://tryfortis.store/products/fortis-control-trainer)

## Los otros que pasaron

| # | Producto | Anuncio GetHookd | Landing | Nota |
|---|---|---|---|---|
| 6 | Changuito-andador Strolee | [219 días](https://app.gethookd.ai/ads/112175077) | [stroleecarts.com](https://stroleecarts.com/) | Gran producto, pero voluminoso y USD 195. Solo si aparece un fabricante local de changuitos |
| 7 | Silla pelota Bloon | [170 días](https://app.gethookd.ai/ads/112047498) | [bloon-paris.com](https://bloon-paris.com/collections/bloon) | Ticket muy alto afuera. En AR se puede armar con pelota de pilates + base + funda de tela |
| 8 | Protector antirronquidos Somnofit-S | [124 días](https://app.gethookd.ai/ads/115187065) | [snorelessnow.com](https://snorelessnow.com/) | Es el **mismo formato** que el protector para bruxismo (#1 del ranking anterior). Sirve como segundo ángulo de esa marca, no como producto aparte |
| 9 | Sábanas frescas CozyOnCozy | [68 días](https://app.gethookd.ai/ads/154031383) | [cozyoncozy.com](https://cozyoncozy.com/products/cozy-cooling-sheets) | Llega el verano. La sábana es commodity; el diferencial es el ángulo "sofocos" |
| 10 | Faja lumbar magnética | [100 días](https://app.gethookd.ai/ads/142261714) | [sanatateforte.ro](https://sanatateforte.ro/) | Tienda catálogo y promesa "magnética" sin sustento: riesgo de cuenta publicitaria |
| 11 | Asistente para levantarse MobilityPal | [117 días](https://app.gethookd.ai/ads/157520096) | [mobility-pal.com](https://mobility-pal.com/) | Catálogo de ayudas para mayores. Encaja como segundo producto de la manija para el auto (Top 10 #10) |
| 12 | Aro inteligente Infinity Hoop | [80 días](https://app.gethookd.ai/ads/145408877) | [infinityhoop.com](https://infinityhoop.com/) | Muy visto en MELI y TikTok. Verificar saturación antes |
| 13 | Corrector de postura Corecare | [50 días](https://app.gethookd.ai/ads/176083162) | [corecareshop.com](https://corecareshop.com/) | 🔴 en AR y ya está el corpiño postural en el Top 15 |

## Descartados en el camino

- **Tiendas catálogo** que pautan un producto con mucho volumen: Kariney y Colody (anillo de fascia masajeador, en las búsquedas de constipación), Flxibleed (silla de tai chi), Reemo, Sameo, Eydology y bunicio.ro.
- **Electrónica**: ReliveX y SmoothSpine (TENS/masajeadores), Mello (calor para cólicos, ya cubierto), SnugWell (almohada con calor y power bank), Vibit (botas de compresión), BedJet, Ozlo y Openhagen (auriculares para dormir), Mivourr (dispositivo íntimo).
- **Suplementos disfrazados**: Immority MoveOn (bebida con colágeno), Elvora (té) y casi todo constipación, reflujo, sofocos y ojo seco.
- **Ya cubiertos**: medias de compresión (Zippra/livia), cuñas y cunitas antirreflujo de bebé (Top 15 #13), ropa interior para pérdidas (Haven, Everdries, Jude: mercado maduro), antifaz con auriculares (Top 15 #8), almohadón ortopédico (Celinva y VogueHom = Top 10 #3), rodillera (Griqos = Top 15 #7), manija para el auto (Piventra = Top 10 #10).
- **Cursos**: Newmindstart "Sciatica Reset" (curso de ejercicios).

## Siguiente paso
1. **Mercado Libre** para el top 5 (no lo medí acá): publicaciones, vendidos y precio de "antifaz calor ojos", "almohada lumbar para dormir", "cuña antirreflujo adulto", "respaldo moto" y "ejercitador piso pélvico hombre".
2. Pasar el #1 o el #2 por el **doc-a-validator** completo. El #2 conviene evaluarlo junto con la almohada de rodillas, como una sola marca de descanso.
3. Antes de comprar stock: abrir 3-5 anuncios del elegido en GetHookd y confirmar el embudo completo.
