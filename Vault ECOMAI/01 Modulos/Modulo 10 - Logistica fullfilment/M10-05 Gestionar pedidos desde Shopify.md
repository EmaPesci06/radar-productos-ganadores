---
modulo: 10
leccion: 5
titulo: "Gestionar pedidos desde Shopify"
duracion: "08:05"
conceptos: ["[[Fulfillment]]", "[[Bundle]]", "[[SKU]]"]
herramientas: ["[[Senydrop]]", "[[Shopify]]", "[[Andreani]]"]
tags: [ecomai, modulo-10, leccion]
---
# Gestionar pedidos desde Shopify

> [!info] [[Modulo 10 - Logistica fullfilment]] · Lección 5 de 8 · ⏱ 08:05 · [▶ Abrir video](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%2010%20-%20Logistica%20fullfilment/Video%205.mp4)

← [[M10-04 Gestionar pedidos desde Tiendanube]] · [[Modulo 10 - Logistica fullfilment|↑ Módulo 10]] · [[M10-06 Pagar Senydrop con USDT vía Binance]] →

## Resumen

Repite el mismo flujo de fulfillment de la clase anterior pero con una tienda en Shopify: cambiar al modo fulfillment, sincronizar productos y combos por SKU, exportar las órdenes en CSV y subirlas a Senydrop para procesarlas. Muestra también la protección contra duplicados y las dos formas de resolver el envío.

## Puntos clave

- Antes de procesar pedidos con Shopify hay que cambiar al modo fulfillment desde la solapa superior de Senydrop, lo que cambia el menú de herramientas disponibles [00:01]-[00:28].
- Igual que en Tiendanube, cada producto se sincroniza pegando su SKU de Senydrop en el campo Inventario → SKU de la ficha del producto en Shopify, y los combos se arman con los SKU separados por el signo más [00:53]-[02:20].
- Para procesar pedidos: se seleccionan las órdenes en Shopify y se usa el botón Exportar eligiendo pedidos seleccionados y formato CSV para Excel [02:45]-[03:14].
- Ese CSV se sube en Senydrop, en Pedidos → Shopify, arrastrándolo o seleccionándolo, y se le da a procesar reporte para que el sistema matchee las órdenes por SKU, incluidos los combos, que se desdoblan en productos independientes [03:14]-[04:09].
- Igual que con Tiendanube, hay dos caminos para el envío: pagar los envíos (Senydrop genera los rótulos de Andreani) o cargar etiquetas propias [04:09]-[04:34].
- El sistema no permite procesar dos veces la misma orden: si se vuelve a subir el mismo reporte, detecta que ya fue procesada y evita duplicados [05:29]-[05:56].
- Al cargar etiquetas propias, el sistema también avisa cuántas etiquetas detectó y cuántas son compatibles con las órdenes de Shopify, y solo gestiona las que matchean [05:56]-[07:10].
- El resto del proceso, empaquetado y despacho, queda a cargo de Senydrop una vez pagadas o cargadas las etiquetas [07:39]-[08:05].

## Conceptos y herramientas

**Conceptos:** [[Fulfillment]] · [[Bundle]] · [[SKU]]
**Herramientas:** [[Senydrop]] · [[Shopify]] · [[Andreani]]

## Transcripción

*Transcripción automática con Whisper large-v3. Puede tener errores en nombres propios o términos técnicos.*

**[00:01]** Bienvenidos a este nuevo vídeo donde vamos a ver cómo funciona la integración de Shopify con CineDrop pero para lo que es el servicio de fulfillment. En el vídeo anterior ya vimos cómo se gestiona para dropshipping pero esta vez vamos a hacer lo mismo para que se entienda cómo funcionaría para fulfillment. Si todavía no lo hiciste lo primero que deberíamos hacer es cambiar al modo fulfillment desde esta solapa aquí arriba y podemos ver cómo se nos cambia el menú con las herramientas que hacen al servicio de fulfillment.

