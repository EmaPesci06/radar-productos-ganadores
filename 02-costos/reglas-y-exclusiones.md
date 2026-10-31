# Reglas de importación y lista de exclusiones

**Este es el primer filtro de las importaciones.** Un producto que no pasa acá no
se importa.

> ## ⚠️ Corrección importante (31/10/2026)
>
> La v1 de este archivo trataba la lista de exclusiones como un **gate universal de
> producto**. Está mal, y el error no es menor: **la lista es de IMPORTAR, no del
> producto.** Con el vault ECOMAI cargado quedó claro que las dos verticales más
> fuertes del ranking esquivan la lista entera porque **no importan nada**:
>
> | Vertical | Cómo esquiva la lista |
> |---|---|
> | **Espuma y textil local** (almohadas) | Se fabrica acá. No pasa por Aduana ni por ANMAT. Cero gates. |
> | **Nicho laboratorio local a façon** (jabón de caqui, loción de magnesio) | Un cosmético **importado** es NO-GO por ANMAT. El **mismo cosmético fabricado a façon** en un laboratorio argentino habilitado entra por habilitación simplificada (**Disp. ANMAT 7939/2025**, Grado 1), bajo el legajo del laboratorio. |
>
> Con mi gate original, el jabón de caqui (90/100, el mejor puntaje de evidencia
> afuera de toda la cartera) habría muerto en el primer filtro sin research. Igual la
> loción de magnesio (89/100).
>
> **La regla correcta:** antes de aplicar esta lista, preguntar **de dónde viene el
> producto**. Si se fabrica o se terceriza en Argentina, esta lista no aplica. Si se
> importa, aplica entera.

### La salida local

El orden de preferencia del curso para resolver el abastecimiento:

| Prioridad | Vía | Cuándo | Dónde |
|---|---|---|---|
| **1** | **Fabricación local** (espuma, textil, tapicería) | Producto voluminoso o pesado | Fábricas de poliuretano, Once, Avellaneda, talleres textiles |
| **2** | **Laboratorio local a façon** | Cosméticos y suplementos | Laboratorio cosmético habilitado en AMBA, bajo Disp. ANMAT 7939/2025 |
| **3** | **Mayorista local** | Lo que ya se importa y se vende acá | Avellaneda a un Toque, Once, importadores |
| **4** | **Courier desde Alibaba** | Solo accesorios livianos (<50 g) y no regulados | Trade Assurance, DDP puerta a puerta |

> **El dato que ordena todo esto:** en el ranking maestro del 31/10, los candidatos
> `fisico-courier` promedian **33,4 puntos sobre 100** y su mejor caso llega a 84. Los
> `fisico-local` promedian **89**. Importar por courier no es neutral: es
> sistemáticamente la peor ruta en el mercado argentino, por aduana, por el tope de
> 50 kg y por el ancla de precio de Mercado Libre.
>
> Correr `python3 01-scorecard/calcular_score.py` y mirar el resumen por tipo.

Vigencia de las referencias: **octubre 2026**. Los límites, franquicias, alícuotas y
el tipo de cambio cambian seguido — verificar en ARCA, Boletín Oficial y la cotización
del día antes de usarlos en una decisión real.

---

## Productos PERMITIDOS

Solo importamos lo que **no necesita aprobaciones ni certificaciones extra**:

- Bijouterie y accesorios
- Indumentaria
- Calzado
- Textiles
- Gadgets y artículos de hogar **sin pilas, sin batería y sin cable**

## Productos EXCLUIDOS — gate duro

| Categoría | Organismo / motivo |
|---|---|
| Cualquier cosa con pilas, batería, cargador, cable o enchufe | Seguridad eléctrica; las baterías complican el envío |
| Wifi, bluetooth, cualquier emisor de radiofrecuencia | ENACOM |
| Cosméticos, perfumes, cremas, higiene personal, productos médicos | ANMAT |
| Todo lo que toca alimentos o bebidas: vasos, termos, utensilios, tuppers, botellas | INAL / ANMAT |
| Juguetes y artículos para bebés o niños | Certificación de seguridad |
| Madera sin tratar, plantas, semillas, productos de origen animal | SENASA |
| Líquidos, aerosoles, polvos | Restricción de transporte |
| Productos con marcas de terceros o réplicas | La aduana los retiene |

