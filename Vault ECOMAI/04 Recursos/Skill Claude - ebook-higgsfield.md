---
modulo: 8
tipo: skill
tags: [ecomai, recurso, skill]
---
# Skill Claude - ebook-higgsfield

> [!info] Archivo original: [ebook-higgsfield.skill](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/ebook-higgsfield.skill) · [[Modulo 8 - Ebooks]]

Skill de Claude para generar ebooks o infoproductos de calidad editorial usando Higgsfield: arma la estructura de páginas, genera los prompts de imagen para cada una y el script para ensamblar el PDF final.

**Se usa en:** [[M8-06 Crear tu ebook con Claude y con Higgsfield|M8·6 Crear tu ebook con Claude y con Higgsfield]]

> [!tip] Cómo instalarla
> En Claude (claude.ai) → Configuración → Capacidades → Skills → subí el archivo .zip/.skill original.

## Archivo: SKILL.md

**Nombre:** ebook-higgsfield · **Descripción:** Genera ebooks infoproducto profesionales de nivel editorial usando Higgsfield (Nano Banana Pro 2K) para crear cada página como imagen de alta calidad. Usar SIEMPRE que el usuario pida crear un ebook, infoproducto, PDF de patrones, guía visual, kit digital, libro de recetas, manual de instrucciones o cualquier producto digital con páginas visuales. También usar cuando el usuario mencione "prompts para ebook", "páginas para Higgsfield", "generar infoproducto", "kit de patrones", "ebook de [cualquier nicho]" o pida crear contenido visual para vender digitalmente. Esta skill produce prompts listos para pegar en Higgsfield Nano Banana Pro 2K que generan páginas de calidad revista, y también construye el PDF final ensamblando las imágenes.

## Skill: Generador de Ebooks con Higgsfield

### Qué hace esta skill

Genera ebooks infoproducto completos de calidad editorial. Cada página del ebook es una imagen
generada con Higgsfield Nano Banana Pro 2K — exactamente como el ebook brasileño de referencia
que supera los 59 anuncios activos en Meta Ads.

**Resultado:** PDF de nivel revista con fotos reales de producto, gráficos técnicos, tablas,
paso a paso visual y estrategia de venta — todo integrado como imagen por página.

---

### Flujo de trabajo obligatorio

#### PASO 1 — Relevamiento del nicho (siempre primero)

Antes de generar nada, obtener del usuario:

```
1. NICHO: ¿De qué trata el ebook? (crochet, cocina, fitness, carpintería, etc.)
2. AVATAR: ¿A quién le vende? (ama de casa, emprendedora, hobbyista, profesional)
3. PROMESA: ¿Qué resultado concreto obtiene quien compra?
4. PRODUCTO: ¿Cuántos patrones/recetas/ejercicios/capítulos tiene?
5. PRECIO: ¿Cuánto va a valer el ebook?
6. PALETA: ¿Colores de la marca? (si no tiene, sugerir según nicho)
7. NOMBRE: ¿Cómo se llama el ebook y la marca?
```

Si el usuario ya dio esta info en la conversación, extraerla directamente sin preguntar.

#### PASO 2 — Definir estructura del ebook

Cada ebook tiene esta arquitectura base (adaptar según nicho):

```
PORTADA (1 pág)
ÍNDICE + BIENVENIDA (2 págs)
[SEPARADOR CATEGORÍA] × cant. categorías (1 pág c/u)
[ÍTEM/PATRÓN/RECETA] × cantidad total:
  └── Pág 1/3: Presentación + foto producto
  └── Pág 2/3: Instrucciones paso a paso
  └── Pág 3/3: Gráfico/diagrama + aplicaciones/usos
SISTEMA DE NEGOCIO (3-5 págs) — si el ebook es para vender
CIERRE (1 pág)
```

#### PASO 3 — Generar prompts para Higgsfield

Para cada página generar un prompt siguiendo los templates de `/references/prompt-templates.md`.

**Regla de oro de los prompts:**
- Siempre especificar: `A4 vertical format, 2:3 ratio`
- Siempre incluir: `professional magazine quality, editorial layout`
- Siempre dar paleta de colores en hex
- Nunca más de 120 palabras por prompt
- Modelo siempre: `nano_banana_pro` resolución `2k`

#### PASO 4 — Ensamblar el PDF

Una vez que el usuario tiene las imágenes descargadas de Higgsfield:

```python
# Script base para ensamblar — ver /references/assembly-script.md
from PIL import Image
from pypdf import PdfWriter, PdfReader
import io

writer = PdfWriter()
for image_path in image_paths:  # lista de rutas en orden
    img = Image.open(image_path).convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="PDF", resolution=150)
    buf.seek(0)
    writer.add_page(PdfReader(buf).pages[0])

with open("ebook_final.pdf", "wb") as f:
    writer.write(f)
```

---

### Estructura de 3 páginas por ítem (universal)

Esta estructura funciona para CUALQUIER nicho. Adaptar el lenguaje pero mantener el esquema:

#### Página 1/3 — PRESENTACIÓN

**Componentes fijos (izquierda 40%):**
- Header con nombre de marca
- Badge numerado del ítem
- Título grande en 2-3 líneas
- Descripción corta (2-3 líneas)
- Ficha técnica con 5 datos clave (íconos)
- Box de precio/valor con color de acento

