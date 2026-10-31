---
modulo: 8
tipo: prompt
tags: [ecomai, recurso, prompt]
---
# Prompt - Landing con Magic Patterns

> [!info] Archivo original: [PROMPT MAGICPATTERNS.pdf](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/PROMPT%20MAGICPATTERNS.pdf) · [[Modulo 8 - Ebooks]]

Prompt extenso equivalente al de Lovable pero adaptado a Magic Patterns, para construir la misma landing larga de venta a partir del copy del producto.

**Se usa en:** [[M8-13 Landing page con Lovable y Magic Patterns|M8·13 Landing page con Lovable y Magic Patterns]]

```text
PROMPT MAGICPATTERNS

Actuá como director de arte y estratega de conversión para infoproductos digitales. Combinás dos oficios: diseñás con criterio editorial premium (paleta, tipografía, jerarquía) y armás cada sección con la lógica de un copywriter de respuesta directa que sabe cuándo el visitante duda.

MISIÓN
Construir una landing larga (long-form sales page) para un producto digital, pensada para tráfico frío de Meta Ads en mobile. Hermosa Y que venda — no una cosa a costa de la otra.

==============================
FASE 1 — LECTURA DEL PRODUCTO
==============================
Antes de tocar HTML, leé el [COPY DE VENTA] del final y devolveme una tabla previa con:

- Nicho exacto (específico, no "educación")
- Comprador ideal (edad, situación, nivel previo, dolor principal)
- Registro emocional dominante (urgencia, calma, aspiración, escape, esperanza, bronca, etc.)
- Paleta HEX de 3 colores (primario, secundario, acento) alineada al registro emocional
- Pareja tipográfica Google Fonts (display para títulos + legible para cuerpo)
- Estilo de mockups (fotografía, 3D, ilustración editorial, glassmorphism, etc.)

Solo después de mostrarme esa tabla pasás al código.

==============================
FASE 2 — PRINCIPIOS DE DISEÑO
==============================
- Mobile first sin excusas — arrancás por mobile y escalás a desktop
- Jerarquía visual fuerte: en cada sección UN elemento domina
- Animaciones al scroll SUTILES: fade in + slide up de 20px máximo. Nada de rebotes, giros ni entradas dramáticas.
- Hover states suaves en todo lo clickeable
- Sombras blandas y modernas (nunca box-shadow duro)
- Aire generoso entre secciones (80-120px desktop, 48-64px mobile)
- Cards con border-radius 16-24px
- Sistema de íconos consistente (Lucide, Phosphor o equivalente). Nunca mezclar sets.
- Prohibido gradientes chillones — si va gradiente, sutil

==============================
FASE 3 — ARQUITECTURA DE LA PÁGINA
==============================
Construí las secciones en este orden exacto:

A) STICKY TOP BAR
   Barra fina arriba con oferta puntual. Color de acento como fondo.

B) HERO
   - Headline: promesa principal del copy
   - Subheadline: 1-2 líneas de para quién y en qué plazo
   - Mockup del producto (describir qué mostrar)
   - CTA primario grande
   - Micro-trust bar debajo: "Acceso inmediato · Pago seguro · Garantía 7 días"

C) IDENTIFICACIÓN DEL DOLOR
   3-5 escenas específicas con ícono al costado. Título tipo "¿Te suena esto?"

D) LA TRANSFORMACIÓN
   Antes vs después. Visual side-by-side o vertical. Emoción de esperanza, no hype.

E) BENEFICIOS
   Grid de 6-8 tarjetas. Cada una: ícono + título corto + 1-2 líneas con verbo concreto ("vas a poder…")

F) QUÉ INCLUYE
   Módulos o capítulos del producto. Formato lista o acordeón. Cada uno con "para qué te sirve" al costado.

G) PREVIEW DEL PRODUCTO
   Mockups reales: páginas del ebook, área de miembros, plantillas. Que se vea qué se está comprando, no solo la portada.

H) STACK DE VALOR + BONOS GRATIS
   Formato "Todo esto lo llevás hoy":
   - Producto principal: valor $X
   - 🎁 Bono 1: valor $Y — HOY GRATIS
   - 🎁 Bono 2: valor $Z — HOY GRATIS
   - 🎁 Bono 3: valor $W — HOY GRATIS
   - Valor total: ~~$suma~~
   - Precio hoy: $precio_real (destacado, en color de acento)

   Reglas para bonos:
   - Cada bono con tarjeta propia (mockup + nombre + qué resuelve)
   - Badge "GRATIS" o "INCLUIDO HOY" en color de acento
   - Precio original tachado + "GRATIS" al lado
   - Aclarar: "Solo incluidos con la compra de hoy"

I) GARANTÍA
   Sección con badge visual (escudo o sello). Texto humano, no legal. Nombre atractivo (ej: "Garantía Sin Vueltas").

J) TESTIMONIOS
   Grid de 6-9 testimonios. Foto + nombre + @IG + texto. Alternar formatos: algunos card limpia, algunos captura de WhatsApp simulada.

K) FAQ
   Acordeón cerrado por default. 8-10 preguntas, cada una matando una excusa específica de compra.

L) CIERRE FINAL
   Repetición del stack + CTA gigante + garantía + urgencia REAL (fecha o cupos, nunca countdown fake).

M) FOOTER
   Marca, contacto, política de privacidad, términos, año. Sin footer legal, Meta puede rechazar la cuenta publicitaria.

==============================
FASE 4 — ELEMENTOS DE CONVERSIÓN
==============================
- CTAs distribuidos: hero, después de beneficios, en el stack, en el cierre. Nunca 3 secciones seguidas sin CTA visible.
- Todos los CTAs del mismo color de acento — el visitante aprende visualmente qué es clickeable
- Trust badges antes del stack (Mercado Pago, SSL, garantía, acceso inmediato)
- Sticky CTA mobile que aparece DESPUÉS del hero, con opción de cerrar
- Micro-copy debajo de cada CTA: "Acceso inmediato · Sin suscripción · Garantía 7 días"
- Countdown SOLO si hay fecha real de fin. Prohibido countdown fake — Meta lo detecta y penaliza el ad.

==============================
FASE 5 — CONTENIDO
==============================
- 100% del texto sale del [COPY DE VENTA] del final
- Prohibido lorem ipsum
- Prohibido inventar cifras de resultados o testimonios
- Si falta contenido para alguna sección, generalo coherente y marcalo con comentario HTML:
      <!-- REEMPLAZAR CON REAL ANTES DE PUBLICAR -->
- El tono de la landing = tono del copy. Si el copy es informal argentino, la landing NO puede ser acartonada.

==============================
FASE 6 — REGLAS TÉCNICAS
==============================
- HTML5 semántico (header, main, section, article, footer)
- Todos los CTAs apuntan a: [LINK_CHECKOUT]
- Imágenes con width, height y alt siempre (previene layout shift)
- Lazy loading en todo excepto el hero
- CSS moderno (variables en :root, grid, flexbox, clamp() para tipografía responsive)
- Cero librerías pesadas — animaciones con CSS o Intersection Observer vanilla
- Meta tags SEO (title, description, og:image, og:title, og:description)
- Favicon incluido (SVG o dataURI)

==============================
FORMATO DE OUTPUT
==============================
1. Tabla de decisiones de diseño (Fase 1)
2. Código completo (HTML + CSS + JS mínimo en un solo archivo autocontenido)
3. 3-5 sugerencias de A/B testing al final (headline alternativo, orden de bonos, color del CTA, formato de testimonios, etc.)

==============================
COPY DE VENTA
==============================
[COPY DE VENTA]

==============================
LINK DEL CHECKOUT
==============================
[LINK_CHECKOUT]
```
