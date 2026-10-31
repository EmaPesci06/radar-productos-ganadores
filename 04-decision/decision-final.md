# Acta de decisión — ¿cuál es nuestro producto winner?

| | |
|---|---|
| **Estado** | 🟡 **DESBLOQUEADA — 16 candidatos cargados, 3 objeciones del radar pendientes de resolver** |
| Fecha de apertura | 2026-10-31 |
| Fecha de desbloqueo | 2026-10-31 (vault ECOMAI cargado) |
| Decisor | Emanuel |
| Fuente del ranking | `Vault ECOMAI/05 Plan de accion/Comparativa integral AR y Planificacion - 31 octubre.md` |

---

## Requisitos de desbloqueo

| # | Requisito | Estado |
|---|---|---|
| 1 | Mínimo 3 candidatos con ficha completa | ✅ **16 cargados** (12 puntuados + 4 descartados) |
| 2 | Costo / unit economics calculado | 🟡 Parcial: calculado para lumbar y ebook #1. Faltan cotizaciones de proveedor para el resto |
| 3 | Corrida de radar y semáforo de saturación | ✅ Radar AR hecho sobre todos |
| 4 | Doc A emitido | 🟡 Parcial: almohada lumbar y antifaz tienen archivo formal. El resto está puntuado pero sin Doc A formal |
| 5 | Scorecard corrido con el mismo criterio | ✅ `python3 01-scorecard/calcular_score.py` |

---

## El ranking

```
 1   Almohada Lumbar Hueso (Ciática) + Bono Ebook      fisico-local      95   EJECUTAR YA
 2   Almohada de Embarazo (U/C) + Brazo Lactancia      fisico-local      94   EJECUTAR YA
 3   Ebook #1: Reto 28 Días Somáticos + Nervio Vago    digital           93   EJECUTAR YA
 4   Ebook #2: Chau Pañal en 3 Días + Kit Imprimible   digital           92   EJECUTAR YA
 5   Jabón / Gel de Caqui (Nonenal) Pack x3            fisico-lab        90   EJECUTAR YA
 6   Loción / Spray de Magnesio Tópico Nocturno        fisico-lab        89   EJECUTAR YA
 7   Ebook #3: Control Pélvico Masculino 21 Días       digital           88   EJECUTAR YA
 8   Guantes de Compresión Artritis (Pack x2/x3)       fisico-courier    84   SEGUNDA OLA
 9   Kit Motoquero / Delivery                          fisico-local      84   SEGUNDA OLA
10   Kit Germinador de Brotes + 3 Semillas             fisico-local      83   SEGUNDA OLA
11   Protector Bucal Bruxismo (Pack x2)                fisico-courier    82   SEGUNDA OLA
12   Antifaz de Vapor Autocalentable                   fisico-courier    68   DESCARTADO (gate)
13-16  Antiatragantamiento · Esmalte marcador ·        fisico-courier     —   DESCARTADO (gate)
       Manta perros · Toalla refrescante
```

---

## Aplicación del método (escrito antes de ver los números)

### Regla principal: gana el score más alto ≥ 88 sin gates ni ejes bloqueantes

→ **Almohada Lumbar Hueso (Ciática): 95/100.**

### Regla de desempate 1: margen < 5 puntos = empate técnico

Se activa. #1 (95) y #2 (94) están a **1 punto**. También #3 (93) y #4 (92).

**Pero el empate es aparente, y es el hallazgo más importante de la corrida:**
#1 y #2 **no son alternativas**. Comparten los mismos proveedores locales de espuma
y textil, la misma marca (Marca 1, ya activa desde el 08/10), el mismo bono (Ebook
Ciática) y el mismo order bump (Loción de Magnesio). No hay que elegir entre ellos:
**son el mismo bet**.

Lo mismo pasa con los ebooks #3 y #4: comparten infraestructura (Shopify/Tiendanube +
Mercado Pago en ARS) y método de producción (Claude + Gamma + Canva).

→ **La decisión real no es "qué producto", es "qué ecosistema primero".**

### Reglas 2 a 4

| Regla | Resultado |
|---|---|
| **2. Gana el de ecosistema más claro** | Ecosistema 1 (Descanso y Columna): 4 productos + bono + bump, y ya está vivo con Marca 1 |
| **3. Gana el de menos pendientes de proveedor** | Ecosistema 1: 9 fabricantes ya contactados el 30/10. Los ebooks: cero proveedor, producción propia |
| **4. Gana el que se testea más barato** | Ebooks: USD 50 contra USD 100 de los físicos, y sin comprar stock |

---

## Recomendación

El sistema no apunta a un producto único, apunta a **dos movimientos en paralelo que no
compiten por los mismos recursos**:

### 🥇 Winner físico: Almohada Lumbar Hueso (Ciática) — 95/100

