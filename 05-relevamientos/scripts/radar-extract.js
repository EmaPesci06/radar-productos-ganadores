#!/usr/bin/env node
/**
 * Radar AR v2 — extraccion por tarjeta.
 *
 * Meta cambio el DOM: los links de anunciante ya no son `view_all_page_id`, ahora
 * son `facebook.com/<page_id|vanity>/`. Esta version ancla en cada
 * "Identificador de la biblioteca", sube al contenedor de la tarjeta y saca de ahi
 * anunciante, fecha, formato, destino y copy.
 *
 * Reglas duras de la skill radar-adlibrary-ar que respeta:
 *   - Solo lectura.
 *   - NUNCA clickea el CTA del competidor: el destino se lee del href
 *     (l.facebook.com/l.php?u=) y se decodifica.
 *
 * Uso:
 *   node radar-extract.js --query "ciatica" [--n 30] [--json out.json]
 *   node radar-extract.js --queries "ciatica,dolor lumbar,almohada" --json out.json
 */
const { chromium } = require('playwright');
const fs = require('fs');

const MESES = { ene:0, feb:1, mar:2, abr:3, may:4, jun:5, jul:6, ago:7, sep:8, oct:9, nov:10, dic:11 };
// Rutas de facebook.com que NO son anunciantes.
const NO_ANUNCIANTE = /^\/(ads|policies|privacy|help|legal|business|about|terms|login|groups|watch|$)/;

function arg(n, d) {
  const i = process.argv.indexOf('--' + n);
  if (i === -1) return d;
  const v = process.argv[i + 1];
  return (v && !v.startsWith('--')) ? v : true;
}

function dias(fecha) {
  if (!fecha) return null;
  const m = fecha.match(/(\d{1,2})\s+([a-z]{3})\w*\.?\s+(\d{4})/i);
  if (!m) return null;
  const mes = MESES[m[2].toLowerCase().slice(0, 3)];
  if (mes === undefined) return null;
  return Math.floor((Date.now() - Date.UTC(+m[3], mes, +m[1])) / 86400000);
}
const lectura = (d) => d === null ? '?' : d >= 60 ? 'PROBADO' : d >= 15 ? 'EN ESCALA' : 'TEST RECIENTE';

async function cargar(page, url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(9000);
  // Sin scroll los <video> no estan en el DOM y los destinos todavia no existen.
  for (let r = 0; r < 3; r++) {
    for (let i = 0; i < 10; i++) { await page.mouse.wheel(0, 1400); await page.waitForTimeout(400); }
    await page.waitForTimeout(3000);
  }
}

async function extraer(page, n) {
  return await page.evaluate(({ N, noAdv }) => {
    const reNoAdv = new RegExp(noAdv);
    const total = (document.body.innerText.match(/~?[\d.,]+\s*resultados?/i) || [])[0] || null;

    // Anclar en cada "Identificador de la biblioteca"
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const anclas = []; let node;
    while ((node = w.nextNode())) {
      if (/Identificador de la biblioteca:/.test(node.textContent)) anclas.push(node.parentElement);
    }

    const ads = [];
    for (const el of anclas.slice(0, N)) {
      // Subir hasta el contenedor que tiene UNA sola tarjeta
      let card = el, prev = el;
      for (let i = 0; i < 30 && card.parentElement; i++) {
        const t = card.innerText || '';
        if ((t.match(/Identificador de la biblioteca/g) || []).length > 1) { card = prev; break; }
        prev = card;
        card = card.parentElement;
      }
      const t = card ? card.innerText : '';
      const id = (el.innerText.match(/(\d+)/) || [])[1] || '';

      // Anunciante: link a facebook.com/<algo>/ dentro de la tarjeta
      let anunciante = '', pageRef = '';
      for (const a of card.querySelectorAll('a[href*="facebook.com/"]')) {
        let path;
        try { path = new URL(a.href).pathname; } catch (e) { continue; }
        if (reNoAdv.test(path)) continue;
        const slug = path.replace(/^\/|\/$/g, '');
        if (!slug || slug.includes('/')) continue;
        pageRef = slug;
        anunciante = (a.innerText || '').trim() || slug;
        break;
      }

      // Destino real SIN clickear
      let destino = '';
      const lk = card.querySelector('a[href*="l.php?u="], a[href*="l.facebook.com/l.php"]');
      if (lk) {
        try { destino = decodeURIComponent(new URL(lk.href).searchParams.get('u') || '').split('?')[0]; }
        catch (e) { /* sin destino legible */ }
      }

      // Formato: video si la tarjeta tiene <video>, imagen si tiene img grande
      let formato = '?';
      if (card.querySelector('video')) formato = 'video';
      else {
        for (const im of card.querySelectorAll('img')) {
          if (im.clientWidth >= 180 && im.clientHeight >= 140) { formato = 'imagen'; break; }
        }
      }

      const lines = t.split('\n').map((s) => s.trim()).filter(Boolean);
      const pi = lines.findIndex((s) => s === 'Publicidad');
      const cuerpo = pi >= 0 ? lines.slice(pi + 1).filter((s) => s !== 'View Page').join(' / ') : '';

      ads.push({
        id,
        anunciante,
        pageRef,
        fecha: (t.match(/En circulación desde el ([^\n]+)/) || t.match(/Se empezó a publicar el ([^\n]+)/) || [])[1] || '',
        formato,
        usanContenido: (t.match(/(\d+)\s+anuncios usan este contenido/) || [])[1] || '1',
        variasVersiones: /varias versiones/.test(t) ? 'si' : 'no',
        destino,
        titular: cuerpo.slice(0, 110),
        cuerpoLargo: cuerpo.length,
        cuerpoHash: cuerpo.slice(0, 260),
      });
    }
    return { total, ads };
  }, { N: n, noAdv: NO_ANUNCIANTE.source });
}

