# Acta de decisión — ¿cuál es nuestro producto winner?

| | |
|---|---|
| **Estado** | ⬜ **PENDIENTE — bloqueada** |
| Fecha de apertura | 2026-10-31 |
| Decisor | Emanuel |
| Bloqueante | No hay candidatos reales cargados (ver `GAPS.md`) |

---

## Por qué está bloqueada y no decidida

El sistema de decisión está completo y funcionando: criterios, gates, pesos,
calculadoras validadas contra un caso real. **Lo que falta son los candidatos.**

Los productos ganadores anteriores — físicos y eprods — están en la carpeta
`Ecommerce Curso`, que esta sesión no pudo leer. Lo único que pude reconstruir del
sistema previo son las cuatro skills del curso que ya están sincronizadas en la cuenta
(`doc-a-validator`, `radar-adlibrary-ar`, `importacion-alibaba-ar`, `doc-b-builder`),
y de ahí salen todos los criterios de `00-marco/`.

**Declarar un winner hoy sería deshonesto**, por una razón concreta: el pre-screening
dejó dos direcciones en verde y las dos son eprods, no porque los eprods sean mejores
sino porque son las únicas donde hay autoridad demostrable con la información que
tengo. Elegir una de esas sería elegir **el único candidato que alcancé a ver**, no el
mejor. Ver `03-candidatos/long-list-inicial.md` § "La asimetría que hay que mirar".

El scorecard está programado para avisar esto mismo: con menos de dos candidatos sobre
el piso de 60, dice que el winner no está comparado.

---

## Qué desbloquea la decisión

| # | Requisito | Estado |
|---|---|---|
| 1 | Mínimo **3 candidatos** con ficha JSON + MD completas | ⬜ |
| 2 | Cada uno con **costo puesto en AR calculado** (físicos) o **unit economics** (eprods) | ⬜ |
| 3 | Cada uno con **corrida de radar** y semáforo de saturación | ⬜ |
| 4 | Cada uno con **Doc A** emitido (GO / GO con flags / NO-GO) | ⬜ |
| 5 | Scorecard corrido sobre todos, con el mismo criterio | ⬜ |

Mientras falte el 1, el resto no tiene sentido.

---

## Cómo se va a decidir (acordado de antemano)

Esto se escribe **antes** de ver los números, para que el método no se acomode al
resultado que queramos.

### Regla principal

Gana el **score más alto** del scorecard, siempre que sea ≥ 60 y no tenga gates
fallados.

### Reglas de desempate

1. **Margen < 5 puntos = empate técnico.** No gana el score. Se decide por el eje que
   más importa hoy, y queda escrito cuál fue y por qué.
2. A igualdad, gana el que tiene **ecosistema más claro** (3+ productos lógicos
   alrededor del mismo dolor). El héroe es la puerta de entrada, no el negocio.
3. A igualdad, gana el que tiene **menos pendientes de proveedor**. Un proveedor sin
   validar es un NO-GO esperando a pasar.
4. A igualdad, gana el que se puede **testear más barato**. El que se valida con menos
   plata vale más que el que promete más.

### Lo que NO decide

- Que nos guste más el producto
- Que ya hayamos invertido tiempo en investigarlo (costo hundido)
- Que sea el que investigamos último (sesgo de recencia — es exactamente la razón por
  la que el Doc A obliga a una sesión por producto)
- Un NO-GO defendido sin evidencia nueva

---

## DECISIÓN

*(a completar cuando se desbloquee)*

### Winner elegido

**Producto:** ___
**Tipo:** físico / eprod
**Score:** ___ /100
**Veredicto:** ___

### Las 3 razones, con evidencia

1.
2.
3.

### Flags que quedan abiertas

| Flag | Cómo se resuelve | Antes de qué |
|---|---|---|
| | | |

### Descartados y por qué

| Candidato | Score | Motivo del descarte | Pivot sugerido |
|---|---|---|---|
| | | | |

Los descartados se guardan con el motivo escrito: evita volver a evaluar lo mismo en
tres meses.

### Primeros pasos post-decisión

1. Doc B del winner (`doc-b-builder`): VOCC real, avatares, ángulos, pricing
2. Validar proveedor antes de comprar stock (si es físico)
3. Definir el test más barato posible y su criterio de éxito **antes** de gastar