Es el score más alto, tiene el ecosistema más claro, el proveedor más avanzado (9
fabricantes contactados) y **no arranca de cero**: se cuelga de la Marca 1 que ya está
lanzada. La almohada de embarazo (94) entra detrás con los mismos proveedores, no en
vez de.

- Oferta: $49.900 (1u) · **$74.900 (combo Lumbar + Rodillas)** · $84.900 (pack x2)
- Todos con el Ebook Ciática 21 Días gratis
- CPA breakeven calculado: **$24.565** (1u) y **$44.068** (pack x2) — ver abajo
- Test: USD 100, GO con CPA ≤ $22.000 en 1u o ≤ $30.000 en combo

### 🥈 Winner digital: Ebook #1 Reto 28 Días Somáticos — 93/100

No compite con la almohada: se testea con USD 50, no necesita proveedor ni stock, y
hace caja mientras la espuma se cotiza. Su ventaja real no es el producto: es el
**hueco de cobro** — nadie en ese nicho cobra en pesos con Mercado Pago.

### 🔴 Lo que queda afuera, y por qué

**Importar por courier.** Los candidatos `fisico-courier` promedian **33,4/100** contra
**89** de `fisico-local`. No es mala suerte con un producto: es que la ruta tiene tres
peajes estructurales (aduana, tope de 50 kg, ancla de precio de MELI). La única
excepción razonable son los guantes de compresión (84), si en algún momento se quiere
hacer una importación chica de prueba.

---

## ⚠️ Objeciones del radar del 31/10 — leer antes de decidir

Después de escribir la recomendación de arriba corrí el Radar AR directo sobre Meta Ad
Library (medición independiente, **el mismo día** que la del vault, con otra
herramienta). Tres de los cuatro candidatos top no dieron lo mismo.

Por el flujo de `06 Analisis compartido/README.md` esto va como **objeción, y decide
Emanuel**: no cambié ningún score. Detalle completo en
`05-relevamientos/2026-10-31-radar-ar-top4.md`.

| Candidato | Hueco vault | Lo que medí | Objeción |
|---|---|---|---|
| Almohada Lumbar | 19/20 | Rodillo hueso **sin competencia**, confirmado. Pero 5 marcas arrancaron en 10 días en almohada ortopédica | 🟡 menor, 19→17 |
| Almohada Embarazo | 20/20 "0 marcas DTC" | **Micolecho: 716 días al aire**, copy al público, tienda propia. Y figura como *proveedor* en el plan | 🔴 fuerte, 20→12 |
| Ebook #1 Somáticos | 19/20 "nadie cobra en ARS" | **Cursa Virtual: 169 días** en tienda `.com.ar`. 3 operadores en `impultienda.ar`. **5 marcas en 15 días.** Isabel Navarro con 14 de 21 ads y ya clonada | 🔴 fuerte, 19→8 |
| Ebook #2 Chau Pañal | 20/20 | **Confirmado exacto.** 18 marcas, todas físicas. Cero digital | ✅ se sostiene |
| Ebook #3 Pélvico | 19/20 | **No se pudo medir** (query SIN_LEER). Único de los 7 a ciegas en este eje | 🟡 sin verificar |

### Cómo quedaría el ranking si aceptás las objeciones

```bash
python3 01-scorecard/calcular_score.py --propuesto
```

```
 1  Almohada Lumbar Hueso           93  (95, -2)   EJECUTAR YA
 2  Ebook #2 Chau Pañal             92  (92)       EJECUTAR YA
 3  Jabón de Caqui                  90  (90)       EJECUTAR YA
 4  Loción de Magnesio              89  (89)       EJECUTAR YA
 5  Ebook #3 Control Pélvico        88  (88)       EJECUTAR YA  ← a ciegas
 6  Almohada de Embarazo            86  (94, -8)   SEGUNDA OLA
10  Ebook #1 Somáticos              82  (93, -11)  SEGUNDA OLA
```

**Lo que cambia:** el winner físico no se mueve — la Almohada Lumbar gana en los dos
escenarios. **El winner digital sí: pasa del Ebook #1 Somáticos al Ebook #2 Chau
Pañal.** Es el único cuyo hueco verifiqué de forma independiente y dio exacto, y su
ventana estacional (octubre-febrero, antes del jardín en marzo) **está abierta ahora**.
En el plan de 6 semanas está recién en la Semana 3: conviene adelantarlo.

Dos cosas más que salieron del radar y sirven para ejecutar:

- **El formato del Chau Pañal es advertorial, no video de producto.** *UltraDries
  Argentina* corre 4 advertorials con 16 días en ese mismo dolor: el formato ya está
  validado acá.
- **Referencia de formato para el nicho de ciática:** *María Elena Vargas*, una
  página-persona con 10 advertorials y 166 días al aire apuntando a GroundingWell. Es el
  patrón de advertorial para +50 del M2-04, corriendo en Argentina.

