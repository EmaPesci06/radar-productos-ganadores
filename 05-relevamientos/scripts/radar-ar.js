#!/usr/bin/env node
/**
 * Radar AR — Meta Ad Library, desde el contenedor.
 *
 * Implementa la logica de extraccion de la skill `radar-adlibrary-ar` con el
 * Chromium + Playwright que ya vienen en el contenedor, sin depender de Claude in
 * Chrome ni de la extension de GetHookd.
 *
 * REQUISITO: `www.facebook.com` tiene que estar habilitado en Network access del
 * entorno. Hoy el proxy responde 403 a CONNECT. Ver
 * 05-relevamientos/2026-10-31-laboratorios-facon-y-anmat.md §4.
 *
 * Reglas duras que respeta (de la skill):
 *   - Solo lectura. No completa formularios, no compra, no se suscribe.
 *   - NUNCA clickea el CTA de un anuncio: ese clic se le cobra al competidor.
 *     El destino real se lee del href (l.facebook.com/l.php?u=) y se decodifica.
 *   - Verifica el orden por impresiones en CADA pagina, no lo asume.
 *
 * Uso:
 *   node radar-ar.js --query "ciatica"                  # descubrir marcas del nicho
 *   node radar-ar.js --page-id 123456789                # relevar una biblioteca
 *   node radar-ar.js --page-id 123456789 --foco         # medir foco sobre 20-30 ads
 *   node radar-ar.js --query "ciatica" --json salida.json
 */

const { chromium } = require('playwright');
const fs = require('fs');

const MESES = { ene:0, feb:1, mar:2, abr:3, may:4, jun:5, jul:6, ago:7, sep:8, oct:9, nov:10, dic:11 };

function arg(name, def) {
  const i = process.argv.indexOf('--' + name);
  if (i === -1) return def;
  const v = process.argv[i + 1];
  return (v && !v.startsWith('--')) ? v : true;
}

function diasAlAire(fechaTexto) {
  if (!fechaTexto) return null;
  const m = fechaTexto.match(/(\d{1,2})\s+([a-z]{3})\w*\.?\s+(\d{4})/i);
  if (!m) return null;
  const mes = MESES[m[2].toLowerCase().slice(0, 3)];
  if (mes === undefined) return null;
  const d = new Date(Date.UTC(+m[3], mes, +m[1]));
  return Math.floor((Date.now() - d.getTime()) / 86400000);
}

function lectura(dias) {
  if (dias === null) return '?';
  if (dias >= 60) return 'PROBADO';       // sobrevivio la optimizacion
  if (dias >= 15) return 'EN ESCALA';
  return 'TEST RECIENTE';                  // puede apagarse manana
}

async function cargar(page, url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);
  // Sin este scroll los <video> no estan en el DOM (todo sale como imagen)
  // y los links de destino todavia no existen.
  for (let i = 0; i < 10; i++) await page.mouse.wheel(0, 1200);
  await page.waitForTimeout(3000);
  for (let i = 0; i < 10; i++) await page.mouse.wheel(0, 1200);
  await page.waitForTimeout(4000);
}

async function verificarOrden(page) {
  // Chequeo barato que complementa, no reemplaza, el visual: la URL tiene que
  // contener sort_data[mode]=total_impressions.
  const url = page.url();
  const porImpresiones = url.includes('total_impressions');
  return {
    modo: porImpresiones ? 'impresiones' : 'OTRO (revisar a mano el desplegable "Ordenar por")',
    url,
  };
}

async function descubrirMarcas(page, query) {
  const url = `https://www.facebook.com/ads/library/?active_status=active&ad_type=all`
    + `&country=AR&q=${encodeURIComponent(query)}&search_type=keyword_unordered&media_type=all`;
  await cargar(page, url);
  const marcas = await page.evaluate(() => {
    const m = {};
    for (const a of document.querySelectorAll('a[href*="view_all_page_id"]')) {
      const id = (a.href.match(/view_all_page_id=(\d+)/) || [])[1];
      if (!id) continue;
      const name = (a.innerText || '').trim();
      if (name && !m[id]) m[id] = name;
    }
    return m;
  });
  const total = await page.evaluate(
    () => (document.body.innerText.match(/~?[\d.,]+\s*resultados?/i) || [])[0] || null);
  return { query, total, marcas };
}

