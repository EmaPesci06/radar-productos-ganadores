---
modulo: 3
leccion: 12
titulo: "Cómo crear la página de inicio de nuestro producto con Claude"
duracion: "26:58"
conceptos: ["[[Landing page]]", "[[Código Liquid]]", "[[Branding]]"]
herramientas: ["[[Claude]]", "[[ChatGPT]]", "[[Higgsfield]]", "[[GoFullPage]]"]
tags: [ecomai, modulo-3, leccion]
---
# Cómo crear la página de inicio de nuestro producto con Claude

> [!info] [[Modulo 3 - Crea tu pagina y tu marca]] · Lección 12 de 20 · ⏱ 26:58 · [▶ Abrir video](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%203%20-%20Crea%20tu%20pagina%20y%20tu%20marca/Video%2012.mp4)

← [[M3-11 Instrucciones del módulo]] · [[Modulo 3 - Crea tu pagina y tu marca|↑ Módulo 3]] · [[M3-13 Creando Liquid y sección de producto]] →

## Resumen

Clase central de la construcción de la landing: David muestra landings de referencia con Liquid personalizado (entre ellas Grunsly) para explicar por qué conviene que el cliente no aterrice directo en el producto, sino que primero pase por una pantalla de inicio explicativa que "no le quiera vender" antes de llegar a la ficha. Usa GoFullPage para sacar un PDF completo de la landing de referencia, se lo pasa a Claude junto con un código Liquid base para que genere la nueva pantalla de inicio adaptada (colores, nombre, precio), y va creando las imágenes con ChatGPT más Higgsfield, subiéndolas a Shopify y pidiéndole a Claude que las ubique en el orden correcto dentro del Liquid. El resultado queda con 8 imágenes propias, lista para pasar a editar la landing del producto en sí.

## Puntos clave

- Muestra landings de referencia con Liquid personalizado (ej. Grunsly) y explica que conviene no llevar al cliente directo al producto, sino primero a una pantalla de inicio que "no le quiera vender" para generar confianza [00:29]-[01:30]
- Aclara que una landing más linda no siempre convierte más: hay landings feas que funcionan muy bien [01:30]-[02:03]
- Va a dejar todos los códigos Liquid documentados para que cada uno se los pase a Claude y los adapte a su producto [01:00]-[02:35]
- Usa GoFullPage para exportar en PDF la landing de referencia completa y se la entrega a Claude junto con el código Liquid base para adaptarla [04:43]-[05:28]
- Ya generado el Liquid, ajusta con Claude el color de marca (pasándole el código hexadecimal) y el nombre del producto directamente por chat [06:24]-[07:42]
- Esa pantalla de inicio puede diseñarse para mandar al cliente directo a la ficha del producto, si no se quiere el paso intermedio [08:22]
- Las imágenes se crean con el flujo de ChatGPT (prompt) más Higgsfield, se suben en Contenido > Archivos de Shopify para conseguir el link, y ese link se le pasa a Claude para que las ubique en el orden pedido dentro del código [09:34]-[13:33]
- Conviene indicarle a Claude el orden exacto de las imágenes (imagen 1, imagen 2, video como imagen intermedia, etc.) para que arme bien el Liquid final [22:44]-[25:09]
- El resultado queda con 8 imágenes propias en la pantalla de inicio, sin sensación de venta forzada, lista para la siguiente clase de edición de la ficha del producto [08:55]-[26:39]

## Conceptos y herramientas

**Conceptos:** [[Landing page]] · [[Código Liquid]] · [[Branding]]
**Herramientas:** [[Claude]] · [[ChatGPT]] · [[Higgsfield]] · [[GoFullPage]]

## Recursos de esta lección