**Componentes fijos (derecha 60%):**
- Foto del producto/resultado terminado (generada con Higgsfield)
- Crédito de foto en pie

#### Página 2/3 — INSTRUCCIONES

**Componentes fijos (izquierda 40%):**
- Lista de materiales/ingredientes/herramientas numerada
- Box de abreviaturas/términos clave
- Medida/tiempo/porción final

**Componentes fijos (derecha 60%):**
- Miniatura de la foto (esquina superior)
- Pasos numerados en cards alternando colores (V1, V2... o Paso 1, Paso 2...)
- Box de acabado/consejo final

#### Página 3/3 — GRÁFICO + APLICACIONES

**Componentes fijos (izquierda 40%):**
- Diagrama técnico (ver tipos en references/)
- Leyenda de símbolos/colores
- Vistas frontal y lateral con medidas

**Componentes fijos (derecha 60%):**
- Tabla de variantes/talles/porciones
- 4 aplicaciones/usos/contextos de venta
- Box de precio con margen

---

### Paletas por nicho (referencias rápidas)

| Nicho | Principal | Acento | Fondo |
|-------|-----------|--------|-------|
| Crochet/tejido | #1A3A6B navy | #C8973A dorado | #F4F7FB |
| Cocina/repostería | #8B1A1A bordo | #F5A623 naranja | #FFF8EC |
| Fitness/yoga | #1A4A2E verde oscuro | #7EC8A4 verde claro | #F0F7F4 |
| Carpintería/DIY | #3D2B1F marrón | #D4A853 madera | #F5F0E8 |
| Belleza/skincare | #6B2D5E violeta | #F5C6D0 rosa | #FFF5F8 |
| Pet care | #1A3D6B azul | #FF8C42 naranja | #F0F7FF |
| Jardinería | #2D5A1B verde | #C8973A dorado | #F4F9F0 |
| Finanzas | #0A2540 azul marino | #00D4AA teal | #F0F8FF |

---

### Tipos de diagrama para Página 3/3 por nicho

**Crochet/tejido:** Esquema de puntos circular o rectangular con símbolos X
**Cocina:** Diagrama de montaje del plato, corte de ingredientes, temperaturas
**Fitness:** Diagrama corporal con músculos activados, ángulos de ejercicio
**Carpintería:** Plano técnico con medidas, cortes, ensamble
**Belleza:** Diagrama de aplicación, zonas del rostro, capas del producto
**Repostería:** Diagrama de capas del postre, decoración, temperaturas
**Jardinería:** Diagrama de plantación, espaciado, profundidad

---

### Reglas de calidad no negociables

1. **Nunca generar más de 6 prompts a la vez** — el usuario necesita tiempo para correrlos en Higgsfield
2. **Siempre empezar con 3 páginas de muestra** (1 ítem completo) antes del ebook completo
3. **Esperar aprobación** del usuario sobre el estilo visual antes de continuar
4. **Cada prompt debe ser autocontenido** — no referenciar otras páginas
5. **Incluir siempre el número de ítem** en el prompt para tracking
6. **Los textos en los prompts deben estar en el idioma del ebook** (español/portugués/inglés)

---

### Cómo manejar los créditos de Higgsfield

Nano Banana Pro 2K = **2 créditos por imagen**

Calcular siempre antes de empezar:
```
Total imágenes = (ítems × 3) + portada + separadores + sistema de negocio + cierre
Total créditos = total imágenes × 2
```

Informar al usuario antes de empezar para que recargue si es necesario.

---

### Archivos de referencia

- `/references/prompt-templates.md` — Templates de prompts por tipo de página y nicho
- `/references/nicho-examples.md` — Ejemplos completos de 3 páginas para 5 nichos distintos
- `/references/assembly-script.md` — Script Python completo para ensamblar PDFs
- `/references/quality-checklist.md` — Checklist de calidad antes de entregar el ebook

Leer el archivo de referencia relevante según la tarea específica.

## Archivo: references/prompt-templates.md

## Templates de Prompts para Higgsfield

### FORMATO BASE (aplicar siempre)

```
[TIPO DE PÁGINA], [DESCRIPCIÓN DEL LAYOUT], [CONTENIDO ESPECÍFICO],
[FOTO/IMAGEN PRINCIPAL], [PALETA DE COLORES], A4 vertical format 2:3 ratio,
professional magazine quality, editorial layout, [NOMBRE DE MARCA] brand
```

---

### PÁGINA 1/3 — PRESENTACIÓN

#### Template Universal Página 1/3

```
Editorial ebook page layout, professional [NICHO] pattern book, [TEMA/TEMPORADA].
LEFT SIDE (40%): white background, dark [COLOR PRINCIPAL] header bar at top with text
"[MARCA] · [AÑO/EDICIÓN]", [COLOR ACENTO] badge "[ÍTEM] [NÚMERO]", large bold title
"[NOMBRE DEL ÍTEM]" in [COLOR PRINCIPAL], description "[DESCRIPCIÓN 1-2 LÍNEAS]",
technical specs card with icons showing: [DATO 1], [DATO 2], [DATO 3], [DATO 4], [DATO 5],
[COLOR PRINCIPAL] price box with [COLOR ACENTO] text "[PRECIO]".
RIGHT SIDE (60%): full-height professional product photo of [DESCRIPCIÓN DEL PRODUCTO],
[DESCRIPCIÓN DEL CONTEXTO/FONDO/PROPS], soft natural lighting, commercial quality.
A4 vertical 2:3 ratio, magazine quality, clean minimal design,
[COLOR PRINCIPAL] [HEX], [COLOR SECUNDARIO] [HEX], [COLOR ACENTO] [HEX]
```

