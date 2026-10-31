# Relevamientos

Investigación hecha **desde el repo**, fechada. Complementa `Vault ECOMAI/05 Plan de accion/`,
no lo reemplaza: el vault sigue siendo la fuente de verdad.

| Archivo | Qué trae |
|---|---|
| `2026-10-31-laboratorios-facon-y-anmat.md` | Short list de 5 laboratorios cosméticos a façon en AR con MOQ **desde 100 unidades**, y la Disp. ANMAT 7939/2025 confirmada en Boletín Oficial. Destraba el pendiente #2 de `GAPS.md` |

## Scripts

### `scripts/radar-ar.js` — Radar AR desde el contenedor

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

> ⚠️ **Hoy no corre:** `www.facebook.com` está bloqueado por la política de red de este
> entorno (el gateway responde 403 a CONNECT). El script detecta el caso y dice cómo
> destrabarlo. Ver `2026-10-31-laboratorios-facon-y-anmat.md` §4.