**Zona gris:** si un gadget "podría" considerarse juguete, buscar la posición
arancelaria y si tiene intervención. Si la tiene → excluido. En la duda, excluido.

> ⚠️ Esta lista choca de frente con las tres categorías más vendidas de Argentina
> (alimentos y bebidas, herramientas y construcción, hogar). Es esperable y no es un
> problema: nuestro modelo no compite por volumen de categoría, compite por nicho de
> dolor con ticket alto y peso bajo. Ver `00-marco/04-evidencia-web-2026.md` §1.

---

## Condición fiscal: testear y después formalizar

**Etapa de test** (1 o 2 importaciones chicas por courier): valida el producto con poca
plata. La ley de Monotributo **no contempla importar para revender**, así que es una
etapa corta, no un modelo de negocio.

**Cuando el producto se valida:** pasar a Responsable Inscripto antes de escalar.
Se recupera el IVA de la importación como crédito fiscal, se recuperan las percepciones
del régimen general y se puede importar con despachante en volúmenes que bajan el costo
por unidad. **Planificarlo con el contador.**

Nunca: subfacturar, partir un envío comercial en varios "personales", usar datos de
terceros. Si el proveedor lo ofrece, el riesgo (retención, multa) es nuestro.

---

## Vías de importación

| Vía | Cuándo | Límites de referencia (verificar vigentes) |
|---|---|---|
| **Courier personal (con franquicia)** | Muestras, uso propio | Hasta USD 3.000 y 50 kg por envío, hasta 3 unidades iguales, sin fin comercial. Franquicia de USD 400 FOB: sin derecho ni estadística (el IVA se paga igual). Hasta 5 envíos por año |
| **Courier comercial** | Lote de test (100-500 unidades chicas) | Hasta USD 3.000 y 50 kg. **Sin franquicia:** paga derecho, estadística, honorarios e IVA sobre todo el valor |
| **Régimen general con despachante** | Más de USD 3.000 o carga | Despachante, IVA adicional y percepciones |

> **Regla práctica:** con **100 o más unidades iguales, asumir courier comercial**,
> aunque el valor sea menor a USD 400. Ya nos pasó: pagamos derecho completo con valor
> declarado por debajo de la franquicia.

---

## Fórmulas de impuestos

### Courier comercial (validada contra un desglose real de DHL)

```
Derecho     = Valor en aduana × % derecho del producto
Estadística = Valor en aduana × 3%
Honorarios  = cargo fijo de gestión del courier (~ARS 22.900 en oct 2026)
IVA         = 21% × (Valor aduana + Derecho + Estadística + Honorarios)

TOTAL al courier = Derecho + Estadística + Honorarios + IVA
```

El IVA se calcula **también sobre los honorarios**. En courier comercial no aparecieron
IVA adicional ni percepciones de Ganancias o IIBB.

### Courier personal con franquicia

```
Excedente   = FOB − 400   (si es negativo, 0)
Derecho     = Excedente × % derecho
Estadística = Excedente × 3%
IVA         = 21% × (Valor aduana + Derecho + Estadística)
+ gestión del courier
```

### Régimen general (referencia)

| Concepto | Cálculo |
|---|---|
| Derecho | % según posición arancelaria, sobre CIF |
| Estadística | 3% sobre CIF |
| IVA | 21% (algunos 10,5%) sobre CIF + derecho + estadística |
| IVA adicional | 20% sobre la misma base |
| Percepción Ganancias | 6% Responsable Inscripto / 11% resto |
| Percepción IIBB | ~2,5% según provincia |
| Extra | Despachante, depósito, flete interno |

---

