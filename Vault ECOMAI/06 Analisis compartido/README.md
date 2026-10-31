---
tags: [ecomai, analisis-compartido, antigravity, claude]
fecha: 2026-10-30
---
# 06 Análisis compartido (Claude + Antigravity + OpenAI)

Carpeta para que **Claude**, **Google Antigravity (Gemini)** y **OpenAI (ChatGPT)** investiguen los mismos productos en paralelo, se crucen objeciones y **Emanuel decida**. Las reglas de investigación son las del curso: [[_Reglas - criterios vault ECOMAI]] (copia de los criterios del vault, Módulo 2 y doc-a-validator). Las tres IA siguen las mismas reglas.

## Qué hay acá

| Archivo | Para qué |
|---|---|
| `README.md` | Este flujo |
| `_Reglas - criterios vault ECOMAI.md` | Las reglas que siguen las dos IA. **Leerlo antes de escribir** |
| `_Plantilla producto.md` | Copiar para cada producto nuevo |
| `Candidatos nuevos.md` | Bandeja de entrada: cualquiera de los dos suma ideas acá |
| `_Prompt para Antigravity.md` | El prompt para pegar en Antigravity |
| `_Contexto para OpenAI.md` | Cómo armar el proyecto en ChatGPT, sus instrucciones y el prompt por producto |
| `Producto - *.md` | Un archivo por producto, con secciones **Claude**, **Antigravity**, **OpenAI** y **Veredicto** |

## Quién busca qué

| | Claude | Antigravity | OpenAI (ChatGPT) |
|---|---|---|---|
| **Fuentes** | GetHookd (vía Chrome de Emanuel), Meta Ad Library AR (Radar AR), Mercado Libre AR, proveedores locales y Alibaba | Google (búsqueda y **Google Trends AR**, 5 años y 12 meses), **TikTok** (tendencias, Creative Center, hashtags, comentarios), YouTube, Reddit, foros AR | **Investigación profunda** (deep research): proveedores mayoristas en AR (método M2-05), reseñas de Amazon y Trustpilot, regulatorio ANMAT y aduana |
| **Aporta** | Ganador afuera, competencia en Meta AR, demanda en MELI, costos y markup | Si el **dolor existe en Argentina**, si la tendencia sube o baja, cómo habla la gente del problema (VOCC), ángulos y formatos de creativo que funcionan en TikTok | Una segunda pasada de proveedores, las quejas del producto de referencia y el **abogado del diablo** |
| **Escribe en** | `## Claude` | `## Antigravity` | `## OpenAI` (ChatGPT no accede al vault: **devuelve la sección y Emanuel la pega**) |

Ninguna borra ni reescribe la sección de otra.

## El flujo, paso a paso

1. **Entrada.** Un producto nuevo entra en [[Candidatos nuevos]] con su fuente y una línea de por qué. Cualquiera de los dos puede sumar.
2. **Archivo.** Cuando Emanuel (o la IA que lo propuso) lo pasa a investigar, se copia [[_Plantilla producto]] como `Producto - <nombre corto>.md` y se marca el estado en la tabla de candidatos.
3. **Investigación en paralelo.** Cada IA (las tres) completa **su** sección con evidencia y links. Sin link, el dato cuenta como 0-1 (regla 1 del doc-A).
4. **Revisión cruzada.** Cada IA lee las secciones de las otras y escribe sus **objeciones** en la tabla "Revisión cruzada": qué dato no le cierra, qué falta, qué contradice lo que encontró. La aludida responde en la misma tabla. Para ChatGPT, Emanuel le pega el archivo actualizado y le pide que objete y responda.
5. **Veredicto.** Emanuel lee las tres secciones y las objeciones, y completa `## Veredicto` (GO, GO con flags, NO-GO o "falta info"). Las IA pueden dejar una **recomendación**, pero la decisión es de Emanuel.
6. **Si es GO**, el producto sigue al plan de acción: proveedores y lanzamiento en `05 Plan de accion/`, después doc-b-builder.

## Reglas de convivencia

- **Fechar todo** (dd/mm/aaaa) y poner **link** a cada dato. Si un dato es una estimación, decirlo.
- Escribir en **español rioplatense**, claro y sin relleno. Tablas cuando sirvan.
- No tocar la sección de la otra IA. Las correcciones van como objeción.
- No mover ni renombrar archivos de otras carpetas del vault. Para referirse a ellos, usar `[[links]]`.
- Productos regulados (suplementos, cosméticos, productos médicos): marcar el **riesgo ANMAT** siempre. Los suplementos van con laboratorio local (façon), no con Alibaba.
- Ética: no prometer curas. Los ángulos se escriben como experiencia, no como tratamiento.

## Estado actual (31/10/2026)

| Producto / Relevamiento | Claude | Antigravity | OpenAI | Veredicto |
|---|---|---|---|---|
| [[Producto - Almohada lumbar ciatica]] | ✅ prellenado (proveedores contactados el 30/10) | ✅ completado (30/10): GO con flags (3 objeciones) | ⏳ pendiente | ⏳ |
| [[Producto - Antifaz ojo seco]] | ✅ prellenado + [[Antifaz - competencia y rentabilidad]] + [[Kit de descanso - proveedores]] | ✅ completado (30/10 y 31/10): NO-GO héroe / GO bump sin aroma | ⏳ pendiente | ⏳ |
| [[Candidatos nuevos]] + [[Comparativa integral AR y Planificacion - 31 octubre]] | ✅ 6 candidatos de X + 3 Ebooks + Radar AR (31/10) | ✅ 3 candidatos nuevos sumados + Comparativa AR completa y Plan de 6 semanas (31/10) | ⏳ pendiente | ⏳ |
