# Qué falta y cómo destrabarlo

---

## 1. 🔴 La carpeta `Ecommerce Curso` no se pudo leer — BLOQUEANTE

**Qué pedí:** acceso a la carpeta `Ecommerce Curso` de tu computadora, donde están los
productos ganadores anteriores (físicos y eprods) y el material del curso.

**Qué pasó:** esta sesión corre en un contenedor en la nube, no en tu máquina. Tu
computadora (`DESKTOP-HINTD1H`) tiene dos carpetas en la lista de Remote Control —
`Ecommerce Curso` y `labia` — y **ninguna de las dos está disponible para sesiones en
la nube**. La causa más probable es que esa computadora corre **Windows**: las carpetas
de Remote Control solo se ofrecen a sesiones en la nube desde Mac o Linux.

No es un permiso que puedas aprobar desde acá, y no hay forma de que yo lo destrabe.

### Tres formas de destrabarlo

| Opción | Cómo | Cuándo conviene |
|---|---|---|
| **A. Sesión local** (recomendada) | Abrí Claude Code en tu máquina — la app de escritorio, o `claude` en una terminal dentro de la carpeta `Ecommerce Curso`. Ahí el acceso a archivos es directo y nativo. | Es lo más cómodo si el material es mucho o son muchos archivos |
| **B. Subir el material acá** | Comprimí la carpeta (o la parte relevante) y adjuntala en el chat. Si son PDFs, docs o planillas, los leo igual | Si querés seguir en esta sesión y el material no es enorme |
| **C. Pegarme lo esencial** | Los productos ganadores con sus números: producto, nicho, ticket, costo, resultado | Si solo hace falta la lista de candidatos y no todo el curso |

**Si elegís A:** este repo ya está pusheado, así que cloná la branch
`claude/affectionate-dirac-h7n4cg` y seguís desde donde quedó. Todo el marco, el
scorecard y las calculadoras ya están ahí.

---

## 2. 🟡 El sistema del curso no cubre eprods

Las cuatro skills del curso están escritas **íntegramente para producto físico**.
No hay criterio de productos digitales codificado en ningún lado.

`00-marco/02-producto-ganador-eprod.md` lo cubre, pero es **nuevo y mío**: lo construí
trasladando la lógica del Doc A a lo digital y completando con evidencia web. Hay que
discutirlo antes de tomarlo como criterio del sistema, sobre todo:

- Los umbrales de CAC/ticket (30% / 50%) son razonables pero **no tienen benchmark
  argentino atrás**. Nadie publica CAC por nicho en AR.
- La tasa de reembolso de referencia (10-15%) es estimación de industria, no dato
  medido.
- Los pesos de los ejes (demanda 25%, canal 20%, autoridad 20%, escalera 20%,
  entregabilidad 15%) son un criterio propio, no heredado.

Si tenés data real de alguno de estos tres puntos en la carpeta del curso, cambia el
scorecard de eprods.

---

## 3. 🟡 Huecos de evidencia web

Lo que busqué y no encontré, para que no construyamos sobre humo:

| Hueco | Impacto | Cómo se cierra |
|---|---|---|
| Ranking confiable de categorías de infoproducto 2026 | No se puede priorizar nicho de eprod con data de mercado | Mirar el marketplace de Hotmart directo + Ad Library AR/ES |
| Ranking CACE por **facturación** (solo encontré unidades) | Las unidades sobre-representan alimentos; facturación serviría más para ticket alto | Buscar el informe completo de CACE |
| CAC por nicho en Argentina | El MUST E5 de eprods queda sin umbral de referencia | Solo se cierra testeando con plata propia |
| Reembolsos reales por categoría en Hotmart | El 10-15% es estimación | Preguntar en el programa, o data de la plataforma |

Casi todo el contenido de "producto ganador" en la web es de vendors que venden
herramientas de dropshipping. Los umbrales están marcados con nivel de confianza en
`00-marco/04-evidencia-web-2026.md` — el 🟥 no se usa para decidir.

---

## 4. 🟡 Cero candidatos cargados

Consecuencia directa del punto 1. El scorecard está probado y funcionando pero corre en
vacío: `python3 01-scorecard/calcular_score.py` hoy devuelve "no hay fichas cargadas".

`03-candidatos/long-list-inicial.md` tiene un pre-screening de **direcciones**, no de
candidatos. Es útil como punto de partida y como muestra de cómo se usa el sistema,
pero no sirve para decidir: ninguna dirección física llegó a verde porque le falta el
dolor específico atrás, y las dos verdes son eprods por falta de alternativas visibles,
no por mérito comparado.

---

## 5. 🟢 Lo que sí quedó listo y probado

| Entregable | Estado |
|---|---|
| Criterios de producto ganador físico (destilados del Doc A + Radar) | ✅ |
| Criterios de producto ganador eprod (nuevo, a discutir) | ✅ |
| Lecciones del caso real de importación, convertidas en criterio | ✅ |
| Evidencia web con nivel de confianza declarado y fuentes | ✅ |
| Scorecard con gates, pesos y umbrales | ✅ |
| Calculadora de score | ✅ probada |
| Calculadora de costo puesto en AR | ✅ **validada contra el caso real**: predice USD 3,63-4,20/unidad y el real fue 3,70 |
| Calculadora de unit economics de eprod | ✅ probada, con conversión por escalón |
| Plantillas de ficha, Doc A y Doc B | ✅ |
| Acta de decisión con método acordado de antemano | ✅ |
