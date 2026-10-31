---
modulo: 8
leccion: 14
titulo: "Landing page con Claude y subida a Shopify"
duracion: "09:40"
conceptos: ["[[Landing page]]", "[[Copy de venta]]", "[[Código Liquid]]", "[[Velocidad de carga]]"]
herramientas: ["[[Claude]]", "[[Shopify]]"]
tags: [ecomai, modulo-8, leccion]
---
# Landing page con Claude y subida a Shopify

> [!info] [[Modulo 8 - Ebooks]] · Lección 14 de 16 · ⏱ 09:40 · [▶ Abrir video](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%208%20-%20Ebooks/Video%2014.mp4)

← [[M8-13 Landing page con Lovable y Magic Patterns]] · [[Modulo 8 - Ebooks|↑ Módulo 8]] · [[M8-15 Ejemplos de tiendas de ebooks ya escaladas]] →

## Resumen

Clase que muestra cómo construir la landing directamente con Claude (usando el modelo Opus, o Sonnet si no se tiene plan pago) a partir de un prompt que se completa con la sales letter, el estilo visual deseado y el link del carrito de Shopify. Explica cómo subir imágenes propias indicando su ubicación, pedirle a Claude que haga carga diferida (lazy load) de las imágenes y que los botones redirijan al carrito salvo el call to action principal. Cierra mostrando cómo pasar el código HTML final a una página nueva de Shopify usando una plantilla Liquid en blanco, para publicarla como página de ventas.

## Puntos clave

- El prompt de landing con Claude se completa con la sales letter, el estilo visual/paleta de colores deseado, una landing de referencia si se tiene, y el link del carrito.
- La sales letter sigue la misma plantilla de copy de venta (promesa, dolores, beneficios, bonos, testimonios, garantía); Claude también puede ayudar a completarla, y hay un ejemplo de referencia ya resuelto.
- Para sacar el link del carrito: copiar la URL del producto, agregarle '.xml', copiar el número de variante y armarlo con el dominio de la tienda; conviene probarlo para confirmar que redirige bien al carrito.
- Para agregar imágenes: subirlas a Shopify (Contenido > Archivos), copiar el enlace y pasárselo a Claude indicando en qué parte de la landing colocarla.
- Pedirle a Claude que haga la landing con lazy load de imágenes (para que cargue más rápido) y que todos los botones redirijan al link del carrito, menos el botón principal de call to action, para que el cliente lea antes de ir directo a pagar.
- También se le puede pedir a Claude que genere imágenes de testimonios con IA, o que rehaga cualquier sección que no convenza.
- Para publicar: pedirle a Claude el código HTML completo, crear una página nueva en Shopify (Tienda online > Páginas), pegar el HTML ahí, y crear un template nuevo en 'Editar código' pegando la plantilla Liquid en blanco (sin header ni footer) para que la página se vea limpia.
- Asignar ese template a la página creada y publicarla; revisar que todos los botones lleven bien al carrito, y ver la clase de Lovable/Magic Patterns para mejorar también el checkout.

## Conceptos y herramientas

**Conceptos:** [[Landing page]] · [[Copy de venta]] · [[Código Liquid]] · [[Velocidad de carga]]
**Herramientas:** [[Claude]] · [[Shopify]]

## Recursos de esta lección

- [[Prompt - Landing con Claude]]
- [[Codigo - Link directo al carrito de Shopify]]
- [[Plantilla - Copy de venta (sales letter)]]
- [[Ejemplo - Copy de venta completo (Plata Que Rinde)]]
- [[Codigo - Plantilla Liquid para pagina de ventas en Shopify]]

## Transcripción

*Transcripción automática con Whisper large-v3. Puede tener errores en nombres propios o términos técnicos.*

