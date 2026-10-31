# Relevamientos

Investigación hecha **desde el repo**, fechada. Complementa `Vault ECOMAI/05 Plan de accion/`,
no lo reemplaza: el vault sigue siendo la fuente de verdad.

| Archivo | Qué trae |
|---|---|
| `2026-10-31-costos-estimados-fisicos.md` | **Costo estimado de fabricación local de los 4 productos de descanso** y precio de venta derivado. Hallazgo: la tabla de markup del Doc A no aplica a fabricación local, manda el CPA breakeven |
| `2026-10-31-radar-ar-top4.md` | **Verificación independiente del hueco de los 4 candidatos top** en Meta Ad Library AR. Tres objeciones, una confirmación. Cambia qué se lanza primero |
| `2026-10-31-laboratorios-facon-y-anmat.md` | Short list de 5 laboratorios cosméticos a façon en AR con MOQ **desde 100 unidades**, y la Disp. ANMAT 7939/2025 confirmada en Boletín Oficial. Destraba el pendiente #2 de `GAPS.md` |

## Scripts

### `scripts/radar-extract.js` — descubrir marcas por dolor (el principal)

```bash
node 05-relevamientos/scripts/radar-extract.js --query "ciatica" --n 30
node 05-relevamientos/scripts/radar-extract.js --queries "nervio vago,dejar el pañal" --json out.json
```

Extrae por tarjeta: anunciante, fecha, formato, destino real y copy. Agrega por marca,
cuenta advertorials, resume los **PROBADOS** (60+ días) y agrupa los copys repetidos.

**Guardia anti falso negativo:** si una query devuelve 0 anuncios **y** sin total
declarado, no lo reporta como hueco — reintenta y, si sigue, la marca `SIN_LEER`. Pasó
de verdad: corriendo 6 queries seguidas con un contexto compartido, las últimas 3 daban
0 anuncios con la página cargando bien. Un 0 se lee como "no hay competencia" y es
justo la conclusión que haría lanzar contra competencia que no se midió.

### `scripts/radar-ar.js` — relevar una biblioteca por page_id

Implementa la lógica de extracción de la skill `radar-adlibrary-ar` con el Chromium +
Playwright que ya vienen en el contenedor, sin depender de Claude in Chrome ni de la
extensión de GetHookd.

```bash
node 05-relevamientos/scripts/radar-ar.js --query "ciatica"                  # descubrir marcas del nicho
node 05-relevamientos/scripts/radar-ar.js --page-id 123456789 --n 5          # relevar una biblioteca
node 05-relevamientos/scripts/radar-ar.js --page-id 123456789 --foco         # foco vs dispersión (20-30 ads)
node 05-relevamientos/scripts/radar-ar.js --query "ciatica" --json salida.json
```

Calcula días al aire y los clasifica con el criterio de la skill (**60+ = probado**,
15-59 = en escala, <15 = test reciente), detecta titulares duplicados comparando el
cuerpo completo, y mide foco vs dispersión sobre 20-30 anuncios.

**Respeta las reglas duras de la skill:**

- Solo lectura. No completa formularios, no compra, no se suscribe.
- **Nunca clickea el CTA de un anuncio de la competencia** — ese clic se le cobra al
  competidor y ensucia sus datos. El destino real se lee del `href`
  (`l.facebook.com/l.php?u=`) y se decodifica.
- Verifica el orden por impresiones, no lo asume.

## Estado de la red (31/10/2026)

| Host | Estado |
|---|---|
| `www.facebook.com` + `static.xx.fbcdn.net` + `*.fbcdn.net` | 🟢 **habilitados** — el radar corre |
| `listado.mercadolibre.com.ar` | 🔴 MELI muestra pantalla de login a IPs de datacenter. **No se arregla con permisos** |
| `trends.google.com` | 🔴 429, rate-limit a la IP del contenedor. **No se arregla con permisos** |
| GetHookd | 🔴 login pago + extensión. Solo desde una sesión local |

La demanda en MELI y la tendencia en Trends hay que mirarlas a mano o desde una sesión
local. La propia skill ya avisa que Trends es frágil y que si no renderiza en dos
intentos hay que saltearlo y decirlo.
