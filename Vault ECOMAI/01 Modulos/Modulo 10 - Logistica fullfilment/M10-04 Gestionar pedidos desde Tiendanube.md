---
modulo: 10
leccion: 4
titulo: "Gestionar pedidos desde Tiendanube"
duracion: "09:25"
conceptos: ["[[Fulfillment]]", "[[Envíos]]", "[[Bundle]]", "[[SKU]]"]
herramientas: ["[[Senydrop]]", "[[Tiendanube]]", "[[Andreani]]"]
tags: [ecomai, modulo-10, leccion]
---
# Gestionar pedidos desde Tiendanube

> [!info] [[Modulo 10 - Logistica fullfilment]] · Lección 4 de 8 · ⏱ 09:25 · [▶ Abrir video](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%2010%20-%20Logistica%20fullfilment/Video%204.mp4)

← [[M10-03 Notificar ingresos de stock al depósito]] · [[Modulo 10 - Logistica fullfilment|↑ Módulo 10]] · [[M10-05 Gestionar pedidos desde Shopify]] →

## Resumen

Explica cómo procesar en Senydrop los pedidos de una tienda en Tiendanube ya integrada, una vez que el pago figura aprobado. Muestra las dos formas de resolver el envío (pagarle las etiquetas a Senydrop o cargar etiquetas propias), cómo se interpretan los combos y cómo se sincroniza automáticamente el estado y el número de seguimiento entre Senydrop y la tienda.

## Puntos clave

- Antes de este paso hay que tener: alta en fulfillment, productos cargados con SKU sincronizado, ingreso de stock notificado y aprobado, y la integración de Senydrop con Tiendanube ya hecha [00:02]-[01:00].
- En Senydrop → Fulfillment → Envíos → Tiendanube aparecen dos opciones: pagar envíos (Senydrop gestiona y cobra las etiquetas de Andreani) o cargar etiquetas propias (sin cobro de gestión) [01:00]-[01:57].
- Para que una orden aparezca en Senydrop, su pago tiene que figurar como aprobado o recibido en Tiendanube; si está pendiente de pago no se la toma [01:57]-[02:27].
- Se pueden seleccionar todas las órdenes o una por una antes de pagar el envío; el checkout de Senydrop muestra el detalle de productos y el costo del servicio de fulfillment por cada orden [02:27]-[03:32].
- Los combos se identifican correctamente: una orden con un SKU compuesto (ej. mochila más riñonera) se despliega como dos productos separados dentro de Senydrop [03:32]-[03:59].
- Una vez pagadas, las órdenes pasan a envíos en curso con estado pendiente; el estado se sincroniza solo, de pendiente a por enviar y de por enviar a enviado, con el número de seguimiento cargado automáticamente en Senydrop y en la tienda [03:59]-[04:55].
- Alternativa: cargar etiquetas propias ya generadas, con el requisito de que el número interno de cada etiqueta coincida con el ID del pedido en Tiendanube [04:55]-[05:46].
- Al subir el archivo de etiquetas, el sistema avisa cuántas detectó y cuántas matchean con pedidos reales de Tiendanube; si sobra o falta alguna, avisa y sigue solo con las que matchean [05:46]-[06:45].
- Con etiquetas propias el costo de envío figura en cero (porque ya se pagó aparte) y solo se cobra el servicio de fulfillment; el resumen de pago trae un lote descargable en PDF con todas las etiquetas cargadas [06:45]-[07:44].

## Conceptos y herramientas

**Conceptos:** [[Fulfillment]] · [[Envíos]] · [[Bundle]] · [[SKU]]
**Herramientas:** [[Senydrop]] · [[Tiendanube]] · [[Andreani]]

## Transcripción

*Transcripción automática con Whisper large-v3. Puede tener errores en nombres propios o términos técnicos.*

**[00:02]** Buenísimo. En este vídeo vamos a ver cómo gestionar un pedido desde nuestra tienda a CineDrop. A esta altura ya pudimos darnos de alta en el servicio de fulfillment en CineDrop. Hemos cargado nuestros propios productos y sincronizado los SKUs con nuestra tienda y hemos notificado de ingresos al depósito de CineDrop. Por eso se actualizó el stock. Así que ahora es momento de gestionar los pedidos. ¿Cómo lo hacemos? Bien. Yo para este ejemplo

