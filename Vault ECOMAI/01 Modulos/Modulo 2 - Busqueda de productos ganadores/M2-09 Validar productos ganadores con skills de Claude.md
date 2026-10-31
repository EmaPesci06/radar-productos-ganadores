---
modulo: 2
leccion: 9
titulo: "Validar productos ganadores con skills de Claude"
duracion: "51:01"
conceptos: ["[[Validación de producto]]", "[[Producto ganador]]", "[[Nicho]]", "[[Buyer persona]]", "[[Dolor del cliente]]", "[[Ángulo de venta]]", "[[Valor percibido]]", "[[UGC]]"]
herramientas: ["[[Claude]]", "[[TrendTrack]]"]
tags: [ecomai, modulo-2, leccion]
---
# Validar productos ganadores con skills de Claude

> [!info] [[Modulo 2 - Busqueda de productos ganadores]] · Lección 9 de 13 · ⏱ 51:01 · [▶ Abrir video](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%202%20-%20Busqueda%20de%20productos%20ganadores/Video%209.mp4)

← [[M2-08 Elegir creativos ganadores con los filtros de Gethookd]] · [[Modulo 2 - Busqueda de productos ganadores|↑ Módulo 2]] · [[M2-10 Explicación de importación con Alibaba]] →

## Resumen

Franco Lucero, nuevo mentor de la comunidad (dos tiendas propias facturando cerca de 200 millones de pesos por mes), presenta dos skills de Claude —documento A (doc-a-validator) y documento B (doc-b-builder)— para investigar productos antes de lanzarlos. El documento A analiza reseñas reales de Amazon, Reddit, Mercado Libre y TikTok para dar un veredicto de go, go con flags o no go, según criterios «must» y «nice» evaluados en tres bloques: market fit, operaciones y márgenes, y ecosistema de marca. Una vez validado, el documento B construye buyer persona, niveles de consciencia del cliente, dolores, objeciones reales y ángulos de venta que después alimentan guiones de UGC, landing y estrategia de marca. Todo se muestra en vivo con un ejemplo real (cápsulas de orégano y semilla negra) y se explica paso a paso cómo instalar las skills en Claude.

## Puntos clave

- Franco Lucero presenta las dos skills de Claude para investigar productos: documento A (decide si el producto va o no va) y documento B (arma la investigación de mercado y estrategia comercial) [01:44]
- El documento A exige evidencia real (reseñas de Amazon, Reddit, Mercado Libre, TikTok) antes de invertir tiempo o plata en testear un producto [02:30]
- Vocabulario clave: "must" es un criterio no negociable (2 o más must caídos = no go automático); "nice" suma pero no define; los veredictos posibles son go, go con flags y no go [02:59]-[03:59]
- El documento A puntúa de 1 a 5 tres bloques: market fit (dolor real, precio lógico de mercado, evidencia), operaciones y márgenes (tamaño, packaging, proveedor, margen) y ecosistema de marca (mecanismo único, recompra, bundles) [04:30]-[05:55]
- Instalación de la skill: Configuración > Capacidades > Personalizar > Habilidades > Crear habilidad > subir el .zip (repetir para documento A y documento B) [06:52]-[07:24]
- Flujo de uso: copiar la URL de la landing del producto y pedirle a Claude citando primero /doc-a "quiero validar el siguiente producto con el documento A"; solo si pasa se cita el documento B agregando landing, nombre y biblioteca de anuncios [08:24]-[09:30]
- Caso práctico (cápsulas de orégano + semilla negra): el documento A da score 4/5 en market fit (marcas de EE.UU. invirtiendo fuerte, categoría vendida en Argentina entre 20.000 y 90.000 pesos) con flags en proveedor (resuelto por fabricarse local) y riesgo regulatorio de ANMAT [16:23]-[21:03]
- Recomendación: pasar todos los productos candidatos por esta validación, aunque al final no se use esa marca, porque igual da una idea de mercado y de marca [11:23]-[11:54]
- El documento B arma el boceto del cliente: fuentes consultadas, citas reales de reseñas, 6 clusters de dolor físico, ángulos potenciales y buyer personas detalladas con edad, situación y objeciones [33:01]-[38:19]
- También define niveles de consciencia del cliente (no consciente, consciente del problema, etc.) y ángulos de venta con estructura TOF (hook de identidad, sin nombrar marca), MOF (educar el mecanismo) y BOF (oferta con bundle) [38:19]-[39:45]
- Compara el formato del producto contra la competencia (ej. cápsulas sin sabor vs. gotas con sabor fuerte y menor adherencia) para encontrar el diferenciador [39:45]-[40:39]
- Con el documento B como "documento madre" se pueden pedir después, en el mismo chat, guiones de UGC con IA, ajustes de landing y de precio, para que Claude mantenga el contexto y la coherencia de marca [42:12]-[46:12]

## Conceptos y herramientas

**Conceptos:** [[Validación de producto]] · [[Producto ganador]] · [[Nicho]] · [[Buyer persona]] · [[Dolor del cliente]] · [[Ángulo de venta]] · [[Valor percibido]] · [[UGC]]
**Herramientas:** [[Claude]] · [[TrendTrack]]

## Recursos de esta lección

- [[Skill Claude - doc-a-validator]]
- [[Skill Claude - doc-b-builder]]

## Transcripción

*Transcripción automática con Whisper large-v3. Puede tener errores en nombres propios o términos técnicos.*

**[00:00]** Así que mandale, todo tuyo. Yo, EMU TV. Bueno, para los que no me conocen, yo soy Franco Lucero, empecé a laburar acá con Agustín Torres en su consultoría y voy a estar haciendo toda la parte de proceso con inteligencia artificial, sistema y demás, para automatizar varios procesos, digamos. Y después, nada, en cuanto a mi experiencia, arranqué hace ocho meses, tengo dos tiendas actualmente.