function resumir(q, r) {
  for (const a of r.ads) { a.dias = dias(a.fecha); a.lectura = lectura(a.dias); }

  // Agregado por anunciante
  const porMarca = {};
  for (const a of r.ads) {
    const k = a.anunciante || a.pageRef || '(sin identificar)';
    porMarca[k] = porMarca[k] || { ads: 0, maxDias: 0, destinos: new Set(), formatos: {}, advertorial: 0 };
    const m = porMarca[k];
    m.ads++;
    if (a.dias !== null) m.maxDias = Math.max(m.maxDias, a.dias);
    if (a.destino) m.destinos.add(a.destino.replace(/^https?:\/\/(www\.)?/, ''));
    m.formatos[a.formato] = (m.formatos[a.formato] || 0) + 1;
    // Advertorial: copy largo (la skill marca 250-350+ palabras) o destino tipo nota
    if (a.cuerpoLargo > 1200 || /\/(blog|nota|notas|articulo|post|pages)\//.test(a.destino)) m.advertorial++;
  }

  // Copys duplicados: mismo texto, creativo distinto = testean angulos visuales
  // sobre un texto ganador. Se agrupan: listar todos los pares da N*(N-1)/2
  // lineas ilegibles (con 14 ads iguales son 91 pares).
  const grupos = {};
  for (const a of r.ads) {
    if (!a.cuerpoHash) continue;
    (grupos[a.cuerpoHash] = grupos[a.cuerpoHash] || []).push(a);
  }
  const dup = Object.values(grupos).filter((g) => g.length > 1).map((g) => ({
    n: g.length,
    marca: g[0].anunciante || '?',
    ids: g.map((a) => a.id),
    titular: g[0].titular.slice(0, 70),
  })).sort((a, b) => b.n - a.n);
  return { query: q, total: r.total, nAds: r.ads.length, ads: r.ads, duplicados: dup,
    marcas: Object.fromEntries(Object.entries(porMarca).map(([k, v]) =>
      [k, { ...v, destinos: [...v.destinos] }])) };
}

function imprimir(s) {
  console.log(`\n${'='.repeat(104)}`);
  console.log(`QUERY: "${s.query}"   total declarado: ${s.total || '?'}   anuncios leidos: ${s.nAds}`);
  console.log('='.repeat(104));
  const marcas = Object.entries(s.marcas).sort((a, b) => b[1].ads - a[1].ads);
  console.log(`\nMarcas distintas: ${marcas.length}\n`);
  console.log('Ads | MaxDias | Lectura       | Adv | Marca                          | Destino principal');
  console.log('-'.repeat(104));
  for (const [nombre, m] of marcas) {
    console.log(`${String(m.ads).padStart(3)} | ${String(m.maxDias || '?').padStart(7)} | `
      + `${lectura(m.maxDias || null).padEnd(13)} | ${String(m.advertorial).padStart(3)} | `
      + `${nombre.slice(0, 30).padEnd(30)} | ${(m.destinos[0] || 'sin destino').slice(0, 40)}`);
  }
  const probados = s.ads.filter((a) => a.dias !== null && a.dias >= 60);
  if (probados.length) {
    console.log(`\n--- ${probados.length} anuncio(s) PROBADO(S) (60+ dias al aire) ---`);
    for (const a of probados.sort((x, y) => y.dias - x.dias)) {
      console.log(`  ${String(a.dias).padStart(4)}d | ${a.formato.padEnd(6)} | ${(a.anunciante || '?').slice(0, 26).padEnd(26)} | ${a.titular.slice(0, 60)}`);
    }
  }
  if (s.duplicados.length) {
    console.log('\n--- Copys repetidos (mismo texto, creativo distinto = testean angulos visuales) ---');
    for (const g of s.duplicados) {
      console.log(`  ${g.n} ads | ${g.marca.slice(0, 26).padEnd(26)} | ${g.titular}`);
      if (g.n >= 5) console.log(`      ^ ${g.n} creativos sobre un texto ganador: es su angulo probado.`);
    }
  }
}

(async () => {
  const qs = arg('queries') ? String(arg('queries')).split(',').map((x) => x.trim())
    : arg('query') ? [String(arg('query'))] : null;
  if (!qs) { console.error('Uso: --query "<dolor>" | --queries "a,b,c" [--n 30] [--json out.json]'); process.exit(1); }
  const n = parseInt(arg('n', '30'), 10);
  const salida = arg('json');

  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const out = [];
  for (let qi = 0; qi < qs.length; qi++) {
    const q = qs[qi];
    // Contexto nuevo por query. Con uno compartido, a partir de la 4a query la
    // pagina dejaba de renderizar y el script devolvia 0 anuncios con la pagina
    // cargando bien: un FALSO NEGATIVO que parece "no hay competencia".
    const ctx = await b.newContext({ locale: 'es-AR', viewport: { width: 1500, height: 1100 } });
    const url = `https://www.facebook.com/ads/library/?active_status=active&ad_type=all`
      + `&country=AR&q=${encodeURIComponent(q)}&search_type=keyword_unordered&media_type=all`;
    let s = null;
    for (let intento = 1; intento <= 2 && !s; intento++) {
      const page = await ctx.newPage();
      try {
        await cargar(page, url);
        const r = await extraer(page, n);
        // Guardia anti falso negativo: 0 anuncios Y sin total declarado no es
        // "no hay competencia", es "no lei la pagina". Reintentar y, si sigue,
        // marcarlo como SIN_LEER en vez de reportar un hueco que no se midio.
        if (r.ads.length === 0 && !r.total) {
          const txt = await page.evaluate(() => document.body.innerText || '');
          const vacioReal = /No se encontraron|no coinciden|0 resultados/i.test(txt);
          if (!vacioReal) {
            console.error(`[${q}] intento ${intento}: 0 anuncios y sin total. `
              + `len=${txt.length}. ${intento < 2 ? 'Reintentando...' : 'SIN_LEER.'}`);
            await page.close();
            if (intento < 2) { await new Promise((r2) => setTimeout(r2, 15000)); continue; }
            out.push({ query: q, estado: 'SIN_LEER',
              nota: 'La pagina no renderizo. NO interpretar como hueco: no se midio.' });
            break;
          }
        }
        s = resumir(q, r);
        imprimir(s);
        out.push(s);
      } catch (e) {
        console.error(`\n[${q}] FALLO: ${e.message.split('\n')[0]}`);
        if (intento >= 2) out.push({ query: q, estado: 'ERROR', error: e.message.split('\n')[0] });
      }
      if (!page.isClosed()) await page.close();
    }
    await ctx.close();
    if (qi < qs.length - 1) await new Promise((r) => setTimeout(r, 12000));
  }
  await b.close();
  if (salida && typeof salida === 'string') {
    fs.writeFileSync(salida, JSON.stringify(out, null, 2));
    console.log(`\nJSON: ${salida}`);
  }
})();
