# Qué falta y cómo destrabarlo

Actualizado **31/10/2026**, después de cargar el vault ECOMAI.

---

## ✅ Resuelto: el vault llegó

El bloqueante principal (no poder leer la carpeta `Ecommerce Curso`) se resolvió
pusheando el **Vault ECOMAI** al repo: 11 módulos, 334 archivos, 6 MB con la
transcripción completa del curso, los relevamientos de GetHookd y Radar AR, los
análisis de producto y el plan de 6 semanas.

De ahí salieron los 16 candidatos, el scorecard real y todos los criterios corregidos.

---

## 🟡 1. Lo que falta para cerrar la decisión

| # | Pendiente | Bloquea |
|---|---|---|
| 1 | **Cotizaciones de los 9 fabricantes de espuma** contactados el 30/10 | El eje de margen de la almohada lumbar y la de embarazo. Sin costo real, el CPA breakeven es estimado |
| 2 | **Llamar a los 5 laboratorios a façon** | El eje de operativa del jabón de caqui (hoy 15/20) y de la loción de magnesio (16/20). ✅ **La short list ya está hecha** (31/10): `05-relevamientos/2026-10-31-laboratorios-facon-y-anmat.md`. Hay labs AR que fabrican **desde 100 unidades**, no desde 2.000. Falta el llamado |
| 3 | **Doc A formal** de los 10 candidatos que no lo tienen | Hoy solo almohada lumbar y antifaz tienen archivo formal en `06 Analisis compartido/` |
| 4 | **La sección de OpenAI** de los dos productos con archivo | En el flujo de 3 IA del vault, ChatGPT todavía no aportó proveedores, reseñas del producto de referencia ni abogado del diablo |
| 5 | **Veredicto de Emanuel** | Las dos IA ya dejaron recomendación. La decisión es tuya |

---

## 🟡 2. Tensiones reales que conviene resolver, no esconder

### 2.1 El scorecard diría que lances 7 productos a la vez

Hay **7 candidatos en zona EJECUTAR YA (≥88)**. Lanzar 7 en paralelo contradice el
principio de foco del propio curso: las tiendas que ganan afuera son monoproducto con
foco 80-100%.

**No es un error del scorecard, es su límite:** prioriza, no secuencia. El plan de 6
semanas del vault ya resuelve la secuencia por ecosistema. Vale dejar escrito que **el
plan manda sobre el scorecard** para decidir qué va primero.

### 2.2 El test de los ebooks es de breakeven, no de rentabilidad

Corriendo `02-costos/rentabilidad-ar.py` sobre el ebook #1 ($19.900):

- CPA de breakeven: **$17.912**
- La regla de corte (5 ventas con USD 50) implica un CPA de **$15.600**
- Con CPA real de $15.000: neto **$2.912** por venta, **ROAS 1,33x**

El ROAS queda muy por debajo del **≥ 2,5** que el vault exige a los físicos. Llegar
justo a 5 ventas con USD 50 valida el ángulo pero **no prueba que el negocio dé plata**.

Para que el ebook sea negocio hace falta subir el ticket o bajar el CPA. El order bump
de $9.900 al 20% de take aporta solo $1.782 (10% más de CPA tolerable): diseñarlo para
30-40%, no para el piso del 20%.

### 2.3 La estacionalidad del ebook #2 se está yendo

"Chau pañal" tiene pico **octubre-febrero** (sacar el pañal con el calor, antes del
jardín en marzo). Hoy es 31 de octubre: la ventana está abierta pero se consume sola.
En el plan está en la Semana 3 (16-22 de noviembre). Si se corre, se pierde hasta el
año que viene.

---

## 🔴 3. Las herramientas del curso están bloqueadas en este entorno

Esto limita qué puedo investigar desde una sesión en la nube, y conviene saberlo antes
de pedirme un relevamiento.

| Herramienta | Estado | Qué se pierde |
|---|---|---|
| **Meta Ad Library** (`www.facebook.com`) | 🔴 El gateway responde **403 a CONNECT** | **El Radar AR entero**: quién pauta, días al aire, foco vs dispersión, ángulos tomados |
| **Mercado Libre AR** (`listado.mercadolibre.com.ar`) | 🔴 El host no resuelve | Demanda real: publicaciones, vendidos, ancla de precio |
| **Google Trends AR** (`trends.google.com`) | 🔴 El host no resuelve | Tendencia 5a/12m y estacionalidad |
| **GetHookd** | 🔴 Login pago + extensión en tu Chrome | La búsqueda de tiendas ganadoras afuera |
| **WebSearch** | 🟢 Funciona | — |

Probé también levantar la Ad Library con el Chromium y Playwright del contenedor: el
proxy la rechaza igual.

**Consecuencia:** desde esta sesión **no puedo buscar candidatos nuevos con el método
del curso**, porque el método es "buscar por el dolor en Ad Library → cruzar con demanda
en MELI → medir el hueco en Meta AR" y los tres pasos necesitan hosts bloqueados. Sí
puedo verificar supuestos regulatorios y encontrar proveedores con WebSearch, que es lo
que hice el 31/10.