**[00:30]** Alrededor de 200 millones por mes de manera estable y nada eso sería como la introducción para la gente que no me conozca que seguramente es en su mayoría así que lo que vamos a estar viendo hoy es básicamente dos skills son súper completas en cuanto a investigación de productos o sea ustedes hacen el research buscan qué producto les interesa y esta herramienta lo que hace es filtrarles si el producto es bueno o no

**[00:59]** En base a criterios que se encuentran en reseñas de Amazon, Reddit y un montón de investigaciones que lo vamos a estar viendo ahora. Así que, nada, voy a compartir pantalla. Así vamos viendo esto. Hola, Fran, ¿cómo estás? ¿Cómo andamos, Joel? ¿Todo bien? Bien, papá. Escuchá, ¿podrías subir un poco el volumen del micro? Así se escucha un poco más fuerte. A ver. ¿Todos me escuchan bajo, Che? Yo, o no sé si será mi celu, pero por si acaso.

**[01:44]** Bueno, acá armé como una breve explicación de lo que es el documento A y el documento B, que son básicamente

**[02:30]** Justamente el documento A y la otra trata el documento B. Lo que hace el documento A es decidir si el producto va o no va. Dice acá, filtra la idea con evidencia real y dicta go o no go antes de que inviertas meses, plata o tires pauta en un testeo que no va a funcionar. Y después, una vez se valida todo lo que es el documento A, se pasa al documento B, que básicamente nos hace como todo un research para ver cómo se vende ese producto.

**[02:59]** Arma toda la investigación de mercado y la estrategia comercial que alimenta todo lo demás. Después, como vocabulario de los documentos, tenemos acá lo que explica, yo esto lo voy a pasar después para que ustedes lo lean tranquilo, que, bueno, must es como no negociable, o sea, si a vos te tira el research must, significa que es no negociable. Si falla, hay flag roja, dos o más must caídos, es un no go automático. Después tenés nice.

**[03:29]** Que significa que suma, pero no define. Y después tenés, bueno, acá explica un par de cosas que por ahí los dejo que lo lean tranquilo después, para que vayan viendo. Y después tenés todo lo que es el veredicto del documento A. Esto sería go, que dice que pasa con todos los más, con un score de 3 o más. Y una vez que el documento A te tira un go, se avanza a lo que es el documento B. Después también existe lo que es el go con flags, que las flags serían básicamente...

**[03:59]** Si te tiran alguna parte de los bloques que hace el research, te tira que por ahí uno es malo y demás, se analiza, se resuelve y se continúa el documento B. Después tenés directamente el no go, que es como que básicamente el producto no es viable testearlo directamente, así que sería como el vocabulario que se va a estar usando en lo que es la skill. Bueno, acá se explica un poquito.

**[04:30]** Lo que es los tres bloques que se evalúan en el documento A, por ejemplo, que es el market fit, básicamente evalúa todo lo que es la marca de afuera, si la gente está pagando un buen ticket por la solución esa, si el mismo dolor existe acá en Argentina, hace un research de todo lo que es Mercado Libre, Reddit, TikTok local, después el precio necesario es lógico para el mercado local, problemas evergreen, no moda 30 días, señales emocionales, soy yo, me pasa igual.

**[04:58]** Hace como todo un research de todo lo que es el vocabulario en base a reseñas y demás que tiene una persona cuando compra este tipo de productos. Y después tenés, por ejemplo, operaciones y márgenes, te dice el producto es chico, liviano, frágil, te dice las variantes, si vas a tener muchas variantes de productos, después si entra en un packaging estándar, un proveedor, si hay proveedores que puedan llegar a conseguir ese tipo de producto, el postventa.

**[05:28]** Foto real del margen. Después te tira todo el ecosistema de marca, todo el mecanismo único que podés usar, el por qué funciona. Después tenés todo lo que es la recompra, que es súper importante. Después te hace todo lo que es los bundles para subir el OV, todo lo que es ecosistema de marca en general. Después se puede construir una marca alrededor del problema, todo lo que son productos del mismo ecosistema.

**[05:55]** La mentalidad, la calidad que soporta, recompra y demás. Y después se pasa, una vez que todo esto se valide, que lo vamos a estar testeando en un ratito, lo vamos a poner en práctica para que vean, se pasa lo que es el documento B. Básicamente dice qué hace y para qué deja para después. Acá te tira todo lo que es el boceo real de la marca, de la persona, el buyer persona, los niveles de conciencia. Se tiran todos estos detalles.

**[06:23]** Lo van a ir viendo directamente en la práctica, no quiero dar como mucho énfasis, sino que quiero pasar directamente a que lo veamos. Así que tenemos lo que es en Claude, le vamos a juntar un .zip que se lo voy a estar pasando al grupo, o ahí vamos a ver cómo se los mandamos, que son básicamente las dos skills, el documento A y el documento B. Para instalarlo, para el que no sabe, se viene acá a lo que es el Claude normal, configuración, acá se viene a capacidades,

**[06:52]** Y acá abajo donde dice habilidades, le dan a personalizar y acá tienen toda la parte de habilidades, le dan a sumar, crear habilidad y subir una habilidad. En esta parte directamente seleccionan el producto, lo arrastran acá o tocan acá y clickean y lo suben. No sé si ahí alguien iba a hablar. Bueno, una vez que suben el documento A, hacen lo mismo con el documento B, son dos puntos zip que directamente lo arrastran y les queda acá subido, como ven acá.

**[07:24]** Documento de Avaliator, documento de Builder. Después, traje acá unos productos como para que veamos un test. Esto es una plataforma TrendTrack, es como un headhook que se usa, nada más que esta me parece mucho más completa y con muchas más funciones. Como ven acá, explicándolo rápido porque esto ya lo vamos a hablar en algunos módulos, te tira todo lo que son, por ejemplo, de la misma marca.

