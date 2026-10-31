---
modulo: 8
tipo: codigo
tags: [ecomai, recurso, codigo]
---
# Codigo - Link directo al carrito de Shopify

> [!info] Archivo original: [CARRITO.pdf](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/CARRITO.pdf) · [[Modulo 8 - Ebooks]]

Formato de link para agregar un producto directo al carrito de Shopify desde afuera de la tienda, y cómo encontrar el ID de la variante agregando .xml a la URL del producto.

**Se usa en:** [[M8-13 Landing page con Lovable y Magic Patterns|M8·13 Landing page con Lovable y Magic Patterns]] · [[M8-14 Landing page con Claude y subida a Shopify|M8·14 Landing page con Claude y subida a Shopify]]

```text
AGREGAR:

.xml

COMPLETAR:

https://DOMINIO/cart/add?id=NUMEROVARIANTE&quantity=1
```

## Cómo usarlo

- Agregá `.xml` al final de la URL del producto en tu tienda (ej. `https://tudominio.com/products/tu-producto.xml`) para ver el ID de cada variante.
- Reemplazá `DOMINIO` por el dominio real de tu tienda y `NUMEROVARIANTE` por el ID de variante que encontraste.
- El link resultante agrega ese producto directo al carrito y sirve para botones de compra directa (por ejemplo, desde un anuncio o una landing externa).