#### Ejemplo — Crochet

```
Editorial ebook page layout, professional crochet pattern book, Argentine Mundial 2026.
LEFT SIDE (40%): white background, dark navy header "LA MUNDIALERA · ARGENTINA 2026",
gold badge "PATRÓN 01", large bold title "LLAVERO PELOTA MUNDIALISTA" in dark navy,
description "Pelota tejida en celeste y blanco con argolla metálica. 6cm. Principiante.",
technical specs with icons: Nivel: Principiante, Medidas: 6cm diámetro, Hilo: Algodón Nro.4,
Aguja: 3.5mm, Tiempo: 45-60min, navy price box gold text "$4.500 ARS".
RIGHT SIDE (60%): full-height professional product photo of handmade crochet ball keychain
in light blue and white, metal keyring, white linen fabric, bamboo crochet hooks, natural light.
A4 vertical 2:3 ratio, magazine quality, navy #1A3A6B, sky blue #75AADB, gold #C8973A
```

#### Ejemplo — Cocina/Repostería

```
Editorial ebook page layout, professional baking recipe book, Argentine home baking collection.
LEFT SIDE (40%): white background, dark bordo header "DULCE ARGENTINA · COLECCIÓN 2026",
orange badge "RECETA 01", large bold title "ALFAJOR DE MAICENA CLÁSICO" in dark bordo,
description "El alfajor argentino de siempre. Suave, dulce y con dulce de leche generoso.",
technical specs with icons: Nivel: Fácil, Porciones: 24 unidades, Tiempo: 90 min,
Conservación: 5 días, Costo: $1.200 ARS, bordo price box orange text "$8.500 ARS el kit".
RIGHT SIDE (60%): professional food photography of homemade alfajores stacked on white plate,
powdered sugar dusting, dulce de leche visible between cookies, warm natural side lighting,
white marble background, rustic linen napkin. A4 vertical 2:3, magazine quality,
bordo #8B1A1A, orange #F5A623, cream #FFF8EC
```

#### Ejemplo — Fitness

```
Editorial ebook page layout, professional fitness guide, home workout collection.
LEFT SIDE (40%): white background, dark green header "ENTRENÁ EN CASA · PROGRAMA 8 SEMANAS",
light green badge "EJERCICIO 01", large bold title "SENTADILLA CON PESO CORPORAL" in dark green,
description "El ejercicio base de todo entrenamiento. Quema calorías y fortalece piernas y glúteos.",
technical specs with icons: Nivel: Principiante, Series: 3x15 reps, Descanso: 60 seg,
Músculos: Cuádriceps/Glúteos, Calorías: ~45 kcal, green price box teal text "SEMANA 1 · DÍA 1".
RIGHT SIDE (60%): professional fitness photo of woman doing perfect squat form, athletic wear,
home gym background, bright natural lighting, motivational aesthetic.
A4 vertical 2:3, magazine quality, dark green #1A4A2E, teal #7EC8A4, white #FFFFFF
```

---

### PÁGINA 2/3 — INSTRUCCIONES / RECETA / PASO A PASO

#### Template Universal Página 2/3

```
Editorial ebook page layout, [TIPO] instructions page, clean white background, A4 vertical.
TOP: dark [COLOR PRINCIPAL] header "[TÍTULO SECCIÓN] · [ÍTEM NÚMERO] · [NOMBRE ÍTEM]".
Small thumbnail photo of finished [PRODUCTO] top right corner.
LEFT COLUMN: [TIPO DE LISTA] with numbered circles: [ITEM 1], [ITEM 2], [ITEM 3], [ITEM 4],
[ITEM 5], [ITEM 6]. [TIPO GLOSARIO] box: [TÉRMINO 1]=[DEF], [TÉRMINO 2]=[DEF], [TÉRMINO 3]=[DEF].
RIGHT COLUMN: step by step numbered cards alternating [COLOR 1] and [COLOR 2]:
[PASO 1 descripción], [PASO 2 descripción], [PASO 3], [PASO 4], [PASO 5], [PASO 6],
[PASO 7], [PASO 8], [PASO 9]. Bottom [COLOR PRINCIPAL] "[TÍTULO FINAL]" completion box:
"[INSTRUCCIÓN FINAL]". Professional typography, [COLOR PRINCIPAL] and [COLOR ACENTO] scheme
```

#### Ejemplo — Crochet

