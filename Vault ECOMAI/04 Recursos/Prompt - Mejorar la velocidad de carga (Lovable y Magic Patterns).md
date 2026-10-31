---
modulo: 8
tipo: prompt
tags: [ecomai, recurso, prompt]
---
# Prompt - Mejorar la velocidad de carga (Lovable y Magic Patterns)

> [!info] Archivo original: [MEJORAR LA VELOCIDAD DE CARGA (LOVABLE_MAGICPATTERNS).pdf](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/MEJORAR%20LA%20VELOCIDAD%20DE%20CARGA%20%28LOVABLE_MAGICPATTERNS%29.pdf) · [[Modulo 8 - Ebooks]]

Prompt para optimizar la velocidad de carga de una landing ya construida en Lovable o Magic Patterns, sin cambiar nada visual: fuentes, CSS, JavaScript, orden del head e imágenes.

**Se usa en:** [[M8-13 Landing page con Lovable y Magic Patterns|M8·13 Landing page con Lovable y Magic Patterns]]

```text
PROMPT PARA MEJORAR LA VELOCIDAD DE CARGA (LOVABLE/MAGICPATTERNS)

Actuá como Performance Engineer que audita landings de infoproductos antes de mandarles tráfico pago. Tu único trabajo en este prompt es uno: hacer que esta página cargue en menos de 1.5 segundos en mobile 4G, SIN QUE EL USUARIO NOTE UN SOLO CAMBIO VISUAL.

Regla no negociable:
Cero cambios en diseño, copy, colores, tipografías, layout, orden de secciones, animaciones visibles o interacciones. Si abro la versión vieja y la nueva en dos pestañas al lado, tienen que ser idénticas. Todo lo que toques es motor, no carrocería.

Tráfico previsto: Meta Ads (Instagram + Facebook), 80% mobile, conexiones 4G promedio de Argentina/LATAM.

──────────────────────────────
BLOQUE 1 — TIPOGRAFÍAS
──────────────────────────────
- Google Fonts se cargan con el patrón preload + onload, NUNCA como <link> bloqueante en el head
- Toda URL de Google Fonts termina en &display=swap
- Cada font-family lleva su fallback de sistema al lado. Para sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif. Para serif: Georgia, 'Times New Roman', serif.
- Precargá con crossorigin="anonymous" el archivo de fuente más usado (el weight que aparece en el hero)

──────────────────────────────
BLOQUE 2 — CSS
──────────────────────────────
Sacá:
- Todos los comentarios
- Todo whitespace innecesario entre reglas
- Todo will-change en elementos sin animación activa
- Todo background-attachment:fixed (mata el scroll en mobile por repaint constante)
- transform:translateZ(0) y backface-visibility:hidden en elementos que no se animan

Sumá:
- Media query @media (prefers-reduced-motion: reduce) que desactive animaciones infinitas para usuarios que lo pidieron a nivel sistema

Sobre animaciones:
- Las que usan transform y opacity → dejalas, son GPU
- Las que animan propiedades de layout (width, height, top, left, margin, padding) → simplificalas o reemplazalas por transform

──────────────────────────────
BLOQUE 3 — JAVASCRIPT
──────────────────────────────
- Todo JS no crítico envuelto en DOMContentLoaded
- TODO listener de scroll, touchstart y touchend lleva { passive: true }
- Features no críticas (contadores, scroll reveal, parallax) inicializan dentro de requestIdleCallback con fallback setTimeout 200ms
- Cursor custom con requestAnimationFrame: desactivalo entero en touch con:
      if (navigator.maxTouchPoints > 0) return;
- IntersectionObserver: creá UNO solo y reusalo para todos los elementos, nunca uno por elemento
- Para scroll reveal usá: rootMargin: '0px 0px -40px 0px', threshold: 0.1

──────────────────────────────
BLOQUE 4 — ORDEN DEL <head>
──────────────────────────────
Reconstruilo exactamente en este orden (crítico para el Critical Rendering Path):

1. <meta charset>
2. <meta viewport>
3. <meta theme-color> con el color dominante del diseño
4. <title> + <meta name="description">
5. preconnect a todos los dominios externos que se usan (fonts.googleapis.com, fonts.gstatic.com, cdn.shopify.com, etc.)
6. dns-prefetch a dominios de pago (checkout, gateway) si aplica
7. preload de la imagen del hero con fetchpriority="high"
8. preload del archivo de fuente principal con crossorigin="anonymous"
9. Google Fonts en modo async (patrón del bloque 1)
10. CSS crítico inline (above the fold)

Todo lo demás va al final del <body>.

──────────────────────────────
BLOQUE 5 — IMÁGENES
──────────────────────────────
Primera imagen visible (hero):
- loading="eager"
- fetchpriority="high"
- decoding="sync"

Todo el resto:
- loading="lazy"
- decoding="async"

Toda imagen sin excepción:
- width y height explícitos en el HTML (previene CLS)
- O aspect-ratio en CSS si es responsive

Si son imágenes de Shopify CDN, sumale a la URL:
&width=[ancho_de_display]&quality=80&format=webp

──────────────────────────────
BLOQUE 6 — LAYOUT SHIFT
──────────────────────────────
- Elementos que aparecen dinámicamente (sticky bar, popups, banners de countdown) NO usan display:none. Usan visibility:hidden o transform:translateY(110%) para no correr el layout cuando aparecen
- Carruseles y sliders tienen min-height definido en el contenedor antes de que el JS inicialice

──────────────────────────────
QUÉ ME DEVOLVÉS
──────────────────────────────
El código completo optimizado, listo para reemplazar el actual. Mismo diseño exacto, motor nuevo.

Antes del código, hacé un checklist rápido confirmando qué de esta lista aplicaste y qué no aplicaba (ej: "no había background-attachment fixed que sacar"). Así sé que revisaste todo.
```
