# Relevamiento — Laboratorios a façon y Disp. ANMAT 7939/2025

| | |
|---|---|
| **Fecha** | 2026-10-31 |
| **Quién** | Claude (sesión en la nube) |
| **Para qué** | Destrabar el pendiente #2 de `GAPS.md`: cotización de laboratorios cosméticos a façon en AMBA |
| **Afecta a** | `jabon-caqui-nonenal` (90/100, operativa 15/20) y `locion-magnesio-topico` (89/100, operativa 16/20) |
| **Herramienta usada** | WebSearch únicamente. **Ad Library, Mercado Libre y GetHookd están bloqueados en esta sesión** (ver §4) |

---

## 1. Lo que importa en una línea

El supuesto regulatorio del Ecosistema 2 **se confirma**, y el cuello de botella que
más miedo daba — el MOQ — **es mucho menor de lo que parecía**: hay laboratorios
argentinos que fabrican **desde 100 unidades**, no desde 2.000.

Eso hace viable un **lote piloto real** del jabón de caqui sin inmovilizar millones.

---

## 2. Disp. ANMAT 7939/2025 — confirmada, con un matiz

🟩 **Confirmado en fuente primaria** (Boletín Oficial, 27/10/2025):

- Reemplaza la habilitación previa por una **declaración jurada digital**, que se
  presenta en la plataforma de ANMAT con CUIT y clave de pago electrónico.
- Presentada la DJ, **la empresa queda habilitada para operar**. ANMAT se reserva
  verificar la exactitud y veracidad **con posterioridad**.
- Aplica a establecimientos nuevos, cambios de Dirección Técnica, cambios de razón
  social y transferencias de titularidad.
- Las empresas ya habilitadas deben empadronarse en **180 días hábiles**, sin arancel.

⚠️ **Dos matices que el vault no tiene:**

1. **No pude confirmar la categoría "Grado 1"** que menciona el vault. Los resultados
   hablan de la DJ y de excluir los domisanitarios **grado 2b** (más tóxicos), pero no
   detallan el grado 1 para cosméticos. Hay que leer el texto completo de la
   disposición. No cambia la conclusión, pero la etiqueta puede estar mal usada.
2. **La DJ no exime de las Buenas Prácticas de Fabricación**, ni de requisitos
   municipales, ambientales, de higiene y seguridad, ni provinciales. Es decir: la
   habilitación se agilizó, **la obligación de fabricar bien no**. Para un façon esto
   lo cubre el laboratorio, que ya las tiene.

### El upside estratégico que aparece

La disposición vuelve mucho más barato **habilitarse uno mismo** como titular, no solo
tercerizar bajo el legajo del laboratorio. No es el camino para el lote piloto —para
eso el façon sigue siendo más rápido— pero sí abre la puerta a tener legajo propio
cuando la marca escale, lo que saca al laboratorio de la posición de cuello de botella.

---

## 3. Laboratorios a façon — short list con el MOQ como filtro

El MOQ es el dato que decide, porque define cuánta plata se inmoviliza en el piloto.

### 🟢 MOQ chico (sirven para el lote piloto)

| Laboratorio | MOQ declarado | Dónde | Nota |
|---|---|---|---|
| **Eneve Cosmética** | **desde 100 unidades** o lotes de 25 kg | AR | Declara que sus controles cumplen requisitos de ANMAT |
| **Carmenta / Biosinergia** | **desde 100 hasta 5.000** unidades por producto | AR | Trabaja con un laboratorio habilitado por ANMAT |
| **Senda Aromática** | "lotes incluso desde pocas unidades" | AR | Sin cifra precisa |
| **Pasmanter** | lotes piloto + escalado industrial | AR | Ofrece certificaciones y documentación para ANMAT: útil si se quiere legajo propio después |
| **Oxapharma** | no publica | AR | **Ya estaba en el plan del vault.** Servicios a terceros |

### 🟡 MOQ grande (recién cuando haya validación)

