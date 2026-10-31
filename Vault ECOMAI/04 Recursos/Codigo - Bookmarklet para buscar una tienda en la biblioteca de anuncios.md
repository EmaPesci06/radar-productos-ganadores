---
modulo: 8
tipo: bookmarklet
tags: [ecomai, recurso, bookmarklet]
---
# Codigo - Bookmarklet para buscar una tienda en la biblioteca de anuncios

> [!info] Archivo original: [FAL.txt](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/FAL.txt) · [[Modulo 8 - Ebooks]]

Bookmarklet que, al clickearlo desde la página de una tienda o de un producto en Dropi, abre la Biblioteca de anuncios de Meta con la búsqueda de esa tienda ya armada.

**Se usa en:** [[M8-02 Buscar ofertas de ebooks con palabras clave|M8·2 Buscar ofertas de ebooks con palabras clave]] · [[M8-04 Instalar el bookmarklet FAL en el navegador|M8·4 Instalar el bookmarklet FAL en el navegador]]

## Qué hace

Es un bookmarklet: un marcador de navegador que ejecuta código JavaScript al clickearlo. Al activarlo sobre la página de una tienda, abre la Biblioteca de anuncios de Meta con una búsqueda de esa tienda:

- Si la página actual es de **Dropi** (`app.dropi...`), usa el último segmento de la URL (el nombre de la tienda/producto en la URL) como término de búsqueda.
- Si es cualquier otra página, usa el dominio de esa página (`window.location.hostname`) como término de búsqueda.

Con eso arma la URL de la Biblioteca de anuncios (`facebook.com/ads/library`, todos los países, todos los tipos de anuncio y de medio, estado "activos") y la abre en una pestaña nueva.

## Cómo instalarlo

1. Mostrá la barra de marcadores del navegador y creá un marcador nuevo (clic derecho → Agregar página, o "Agregar marcador").
2. Ponele un nombre, por ejemplo "Buscar en Ad Library".
3. En el campo de la URL/dirección, pegá el código original tal cual (empieza con `javascript:`), reemplazando lo que haya por defecto.
4. Guardalo. Para usarlo, entrá a la página de la tienda o al producto en Dropi y hacé clic en el marcador.

## Código original (para pegar como URL del marcador)

```text
javascript:(function()%7Bconst currentUrl %3D window.location.href%3B%0Alet tienda%3B%0A%0Aif (currentUrl.includes("app.dropi")) %7B%0A  const lastSegment %3D currentUrl.substring(currentUrl.lastIndexOf('%2F') %2B 1)%3B%0A  tienda %3D lastSegment.replace(%2F-%2Fg%2C ' ')%3B%0A%7D else %7B%0A  tienda %3D window.location.hostname%3B%0A%7D%0A%0Aconst url %3D %60https%3A%2F%2Fwww.facebook.com%2Fads%2Flibrary%2F%3Factive_status%3Dactive%26ad_type%3Dall%26country%3DALL%26q%3D%24%7Btienda%7D%26search_type%3Dkeyword_unordered%26media_type%3Dall%60%3B%0Awindow.open(url%2C '_blank')%3B%0A%7D)()
```

## Código decodificado (para leerlo)

```javascript
(function () {
  const currentUrl = window.location.href;
  let tienda;

  if (currentUrl.includes("app.dropi")) {
    const lastSegment = currentUrl.substring(currentUrl.lastIndexOf('/') + 1);
    tienda = lastSegment.replace(/-/g, ' ');
  } else {
    tienda = window.location.hostname;
  }

  const url = `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=${tienda}&search_type=keyword_unordered&media_type=all`;
  window.open(url, '_blank');
})();
```
