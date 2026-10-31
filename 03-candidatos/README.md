# Candidatos

**16 candidatos cargados** (31/10/2026), tomados del ranking maestro del vault:
`Vault ECOMAI/05 Plan de accion/Comparativa integral AR y Planificacion - 31 octubre.md`.

```bash
python3 01-scorecard/calcular_score.py                              # ranking completo
python3 01-scorecard/calcular_score.py --tipo digital               # solo ebooks
python3 01-scorecard/calcular_score.py --detalle almohada-lumbar-ciatica
```

---

## Dónde vive cada cosa

| | |
|---|---|
| `<slug>.json` | Los 5 scores con su evidencia, gates, flags y pendientes. **Alimenta el scorecard** |
| El análisis completo | **En el vault**, no acá. Cada JSON apunta a su fuente en el campo `fuente_vault` |

No dupliqué el análisis del vault en archivos `.md` de esta carpeta: sería una copia
que se desactualiza. El vault es la fuente de verdad; estas fichas son el índice
puntuado y comparable.

Los archivos que empiezan con `_` son plantillas y el scorecard los ignora.

---

## Los 16

| Candidato | Tipo | Score | Veredicto |
|---|---|---|---|
| Almohada Lumbar Hueso (Ciática) + Bono Ebook | fisico-local | 95 | 🟢 EJECUTAR YA |
| Almohada de Embarazo (U/C) + Brazo Lactancia | fisico-local | 94 | 🟢 EJECUTAR YA |
| Ebook #1: Reto 28 Días Somáticos + Nervio Vago | digital | 93 | 🟢 EJECUTAR YA |
| Ebook #2: Chau Pañal en 3 Días + Kit Imprimible | digital | 92 | 🟢 EJECUTAR YA |
| Jabón / Gel de Caqui (Nonenal) Pack x3 | fisico-lab | 90 | 🟢 EJECUTAR YA |
| Loción / Spray de Magnesio Tópico Nocturno | fisico-lab | 89 | 🟢 EJECUTAR YA |
| Ebook #3: Control Pélvico Masculino 21 Días | digital | 88 | 🟢 EJECUTAR YA |
| Guantes de Compresión Artritis (Pack x2/x3) | fisico-courier | 84 | 🟡 SEGUNDA OLA |
| Kit Motoquero / Delivery | fisico-local | 84 | 🟡 SEGUNDA OLA |
| Kit Germinador de Brotes + 3 Semillas | fisico-local | 83 | 🟡 SEGUNDA OLA |
| Protector Bucal Bruxismo (Pack x2) | fisico-courier | 82 | 🟡 SEGUNDA OLA |
| Antifaz de Vapor Autocalentable | fisico-courier | 68 | 🔴 DESCARTADO (gate) |
| Dispositivo Antiatragantamiento | fisico-courier | — | 🔴 DESCARTADO (gate) |
| Esmalte en Marcador (Pack x5) | fisico-courier | — | 🔴 DESCARTADO (gate) |
| Manta Refrescante para Perros | fisico-courier | — | 🔴 DESCARTADO (gate) |
| Toalla Refrescante (Sofocos) | fisico-courier | — | 🔴 DESCARTADO (gate) |

Los 4 últimos los puntuó el vault **como grupo** (<60/100) sin desglose por eje. No les
inventé scores: van sin calificar, con el gate documentado. El gate manda igual.

### El patrón por tipo

| Tipo | Candidatos | Mejor | Promedio |
|---|---|---|---|
| `fisico-local` | 4 | 95 | **89,0** |
| `digital` | 3 | 93 | **91,0** |
| `fisico-lab` | 2 | 90 | **89,5** |
| `fisico-courier` | 7 | 84 | **33,4** |

**Importar por courier no es neutral: es sistemáticamente la peor ruta.** Tres peajes
estructurales — aduana, tope de 50 kg y el ancla de precio de Mercado Libre. Los 5
descartados son todos `fisico-courier`.

---

## Reglas para cargar un candidato nuevo

1. **Primero el gate, después el research.** Y antes del gate, preguntar **de dónde
   viene el producto**: la lista de exclusiones es de importar, no del producto. Un
   cosmético a façon local no pasa por ninguna.
2. **Un score sin evidencia va en 0-1**, no en 10 (regla 1 del Doc A). Con link.
3. **Un eje en 0-5 es bloqueante**, pase lo que pase con el total.
4. **El costo va calculado:** `02-costos/rentabilidad-ar.py` para el CPA breakeven,
   `02-costos/costo-puesto-ar.py` si se importa.
5. **Los precios en ARS llevan fecha.** Con la inflación un benchmark vence en semanas.
6. **Los descartados se guardan** con el motivo y el rescate posible. El antifaz murió
   como tienda pero vive como order bump.