async function relevarBiblioteca(page, pageId, n) {
  const url = `https://www.facebook.com/ads/library/?active_status=active&ad_type=all`
    + `&country=AR&view_all_page_id=${pageId}&sort_data[direction]=desc`
    + `&sort_data[mode]=total_impressions`;
  await cargar(page, url);
  const orden = await verificarOrden(page);

  const datos = await page.evaluate((N) => {
    const media = {};
    for (const m of document.querySelectorAll('video, img')) {
      if (m.tagName === 'IMG' && (m.clientWidth < 200 || m.clientHeight < 150)) continue;
      let a = m;
      for (let i = 0; i < 25 && a; i++) {
        const t = a.innerText || '';
        const ids = t.match(/Identificador de la biblioteca:\s*(\d+)/g);
        if (ids && ids.length === 1) {
          const id = t.match(/Identificador de la biblioteca:\s*(\d+)/)[1];
          if (!media[id]) media[id] = (m.tagName === 'VIDEO' ? 'video' : 'imagen');
          break;
        }
        a = a.parentElement;
      }
    }
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const hits = []; let node;
    while ((node = w.nextNode())) {
      if (node.textContent.startsWith('Identificador de la biblioteca:')) hits.push(node.parentElement);
    }
    const ads = hits.slice(0, N).map((el) => {
      let card = el;
      for (let i = 0; i < 25 && card.parentElement; i++) {
        const t = card.innerText || '';
        if ((t.match(/Identificador de la biblioteca/g) || []).length > 1) { card = null; break; }
        if (t.includes('Publicidad') && t.length > 400) break;
        card = card.parentElement;
      }
      const t = card ? card.innerText : '';
      const id = el.innerText.match(/(\d+)/)[1];
      const lines = t.split('\n').map((s) => s.trim()).filter(Boolean);
      const pi = lines.findIndex((s) => s === 'Publicidad');
      const body = pi >= 0 ? (lines.slice(pi + 1).filter((s) => s !== 'View Page')[0] || '') : '';
      // Destino real SIN clickear: el CTA pasa por el redirector de FB.
      let dest = '';
      const lk = card && card.querySelector('a[href*="l.php?u="], a[href*="l.facebook.com/l.php"]');
      if (lk) {
        try { dest = decodeURIComponent(new URL(lk.href).searchParams.get('u') || '').split('?')[0]; }
        catch (e) { /* sin destino legible */ }
      }
      return {
        id,
        fecha: (t.match(/En circulación desde el ([^\n]+)/)
             || t.match(/Se empezó a publicar el ([^\n]+)/) || [])[1] || '',
        formato: media[id] || '?',
        usanContenido: (t.match(/(\d+)\s+anuncios usan este contenido/) || [])[1] || '1',
        variasVersiones: /varias versiones/.test(t) ? 'si' : 'no',
        destino: dest,
        titular: body.slice(0, 95),
        cuerpo: pi >= 0 ? lines.slice(pi + 1).join(' / ').slice(0, 260) : '',
      };
    });
    return {
      total: (document.body.innerText.match(/~?[\d.,]+\s*resultados?/i) || [])[0] || null,
      ads,
    };
  }, n);

  for (const a of datos.ads) {
    a.dias = diasAlAire(a.fecha);
    a.lectura = lectura(a.dias);
  }
  // Titulares duplicados: mismo copy + creativo distinto = testean angulos
  // visuales sobre un texto ganador. Se compara el cuerpo, no la primera linea.
  const dup = [];
  for (let i = 0; i < datos.ads.length; i++) {
    for (let j = i + 1; j < datos.ads.length; j++) {
      if (datos.ads[i].cuerpo && datos.ads[i].cuerpo === datos.ads[j].cuerpo) dup.push([i + 1, j + 1]);
    }
  }
  return { pageId, orden, ...datos, duplicados: dup };
}