### Cómo se destraba

Menú del entorno en la barra de título de la sesión → **Edit** → **Network access**: o
se sube el nivel de acceso, o se agregan estos dominios bajo **Allowed domains** dejando
tildada la casilla de package managers:

```
www.facebook.com
listado.mercadolibre.com.ar
www.mercadolibre.com.ar
trends.google.com
```

Pasos: https://code.claude.com/docs/en/cloud-environments#network-access

Ya está escrito y probado el script que corre el Radar AR en cuanto se habilite:
`05-relevamientos/scripts/radar-ar.js`. GetHookd no, porque necesita tu login.

---

## 🟡 4. Huecos de evidencia que siguen abiertos

| Hueco | Impacto | Cómo se cierra |
|---|---|---|
| **CPA real por nicho en Meta AR** | Todos los CPA objetivo ($15.000, $22.000, $32.000) son objetivos, no medidos | Solo se cierra testeando. Es la razón de la regla de los USD 50 |
| **Take rate real del order bump** | El 20% es el piso que pide el vault, no un dato propio | Primer ebook lanzado |
| **Tasa de reembolso de ebooks en ARS** | Afecta el flujo real, no el bruto | Primer ebook lanzado |
| Ranking de CACE por **facturación** (solo hay por unidades) | Las unidades sobre-representan alimentos | Informe completo de CACE |
| Si el laboratorio a façon acepta MOQ chico | Define si el nicho laboratorio es viable hoy o en 6 meses | 🟡 **Parcialmente cerrado:** Eneve declara desde 100 u. y Carmenta/Biosinergia 100-5.000, pero son declaraciones comerciales sin confirmar. Los 5 llamados del pendiente #2 |
| Si la categoría "Grado 1" de la Disp. 7939/2025 es la correcta | Etiqueta del trámite en todo el plan del Ecosistema 2 | No pude confirmarla: los resultados solo hablan de excluir domisanitarios grado 2b. Leer el texto completo de la disposición |

---

## 🟢 5. Lo que quedó listo y probado

| Entregable | Estado |
|---|---|
| Criterios de producto físico, con filtros de GetHookd, fórmula del hueco y patrón de 5 reglas | ✅ del vault |
| Criterios de ebook, del Módulo 8 | ✅ del vault |
| Lecciones del caso real de importación, convertidas en 13 criterios | ✅ |
| Scorecard de 5 ejes × 20, igual para físicos y ebooks | ✅ del vault |
| Calculadora de score con gates y ejes bloqueantes | ✅ probada sobre 16 candidatos |
| **Calculadora de rentabilidad AR** (CPA y ROAS de breakeven, bundles, order bump) | ✅ reproduce la lógica de bundles de M2-12 |
| Calculadora de costo puesto en AR | ✅ validada contra el caso real (predice USD 3,63-4,20; el real fue 3,70) |
| 16 fichas de candidatos con evidencia y links | ✅ |
| Acta de decisión con el método aplicado | ✅ |
| **Radar AR en Playwright**, con las reglas duras de la skill (nunca clickea el CTA del competidor) | ✅ escrito y probado. Espera que se habilite `www.facebook.com` |
| Short list de 5 laboratorios a façon con MOQ desde 100 u. + Disp. 7939/2025 en fuente primaria | ✅ 31/10 |

---

## 📝 6. Lo que corregí de mis propias versiones

Las primeras versiones de este repo las escribí sin acceso al curso. Tres cosas estaban
mal, y están documentadas en el archivo donde ocurrieron:

| Qué estaba mal | Consecuencia si no se corregía | Dónde |
|---|---|---|
| **Los pesos del scorecard eran míos** (30/25/15/15/15) y el vault ya tenía el suyo (5×20) | Dos scorecards incompatibles: físicos y ebooks no podrían competir en un solo ranking, que es justo lo que hace falta para decidir | `01-scorecard/README.md` |
| **El criterio de eprods pedía "autoridad propia"** (mi MUST E3) | Es **lo contrario** de M8-03, que pide ofertas **sin marca personal** porque una marca personal no se puede modelar. Con mi criterio los 3 ebooks del ranking fallaban un MUST | `00-marco/02-producto-ganador-eprod.md` |
| **Traté la lista de exclusiones como gate de producto** | Es gate de **importar**. El jabón de caqui (90/100) y la loción de magnesio (89/100) habrían muerto en el primer filtro, cuando en realidad se fabrican a façon acá y no pasan por ANMAT ni aduana | `02-costos/reglas-y-exclusiones.md` |

También quedó obsoleto `03-candidatos/long-list-inicial.md`: era un pre-screening de
*direcciones* hecho sin los candidatos reales, y su conclusión ("las dos direcciones
verdes son eprods") era un artefacto de no tener físicos cargados. Se mantiene solo
como registro de cómo se veía el problema antes del vault.
