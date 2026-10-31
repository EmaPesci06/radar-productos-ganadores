# Qué es un producto ganador — EPROD (digital)

> ⚠️ **Nota de origen.** Nuestras skills del curso (`doc-a-validator`,
> `radar-adlibrary-ar`, `importacion-alibaba-ar`, `doc-b-builder`) están escritas
> **íntegramente para producto físico**. No hay criterio de eprods codificado en el
> sistema. Este documento es nuevo: construido trasladando la lógica del Doc A a lo
> digital, más evidencia web de 2026 (ver `04-evidencia-web-2026.md`).
> Tratarlo como **v1 a discutir**, no como criterio heredado.

---

## El cambio de eje: qué se invierte respecto del físico

Los dos negocios no se evalúan igual. Lo que en físico es el riesgo principal, en
digital es gratis — y al revés.

| Eje | Físico | Eprod |
|---|---|---|
| Margen bruto | 20-40% neto tras costos | **85-95%**, casi irrelevante como filtro |
| Costo marginal por unidad | Alto (producto + flete + impuestos) | ~0 |
| Capital inicial | Stock, importación, aduana | Tiempo de producción |
| Riesgo de inventario | Alto | **Nulo** |
| Logística y regulación | ANMAT, aduana, courier | Nulo |
| **Lo que mata el negocio** | El markup no da / se agota el stock | **El CAC supera el ticket** y no hay escalera de valor |
| **Lo que hay que probar antes** | Que el margen cierre | **Que alguien pague**, no que alguien se interese |
| Barrera de entrada | Capital | **Autoridad / prueba** — y es más difícil de copiar |
| Reembolsos | ~bajo | Alto (10-15% típico en infoproductos); afecta el flujo real |

**Consecuencia práctica:** en físico la pregunta es *"¿cierra el margen?"*. En eprod
el margen siempre cierra, y la pregunta es *"¿puedo adquirir un cliente por menos de
lo que vale, y tengo con qué subirle el ticket después?"*.

---

## Los MUSTs de un eprod

Mismo criterio que el Doc A: cada uno se califica 0-5 y **falla si está por debajo de 3**.

| # | MUST | Cómo se verifica |
|---|---|---|
| E1 | **Alguien ya está pagando por resolver este dolor** | Competencia cobrando con precio público: Hotmart, Gumroad, Etsy, cursos sueltos, Ad Library. No "hay interés" — hay precio y hay checkout. |
| E2 | **El dolor es específico, no una categoría** | "Aprender marketing" o "ponerse en forma" no vende. Tiene que estar acotado el cliente, el caso de uso y la transformación. |
| E3 | **Tenemos autoridad o ventaja injusta para hablar de esto** | Resultado propio, experiencia, acceso, audiencia, o data que otro no tiene. Sin esto, el eprod es un PDF más. |
| E4 | **La transformación es demostrable** | Se puede mostrar un antes/después, un número, un entregable concreto. Si no se puede probar, no se puede vender dos veces. |
| E5 | **Hay un canal de adquisición con CAC por debajo del ticket** | Orgánico existente, ads con números de la categoría, o afiliados. Un eprod sin canal es un archivo en una carpeta. |
| E6 | **Hay escalera de valor arriba del producto de entrada** | Entry → core → premium (plantilla → curso → servicio/comunidad). Un solo SKU digital no sostiene un negocio. |
| E7 | **El producto se puede entregar y sostener sin que nos coma la vida** | Si requiere soporte 1-a-1 permanente, no es un eprod: es un servicio disfrazado. |

**NO-GO automático si:**
- Falla E1 (nadie paga) o falla E2 (promesa genérica) → muere acá, sin más research
- Fallan 2+ MUSTs cualesquiera
- El CAC estimado > 50% del ticket y no hay escalera de valor que lo recupere

---

## Los NICEs

| NICE | Por qué suma |
|---|---|
| Recurrencia natural (comunidad, suscripción, actualizaciones) | LTV sin CAC nuevo |
| Producible con lo que ya tenemos (sin filmar 40 horas) | Time-to-market |
| Reusable: un mismo activo en varios formatos | Plantilla → curso → cohort |
| Permite afiliados | Canal sin CAC propio (fuerte en LATAM vía Hotmart) |
| Bajo índice de reembolso esperable en la categoría | Flujo real vs flujo bruto |
| Se puede vender en USD a mercado hispano amplio | Saca el techo del poder de compra local |

---

## Formatos, ordenados por dificultad de ejecución

