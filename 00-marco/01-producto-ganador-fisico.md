# Qué es un producto ganador — FÍSICO

Destilado de nuestro propio sistema: el checklist del Documento A y el radar de
Meta Ad Library. No es teoría de internet: son los criterios con los que ya
estamos evaluando.

> **Regla madre:** se califica con **evidencia real, no con opinión**. Cada punto
> necesita un link que se pueda abrir. Sin evidencia → score 0-1 y se declara
> "sin evidencia suficiente". Mejor un NO-GO conservador que un GO inflado.

---

## 1. Los 7 MUSTs/NICEs de entrada (checklist global)

Si fallan **2 o más MUSTs** de esta tabla → NO-GO automático, sin research.

| # | Pregunta | Tipo |
|---|---|---|
| 1 | ¿Tiene mecanismo único y alto valor percibido? | **MUST** |
| 2 | ¿Puedo construir varios productos coherentes alrededor del mismo problema/cliente? | NICE |
| 3 | ¿Existe plan claro para subir AOV? (bundles, upsells, OTOs) | NICE |
| 4 | ¿Existe plan claro para subir LTV? (recompra, accesorios, email/SMS) | NICE |
| 5 | ¿Aceptaría ir breakeven en front-end confiando en el back-end? | NICE |
| 6 | ¿Calidad + experiencia soportan estrategia de largo plazo? | **MUST** |
| 7 | ¿La marca está pensada para años (ecosistema), no un solo hit? | **MUST** |

El punto 7 es el que más se saltea y el que más duele: un producto que no puede
sostener una marca es un hit, y un hit se apaga cuando se apaga el ángulo.

---

## 2. Bloque Market Fit — ¿el problema es real y se paga?

Los **MUSTs** de este bloque (score 0-5 cada uno, falla si < 3):

| Ítem | Dónde se verifica |
|---|---|
| Hay marcas afuera invirtiendo fuerte (muchos ads, meses corriendo) | Meta Ad Library US/UK/AU/ES |
| Hay gente pagando buen ticket por la solución | Mercado Libre, Amazon, tiendas DTC |
| **Existe el mismo dolor y nicho en Argentina** | MELI AR, Google AR, Reddit AR/LATAM, TikTok AR |
| El precio que necesitamos cobrar es lógico para el mercado local | Costo × markup vs precio promedio MELI AR |
| El problema es **evergreen**, no moda de 30 días | Google Trends AR, 5 años |

NICEs: espacio competitivo local, señales emocionales ("soy yo / me pasa igual"),
historias de transformación, consumidores ya gastando en alternativas.

**El MUST que más candidatos mata:** el dolor existe afuera pero no acá, o existe
acá pero a un ticket que no soporta el markup que necesitamos.

---

## 3. Bloque Operaciones — ¿escala en la vida real o solo en Excel?

### 3.1 El producto

- Chico/mediano, no pesado, no muy frágil → **MUST**
- Pocas variantes (1-3 SKUs) → NICE
- Post-venta simple, uso intuitivo → **MUST** (se verifica en reviews de competencia:
  si la gente se queja de "no entendí cómo usarlo", el soporte te come el margen)

### 3.2 La tabla de markup mínimo

Es la regla dura. Si el precio sugerido queda lejos de lo que se vende en MELI AR,
flag amarilla; si queda **muy** lejos, NO-GO.

| Costo del producto (puesto en AR) | Markup mínimo | Precio sugerido |
|---|---|---|
| $2.000 – $5.000 | ×10 | $20.000 – $50.000 |
| $5.000 – $10.000 | ×7 | $35.000 – $70.000 |
| $10.000 – $20.000 | ×5 | $50.000 – $100.000 |
| $20.000 – $35.000 | ×4 | $80.000 – $140.000 |
| $35.000 – $50.000 | ×3 | $105.000 – $150.000 |

> ⚠️ El costo que entra en esta tabla es el **costo puesto en Argentina**, no el
> precio de Alibaba. En productos baratos por courier el multiplicador real fue
> **×3,1** (ver `00-marco/03-lecciones-casos-previos.md`). Usar
> `02-costos/costo-puesto-ar.py` antes de aplicar la tabla.

### 3.3 Proveedor

MUSTs: puede abastecer volumen, tiempos claros, calidad constante.
Si todavía no se investigó (lo normal en esta etapa), marcar **PENDIENTE — validar
antes de comprar stock** y no penalizar el score. Pero la advertencia queda escrita.

