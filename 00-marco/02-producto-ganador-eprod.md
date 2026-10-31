# Qué es un producto ganador — EBOOK / INFOPRODUCTO

> **Corrección del 31/10/2026.** La v1 de este archivo la escribí yo inventando siete
> MUSTs (E1-E7) porque no tenía acceso al material del curso. Con el vault cargado
> quedó claro que **el Módulo 8 ya define los criterios**, y que uno de mis MUSTs
> era directamente **contrario** al del curso. Ver §"Dónde me había equivocado".
>
> Fuente: `Vault ECOMAI/01 Modulos/Modulo 8 - Ebooks/` (M8-01, M8-03) y
> `05 Plan de accion/Hueco ebooks AR - 31 octubre.md`.

---

## El principio

**No se vende un producto, se vende una transformación.** La pregunta guía es: qué
problema puedo ayudar a resolver, para quién, y cómo lo voy a comunicar (M8-01).

> "Las personas no compran archivos, cursos o productos. Compran resultados,
> soluciones o transformaciones." No se venden 300 recetas saludables: se vende que
> esa persona se sienta mejor consigo misma.

Un producto ganador resuelve una **necesidad real que la gente ya está buscando**:
ganar dinero, ahorrar tiempo, verse mejor, sentirse mejor.

---

## Los 5 nichos donde buscar

Las áreas más importantes de la vida (M8-01):

| Nicho | |
|---|---|
| **Salud** | el más fuerte en el relevamiento real (somáticos, piso pélvico, ciática) |
| **Dinero** | |
| **Relaciones** | |
| **Mentalidad** | nervio vago, cortisol, ansiedad |
| **Productividad** | |

Y una sexta que apareció en la práctica y funciona muy bien en AR: **maternidad**
(chau pañal, sueño infantil).

---

## Criterios para elegir una oferta a modelar (M8-03)

Los tres filtros duros al mirar la Biblioteca de Anuncios:

| # | Filtro | Por qué |
|---|---|---|
| 1 | **≥ 20 anuncios activos corriendo hace más de 3-4 días** | Para asegurarse de que no es alguien recién testeando |
| 2 | **Sin marca personal detrás** | "Si Taylor Swift vende un ebook, le van a comprar a ella por quién es." Una marca personal no se puede modelar |
| 3 | **Que venda un solo producto**, no varios | Tienda monoproducto = sabe qué vende |

### Modelar ≠ copiar y pegar

Copiar literal una oferta escalada **beneficia al original**: esa persona tiene más
anuncios, más tiempo al aire y más presupuesto, ofreciendo exactamente lo mismo. El
cliente le compra a ella.

Modelar es tomar la oferta escalada como base y **subir el valor percibido**:

- Combos (2x1, 3x1, 4x1)
- Sumar clases grabadas
- Mejorar la estética
- Mejorar la promesa y adaptarla a los dolores reales del cliente
- Mejorar la comunicación de la landing

### Más criterios que salieron de la práctica

Del relevamiento real del 31/10, lo que separó al #1 del resto:

| Criterio | Caso |
|---|---|
| **Días al aire por encima de 150** | Isabel Navarro 172 días · Big Little Feelings 355 días |
| **Hueco de COBRO, no solo de producto** | El hallazgo que define el ebook #1: nadie cobra en **pesos con Mercado Pago**. Isabel Navarro cobra en moneda extranjera con español neutro. Entrar en **ARS con voseo** es el diferencial |
| **Estacionalidad a favor** | "Chau pañal" tiene pico de octubre a febrero: las madres sacan el pañal con el calor y antes del jardín en marzo |
| **Dolor vergonzante** | Piso pélvico masculino: nadie va a una farmacia de barrio a pedirlo. Compra 100% privada desde el celular |
| **El dolor tiene traba física** | Regla 3 del patrón: cuando el producto físico choca con ANMAT, se entra con el ebook. Cuando el físico es fuerte, el ebook va de **bono gratis** |

---

## La promesa

Es lo primero que ve el cliente al entrar a la landing. Tiene que ser **alcanzable**:
no vender humo (M8-01).

Para subir el valor percibido, mostrar **beneficios y resultados**, no características
técnicas. No una lista de funciones: "organizar tu dinero y dejar de preocuparte".

