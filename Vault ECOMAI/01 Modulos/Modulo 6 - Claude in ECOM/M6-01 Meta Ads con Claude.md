---
modulo: 6
leccion: 1
titulo: "Meta Ads con Claude"
duracion: "04:28"
conceptos: ["[[Conector MCP]]", "[[Métricas publicitarias]]", "[[CPA]]", "[[ROAS]]"]
herramientas: ["[[Claude]]", "[[Meta Ads]]"]
tags: [ecomai, modulo-6, leccion]
---
# Meta Ads con Claude

> [!info] [[Modulo 6 - Claude in ECOM]] · Lección 1 de 3 · ⏱ 04:28 · [▶ Abrir video](file:///C:/Users/WIN-10/Desktop/Ecommerce%20Curso/Modulo%206%20-%20Claude%20in%20ECOM/Video%201.mp4)

[[Modulo 6 - Claude in ECOM|↑ Módulo 6]] · [[M6-02 Analizar pedidos de Shopify con Claude]] →

## Resumen

Explica cómo conectar Claude a Meta Ads mediante un conector MCP personalizado, ya que no existe una conexión directa oficial. Con el conector armado, Claude puede leer cuentas publicitarias individuales (no portafolios completos) y responder preguntas sobre el mejor anuncio, el CPA y la frecuencia de una cuenta puntual. También muestra cómo darle contexto de negocio (CPA y ROAS de equilibrio) para que identifique qué campañas están en pérdida.

## Puntos clave

- No hay conexión directa de Claude con Meta Ads, pero sí indirecta y válida vía un conector MCP personalizado [00:00].
- Para armarlo: Configuración → Conectores → Agregar conector personalizado, poniendo un nombre (ej. Meta Ads) y la URL mcp.facebook.com/ads [00:29]-[01:26].
- El conector lee cuentas publicitarias puntuales, no portafolios completos [00:00], [03:04].
- Al autorizar el acceso a Facebook conviene tildar permitir siempre en los distintos permisos, para no tener que aprobar cada acción [01:26]-[01:59].
- Ejemplo de prompt: pedirle a Claude que se conecte vía MCP, busque una cuenta publicitaria por nombre y diga el mejor anuncio con sus métricas de CPA y frecuencia [02:30]-[03:04].
- Dándole el CPA y el ROAS de equilibrio propios (ej. CPA breakeven 38.000 pesos, ROAS break 2.4), Claude puede señalar qué campañas están en pérdida [03:31]-[04:02].
- Este análisis depende de tener antes calculados los costos y el punto de equilibrio del producto [04:02].
- A futuro se van a sumar skills específicas de métricas para leer directamente por MCP [04:16].

## Conceptos y herramientas

**Conceptos:** [[Conector MCP]] · [[Métricas publicitarias]] · [[CPA]] · [[ROAS]]
**Herramientas:** [[Claude]] · [[Meta Ads]]

## Recursos de esta lección

- [Doc Meta Ads](https://docs.google.com/document/d/1fjHh_O4Vd5Zei5vAT94tpxXbAZeXBcMkS_V34oHciH8/edit?usp=sharing)

## Transcripción

*Transcripción automática con Whisper large-v3. Puede tener errores en nombres propios o términos técnicos.*

**[00:00]** Bien, vamos a aplicar lo que es la conexión biorápido de Claude vía MACP, que es algo... no tiene directamente conexión directa, pero sí indirecta y totalmente válido para que puedan ver cuentas publicitarias. Portafolios no lo detecta tanto, pero sí cuentas publicitarias. Acá igualmente les voy a dejar después el paso a paso, pero bueno, lo que tienen que hacer es ir a la parte de Claude.

**[00:29]** Vamos a mover esto, van acá a personalizar, se van a conectores, y como ven yo ya lo tenía acá, pero voy a apretar acá, y es esto el MSP, lo que tienen que copiar. Copiado, msp.facebook.com barra ads. Pero bueno, vamos, como si ustedes no lo tenían, vamos acá, vamos a agregar, vamos a agregar conector personalizado, acá le ponen.

**[00:59]** Meta Ads o algo que lo relacione. Y acá va justamente el link. Esto lo dejan así como está. No hace falta. Bueno, acá mi marca que ya existe. Vamos a ver si lo puedo eliminar. Vamos a lo nuevo. Agregar. Conector. Nombre. Meta Ads. Y URL. Ahora sí. Agregar.

**[01:26]** Verificar la conexión. Bueno, aún no está conectado. Esto lo que va a hacer es abrir un link en nuestro navegador preterminado. Así que eso, fíjense que ya están logueados en su navegador preterminado. Continuar ahí. Básicamente es acceso a Facebook. Esto también, permitir. Y bueno, ahí ya tienen, digamos, todo. Acá esto es justamente las cosas que requiere aprobación. Yo la verdad siempre lo que hago es que

**[01:59]** Lo pongo en permitir siempre, permitir siempre. Pero bueno, esto es más que nada a gusto para que no me vayan preguntando cosas. Entonces, yo cuando, por ejemplo, vamos a una campaña, voy a entrar a mi Facebook. Voy a pausar un segundo en esta parte. Ahí ya entré a lo que sería el portafolio. Recuerden que lee cuentas publicitarias, no portafolios. Entonces, no sé, yo voy a alguna de estas tiendas.

**[02:30]** Y voy a esta que se llama cuenta publicitaria Tienda Casanova creo que se sigue llamando. Bueno, entonces lo que le digo, vamos a Claude, vamos a un nuevo chat, conectate vía MSP a Meta Ads y búscame la cuenta publicitaria Tienda Casanova y por las dudas...

**[03:04]** del portafolio jesús hogar pero tengo entendido que no lee los portafolios decirme el mejor anuncio y qué métricas tiene de CPA y frecuencia para decir algo digamos entonces bueno ahí justamente está el nombre cuenta publicitaria de tienda casa nueva y creo que no sé si la clave del día pero vamos a

**[03:31]** Lo que nosotros podemos hacer es que va a leer métricas y bueno, algunas cosas más que ahora vamos a ver. Vamos a esperar que cargue. Bueno, y esto es justamente lo que ustedes pueden lograr en métricas. Y acá es cuestión de que puedan hablarle. Por ejemplo, mi CPA breakeven es 38.000 pesos. ¿Cuáles son los que están en pérdida? Y mi ROAS break es 2.4.

**[04:02]** Todo esto obviamente desde la clase de costos para que puedan analizar y para que puedan ayudar a analizar mucho más. Después lo que vamos a agregar es como muchas más cosas digamos, cosas puntuales como por ejemplo la skill de métrica ya que sea directamente por MSP y demás pero bueno de momento ya tienen conectado esta parte que ya se pueden hacer muchas más cosas.
