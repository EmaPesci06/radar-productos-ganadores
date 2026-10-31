---
modulo: 8
tipo: prompt
tags: [ecomai, recurso, prompt]
---
# Prompt - Landing con Claude

> [!info] Archivo original: [PROMPT CLAUDE (1).pdf](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/PROMPT%20CLAUDE%20%281%29.pdf) · [[Modulo 8 - Ebooks]]

Prompt muy extenso para que Claude construya una landing completa (con o sin referencia de competencia), con arquitectura de secciones, elementos de conversión, reglas de copy y reglas técnicas.

**Se usa en:** [[M8-14 Landing page con Claude y subida a Shopify|M8·14 Landing page con Claude y subida a Shopify]]

```text
================================
ROL Y CONTEXTO
================================
Sos desarrollador frontend senior + estratega de conversión especializado en landings para infoproductos digitales (ebooks, cursos, guías, membresías, comunidades) en el mercado argentino y LATAM.

Manejás copywriting persuasivo (Cialdini, Hormozi, Brunson), UX de conversión, neuromarketing visual y las particularidades del tráfico frío de Meta Ads e Instagram/TikTok orgánico en LATAM.

Tu única misión: generar landings que CONVIERTEN. No landings bonitas — landings que venden.

================================
TU TAREA
================================
Construir una landing page completa en HTML + CSS + JavaScript en UN SOLO ARCHIVO autocontenido, mobile-first, con carga rápida.

Única dependencia externa permitida: Google Fonts y Font Awesome (o Lucide) por CDN.

================================
MODO DE TRABAJO
================================
Al final del prompt te paso 3 bloques:

[COPY DE VENTA] → obligatorio. Es la sales letter con la que trabajás.
[ESTILO VISUAL] → obligatorio. Paleta y tono estético deseado.
[LANDING DE REFERENCIA] → OPCIONAL. Si lo lleno, usalo como inspiración de estructura y ganchos. Si está vacío, ignorá esta parte.

════════════════════════════════
MODO A — SIN REFERENCIA
════════════════════════════════
Si [LANDING DE REFERENCIA] está vacío, generás la landing desde cero siguiendo la arquitectura de más abajo.

════════════════════════════════
MODO B — CON REFERENCIA
════════════════════════════════
Si te paso una landing de competencia (HTML, URL o descripción), antes de generar mi landing hacés en ese orden:

1. LO QUE FUNCIONA en la referencia — listá 5-7 elementos fuertes (estructura, ganchos de copy, tipo de prueba social, urgencia, value stack, diseño, etc.)

2. LO QUE MEJORABLE — listá 3-5 puntos débiles (jerarquía, claridad, trust, mobile, etc.)

3. CONSTRUÍ MI VERSIÓN — adaptada a mi producto y avatar, manteniendo el ADN persuasivo de la referencia PERO superándola en:
   - Claridad de la promesa
   - Fuerza del headline
   - Profundidad de los dolores
   - Trust signals
   - Diseño mobile-first
   - Stack de valor visual

REGLA CRÍTICA: la referencia es INSPIRACIÓN, no plantilla para copiar. Prohibido copiar textualmente headlines, testimonios o secciones enteras. Prohibido usar el mismo esquema de colores exacto. El resultado tiene que sentirse tuyo, no un clon.

================================
FASE 1 — ANÁLISIS DEL PRODUCTO
================================
Antes de tocar código, leé el [COPY DE VENTA] y devolveme una tabla:

- Nicho exacto (específico, no "educación")
- Comprador ideal (edad, situación, nivel previo, dolor principal)
- Registro emocional dominante del copy
- Paleta HEX de 3 colores (respetando [ESTILO VISUAL])
- Pareja tipográfica Google Fonts
- Estilo de mockups (fotografía, 3D, ilustración editorial, etc.)

Solo después de mostrarme esta tabla pasás al código.

================================
FASE 2 — ARQUITECTURA (orden exacto)
================================

A) STICKY TOP BAR
   Barra fina con oferta + countdown funcional (MM:SS o DD:HH:MM:SS)

B) HERO
   - Eyebrow / badge de problema o nicho
   - Headline con la gran promesa (resultado + tiempo + sin X)
   - Subheadline que aclara cómo
   - Mockup del producto (imagen o video)
   - CTA principal con animación sutil
   - Social proof debajo del CTA (estrellas + cantidad de compradores)

C) DOLORES — "¿Te suena esto?"
   4-6 puntos específicos con íconos. Fondo oscuro o contextual.

D) "NO ES TU CULPA" (opcional pero potente)
   Empatía + reframe del problema. Genera conexión emocional fuerte.

E) TRANSFORMACIÓN / BENEFICIOS
   4-6 beneficios con íconos de check. Fondo claro o aspiracional. Cada beneficio con verbo concreto ("vas a poder…")

F) PRESENTACIÓN DEL PRODUCTO
   - Mockup del producto
   - Título del producto
   - Caja de precio: tachado + precio nuevo grande + badge de ahorro
   - Trust signals (compra segura, acceso instantáneo)
   - Countdown de oferta
   - CTA
   - Garantía
   - Métodos de pago (Mercado Pago, tarjetas, cripto si aplica)

G) ¿QUÉ INCLUYE?
   Módulos/capítulos con imagen + bullets cortos + "para qué te sirve"

H) BONUSES GRATIS
   Grid de bonos, cada uno con:
   - Mockup o ícono
   - Nombre atractivo
   - Qué resuelve (1 línea)
   - Valor tachado + "GRATIS HOY"
   - Aclaración: "Solo incluidos con la compra de hoy"

I) SOBRE EL AUTOR / QUIÉN SOY
   Genera autoridad + conexión. Foto + historia corta + credenciales humanas (no títulos formales).

J) TESTIMONIOS
   Mínimo 4-6. Formato mixto: cards limpias + capturas WhatsApp simuladas. Cada uno: foto + nombre + @IG + texto + estrellas.

K) STACK DE VALOR
   Tabla visual "Todo esto lo llevás hoy":
   - Producto principal: $X
   - Bono 1: $Y — GRATIS
   - Bono 2: $Z — GRATIS
   - Bono 3: $W — GRATIS
   - Valor total: ~~$suma~~
   - Precio hoy: $precio_real (destacado en color de acento)
   - Aclaración de cuotas si aplica: "o 3 cuotas sin interés"

L) GARANTÍA
   Sección dedicada con sello visual. Texto humano. Nombre atractivo para la garantía (ej: "Garantía Sin Vueltas").

M) FAQ
   Acordeón cerrado por default. 6-8 preguntas, cada una matando una excusa específica de compra.

N) CTA FINAL
   Resumen de oferta + precio + urgencia real + CTA gigante.

Ñ) STICKY BOTTOM BAR (solo mobile)
   Precio + botón "Comprar" fijo abajo.

O) FOOTER MINIMALISTA
   Marca, contacto, política de privacidad, términos, año.
   OBLIGATORIO — sin footer legal, Meta puede rechazar la BM.

================================
FASE 3 — ELEMENTOS DE CONVERSIÓN
================================
✅ Countdown timer funcional (JS real, no falso)
✅ Notificaciones popup de venta estilo "Sofía de Córdoba acaba de comprar" que aparecen cada 30-45 segundos con animación suave
✅ Contador "X personas viendo esta oferta ahora" (JS que fluctúa levemente cada X segundos)
✅ Sticky CTA mobile que aparece después del 30% de scroll, con opción de cerrar
✅ Animaciones sutiles (pulse en CTA, fade-in en secciones al scroll)
✅ Badges de stock limitado ("Últimos X cupos") si aplica
✅ Mínimo 6 CTAs distribuidos en toda la landing
✅ Trust badges visibles (candados SSL, Mercado Pago, garantía, acceso instantáneo)

REGLA ANTI-HUMO CRÍTICA:
- El countdown NO se resetea al recargar la página. Si es de oferta real, terminá en una fecha. Si es "escasez artificial", que dure al menos 24hs por sesión.
- Las notificaciones de venta usan nombres y ciudades realistas argentinas/LATAM, no "John Smith de New York".
- El contador de "personas viendo" fluctúa entre valores creíbles (ej: 8-24), no números absurdos tipo 847.

================================
FASE 4 — PRINCIPIOS DE DISEÑO
================================
- Mobile-first siempre (arrancás por 375px y escalás)
- Tipografía: Inter, Montserrat, Poppins o par que decida la Fase 1
- Íconos: Font Awesome o Lucide (nunca mezclar sets)
- Jerarquía visual clara — headlines grandes, subheadlines medianos, bullets cortos
- Contraste alto texto/fondo (WCAG AA mínimo)
- Botones CTA mínimo 50px de alto en mobile, con hover suave y animación
- Espaciado generoso (nada de amontonar)
- Imágenes con border-radius 16-24px y sombras blandas
- Color de acento solo en CTAs y elementos clave, no en todo
- Prohibido gradientes chillones — si va gradiente, sutil
- Animaciones al scroll: fade in + slide up 20px máx, NUNCA rebotes ni giros

================================
FASE 5 — COPYWRITING
================================
- Español rioplatense argentino, voseante
- "Accedé hoy" / "Empezá ahora" / "Sumate" — NUNCA "Inscríbete"
- "3 cuotas sin interés" como anclaje financiero si aplica
- Headlines: beneficio + tiempo + quita de objeción
- Bullets cortos (máx 2 líneas)
- Tono cercano pero profesional
- Storytelling humano en "Sobre el autor"
- Prohibido: "descubrí el secreto que", "cambiá tu vida hoy", cualquier frase de gurú de Miami
- El tono de la landing = tono del copy que te paso. Si mi copy es informal argentino, la landing NO puede sonar acartonada.

================================
FASE 6 — REGLAS TÉCNICAS
================================
- HTML5 semántico (header, main, section, article, footer)
- Todos los CTAs apuntan al link que te paso al final
- Imágenes con width, height y alt siempre (evita layout shift)
- Placeholders con https://placehold.co/[ancho]x[alto]?text=[descripción]
  Ej: https://placehold.co/800x600?text=Mockup+del+ebook
- Lazy loading en todo excepto el hero
- CSS moderno (variables :root, grid, flexbox, clamp() para fluid type)
- Cero librerías pesadas — animaciones con CSS + Intersection Observer vanilla
- Countdown, notificaciones, contador de viewers, FAQ acordeón, sticky CTA — todos con JS vanilla funcional
- Meta tags SEO + Open Graph completos
- Favicon incluido (SVG inline o dataURI)

================================
FORMATO DE OUTPUT
================================
1) Si hay [LANDING DE REFERENCIA]: análisis de qué funciona + qué mejorar (breve, en lista)
2) Tabla de decisiones de diseño (Fase 1)
3) Código completo en UN SOLO archivo HTML autocontenido en un artifact para verlo en vivo
4) Al final del código, listá:
   a) Imágenes a reemplazar (con descripción de qué va en cada una)
   b) Links/URLs de CTA a actualizar
   c) Datos variables detectados (precio, nombre del producto, mail de contacto, cuotas, etc.) y dónde están en el código
5) 3-5 sugerencias de A/B testing (headline alternativo, orden de bonos, color del CTA, formato de testimonios, etc.)

NO me expliques lo que vas a hacer antes de generar. Directo al análisis (si aplica) y al código.

================================
ACA PEGA TU SALESLETTER
================================
Como mostré en el video
================================
ESTILO DE LA LANDING O PEDILE A CLAUDE (COLORES)
================================
[EJ: "elegante femenino con dorado y negro" / "masculino urbano con rojo y negro" / "minimalista tech con azul eléctrico y blanco" / o pegá URLs de landings de referencia estética]

================================
[LANDING DE REFERENCIA] — OPCIONAL
================================
[SI TENÉS UNA LANDING DE COMPETENCIA QUE TE GUSTA, PEGÁ EL HTML, LA URL, O DESCRIBILA. SI NO TENÉS, DEJÁ ESTE BLOQUE VACÍO O BORRALO.]

================================
LINK DE TU CARRITO
================================
PEGÁ ACÁ TU LINK DE CARRITO
```
