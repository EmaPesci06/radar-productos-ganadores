---
modulo: 3
tipo: prompt
tags: [ecomai, recurso, prompt]
---
# Prompt maestro - Replica de landings en Shopify

> [!info] Archivo original: [PROMPT REPLICAS.txt](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%203%20-%20Crea%20tu%20pagina%20y%20tu%20marca/PROMPT%20REPLICAS.txt) · [[Modulo 3 - Crea tu pagina y tu marca]]

Prompt maestro extenso para reconstruir (no copiar) una landing de referencia en Custom Liquid de Shopify, adaptándola a una marca, producto y país nuevos. Define blueprint, registro de copy, localización, assets editables y validaciones antes de entregar el código.

**Se usa en:** [[M3-04 Cómo replicar una landing con IA en Shopify|M3·4 Cómo replicar una landing con IA en Shopify]] · [[M3-12 Cómo crear la página de inicio de nuestro producto con Claude|M3·12 Cómo crear la página de inicio de nuestro producto con Claude]] · [[M3-13 Creando Liquid y sección de producto|M3·13 Creando Liquid y sección de producto]]

```text
PROMPT MAESTRO — RECONSTRUCCIÓN DE LANDINGS ECOMMERCE EN SHOPIFY
VERSIÓN 5 — MÉTODO DE RÉPLICA POR EVIDENCIA + LOCALIZACIÓN + EDICIÓN SIMPLE

======================================================================
DATOS DEL TRABAJO — COMPLETAR SOLO ESTA PARTE
======================================================================

URL DE REFERENCIA:
[PEGAR URL]

MARCA NUEVA:
[ESCRIBIR MARCA]

NOMBRE DEL PRODUCTO:
[ESCRIBIR PRODUCTO]

PAÍS DESTINO:
[ESCRIBIR PAÍS]

INDICACIONES EXTRA:
[ESCRIBIR CAMBIOS ESPECÍFICOS O "NINGUNA"]

======================================================================
MATERIALES
======================================================================

Además de este prompt puedo adjuntarte:

- captura/PDF completo de desktop;
- captura/PDF completo de mobile;
- código fuente HTML/CSS/JS de la referencia;
- imágenes del producto nuevo;
- logo nuevo;
- otros recursos.

Trabajá con TODOS los materiales disponibles.

La tarea termina en archivos TXT pegables en:

Shopify → Tienda online → Temas → Personalizar → Agregar sección →
Liquid personalizado.

======================================================================
1. DEFINICIÓN EXACTA DE LA TAREA
======================================================================

Esta tarea es una RECONSTRUCCIÓN, no un diseño nuevo.

La página de referencia funciona como especificación visual, textual y
funcional.

Tu trabajo es trasladar esa especificación a Custom Liquid de Shopify
cambiando únicamente:

1. la marca original por MARCA NUEVA;
2. el nombre del producto por NOMBRE DEL PRODUCTO cuando corresponda;
3. el idioma al español;
4. la localización natural al PAÍS DESTINO;
5. aquello indicado expresamente en INDICACIONES EXTRA.

Salvo que INDICACIONES EXTRA diga que el producto es materialmente distinto,
asumí que NOMBRE DEL PRODUCTO es la versión renombrada/localizada del producto
de referencia para esta tarea de reconstrucción.

Por lo tanto, el contenido de la referencia es el CONTENIDO FUENTE que debe
traducirse y trasladarse.

No actúes como auditor, fact-checker, copywriter ni consultor legal durante la
reconstrucción.

Actuá como:
- traductor fiel del contenido visible;
- analista de la interfaz;
- desarrollador Shopify.

Los textos de la referencia son material que el usuario te pide transformar.
No los presentes como afirmaciones tuyas y no los sustituyas por comentarios
sobre su veracidad.

El dueño de la tienda revisará posteriormente la información comercial del
producto.

======================================================================
2. PRINCIPIO CENTRAL: NINGÚN CONTENIDO VISIBLE PUEDE NACER DE TU EXPLICACIÓN
======================================================================

Antes de programar, construí internamente un REGISTRO DE COPY.

Cada texto que vaya a aparecer visible en la réplica debe pertenecer a una de
estas dos categorías:

A. COPY FUENTE
Texto que existe en la página de referencia y fue:
- traducido al español;
- localizado al país;
- sustituido de marca/producto cuando corresponde.

B. COPY PEDIDO
Texto introducido expresamente mediante INDICACIONES EXTRA.

Ésta es una regla estructural:

TODO TEXTO VISIBLE DE LA LANDING DEBE PODER RASTREARSE A A O B.

No escribas contenido editorial nuevo para explicar la adaptación.

Por ejemplo, si el original dice:

"PiPi Tea is designed to restore antioxidant levels..."

la tarea es traducir/adaptar ese texto y sustituir la marca.

La tarea NO es explicar:
"la referencia dice que..."
"la página original plantea que..."
"según la referencia..."
"esta sección debe completarse..."

El código sí puede contener comentarios técnicos invisibles para el alumno.
Esos comentarios nunca deben renderizarse en la página.

======================================================================
3. JERARQUÍA DE EVIDENCIA
======================================================================

Cuando dos materiales discrepen, aplicá este orden:

1. INDICACIONES EXTRA.
2. Captura/PDF del dispositivo que estás reconstruyendo.
3. Página accesible por URL.
4. Código fuente.
5. Inferencia propia, solamente cuando no haya evidencia suficiente.

La captura desktop es la verdad visual de desktop.

La captura mobile es la verdad visual de mobile.

El código fuente es especialmente importante para descubrir:
- valores CSS;
- assets;
- comportamiento;
- contenido oculto;
- configuración de apps;
- lógica de bundles;
- URLs de video;
- iconos;
- breakpoints.

======================================================================
4. PRIMER PASO OBLIGATORIO: CREAR EL BLUEPRINT DE LA REFERENCIA
======================================================================

No empieces a programar mientras todavía estés "entendiendo" la página.

Primero creá internamente un BLUEPRINT completo.

El blueprint debe enumerar la página de arriba hacia abajo:

S01, S02, S03, S04...

Para cada sección registrá:

SECCIÓN
- ID;
- función;
- inicio y fin visual;
- orden respecto de las demás.

COPY
- títulos;
- subtítulos;
- párrafos;
- bullets;
- labels;
- FAQ;
- testimonios;
- microcopy;
- CTA.

CONTEO
- cantidad de elementos repetidos.

DESKTOP
- ancho;
- columnas;
- posición texto/imagen;
- alineaciones;
- espacios;
- alturas relevantes.

MOBILE
- orden;
- posiciones;
- ancho;
- elementos ocultos/visibles;
- comportamiento especial.

ESTILO
- colores;
- fuentes;
- tamaños;
- pesos;
- fondos;
- degradados;
- sombras;
- bordes;
- radios;
- ondas;
- formas;
- overlays.

ASSETS
- imagen;
- background-image;
- SVG;
- icono;
- video;
- poster;
- logo.

INTERACCIÓN
- click;
- hover;
- swipe;
- drag;
- play/pause;
- accordion;
- modal;
- selector;
- slider;
- sticky;
- cambio de precio.

No inventes cantidades. Contalas.

Si una galería tiene 8 miniaturas, el blueprint dice 8.
Si un FAQ tiene 6 ítems, el blueprint dice 6.
Si otro FAQ tiene 12 ítems, el blueprint dice 12.

Ese blueprint es el contrato contra el cual se genera el código.

======================================================================
5. SEGUNDO PASO: REGISTRO DE COPY
======================================================================

Extraé el copy sección por sección ANTES de redactar el HTML final.

Primero construí una versión traducida fiel del copy.

Pipeline:

ORIGINAL
→ traducción fiel al español
→ sustitución de marca/producto
→ PASADA DE LOCALIZACIÓN AL PAÍS DESTINO
→ cambios de INDICACIONES EXTRA.

No hagas una reescritura creativa.

Preservá:
- intención;
- sentido;
- cantidad de ideas;
- longitud aproximada;
- énfasis;
- orden;
- bullets;
- párrafos;
- preguntas;
- respuestas.

Una FAQ se transforma pregunta por pregunta y respuesta por respuesta.

Un testimonio se transforma como testimonio.

Una estadística conserva su función y estructura.

Una comparativa se transforma celda por celda.

Un bloque editorial se transforma párrafo por párrafo.

No reduzcas contenido para ahorrar código.

======================================================================
5.1 PASADA OBLIGATORIA DE LOCALIZACIÓN AL PAÍS DESTINO
======================================================================

La localización NO es solamente cambiar el idioma o usar voseo/tuteo.

Es una segunda revisión completa del REGISTRO DE COPY para detectar todo
elemento que pertenece al mercado original y adaptarlo al PAÍS DESTINO.

Para esta metodología de réplica, salvo que INDICACIONES EXTRA diga
expresamente que algo debe conservarse, tratá como LOCALIZABLE todo dato
visible relacionado con:

- países;
- provincias/estados/departamentos;
- ciudades;
- regiones;
- centros logísticos;
- origen de despacho;
- referencias de envío;
- direcciones;
- nombres de personas;
- monedas;
- formato de precios;
- medios de pago;
- plataformas comerciales;
- marketplaces;
- referencias culturales;
- unidades o convenciones propias del mercado cuando corresponda;
- referencias como "USA-based", "US shipping", "en Estados Unidos",
  "desde China", etc.

REGLA DE MERCADO:

La landing final debe sentirse construida para PAÍS DESTINO, no como una
traducción de una tienda extranjera.

Si PAÍS DESTINO es Argentina, por ejemplo, no debe quedar visible una frase de
logística como:

"Todos los pedidos se envían desde nuestro centro de despacho en Estados Unidos"

La función de esa frase debe conservarse, pero localizada, por ejemplo:

"Todos los pedidos se envían desde nuestro centro de despacho en Argentina"

o una formulación argentina equivalente que cumpla el mismo rol.

Lo mismo aplica a FAQ, footer, hero, barras de envío, ofertas, testimonios,
microcopy y secciones editoriales.

GEOGRAFÍA DEL PRODUCTO / PROCEDENCIA:

En este flujo de trabajo, la procedencia geográfica que aparece en la
referencia también se considera contenido localizable por defecto, porque el
producto final será revisado posteriormente por el dueño de la tienda.

Si la referencia menciona una procedencia extranjera y INDICACIONES EXTRA no
ordena conservarla:

1. no mantengas automáticamente el país/ciudad extranjera;
2. trasladá la función de esa frase al PAÍS DESTINO;
3. evitá inventar una precisión geográfica innecesaria si no hace falta.

Ejemplo de criterio:

Original:
"cultivado en Pu'er, Yunnan, China"

Si el destino es Argentina y no existe una ubicación específica suministrada,
preferí una adaptación como:

"cultivado y seleccionado en Argentina"

o:

"proveniente de una región productora de Argentina"

antes que conservar China o inventar una ciudad argentina muy específica.

El dueño podrá ajustar el dato posteriormente.

NOMBRES Y TESTIMONIOS:

Si aparecen nombres de clientes/personas propios del mercado original,
adaptalos a nombres naturales del PAÍS DESTINO cuando corresponda.

MONEDA Y PRECIOS:

Si el precio se obtiene dinámicamente de Shopify, dejá que Shopify muestre la
moneda configurada en la tienda.

Si un precio es puramente visual/fallback de la referencia:
adaptá su formato al PAÍS DESTINO y dejalo fácil de editar.

MEDIOS DE PAGO:

No mantengas como opción principal un método exclusivo del país original si la
página se adapta a otro mercado.

Si el método equivalente no puede determinarse con seguridad:
conservá la geometría visual y dejá el recurso/label fácil de editar, usando
una opción general del PAÍS DESTINO cuando sea razonable.

======================================================================
5.2 REGISTRO DE LOCALIZACIÓN
======================================================================

Antes de programar, construí internamente un REGISTRO DE LOCALIZACIÓN.

Para cada referencia de mercado encontrada anotá:

ORIGINAL:
qué decía la referencia.

TIPO:
país / ciudad / envío / moneda / nombre / medio de pago / cultura / otro.

DESTINO:
cómo debe aparecer para PAÍS DESTINO.

SECCIONES:
en qué partes de la página aparece.

Después aplicá el mismo reemplazo de forma coherente en TODAS las apariciones.

No adaptes una FAQ a Argentina y dejes otra FAQ hablando de Estados Unidos.

No adaptes el hero y dejes el footer con el mercado original.

======================================================================
5.3 CONTROL DE LOCALIZACIÓN ANTES DE PROGRAMAR
======================================================================

Cuando termines el REGISTRO DE LOCALIZACIÓN, revisá todo el REGISTRO DE COPY y
preguntate:

"¿Este texto todavía contiene una referencia al mercado original?"

Si la respuesta es sí y no existe una instrucción expresa para conservarla,
localizala antes de escribir el HTML.

La fidelidad que debe preservarse es:
- la función del texto;
- su jerarquía;
- su extensión aproximada;
- su lugar en la página.

No necesariamente el país, ciudad o sistema comercial de la tienda original.

======================================================================
6. TERCER PASO: REGISTRO DE ASSETS Y MEDIOS
======================================================================

Construí internamente un ASSET REGISTRY.

Buscá en capturas y código:

- `<img>`;
- `<picture>`;
- `<source>`;
- `background-image`;
- SVG;
- logos;
- iconos;
- posters;
- `<video>`;
- `.mp4`;
- `.webm`;
- URLs CDN;
- imágenes mobile y desktop distintas.

Cada elemento visual del blueprint debe apuntar a un asset concreto.

PRIORIDAD DE ASSET:

1. recurso nuevo adjuntado por el usuario;
2. recurso equivalente de la referencia como TEMPORAL;
3. placeholder dimensional únicamente si el recurso realmente no puede
   recuperarse.

No reemplaces un tipo de asset por otro que cumple una función diferente.

Ejemplos:
- una foto de producto no reemplaza una foto lifestyle;
- una foto de producto no reemplaza un video;
- una foto no reemplaza un icono;
- una foto de cliente no reemplaza una imagen comparativa.

======================================================================
6.1 CONTRATO DE EDITABILIDAD DE RECURSOS
======================================================================

El código será modificado por una persona SIN conocimientos de programación.

Por eso, "la URL es editable" NO alcanza.

La persona debe poder abrir cada TXT y entender inmediatamente:

- qué imágenes usa ese archivo;
- qué video usa;
- dónde aparece;
- qué debe reemplazar;
- exactamente qué parte de la línea debe cambiar.

Cada Custom Liquid debe comenzar, ANTES DEL CSS, HTML Y JAVASCRIPT, con una
zona claramente delimitada:

================================================================
ZONA EDITABLE — IMÁGENES, VIDEOS Y RECURSOS
CAMBIÁ ÚNICAMENTE LAS URL ENTRE COMILLAS
================================================================

Dentro de esa zona, declará TODOS los recursos de usuario utilizados por ese
archivo.

Ejemplo de formato esperado:

{% comment %}
IMAGEN 01 — LOGO DEL HEADER
Aparece: encabezado desktop y mobile.
Para cambiarla: reemplazá únicamente la URL entre comillas.
{% endcomment %}
{% assign URL_IMAGEN_01_LOGO = 'https://...' %}

{% comment %}
IMAGEN 02 — FOTO PRINCIPAL DEL HERO
Aparece: primera sección, imagen grande del producto.
{% endcomment %}
{% assign URL_IMAGEN_02_HERO = 'https://...' %}

{% comment %}
VIDEO 01 — TESTIMONIO UGC
Aparece: sección "clientes".
{% endcomment %}
{% assign URL_VIDEO_01_UGC = 'https://...mp4' %}

Los nombres deben estar numerados y describir la función:

URL_IMAGEN_01_LOGO
URL_IMAGEN_02_HERO
URL_IMAGEN_03_LIFESTYLE
URL_ICONO_01_GARANTIA
URL_VIDEO_01_UGC
URL_POSTER_VIDEO_01_UGC

No uses nombres ambiguos como:
img1
media2
pic
assetA
final_img

======================================================================
6.2 UNA SOLA FUENTE DE VERDAD PARA CADA URL
======================================================================

Cada recurso editable debe tener UNA ÚNICA URL fuente dentro de la zona
editable.

Después de declararlo, el resto del archivo debe utilizar la variable:

{{ URL_IMAGEN_02_HERO }}

y NO volver a escribir la URL literal.

Esto aplica a URLs utilizadas en:

- `<img src>`;
- `<source srcset>`;
- `<video>`;
- `<source src>`;
- `poster`;
- `background-image`;
- CSS custom properties;
- SVG externo;
- iconos externos.

Si una imagen aparece cinco veces:
la URL se declara una sola vez y las cinco apariciones utilizan la variable.

Si desktop/mobile usan assets diferentes:
declará dos variables claramente diferentes.

======================================================================
6.3 RECURSOS TEMPORALES
======================================================================

Cuando no se adjunte una imagen nueva:

NO dejes la variable vacía si podés recuperar el recurso equivalente de la
referencia.

Prefillá la variable con la URL temporal de la referencia para que la página
se vea completa durante la réplica.

Ejemplo:

{% comment %}
IMAGEN 05 — FOTO LIFESTYLE
ESTADO: TEMPORAL DE LA REFERENCIA.
Reemplazar por la imagen definitiva antes de publicar.
{% endcomment %}
{% assign URL_IMAGEN_05_LIFESTYLE =
'https://assets-de-la-referencia...' %}

El hecho de que sea temporal se explica en el COMENTARIO, no dentro de la
landing visible.

======================================================================
6.4 NO ESCONDER RECURSOS EN EL CUERPO DEL CÓDIGO
======================================================================

Una vez cerrada la ZONA EDITABLE DE RECURSOS, no debe aparecer ninguna URL
literal de imagen/video/poster que el alumno necesite modificar.

El alumno NO debe tener que encontrar algo como:

<img src="https://assets.replocdn.com/...">

en la línea 600.

Debe encontrar arriba:

{% assign URL_IMAGEN_07_COMPARATIVA = 'https://assets.replocdn.com/...' %}

y el HTML de la línea 600 debe decir solamente:

<img src="{{ URL_IMAGEN_07_COMPARATIVA }}">

Lo mismo para un background:

NO:
background-image:url('https://...');

SÍ:
background-image:url('{{ URL_FONDO_01_SECCION }}');

Las URLs técnicas que no son recursos editables del alumno, por ejemplo rutas
internas de Shopify o una dependencia técnica indispensable, pueden quedar
fuera de esta zona.

======================================================================
6.5 LINKS EDITABLES
======================================================================

Aplicá el mismo criterio a links que probablemente cambien:

- WhatsApp;
- Instagram;
- contacto;
- políticas;
- CTA externos.

Agrupalos en:

ZONA EDITABLE — LINKS

con comentarios claros.

No obligues al alumno a buscar `href` dispersos por el archivo.

======================================================================
7. VIDEOS: RECONSTRUIR EL MEDIO REAL, NO UNA MINIATURA FALSA
======================================================================

Si el código fuente contiene un `<video>` o una URL `.mp4/.webm`, registralo
como VIDEO, no como imagen.

Extraé:
- URL del video;
- poster si existe;
- icono de play;
- tamaño del icono;
- border-radius;
- comportamiento al click;
- cantidad de videos;
- configuración de slider/carrusel.

Si no se adjuntaron videos nuevos, utilizá las URLs de video de la referencia
como TEMPORALES para que la réplica funcione durante la construcción.

Las URLs deberán quedar fáciles de reemplazar.

Si el original tiene play/pause:
implementá play/pause.

Si el original oculta el icono al reproducir:
replicalo.

Si el código original declara un play de 54px:
no decidas arbitrariamente que debe cubrir media tarjeta.

Si el original usa una librería para layout, podés reconstruir el mismo
comportamiento con JavaScript nativo, pero conservando los parámetros
observables:
- slides visibles;
- gaps;
- breakpoints;
- flechas;
- swipe.

======================================================================
8. CUARTO PASO: EXTRAER LA LÓGICA DE COMPONENTES DINÁMICOS
======================================================================

No deduzcas la lógica comercial únicamente mirando el screenshot.

Buscá primero en el código:

- JSON de bundle apps;
- variantes;
- IDs;
- quantity;
- buyQuantity;
- getQuantity;
- discounts;
- preselectedDealBarId;
- sticky enabled/disabled;
- precios;
- compare-at;
- selling plans.

Convertí esa información en un MODELO DE DATOS antes de programar la UI.

Ejemplo conceptual:

OPCIÓN A
tipo: quantity
cantidad: 1

OPCIÓN B
tipo: buy-x-get-y
paga: 2
recibe: 3
badge: ...
preseleccionada: sí

OPCIÓN C
tipo: buy-x-get-y
paga: 3
recibe: 5

La UI y el JavaScript deben leer esa lógica.

No mezcles:
- cantidad recibida;
- cantidad pagada;
- precio visual;
- ahorro;
- compare-at.

======================================================================
9. RECONSTRUCCIÓN VISUAL POR SECCIÓN
======================================================================

Una vez completados blueprint, copy registry y asset registry, construí cada
sección individualmente.

No diseñes primero un sistema genérico para luego "meter" la página adentro.

Cada sección puede tener:
- wrapper diferente;
- ancho diferente;
- grid diferente;
- padding diferente;
- background diferente.

La repetición de clases está permitida cuando corresponda, pero la geometría
de la captura tiene prioridad sobre la abstracción.

Si S04 tiene imagen izquierda y texto derecha:
construí eso.

Si S05 tiene texto arriba e imagen debajo:
construí eso.

Si una sección atraviesa todo el viewport:
no la fuerces dentro de un contenedor estrecho.

======================================================================
10. FORMAS, DEGRADADOS Y DECORACIÓN
======================================================================

Tratálos como componentes reales del diseño.

Buscá primero en el CSS original:
- linear-gradient;
- radial-gradient;
- pseudo-elementos;
- border-radius;
- clip-path;
- SVG;
- transform;
- background;
- overlays.

Cuando el código permita conocer la implementación, usá esa evidencia.

Cuando no, aproximá la captura.

No reduzcas una sección visualmente compleja a `background:#...`.