**[07:54]** Todas las cuentas publicitarias que la están publicitando, como ven tiene un montón, este tiene 388 anuncios prendidos con otro nombre, acá otro nombre, se tira literal todo, después te tira cuántos tienen en TikTok, en Google Ads, los flujos de email. A nivel research y espía, si pueden pagar Trend Track es mucho más completo que Headhook. Así que, eso como para que lo tengan en cuenta, pero el que tiene Headhook es prácticamente lo mismo.

**[08:24]** Sirve para espiar marcas. Traje esta, por ejemplo, para que le apliquemos las skills y veamos, que es como el orégano. Lo que se hace es directamente entrar a la página del producto. Acá tienen todo lo que es la landing del producto, por ejemplo. Copian la URL, vienen a Claude, una vez que ya subieron las skills, obviamente, y, por ejemplo, ponen quiero validar

**[08:58]** El siguiente producto con el documento A. Y citan el documento. Esto se cita en el slash doc A. Siempre el documento A es el primero que se adjunta porque es el que te hace todo el análisis grueso para ver si el producto pasa o no pasa. Después, una vez que el producto pase y esté validado, citan el documento B. Y acá le adjuntan todos los detalles que ustedes le pueden adjuntar. Le tiran ahí la landing del producto.

**[09:30]** Le tiran el nombre. Después si le pueden tirar la biblioteca de anuncios también. Pero nada, con eso ya se les va a hacer. Acá pueden usar, con el sonnet anda bastante bien. Es más, lo vamos a hacer con este para que sea más rápido. Y esto básicamente, nada, le va a tirar como todo el análisis que ahí lo vamos a ir viendo. Pero bueno, lo que es dentro de la skill del documento A, se encuentra todo lo que estábamos explicando recién en todo esto, que analiza absolutamente todo.

**[10:09]** Está muy completo, todo lo que es Reddit, todo, para que no se deje nada como fuera y se analice completo, digamos. Así que nada, ahí vamos a esperar a ver qué nos da. Mientras tanto, no sé si alguno tiene alguna consulta, alguna duda. Los documentos se los voy a estar pasando ahí a lo que es el WhatsApp o lo vamos a estar juntando a un drive para que lo puedan descargar. Bueno, acá ya empiezan a hacernos preguntas, por ejemplo, ¿por qué te interesa esta idea puntualmente? Nada, le dicen que la vieron en...

**[10:51]** Fuerte o pautando fuerte en lo que es la biblioteca de anuncio. Después este producto es para, y acá te pregunta si es para una marca separada, aparte el ecosistema de una marca existente. Ponen que es una marca nueva y ya va a empezar a hacer toda la investigación. Es normal que les haga algunas preguntas para entender un poco, así que eso lo resuelven rápido. Después no sé si hay alguna duda.

**[11:23]** Yo quería consultar, hace poco, la semana pasada me uní a lo que es el programa, y quería consultar si el producto que elegimos ahora, por lo menos los que recién empezaron, si recomendás pasarlo por estas herramientas. Sí, yo recomiendo, e incluso yo mismo lo hago, es pasarlo siempre por esta herramienta para que, de última, si no lo vas a aplicar, mínimo te da como una idea de marca y te da como una idea general del mercado, entonces como que está muy bueno.

**[11:54]** Bien, genial, gracias. A nivel análisis, yo les recomiendo a todos que todos los productos que lo puedan pasar por estas skills, lo pasen. Ven que acá les hace todo el research de todo lo que es TikTok, de todo lo que es Mercado Libre, acá todo lo que es Anmat. Esto lo tiene agregado toda la parte de Anmat, pero bueno, es como una flag que seguramente les tire que nosotros para hacer productos químicos, ya saben, tienen el laboratorio.

**[12:21]** Yo, amigo, ¿sabés que no me quedó claro cómo conectar la skill a Claude?

**[12:57]** Vienen acá configuración, en configuración vienen acá capacidades y en capacidades bajan al todo y les aparece esto que es habilidades, las habilidades se han movido a personalizar. Tocan acá personalizar y acá les tira todas las habilidades que ustedes le pueden subir. Entonces nada, suben acá, agregar una habilidad, crear habilidad y subir una habilidad. Y acá directamente o arrastran el archivo o tocan acá y lo seleccionan.

**[13:26]** Obviamente el archivo que le vamos a pasar posteriormente a esta llamada. Que bueno, esto es todo lo que contiene la skill, si la quieren leer, fíjense que tiene todo el análisis, todo el rol que cumple básicamente. Igual tranqui chicos, esta clase está siendo grabada, así que todo lo que es funcionamiento, técnico, todo eso lo van a repasar, incluso no solamente va a estar la llamada, sino el documento, el resumen, como para que también no tengan que leer toda la llamada, sino leerlo también.

**[13:57]** Pero bueno, hablando un poco más de ese documento, la palabra específica es research. Es como realmente saber si el producto es bueno por muchas cosas. Franco lo que hizo era agregar reseñas. Muchos usan Reddit, no sé si alguien de acá usa Reddit, pero se usa mucho Reddit para, no sé, para ver consultas reales de personas reales, no solamente para vender.

**[14:22]** Entonces, este documento es justamente para confirmar si realmente el dolor del producto en sí es existente y se soluciona de verdad. Y se los resume todo, todo, todo en esa habilidad. Por eso es que está tan bueno este documento y después el final también. Claro, en resumen es eso, literal. O sea, hacer un research y ver si realmente vale la pena el producto o no. Y bueno, ver por qué sí y por qué no. Que básicamente te lo tira acá cuando...

