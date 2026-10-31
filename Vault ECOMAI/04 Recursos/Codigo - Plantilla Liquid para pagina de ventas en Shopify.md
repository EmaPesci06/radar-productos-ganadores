---
modulo: 8
tipo: codigo
tags: [ecomai, recurso, codigo]
---
# Codigo - Plantilla Liquid para pagina de ventas en Shopify

> [!info] Archivo original: [CODIGO.pdf](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/CODIGO.pdf) · [[Modulo 8 - Ebooks]]

Plantilla mínima de Liquid para una página de Shopify en blanco (sin header ni footer del tema), pensada para usar como página de ventas.

**Se usa en:** [[M8-14 Landing page con Claude y subida a Shopify|M8·14 Landing page con Claude y subida a Shopify]]

```liquid
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ page.title }}</title>
{{ content_for_header }}
<style>
  body { margin: 0; padding: 0; }
</style>
</head>
<body>
{{ page.content }}
</body>
</html>
```

## Cómo usarlo

- Guardá este archivo como plantilla de página con el nombre `page.paginadeventas.liquid` en el tema de Shopify.
- Asignale esa plantilla a la página que va a funcionar como landing/página de ventas, para que cargue en blanco (sin header ni footer del tema) y muestre solo el contenido de la página.