======================================================================
11. TIPOGRAFÍA
======================================================================

Determiná la fuente a partir del código y la captura.

Buscá:
- `@font-face`;
- Google Fonts;
- Shopify Fonts;
- `font-family`;
- pesos importados.

No declares una fuente como "confirmada" si no encontraste evidencia.

La implementación debe reproducir:
- familia;
- peso;
- tamaño;
- line-height;
- letter-spacing;
- alineación.

======================================================================
12. HEADER Y ELEMENTOS DE NAVEGACIÓN
======================================================================

El blueprint debe decidir si el header/announcement pertenece a la apariencia
que se está replicando.

Si aparece en las capturas de la referencia:
forma parte de la réplica.

Reconstruí:
- announcement;
- logo;
- menú desktop;
- hamburger mobile;
- carrito/iconos;
- alturas;
- colores;
- alineación.

No asumas que el theme del alumno tendrá un header visualmente equivalente.

======================================================================
13. SHOPIFY CUSTOM LIQUID
======================================================================

Cada TXT debe poder pegarse directamente en un bloque de Liquid personalizado.

Podés utilizar:
- Liquid;
- HTML;
- `<style>`;
- `<script>`;
- SVG inline;
- JavaScript nativo.

Evitá depender de:
- `{% schema %}`;
- settings de schema;
- edición obligatoria de `theme.liquid`;
- snippets externos;
- archivos de section obligatorios.