## Derecho de importación por rubro (referencia oct 2026 — verificar)

| Rubro | Derecho | Fuente |
|---|---|---|
| **Bijouterie (7117)** | **35%** | Confirmado con desglose real de DHL |
| Indumentaria y calzado | **20%** | Decreto 236/2025 (bajó de 35%) |
| Telas | 18% | Decreto 236/2025 |
| Gadgets / hogar sin pilas | Varía según material y uso | Buscar la posición arancelaria de cada producto |

Si no se encuentra el derecho exacto: **calcular con 20% y con 35% y mostrar el rango.**

> El derecho es un **eje de decisión de producto**, no un detalle administrativo. En el
> caso real, el 35% de bijouterie fue casi la mitad de los impuestos pagados.

---

## Flete: peso real vs volumétrico

Se cobra el **mayor** de los dos, redondeado hacia arriba al medio kilo.

| Vía | Peso volumétrico |
|---|---|
| Courier express (DHL, FedEx, UPS) | L × A × H (cm) ÷ **5.000** |
| Carga aérea | L × A × H (cm) ÷ **6.000** |
| Marítimo consolidado | por m³ (mínimo 1 m³) |

Si el volumétrico supera al real, **estamos pagando aire**: revisar packaging o armado
de la caja.

### Qué vía conviene

- Muestras o test (hasta ~50 kg): **courier**. Rápido (5-10 días hábiles), sin despachante.
- ~100-500 kg: cotizar **carga aérea** con forwarder vs courier.
- Más de 1-2 m³: **marítimo consolidado** (45-75 días, con despachante).

**Referencia de flete** (caso real DHL Express China→Argentina, oct 2026):
**~USD 14,8 por kg cobrado**. Usar solo si el proveedor no cotizó; siempre preferir la
cotización real.

---

## Medio de pago

Pagar **siempre dentro de Alibaba** (sección de pagos / Trade Assurance). Nunca por fuera.

Medio recomendado: tarjeta en dólares de una app tipo DolarApp (ARQ), que no cobra
percepciones; el costo es un dólar algo más alto. **Contar ~5% extra** sobre el total
de Alibaba (caso real: orden de USD 478 → USD 503 cobrados).

Si se paga con tarjeta en pesos, buscar las percepciones vigentes sobre consumos en
dólares y sumarlas al costo.

---

## Checklist de proforma — antes de pagar

La proforma es lo que ve la aduana. En el caso real vino con errores en 4 campos.

- [ ] Nombre del comprador correcto
- [ ] **CUIT en el campo de identificación fiscal**, rotulado como CUIT o Tax ID
      (no "CNPJ", que es de Brasil, ni metido en el campo de e-mail)
- [ ] Dirección completa, ciudad, provincia, código postal y país
- [ ] Teléfono con +54 y e-mail correctos
- [ ] Cantidad por modelo y variante = lo acordado en el chat
- [ ] Precio unitario y total correctos. **Packaging en renglón aparte**, sin contarlo
      como "piezas" del producto
- [ ] Descripción clara y real con material (ej. "stainless steel necklace, imitation
      jewelry", no solo "necklace")
- [ ] Posición arancelaria (HS code) coherente con cada ítem — **el packaging no lleva
      el código del producto**
- [ ] Peso bruto (kg), cantidad de cajas y medidas de la caja master
- [ ] Condiciones de pago y plazo de despacho, coherentes con la orden
- [ ] Flete separado del valor de la mercadería

> **Los plazos del chat no son los de la orden.** Confiar en la orden de Alibaba.

---

## Fuentes a verificar en cada uso

- ARCA – Régimen de Courier (límites, franquicia, envíos por año): servicioscf.afip.gob.ar
- Boletín Oficial (en 2026 se anunció una reforma del régimen courier)
- Cotización del dólar oficial del día
- Derecho de importación de la posición arancelaria del producto
  (indumentaria y calzado: Decreto 236/2025)

Ante cualquier duda fiscal: **validarlo con el contador.**