**[14:54]** Aplicá el documento. Esto tarda un poco, lo tendría que haber hecho con el otro, pero si pueden usar el más complejo que sea, mejor, porque les va a hacer el análisis mucho más completo. Igual, está bien que tarde, o sea, es mejor que se vea que tarde y que justamente esté leyendo absolutamente todo. Bueno, ahí ya está terminando igual, ¿no? Sí, está terminando de armar todo. Franco, ¿todo este archivo y esta cosa lo armaste vos?

**[15:53]** Sí, lo armé, lo saqué de otras schools y lo moldé, digamos, a la investigación de mercado que sirve acá. Está muy bueno, se ve muy completo la verdad. Pero sí, es como la base de info de todos lados. Bueno, acá te tira como todo el documento y todo el análisis, digamos, de la validación completa. Bueno, acá te explica lo que es el producto, te explica lo que es el nicho.

**[16:23]** Te explica la Argentina con texto, dice marca separada porque interesa a Franco, que está pegando fuerte, bueno. Y acá te tira todo lo que es el checklist global que te dice básicamente qué pasa con flags. O sea, tiene algunas flags que habría que resolver, pero el producto pasa todo lo que es el análisis. Así que nada, había que leer todo esto. Por ejemplo, acá te pregunta mecanismo único y alto valor percibido. Te tira un must y un score 4 sobre 5.

**[16:51]** Que te dice combo de orégano más semilla negra, es diferenciador versus la oferta argentina actual, mono ingrediente. Aunque en Estados Unidos ya lo replican varias marcas. Bueno acá te tira todo básicamente, vamos a ver, acepta break even, definido, calidad, marca pensada para años, te tira por ejemplo 3 sobre 5, te dice marca nueva, todavía sin visión de ecosistema más allá de este escudo. Después te tira todo lo que es los bloques que les explicaba recién en el...

**[17:23]** Archivo ese que había armado, que te dice, bueno, un score promedio 4 sobre 5, o sea que es un score bueno, y más fallado ninguno. Te dice marcas de afuera invirtiendo fuerte, 4 sobre 5, o sea que hay marcas de afuera invirtiendo fuerte. Gente que paga buen ticket, 4 sobre 5 también. Resilia cobra 30 a 89 dólares según el pack. En Argentina la categoría 6 teoreano ya factura en el rango de 20 mil a 90 mil pesos.

**[17:52]** Así que, bueno, a tenerlo en cuenta que se puede vender un ticket alto o un middle ticket, digamos, de 60 lucas, por ejemplo, que eso está muy bueno porque por ahí hay muchos fármacos que vas a pasar por esta skill que después te das cuenta que la venden en farmacia por 10 lucas y que por ahí el diferenciador que tenés que tener es mucho más grande que por ahí con un producto así. Después te dice, bueno, mismo nicho Dolor en Argentina, te dice que sí, que ya existe, que hay demanda

**[18:23]** Prova, Natier, marca local, más mil reviews. Bueno, acá te tira todas las marcas que están vendiendo acá en Argentina y que le está yendo bien, o sea que el dolor existe y que se está vendiendo. Después, bueno, el precio lógico para el mercado. Papel Sierra, bueno, esto te lo tira como si vos lo fueses a importar, pero nosotros lo fabricamos acá localmente, así que no habría problema con eso. Después, bueno, te dice Evergreen.

**[18:51]** Que no es moda, te tira categoría de bienestar, inmunidad, sostenida en el tiempo. No es un fenómeno de 30 días, es decir que el producto es sostenible durante el tiempo. Después de evidencia recopilada, te tira en TikTok shop. Que hay un competidor, microingrediente, acumula 62.000 ventas en formato combo. Acá te tira más de todo, de dónde sacó la evidencia, Mercado Libre, Mercado Libre Argentina.

**[19:18]** Buscando el mismo nombre en Melia, Argentina, prácticamente sin resultados específicos, Semilla Negra es un invento nuevo para el mercado argentino. O sea que este producto aprueba bastante bien, digamos. Este es como el bloque 1, que es el market feed. Después tenés el bloque 2, que serían operaciones y márgenes, que pasa, pero con pendientes. Habría que ver dónde es que tiene esas pendientes, que bueno, acá por ejemplo es el proveedor.

**[19:43]** Lo cual nosotros no le especificamos directamente desde un inicio que lo podríamos haber hecho y haberle dicho tema proveedor ya lo tenemos resuelto entonces esto directamente no se lo hubiese tirado porque es como el producto que estamos viendo es un químico como ven es un doy pack con unas semillas de orégano con unas cápsulas perdón de orégano y esto se puede fabricar acá localmente así que no habría drama con el tema proveedor.

**[20:10]** Después te dice el margen, aplicando la tabla del documento A, un costo FOP tópico, bueno acá te tira toda data, después bloque 3, ecosistema de marca, pasa con flags. El mecanismo 2 en 1 no es único a nivel mundial, varias marcas de Estados Unidos lo copiaron de Resilia, pero sí sería el primero en Argentina, gana ventana de tiempo. Bueno, acá te tiene un montón de data que es para leer y analizar porque está muy bueno.

**[20:37]** Y te tira realmente con data validada por qué el producto puede funcionar y por qué no, y qué flags presenta, o sea, qué problemas tenés para resolver, por ejemplo, y que el producto sea un 10 de 10. Bueno, acá tenés el riesgo regulatorio, esto es lo que le hablaba anteriormente. Pero bueno, en términos generales, el producto pasa, digamos, el checklist global.

**[21:03]** Pasa con algunas flags a resolver como vimos el proveedor y temas regulatorios o sea que no es problema eso y una vez que les convence a ustedes realmente el producto directamente le citan el documento B y le dicen listo tengo la parte regulatoria y del proveedor resuelto con el documento B y le citan el documento B y ya ahora le haría como todo el proceso de investigación de marca para ver en

