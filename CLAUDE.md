# Cómo trabajar en este repo

Repo de decisión de producto, no de código. Español rioplatense.

## Estructura

| Carpeta | Regla |
|---|---|
| **`Vault ECOMAI/`** | **La fuente de verdad.** 11 módulos, 334 archivos con la transcripción del curso, los relevamientos y el plan. Si un criterio del repo contradice al vault, **gana el vault**. No editar ni reorganizar el vault desde acá. |
| `00-marco/` | Los criterios, destilados del vault. **No se cambian sin discutirlo.** Si un criterio cambia, los scores anteriores dejan de ser comparables. |
| `01-scorecard/` | Los 5 ejes × 20 del vault, más los gates. Cambiar un peso invalida la comparación entre los 16 candidatos ya cargados: si se cambia, recalcular todo. |
| `02-costos/` | Calculadoras. `rentabilidad-ar.py` es la que manda para decidir (CPA y ROAS de breakeven). `costo-puesto-ar.py` está **validada contra un caso real** (`--caso-real`): si se la modifica, correr ese flag y verificar que siga prediciendo USD 3,63-4,20 por unidad (el real fue 3,70). |
| `03-candidatos/` | Una ficha JSON por candidato. El análisis completo vive **en el vault**, no acá: cada JSON apunta a su fuente en `fuente_vault`. Los `_*` son plantillas y el scorecard los ignora. |
| `04-decision/` | El acta. El método de decisión se escribe **antes** de ver los números. |
| `templates/` | Doc A y Doc B en blanco. |

## Reglas de contenido

1. **Evidencia o nada.** Todo dato lleva link. Un score sin evidencia va en 0, no en 2.
   Si una fuente es un vendor con interés comercial, se marca 🟥 y no se usa para
   decidir.
2. **Los precios en ARS llevan fecha.** Con la inflación un benchmark vence en semanas.
3. **El costo es el costo puesto en Argentina**, nunca el de Alibaba. Correr la
   calculadora, no estimar.

   Y ojo con cuál: `costo-puesto-ar.py` es para **importar**;
   `estimar-costo-fabricacion.py` es para **fabricar acá**. No son intercambiables.

4. **La tabla de markup del Doc A es para importación, no para fabricación local.**
   Los 4 productos de descanso la fallan (×1,5 a ×2,8 contra ×3 a ×5), porque fabricando
   acá el costo base es 3-4 veces más alto y ×5 da precios 2-3 veces por encima del ancla
   de MELI. Para fabricación local el filtro es el **CPA de breakeven**, como dice M2-12.
   Ver `05-relevamientos/2026-10-31-costos-estimados-fisicos.md`.
5. **No inventar candidatos ni números.** Si falta un dato, se marca PENDIENTE. Un
   placeholder con pinta de dato real es peor que un hueco declarado.
6. **Distinguir lo heredado de lo nuevo.** Todo lo que viene del vault es criterio del
   curso y manda. Lo que agregué yo va marcado como mío, con la fecha. Las tres
   correcciones del 31/10 están documentadas en el archivo donde ocurrió el error, no
   borradas: sirve saber qué estaba mal y por qué.

7. **Un eje en 0-5 es bloqueante**, pase lo que pase con el total. El dispositivo
   antiatragantamiento tenía dolor y hueco publicitario, y murió por ANMAT Clase II.

8. **Antes de aplicar la lista de exclusiones, preguntar de dónde viene el producto.**
   La lista es de **importar**. Fabricación local y laboratorio a façon no pasan por
   ninguna de esas trabas.

## Skills que alimentan el repo

Están sincronizadas en la cuenta, no en el repo:

- `doc-a-validator` — validación GO/NO-GO (una sesión por producto)
- `radar-adlibrary-ar` — saturación y competencia en Meta Ad Library AR
- `importacion-alibaba-ar` — costo puesto en AR, impuestos, proveedor
- `doc-b-builder` — VOCC, avatares, ángulos, pricing (post-decisión)

Las cuatro son de **producto físico**. El criterio de ebooks está en el Módulo 8 del
vault, destilado en `00-marco/02-producto-ganador-eprod.md`.

El vault también documenta un **flujo de 3 IA en paralelo** (`06 Analisis compartido/`):
Claude toma GetHookd + Meta Ad Library AR + MELI + proveedores; Antigravity toma Google
Trends + TikTok + Reddit + VOCC; ChatGPT toma deep research de proveedores, reseñas y
abogado del diablo. **Ninguna borra ni reescribe la sección de otra** — las correcciones
van como objeción en la tabla de revisión cruzada. Emanuel decide.

## Antes de dar una decisión por cerrada

- [ ] ¿El criterio que estoy usando sale del vault, o es mío? ¿Está marcado?
- [ ] ¿Hay al menos 3 candidatos con ficha completa?
- [ ] ¿Cada score tiene evidencia con link?
- [ ] ¿El costo salió de la calculadora, no de una estimación?
- [ ] ¿Se corrió el scorecard sobre todos con el mismo criterio?
- [ ] ¿Los descartados quedaron con el motivo escrito?
- [ ] ¿El método de decisión estaba escrito antes de ver los scores?