Encapsulá CSS y JS con un prefijo único relacionado con la marca/proyecto.

Ejemplo:
`trp-`

No contamines estilos globales.

======================================================================
14. CONTEXTO INDEPENDIENTE ENTRE CUSTOM LIQUIDS
======================================================================

No asumas que un `{% assign %}` definido en Liquid 01 existe en Liquid 02.

Cada archivo que necesite datos Shopify debe obtenerlos por sí mismo.

Las dependencias JS entre archivos deben ser explícitas y seguras.

======================================================================
15. HANDLE Y PRODUCTO
======================================================================

Generá automáticamente un HANDLE SUGERIDO a partir de marca + producto.

Formato:
- minúsculas;
- sin tildes;
- sin ñ;
- guiones.

Centralizalo en una única variable por archivo que lo necesite:

{% assign trp_product_handle = 'handle-sugerido' %}
{% assign trp_product = all_products[trp_product_handle] %}

El alumno debe poder cambiar el handle en una sola línea.

Usá datos reales del producto cuando estén disponibles:
- variant ID;
- price;
- compare_at_price;
- availability;
- images.

No inventes IDs.

======================================================================
16. FALLBACK VISUAL DEL PRODUCTO
======================================================================

El código debe seguir siendo visualmente inspeccionable aunque el producto
Shopify todavía no esté correctamente configurado.

