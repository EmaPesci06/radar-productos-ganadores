# Documento A — Validación de Producto/Mercado

> Formulario en blanco. Lo normal es que lo llene la skill `doc-a-validator`
> (una sesión por producto, no todos juntos). Esto sirve para llenarlo a mano o
> para revisar la salida.
>
> **Regla madre:** evidencia real, no opinión. Sin evidencia → score 0-1 y se
> declara "sin evidencia suficiente".

| | |
|---|---|
| Producto | |
| Nicho | |
| Mercado | Argentina |
| Fecha | |
| Contexto | marca nueva / pivot / producto para ecosistema existente |

---

## Checklist global

| # | Pregunta | Tipo | Score | Evidencia |
|---|---|---|---|---|
| 1 | ¿Mecanismo único y alto valor percibido? | MUST | /5 | |
| 2 | ¿Varios productos coherentes alrededor del mismo problema/cliente? | NICE | /5 | |
| 3 | ¿Plan claro para subir AOV? | NICE | /5 | |
| 4 | ¿Plan claro para subir LTV? | NICE | /5 | |
| 5 | ¿Aceptaría breakeven en front-end por confianza en back-end? | NICE | /5 | |
| 6 | ¿Calidad + experiencia soportan largo plazo? | MUST | /5 | |
| 7 | ¿Marca pensada para años, no un hit? | MUST | /5 | |

**2 o más MUSTs fallados → NO-GO automático.**

---

## Bloque 1 — Market Fit

| Ítem | Tipo | Score | Fuente + link | Insight |
|---|---|---|---|---|
| 1.1 Marcas afuera invirtiendo fuerte | MUST | /5 | Ad Library US/UK/AU/ES | |
| 1.2 Gente pagando buen ticket | MUST | /5 | MELI, Amazon, DTC | |
| 1.3 Mismo dolor y nicho en Argentina | MUST | /5 | MELI AR, Google AR, Reddit, TikTok | |
| 1.4 Precio necesario es lógico localmente | MUST | /5 | costo × markup vs MELI AR | |
| 1.5 Competencia local deja espacio | NICE | /5 | top 5 competidores AR | |
| 1.6 Problema evergreen, no moda de 30 días | MUST | /5 | Google Trends AR 5 años | |
| 1.7 Señales emocionales ("soy yo / me pasa igual") | NICE | /5 | comentarios, reviews, TikTok | |
| 1.8 Historias de transformación | NICE | /5 | reviews 5★, testimonios | |
| 1.9 Consumidores ya gastando en alternativas | NICE | /5 | volumen MELI/Amazon | |

**Score MUSTs:** /5 — **Score NICEs:** /5 — **MUSTs fallados:**
**Conclusión:**

---

## Bloque 2 — Operaciones, costos y márgenes

### 2.1 Operativa

| Ítem | Tipo | Score | Evidencia |
|---|---|---|---|
| Chico/mediano, no pesado, no frágil | MUST | /5 | dimensiones y peso de similares |
| Pocas variantes (1-3 SKUs) | NICE | /5 | |
| No requiere instalación compleja / mucho soporte | NICE | /5 | reviews competencia |

### 2.2 Envíos y post-venta

| Ítem | Tipo | Score | Evidencia |
|---|---|---|---|
| Entra en packaging estándar | NICE | /5 | |
| No se deforma ni rompe | NICE | /5 | reviews: quejas de roturas |
| Post-venta simple, uso intuitivo | MUST | /5 | reviews: gente perdida |

### 2.3 Proveedor

| Ítem | Tipo | Score | Estado |
|---|---|---|---|
| Puede abastecer volumen | MUST | /5 | investigado / **PENDIENTE** |
| Tiempos claros y realistas | MUST | /5 | |
| Calidad constante | MUST | /5 | |
| Condiciones mejoran con volumen | NICE | /5 | |
| Plan B (2do proveedor) | NICE | /5 | |

> Si todavía no se investigó: marcar **PENDIENTE — validar antes de comprar stock**
> y no penalizar el score global. La advertencia queda escrita.

### 2.4 Margen real

Correr `02-costos/costo-puesto-ar.py` y pegar la salida:

```
```

| | |
|---|---|
| Costo puesto en AR | ARS |
| Markup mínimo (tabla) | × |
| Precio piso | ARS |
| Precio de mercado hoy en MELI AR *(fecha: )* | ARS |
| ¿Coherente? | sí / flag amarilla / NO-GO |

---

## Bloque 3 — Ecosistema de marca

| Ítem | Tipo | Score | Evidencia |
|---|---|---|---|
| "Por qué funciona" claro y diferente | MUST | /5 | |
| La comunicación justifica precio mayor | NICE | /5 | competidores premium |
| Promete transformación visible o sentida | MUST | /5 | |
| Beneficios premium (tiempo, comodidad, estatus, salud, performance) | NICE | /5 | |
| Héroe tiene recompra (consumible o accesorios) | NICE | /5 | |
| Siguientes pasos lógicos post-compra | NICE | /5 | |
| Packs/bundles que suben AOV sin complicar operativa | NICE | /5 | |
| Upsells/cross-sells coherentes | NICE | /5 | |
| El nicho/dolor aguanta una marca, no un SKU | MUST | /5 | |
| Naming/branding no limitan a un SKU | NICE | /5 | |
| Mensaje central extensible | NICE | /5 | |
| Calidad soporta recompras y recomendaciones | MUST | /5 | reviews: quejas recurrentes |
| Experiencia completa pensada (packaging, envío, soporte) | NICE | /5 | |

**Mecanismo único:** definido / por definir
**Productos del ecosistema (3-5):**

---

## Decisión final

| | |
|---|---|
| Checklist global | PASA / NO PASA |
| Bloque 1 Market Fit | PASA / NO PASA / FLAG |
| Bloque 2 Operaciones | PASA / NO PASA / FLAG |
| Bloque 3 Ecosistema | PASA / NO PASA / FLAG |
| **DECISIÓN** | **GO / GO con flags / NO-GO** |

**3 razones principales:**
1.
2.
3.

**Evidencia recopilada (todos los links revisados):**
-

**Si es NO-GO — pivots sugeridos:**
1.
2.
3.

**Si es GO con flags — resolver antes de avanzar:**
-

**Si es GO:** siguiente paso es el Doc B (`doc-b-builder`). Guardar este archivo como
`doc-a-<producto>.md` para que la skill lo lea directo.
