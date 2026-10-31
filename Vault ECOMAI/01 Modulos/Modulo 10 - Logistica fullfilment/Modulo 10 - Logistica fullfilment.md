---
modulo: 10
tags: [ecomai, modulo-10, moc]
---
# Modulo 10 - Logistica fullfilment

> [!abstract] 8 lecciones · ⏱ 44:47 de video

← [[Modulo 9 - Algoritmo para ecommerce]] · [[00 - Inicio|↑ Inicio]]

Este módulo es una guía práctica para operar el servicio de fulfillment de Senydrop, la plataforma argentina que guarda stock propio en su depósito y despacha los pedidos por vos. Cubre todo el circuito: darse de alta, cargar productos y sincronizar sus SKU con la tienda (incluyendo cómo armar combos), notificar ingresos de mercadería al depósito, y procesar pedidos tanto desde Tiendanube como desde Shopify, pagando los envíos o cargando etiquetas propias. También incluye cómo pagar el servicio en USDT vía operaciones P2P de Binance, cómo integrar técnicamente Shopify con Senydrop, y cómo configurar en el checkout el envío a sucursales de Andreani. Al terminar el módulo vas a poder tener tu logística funcionando de punta a punta sin manejar stock propio en tu casa.

## Lecciones

### 1. [[M10-01 Alta en el fulfillment de Senydrop|Alta en el fulfillment de Senydrop]] · 01:44

Muestra el primer paso para operar con Senydrop: pedir el alta en el servicio de fulfillment desde la sección homónima de la plataforma. Explica qué pide el formulario de solicitud, cuánto tarda la aprobación y cuál es el siguiente paso una vez aprobada la cuenta.

### 2. [[M10-02 Cargar productos y sincronizar SKU|Cargar productos y sincronizar SKU]] · 04:56

Explica cómo dar de alta cada producto propio en Senydrop (título, categoría y descripción básica), cómo queda asignado un SKU por producto una vez aprobado, y cómo cargar ese SKU en la tienda para que las ventas se sincronicen. Cierra con el método para vender combos, cargando varios SKU separados por el signo más en una misma publicación.

### 3. [[M10-03 Notificar ingresos de stock al depósito|Notificar ingresos de stock al depósito]] · 03:50

Muestra cómo avisarle a Senydrop que se le va a enviar mercadería al depósito para que la reciba y actualice el stock. Explica qué datos pide la notificación de ingreso, los distintos estados por los que pasa, y qué pasa si la cantidad recibida no coincide con la notificada.

### 4. [[M10-04 Gestionar pedidos desde Tiendanube|Gestionar pedidos desde Tiendanube]] · 09:25

Explica cómo procesar en Senydrop los pedidos de una tienda en Tiendanube ya integrada, una vez que el pago figura aprobado. Muestra las dos formas de resolver el envío (pagarle las etiquetas a Senydrop o cargar etiquetas propias), cómo se interpretan los combos y cómo se sincroniza automáticamente el estado y el número de seguimiento entre Senydrop y la tienda.

### 5. [[M10-05 Gestionar pedidos desde Shopify|Gestionar pedidos desde Shopify]] · 08:05

Repite el mismo flujo de fulfillment de la clase anterior pero con una tienda en Shopify: cambiar al modo fulfillment, sincronizar productos y combos por SKU, exportar las órdenes en CSV y subirlas a Senydrop para procesarlas. Muestra también la protección contra duplicados y las dos formas de resolver el envío.

### 6. [[M10-06 Pagar Senydrop con USDT vía Binance|Pagar Senydrop con USDT vía Binance]] · 05:41

Explica el circuito completo para pagarle a Senydrop en dólares: comprar USDT en Binance con pesos mediante una operación P2P, y después enviárselos directamente al Binance ID que provee Senydrop. Detalla cómo comparar ofertas, cómo transferir y confirmar el pago, y cómo verificar los datos antes de enviar las criptomonedas.

### 7. [[M10-07 Integrar Shopify con Senydrop|Integrar Shopify con Senydrop]] · 04:20

Guía técnica paso a paso para conectar una tienda de Shopify con Senydrop mediante una app propia creada en el panel de desarrolladores de Shopify. Cubre desde la creación de la app hasta pegar el ID de cliente y el secret en Senydrop para dejar la integración funcionando.

### 8. [[M10-08 Configurar envío a sucursal de Andreani|Configurar envío a sucursal de Andreani]] · 06:44

Explica las dos formas de configurar en el checkout el envío a sucursal de Andreani cuando la tienda está integrada con Senydrop: un método simple disponible en cualquier plan de Shopify, y un método avanzado (que requiere un plan superior de Shopify) que además deja elegir envío a domicilio, definir costos y mostrarle al cliente las sucursales más cercanas dentro del propio checkout.

## Notas

Senydrop es el nombre real de la herramienta central del módulo; Whisper la transcribió de formas muy distintas en cada video (CineDrop, Zenidrop, Zeny Drop, Sendigrop, Seridrop, Zenith Drop, SenderUp, Ceridrop, SaniDrop, SignDrop, CineGrowth), corregidas acá tras confirmar por una búsqueda externa que se trata de senydrop.com, un servicio argentino de fulfillment/logística integrado con Tiendanube, Shopify y Mercado Libre que despacha con Andreani. El video 4 hace referencia a un video previo de cómo integrar Senydrop con Tiendanube que no forma parte de este lote de lecciones asignado.