---

## Tres cosas para tener presentes antes de ejecutar

Salen de correr los números, no del ranking.

### 1. El scorecard solo te diría que lances 7 productos a la vez

Hay **7 candidatos en zona EJECUTAR YA**. Lanzar 7 cosas en paralelo contradice el
principio de foco del propio curso — y el relevamiento muestra por qué: las tiendas
que ganan afuera son **monoproducto con foco 80-100%**.

El plan de 6 semanas del vault ya resuelve esto secuenciando por ecosistema. **El
scorecard prioriza; el plan de 6 semanas es el que manda sobre qué se hace primero.**

### 2. Los ebooks tienen el margen más fino de la cartera, y el test no lo prueba

Corriendo `02-costos/rentabilidad-ar.py` sobre el ebook #1:

| | |
|---|---|
| CPA de breakeven | $17.912 |
| Con CPA real de $15.000 | neto **$2.912** por venta (14,6%) |
| ROAS real | **1,33x** |

Dos cosas:

- El **ROAS queda en 1,33x**, muy por debajo del ROAS ≥ 2,5 que el propio vault exige
  a los físicos. No está mal el ebook: es que $19.900 con CPA $15.000 deja $2.912. El
  margen del 90% se lo come la publicidad.
- La regla de corte (**5 ventas con USD 50**) implica un CPA de **$15.600**, casi igual
  al breakeven de $17.912. **Llegar justo a 5 ventas valida la demanda pero no prueba
  que dé plata.** Tratarlo como validación de ángulo, no de rentabilidad.

Esto no cambia el ranking (los ebooks puntúan alto por operativa y hueco, y es cierto).
Cambia **qué esperar del test**. Ver `00-marco/02-producto-ganador-eprod.md`.

### 3. El combo es el que cierra, no la unidad

| Oferta | Precio | $/unidad | CPA breakeven | Margen pre-ads |
|---|---|---|---|---|
| Almohada lumbar 1u | $49.900 | $49.900 | $24.565 | 49,2% |
| Pack x2 | $84.900 | $42.450 | **$44.068** | **51,9%** |

El precio por unidad **baja** y el margen **sube**, porque los costos fijos por pedido
se reparten. Es la regla 2 del patrón y la lección de M2-12. El combo Lumbar + Rodillas
a $74.900 es el que hay que empujar como "el más elegido".

---

## DECISIÓN

*La completa Emanuel. El sistema recomienda, no decide.*

| | |
|---|---|
| **Winner físico** | ⬜ |
| **Winner digital** | ⬜ |
| **Qué se frena** | ⬜ |
| **Por qué** | ⬜ |
| **Fecha** | ⬜ |

### Si se confirma la recomendación, el siguiente paso es la Semana 1 del plan

1. Recibir las cotizaciones de los 9 fabricantes de espuma contactados el 30/10
   (filtro: forma de hueso tallada real, no cilindro liso, a ≤ $10.000-$12.000)
2. Contactar 5 laboratorios cosméticos a façon en AMBA (jabón de caqui + loción de magnesio)
3. Generar el Ebook Ciática 21 Días (bono) y el Ebook #1 Somáticos + sus 4 bonos
4. Desglosar la landing de Isabel Navarro (`herramientas-somaticas.netlify.app`)

Plan completo: `Vault ECOMAI/05 Plan de accion/Comparativa integral AR y Planificacion - 31 octubre.md` §5.

---

## Descartados, con el motivo escrito

| Candidato | Score | Motivo | Rescate |
|---|---|---|---|
| Antifaz de vapor | 68 | CPA breakeven de $7.353, por debajo del piso comprable en Meta AR. Y 300 kits = 108 kg, rompe el tope de 50 kg del courier | Order bump sin aroma en el checkout de las almohadas |
| Dispositivo antiatragantamiento | — | Producto Médico Clase II sin PM de ANMAT. Brecha de precio insalvable ($13.495 en MELI vs $129.999 DTC) | Solo con alianza con un importador que ya tenga PM |
| Esmalte en marcador | — | Cosmético importado sin legajo + líquidos restringidos por DHL + nadie busca el término en AR | Ninguno |
| Manta refrescante perros | — | Gel pesado (1,5-3 kg), talles que parten el stock, y Gadnic ya domina MELI con Full y cuotas | Ninguno |
| Toalla refrescante | — | Commodity quemado en MELI, CPA breakeven $8.000-$9.000, y la ventana de verano ya no da los tiempos | Regalo/bump de verano si se compra en Once a $2.500 |

Los 4 últimos los puntuó el vault **como grupo** (<60/100) sin desglose por eje. No les
inventé scores: van sin calificar, con el gate documentado. El gate manda igual.