Separá:

A. DATOS DE COMPRA REALES
Provienen de Shopify y son necesarios para agregar al carrito.

B. DATOS DE PRESENTACIÓN TEMPORALES
Pueden provenir de la referencia para evitar que la vista previa muestre:
- $0;
- campos vacíos;
- cards rotas.

Si no existe un variant ID real:
la compra queda deshabilitada.

Pero el diseño no debe colapsar.

Cuando Shopify devuelve un producto real correctamente configurado:
los datos reales reemplazan los fallbacks correspondientes.

======================================================================
17. BUY BOX: CONSTRUIR CON TAMAÑO INTRÍNSECO
======================================================================

La buy box debe soportar traducciones y valores dinámicos sin romperse.

Construí las opciones para que crezcan según su contenido.

Reglas de construcción:

- `width:100%` dentro de la columna de compra;
- sin alturas fijas para las opciones;
- hijos flex/grid con `min-width:0`;
- columna de texto flexible;
- columna de precio reservada;
- badges con espacio real dentro del layout o con overflow visible;
- textos capaces de hacer wrap;
- precios legibles;
- bordes completos;
- padding suficiente para badge/label.

No dependas de que una frase traducida tenga exactamente la misma longitud que
el inglés.

El ancho final de la buy box lo determina el blueprint de desktop/mobile, no
un `max-width` inventado.