```
Editorial ebook page layout, crochet recipe page, clean white background, A4 vertical.
TOP: dark navy header "RECETA TÉCNICA · PATRÓN 01 · LLAVERO PELOTA MUNDIALISTA".
Small thumbnail photo of finished crochet ball keychain top right.
LEFT COLUMN materials list numbered circles: 1.Hilo algodón celeste 15g, 2.Hilo blanco 10g,
3.Aguja 3.5mm, 4.Relleno fibra 10g, 5.Argolla metálica, 6.Packaging bolsita + tag.
Abbreviations box: pb=punto bajo, aum=aumento, dism=disminución, MR=anillo mágico.
RIGHT COLUMN step cards navy and gold alternating: V1 MR 6pb (6), V2 6 aum (12),
V3 *1pb 1aum* x6 (18), V4 *2pb 1aum* x6 (24), V5-V7 24pb rectas, V8 cambiar blanco 24pb,
V9 *2pb 1dism* x6 (18) rellenar, V10 *1pb 1dism* x6 (12), V11 6 dism cerrar.
Bottom navy ACABADO box: "Coser argolla firmemente. Esconder hebras."
Professional typography, navy and gold color scheme
```

#### Ejemplo — Repostería

```
Editorial ebook recipe page, baking instructions, clean white background, A4 vertical.
TOP: dark bordo header "RECETA TÉCNICA · RECETA 01 · ALFAJOR DE MAICENA".
Small thumbnail photo of finished alfajores top right.
LEFT COLUMN ingredients numbered circles: 1.Manteca 200g, 2.Azúcar impalpable 120g,
3.Maicena 300g, 4.Harina 100g, 5.Yemas 3 unidades, 6.Dulce de leche 400g.
KEY BOX: T°=temperatura, MP=molde plano, C.s.=cantidad suficiente.
RIGHT COLUMN step cards bordo and orange alternating: Paso 1 Batir manteca y azúcar hasta cremar,
Paso 2 Agregar yemas de a una integrando bien, Paso 3 Incorporar harina y maicena tamizadas,
Paso 4 Formar cilindro y refrigerar 30 minutos, Paso 5 Cortar rodajas de 1cm,
Paso 6 Hornear 160°C 12-15 min sin dorar, Paso 7 Enfriar completamente antes de rellenar,
Paso 8 Rellenar con dulce de leche generoso, Paso 9 Rebozar en coco rallado o glasé.
Bottom bordo CONSEJO box: "No hornear de más — la maicena debe quedar blanca."
Professional food styling typography, bordo and orange scheme
```

---

### PÁGINA 3/3 — GRÁFICO + APLICACIONES + VENTA

#### Template Universal Página 3/3

```
Editorial ebook page, [TIPO] chart and [APLICACIONES/USOS] page, A4 vertical, white background.
[COLOR ACENTO] header "GRÁFICO Y [SECCIÓN] · [ÍTEM NÚMERO] · [NOMBRE ÍTEM]".
LEFT COLUMN: [TIPO DE DIAGRAMA TÉCNICO] showing [DESCRIPCIÓN DEL DIAGRAMA],
[SÍMBOLOS/LEYENDA], [NÚMEROS/ETIQUETAS], [VISTAS ADICIONALES].
Below: [LEYENDA/REFERENCIAS] box with symbol explanations.
RIGHT COLUMN: table "[TÍTULO TABLA]" with rows [VARIANTE 1/datos], [VARIANTE 2/datos],
[VARIANTE 3/datos]. Section "4 [APLICACIONES/USOS/CONTEXTOS]" with icon cards:
[APP 1]/[APP 2]/[APP 3]/[APP 4].
Bottom [COLOR PRINCIPAL] price box "[PRECIO] · [MARGEN/BENEFICIO]".
Professional magazine quality, [COLOR PRINCIPAL] [HEX], [COLOR SECUNDARIO] [HEX], [COLOR ACENTO] [HEX]
```

#### Ejemplo — Crochet

```
Editorial ebook page, crochet chart and sales page, A4 vertical, white background.
Gold header "GRÁFICO Y VENTA · PATRÓN 01 · LLAVERO PELOTA".
LEFT COLUMN: crochet stitch diagram of sphere showing concentric circular rounds,
X symbols for single crochet, increase/decrease arrows, round numbers 1-11 on side.
Below front view and side view drawings of ball 6cm with keyring.
Legend: X=punto bajo, up-arrow=aumento, down-arrow=disminución.
RIGHT COLUMN: table MEDIDAS POR TALLE rows P=5cm/20g/35min, M=6cm/25g/45min, G=7cm/32g/60min.
Section 4 APLICACIONES DE VENTA icon cards: Llavero/Souvenir/Corporativo/Merchandising.
Bottom navy price box "$4.500 ARS · Margen 75%".
Navy #1A3A6B, sky blue #75AADB, gold #C8973A
```

#### Ejemplo — Cocina

```
Editorial ebook page, baking diagram and sales page, A4 vertical, white background.
Orange header "DIAGRAMA Y VENTA · RECETA 01 · ALFAJOR DE MAICENA".
LEFT COLUMN: cross-section diagram of alfajor showing layers: bottom cookie/dulce de leche
filling/top cookie/glazing coat, measurements and thickness labels, temperature diagram
showing 160°C oven icon, storage diagram showing 5-day shelf life.
Below: front view circle 5cm diameter, side view showing 2.5cm height.
Legend: color codes for each layer.
RIGHT COLUMN: table VARIANTES rows Mini=3cm/1 cda DDL, Clásico=5cm/2 cdas DDL,
Grande=7cm/3 cdas DDL. Section 4 FORMAS DE VENDER icon cards:
Por unidad/Caja x12/Kit regalo/Pedidos evento.
Bottom bordo price box "$8.500 ARS la caja x12 · Margen 70%".
Bordo #8B1A1A, orange #F5A623, cream #FFF8EC
```