| Laboratorio | MOQ | Confianza |
|---|---|---|
| **Laboratorio Basel** (CABA) | 2.000-5.000 según complejidad de la fórmula | 🟥 dato de un blog de 466 días. Confirmar |
| **LACA** (CABA) | 3.000-7.000 unidades | 🟥 mismo blog. Confirmar |
| **Laboratorio Reig** (Villa Maipú, BA) | no publica. +40 años, producción y envasado bajo BPM | 🟨 sitio propio |
| **Livepharma** | no publica. Ofrece desarrollo de marca propia **y registro ante ANMAT** | 🟨 sitio propio |

### ❌ Descartados por ubicación

Laboratorios Vesna (España, MOQ 25 u. para fórmulas ya registradas), Natural Cosmetic
Lab (Alicante, 1.000 u.), GoDreams (México y Colombia, 500 u./SKU), Carmado (300 u.,
ubicación sin confirmar). **Fabricar un cosmético afuera reintroduce el problema que el
façon local venía a resolver:** vuelve a ser cosmético importado.

---

## 4. Lo que NO pude hacer, y por qué

Las tres herramientas centrales del curso están **bloqueadas por la política de red de
este entorno**:

| Herramienta | Estado | Qué se pierde |
|---|---|---|
| **Meta Ad Library** (`www.facebook.com`) | 🔴 Bloqueada: el gateway responde 403 a la conexión | **El Radar AR entero.** Sin esto no puedo medir quién pauta, días al aire, foco vs dispersión ni ángulos tomados |
| **Mercado Libre AR** (`listado.mercadolibre.com.ar`) | 🔴 El host no resuelve | Demanda real: publicaciones, vendidos, ancla de precio |
| **Google Trends AR** (`trends.google.com`) | 🔴 El host no resuelve | Tendencia 5a/12m y estacionalidad |
| **GetHookd** | 🔴 Requiere login pago + extensión en el Chrome de Emanuel | La búsqueda de tiendas ganadoras afuera |
| **WebSearch** | 🟢 Funciona | Lo único que usé acá |

Probé además levantar la Ad Library con el Chromium y Playwright que vienen en el
contenedor: el proxy la rechaza igual (403 a CONNECT sobre `www.facebook.com:443`).

**Consecuencia honesta: desde esta sesión no puedo buscar candidatos nuevos con el
método del curso.** El método es "buscar por el dolor en Ad Library → cruzar con
demanda en MELI → medir el hueco en Meta AR", y los tres pasos necesitan hosts
bloqueados. Lo que sí puedo hacer con WebSearch es lo de este archivo: verificar
supuestos regulatorios y encontrar proveedores.

### Cómo se destraba

Para habilitar los hosts: en el menú del entorno en la barra de título de la sesión →
**Edit** → **Network access**. O se sube el nivel de acceso, o se agregan estos
dominios bajo **Allowed domains** dejando tildada la casilla de package managers:

```
www.facebook.com
listado.mercadolibre.com.ar
www.mercadolibre.com.ar
trends.google.com
```

Pasos: https://code.claude.com/docs/en/cloud-environments#network-access

Con eso puedo correr el Radar AR desde acá con Playwright, usando los mismos scripts de
extracción de la skill `radar-adlibrary-ar`. GetHookd no, porque necesita tu login.

---

## 5. Qué hacer con esto

### No cambié ningún score

El eje de operativa del jabón de caqui sigue en **15/20** y el de la loción en
**16/20**, a propósito: los MOQ de arriba son **declaraciones comerciales de los
propios laboratorios**, no datos confirmados. La regla 1 del Doc A manda — una fuente
con interés comercial no decide.

**Si al llamar se confirma un MOQ de 100-500 unidades con BPM y legajo vigente, la
operativa de los dos candidatos sube**, y con ella el score total. Eso puede mover el
jabón de caqui (90) por encima del Ebook #3 (88) y acercarlo a la loción (89).