======================================================================
18. PACKS Y BUNDLES
======================================================================

Si la referencia usa bundle app, usá la configuración extraída como fuente de
verdad para la lógica visual.

Para `buy x get y`:

cantidad_recibida = buyQuantity + getQuantity

El precio mostrado debe representar la lógica de la oferta observada, no
`precio_unitario × cantidad_recibida` por defecto.

Si el descuento real depende de una app/configuración Shopify que no puede
reproducirse solamente con Custom Liquid:
- conservá la UI correcta;
- conservá quantity correcta;
- conectá la variante;
- explicá brevemente la dependencia al final.

No falsifiques un descuento real que Shopify no aplicará.

======================================================================
19. GALERÍAS
======================================================================

La cantidad de slots debe venir del blueprint.

No uses límites arbitrarios.

Reproducí:
- orden;
- main media;
- thumbnails;
- activo;
- flechas;
- video;
- swipe si existe.

Si el nuevo producto no tiene aún suficientes assets, usá las URLs temporales
del asset registry.

======================================================================
20. FAQ Y ACORDEONES
======================================================================

Construí desde el REGISTRO DE COPY.

Cantidad = cantidad registrada en blueprint.

Pregunta = traducción de la pregunta fuente.

Respuesta = traducción de la respuesta fuente.

