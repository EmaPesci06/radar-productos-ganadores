# Cómo trabajar en este repo

Repo de decisión de producto, no de código. Español rioplatense.

## Estructura

| Carpeta | Regla |
|---|---|
| `00-marco/` | Los criterios. **No se cambian sin discutirlo** — son la base de todas las decisiones. Si un criterio cambia, los scores anteriores dejan de ser comparables. |
| `01-scorecard/` | Pesos y gates. Mismo criterio: cambiar un peso invalida la comparación entre candidatos ya evaluados. Si se cambia, recalcular todo. |
| `02-costos/` | Calculadoras. La de `costo-puesto-ar.py` está **validada contra un caso real** (`--caso-real`). Si se la modifica, correr ese flag y verificar que siga prediciendo USD 3,63-4,20 por unidad (el real fue 3,70). |
| `03-candidatos/` | Una ficha JSON + una MD por candidato. Los `_*` son plantillas y el scorecard los ignora. |
| `04-decision/` | El acta. El método de decisión se escribe **antes** de ver los números. |
| `templates/` | Doc A y Doc B en blanco. |

## Reglas de contenido

1. **Evidencia o nada.** Todo dato lleva link. Un score sin evidencia va en 0, no en 2.
   Si una fuente es un vendor con interés comercial, se marca 🟥 y no se usa para
   decidir.
2. **Los precios en ARS llevan fecha.** Con la inflación un benchmark vence en semanas.
3. **El costo es el costo puesto en Argentina**, nunca el de Alibaba. Correr la
   calculadora, no estimar.
4. **No inventar candidatos ni números.** Si falta un dato, se marca PENDIENTE. Un
   placeholder con pinta de dato real es peor que un hueco declarado.
5. **Distinguir lo heredado de lo nuevo.** Los criterios de físicos vienen de las
   skills del curso. Los de eprods los escribí yo y están marcados como v1 a discutir.
   No mezclar las dos autoridades.

## Skills que alimentan el repo

Están sincronizadas en la cuenta, no en el repo:

- `doc-a-validator` — validación GO/NO-GO (una sesión por producto)
- `radar-adlibrary-ar` — saturación y competencia en Meta Ad Library AR
- `importacion-alibaba-ar` — costo puesto en AR, impuestos, proveedor
- `doc-b-builder` — VOCC, avatares, ángulos, pricing (post-decisión)

Las cuatro son de **producto físico**. Para eprods, el criterio está solo en
`00-marco/02-producto-ganador-eprod.md`.

## Antes de dar una decisión por cerrada

- [ ] ¿Hay al menos 3 candidatos con ficha completa?
- [ ] ¿Cada score tiene evidencia con link?
- [ ] ¿El costo salió de la calculadora, no de una estimación?
- [ ] ¿Se corrió el scorecard sobre todos con el mismo criterio?
- [ ] ¿Los descartados quedaron con el motivo escrito?
- [ ] ¿El método de decisión estaba escrito antes de ver los scores?
