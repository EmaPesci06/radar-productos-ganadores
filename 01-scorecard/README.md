# Scorecard — la matriz de decisión

> **Corrección del 31/10/2026.** La primera versión de este archivo usaba pesos que
> inventé (30/25/15/15/15 para físicos, otros cinco para eprods). Con el vault ECOMAI
> cargado quedó claro que **ya existe un scorecard propio**, el que se usó en
> `05 Plan de accion/Comparativa integral AR y Planificacion - 31 octubre.md` para
> rankear 13 candidatos. Este archivo ahora replica ese scorecard. Los pesos míos se
> descartaron: no había candidatos evaluados con ellos, así que no se invalidó nada.

El scorecard existe para que dos candidatos sean **comparables**. Mismos ejes, mismos
pesos, misma escala — y la misma escala para físicos y para ebooks, que es lo que
permite que compitan en un solo ranking.

---

## Los 5 ejes, 20 puntos cada uno

| Eje | Puntos | Qué mide | Dónde se verifica |
|---|---|---|---|
| **1. Evidencia afuera** | 20 | ¿Hay alguien ganando con esto en otro país? | GetHookd, Meta Ad Library US/ES/BR/AU |
| **2. Demanda y dolor en AR** | 20 | ¿El mismo dolor existe acá y la gente lo busca? | Google Trends AR (5a/12m), MELI AR, Reddit, TikTok, YouTube, foros |
| **3. Hueco en Meta AR** | 20 | ¿Está libre la cancha publicitaria local? | Radar AR sobre Meta Ad Library AR |
| **4. Facilidad operativa** | 20 | ¿Sin traba de ANMAT ni de Aduana? ¿Proveedor real? | Disp. ANMAT, posición arancelaria, peso/volumen, proveedores |
| **5. Margen y ecosistema** | 20 | ¿Cierra el CPA breakeven? ¿Hay AOV/LTV? | Calculadora de rentabilidad, packs, upsells, recompra |

**Total: 100.**

Escala por eje:

| Puntos | Significado |
|---|---|
| 18-20 | Evidencia fuerte y directa, varias fuentes coinciden |
| 14-17 | Evidencia clara con algún hueco |
| 10-13 | Evidencia suficiente pero con una traba identificada |
| 6-9 | Traba seria o evidencia débil |
| 0-5 | **Bloqueante o sin evidencia** (declararlo, no inventar un 10) |

> **Regla 1 del Doc A:** sin link, el dato cuenta 0-1. No se rellena con intuición.

---

## Umbrales de veredicto

Calibrados contra el ranking real del 31/10, donde el #1 sacó 95 y el corte de
descarte quedó bajo 60:

| Score | Veredicto | Qué hacer |
|---|---|---|
| **≥ 88** | 🟢 **EJECUTAR YA** | Al plan de acción: proveedor, muestras, lanzamiento |
| **80-87** | 🟡 **SEGUNDA OLA / CON CAUTELA** | Válido, pero hay una traba que resolver primero |
| **60-79** | 🟠 **SOLO COMO BUMP O BONO** | No sostiene una tienda propia. Sirve dentro de otra oferta |
| **< 60** | 🔴 **DESCARTADO / FRENADO** | Con el motivo escrito |

Un eje en 0-5 es **bloqueante**, independientemente del total: el Dispositivo
Antiatragantamiento tenía dolor y hueco publicitario, y murió por ANMAT Clase II.

---

## GATES — NO-GO automático

Si cualquiera de estos se cumple, el candidato muere sin research.

### Gates regulatorios y de aduana

| Gate | Por qué | Caso real |
|---|---|---|
| **Producto Médico Clase II sin PM aprobado** | Pautar sin número de PM expone a denuncia y bloqueo de cuenta | Dispositivo antiatragantamiento |
| **Cosmético o suplemento importado sin legajo** | ANMAT frena en Aduana | Esmalte en marcador |
| **Líquidos, aerosoles o polvos por courier** | Carga peligrosa, DHL restringe | Esmalte en marcador |
| El envío supera **50 kg** (tope del régimen courier) | No entra, hay que ir a carga aérea con despachante | Kit de descanso: 300 kits = 108 kg |

> ⚠️ **Estos gates son de IMPORTAR, no del producto.** Un cosmético fabricado a façon
> en un laboratorio local habilitado **no pasa por ninguno** — es la vertical del nicho
> laboratorio. Ver `02-costos/reglas-y-exclusiones.md` §"La salida local".

### Gates de mercado

| Gate | Por qué | Caso real |
|---|---|---|
| **Ancla de precio en MELI** demasiado baja frente al precio DTC | El cliente compara y se va | Antiatragantamiento: $13.495 en MELI vs $129.999 DTC |
| **Commodity quemado en MELI** | No hay margen ni diferenciación posible | Toalla refrescante |
| **CPA breakeven por debajo de ~$10.000** | No se puede comprar tráfico a ese precio en Meta AR | Antifaz suelto: breakeven $7.353 |
| Unidad suelta de **menos de $40.000** sin pack | Los costos fijos por pedido (envío ~$7.000 + fulfillment ~$1.500 + CPA ~$15.000) se la comen | Regla 2 del patrón ganador |
| Ya domina un **jugador grande con Full y cuotas** en MELI | Margen DTC muy fino | Manta refrescante: Gadnic |

### Gates del Doc A (se mantienen)

- Fallan 2+ MUSTs del checklist global
- Fallan 2+ MUSTs de Market Fit
- Falla un MUST de Market Fit **+** un MUST de Ecosistema
- El margen no cierra contra el precio de MELI AR

---

## Reglas de corte del test (disciplina de capital)

El scorecard decide qué se testea. **Esto decide qué se escala.**

| Formato | Presupuesto de test | GO (escalar) | STOP (cortar o iterar) |
|---|---|---|---|
| **Ebook** ($17.900-$19.900) | USD 50 (~$78.000) | **≥ 5 ventas**, CPA ≤ $15.000, take rate del order bump ≥ 20% | < 3 ventas con USD 50 → cambiar hook. Dos giros sin mejora → siguiente ebook |
| **Almohada lumbar** ($49.900 / combo $74.900) | USD 100 (~$156.000) | CPA ≤ $22.000 en 1u o ≤ $30.000 en combo (ROAS ≥ 2,5) | CTR del video < 1,2% → rehacer los primeros 3 segundos |
| **Almohada embarazo** ($79.900 / kit $99.900) | USD 100 | CPA ≤ $32.000 (ROAS ≥ 2,5) | Muchos carritos abandonados → destacar cuotas sin interés |
| **Jabón de caqui** (pack x3 $34.900) | USD 50-80 | CPA ≤ $14.000 (ROAS ≥ 2,5 + recompra a 60 días) | Nunca vender barra suelta a precio accesible: forzar el pack |

Criterio general del vault: **mínimo 5 ventas por cada USD 50 invertidos.**

---

## Uso de la calculadora

```bash
python3 01-scorecard/calcular_score.py
```

Lee todos los `03-candidatos/*.json`, aplica gates y suma los 5 ejes.

```bash
python3 01-scorecard/calcular_score.py --detalle almohada-lumbar-ciatica
```

Desglose eje por eje de un candidato.

```bash
python3 01-scorecard/calcular_score.py --tipo digital
```

Filtra por tipo (`fisico-local`, `fisico-courier`, `fisico-lab`, `digital`).