Evidencia web 2026 (vendor blogs, confianza media — ver `04-evidencia-web-2026.md`):
los **templates y assets simples** son la categoría de mayor volumen en Gumroad y
Etsy, y la más fácil de lanzar. Los cursos tienen ticket más alto pero mucho más
costo de producción y más reembolsos.

| Formato | Ticket típico | Costo de producción | Riesgo | Cuándo elegirlo |
|---|---|---|---|---|
| Plantilla / preset / asset pack | Bajo | Bajo | Bajo | Entrada a la escalera, validar demanda rápido |
| Printable / planner | Bajo | Bajo | Bajo | Nicho con intención de compra estética clara |
| Ebook / guía | Bajo-medio | Bajo-medio | Bajo | Capturar leads o validar la promesa |
| Curso autogestionado | Medio-alto | **Alto** | Medio | Solo con E1 y E3 fuertes ya probados |
| Cohort / comunidad | Alto | Medio + tiempo recurrente | Medio | Si hay autoridad y aguanta recurrencia |
| Servicio productizado | Alto | Alto (tiempo) | Alto | Hace caja rápido; **no escala** — usar como back-end |

**Recomendación de secuencia:** validar con el formato barato (plantilla/guía) y
recién después construir el caro (curso/cohort) sobre un dolor ya probado con
checkout real.

---

## Unit economics de un eprod (lo que sí hay que calcular)

El margen bruto no es el número que importa. Los que importan:

```
Ticket (ARS o USD)
− comisión de plataforma      (Hotmart ~9,9% + USD 0,50 por venta — verificar vigente)
− pasarela de pago            (Mercado Pago / Stripe)
− impuestos                   (consultar con contador: IVA/Ganancias/IIBB según condición)
− reembolsos esperados        (10-15% típico; usar el de la categoría si se conoce)
= Ingreso neto por venta

CAC = inversión en ads ÷ ventas atribuidas

Margen de contribución = Ingreso neto − CAC
LTV = Ingreso neto × compras promedio en la escalera
```

**Umbrales de trabajo** (nuestros, para discutir — no son benchmark de industria):

| Ratio | 🟢 | 🟡 | 🔴 |
|---|---|---|---|
| CAC / Ticket | < 30% | 30-50% | > 50% sin escalera |
| LTV / CAC | ≥ 3 | 2-3 | < 2 |
| Reembolsos | < 8% | 8-15% | > 15% |

Calculadora: `02-costos/margen-eprod.py`.

---

## Saturación en eprods: cómo se mide

El radar de Ad Library sirve igual, pero hay fuentes propias de digital:

| Señal | Dónde | Qué leer |
|---|---|---|
| Quién anuncia y hace cuánto | Meta Ad Library AR/ES/MX | Días al aire 60+ = oferta probada. Mismo criterio que físico. |
| Oferta y precios de la categoría | Hotmart marketplace, Gumroad, Udemy | Rango de ticket real, no el aspiracional |
| Demanda de búsqueda | Google Trends, autocompletado, "people also ask" | Si nadie busca el dolor, el ads tiene que crear la categoría (carísimo) |
| Dolor crudo, en sus palabras | Reddit, TikTok, comentarios de YouTube | Materia prima del copy. Es la VOCC del Doc B |
| Oferta existente gratis | YouTube, blogs | **Clave:** si la respuesta completa está gratis y bien hecha, el eprod tiene que vender otra cosa (velocidad, acompañamiento, plantilla lista) |

**La pregunta que no está en el radar de físicos:** *¿por qué alguien pagaría por esto
si YouTube ya lo explica?* Las respuestas válidas son tres: **velocidad**
(te ahorro 40 horas), **certeza** (está probado, no tenés que adivinar) y
**acompañamiento** (alguien te corrige). Si no hay ninguna de las tres, es NO-GO.

---

## Niveles de conciencia: igual que en físico

El 80% de los ads ganadores juega en **Consciente del problema** y **Consciente de
la solución**. En eprods esto se cumple igual o más, porque la categoría casi siempre
existe. Si se propone más del 30% del presupuesto creativo en niveles extremos
(No Consciente o Totalmente Consciente), hay que justificar por qué.

Distribución sugerida (del `doc-b-builder`, aplica tal cual):

- 50% niveles 2-3 (problema + solución)
- 25% nivel 4 (producto) — retargeting / MOF
- 15% nivel 5 (totalmente consciente) — BOF, promos
- 10% nivel 1 (no consciente) — TOF amplio, solo si el nicho lo justifica