#### Ejemplo — Fitness

```
Editorial ebook page, fitness diagram and workout page, A4 vertical, white background.
Teal header "DIAGRAMA Y RUTINA · EJERCICIO 01 · SENTADILLA".
LEFT COLUMN: anatomical body diagram showing muscles activated in squat: quadriceps/glutes
/hamstrings highlighted in teal green, correct posture angles marked 90°, back straight arrow,
knees tracking toes indicator, two-position diagram showing start and bottom position.
Below: common mistakes diagram showing wrong vs right form with red X and green checkmark.
RIGHT COLUMN: table PROGRESIÓN SEMANAL rows Semana 1=3x10 reps, Semana 2=3x12,
Semana 3=3x15, Semana 4=4x15. Section 4 VARIANTES icon cards:
Con peso/Con salto/En una pierna/Con banda. 
Bottom dark green box "PROGRAMA COMPLETO 8 SEMANAS · 3 días/semana".
Dark green #1A4A2E, teal #7EC8A4, light green background #F0F7F4
```

---

### PORTADA

#### Template Portada

```
Professional ebook cover design, [NICHO] themed, [NOMBRE EBOOK].
Dark [COLOR PRINCIPAL] background with subtle [TEXTURA/PATRÓN DECORATIVO].
Decorative circles and [ELEMENTO DECORATIVO NICHO] in darker shade of [COLOR PRINCIPAL].
[ELEMENTOS DECORATIVOS] scattered across background.
TOP: [COLOR ACENTO] text "[MARCA] PRESENTA".
CENTER: Large bold title "[LÍNEA 1 TÍTULO]" in white, "[LÍNEA 2 TÍTULO]" in [COLOR SECUNDARIO],
"[SUBTÍTULO]" in white bold, decorative [COLOR ACENTO] horizontal line.
[COLOR ACENTO] badge "[EDICIÓN/COLECCIÓN]".
Content preview box: 5 bullet points with icons listing main contents.
3 stat badges showing [NÚMERO 1] [LABEL], [NÚMERO 2] [LABEL], [NÚMERO 3] [LABEL].
Quote box: "[FRASE MOTIVACIONAL DEL NICHO]".
Bottom: "[MARCA] ® · [AÑO]" in muted [COLOR].
A4 vertical 2:3 ratio, premium editorial design, [COLOR PRINCIPAL] [HEX], [COLOR SEC] [HEX], [COLOR ACENTO] [HEX]
```

---

### SEPARADOR DE CATEGORÍA

#### Template Separador

```
Professional ebook category divider page, [NICHO] themed, full page.
Solid [COLOR DE CATEGORÍA] background with decorative circles in darker shade.
Scattered [ELEMENTO DECORATIVO] icons.
TOP stripes: alternating [COLOR SEC] and white horizontal stripes 20px tall.
BOTTOM stripes: same pattern.
Centered content:
"[NOMBRE EBOOK] · EDICIÓN [AÑO]" in [COLOR ACENTO] small caps.
"CATEGORÍA [LETRA/NÚMERO]" in white medium.
Giant decorative letter "[LETRA]" in [COLOR ACENTO] font size 200+.
"[NOMBRE DE CATEGORÍA]" in white large serif font.
"[NÚMERO] [tipo de ítems] · [NIVEL]" in [COLOR SEC].
List of [NÚMERO] items with [COLOR ACENTO] numbered circles and white text.
Bottom [COLOR ACENTO] badge "[RANGO DE PRECIOS]".
A4 vertical 2:3, [COLOR CATEGORÍA] [HEX], [COLOR ACENTO] [HEX], white
```

## Archivo: references/nicho-examples.md

## Checklist de Calidad y Ejemplos por Nicho

### CHECKLIST ANTES DE ENTREGAR PROMPTS AL USUARIO

#### Para cada prompt verificar:
- [ ] Especifica formato A4 vertical 2:3
- [ ] Incluye "professional magazine quality, editorial layout"
- [ ] Paleta de colores con códigos hex
- [ ] Número de ítem visible en el prompt
- [ ] Contenido en el idioma correcto del ebook
- [ ] Máximo 120 palabras
- [ ] Columna izquierda 40% / derecha 60% en Pág 1
- [ ] Miniatura de foto en Pág 2 (esquina superior derecha)
- [ ] Diagrama técnico específico para el tipo de pieza en Pág 3

#### Para el ebook completo verificar:
- [ ] Portada generada
- [ ] Separadores de categoría por cada grupo
- [ ] 3 páginas por ítem (no 2, no 4 — exactamente 3)
- [ ] Página 3 con diagrama DIFERENTE para cada tipo de ítem
- [ ] Sistema de negocio incluido si el ebook es para vender
- [ ] Página de cierre

---

### EJEMPLOS COMPLETOS POR NICHO

#### NICHO: MACRAMÉ