**[00:29]** Tengo tres órdenes que voy a procesar dentro de CineDrop con el servicio de Fulfillment. Como podemos ver, los productos que contienen las órdenes son exactamente los mismos que ya veníamos trabajando en el ejemplo anterior. Así que vemos que son la orden 288, 287 y 286. Bien, vamos a ir a CineDrop y vamos a ir siempre dentro de la solapa de Fulfillment, vamos a ir a la sección de envíos. Yo para este ejemplo todavía no tengo órdenes en curso.

**[01:00]** Así que para el primer paso es ir a Tiendanube. Previamente debemos hacer la integración con Tiendanube. Si todavía no lo hiciste te invito a que veas el vídeo de cómo integrar CineDrop con Tiendanube. Yo para este caso ya tengo mi tienda integrada. Acá en integraciones puedo ver cómo efectivamente mi integración está activa. Bien, vamos a ir a Tiendanube y acá nos arroja dos posibles opciones tanto pagar envíos o

**[01:29]** Cargar etiquetas. ¿Qué significa esto? Bien, nosotros ofrecemos un servicio de principio a fin. Es decir, si vos necesitas que nosotros gestionemos las etiquetas, nos las abonas a nosotros y nosotros nos encargamos de generar las etiquetas y el resto del proceso. Ahora, si vos gestionas tus propias etiquetas, también puedes dar la opción de cargar las etiquetas y obviamente no te cobramos la gestión de las etiquetas. Eso queda a preferencia de cada cliente y de cada tienda.

**[01:57]** En este caso, en este ejemplo, vamos a ver por la opción 1 que es pagar etiquetas. Vamos a ir a pagar etiquetas y vamos a ir a continuar. Bien, está obteniendo los datos de nuestras ventas en CineDrop. Como podemos ver, aún no hay órdenes disponibles. ¿Por qué sucede esto? Bueno, uno de los motivos por los cuales puede suceder es que nuestras órdenes todavía están en pendientes de pago. Para que CineDrop las pueda registrar y tomar como válidas, éstas deben estar con el estado del pago aprobado.

**[02:27]** Así que vamos a hacerlo. Vamos a marcar como pago recibido. Esto va a depender de cada cliente y de cada configuración de cada tienda, pero el estado siempre es el mismo. Yo voy a probar las tres que teníamos como para el ejemplo y ahora si volvemos a CineDrop y actualizamos, vamos a ver cómo ahora las órdenes que teníamos ya nos aparecen con los correspondientes SKUs de los productos que veníamos gestionando. Así que el siguiente paso sería seleccionarlas

**[03:00]** Puedo seleccionar todas o seleccionar una por una, la que prefiera en este caso. Yo voy a seleccionar todas y voy a ir a pagar. Bien, este es el checkout donde vamos a poder ver un detalle de las órdenes que le vamos a transferir a CineDrop para que ellos puedan gestionar y hacer los despachos correspondientes. Podemos ver que si desplegamos están nuestros productos de las ventas que teníamos en los tres casos y podemos ver acá un resumen del valor del envío.

**[03:32]** Y el servicio fulfillment por 3. Así que vamos a ir a pagarlas y procedemos al siguiente paso. Algo importante a destacar es el tema de los combos. Podemos ver cómo habíamos cargado este producto que es un combo que tiene la mochila más la riñonera y habíamos cargado el SKU separado por un más. Así que la orden 288 podemos ver cómo la interpreta CENIDROP. Podemos ver que la orden 288

**[03:59]** Ya nos indica que son dos productos y podemos ver que ambos están por separados por lo cual esto nos indica que la integración de los combos es correcta. Excelente, ya hemos abonado las órdenes y ahora podemos ver cómo en la sección de envíos en curso nos aparecen nuestras tres órdenes correspondientes a el ID 288, 87 y 86. Podemos ver que el estado está en pendiente

**[04:25]** Y el código de seguimiento se va a cargar una vez que Zenydrop gestione las etiquetas y haga el despacho. Una vez que Zenydrop haga el despacho al correo y el correo haga el PIC correspondiente, el estado se va a sincronizar automáticamente. Nosotros, a partir de aquí, ya no tenemos que gestionar más nada. El sistema se va a encargar de pasar el estado de pendiente a por enviar y de por enviar a enviado, cargándole el número de seguimiento

