---
modulo: 10
leccion: 7
titulo: "Integrar Shopify con Senydrop"
duracion: "04:20"
conceptos: ["[[Fulfillment]]"]
herramientas: ["[[Senydrop]]", "[[Shopify]]"]
tags: [ecomai, modulo-10, leccion]
---
# Integrar Shopify con Senydrop

> [!info] [[Modulo 10 - Logistica fullfilment]] · Lección 7 de 8 · ⏱ 04:20 · [▶ Abrir video](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%2010%20-%20Logistica%20fullfilment/Video%207.mp4)

← [[M10-06 Pagar Senydrop con USDT vía Binance]] · [[Modulo 10 - Logistica fullfilment|↑ Módulo 10]] · [[M10-08 Configurar envío a sucursal de Andreani]] →

## Resumen

Guía técnica paso a paso para conectar una tienda de Shopify con Senydrop mediante una app propia creada en el panel de desarrolladores de Shopify. Cubre desde la creación de la app hasta pegar el ID de cliente y el secret en Senydrop para dejar la integración funcionando.

## Puntos clave

- El panel de integraciones de Senydrop trae un instructivo paso a paso con los datos que hay que ir copiando y pegando [00:02]-[00:32].
- En el admin de Shopify: Configuración → Aplicaciones → Desarrollar apps → Developer dashboard [00:32]-[01:03].
- Ahí se crea una app nueva, con nombre propio, para conectar con Senydrop [01:03]-[01:34].
- Hay que completar la URL y los alcances (scopes) de permisos que Senydrop indica en su panel, copiándolos directamente de ahí [01:34]-[02:05].
- Se publica la app con el botón Publicar (dos veces; la versión es opcional) [02:05]-[02:38].
- Después hay que ir a la app creada y darle Instalar app, eligiendo la tienda correspondiente si hay varias cuentas de Shopify, y confirmar los permisos [02:38]-[03:11].
- De vuelta en Senydrop, se completa la integración pegando el ID de cliente y el secret que da el Developer dashboard de Shopify, y se le da a conectar [03:11]-[04:15].

## Conceptos y herramientas

**Conceptos:** [[Fulfillment]]
**Herramientas:** [[Senydrop]] · [[Shopify]]

## Transcripción

*Transcripción automática con Whisper large-v3. Puede tener errores en nombres propios o términos técnicos.*

**[00:02]** En este caso vamos a seguir las instrucciones y el paso a paso para lograr integrar nuestra tienda de Shopify dentro de Zenith Drop. El primer paso es justamente ir a integraciones, seleccionar la opción de Zenith Drop y justamente cuando abrimos el panel de configuración de Zenith Drop tenemos como primer ítem las instrucciones. El primer paso es ir a nuestro administrador de nuestra tienda de Shopify.

**[00:32]** le damos clic aquí nos va a redireccionar aquí si no estamos logueado nos va a pedir que lo hagamos ingresamos una vez dentro del administrador de nuestra tienda vamos a ir a la sección de configuración aquí abajo luego a la parte de aplicaciones una vez en la sección de aplicaciones vamos a ir a desarrollar apps y luego a desarrollar apps en dev dashboard esto nos va a redireccionar a una sección que es para desarrolladores pero

**[01:03]** Que con algunos simples pasos igual vamos a poder crear nuestra aplicación. Vamos a crear app, aquí nos va a pedir el nombre y le vamos a dar a crear como dice aquí. Luego nos va a pedir algunos parámetros más para terminar de configurar y crear nuestra aplicación que se conecte con Seridrop. Aquí nos va a pedir algunos datos que los tenemos nuevamente en nuestro listado de configuración.

**[01:34]** Nos va a pedir primero una URL, la cual directamente la podemos copiar de acá. Esto la vamos a pegar acá donde dice example.com. Luego nos va a pedir un conjunto de accesos, de permisos, los cuales también los podemos copiar desde aquí y los vamos a pegar directamente en accesos a alcances. Una vez finalizado estas dos configuraciones, como nos indica

**[02:05]** El paso a paso le vamos a dar a publicar y luego nuevamente a publicar. Publicar, esto es opcional, poner una versión, le vamos a dar solamente a publicar. Perfecto. Acá tenemos las versiones que se generan de esta misma aplicación. Si nosotros vemos aquí, tenemos algunas secciones de esta aplicación que acabamos de crear. Lo que nos indica las instrucciones es que lo que tenemos que hacer posteriormente en el panel de la izquierda es

**[02:38]** Ir a la aplicación y luego ir al botón instalar app. Esto es de esta manera. Vamos a la pantalla principal de nuestra aplicación y aquí tenemos el instalar app. Bueno, acá en este caso yo tengo asignadas varias cuentas con varias tiendas de Shopify dentro de la misma cuenta. Voy a seleccionar en la que quiero que se incorpore y acá nos va a pedir que confirmemos los permisos que acabamos de

**[03:11]** En este caso ya terminamos lo necesario dentro del administrador de Shopify y lo que vamos a hacer es ir a completar la integración. Acá nos va a redirigir nuevamente a la sección donde habíamos iniciado y donde estábamos siguiendo el paso a paso del tutorial. En este caso ya nos copió el dominio que es necesario. Nos van a faltar estos dos datos.

**[03:41]** que los vamos a sacar de nuevamente el test dashboard que no lo habíamos cerrado configuración tenemos una id de cliente que lo podemos copiar directamente aquí lo vamos a pegar aquí y un secret secreto que también le vamos a dar a pegar lo vamos a pegar aquí y luego le vamos a terminar con conectar y aquí ya tenemos

**[04:15]** La integración con Shopify finalizada.