**Nombre ebook:** Kit Macramé Boho 2026 — 20 Diseños para Vender
**Avatar:** Artesana argentina 25-45 años que vende en ferias y redes
**Paleta:** Marrón tierra #5C3A1E · Beige #D4A853 · Crema #FFF8F0

**Prompts Patrón 01 — Colgante de Pared Boho:**

Pág 1/3:
```
Editorial ebook page layout, professional macrame pattern book, Argentine handcraft collection 2026.
LEFT SIDE (40%): white background, dark brown header "KIT MACRAMÉ BOHO · ARGENTINA 2026",
golden badge "PATRÓN 01", large bold title "COLGANTE DE PARED BOHO" in dark brown,
description "Diseño geométrico en macramé natural. Elegante, moderno y muy vendible.",
technical specs with icons: Nivel: Principiante, Medidas: 30x60cm, Hilo: Macramé 3mm,
Soporte: Rama de madera, Tiempo: 2-3 horas, brown price box gold text "$12.000 ARS".
RIGHT SIDE (60%): professional product photo of handmade macrame wall hanging, natural cotton cord,
geometric diamond pattern, wooden dowel, white wall background, warm natural lighting, boho aesthetic.
A4 vertical 2:3, magazine quality, brown #5C3A1E, gold #D4A853, cream #FFF8F0
```

Pág 2/3:
```
Editorial ebook page, macrame instructions, clean white background, A4 vertical.
TOP: dark brown header "INSTRUCCIONES · PATRÓN 01 · COLGANTE BOHO".
Small thumbnail top right. LEFT COLUMN materials: 1.Hilo macramé natural 3mm 40m,
2.Rama madera 35cm, 3.Tijera, 4.Cinta métrica, 5.Cepillo para flecos, 6.Packaging.
KNOTS BOX: NS=nudo simple, NCD=nudo de cabeza de alondra, NCH=nudo cuadrado horizontal.
RIGHT COLUMN steps brown and gold: Paso 1 Cortar 20 hebras de 200cm c/u,
Paso 2 Montar en rama con nudo cabeza de alondra, Paso 3 Primera fila nudos cuadrados,
Paso 4 Segunda fila nudos alternados, Paso 5 Crear rombo central con nudos diagonales,
Paso 6 Continuar patrón geométrico x4 filas, Paso 7 Fila de cierre nudos simples,
Paso 8 Cortar flecos a 15cm parejos, Paso 9 Peinar flecos con cepillo.
Bottom brown CONSEJO box: "Tensar parejo desde el inicio para resultado profesional."
```

Pág 3/3:
```
Editorial ebook page, macrame diagram and sales, A4 vertical, white background.
Gold header "DIAGRAMA Y VENTA · PATRÓN 01 · COLGANTE BOHO".
LEFT COLUMN: technical macrame diagram showing top-down view of knot pattern,
horizontal and diagonal lines indicating cord paths, knot symbols: square knots X,
half hitches /, lark's head O, row numbers 1-12 on side, color-coded sections for
pattern repetitions. Below: front view 30x60cm with measurement arrows,
side view showing 2cm thickness at knot points.
RIGHT COLUMN: table VARIANTES rows Pequeño=20x40cm/25m/1.5hs, Mediano=30x60cm/40m/3hs,
Grande=45x80cm/70m/5hs. Section 4 FORMAS DE VENDER: Decoración hogar/Regalo casamiento/
Foto sesión/Tienda online. Bottom brown "$12.000 ARS · Margen 75%".
Brown #5C3A1E, gold #D4A853, cream #FFF8F0
```

---

#### NICHO: REPOSTERÍA ARGENTINA

**Nombre ebook:** La Pastelería Argentina — 20 Clásicos para Vender
**Avatar:** Emprendedora gastronómica que vende tortas y pasteles desde casa
**Paleta:** Bordo #8B1A1A · Naranja #F5A623 · Crema #FFF8EC

**Prompts Receta 01 — Torta Rogel:**

Pág 1/3:
```
Editorial ebook page, professional baking recipe book, Argentine pastry collection.
LEFT SIDE (40%): white background, dark bordo header "LA PASTELERÍA ARGENTINA · COLECCIÓN 2026",
orange badge "RECETA 01", large bold title "TORTA ROGEL CLÁSICA" in dark bordo,
description "El postre argentino más icónico. Capas crujientes con dulce de leche y merengue.",
specs icons: Nivel: Intermedio, Porciones: 12, Tiempo total: 3 horas,
Conservación: 2 días, Precio venta: $18.000 ARS, bordo price box orange "$18.000 ARS".
RIGHT SIDE (60%): professional food photography of Torta Rogel, multiple crispy pastry layers,
dulce de leche between each layer, meringue topping with golden peaks, side view showing layers,
white cake stand, soft studio lighting, elegant pastry presentation.
A4 vertical 2:3, magazine quality, bordo #8B1A1A, orange #F5A623, cream #FFF8EC
```

---

#### NICHO: PLANTAS Y JARDÍN

**Nombre ebook:** Jardín en Casa — 20 Plantas Fáciles y Rentables
**Avatar:** Amante de las plantas que quiere vender esquejes y macetas
**Paleta:** Verde oscuro #2D5A1B · Verde claro #7EC86A · Tierra #C8973A

