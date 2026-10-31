# Candidatos

Una ficha por candidato. Dos archivos por candidato:

| Archivo | Para qué |
|---|---|
| `<slug>.json` | Alimenta el scorecard. Scores, gates, flags. |
| `<slug>.md` | El razonamiento y la evidencia completa. |

Los archivos que empiezan con `_` son plantillas y el scorecard los ignora.

```bash
cp 03-candidatos/_plantilla-candidato.json 03-candidatos/mi-producto.json
cp 03-candidatos/_plantilla-candidato.md   03-candidatos/mi-producto.md
# llenar, y después:
python3 01-scorecard/calcular_score.py
```

---

## Estado

**No hay candidatos reales cargados.** Los productos ganadores anteriores (físicos y
eprods) están en la carpeta `Ecommerce Curso`, que no se pudo leer desde esta sesión.
Ver `GAPS.md`.

Lo que sí hay: `long-list-inicial.md`, un pre-screening de **direcciones** candidatas
derivado de nuestras restricciones operativas + la evidencia web. Es el paso 2 del
flujo (Fase 1 del Doc A), no reemplaza las fichas.

---

## Reglas para cargar un candidato

1. **Un score sin evidencia va en 0**, no en 2. "Me parece que sí" no es evidencia.
   La plantilla pide link en cada eje porque sin link el score no vale.

2. **Primero el gate, después el research.** Antes de abrir Ad Library, chequear
   `02-costos/reglas-y-exclusiones.md`. Un producto con pilas no merece una tarde.

3. **El costo va calculado, no estimado.** Correr `02-costos/costo-puesto-ar.py`
   y pegar la salida en el `.md`. El precio de Alibaba no es el costo: en el caso real
   el multiplicador fue ×3,1.

4. **Los precios en ARS llevan fecha.** Con la inflación, un benchmark de precio vence
   en semanas. Sin fecha, el dato no sirve en dos meses.

5. **Mínimo 3 candidatos antes de decidir.** Un winner sin comparación no está
   elegido, está aceptado por falta de alternativas. El scorecard avisa cuando hay
   menos de dos sobre el piso.

6. **Los descartados se guardan.** Un NO-GO con el motivo escrito y los pivots
   sugeridos vale tanto como un GO: evita volver a evaluar lo mismo en tres meses.