**[00:00]** Buenas, holi gente. En esta clase les voy a mostrar cómo pueden hacer su landing page utilizando Claude. Así que lo primero, yo acá estoy utilizando Opus 4.7. Si no tienen Claude pago, pueden utilizar lo que viene siendo Sonnet. Así que lo primero que vamos a hacer es completar este prompt que yo les dejé. Bueno, este vendría siendo el prompt. Tienen que completar acá con su copy de venta. Bueno, esto no sé por qué está acá. Simplemente acá hay que pegar la sales letter. Esto lo voy a corregir ahora.

**[00:27]** Y acá pueden indicar también el estilo visual que quieren, la paleta de colores, etc. Acá si tienen alguna landing de referencia, y acá el link de su carrito, que ahora les voy a mostrar bien cómo sacarlo. Primero, la sales letter, acá les dejo la sales letter, que básicamente acá tienen que pegar su promesa, los dolores de su landing page, bueno, los beneficios, también si quieren borrar alguna sección, bueno, la borran.

**[00:53]** Acá pegan sus bonos, los testimonios, la garantía, etcétera. Básicamente lo que va a contener toda su tienda. Mismo también le pueden pedir ayuda a Claude para que les complete su sales letter de su producto. Y acá les puse también un ejemplo de cómo quedaría la sales letter. Bueno, la promesa, los dolores, acá los copian y pegan, los beneficios, etcétera, etcétera. Y ahora, para sacar el carrito, vamos a ir acá a carrito, vamos a ir a nuestra tienda Shopify, vamos a ir a nuestro producto,

**[01:29]** Vamos acá en la biblia del proyecto y vamos a bajar acá hasta el lapicito. Bien, ahora este link lo vamos a copiar y lo vamos a pegar acá en el navegador y le vamos a agregar .xml, ¿ok? Y nos va a salir esto. Acá lo que tenemos que copiar es este numerito que vemos por acá. Lo copiamos y acá... Bueno, acá en este documento que les dejé tenemos que básicamente completar esto.

**[02:07]** Así que voy a copiar esto. Bueno, ahí lo copié. Lo voy a anotar en un bloc de notas. Y acá vamos a poner el número de variante que habíamos copiado. Bueno, acá pegamos el número de variante y nuestro dominio que vendría siendo esto, Shopify.com. Y lo pegamos. Y también yo me gusta verificar si realmente me lleva el carrito, así que lo voy a copiar y pegar acá y ver si nos lleva.

**[02:47]** Bueno bien listo, ahí estaría. Bueno como ven acá yo ya puse el link del carrito que igual les indica dónde tienen que colocarlo, la landing de referencia y acá van a pegar su sales letter. Así que con todo esto ya lo que hacemos es copiarlo y se lo vamos a pegar a Claude. Así que nada, una vez que se lo pasamos a Claude vamos a darle enter y nos va a estar armando la landing. Bueno miren acá me terminó de armar recién la landing page.

**[03:23]** Entonces ahora lo que vamos a hacer es mostrarles cómo pueden subir las imágenes para que aparezcan acá en la landing. Por ejemplo, les voy a mostrar una imagen de referencia, pero ustedes tienen que hacerlo con cada imagen que quieran agregar a la landing page. Por ejemplo, a ver esto acá, bueno, básicamente vamos a ir a nuestra tienda Shopify, vamos a ir acá donde dice contenido, me costó encontrarlo, en archivos,

**[03:58]** Acá vamos a subir archivos y vamos a subir la imagen. Bueno, ahí subí una imagen, entonces, ¿qué vamos a hacer? Bueno, vamos a darle acá a copiar enlace, vamos a ir a Claude y le vamos a decir, bueno, te voy a pasar las imágenes de la landing y dónde quiero que las coloques. Ok. Entonces, yo voy a pegar esta imagen.

**[04:34]** Imagen 1. Voy a pegar la imagen 1 y le voy a decir que la quiero acá colocada al principio. O le mandan donde quieren que la coloque. Yo voy a decir que la coloque acá. También tienen que pedirle que, bueno, para mejorar la velocidad de carga pídanle que se las haga lazy load. Haceme la landing lazy load.