**[21:41]** ¿A qué lado lo pueden apuntar ustedes y cómo sería la manera correcta de venderlo acá en Argentina? Que bueno, también va a tardar un ratito más, así que no sé si a alguno le quedó alguna duda con respecto a esto. Vicentino había dejado una duda en el chat. La próxima la pongo en la otra pantalla. La verdad que depende, si tenés la posibilidad de pasarte al pro,

**[22:21]** Está muy bueno. Ahí Santino pregunta si vale la pena ugradear el plan de Claude. Y la verdad que si lo podés ugradear está muy bueno y se pueden hacer un montón de cosas. Así que más si usás Claude Code, Ponele y toda la onda, ugradearlo vale la pena 100%. Ahora con el de 20 dólares también se pueden hacer un montón de cosas. Daniel, una duda. Entré recién a la mentoría. ¿Habría que hacer algún cambio a este documento para que aplique para Colombia?

**[23:02]** A términos generales lo podés usar de igual manera, porque la info y la data y los mercados son muy parecidos o muy similares, pero sí habría que hacerle ahí algunas modificaciones, habría que verlo y se lo hacemos, por ahí para que busque directamente y apunte a lo que es Colombia, pero lo podés usar de igual manera.

**[23:35]** Arranco de cero, no tengo nada todavía. ¿Tenés review o data propia? No, todavía no vendí nada de esto. Ahí responden las preguntas que le hacen. ¿Qué significa? ¿Cómo, Eduardo? Bueno, esto tarda un rato, como vieron. Y este documento, el documento B, que les arma, es súper completo y tiene un montón de data y un montón de info que está muy buena para que la analicen. En base a eso, yo, por ejemplo, hago la investigación.

**[24:19]** Y en base a eso saco lo que es UGC, UGC real o UGC con IA, o armo los guiones a partir de este documento porque es como, te detalla literalmente los dolores puntuales que tiene el cliente, porque busca reseñas en Reddit, qué opina la gente en Mercado Libre, entonces como que matás todas las objeciones en base a la reseña real de la gente, digamos. Más que nada eso sirve mucho, chicos, porque la gente se identifica también con situaciones, no solamente con...

**[25:01]** ¡Suscríbete al canal!

**[25:31]** ¡Suscríbete al canal!

**[26:01]** Pueden hacer directamente videos de cero, que bueno, justamente ya se están haciendo los videos de UGC, digo, los videos con IE directamente, creo que para esta semana ya va a estar, porque arman de cero, y arman una marca totalmente de cero. Con la mano derecha ya saben qué es lo que hay acá, qué es lo que no hay, buscan un hueco en el mercado y se meten directamente ahí. Van directamente por los ángulos de dolores y no tanto, no sé.

**[26:29]** Solamente improvisando o copiando. Que está bien copiar porque se supone que son ángulos que funcionan, pero también está bueno testear nuevos ángulos constantemente. Que no sé si eso te pasó, por ejemplo, Franco, de que ya hayas testeado todo teniendo en cuenta la marca de referencia y ya solamente un momento te quedaste sin ángulos. Y esto te ayudó en eso. Claro, una vez que ya replicaste y ya probaste los formatos y cosas que funcionan afuera y las testeaste acá en Argentina,

**[26:58]** Y te quedaste sin idea o sin cosa para hacer, justamente lo mejor es acceder a estos documentos que te genera porque directamente te da como dolores muy puntuales, entonces agrega mucho valor percibido al decir al cliente directamente le tocas el punto en base a las objeciones que presentan en otras plataformas. Por eso está súper completo y además ya para armar una marca.

**[27:26]** También necesitás esa idea creativa de uno, digamos. O sea, no podés generar una marca estable solamente replicando lo que existe afuera. Porque si ellos no largan más nada vos te quedaste sin contenido, digamos. Y respondiendo ahí a lo de Claude, chicos, o sea, pueden arrancar con el básico, pero creo que hacen un par de consultas más y ya se termina. Capaz cuando apenas arrancan, sí, o sea, arranquen con el básico, pero la verdad es una buena inversión.

**[27:57]** Pueden tener como 100 empleados usando bien Claude, así que arranquen con lo básico y vayan subiendo a base de sus necesidades, más que nada. Eso lo van analizando ustedes según el uso que le dan. No sé, si usan el más básico pero todo el tiempo se quedan sin crédito diario, y bueno, ya hagan la inversión de ir a uno más. Depende del uso de cada uno. Sí, con el básico, bueno, se pueden hacer un par de cosas, pero si tienen la posibilidad de pasarse al...

**[28:31]** A la segunda opción de 100 dólares o al de 200, ni la duden porque les sale mucho más rentable. O sea, vamos a ver toda la parte de automatización de WhatsApp, todas esas cosas que por ahí tienen que contratar una persona real para que lo resuelva, que se lo va a resolver directamente un agente y les sale muchísimo más barato que andar pagando y delegando absolutamente todo. Así que a nivel inversión es una red contra inversión y está muy buena.

**[29:05]** Hola, buenas tardes. Yo tengo una pregunta, soy nueva, estoy en medio de la etapa de buscar producto. Esta herramienta, estas habilidades, ¿habría que usarlas con pocos productos que estamos como más convencidos de ir o directamente me conviene más solo con toda la lista de productos que vengo armando desde ayer? Y ahí también va a depender el plan que tengas.

**[29:33]** De Claude, porque si lo usás con todos, por ejemplo, por ahí el más básico no te va a alcanzar y se te van a gastar los puntos rapidísimo, pero si tenés la posibilidad de pagar el de 100 o el de 200 y podés pasarlos a todos los productos, es lo mejor, o sea, te sacás las dudas directamente de todos. Perfecto, gracias. Ahora, en caso de que estés convencida con... Una cosa, ¿la parte creativa también te va a dar recomendaciones o solo te nombra los dolores? No, no, te da recomendaciones, te tira...