**Prompt Planta 01 — Pothos o Poto:**

Pág 1/3:
```
Editorial ebook page, professional plant guide, home gardening collection Argentina 2026.
LEFT SIDE (40%): white background, dark green header "JARDÍN EN CASA · GUÍA COMPLETA",
earth-tone badge "PLANTA 01", large bold title "POTHOS — LA INMORTAL" in dark green,
description "La planta más fácil de propagar y vender. Tolera cualquier condición y crece sola.",
specs icons: Dificultad: Muy fácil, Luz: Indirecta, Riego: Cada 10 días,
Propagación: Esquejes en agua, Precio esqueje: $1.500 ARS, green price box "$1.500 ARS".
RIGHT SIDE (60%): professional plant photography of healthy pothos in terracotta pot,
trailing vines with heart-shaped variegated leaves, bright indirect window light,
white wall background, cozy home aesthetic, plant parent lifestyle photo.
A4 vertical 2:3, magazine quality, dark green #2D5A1B, light green #7EC86A, earth #C8973A
```

---

#### NICHO: FITNESS EN CASA

**Nombre ebook:** 30 Días de Entrenamiento en Casa — Programa Completo
**Avatar:** Mujer 25-40 que quiere entrenar sin ir al gimnasio
**Paleta:** Verde oscuro #1A4A2E · Teal #7EC8A4 · Blanco #FFFFFF

**Prompt Ejercicio 01 — Burpee:**

Pág 1/3:
```
Editorial ebook page, professional fitness guide, home workout program 30 days.
LEFT SIDE (40%): white background, dark green header "ENTRENÁ EN CASA · 30 DÍAS",
teal badge "EJERCICIO 01", large bold title "EL BURPEE PERFECTO" in dark green,
description "El ejercicio más completo del programa. Trabaja todo el cuerpo en un solo movimiento.",
specs icons: Nivel: Intermedio, Series: 3x8-12 reps, Descanso: 90 seg,
Músculos: Cuerpo completo, Calorías: ~65 kcal/serie, green box teal text "SEMANA 1 · DÍA 2".
RIGHT SIDE (60%): professional fitness photography of woman doing burpee, athletic wear,
bright home gym, motivational poster wall, perfect form shown at squat position,
natural lighting, energetic and empowering aesthetic.
A4 vertical 2:3, magazine quality, dark green #1A4A2E, teal #7EC8A4, white #FFFFFF
```

---

### NICHOS ADICIONALES — REFERENCIAS RÁPIDAS

#### Carpintería/DIY
- Diagrama Pág 3: Planos técnicos con medidas, vista explosionada, lista de cortes
- Tip: Incluir nivel de dificultad en herramientas (no conocimiento)
- Fotos: Pieza terminada + detalle de ensamble + en contexto del hogar

#### Costura/Bordado
- Diagrama Pág 3: Patrón de corte a escala, tipos de puntadas, tabla de tallas
- Tip: Incluir cantidad de tela en metros, no en gramos
- Fotos: Prenda puesta en modelo + detalle de costuras + flat lay

#### Meditación/Bienestar
- Estructura diferente: 2 págs por práctica (descripción + guía visual)
- Diagrama: Diagrama corporal de posturas con puntos de atención
- Fotos: Persona en postura correcta, ambiente tranquilo, luz suave

#### Tejido con palillos (knitting)
- Igual que crochet pero con diagrama de puntos cuadrados (no puntos)
- Símbolos: loops, knit, purl, yarn over
- Paleta: más suave, tonos naturales lana

#### Cosmética natural
- Diagrama: Ingredientes con % y propiedades, proceso de mezcla
- Incluir: pH objetivo, temperatura de mezcla, tiempo de curado
- Fotos: Producto terminado en packaging premium, ingredientes naturales visibles

## Archivo: references/assembly-script.md

## Script de Ensamble PDF y Checklist Final

### SCRIPT PYTHON COMPLETO — ENSAMBLAR EBOOK

