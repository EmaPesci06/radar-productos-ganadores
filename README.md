# Radar de Productos Ganadores

Sistema de decisión para elegir **un** producto winner — físico o digital (eprod) — con
criterios explícitos, evidencia citable y un scorecard que se calcula, no se opina.

Mercado objetivo por defecto: **Argentina**.
Última actualización: **2026-10-31**.

---

## Para qué sirve este repo

Tres preguntas, en este orden:

1. **¿Qué es un producto ganador para nosotros?** → `00-marco/`
2. **¿Cómo lo medimos sin autoengañarnos?** → `01-scorecard/` y `02-costos/`
3. **¿Cuál elegimos?** → `03-candidatos/` (fichas) → `04-decision/decision-final.md`

El repo no reemplaza la investigación: la ordena y la hace comparable entre
candidatos. Un candidato sin evidencia no entra, y un candidato con evidencia
floja entra con score bajo.

---

## Índice

| Carpeta | Qué hay |
|---|---|
| `00-marco/01-producto-ganador-fisico.md` | Los criterios para productos físicos, destilados de nuestro propio sistema (Doc A + Radar AdLibrary) |
| `00-marco/02-producto-ganador-eprod.md` | Los criterios para productos digitales. Ejes distintos: el margen es ~90%, lo que mata es el CAC |
| `00-marco/03-lecciones-casos-previos.md` | Lo que ya nos pasó y no hay que repetir (incluye la primera importación real, sep-oct 2026) |
| `00-marco/04-evidencia-web-2026.md` | Lo que dice la web hoy, con links y nivel de confianza declarado |
| `01-scorecard/` | Matriz de decisión con pesos, gates de NO-GO y calculadora |
| `02-costos/` | Costo puesto en Argentina (físicos) y unit economics (eprods) |
| `03-candidatos/` | Una ficha por candidato + long-list inicial |
| `04-decision/decision-final.md` | El acta de decisión. Hoy: **PENDIENTE** |
| `templates/` | Doc A y Doc B en blanco, listos para llenar |

---

## Cómo se usa (flujo completo)

```
Idea
  │
  ├─ 1. Gate de exclusión          → 02-costos/reglas-y-exclusiones.md
  │     ¿Es importable/operable?     Si no pasa: muere acá, sin research.
  │
  ├─ 2. Pre-screening               → 03-candidatos/long-list-inicial.md
  │     Verde / amarillo / rojo      Sin búsquedas. Barato y rápido.
  │
  ├─ 3. Doc A (validación)          → skill `doc-a-validator` + templates/doc-a.md
  │     MUSTs y NICEs con evidencia  Salida: GO / GO con flags / NO-GO
  │
  ├─ 4. Radar de saturación         → skill `radar-adlibrary-ar`
  │     Semáforo verde/amarillo/rojo  Quién escala, foco, ángulos tomados
  │
  ├─ 5. Costo real                  → 02-costos/costo-puesto-ar.py
  │     Costo por unidad en AR        Si el markup no da, muere acá.
  │
  ├─ 6. Scorecard                   → 01-scorecard/calcular_score.py
  │     Score 0-100 comparable        Mismos ejes, mismos pesos, todos los candidatos
  │
  └─ 7. Decisión                    → 04-decision/decision-final.md
        Un winner, con razones        Y los descartados, con el motivo escrito
```

Los pasos 3 y 4 ya están automatizados en skills que tenés instaladas. Este repo
es la capa de arriba: dónde se guarda el resultado y cómo se compara entre ideas.

---

## Skills que alimentan este repo

Están sincronizadas en tu cuenta y son la fuente de los criterios de `00-marco/`:

| Skill | Rol en el flujo |
|---|---|
| `doc-a-validator` | Paso 3. Emite GO/NO-GO con MUSTs y NICEs |
| `radar-adlibrary-ar` | Paso 4. Saturación, foco de competidores, ángulos tomados |
| `importacion-alibaba-ar` | Paso 5. Costo puesto en Argentina, impuestos, flete |
| `doc-b-builder` | Post-decisión. VOCC, avatares, ángulos, pricing |

---

## Estado actual

- ✅ Marco de criterios (físicos y eprods)
- ✅ Scorecard con pesos y gates
- ✅ Calculadoras de costo y de score
- ✅ Long-list inicial de direcciones candidatas (derivada de web + nuestras restricciones)
- ⬜ **Fichas de candidatos reales** — faltan los datos de la carpeta `Ecommerce Curso`
- ⬜ **Decisión final** — bloqueada hasta tener al menos 3 candidatos con ficha completa

Ver `GAPS.md` para qué falta exactamente y cómo destrabarlo.