**[30:06]** Varias cosas que ahí la vamos a ver cuando nos genere el documento, pero si te resuelve tanto dolores, ángulos, por dónde atacar la marca, dónde está el hueco de mercado, nada, está muy completo. Muy bien. Está generando todo, tarda un rato. Bueno, ahí nos terminó de generar todo el documento B. Que bueno, acá nos genera un documento súper largo. Está buenísimo leer porque es tipo de producto que vamos a alargar y está bueno prestarle atención a todo. Una vez que larguen producto,

**[31:34]** Lárguenlo conscientemente lo que vendan. O sea, sepan lo que venden y sepan al público que apuntan porque es súper importante conectar con el cliente y de ese modo bajás CPM, bajás CPA, bajás todas las métricas relevantes que hay porque justamente vas a atacar cosas puntuales y vos vas a estar sabiendo lo que estás vendiendo. O sea, vas a saber cómo conectar con ese cliente. Así que nada. Bueno, acá nos tira todo lo que es.

**[32:04]** El boceo del cliente, digamos. Bueno, acá nos tiró que por política de uso de Claude no se producen bloques extensos de reseñas con derechos de autor. Bueno, acá Claude, esto es la primera que me lo tira. Por ahí puede ser el plan, pero nada, nos dice básicamente que no nos va a tirar como reseñas para agregar a nuestra tienda. Después tenemos todo lo que es la sección 1, datos del caso. Bueno, acá te tira todo lo que es producto, nicho.

**[32:33]** El país, Argentina, avatar principal, el problema que resuelve, baja defensa que se traduce en el resfrío, molestias recurrentes, sobre todo en invierno. El resultado, sentirse con más resistencia y energía pareja sin estar siempre cayéndose con algo. El mecanismo único, candidato, primer combo, orégano más semilla negra en softgel, no en gotas, disponible en Argentina. Se refina en sección 8.

**[33:01]** Precio observado en el mercado, Argentina ronda entre 20.000 y 90.000 pesos argentinos según la marca formato. Y bueno, en Estados Unidos entre 30 dólares y 90 dólares según el pack. Después tenés los competidores directos acá en Argentina, que esto es lo que habíamos visto en el documento A. Después tenés la regulación aplicable, bueno, lo que es toda la parte de Armat. Y después pasa a la sección 2, que es como el boceo de los clientes.

**[33:28]** ¿Qué te tira? Bueno, fuentes consultadas, te dice de dónde sacó toda la información y todo el banco del boceo, más los patrones, más citas puntuales. Esto como lo que la gente más reseña o escribe, por ejemplo, una vez que compra el producto. Acá te dice que el cliente escribe el cobro de la suscripción, cómo nos robaron, exige reembolso inmediato. Bueno, acá tiró como el modelo de suscripción que se suele usar en Estados Unidos, que no sé qué problema habrá tenido, pero después tenés un reclamo recurrente.

**[33:59]** Que dice también, otro problema con la suscripción. Esto te dice hinchazón, nota mejor en su digestión en menos de dos semanas y deja de preocuparse por cada comida. Acá en Amazon, una usuaria relata que dejó de sentir esa sensación de hinchada en la zona media del cuerpo. Es que ya acá les va tirando como información donde ustedes dicen, bueno, zona media del cuerpo, hinchazón, ya tienen como, pueden generar videos muy puntuales sobre el dolor.

**[34:28]** Que eso está muy bueno. Después, nada, te dice acá otra reseña. Mejora notable en la energía diaria, menos niebla mental y menos bajón de la tarde. Después en TikTok, ahora dice haber mejorado su alimentación y que el aceite de orégano suma a esos cambios. Bueno, acá te tira más reseñas de todos lados, de Mercado Libre. Bueno, acá tienen la parte de sabor, por ejemplo. Usuaria toma aceite diluido en aceite de oliva por el sabor.

**[34:58]** Para apuntar también a la parte del sabor del producto. Acá esto lo tienen que leer y analizar todo. Después tienen, bueno, 6 clusters por dolor físico. Tenés como toda la gente que te puede llevar a comprar. Defensas bajas, resfrío recurrente. Acá tenés resfrío, garganta, gripe estacional que vuelve una y otra vez, busca estacional, marcada en invierno. Acá tenés tipo el ángulo potencial, que es defensas bajas. Directamente hablarle a las personas que...

**[35:27]** Tienen defensa baja y tienen quizás estos síntomas. Después tenés la sensación de panza hinchada, mejoras reportadas en regularidad intestinal. Tenés el ángulo, que es la panza hinchada, ángulo bajón de la tarde, ángulo se acabó el asco, que esto apunta a todo lo que es la parte del sabor. Después tenés compra clara, sin sorpresas. El mayor resumen de queja del benchmark de Sicilia no es el producto, es el cobro recurrente no claro.

**[35:57]** Bueno, esto también habla de la parte de las suscripciones. Después, bueno, tenés la sección 3, que es el destilado accionable, el dolor principal, serían las defensas bajas que se traducen en el resfrío, bueno, todo eso que vimos. Y después tenés toda la parte de dolores secundarios, hinchazón, cansancio, bajón de energía en la tarde, rechazo del sabor, desconfianza en compra directa de sitios nuevos, sensibilidad estomacal al tomarlos en ayunas. Después tenés la cadena de consecuencias del dolor principal, el problema.

**[36:26]** La consecuencia diaria, se despierta con la garganta áspera, arranca el día ya cansada. Claro que tiene un montón de data como para que literal armen videos directamente de esto. A una persona que se despierta con la garganta áspera y arranca el día cansada. Después tenés todo el costo emocional, sensación de estar siempre a medio de funcionar, el costo social, falta al laburo, pide cambios de planes con amigos, familia. Después tenés las objeciones, alternativas probadas y cómo se destruyen.