**Mobile-first, no negociable:** revisar siempre cómo se ve la oferta en celular,
porque el 99% de las ventas van a ser desde ahí (M8-01).

---

## Unit economics: el eje más flojo de los ebooks, y por qué

El margen bruto de un ebook es ~90%, lo que lo hace parecer imbatible. **No lo es**,
y los números del vault lo muestran: en el ranking maestro del 31/10, los tres ebooks
sacaron **17, 15 y 13 sobre 20** en el eje de margen y ecosistema — los tres puntajes
más bajos de los siete candidatos aprobados.

### Lo que encontré al correr los números

Corriendo `02-costos/rentabilidad-ar.py` sobre el ebook #1 ($19.900, Responsable
Inscripto, sin costo de producto):

```
CPA de breakeven        $17.912
Con CPA real de $15.000:
  Neto por venta         $2.912   (14,6% sobre venta)
  ROAS real                1,33x
```

**Dos hallazgos que conviene tener presentes antes de lanzar:**

1. **El ROAS del ebook queda en 1,33x**, muy por debajo del **ROAS ≥ 2,5** que el
   propio vault exige para los productos físicos. No es que el ebook esté mal: es que
   un ticket de $19.900 con un CPA de $15.000 deja $2.912. El margen del 90% se lo
   come la publicidad, no los costos.

2. **La regla de corte del test es un test de breakeven, no de rentabilidad.** USD 50
   (~$78.000) dividido 5 ventas da un CPA implícito de **$15.600**, que es casi
   exactamente el CPA de breakeven de $17.912. Llegar justo a 5 ventas con USD 50
   **valida que hay demanda, pero no prueba que el negocio dé plata.**

3. **El order bump mueve menos de lo que parece.** $9.900 con take rate del 20% aporta
   $1.782 promedio por venta: sube el CPA tolerable apenas un 10%.

**Qué hacer con esto (no es un NO-GO, es una condición):**

- El test de USD 50 sirve para lo que sirve: saber si el ángulo engancha. Tratarlo como
  validación de demanda, no como prueba de rentabilidad.
- Para que el ebook sea negocio hace falta **una de dos**: subir el ticket (bundle de
  ebooks, clases grabadas, acceso a comunidad) o **bajar el CPA** con creativos que
  rindan mejor que el promedio.
- El take rate del bump ≥ 20% que pide el vault es un **piso, no un objetivo**. Vale la
  pena diseñar el bump para 30-40%.

> Esto no contradice el ranking: los ebooks están arriba porque ganan en operativa
> (20/20: cero ANMAT, cero aduana, cero stock) y en hueco de Meta AR. Son el camino
> más rápido a facturar, con el margen más fino. Saberlo de antemano evita la sorpresa.

---

## Dónde me había equivocado

Para que quede trazable qué era mío y qué es del curso:

| Mi v1 (descartada) | El criterio real | Por qué estaba mal |
|---|---|---|
| **MUST E3: "tenemos autoridad o ventaja injusta para hablar de esto"** | M8-03 pide **lo contrario**: elegir ofertas **SIN marca personal** | Mi criterio asumía un modelo de creador construyendo audiencia propia. El modelo del curso es **modelar ofertas escaladas**: la marca personal es un obstáculo, porque no se puede modelar. Con mi criterio, los tres ebooks del ranking habrían fallado un MUST |
| MUST E1-E7 con umbrales propios | Los 3 filtros de M8-03 + los 5 ejes del scorecard | Inventé una estructura paralela a la que ya existía |
| Umbrales CAC/ticket de 30% / 50% | **CPA ≤ $15.000** y ROAS ≥ 2,5, en pesos | Mis porcentajes no tenían referencia argentina. Los del curso sí |
| Pesos propios (demanda 25 / canal 20 / autoridad 20 / escalera 20 / entregabilidad 15) | Los 5 ejes de 20 del vault, iguales para físicos y ebooks | Tener dos scorecards impedía que físicos y ebooks compitieran en un solo ranking, que es justo lo que hace falta para decidir |

**Lo único de mi v1 que sobrevive** (y está marcado como mío, no heredado): el cálculo
de unit economics de arriba y los tres hallazgos que salieron de correrlo.