**[00:28]** En vídeos anteriores ya vimos cómo darnos de alta en fulfillment, cómo cargar un producto, cómo avisar y notificar de ingresos y cómo hacemos los pedidos en Tiendanube, por lo cual ahora vamos a ver cómo hacer los pedidos pero con Shopify. Bien, si nosotros nos vamos a productos podemos ver que tenemos los mismos productos cargados que vimos con el ejemplo de Tiendanube. Tenemos la mochila y la riñonera con el SKU y el stock correspondiente.

**[00:53]** Bien, lo que voy a hacer es irme a Shopify y podemos ver como ya tenemos cargado la riñonera con un copy paste de título, descripción y multimedia para el ejemplo y también creamos la mochila y el combo que son justamente la mochila y la riñonera en modo de combo para que se entienda cómo se procesa esto. Bien, lo que tenemos que hacer es muy simple, vamos a ir a CineDrop y vamos a copiar los SKUs que tenemos en la sección. Voy a copiar el SKU de la mochila

**[01:22]** Voy a irme a Shopify, voy a irme a la mochila, y aquí abajo donde dice inventario vamos a poner SKU, vamos a pegar el SKU y vamos a guardarlo. Perfecto, una vez que queda guardado ya tenemos esta mochila sincronizada para el posterior proceso de ventas. Vamos a ir a la riñonera, copiamos el SKU y hacemos lo mismo con el producto. Vamos a la sección del SKU, la pegamos y la guardamos.

**[01:51]** De esta manera tenemos también este otro producto sincronizado y con el tema del combo es muy sencillo vamos a hacer lo mismo lo que ya conocen le va a sonar familiar vamos a copiar el código que ya teníamos de la riñonera vamos a agregarle un más y vamos a pegar el código de la mochila que nos hacía falta entonces de esta manera le indicamos cuando se haga la sincronización con CineDrop con los pedidos que los pedidos que tengamos con estas ventas

**[02:20]** El SKU1 y el SKU2 separados por un más le va a indicar que son dos artículos independientes. Ahora le vamos a dar un ejemplo cuando generemos un pedido. Vamos a guardar también y de esta manera ya tenemos este producto sincronizado como con dos artículos distintos, la mochila y la riñonera. Bien, de esta manera ya tenemos cargado y sincronizado nuestros productos de fulfillment en Shopify.

**[02:45]** Bien, yo para este caso tengo dos pedidos creados que es el 1001 y el 1002 con artículos de fulfillment. Podemos ver cómo tenemos la mochila y en el otra venta tenemos el combo, lo que sería la riñonera más la mochila. Bien, ¿cómo procesamos estas órdenes para SaniDrop? Es muy sencillo, tenemos que seleccionar, yo en este caso voy a seleccionar estas dos órdenes, pueden ser 100, 200, 40, la que te hagan falta procesar.

**[03:14]** Bien, yo para el caso voy a generar estas dos y voy a ir a la sección de este botón que dice exportar. Aquí me tira la página actual pero yo en este caso voy a seleccionar la que dice justamente que seleccione esos dos pedidos manuales. En exportar como voy a dejar la opción de csv para excel y simplemente vamos a darle al botón de exportar pedidos. Bien, esto nos va a generar un archivo csv el cual vamos a cargar en CineDrop. Vamos a ir a CineDrop

**[03:43]** Vamos a ir a la sección de pedidos y vamos a ir a la sección de Shopify. Acá directamente podemos arrastrar el archivo descargado o bien podremos hacer clic y seleccionarlo. Bien, vamos a ir al botón de procesar reporte y aquí podemos ver cómo efectivamente, como ya tenemos cargado nuestros SKUs dentro de nuestros productos, el sistema se encarga de sincronizar y machar correctamente las órdenes. Podemos ver que tenemos la 1001

**[04:09]** Y la 1002, como así también podemos ver cómo el combo está generando dos artículos independientes. Si vamos a la sección de pedidos y corroboramos que la orden que tenía el combo que es la 1002, podemos ver cómo efectivamente en SignDrop la 1002 generó los dos productos por separado. Bien, ahora lo que queda es seleccionarlas y ir a continuar. Acá tenemos dos opciones.

