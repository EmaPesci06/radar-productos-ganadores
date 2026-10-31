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
| `00-marco/02-producto-ganador-eprod.md` | Los criterios para ebooks e infoproductos, del Módulo 8 del curso |
| `00-marco/03-lecciones-casos-previos.md` | Lo que ya nos pasó y no hay que repetir (incluye la primera importación real, sep-oct 2026) |
| `00-marco/04-evidencia-web-2026.md` | Lo que dice la web hoy, con links y nivel de confianza declarado |
| `01-scorecard/` | Matriz de decisión con pesos, gates de NO-GO y calculadora |
| `02-costos/` | **`rentabilidad-ar.py`** (CPA y ROAS de breakeven, el número que manda), costo puesto en AR, y reglas de importación |
| `03-candidatos/` | Una ficha por candidato + long-list inicial |
| `04-decision/decision-final.md` | El acta de decisión. Hoy: **desbloqueada, 16 candidatos cargados** |
| `05-relevamientos/` | Investigación hecha desde el repo, fechada. Incluye `scripts/radar-ar.js`, el Radar AR en Playwright |
| `Vault ECOMAI/` | El vault de Obsidian con la transcripción completa del curso (11 módulos, 334 archivos). **Es la fuente de verdad** de todos los criterios |
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

## Estado actual (31/10/2026)

- ✅ Marco de criterios, corregido contra el vault ECOMAI
- ✅ Scorecard del vault: 5 ejes × 20 puntos, iguales para físicos y ebooks
- ✅ Calculadoras: score, rentabilidad en AR (CPA/ROAS breakeven), costo puesto en AR
- ✅ **16 candidatos cargados** (12 puntuados + 4 descartados con el motivo escrito)
- 🟡 **Decisión: desbloqueada.** El sistema recomienda; la decisión es de Emanuel

### El ranking, en una línea

**Almohada Lumbar Hueso (95/100)** como winner físico y **Ebook #1 Somáticos (93/100)**
como winner digital — no compiten, se testean en paralelo con presupuestos distintos.
Ver `04-decision/decision-final.md`.

```bash
python3 01-scorecard/calcular_score.py
```

### Lo que corregí al cargar el vault

Las primeras versiones de este repo las escribí sin acceso al material del curso, y
tres cosas estaban mal. Están documentadas en el archivo donde ocurrieron:

| Qué | Dónde |
|---|---|
| Los pesos del scorecard eran míos; el vault ya tenía el suyo (5 ejes × 20) | `01-scorecard/README.md` |
| El criterio de eprods pedía "autoridad propia"; el curso pide **lo contrario** (ofertas sin marca personal) | `00-marco/02-producto-ganador-eprod.md` |
| Traté la lista de exclusiones como gate de producto; es gate de **importar** | `02-costos/reglas-y-exclusiones.md` |

Ver `GAPS.md` para lo que todavía falta.
