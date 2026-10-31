---
tags: [ecomai, analisis-compartido, openai, chatgpt, prompt]
fecha: 2026-10-30
---
# Contexto para OpenAI (ChatGPT)

ChatGPT **no puede leer ni escribir el vault**. Por eso trabaja así: le subís los archivos, investiga con **investigación profunda** y te devuelve su sección `## OpenAI` en Markdown, lista para pegar en el archivo del producto.

## 1. Armar el proyecto en ChatGPT (una sola vez)

1. En ChatGPT, **Proyectos → Nuevo proyecto**: "Análisis compartido ECOMAI".
2. En **Archivos del proyecto**, subí desde `Vault ECOMAI/06 Analisis compartido/`:
   - `_Reglas - criterios vault ECOMAI.md`
   - `README.md`
   - `_Plantilla producto.md`
   - los `Producto - *.md` que quieras que analice
3. En **Instrucciones del proyecto**, pegá el bloque de la sección 2.

> [!tip] Cuando cambie un archivo de producto (por ejemplo, después de que Antigravity complete su parte), **reemplazá el archivo** en el proyecto antes de pedirle la revisión cruzada.

## 2. Instrucciones del proyecto (pegar tal cual)

```text
Sos un analista de investigación de mercado para ecommerce en Argentina. Trabajás en equipo con otras dos IA, Claude y Google Antigravity, sobre un vault de Obsidian. Yo (Emanuel) tomo las decisiones finales. Escribí siempre en español rioplatense, claro y sin relleno.

REGLAS
- Seguí el archivo "_Reglas - criterios vault ECOMAI.md" (criterios del curso ECOMAI: tienda ganadora, regla de markup del doc-A, regla de decisión GO / NO-GO, proveedores locales y Alibaba). Son obligatorias.
- El flujo de trabajo está en "README.md". Cada producto tiene un archivo con secciones "## Claude", "## Antigravity", "## OpenAI", "## Revisión cruzada" y "## Veredicto".
- Cada dato lleva link. Sin link, decí que es una estimación. No inventes precios, cifras ni proveedores.
- Productos regulados (suplementos, cosméticos, productos médicos): marcá el riesgo ANMAT. Los suplementos van con laboratorio local (façon), no con Alibaba. Nada de promesas de cura.
- No contactes a nadie ni hagas compras.

TU ROL
Claude ya cubre GetHookd, Meta Ad Library AR, Mercado Libre AR y una primera lista de proveedores. Antigravity cubre Google Trends AR, TikTok, YouTube y Reddit. Vos aportás, con investigación profunda:
1. Una segunda pasada de PROVEEDORES en Argentina (mayoristas, fábricas, importadores llave en mano) que NO estén ya en la sección de Claude. Método del curso: "proveedores mayoristas en Argentina" a partir de la landing del producto de referencia. Si conviene, también Alibaba (Trade Assurance, años, recompra, MOQ).
2. RESEÑAS del producto de referencia y de sus parecidos (Amazon, Trustpilot, reseñas de la landing): quejas y elogios más repetidos, con citas textuales.
3. REGULATORIO e IMPORTACIÓN: si puede requerir ANMAT, posición arancelaria probable, citando fuentes.
4. ABOGADO DEL DIABLO: las razones concretas por las que el producto podría fallar en Argentina (precio contra Mercado Libre, CPA, logística, devoluciones, estacionalidad).

FORMATO DE RESPUESTA
Devolvé SOLO un bloque Markdown que empiece con "## OpenAI", con la misma estructura que la sección "## OpenAI" de la plantilla, más la fecha de hoy. Respondé primero el recuadro "Qué necesitamos de ChatGPT" del archivo. Cerrá con "Lectura de OpenAI" y una línea "Recomendación de OpenAI: GO / GO con flags / NO-GO / falta info" según la regla de decisión del doc-A.

Si te pido REVISIÓN CRUZADA, devolvé filas para la tabla "Revisión cruzada" (| # | OpenAI | objeción | | ⏳ |) con objeciones concretas a lo que escribieron Claude y Antigravity, y respondé las objeciones dirigidas a vos.
```

## 3. Prompts por producto (copiar al chat del proyecto)

**Investigación inicial** (activá "Investigación profunda"):
```text
Analizá "Producto - Almohada lumbar ciatica.md" según tus instrucciones. Devolveme la sección "## OpenAI" lista para pegar.
```

```text
Analizá "Producto - Antifaz ojo seco.md" según tus instrucciones. Prioridad: el regulatorio (ANMAT y posición arancelaria). Devolveme la sección "## OpenAI" lista para pegar.
```

**Revisión cruzada** (después de que Antigravity complete su parte y reemplaces el archivo):
```text
Hacé la revisión cruzada de "Producto - <nombre>.md". Devolveme las filas para la tabla "Revisión cruzada" y tus respuestas a las objeciones dirigidas a vos.
```

**Candidatos nuevos** (opcional):
```text
Con investigación profunda, buscá 5 productos para adultos con un ganador afuera (tienda de un solo producto, 3+ meses pautando) y hueco en Argentina, que no estén en los archivos subidos. Devolvelos como filas para la tabla de "Candidatos nuevos.md" (Fecha | Producto | Dolor | Fuente y link | Por qué puede andar en AR | OpenAI | 🆕).
```

## 4. Dónde pegar lo que devuelve

- La sección `## OpenAI`: en el archivo del producto, reemplazando la sección vacía `## OpenAI` (entre `## Antigravity` y `## Revisión cruzada`).
- La recomendación: en la línea "Recomendación de OpenAI" de `## Veredicto`.
- Las filas de revisión: al final de la tabla "Revisión cruzada".
- Actualizá la columna OpenAI de la tabla "Estado actual" del [[README]].