**[04:55]** Tanto en CineDrop como en tu propia tienda nube, que lo vamos a ver cómo funciona en el ejemplo que vamos a ver a continuación. Ahora vamos a ver cómo sería cargar órdenes de la forma contraria, es decir, en lugar de pagar las etiquetas y que las gestione el mismo CineDrop, cargar nuestras propias etiquetas. Yo, por ejemplo, para este caso

**[05:18]** Tengo etiquetas ya generadas de ejemplo las cuales podemos ver que tienen el famoso número de seguimiento y un requisito muy importante para que todo funcione correctamente es que en el número de interno debe estar cargado el número de ID de tu venta en Tiendanube. Yo tengo exactamente las tres órdenes la 287 y la 288 como habíamos visto en el ejemplo de nuestras ventas. Así que ahora vamos a ir a Tiendanube

**[05:46]** Y en lugar de poner pagar envíos, vamos a darle a cargar etiquetas. Bien, acá podemos ver un poco más de detalle cuáles son los pasos y los requisitos que requiere, que es un poco exactamente lo que les expliqué recién de qué número de interno debe estar con el ID de su venta en Tiendanube. Así que vamos a seleccionar acá y seleccionar el archivo de la etiqueta. Le damos a subir y abre acá. Podemos ver cómo el sistema

**[06:16]** Ha reconocido las tres etiquetas por lo cual nos indica que las órdenes detectadas fueron tres y las órdenes compatibles con Tiendanube también fueron tres. Si por ejemplo cargáramos una etiqueta que tiene una hoja de más o un ajo de sobra, el sistema se va a encargar de avisarnos que por ejemplo de tres etiquetas puede detectar dos. Podríamos continuar igual y lo que va a hacer el sistema es solamente procesar las etiquetas que sí hayan tenido el match correspondiente.

**[06:45]** En este caso como las tres son de tres todo sale perfecto así que vamos a ir a pagar. Acá podemos ver que a diferencia de la opción donde nosotros le pagamos las etiquetas a CineDrop en esta oportunidad que cargamos nuestras propias etiquetas este resumen viene con un número de lote el cual contiene el pdf que nosotros cargamos con todas las órdenes correspondientes. También podemos observar que ahora el valor del envío es cero ya que

**[07:16]** Has cargado justamente las etiquetas y las has abonado previamente, por lo que nosotros en este caso solamente cobraremos el servicio de fulfillment. Así que ahora quedaría solamente pagar y continuar con el proceso. Buenísimo, una vez abonadas las órdenes podemos observar como ahora en la sección de envíos, en curso, nuestras órdenes que acabamos de abonar efectivamente nos aparecen en esta sección. A diferencia de las etiquetas que nosotros pagamos,

**[07:44]** Es decir, estas las hemos cargado nosotros, por ende acá nos aparece el lote relacionado para poder descargar las etiquetas siempre que lo necesitemos. Como también podemos ver que el número de seguimiento ya se ha cargado, porque el sistema detectó las etiquetas con su número de seguimiento y directamente ya les ingresó ahora. Como el estado recién está en revisión, ahora queda esperar de que CineDrop las despache para que automáticamente los diferentes estados se vayan impactando directamente en CineDrop y en nuestra tienda.

**[08:14]** Bien, ahora podemos ver cómo los estados de los pedidos han pasado a por enviar automáticamente. Si vamos a nuestra Tiendanube y actualizamos, también podemos ver cómo se actualizó e impactó automáticamente en nuestras órdenes correspondientes con el estado por enviar. Esto es gracias a la integración. Y ahora el estado ha sido enviado.

**[08:38]** Este es el último estado en el cual nos indica que efectivamente desde el depósito han podido despachar las órdenes correspondientes. Si nos vamos a nuestro Tiendanube y volvemos a actualizar podemos ver que las órdenes que estaban en por enviar han sido enviadas y este estado también se actualiza automáticamente. Cuando el estado ha sido enviado recién ahí impactará el número de seguimiento o nuestras órdenes. Podemos ver que además de que el estado ha sido enviado también el número de seguimiento se ha cargado automáticamente.

**[09:07]** Por lo que ahora si nosotros ingresáramos a este link podemos ver también el detalle que nos da Andriani respecto a ese seguimiento. Así que eso ha sido todo. Cualquier duda o consulta lo pueden hacer a través de Atención al Cliente. Espero que les haya sido de utilidad y haya quedado todo claro.
