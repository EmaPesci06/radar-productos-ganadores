# Scorecard — la matriz de decisión

El scorecard existe para que dos candidatos sean **comparables**. Mismos ejes,
mismos pesos, misma escala. Sin esto, la decisión la gana el producto que
investigamos último, no el mejor.

---

## Cómo funciona

```
1. GATES      → ¿sobrevive? Si falla un gate, score = 0 y NO-GO. No se calcula nada más.
2. EJES        → cada eje se califica 0-5 con evidencia citable
3. PESO        → cada eje pesa distinto según si es físico o eprod
4. SCORE       → 0-100, comparable entre candidatos
5. VEREDICTO   → GO / GO con flags / NO-GO
```

Escala de cada ítem:

| Score | Significado |
|---|---|
| 5 | Evidencia fuerte y directa. Múltiples fuentes coinciden. |
| 4 | Evidencia clara, con algún hueco menor. |
| 3 | Evidencia suficiente. **Piso de aprobación de un MUST.** |
| 2 | Evidencia débil o indirecta. |
| 1 | Casi nada. Indicios sueltos. |
| 0 | **Sin evidencia suficiente** (declararlo así, no inventar un 2) |

> Un MUST en 0-2 es un MUST **fallado**. No se promedia para taparlo.

---

## GATES — NO-GO automático

Si cualquiera de estos se cumple, el candidato muere sin research.

### Gates comunes

| Gate | Por qué |
|---|---|
| Fallan 2+ MUSTs del eje correspondiente | Regla del Doc A |
| No hay evidencia de que **alguien ya pague** por resolver el dolor | Sin esto todo lo demás es especulación |
| El problema es una moda de <6 meses sin historial | No sostiene una marca |

### Gates de físico

| Gate | Por qué |
|---|---|
| Producto en la **lista de excluidos** y sin proveedor local | Ver `02-costos/reglas-y-exclusiones.md` |
| Markup alcanzable **< ×3** sobre el costo puesto en AR | La tabla de markup es piso, no objetivo |
| Semáforo de saturación 🔴 **sin** diferencial de oferta/formato/segmento | Entrar de frente contra alguien que ya optimizó |
| Falla un MUST de Market Fit **+** un MUST de Ecosistema | Regla del Doc A |

### Gates de eprod

| Gate | Por qué |
|---|---|
| Falla E1: **nadie está pagando** por este dolor hoy | MUST ineludible |
| Falla E2: la promesa es una **categoría**, no un dolor específico | "Aprender marketing" no vende |
| CAC estimado > 50% del ticket **y** no hay escalera de valor | El negocio no cierra |
| La respuesta completa está **gratis y bien hecha** en YouTube, y no vendemos velocidad / certeza / acompañamiento | No hay razón para pagar |

---

## Pesos — PRODUCTO FÍSICO

| Eje | Peso | Qué mide | MUSTs incluidos |
|---|---|---|---|
| **A. Market Fit** | **30%** | ¿El dolor existe, acá, y se paga? | Marcas invirtiendo afuera · Ticket pagado · Dolor existe en AR · Precio lógico local · Evergreen |
| **B. Unit economics** | **25%** | ¿Cierra el margen con el costo puesto en AR? | Markup vs tabla · Costo real calculado · Peso/volumen |
| **C. Saturación / espacio** | **15%** | ¿Hay lugar para entrar? | Semáforo del radar · Competidores enfocados · Ángulos libres |
| **D. Operativa y regulatorio** | **15%** | ¿Se puede operar sin fricción fatal? | Permitido · Post-venta simple · Proveedor · ANMAT |
| **E. Ecosistema (AOV/LTV)** | **15%** | ¿Marca o hit suelto? | Mecanismo único · Nicho aguanta marca · Recompra · Calidad |

**Por qué estos pesos:** Market Fit y unit economics se llevan el 55% porque son los
dos ejes que, fallados, no se arreglan con ejecución. Saturación pesa menos que
Market Fit porque un mercado caliente se puede atacar con ángulo propio — un mercado
que no existe, no.

## Pesos — EPROD

| Eje | Peso | Qué mide | MUSTs incluidos |
|---|---|---|---|
| **A. Demanda pagada** | **25%** | ¿Alguien paga hoy, con precio público? | E1, E2 |
| **B. Canal y CAC** | **20%** | ¿Se puede adquirir cliente por menos del ticket? | E5 |
| **C. Autoridad / ventaja injusta** | **20%** | ¿Por qué nosotros y no cualquiera? | E3, E4 |
| **D. Escalera de valor / LTV** | **20%** | ¿Hay algo arriba del producto de entrada? | E6 |
| **E. Entregabilidad** | **15%** | ¿Se produce y se sostiene sin comernos la vida? | E7 |

**Por qué cambian los pesos:** en eprod el margen bruto es ~90% y no discrimina entre
candidatos, así que no es eje. Lo que discrimina es el canal (B) y la autoridad (C):
son lo más difícil de conseguir y lo más difícil de copiar.

---

## Umbrales de veredicto

| Score | Veredicto | Qué hacer |
|---|---|---|
| **≥ 75** | 🟢 **GO claro** | Avanzar a Doc B |
| **60-74** | 🟡 **GO con flags** | Avanzar, pero resolver las flags antes de comprar stock / producir |
| **45-59** | 🟠 **Standby** | No descartar, pero no es el winner. Falta evidencia o falta ángulo. |
| **< 45** | 🔴 **NO-GO** | Descartar con el motivo escrito. Guardar pivots sugeridos. |

Un candidato con score alto pero un **MUST fallado** no es GO: es GO con flags, y la
flag es ese MUST. El score no compra MUSTs.

---

## Uso de la calculadora

```bash
python3 01-scorecard/calcular_score.py
```

Lee todos los `03-candidatos/*.json`, aplica gates y pesos, e imprime el ranking.

```bash
python3 01-scorecard/calcular_score.py --detalle nombre-del-candidato
```

Muestra el desglose eje por eje de un candidato.