---

## 4. Bloque Ecosistema — ¿marca o producto suelto?

MUSTs:

- **Mecanismo único definido:** un "por qué funciona" claro y distinto. Si no se
  puede explicar en una frase, no existe.
- **Promete transformación visible o sentida**, no un accesorio.
- **El nicho/dolor aguanta una marca**, no un solo SKU.
- **La calidad soporta recompras y recomendaciones** (se verifica en reviews de
  productos similares: quejas recurrentes de calidad = flag).

NICEs: recompra o accesorios, 3-5 productos lógicos del ecosistema, bundles que
suben AOV sin complicar la operativa, upsells alineados a la misma promesa,
mensaje central extensible.

**Front-end vs back-end:** el héroe es la puerta de entrada, no donde se maximiza
margen. Objetivo sano: no perder plata en la primera compra y multiplicar con el
back-end. No obsesionarse con CPA bajo — mirar AOV + LTV.

---

## 5. Saturación — el semáforo del radar

Un producto puede pasar todo lo anterior y seguir siendo mala idea si el mercado AR
ya está peleado. Umbrales guía (no dogma: si un eje contradice a los otros, se dice
en vez de promediar a ciegas):

| Eje | 🟢 Verde | 🟡 Amarillo | 🔴 Rojo |
|---|---|---|---|
| Marcas DTC distintas con el mismo dolor en AR | 0-2 | 3-5 | 6+ |
| Anuncios activos de la marca líder | <50 | 50-200 | >200 |
| Marcas que arrancaron ads en los últimos 15 días | 0-1 | 2-3 | 4+ |
| Solapamiento de ángulos entre marcas | ninguno | 1 compartido | 2+ compartidos |
| Demanda MELI vs inversión publicitaria | vendidos altos, pocas marcas | parejo | muchas marcas, pocos vendidos |
| Competidores **enfocados** (foco ≥70% en este producto) | 0-1 | 2 | 3+ |

Lectura:

- 🟢 **Abierto** — demanda con poca inversión peleando. Entrada limpia.
- 🟡 **Caliente** — validado y con competencia real. Se entra con ángulo propio, no clonando al líder.
- 🔴 **Saturado** — solo con diferencial fuerte de oferta, formato o segmento.

### Dos señales que valen más que el conteo de marcas

**Días al aire** separa ganador de test:

| Días al aire | Lectura |
|---|---|
| **60+** | 🏆 Probado — sobrevivió la optimización. Este es el creativo a estudiar. |
| 15-59 | 📈 En escala — funciona, sin confirmar. |
| <15 | 🧪 Test reciente — puede apagarse mañana. No concluir nada. |

**Foco vs dispersión** identifica al competidor peligroso:

| Patrón | Significado |
|---|---|
| 1 producto, foco 80-100% | Marca monoproducto. **El más peligroso:** sabe qué vende y lo escala. |
| 1 producto, 2-3 destinos (ficha + advertorial) | Embudo maduro de varios pisos. |
| 4-8 productos distintos | Tienda de catálogo. Te cruza de costado. |
| 10+ productos, foco <20% | Tienda general tirando espagueti. Poca amenaza — pero ojo: tanta rotación suele significar que nada pegó. |

Cinco tiendas de catálogo pesan menos que dos marcas enfocadas.

---

## 6. Reglas de decisión (estrictas)

**NO-GO automático si:**
- Fallan 2+ MUSTs del checklist global
- Fallan 2+ MUSTs de Market Fit
- Falla cualquier MUST de Market Fit **+** cualquier MUST de Ecosistema
- El margen no es viable (precio sugerido muy lejos del mercado AR)
- El producto está en la lista de excluidos de importación y no hay proveedor local

**GO con flags amarillas si:**
- Pasa todos los MUSTs pero tiene 3+ NICEs en score 0-2
- Pasa todos los MUSTs pero hay MUSTs en "sin evidencia suficiente"

**GO claro si:**
- Todos los MUSTs con score 3+
- NICEs mayormente 3+

---

## 7. Defensa permitida, pero con evidencia

Si el sistema marca NO-GO, se puede justificar. Se reevalúa **solo si** se aporta:

- Links o datos que no se habían revisado
- Datos reales de proveedores
- Un cambio de ángulo u oferta que cambia el análisis

Si solo hay insistencia sin evidencia nueva, el NO-GO se mantiene. El rol del
sistema no es decirnos lo que queremos escuchar.