async function medirFoco(page, pageId) {
  // 5 anuncios es muestra chica para esto: la skill pide 20-30.
  const url = `https://www.facebook.com/ads/library/?active_status=active&ad_type=all`
    + `&country=AR&view_all_page_id=${pageId}&sort_data[direction]=desc`
    + `&sort_data[mode]=total_impressions`;
  await cargar(page, url);
  for (let i = 0; i < 20; i++) await page.mouse.wheel(0, 1500);
  await page.waitForTimeout(4000);

  return await page.evaluate(() => {
    const dests = [];
    for (const a of document.querySelectorAll('a[href*="l.php?u="], a[href*="l.facebook.com/l.php"]')) {
      try {
        const u = decodeURIComponent(new URL(a.href).searchParams.get('u') || '').split('?')[0];
        if (u) dests.push(u);
      } catch (e) { /* ignorar */ }
    }
    const norm = (u) => { try { const x = new URL(u); return x.hostname.replace(/^www\./, '') + x.pathname.replace(/\/$/, ''); } catch (e) { return u; } };
    const tipo = (u) => /\/products?\//.test(u) ? 'producto'
      : /\/(blog|nota|notas|articulo|art[ií]culo|post|pages)\//.test(u) ? 'advertorial'
      : /\/collections?\//.test(u) ? 'coleccion' : 'home/otro';
    const c = {};
    for (const d of dests) { const k = norm(d); c[k] = (c[k] || 0) + 1; }
    const orden = Object.entries(c).sort((a, b) => b[1] - a[1]);
    const productos = new Set(dests.filter((d) => /\/products?\//.test(d))
      .map((d) => norm(d).split('/products/')[1] || norm(d).split('/product/')[1]));
    const tipos = {};
    for (const d of dests) { const k = tipo(d); tipos[k] = (tipos[k] || 0) + 1; }
    return {
      adsConLink: dests.length,
      destinosDistintos: orden.length,
      productosDistintos: productos.size,
      focoTop: orden[0] ? Math.round(orden[0][1] / dests.length * 100) + '%' : '-',
      tipos,
      top: orden.slice(0, 8),
    };
  });
}

(async () => {
  const query = arg('query');
  const pageId = arg('page-id');
  const n = parseInt(arg('n', '5'), 10);
  const salida = arg('json');

  if (!query && !pageId) {
    console.error('Uso: node radar-ar.js --query "<dolor>"  |  --page-id <id> [--foco] [--n 5]');
    process.exit(1);
  }

  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ locale: 'es-AR', viewport: { width: 1400, height: 1000 } });
  let out;
  try {
    if (query) {
      out = await descubrirMarcas(page, query);
      console.log(`\nQuery: "${out.query}"   total declarado: ${out.total || '?'}`);
      console.log(`Marcas distintas: ${Object.keys(out.marcas).length}\n`);
      for (const [id, nombre] of Object.entries(out.marcas)) console.log(`  ${id}  ${nombre}`);
      console.log('\nDescartar retailers genericos y marketplaces (Mercado Libre, farmacias,');
      console.log('medios) y quedarse con las DTC del nicho. Las que aparecen en varias');
      console.log('queries van primero: esa repeticion ya es senal.\n');
    } else {
      out = await relevarBiblioteca(page, pageId, n);
      console.log(`\npage_id ${out.pageId}   total: ${out.total || '?'}   orden: ${out.orden.modo}\n`);
      console.log('# | ID biblioteca     | Fecha        | Dias | Lectura       | Fmt    | Destino');
      console.log('-'.repeat(110));
      out.ads.forEach((a, i) => {
        console.log(`${i + 1} | ${a.id.padEnd(17)} | ${(a.fecha || '?').slice(0, 12).padEnd(12)} `
          + `| ${String(a.dias ?? '?').padStart(4)} | ${a.lectura.padEnd(13)} | ${a.formato.padEnd(6)} `
          + `| ${(a.destino || 'sin destino').slice(0, 45)}`);
      });
      if (out.duplicados.length) {
        console.log('\nTitulares duplicados (mismo copy, creativo distinto = testean angulos visuales');
        console.log('sobre un texto ganador): ' + out.duplicados.map(([a, b]) => `#${a}=#${b}`).join(' . '));
      }
      if (out.ads.some((a) => a.formato === '?')) {
        console.log('\n[!] Hay formatos en "?": falto scroll. Volver a correr.');
      }
      if (arg('foco')) {
        const f = await medirFoco(page, pageId);
        console.log('\n--- FOCO vs DISPERSION (sobre ' + f.adsConLink + ' anuncios con link) ---');
        console.log(JSON.stringify(f, null, 1));
        const prods = f.productosDistintos;
        console.log('\nLectura: ' + (prods <= 1 && parseInt(f.focoTop) >= 80
          ? 'MARCA MONOPRODUCTO. El competidor mas peligroso: sabe que vende y lo escala.'
          : prods >= 10 ? 'Tienda general tirando espagueti. Poca amenaza directa.'
          : prods >= 4 ? 'Tienda de catalogo. Compite en el nicho pero no vive de el.'
          : 'Embudo de varios pisos sobre el mismo producto. Operacion madura.'));
        console.log('Cruzar siempre con los dias al aire: foco alto con pocos dias es una');
        console.log('marca nueva apostando a una carta, no un ganador probado.\n');
        out.foco = f;
      }
    }
    if (salida && typeof salida === 'string') {
      fs.writeFileSync(salida, JSON.stringify(out, null, 2));
      console.log(`\nJSON escrito en ${salida}`);
    }
  } catch (e) {
    console.error('\nFALLO:', e.message);
    if (/ERR_TUNNEL|403|ENOTFOUND/.test(e.message)) {
      console.error('\nwww.facebook.com no esta habilitado en Network access de este entorno.');
      console.error('Menu del entorno en la barra de titulo -> Edit -> Network access.');
      console.error('Ver 05-relevamientos/2026-10-31-laboratorios-facon-y-anmat.md §4');
    }
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
})();