**[05:07]** Y también de paso le voy a decir que todos los botones también rediríjeme los botones a este link. Y le vamos a pegar el link del carrito, por las dudas. Menos el primer botón call to action. Este botón yo les recomiendo, como le estoy pidiendo ahora a Claude, que no lo redireccionen directamente al carrito.

**[05:37]** Porque por ahí hay muchas personas que entran y le dan al botón y no llegaron a leer lo de la landing page. El precio con lo que incluye. Por eso lo dije así nomás, ¿ok? Y esto se lo vamos a mandar. También algo que pueden hacer si no les gusta cómo se las hizo, bueno, le pueden decir que se las vuelva a hacer. Por ejemplo, si no les gusta esta sección, bueno, que se la cambien. O literalmente customizar lo que quieran.

**[06:06]** Algo también que pueden hacer es pedirle que les salga, por ejemplo, las imágenes con IA de los testimonios, que les utilice imágenes generadas con IA. A ver si acá ya... Bueno, listo. Ahora le voy a pedir que me pase el código HTML completo. Pásame el código HTML completo para, ahora sí, subir esta landing a Shopify. Ahora les voy a mostrar cómo pueden subirla a Shopify. Bueno, ok. Ya que tenemos el código HTML, lo vamos a copiar y vamos a ir para Shopify.

**[06:41]** Vamos a ir acá en tienda online, vamos a ir a páginas y acá vamos a añadir una página. De nombre le pueden poner el nombre de su ebook o lo que quieran. No sé, ejemplo, yo le voy a poner ejemplo nomás. Y acá en la parte de acá donde dice mostrar editor y mostrar html vamos a pegar el código. Vamos a guardar. Bien, ahora para que se muestre en la tienda lo que tenemos que hacer es ir a tienda online

**[07:19]** Vamos a ir a los tres puntitos y vamos a ir a editar código. Bueno, bien, ahora acá vamos a ir a templates, como les dije, y agregar. Bueno, acá cuando agregamos un archivo en templates, vamos a ponerle, por ejemplo, acá le dejé esto de ejemplo, vamos a copiarlo. Otra vez haremos archivo, le ponemos este nombre. Yo le puse página de ventas, pero si quieren pueden poner el nombre de su ebook para identificarlo mejor.

**[08:02]** Y ahora vamos a ir acá al liquid y vamos a pegar este código que también les dije. Lo copiamos, vamos acá y lo pegamos y ahora le damos a guardar. Una vez que ya lo hayamos guardado vamos a ir otra vez a nuestra tienda, vamos a ir a páginas y ahora acá donde teníamos esto, acá vamos a poner visible y acá en plantilla vamos a poner

**[08:39]** Página de ventas, que es el nombre que le había puesto yo, pero a ustedes les va a aparecer con el nombre que le hayan puesto ustedes. Y le damos a guardar. Bien, ahora sí le damos a ver. Bueno, como ven acá, lo hubiera dicho, como ven se ve negro, no se llega a leer bien, pero bueno, ustedes pueden pedírselo a Claude y que se los modifique. Pero como ven acá, la imagen que yo la había subido y le dije dónde quería. Y ya tendríamos la landing page acá lista para, bueno, para utilizar. Nuestra landing page lista.

**[09:10]** Y asegúrense también que los botones anden. Por ejemplo, a ver, este botón. Bueno, como vemos, lleva el carrito. Ah, y miren también en la clase, mírense el final de la clase de Lovable y Magic Patterns, donde enseño a hacer sus landings con esas dosías, porque les muestro también cómo mejorar el tema del checkout y hacerlo más atractivo. Porque acá también les va a aparecer un texto de cobrar impuestos y no sé qué. Y entonces, mírense esa clase que les muestro cómo mejorar el checkout.