### Los 5 llamados, en orden

Priorizados por MOQ chico, que es lo que define el piloto:

1. **Eneve Cosmética** — desde 100 unidades. El mejor candidato para el piloto
2. **Carmenta / Biosinergia** — 100 a 5.000, con laboratorio habilitado ANMAT
3. **Pasmanter** — lotes piloto + documentación ANMAT para el día que haya legajo propio
4. **Oxapharma** — ya estaba en el plan, pedir MOQ
5. **Senda Aromática** — pedir cifra concreta

**Qué preguntar en los cinco** (sirve para los dos productos, se cotizan juntos):

- MOQ real por SKU y por lote, para: (a) barra o gel con extracto de caqui + té verde,
  (b) loción de cloruro de magnesio + lavanda
- Costo por unidad a ese MOQ, y a 500 / 1.000 / 5.000
- ¿Fabrican **bajo su legajo** o hay que tener legajo propio?
- ¿Están empadronados bajo la Disp. 7939/2025? (plazo de 180 días hábiles)
- Plazo de entrega desde la aprobación de la muestra
- ¿Hacen la muestra? ¿Cuánto cuesta y cuánto tarda?
- ¿Envasado y etiquetado incluidos, o aparte?

> Objetivo de costo del vault: **≤ $3.500-$4.000 por unidad** para salir con el pack x3
> a $34.900. Correr `02-costos/rentabilidad-ar.py --costo <el que coticen> --bundle 3:34900`
> con cada cotización que entre.

---

## Fuentes

**Disp. ANMAT 7939/2025**
- [Boletín Oficial — Disposición 7939/2025 (27/10/2025)](https://www.boletinoficial.gob.ar/detalleAviso/primera/333450/20251027) 🟩
- [Texto original de la disposición](https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-7939-2025-419276/texto) 🟩
- [Presentación de Declaración Jurada de habilitación de empresas](https://www.argentina.gob.ar/servicio/presentacion-de-declaracion-jurada-de-habilitacion-de-empresas-disposicion-ndeg-79392025) 🟩
- [Entrada en vigencia (argentina.gob.ar)](https://www.argentina.gob.ar/noticias/hoy-entra-en-vigencia-la-disposicion-793925-de-cosmeticos-domisanitarios-y-productos) 🟩
- [Qué implica la flexibilización (Infobae)](https://www.infobae.com/salud/2025/10/27/de-a-poco-la-nueva-anmat-que-implica-la-flexibilizacion-para-productos-cosmeticos-y-de-higiene-personal/) 🟨
- [Instructivo de habilitación de establecimientos (ANMAT, 2015)](http://www.anmat.gob.ar/webanmat/formularios/cosmeticos/Instructivo_Habilitacion_2015.pdf) 🟩 (anterior a la disposición, sirve para el marco general)

**Laboratorios** — todos 🟨 sitio propio, salvo donde se indica
- [Eneve Cosmética](https://www.enevecosmetica.com.ar/)
- [Carmenta / Biosinergia](https://carmenta-estudiosnaturales.com/biosinergia-agenciacosmetica/)
- [Senda Aromática](https://sendaaromatica.com/fabricacion-de-cosmetica-a-terceros/)
- [Pasmanter](https://www.pasmanter.com.ar/servicios/)
- [Oxapharma](https://oxapharma.com/outsoursing-services/)
- [Laboratorio Reig](https://www.laboratorioreig.com/)
- [Livepharma](https://www.livepharma.com.ar/servicios.html)
- [Directorio de fábricas y laboratorios de cosméticos en Argentina](https://www.directoriodefabricas.com/argentina/fabricantes-cosmeticos-argentina.html) 🟨
- [Top 5 private label cosmetics manufacturers in Argentina](https://xiranskincare.com/top-5-private-label-cosmetics-manufacturers-in-argentina/) 🟥 blog de 466 días, de donde salen los MOQ de Basel y LACA
