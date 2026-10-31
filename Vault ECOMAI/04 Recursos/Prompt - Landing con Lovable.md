---
modulo: 8
tipo: prompt
tags: [ecomai, recurso, prompt]
---
# Prompt - Landing con Lovable

> [!info] Archivo original: [PROMPT  LOVABLE.pdf](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/PROMPT%20%20LOVABLE.pdf) · [[Modulo 8 - Ebooks]]

Prompt extenso para construir en Lovable una landing larga de venta a partir del copy del producto, con arquitectura de secciones, reglas de diseño y de conversión.

**Se usa en:** [[M8-13 Landing page con Lovable y Magic Patterns|M8·13 Landing page con Lovable y Magic Patterns]]

```text
PROMPT LOVABLE

Actuá como director de arte y estratega de conversión para infoproductos digitales. Combinás dos oficios: diseñás con criterio de revista premium, y armás cada sección con la lógica de un copywriter de respuesta directa.

Tu tarea:
Construir una landing larga (long-form sales page) para un producto digital, pensada para recibir tráfico frío de Meta Ads en mobile. La página tiene que ser hermosa Y vender — no una cosa a costa de la otra.

──────────────────────────────
FASE 1 — LECTURA DEL PRODUCTO
──────────────────────────────
Antes de tocar HTML, analizá el copy de venta que te paso al final y extraé:

- Nicho exacto (no "educación", sino "cursos de ebooks para principiantes en LATAM")
- Comprador ideal (edad, situación económica, nivel previo, dolor principal)
- Registro emocional dominante del copy (urgencia, calma, aspiración, bronca contra el sistema, promesa de escape, etc.)

En base a eso, decidís el sistema visual:

- Paleta de 3 colores en HEX (primario, secundario, acento) coherente con el registro emocional
- Pareja tipográfica de Google Fonts (una display para títulos, una legible para cuerpo)
- Estilo de mockups e ilustraciones (fotografía, 3D, ilustración editorial, glassmorphism, etc.)

Mostrame estas decisiones al principio del output, antes del código.

──────────────────────────────
FASE 2 — PRINCIPIOS DE DISEÑO
──────────────────────────────
- Mobile first sin excusas (arrancás diseñando el mobile y escalás a desktop, no al revés)
- Jerarquía visual fuerte: en cada sección hay UN elemento que domina
- Animaciones al scroll sutiles (fade in + slide up de 20px máximo, nada de rebotes ni giros)
- Hover states suaves en todo lo clickeable
- Sombras blandas y modernas (nunca box-shadow duro tipo 2015)
- Aire generoso entre secciones (padding vertical grande, 80-120px en desktop)
- Componentes tipo card con border-radius de 16-24px
- Ícon system consistente (Lucide, Phosphor o equivalente, no mezclar)

──────────────────────────────
FASE 3 — ARQUITECTURA DE LA PÁGINA
──────────────────────────────
Construí las secciones en este orden exacto:

1. STICKY TOP BAR
   Barra fina arriba con oferta puntual (ej: "Promo termina hoy" o "50% off por lanzamiento"). Fondo del color de acento.

2. HERO
   - Headline: la promesa principal extraída del copy
   - Subheadline: 1-2 líneas que aclaran para quién y en qué plazo
   - Mockup del producto (placeholder — describí qué mostrar)
   - CTA primario grande
   - Micro-trust bar debajo del CTA (3 elementos tipo "Pago seguro | Garantía 7 días | Acceso inmediato")

3. IDENTIFICACIÓN DEL DOLOR
   Sección donde el visitante se ve reflejado. 3-5 escenas específicas con íconos o ilustraciones al costado. Título tipo "¿Te suena esto?"

4. LA TRANSFORMACIÓN (antes vs después)
   Visual side-by-side o vertical mostrando cómo cambia la vida del comprador después de aplicar el producto. Emoción de esperanza, no de hype.

5. BENEFICIOS
   Grid de 6-8 tarjetas. Cada una: ícono + título corto + 1-2 líneas de qué gana el comprador. Redactar con "vas a poder…" + verbo concreto.

6. QUÉ INCLUYE (contenido del producto)
   Módulos, capítulos o unidades del producto. Formato lista o acordeón. Cada módulo con su valor implícito.

7. PREVIEW DEL PRODUCTO
   Mockups reales del producto (interfaces, páginas del ebook, screenshots del área de miembros, etc.). Que se vea qué está comprando.

8. STACK DE VALOR + BONOS
   Presentación tipo "Todo esto lo llevás hoy":
   - Producto principal: valor X
   - Bono 1: valor Y — HOY GRATIS
   - Bono 2: valor Z — HOY GRATIS
   - Bono 3: valor W — HOY GRATIS
   - Valor total si se comprara por separado: suma de todo
   - Precio hoy: precio real (visualmente destacado, mucho más chico que el valor total)

   Reglas visuales para los bonos:
   - Cada bono se presenta como si fuera un producto independiente, con su propia tarjeta (imagen o mockup + nombre + qué resuelve)
   - En cada tarjeta de bono va un badge visual tipo "GRATIS" o "INCLUIDO HOY" en el color de acento, tachando visualmente el precio original
   - Formato del precio: <span style="text-decoration: line-through">$15.000</span> <strong>GRATIS</strong>
   - Los bonos NO se venden por separado en la página — son exclusivos de esta compra. Aclararlo con una línea del tipo "Solo disponibles hoy junto al producto principal"

   Framing psicológico del stack:
   El comprador tiene que sentir que si compra hoy se lleva todo por mucho menos de lo que vale. La suma de valor total tiene que ser claramente mayor al precio final — realista, no inflada (ver bloque de reglas anti-humo).

9. GARANTÍA
   Sección con badge visual (ícono de escudo o sello). Texto humano de la garantía, no legal. Nombre atractivo para la garantía.

10. TESTIMONIOS
    Grid de 6-9 testimonios. Foto + nombre + @ de Instagram + texto. Alternar formatos (algunos card, algunos captura de WhatsApp simulada).

11. FAQ
    Acordeón cerrado por default. 8-10 preguntas cada una atacando una excusa específica de compra.

12. CIERRE FINAL
    Repetición del stack de valor + CTA gigante + recordatorio de la garantía + urgencia real (no falsa).

13. FOOTER
    Mínimo: nombre de la marca, contacto, links legales (política de privacidad, términos), año actual.

──────────────────────────────
FASE 4 — ELEMENTOS DE CONVERSIÓN
──────────────────────────────
- CTAs distribuidos: hero, después de beneficios, en el stack, y en el cierre. Nunca dejes 3 secciones sin un CTA visible.
- Todos los CTAs con el mismo color de acento — el visitante aprende visualmente qué es clickeable
- Trust badges antes del stack de valor (Mercado Pago, SSL, garantía, acceso inmediato)
- Countdown real solo si hay una oferta real que termina. Prohibido countdown fake que se resetea.
- Micro-copy debajo de cada CTA: "Acceso inmediato — Sin suscripción — Garantía 7 días"
- Sticky CTA en mobile que aparece después del hero (que no tape contenido, con transición suave)

──────────────────────────────
FASE 5 — CONTENIDO
──────────────────────────────
Sacá el 100% del texto del copy que te paso al final. Prohibido lorem ipsum. Prohibido inventar cifras de resultados.

Si el copy no cubre alguna sección (por ejemplo, no hay testimonios todavía), generá contenido persuasivo coherente con el resto y marcalo con un comentario HTML tipo <!-- REEMPLAZAR CON REAL --> para que el usuario sepa qué falta cambiar antes de publicar.

──────────────────────────────
FASE 6 — REGLAS TÉCNICAS
──────────────────────────────
- HTML5 semántico (header, main, section, article, footer)
- Todos los CTAs apuntan a: [LINK_CHECKOUT]
- Imágenes con width, height y alt siempre
- Lazy loading en todo lo que no sea el hero
- CSS moderno (variables CSS en :root, grid, flexbox, clamp() para tipografías responsive)
- Cero librerías pesadas — animaciones con CSS o Intersection Observer vanilla
- Meta tags SEO básicos (title, description, og:image, og:title)

──────────────────────────────
FORMATO DE OUTPUT
──────────────────────────────
1. Primero: las decisiones de diseño (nicho detectado, comprador, registro emocional, paleta HEX, tipografías, estilo visual)
2. Después: el código completo (HTML + CSS + JS mínimo) en un solo archivo autocontenido
3. Al final: 3-5 sugerencias de qué probar en A/B testing (headline alternativo, orden de bonos, color del CTA, etc.)

──────────────────────────────
COPY DE VENTA
──────────────────────────────
[COPYDEVENTA]

──────────────────────────────
LINK DEL CHECKOUT
──────────────────────────────
[LINK_CHECKOUT]
```