**[36:54]** Objeción, por ejemplo, una de las objeciones es la gota de aceite de orégano saben horrible. La alternativa probada es gotas líquidas. ¿Por qué falló? Rechazo de sabor repetido, varias reseñas mencionan que hay que diluirlo o acostumbrarse. ¿Cómo se destruye? Con otro formato, digamos, softgel, sin sabor, comparativa directa versus gotas en el ángulo del mecanismo. ¿Alguna otra objeción? A ver...

**[37:20]** Me puede hacer mal al estómago, ponerles una objeción que encontró en el análisis que hizo. Y una alternativa probada es objeción anticipatoria de tolerabilidad. ¿Por qué falló? Dice, el patrón real así es si se toma en ayunas. Entonces podés apuntar a un ángulo de que hay que tomarlo junto a una comida, por ejemplo. Después tenés todo el lenguaje exacto, palabras o frases repetidas que encontró.

**[37:51]** Se me fue la hinchazón, panza liviana, bajón de la tarde, sabor horrible, me cobraron sin avisar. Bueno, esto es toda la parte de solución, no estoy todo el tiempo resfriada. Bueno, acá te dice los ángulos que podés atacar. Y acá te dice, básicamente, te da como una buyer persona, que te dice la persona 1, la que no se puede enfermar. Te dice de 34 a 42 años, madre con hijos, sin edad escolar. Te explica toda la situación actual, tipo, te detalla todo el...

**[38:19]** Los problemas, objeciones, dolores que puede llegar a tener ese buyer persona y cómo vos se lo podés resolver. Después, una persona 2, la que entrena pero anda hinchada, y persona 3, la que no puede bajar el ritmo. Después tenés sección 5, nivel de conciencia y ejecución. Nivel no consciente, o sea, esto para un embudo de ventas, viene joya. O le hablás a la parte no consciente que piensa algo no anda bien pero no sé qué, siente el síntoma sin nombrarlo. O sea, le hablás a una persona que...

**[38:49]** No conoce bien a qué se debe su dolor y vos básicamente le traes la solución. Esto es un embudo para armar que está muy bueno. Después la sección 6, ángulos de venta. También acá te da para el ángulo 1, que sería defensa baja, no estar siempre resfriada. Acá incluso te explica toda la parte de embudo de venta, TOF, hook de identidad, más síntomas sin nombrar la marca todavía. O sea, para una persona que no conoce mucho de...

**[39:18]** Del producto ni nada, ni siquiera se lo nombrás, sino que la nutrís directamente, después como MOF, la educás del mecanismo, más comparativa, versus tomar vitamina C reactivamente, por ejemplo. Y después, ya para alguien que conoce tu marca, directamente le presentás una oferta más un bundle por dos, por tres, con foco en temporada completa, no solo una compra. Tipo, esto está buenísimo para que lo lean, lo entiendan.

**[39:45]** Pero literal le explica toda la parte de embudo de venta, todas las objeciones que puede llegar a tener el cliente, todos los dolores, absolutamente todo. Acá, bueno, con otro ángulo. Acá con otro ángulo. Después, nada, sección 7, inventario de prof. Acá te da como la comparativa de formato, descripción gotas, tiene sabor fuerte, abandono versus cápsulas.

**[40:11]** Sin sabor, mayor adherencia, es decir, que ustedes pueden hacer videos directamente comparando su producto con otro que se venda en gotas, por ejemplo, y ustedes lo venden en cápsulas. Entonces le ponen que no tiene sabor, tiene mayor adherencia, funciona mejor, no sé, todo lo que es. Toda la data que hay acá les brinda un montón de herramientas para que puedan revisar. Después, bueno, acá te dice la fuente de dónde sacó esto, que es como las reseñas de Meli.

**[40:39]** Natier, más reseñas, Black Set Oil de afuera. Para qué ángulo sirve mejor, acá te explica el ángulo 4 formato y apoyo en ángulo 1 y 2. Después te tira tipo la competencia, el gap y la diferenciación que tenés como el snapshot de competidores. Acá te dice la marca Natier de Argentina, vende entre 7.000 y 42.000 pesos. Tiene un aceite de orégano tradicional. El mecanismo que usan, la oferta.

**[41:08]** Sin bandas claros y las debilidades. Tiene un sabor fuerte porque lo venden en gotas, un copy con claims ilegales en varias publicaciones, riesgo de marca, no de producto. Te tira literalmente todo esto para que se sienten, lo lean y en base a esto directamente, en base a este documento después le pueden pedir a Claude que les arme directamente los guiones para mandar a hacer UGC con IA y los va a entender porque él mismo hizo todo el research, digamos.

**[41:37]** Y toda la data que está acá. Pero sería como básicamente eso, la parte de skills y de búsqueda de mercado para que ustedes puedan elaborar una marca, si quieren desde cero, o para complementar la marca que ustedes ya van a tirar, digamos. No sé si quedó alguna duda, algo que tengan para decirme. Yo diría que apuntes, o sea, con tu experiencia en este documento. Ok, tengo eso. Franco, ¿qué hace una vez que ya tiene toda esa información?

**[42:12]** Con esta información del documento, ¿cuáles son? O sea, básico, digamos, no completo todo punto por punto, pero ¿cuál es tu plan de acción después de tener todo esto, por ejemplo? Yo con estos documentos directamente los suelo usar para armar directamente la marca desde cero, o sea, fijarme qué precios son acordes para, ahí hago toda la parte de costos para ver.

**[42:40]** Que quede acorde no sobre vender un precio súper caro ni un precio súper barato, teniendo en cuenta que este producto se puede vender caro por el diferencial y el mecanismo único que tiene, que te lo dice el propio documento. Armo toda la parte de la landing, todo en base a esto básicamente. Y después, nada, soy mucho de armar directamente UGC con este documento.