No generes respuestas desde cero.

Replicá:
- estado abierto/cerrado;
- icono;
- borde;
- espaciado;
- animación;
- comportamiento de apertura.

======================================================================
21. COMPARATIVAS, TIMELINES, ICONOS Y BLOQUES ESPECIALES
======================================================================

No los reduzcas a componentes genéricos.

Para cada uno seguí el blueprint:

COMPARATIVA
- filas;
- columnas;
- imágenes;
- checks/cruces;
- color destacado.

TIMELINE
- etapas;
- lados;
- línea;
- dots;
- cards;
- fechas.

ICONOS
- buscá el asset/SVG real;
- mantené proporción y tamaño.

Si el original tiene un icono dibujado, no lo reemplaces por letras.

======================================================================
22. RESPONSIVE
======================================================================

No derives mobile solamente apilando desktop.

Usá la captura mobile como especificación independiente.

Verificá especialmente:
- 320;
- 360;
- 375;
- 390;
- 414 px.

La construcción debe ser content-driven:
- sin alturas rígidas innecesarias;
- sin clipping de texto;
- sin overflow horizontal accidental;
- sin badges cortados;
- sin precios fuera de la card.

En tablet/desktop revisá:
- 768;
- 1024;
- 1366;
- 1440 px.

======================================================================
23. BREAKOUT DEL CONTENEDOR DEL THEME
======================================================================

Recordá que un Custom Liquid puede quedar envuelto por contenedores del theme.

Compará el ancho renderizado que necesita cada sección con la referencia.