**[04:34]** En CineDrop puedes procesar tus ventas de full film ya sea pagando los envíos, lo cual nosotros vamos a procesar los rótulos de Andreani y los vamos a generar para que se puedan despachar, o bien puedes cargar tus propios rótulos. Yo en este caso vamos a dar ir por el ejemplo de pagar los envíos. Voy a seleccionar, vamos a poner ir a pagar y acá podemos ver un detalle de las órdenes que generamos, ver que correctamente están los productos que seleccionamos y podemos ver que ya podemos

**[05:04]** Realizar el pago. Genial, acabo de abonar las dos órdenes y ahora podemos ver cómo efectivamente aparecen en la sección de en curso. Una vez que aparecen en esta sección, eso significa que SenderUp ya está notificado de estos pedidos y va a proceder a despacharlos. El primer estado es pendiente y luego, cuando se pase a por enviar y enviado, se van a sincronizar automáticamente y vamos a obtener también el número de seguimiento correspondiente.

**[05:29]** Algo que cabe destacar es que si nosotros podríamos volver a procesar las mismas órdenes podríamos cargar de nuevo el mismo ssb procesarlas pero el sistema no nos va a permitir porque ya detecta que estas órdenes han sido procesadas con anterioridad porque bueno esto puede generar algún conflicto de no tener bien identificado a veces qué órdenes se procesó y cuáles no entonces de esta manera el sistema lo simplifica no permitiéndonos procesar duplicados de órdenes que ya han sido generadas buenísimo

**[05:56]** Ahora recapitulemos y vamos a hacer el mismo caso pero cargando etiquetas. En vez de pagarlas vamos a cargarla. Funciona muy parecido. El primer paso es ir a la sección de Shopify, vamos a seleccionar las órdenes que teníamos exportadas y procesar reporte. Bien, vamos a seleccionarlas y poner continuar. En lugar de seleccionar pagar envíos vamos a ir por la opción de cargar nuestras propias etiquetas.

**[06:21]** Bien, ustedes pueden ver que acá tengo un ejemplo de cómo sería una etiqueta válida. Podemos ver que tiene el número de interno. Yo dejé la 1001 y justamente también la 1002. También para el ejemplo generé una más que es 1003, que no la tenemos en el reporte, pero vamos a ver cómo funcionaría. Vamos a cargarla y una vez que tengamos el archivo vamos a darle a subir. Bien, el sistema nos indica que ha detectado en total tres etiquetas, como hemos visto hoy la 1001, 1002 y 1003.

**[06:50]** Pero las que son compatibles con Shopify son dos, justamente las que teníamos la 1001 y 1002 y nos indica que faltaría una. Justamente para este caso lo vamos a hacer así para que se entienda el concepto. Vamos a ir a pagar y lo que va a hacer el sistema es simplemente gestionar las órdenes que sí tengamos las etiquetas.

**[07:10]** Vamos a ver cómo nos genera un lote el cual si vamos a ingresar podemos ver que nada más contiene las dos hojas y un resumen de los pedidos de estas órdenes. Bien, ahora solamente quedaría abonarlas y continuar con el proceso. Perfecto y una vez más podemos ver como una vez que abonamos las órdenes automáticamente se transfieren en la sección de en curso en CineDrop lo cual esto indica que ya estas órdenes están listas para despachar.

**[07:39]** Bien, podemos ver también que podemos ver el lote que generó las etiquetas por si en algún momento necesitamos volver a recapitular o revisar qué etiquetas corresponden a estos pedidos. Así que eso ya es todo, el resto del proceso queda en manos de Cinerop, tanto el empaquetado, despachado y todo lo que tenga que ver con la gestión. Así que esto ha sido todo, espero que les sirva y cualquier duda pueden estar comunicándose con atención al cliente, el cual van a estar despejándose cualquier tipo de consulta.