**[43:06]** Y directamente lo armo en el mismo chat que hice el documento, por ejemplo, le digo acá el Claude. Lo vamos a hacer con un prompt súper fácil y sencillo, pero pueden elaborarlo un poco más y entender a qué le quieren hablar, pero no sé. Por ejemplo, vamos a decirle que nos arme algunos guiones para el ángulo 1. Necesito armar UGC con IA para el ángulo 1.

**[43:39]** Quiero que me escribas el avatar que sería conveniente desarrollar en cuanto a la edad y dolores y después tres guiones para armar UGC con IA coherente y que ataque a todas las objeciones.

**[44:12]** Que pueda llegar a tener mi buyer persona. Bueno esto es idealmente le escriben más cosas pero nada para hacerlo rápido vamos a armar ahí y yo esto bueno toda la parte de UGC con IA después ahí Agus tiene la data de cómo hacerlo pero la pueden desarrollar usted o delegarla que se los hagan y le pasan literal el guión y ya tiene como contexto y memoria de qué es lo que desarrolló y por qué estos guiones son buenos.

**[44:43]** Obviamente yo absolutamente todo lo que me dé acá, como los guiones que me da acá, los desarrollo y los armo a mi manera y a mi gusto en algunos detalles, no es que se tienen que basar 100% en la inteligencia artificial, porque por ahí está bueno tener como ese criterio propio de decir, capaz que te di una palabra que no se utiliza mucho, cambiársela, tipo prestar atención en todo lo que se, a lo que respecta armar.

**[45:11]** marca o armar productos o largar algo pero nada acá se pueden guiar absolutamente de todo o sea en base a esto arman todo lo que es la landing que ya vamos a ver el módulo que estoy grabando para la school directamente conectar cloud code a Shopify y hacer una landing super coherente e incluso en base a este documento por ejemplo después nada como otro tip

**[45:42]** Por así decirlo, yo suelo, dependiendo el ángulo y el video que uso, lo redirijo a una landing distinta. Por ahí es la misma landing, por ejemplo, esta, pero qué sé yo, acá habla de la hinchazón, y si yo en el video hablo de la persona que está cansada, directamente toco los claims de una persona que esté cansada. Entonces como que al cliente directamente lo hace sentir mucho más parte del problema y le matás todas las objeciones que tiene. Que eso con Claude se hace...

**[46:12]** Rapidísimo, literal, se duplica la landing, se cambian los claims y te lo hacen en menos de 10 minutos. Que toda esa parte la vamos a estar viendo ahí en la School de Abus y en llamadas para que puedan básicamente hacer todo casi automatizado, porque si bien, como digo, hay que tener un poco de criterio y saber qué cosas están buenas, qué cosas están malas, pero todo este documento y las dos skills que están, están desarrolladas en base.

**[46:41]** Este, recuerden chicos, es un documento madre, o sea, es para que se apalanquen a todo lo que necesiten después de haber hecho esto, como dijo Franco, guiones, páginas, temas, ángulos, o sea, va a ser su documento que lo van a usar para todo, que lo van a poder adjuntarlo para cada pregunta.

**[47:12]** Para cada cosa que necesiten. Así que, más que nada, para no marearse, no adelantarse algo, esto es como el documento principal que van a usar a partir de ahora de que, cuando ya eligieron una marca. Y está todo, que es todo lo que hablamos a la hora de elegir un producto. Obviamente antes vemos unas cosas básicas, por ejemplo, que esté validado, con o sin anuncios, que ya veamos un poco, obviamente, ahí entra la parte

**[47:41]** ¡Suscríbete al canal!

**[48:11]** A partir de ahora este documento va a ser como la palanca de todo lo que viene después. Y bueno, no sé si tenés para darnos un consejo franco de en qué más podemos usarlo, cómo usarlo y en general, ¿no? Y este, o sea, yo por ejemplo cuando hago todo el research de marca lo uso y lo adjunto a todo. O sea, yo voy a hacerle una pregunta al Claude, ponerle en otro chat o lo que sea, directamente para que tenga como referencia de qué trata mi marca.

**[48:41]** ¿Cuál es mi diferenciador y demás? Le adjunto el documento y le pregunto. O sea, solamente para que tenga un análisis, no hace falta que sea ley hacer absolutamente todo bajo este documento, porque incluso la metodología de seguir replicando videos de afuera y largar marca sigue sirviendo, pero llega un punto donde si afuera no largan videos, no largan cosas y ustedes no desarrollan,

**[49:06]** Su marca pasa a ser muy inestable y demás, y justamente para eso está el documento B y el documento A, para que ustedes armen marca y armen video y desarrollen ideas creativas en función a eso. Acá ponen los guiones que me dio, no los especifique yo, pero bueno, es para un público muy caliente, fíjate que son súper cortos y nos tiran ahí como un diferenciador.

**[49:35]** Así que nada, acá les expliqué que me gustaría nutrir directamente a la gente con videos mucho más largos, así que nada, ahí vamos a ver qué nos desarrolla. Tarda un poquito, pero todo el análisis que te hace marca, la verdad que está, no sé qué opinás vos, Agus. No, no, está todo perfecto. Los guiones después lo implementaremos seguramente algo más específico para cada situación, junto también con la parte de la página, así que tranqui.

**[50:06]** Tranqui con eso. Y bueno chicos, alguna duda o consulta que quieran hacerle Franco, recuerden que él solamente va a estar dando al menos una clase semanal con ustedes. Obviamente Franco sabe de todo, de nuevo, tiene marcas facturando 200 palos arriba por mes, entonces las clases de dudas van a ser para todo, pero él se apalanca de todo esto que es con la guía más que nada para usarla a su favor, no es para...

**[50:35]** Porque está aburrido o algo así. Así que eso para que ya lo sepan. Y bueno, no sé, dudas, consultas para Franco, que ya quieran hacerle sobre esto, algo que quieran saber. Yo le quería consultar el tema de porcentajes, cuánto porcentaje tiene que funcione con este método, nada, validar o pegar un producto.