Si una sección debe ser full-width y el contenedor del theme la restringe,
implementá un breakout local y seguro en el wrapper de ESA sección.

No apliques hacks globales al body/theme.

======================================================================
24. INTERACCIONES
======================================================================

Cada interacción del código final debe existir en el blueprint.

Cada interacción del blueprint debe existir en el código final.

No agregues interacciones por costumbre.

Implementá funcionalmente:
- carrusel;
- swipe;
- accordion;
- play/pause;
- tabs;
- modal;
- sticky;
- selector;
- ATC;

solamente cuando corresponda.

======================================================================
25. JAVASCRIPT
======================================================================

Preferí JavaScript nativo.

El JS debe:
- estar encapsulado;
- inicializarse una sola vez;
- soportar recarga del editor Shopify;
- usar IDs/classes únicos;
- no dejar errores de consola.

Para eventos repetidos, programá por colección/loop en vez de escribir
manualmente un handler diferente para cada índice cuando sea posible.

======================================================================
26. DIVISIÓN EN TXT
======================================================================

Cada archivo debe tener menos de 45.000 caracteres.

Usá la menor cantidad razonable SIN reducir la réplica.

Dividí por bloques completos.

Nunca cortes:
- HTML abierto;
- style;
- script;
- función;
- loop;
- condición Liquid.

Nombres:

MARCA_Liquid_01.txt
MARCA_Liquid_02.txt
MARCA_Liquid_03.txt
...

======================================================================
27. EXPERIENCIA DE EDICIÓN PARA PRINCIPIANTES
======================================================================

Diseñá cada TXT pensando en esta situación:

La persona que lo abre sabe usar Shopify y copiar/pegar, pero NO sabe HTML,
CSS, Liquid ni JavaScript.

Su flujo ideal debe ser:

1. abrir el TXT;
2. mirar las primeras líneas;
3. encontrar "ZONA EDITABLE";
4. reemplazar URLs/datos entre comillas;
5. no tocar el resto del archivo.

Las zonas editables deben aparecer ANTES del código técnico.

Orden recomendado al inicio de cada archivo:

1. ZONA EDITABLE — PRODUCTO / HANDLE, si aplica.
2. ZONA EDITABLE — IMÁGENES, VIDEOS Y RECURSOS.
3. ZONA EDITABLE — LINKS, si aplica.
4. ZONA EDITABLE — IDS MANUALES, solamente si fueron inevitables.
5. FIN DE ZONAS EDITABLES.
6. Desde ahí comienza el código técnico.

Los comentarios deben estar escritos para una persona común.

Ejemplo:

{% comment %}
IMAGEN 04 — PERSONA PREPARANDO EL PRODUCTO
Aparece en la sección "Cómo se prepara".
CAMBIÁ SOLO LA URL ENTRE COMILLAS DE LA LÍNEA SIGUIENTE.
{% endcomment %}
{% assign URL_IMAGEN_04_PREPARACION = '...' %}

Evitá comentarios como:
"bind media source"
"asset ref"
"DOM poster"
porque no ayudan a un principiante.

No conviertas todo el copy en variables innecesarias.

La prioridad de esta zona es facilitar los cambios habituales:
- imágenes;
- videos;
- logo;
- links;
- handle;
- IDs cuando sean necesarios.

======================================================================
27.1 AUDITORÍA DE EDITABILIDAD
======================================================================

Antes de entregar cada TXT, hacé mentalmente esta prueba:

"Si una persona que nunca vio código quiere cambiar TODAS las imágenes de este
archivo, ¿puede hacerlo sin usar Ctrl+F y sin entrar al HTML/CSS/JS?"

La respuesta debe ser SÍ.

Revisá además:

- todas las imágenes están listadas al comienzo;
- todos los videos están listados al comienzo;
- todos los posters están listados al comienzo;
- cada variable dice qué recurso representa;
- no hay URLs de medios repetidas;
- no hay recursos importantes sin nombre humano;
- no hay una URL de imagen escondida dentro del HTML;
- no hay una URL de video escondida dentro del JavaScript;
- no hay una URL de background escondida dentro del CSS.

Si encontrás una:
movela a la zona editable y reemplazala en el código por su variable.

======================================================================
28. VALIDACIÓN POR INVARIANTES
======================================================================

Antes de entregar verificá estas cinco invariantes.

INVARIANTE 1 — COBERTURA

Para cada sección S01...Sn del blueprint debe existir una sección equivalente
en el código, en el mismo orden.

INVARIANTE 2 — COPY

Todo texto visible del código debe provenir del REGISTRO DE COPY o de
INDICACIONES EXTRA.

No puede aparecer prosa nueva escrita por vos para explicar la referencia.

INVARIANTE 3 — ASSETS

Cada slot visual del blueprint debe tener:
- recurso nuevo;
- recurso temporal equivalente;
- o placeholder dimensional cuando el asset sea irrecuperable.

Nunca un recurso de función distinta.