- [[Prompt maestro - Replica de landings en Shopify]]
- [Carpeta de códigos Liquid en Drive](https://drive.google.com/drive/folders/1BgmMBZ4_SumpL991XtMxIpyTBzpKgzKO?usp=sharing)

## Transcripción

*Transcripción automática con Whisper large-v3. Puede tener errores en nombres propios o términos técnicos.*

**[00:01]** Hola chicos, el día de hoy les estaré explicando cómo crear nuestra landing desde cero. Como pueden ver, esta ya tiene un poco de estructura, pero porque ayer estábamos haciendo la clase y se nos pasó, pero no importa. Primero que todo, les voy a enseñar cómo puede quedar una landing con códigos liquid personalizados. Les voy a enseñar una que ya yo tengo, que probé un producto y funcionó, pero la estamos creando nuevamente y estructurando mejor.

**[00:29]** Pero bueno, les voy a dejar acá dos muestras. Estas son bonitas. Vamos a ponerla por el celular. Perfecto, ok. Si se dan cuenta, primero que todo, no llegamos directo al producto al cliente. O sea, porque también la venta impulsiva, por decirlo así, primero tiene que pasar porque el cliente siente que no le quieras vender. O sea, tenemos que intentarlo venderle para así venderle. Pero bueno, les explico.

**[01:00]** Por ejemplo, aquí es por todo lo importante hacerlo, por eso se lo dejaré el liquid personalizado, se lo dejaré en el documento y así ustedes se lo dan a Claude y lo adaptan a su producto. Ahora lo vamos a hacer para que entiendan. Mira, porque Grunzly es diferente, explica todo, te da las imágenes, los tres pilares de Grunzly. O sea, se ponen a ver y luego cuando el cliente termina de bajar en todo esto, le puede dar, quiero probar Grunzly sin riesgo y lo lleva al producto, lo lleva a la página del producto como tal.

**[01:30]** Los comentarios, todo. Y aquí abajo también está el producto. O sea, el cliente cuando baje, lo puede comprar acá mismo. O si no, cuando le den al botón, nos va a llevar hacia esta página. Vamos a apuntar esto un poco. Lo ponemos en el suelo otra vez. Y bueno, nos lleva a esta página de productos. Si se ven, si se ponen a detallar la página, está hermosa. Hermosa. Y no solo hermosa, porque no todas las páginas son hermosas y convierten. O sea, más bien, todas las páginas.

**[02:03]** Mientras más hermosa, a veces menos convierta. Si se dan cuenta, a veces hay landing súper feas que no le gustan a uno y cuando vas a ver, están funcionando al cien. Entonces, acá tenemos, todo esto son temas liquid, todo, si se ponen a ver acá, esto es un liquid, esto es imagen y texto, todo esto lo vamos a hacer con Higgsfield, esto también es un liquid y les voy a dejar todos estos liquids, como pueden ver acá, ajá, acá, me sale.

**[02:35]** Todo se los voy a dejar para si ustedes lo adquieren a su producto, se lo dan a Claude y se lo hace idéntico con la información de su producto, todo. Este también es otro liquid, porque me gusta más y se ve más lindo. Porque la otra, que es esta, que es la del producto que estamos haciendo, no, no me gusta, no. Es como feo. Ok, comencemos. Acá vamos a quitar toda esta pantalla del inicio y la vamos a hacer como se los acabo de mostrar.

**[03:05]** Vamos a quitar esta foto. Vamos a quitar esto. Vamos a quitar esto. Dejamos el producto, obviamente. Vamos a esta. Y acá nos vamos. Este es el liquid. Ok, aquí estamos en la pantalla del inicio. Perfecto, sí. Este es el tiempo. El liquid. Bueno, vamos a copiarlo. Obviamente yo se los voy a dar. Entonces vamos a copiar. Se van a ir a Claude. Se van a ir a Claude. Y les van a poner.

**[03:56]** Ahora vamos a buscar, vamos a ponerle acá, le ponemos el link, le vamos a poner acá arriba, le vamos a poner el link, ya les puedo dejar este pro también, sin problema, le ponemos el código ahí.

**[04:43]** Y con estas apps, con estas, se las voy a dejar también en el documento GoFullPage, pueden hacerle script completo a la página, en PDF, en imágenes, en todo. Acá lo tenemos, descargamos el PDF. Una vez descargado el PDF, se lo vamos a dar a Claude. Y también le podemos poner el PDF. Ahí comienza a trabajar, mientras.

**[05:28]** Ok, procedemos a quitarle el encabezado, la barra de anuncios. Vamos a ver qué tal va el liquid. Ahí lo está creando. Mientras lo crea, vamos a esperar un rato. Ok, ya terminó de crear el liquid. Aquí está, vamos a verlo. Vamos a ver cómo se ve la landing.

**[06:24]** Esas imágenes tenemos que ponerlas nosotros en el contenido, ya les voy a explicar cómo. Perfecto. Ok, si pueden leer, se dan cuenta que quedó idéntico, hasta el botón, todo, pero el color no nos gustó, entonces nos falta acomodar el color y las imágenes. Vamos para acá, vamos a abrir este nuestro pestaño y le vamos a decir, necesito que me cambie.

**[07:07]** Aquí yo tengo el código del color de nuestro producto. Tocamos acá, le damos a editar y acá vamos a ver el color. Lo copiamos, le damos el código. ¿Qué otro detalle le íbamos a arreglar? Las imágenes, ok. Ah, y el nombre, porque si yo voy a poner el nombre de este producto, se llama...

**[07:42]** Mientras lo mejora, vamos a esperar un toque. Ok, ya Claude terminó de hacer el link. Vamos a copiarlo. Lo pegamos de nuevo. Es este. Igualmente esto, si ustedes quieren, no lo ponen.

**[08:22]** Y mandan al cliente directamente a la página del producto, no hay problema, esto lo quitamos y luego lo ponemos normal y ya, si no lo quieren. Acá este espacio lo podemos configurar acá, se acomoda, el de arriba igual, este lo podemos poner más pegadito arriba, más lindo, perfecto. Y si se dan cuenta tiene 1, 2, 3, 4, 5, 6, 7, 8 imágenes.

**[08:55]** Tiene 8 imágenes, perfecto. Entonces, vamos a guardar acá. Vamos a guardar acá. Vamos al producto. Y todo esto lo podemos hacer, esta misma imagen, la podemos hacer con guía. Igualmente ustedes pueden hacer la imagen de su preferencia, la que quieran ponerle a su producto, todo. Entonces, ¿qué vamos a hacer nosotros? Vamos a agarrarlo. No me deja agarrarlo. Entonces, lo que vamos a hacer es, vamos a buscar...

**[09:34]** Vamos a crear las imágenes. Yo soy ChatGPT para los poros de las imágenes porque quedan perfectamente limpios y profesionales. Las fotos quedan increíbles. Porque Claude a veces con las imágenes se equivoca y así. Entonces vamos a esta otra aplicación, a lo right click, a grabar imágenes.

**[10:17]** Se lo ponemos acá y le decimos eso así. Disculpa si se escucha ruido alrededor, pero bueno. Ok, le ponemos eso así. Le buscamos la foto de nuestro producto. Vamos a ponerle, a ver, esto que tenemos acá. Vamos a hacer la captura y solo a nuestro producto. Ahí lo tenemos. Se lo vamos a hacer.

**[11:21]** Ahí comenzará a crear el prompt, luego venimos por acá, le ponemos la misma foto a nuestro producto de Higgsfield, ponemos acá, perfecto. Aquí vamos a ver que crea el prompt, se demora un poco, ok, acá crea el prompt, luego para las otras imágenes lo pondremos en forma rápida el video y así van a ver un poco más rápido y mejor como creo las imágenes, para así ser más eficiente.

**[12:07]** Igual yo les puedo dejar todos los prongs, se los voy a dejar en los documentos para que los funcione y puedan usarlo o adaptan los prongs a ustedes así para que se puedan ayudar. Por eso se los estoy enseñando a hacer de esta manera. Entonces ponemos el programa, ponemos la foto, la queremos cuadrada y vamos a generar. Mientras la genero vamos a esperar un rato para luego explicarle cómo la ponemos en el link. Ok, acá ya nos creó la imagen, vamos a descargarla.

**[12:45]** Luego venimos y acá en la otra pestaña que abrimos nos vamos a contenido. En contenido nos vamos a archivos y tenemos que subir la foto acá. La subimos acá. Ok, la subimos acá a la imagen. Esperamos que se suba. Demorada, demorada, casi nada. Ok, ahora vamos a copiar el enlace y se lo vamos a dar a Claude. Le vamos a decir en la primera parte de arriba.

**[13:33]** Ahí le ponemos el link de la imagen. Tenemos que darle la imagen con link, pero primero tenemos que subirla a Shopify, obvio, para obtener el link, pero para así las imágenes queden perfectas y se puedan poner en el liquid personalizado, porque si no le pasan el link de la imagen a Claude, no les va a poder acomodar el pro. Ahí está. Ahí va a modificar esa foto. Las demás las hago en cámara rápida y así ven el proceso más rápido.

**[14:02]** Ahí está haciendo el liquid, ahí ya está listo. Vamos a cerrar esto para que se apodice y lo volvemos a ver. Lo copiamos, seguro les aparece así, pero obvio, porque se les está mostrando acá. Luego nos venimos y lo ponemos otra vez. Como pueden ver, ahí está la imagen, se ve perfecta, ustedes lo ven haciendo todas las imágenes para que vean cómo se hace. Ok, vamos a continuar creando las imágenes.

**[14:59]** Ahí le vamos a poner, vamos a sacarle un script a esto, otra vez, le sacamos el script y se lo vamos a dar a este artículo. Vamos a robarlo en tu tableta. Con la foto ya quedaría bien. Le damos la imagen, le damos la imagen, y listo. Oh bueno, quiero crear la imagen en él. Si crea la imagen y queda perfecta, no está mal. Pero vamos a ver qué tal. Si no, le decimos que no...

**[16:19]** Que nos haga el prom para Claude. Para Claude, no, para Higgsfield, disculpen. Ok, acá creo el prom. Perfecto, ahora vamos a ir haciendo las aportaciones. Vamos a buscar un videito. Ok, ok, ahí creo la foto. Ok, como les venía diciendo, vamos a poner un videito, que ese lo vamos a buscar ahora. Vamos a hacer esta foto también. Acá me creo el otro prom. Vamos copiando. Vamos buscando el otro.

**[18:20]** Lo hago así para ser más eficiente y ser más rápido y no estar esperando que termine. Más probes, sí. Ok, ahí lo creó. Vamos a darle nota. Y ponemos el que vemos. Lo preparamos. No sé por qué la cámara no se pasa a cada página cuando cambio, pero bueno. Ok. Acá está creando este. Luego de este está ahí. Ok, ahí la creó. Ahí la creé. Y bueno, así lo está creando. Ok.

**[20:36]** Ya tenemos todo. Ahora vamos a buscar un video como este. Vamos a meterle el file al producto. Así pueden ver los creativos que tiene disponible. De donde lo estamos copiando, el producto que queramos. Este me gusta. Disculpa, le damos en calidad. Lo ponemos en HD. Activamos esto. Y le ponemos el video. Obvio, el video lo tienen que traducir, editar. Editar, disculpa.

**[21:11]** Pero bueno, vamos a ponerlo así por ahora. Ya me creo el otro pro. Así lo ponemos. Perfecto. Vamos a ir descargando las fotos. Tenemos todas las imágenes. Vamos a esperar que se descargue esta, que se termine esta. Perfecto. Ya tenemos todas las imágenes. Ahora nos vamos acá en contenido y archivo y vamos a subir todas las imágenes y el video.

**[22:12]** Obviamente no importa el orden, sube todo, las imágenes y el video. Vamos a esperar que todo se suba perfectamente. Cuando todo se complete, vamos a agarrar cada link del video, como de la imagen, se lo vamos a dar a Claude para que nos ponga nuestro link. ¿Qué vamos a hacer? Necesito que ponga las siguientes imágenes. ¿Dónde van imágenes?

**[22:44]** El orden que te daré. La imagen que queremos, bueno, la de aquella está puesta, pero vamos a dárselo otra vez para que no se equivoque. Son 2, 3, 4, ok, ya acabó el video. 4, 5, 6, 7. Esta es la imagen 1, copiamos el link. Acá, guardamos esto. Vamos aquí al final y ponemos imagen 2. Ok.

**[23:20]** La que va de segundo. La que va de segundo por... Ok, esa es. Esta es la que va de segundo. Se lo ponemos acá. Volvemos a copiar esto, lo escribimos como ustedes desean. Vamos a poner acá imagen 3. Y así le vamos a poner sucesivamente como queremos las imágenes. La 4. La 4 es el video. Vamos a ponerlo acá. Vamos a ir viendo el video.

**[24:12]** Luego el video, que sería imagen 5. Luego la otra imagen. Es esta, si no me equivoco. Imagen 6. Imagen 7. Ok, vamos a hacerlo así. Imagen 7. Creo que nos falta una sola imagen, pero no sé.

**[25:09]** Igual él lo va a modificar y lo va a hacer bien. Vamos a esperar a que lo cree. Está creando el código. Está ajustando. Acá nunca van a poder ver los videos y las cosas porque obviamente está cargado en el Shopify. Cuando lo ponga en el Shopify sí se va a ver todo perfecto. Vamos a esperar a que termine. Perfecto. Aquí está. Vamos a probar ahora qué tal quedó. Ok, ya está entregando las imágenes. Perfecto. Aquí tenemos el video.

**[26:07]** La otra imagen y listo. Lo modificamos. Bueno, ya le quitamos el relleno. Quedó perfecto. Así cuando el cliente entra a tu landing, no siente que está surgido en venderlo, porque eso también hace que el cliente se vaya. Aquí tenemos lista la pantalla de inicio con Claude. Está perfecta. Hicimos el tema Liquid. Igualmente ustedes el tema lo pueden editar el Liquid personalizado ustedes.

**[26:39]** Le pueden decir que le cambie algo, que les ponga otro nombre, otra imagen, que le quite imágenes. O sea, ustedes literalmente tienen mente abierta para hacer todo lo que quieran de eso. Ahora vamos a pasar a editar la landing como tal. Nos vemos en el siguiente video.