```python
#!/usr/bin/env python3
"""
Ensamblador de Ebook desde imágenes Higgsfield
Uso: python3 ensamblar_ebook.py --carpeta ./imagenes --salida ebook_final.pdf
"""

import os
import sys
import argparse
import io
from pathlib import Path

def ensamblar_ebook(carpeta: str, salida: str, dpi: int = 150):
    """
    Ensambla todas las imágenes de una carpeta en un PDF.
    Las imágenes se ordenan alfabéticamente — nombrarlas p01, p02, etc.
    """
    try:
        from PIL import Image
        from pypdf import PdfWriter, PdfReader
    except ImportError:
        print("Instalando dependencias...")
        os.system("pip install Pillow pypdf --break-system-packages -q")
        from PIL import Image
        from pypdf import PdfWriter, PdfReader

    # Extensiones válidas
    extensiones = {'.jpg', '.jpeg', '.png', '.webp'}
    
    # Obtener lista de imágenes ordenadas
    carpeta_path = Path(carpeta)
    imagenes = sorted([
        f for f in carpeta_path.iterdir()
        if f.suffix.lower() in extensiones
    ])
    
    if not imagenes:
        print(f"ERROR: No se encontraron imágenes en {carpeta}")
        return False
    
    print(f"Encontradas {len(imagenes)} imágenes. Ensamblando...")
    
    writer = PdfWriter()
    
    for i, img_path in enumerate(imagenes):
        print(f"  [{i+1}/{len(imagenes)}] {img_path.name}")
        
        try:
            img = Image.open(img_path).convert("RGB")
            buf = io.BytesIO()
            img.save(buf, format="PDF", resolution=dpi)
            buf.seek(0)
            reader = PdfReader(buf)
            writer.add_page(reader.pages[0])
        except Exception as e:
            print(f"  SKIP: Error procesando {img_path.name}: {e}")
            continue
    
    # Metadatos
    writer.add_metadata({
        "/Creator": "Higgsfield + La Mundialera Skill",
        "/Producer": "ebook-higgsfield skill v1.0",
    })
    
    with open(salida, "wb") as f:
        writer.write(f)
    
    size_mb = os.path.getsize(salida) / 1024 / 1024
    print(f"\n✅ PDF listo: {salida}")
    print(f"   Páginas: {len(imagenes)}")
    print(f"   Tamaño: {size_mb:.1f} MB")
    return True


def reemplazar_foto(pdf_base: str, pagina: int, foto: str, salida: str):
    """
    Reemplaza el placeholder de foto en una página específica del PDF.
    Útil para actualizar fotos sin regenerar todo el ebook.
    
    pagina: número de página (1-indexed)
    foto: ruta a la imagen nueva
    """
    from PIL import Image
    from pypdf import PdfWriter, PdfReader
    import io
    
    reader = PdfReader(pdf_base)
    writer = PdfWriter()
    
    for i, page in enumerate(reader.pages):
        if i + 1 == pagina:
            # Esta página se reemplaza con la foto nueva
            img = Image.open(foto).convert("RGB")
            buf = io.BytesIO()
            img.save(buf, format="PDF", resolution=150)
            buf.seek(0)
            new_reader = PdfReader(buf)
            writer.add_page(new_reader.pages[0])
        else:
            writer.add_page(page)
    
    with open(salida, "wb") as f:
        writer.write(f)
    print(f"✅ Página {pagina} reemplazada en {salida}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ensamblador de ebook desde imágenes Higgsfield")
    parser.add_argument("--carpeta", required=True, help="Carpeta con las imágenes")
    parser.add_argument("--salida", default="ebook_final.pdf", help="Nombre del PDF de salida")
    parser.add_argument("--dpi", default=150, type=int, help="Resolución del PDF (default: 150)")
    
    args = parser.parse_args()
    ensamblar_ebook(args.carpeta, args.salida, args.dpi)
```

---

### CONVENCIÓN DE NOMBRES DE ARCHIVOS

Para que el ensamble quede en el orden correcto, nombrar las imágenes así:

```
p001_portada.png
p002_indice.png
p003_bienvenida.png
p004_cat_A.png          ← separador categoría A
p005_patron01_pag1.png
p006_patron01_pag2.png
p007_patron01_pag3.png
p008_patron02_pag1.png
...
p091_sistema_negocio_1.png
p092_sistema_negocio_2.png
p093_cierre.png
```

---

### CALCULADORA DE CRÉDITOS HIGGSFIELD

```
Nano Banana Pro 2K = 2 créditos por imagen

FÓRMULA:
total_páginas = (ítems × 3) + 1 portada + cant_categorías + cant_págs_sistema + 1 cierre
total_créditos = total_páginas × 2

EJEMPLOS:
- Ebook 10 ítems, 2 categorías, 3 págs sistema = (30 + 1 + 2 + 3 + 1) × 2 = 74 créditos
- Ebook 20 ítems, 4 categorías, 3 págs sistema = (60 + 1 + 4 + 3 + 1) × 2 = 138 créditos
- Ebook 30 ítems, 5 categorías, 5 págs sistema = (90 + 1 + 5 + 5 + 1) × 2 = 204 créditos
```

---

### CHECKLIST FINAL DE CALIDAD

#### Antes de entregar al cliente:

**Estructura:**
- [ ] Portada profesional con nombre de marca visible
- [ ] Índice o tabla de contenidos
- [ ] Bienvenida personalizada
- [ ] Separadores de categoría (si aplica)
- [ ] 3 páginas por ítem SIN EXCEPCIÓN
- [ ] Sistema de negocio / consejos de venta
- [ ] Página de cierre con CTA

**Visual:**
- [ ] Paleta de colores consistente en TODAS las páginas
- [ ] Nombre de marca en header de cada página
- [ ] Numeración de páginas visible
- [ ] Diagrama diferente para cada tipo de ítem (no copiar el mismo)
- [ ] Foto del producto en cada Pág 1/3 (real o placeholder premium)

**Contenido:**
- [ ] Datos técnicos correctos y consistentes
- [ ] Precios de venta sugeridos incluidos
- [ ] Márgenes calculados correctamente
- [ ] Sistema de negocio con 3 escenarios de ganancia
- [ ] Garantía mencionada

**Técnico:**
- [ ] PDF ensamblado en orden correcto
- [ ] Resolución 150 DPI mínimo
- [ ] Tamaño final menor a 50MB
- [ ] Nombre de archivo profesional (no "ebook_v3_final_DEFINITIVO.pdf")