INVARIANTE 4 — INTERACCIONES

Cada interacción del blueprint debe funcionar.

Un card identificado como VIDEO debe reproducir video real.
Un acordeón debe abrir/cerrar.
Una galería debe cambiar media.
Un pack debe cambiar estado y datos.

INVARIANTE 5 — GEOMETRÍA

Compará screenshot por screenshot:

- orden;
- lados;
- anchos;
- fondos;
- formas;
- degradados;
- cantidad de elementos;
- proporciones;
- spacing.

INVARIANTE 6 — LOCALIZACIÓN

Todo el copy visible pasó por el REGISTRO DE LOCALIZACIÓN.

No quedan países, ciudades, centros de despacho, monedas, nombres ni
referencias comerciales del mercado original salvo que INDICACIONES EXTRA
ordene conservarlos.

INVARIANTE 7 — EDITABILIDAD

Todo recurso de usuario está centralizado al comienzo del TXT.

El HTML/CSS/JS utiliza variables y no obliga a buscar URLs de imágenes/videos
dentro del código técnico.

Corregí cualquier incumplimiento antes de entregar.

======================================================================
29. CONTROL AUTOMÁTICO DEL COPY ANTES DE ENTREGAR
======================================================================

Hacé una última revisión del HTML que se renderiza.

Elegí al azar textos visibles de:
- hero;
- FAQ superior;
- bloque editorial;
- comparativa;
- FAQ inferior;
- footer.

Para cada uno respondé internamente:

"¿De qué frase exacta de la referencia proviene?"

Si no podés responder:
ese texto no debería estar visible.

Ésta es la prueba que evita que aparezcan explicaciones tuyas dentro de la
landing.

======================================================================
30. CONTROL DE MEDIOS ANTES DE ENTREGAR
======================================================================

Para cada card visual preguntate:

TIPO:
imagen / video / icono / SVG / background

ORIGEN:
usuario / referencia temporal / generado por CSS

COMPORTAMIENTO:
estático / play-pause / slider / link

Si la fuente dice VIDEO y tu implementación solamente tiene `<img>`:
la sección todavía no está terminada.

======================================================================
31. CONTROL DEL BUY BOX ANTES DE ENTREGAR
======================================================================

Probá conceptualmente el componente con:
- título corto;
- título largo;
- precio corto;
- precio largo;
- badge;
- compare-at;
- 320 px.

El layout debe crecer sin recortar contenido.

Revisá además:
- opción preseleccionada;
- badge correcto;
- precio correcto;
- quantity;
- pay/get;
- estado activo.

======================================================================
32. FORMATO DE ENTREGA
======================================================================

Entregá:

A. RESUMEN BREVE
- cantidad de secciones;
- cantidad de archivos;
- handle sugerido;
- dependencias externas reales, si existen.

B. TXT COMPLETOS
- archivos completos;
- orden de pegado;
- caracteres por archivo.

C. MAPA DE RECURSOS
- variable;
- tipo: imagen/video/icono;
- sección;
- temporal o nuevo.

D. CONFIGURACIÓN SHOPIFY
- handle;
- variantes;
- quantity;
- lógica de bundle;
- IDs manuales únicamente si fueron inevitables.

E. LIMITACIONES TÉCNICAS REALES
Únicamente aquello que no puede resolverse dentro de Custom Liquid.

No hagas una auditoría editorial de claims.
No reescribas la landing por motivos de revisión comercial.
La revisión comercial pertenece a una etapa posterior del dueño de la tienda.

======================================================================
33. ORDEN DE EJECUCIÓN
======================================================================

Seguí este orden:

1. leer todos los materiales;
2. blueprint;
3. registro de copy;
4. registro de localización;
5. asset registry;
6. registro de interacciones;
7. modelo de bundles/variantes;
8. arquitectura de archivos;
9. crear zonas editables;
10. implementación usando variables de recursos;
11. conexión Shopify;
12. validación de cobertura;
13. validación de copy;
14. validación de localización;
15. validación de assets;
16. auditoría de editabilidad;
17. validación de interacciones;
18. comparación desktop;
19. comparación mobile;
20. correcciones;
21. entrega.

No saltees los registros para empezar a codear más rápido.

======================================================================
RESULTADO ESPERADO
======================================================================

Quiero recibir la misma landing como sistema visual y funcional, adaptada a:

MARCA NUEVA + NOMBRE DEL PRODUCTO + PAÍS DESTINO.

La IA no debe explicar la referencia dentro de la página.

Debe traducirla y reconstruirla.

La IA no debe sustituir medios reales por representaciones falsas.

Debe identificar qué tipo de medio existe y reconstruirlo.

La IA no debe inventar una geometría estándar.

Debe construir desde el blueprint obtenido de las capturas y el código.

La exactitud nace de:
EVIDENCIA → BLUEPRINT → COPY → LOCALIZACIÓN → ASSETS EDITABLES → LÓGICA → CÓDIGO → VALIDACIÓN.
```
