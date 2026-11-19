// Genera i mockup (PNG) degli annunci Retica. Uso: node tools/mockup/build_mockups.js
// Stile = brand Retica (sito retica.ai): navy #23253C, corallo #FF8A73, blu #5580FF, viola #58468C, font Poppins.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../..');
const HTML = path.join(__dirname, 'html');
const OUT = path.join(ROOT, 'output/mockup');
fs.mkdirSync(OUT, { recursive: true });
const ads = JSON.parse(fs.readFileSync(path.join(ROOT, 'analysis/ads.json'), 'utf8'));
const byId = Object.fromEntries(ads.map(a => [a.id, a]));
const LOGO_L = 'file://' + ROOT + '/assets/retica/logo_retica-3.png'; // bianco, per fondi scuri
const LOGO_D = 'file://' + ROOT + '/assets/retica/logo_retica-2.png'; // scuro
const AVATAR = 'file://' + ROOT + '/assets/retica/avatar_retica_derivato.png';

const CSS = `
@font-face{font-family:P;font-weight:300;src:url(../fonts/poppins-latin-300-normal.woff2)}
@font-face{font-family:P;font-weight:400;src:url(../fonts/poppins-latin-400-normal.woff2)}
@font-face{font-family:P;font-weight:500;src:url(../fonts/poppins-latin-500-normal.woff2)}
@font-face{font-family:P;font-weight:600;src:url(../fonts/poppins-latin-600-normal.woff2)}
@font-face{font-family:P;font-weight:700;src:url(../fonts/poppins-latin-700-normal.woff2)}
@font-face{font-family:P;font-weight:800;src:url(../fonts/poppins-latin-800-normal.woff2)}
:root{--navy:#23253C;--navy2:#1A1C2E;--coral:#FF8A73;--blue:#5580FF;--purple:#58468C;--ink:#2A2A2A;--mut:#716C80;--green:#75D69C;--paper:#fff}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:P,sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.cv{position:relative;overflow:hidden;background:radial-gradient(1200px 800px at 85% -10%,#34376a 0%,var(--navy) 55%,var(--navy2) 100%)}
.logo{position:absolute;left:64px;top:58px;height:64px}
.h{font-weight:700;line-height:1.08;letter-spacing:-.5px}
.co{color:var(--coral)} .bl{color:var(--blue)}
.pill{display:inline-block;background:var(--coral);color:#fff;font-weight:600;letter-spacing:2px;border-radius:999px;padding:22px 44px;font-size:30px}
.pill.b{background:var(--blue)}
.paper{background:#fff;border-radius:14px;box-shadow:0 30px 70px rgba(0,0,0,.35);color:#333;padding:26px;position:relative}
.bar{height:11px;border-radius:6px;background:#D9DCE6;margin:11px 0}
.row{display:flex;gap:10px;align-items:center;margin:9px 0}
.cell{height:22px;border-radius:5px;background:#E6E9F2}
.det{outline:3px solid var(--blue);background:rgba(85,128,255,.15)}
.det2{outline:3px solid var(--coral);background:rgba(255,138,115,.18)}
.card{background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.14);border-radius:22px;padding:30px}
.kv{display:flex;justify-content:space-between;font-size:26px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.12)}
.kv span:first-child{color:#aab0d6}.kv span:last-child{font-weight:600}
.sub{position:absolute;left:90px;right:90px;width:auto;margin:0 auto;background:rgba(0,0,0,.72);color:#fff;font-weight:600;font-size:42px;line-height:1.25;text-align:center;padding:18px 30px;border-radius:14px}
.chip{display:inline-block;border:2px solid var(--blue);color:#fff;background:rgba(85,128,255,.18);border-radius:12px;padding:10px 22px;font-weight:600;font-size:28px;margin:6px}
.star{color:#FFC94D;font-size:34px;letter-spacing:4px}
.arrow{width:0;height:0}
.dots{display:flex;gap:10px}.dots i{width:14px;height:14px;border-radius:50%;background:var(--coral)}
`;
const page = (w, h, body, extra = '') => `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}${extra}</style></head><body><div class="cv" style="width:${w}px;height:${h}px">${body}</div></body></html>`;
const logo = `<img class="logo" src="${LOGO_L}">`;
const paperLines = (n = 5, det = true) => {
  let s = ''; for (let i = 0; i < n; i++) s += `<div class="row"><div class="cell ${det && i % 2 === 0 ? 'det' : ''}" style="width:${28 + (i * 7) % 20}%"></div><div class="cell ${det && i % 3 === 0 ? 'det2' : ''}" style="width:${30 + (i * 11) % 25}%"></div><div class="cell" style="width:14%"></div></div>`; return s;
};
const ddt = (w = 360, rows = 6, rot = 0, det = true) => `<div class="paper" style="width:${w}px;transform:rotate(${rot}deg)"><div style="font-weight:700;font-size:21px;letter-spacing:1px;color:#23253C">DOCUMENTO DI TRASPORTO</div><div class="bar" style="width:55%"></div><div class="bar" style="width:38%"></div>${paperLines(rows, det)}<div class="bar" style="width:70%;margin-top:22px"></div></div>`;
const pile = () => `<div style="position:relative;width:520px;height:560px">
 <div style="position:absolute;left:10px;top:60px">${ddt(340, 5, -9, false)}</div>
 <div style="position:absolute;left:150px;top:10px">${ddt(340, 5, 7, false)}</div>
 <div style="position:absolute;left:70px;top:150px">${ddt(340, 6, -2, false)}</div></div>`;
const datacard = (rows, w = 380, title = 'Dati strutturati') => `<div class="card" style="width:${w}px"><div style="font-weight:700;font-size:26px;color:var(--green);margin-bottom:6px">✓ ${title}</div>${rows.map(r => `<div class="kv"><span>${r[0]}</span><span>${r[1]}</span></div>`).join('')}</div>`;
const flowArrow = (w = 110) => `<div style="display:flex;align-items:center;width:${w}px;justify-content:center"><svg width="${w}" height="40" viewBox="0 0 ${w} 40"><line x1="4" y1="20" x2="${w - 18}" y2="20" stroke="#FF8A73" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/><polygon points="${w - 22},8 ${w - 2},20 ${w - 22},32" fill="#FF8A73"/></svg></div>`;
const ddtRows = [['N. documento', 'DDT 2481'], ['Data', '12/03'], ['Fornitore', 'Esempio Srl'], ['Articolo', 'Vite M8 × 40'], ['Quantità', '500']];

const files = {}; // nome -> {w,h,html}
const add = (name, w, h, body, extra) => files[name] = { w, h, html: page(w, h, body, extra) };

// ---------- A01 video (4:5 + 1:1)
const subtitle = (t, bottom) => `<div class="sub" style="bottom:${bottom}px">${t}</div>`;
add('A01_frame1_hook_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:960px;font-size:84px">Quante ore al mese ricopi <span class="co">ordini a mano</span>?</div>
 <div style="position:absolute;left:260px;top:560px">${pile()}</div>${subtitle('Quante ore passa il tuo team a ricopiare ordini?', 120)}`);
add('A01_frame2_flusso_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:960px;font-size:70px">Retica legge il documento, <span class="co">qualunque layout</span></div>
 <div style="position:absolute;left:50px;top:520px;display:flex;align-items:center;gap:6px">${ddt(360, 6, 0, true)}${flowArrow(120)}${datacard(ddtRows, 440)}</div>${subtitle('Legge testi e tabelle, anche se il layout cambia', 120)}`);
add('A01_frame3_cta_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:210px;width:960px;font-size:84px">Restituisci tempo <span class="co">al tuo team</span></div>
 <div style="position:absolute;left:64px;top:620px"><span class="pill">RICHIEDI DEMO</span></div>
 <div style="position:absolute;left:64px;top:780px;font-size:34px;color:#c9ccea;width:900px">Calcola il tuo risparmio annuo su retica.ai</div>${subtitle('Calcola quanto puoi risparmiare con Retica', 120)}`);
add('A01_cover_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:960px;font-size:84px">Quante ore al mese ricopi <span class="co">ordini a mano</span>?</div>
 <div style="position:absolute;left:260px;top:560px">${pile()}</div>
 <div style="position:absolute;right:70px;bottom:220px;width:150px;height:150px;border-radius:50%;background:var(--coral);display:flex;align-items:center;justify-content:center"><div style="border-left:50px solid #fff;border-top:30px solid transparent;border-bottom:30px solid transparent;margin-left:14px"></div></div>
 <div style="position:absolute;left:64px;bottom:80px;font-size:30px;color:#c9ccea">0:30 · sottotitoli in italiano</div>`);
add('A01_cover_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:160px;width:950px;font-size:78px">Quante ore al mese ricopi <span class="co">ordini a mano</span>?</div>
 <div style="position:absolute;left:300px;top:470px;transform:scale(.8);transform-origin:top left">${pile()}</div>
 <div style="position:absolute;right:60px;bottom:60px;width:130px;height:130px;border-radius:50%;background:var(--coral);display:flex;align-items:center;justify-content:center"><div style="border-left:42px solid #fff;border-top:26px solid transparent;border-bottom:26px solid transparent;margin-left:12px"></div></div>`);

// ---------- A02 quote card (TLA)
add('A02_quote_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:950px;font-size:92px">Basta uno zero in più.</div>
 <div style="position:absolute;left:64px;top:480px;display:flex;gap:30px;align-items:stretch">
  <div class="paper" style="width:440px;padding:34px"><div style="font-size:22px;color:#888;font-weight:600;letter-spacing:1px">ORDINE (PDF)</div><div class="bar" style="width:70%"></div><div style="font-size:30px;margin-top:20px;font-weight:600;color:#23253C">Quantità: <span style="outline:3px solid var(--blue);padding:2px 10px;border-radius:6px">100 pz</span></div></div>
  <div style="display:flex;align-items:center"><svg width="60" height="40"><polygon points="0,6 40,20 0,34" fill="#FF8A73"/></svg></div>
  <div class="paper" style="width:440px;padding:34px;background:#fff"><div style="font-size:22px;color:#888;font-weight:600;letter-spacing:1px">GESTIONALE (DIGITATO)</div><div class="bar" style="width:70%"></div><div style="font-size:30px;margin-top:20px;font-weight:600;color:#23253C">Quantità: <span style="outline:3px solid #F4524D;background:rgba(244,82,77,.14);padding:2px 10px;border-radius:6px;color:#F4524D">1000 pz</span></div></div>
 </div>
 <div style="position:absolute;left:64px;top:790px;width:950px;font-size:40px;line-height:1.35;color:#d9dcf5;font-weight:400">Il lavoro di un copia-incolla non dovrebbe costare un errore.</div>
 <div style="position:absolute;left:64px;bottom:64px;font-size:30px;color:#9fa4cf">retica.ai</div>`);

// ---------- A03 document ad (3 pagine)
const steps = [['1', 'Identifica', 'il blocco di testo da scansionare'], ['2', 'Etichetta', 'l\'AI legge e associa un\'etichetta ad ogni testo'], ['3', 'Salva', 'la posizione e il contenuto del blocco'], ['4', 'Crea il modello', 'del documento dai blocchi salvati']];
add('A03_pagina1_copertina_4x5', 1080, 1350, `${logo}
 <div style="position:absolute;left:64px;top:190px;font-size:28px;letter-spacing:4px;color:var(--coral);font-weight:600">GUIDA GRATUITA</div>
 <div class="h" style="position:absolute;left:64px;top:250px;width:950px;font-size:92px">Automatizza <span class="co">DDT e ordini</span> in 4 passi</div>
 <div style="position:absolute;left:64px;top:760px;display:flex;gap:30px;align-items:center">${ddt(300, 5, -4, true)}${flowArrow(90)}${datacard([['DDT', '2481'], ['Qtà', '500']], 330)}</div>
 <div style="position:absolute;left:64px;bottom:70px;font-size:30px;color:#c9ccea">Retica · lettore documenti con intelligenza artificiale</div>`);
add('A03_pagina2_4passi_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:950px;font-size:68px">Come Retica impara <span class="co">il tuo documento</span></div>
 <div style="position:absolute;left:64px;top:400px;width:952px">${steps.map(s => `<div class="card" style="display:flex;gap:28px;align-items:center;margin-bottom:22px;padding:26px 30px"><div style="width:76px;height:76px;border-radius:50%;background:var(--blue);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:38px;flex:none">${s[0]}</div><div style="font-size:34px;line-height:1.25"><b>${s[1]}</b> ${s[2]}</div></div>`).join('')}</div>`);
add('A03_pagina3_cta_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:950px;font-size:74px">Nella guida trovi</div>
 <div style="position:absolute;left:64px;top:340px;width:950px;font-size:38px;line-height:1.5;color:#e4e6fa">
  <div style="margin-bottom:20px"><span class="co">✓</span> Quali documenti puoi automatizzare</div>
  <div style="margin-bottom:20px"><span class="co">✓</span> Come i dati arrivano nel tuo gestionale</div>
  <div style="margin-bottom:20px"><span class="co">✓</span> Cosa cambia per il tuo team</div>
  <div style="margin-bottom:20px"><span class="co">✓</span> Come partire senza fermare le attività</div></div>
 <div style="position:absolute;left:64px;top:900px"><span class="pill">SCARICA LA GUIDA</span></div>
 <div style="position:absolute;left:64px;top:1030px;font-size:28px;color:#9fa4cf">Indice indicativo — contenuti da definire con il cliente</div>`);

// ---------- A04 calcolatore
add('A04_calcolatore_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:160px;width:950px;font-size:76px">Quanto ti costa inserire <span class="co">documenti a mano</span>?</div>
 <div class="paper" style="position:absolute;left:64px;top:470px;width:952px;padding:40px;color:#23253C">
  <div style="font-size:26px;color:#716C80;font-weight:500">Documenti inseriti manualmente ogni mese</div><div style="height:64px;border:2px solid #D3D6E6;border-radius:12px;margin:10px 0 26px"></div>
  <div style="font-size:26px;color:#716C80;font-weight:500">Tempo medio di inserimento per documento</div><div style="height:64px;border:2px solid #D3D6E6;border-radius:12px;margin:10px 0 30px"></div>
  <div style="display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:24px;color:#716C80">Risparmio annuo con Retica</div><div style="font-size:60px;font-weight:700;color:#FF8A73">€ … / anno</div></div><span class="pill b" style="font-size:26px;padding:20px 36px">CALCOLA</span></div></div>`);

// ---------- A05 carosello 5 card
const cardsHTML = byId.A05.cards;
const cardBody = [
  `<div class="h" style="position:absolute;left:64px;top:300px;width:950px;font-size:100px">${cardsHTML[0].replace('Il risultato no.', '<span class="co">Il risultato no.</span>')}</div><div style="position:absolute;left:64px;bottom:90px;font-size:34px;color:#c9ccea">Scorri →</div>`,
  `<div style="position:absolute;left:64px;top:170px;font-size:28px;letter-spacing:4px;color:var(--coral);font-weight:600">01 · ORDINI</div><div class="h" style="position:absolute;left:64px;top:225px;width:950px;font-size:76px">${cardsHTML[1]}</div><div style="position:absolute;left:100px;top:470px;display:flex;align-items:center;gap:6px">${ddt(380, 6, 0, true)}${flowArrow(110)}${datacard([['Cliente', 'Esempio Spa'], ['Ordine', 'OA 7742'], ['Righe', '14']], 400)}</div>`,
  `<div style="position:absolute;left:64px;top:170px;font-size:28px;letter-spacing:4px;color:var(--coral);font-weight:600">02 · TRASPORTO</div><div class="h" style="position:absolute;left:64px;top:225px;width:950px;font-size:76px">${cardsHTML[2]}</div><div style="position:absolute;left:100px;top:470px;display:flex;align-items:center;gap:6px">${ddt(380, 7, 0, true)}${flowArrow(110)}${datacard([['DDT', '2481'], ['Fornitore', 'Esempio Srl'], ['Righe', '23']], 400)}</div>`,
  `<div style="position:absolute;left:64px;top:170px;font-size:28px;letter-spacing:4px;color:var(--coral);font-weight:600">03 · FATTURE</div><div class="h" style="position:absolute;left:64px;top:225px;width:950px;font-size:76px">${cardsHTML[3]}</div><div style="position:absolute;left:100px;top:470px;display:flex;align-items:center;gap:6px">${ddt(380, 5, 0, true).replace('DOCUMENTO DI TRASPORTO', 'FATTURA')}${flowArrow(110)}${datacard([['Documento', 'Fattura'], ['Importo', '… €'], ['Scadenza', '…']], 400)}</div>`,
  `<div class="h" style="position:absolute;left:64px;top:280px;width:950px;font-size:92px">${cardsHTML[4].replace('tuoi documenti', '<span class="co">tuoi documenti</span>')}</div><div style="position:absolute;left:64px;top:700px"><span class="pill">RICHIEDI DEMO</span></div>`,
];
cardBody.forEach((b, i) => add(`A05_card${i + 1}_1x1`, 1080, 1080, logo + b));

// ---------- A06 integrazione
add('A06_integrazione_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:950px;font-size:78px">Dal documento al tuo <span class="co">ERP</span>, senza trascrizioni</div>
 <div style="position:absolute;left:64px;top:420px;width:952px;display:flex;flex-direction:column;align-items:center;gap:0">
  <div style="display:flex;align-items:center;gap:26px">${ddt(300, 4, 0, true)}<div style="font-size:30px;color:#c9ccea;width:330px;line-height:1.3">PDF, immagini, scansioni<br><span style="color:var(--coral);font-weight:600">importati via API o FTP</span></div></div>
  <svg width="40" height="70" viewBox="0 0 40 70"><line x1="20" y1="4" x2="20" y2="48" stroke="#FF8A73" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/><polygon points="8,46 20,66 32,46" fill="#FF8A73"/></svg>
  <div class="card" style="width:640px;text-align:center;padding:26px;border-color:var(--blue)"><img src="${LOGO_L}" style="height:64px"><div style="font-size:28px;color:#c9ccea;margin-top:10px">legge, etichetta, valida</div></div>
  <svg width="40" height="70" viewBox="0 0 40 70"><line x1="20" y1="4" x2="20" y2="48" stroke="#FF8A73" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/><polygon points="8,46 20,66 32,46" fill="#FF8A73"/></svg>
  <div style="font-size:28px;color:var(--coral);font-weight:600;margin:-6px 0 12px">CSV · XML · JSON</div>
  <div style="display:flex;gap:18px;width:100%">${['ERP', 'CRM', 'Gestionale'].map(x => `<div class="card" style="flex:1;padding:22px 10px;text-align:center;font-weight:600;font-size:32px;border-color:var(--green)">${x}</div>`).join('')}</div></div>
 `);

// ---------- A07 DDT before/after
add('A07_ddt_prima_dopo_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:160px;width:950px;font-size:72px">DDT nel gestionale, <span class="co">senza riscrivere nulla</span></div>
 <div style="position:absolute;left:64px;top:440px;width:460px"><div style="font-size:26px;letter-spacing:3px;color:#aab0d6;font-weight:600;margin-bottom:18px">OGGI</div>${ddt(400, 6, -3, false)}<div style="font-size:30px;margin-top:24px;color:#d9dcf5">Riga per riga, a mano</div></div>
 <div style="position:absolute;left:560px;top:440px;width:460px"><div style="font-size:26px;letter-spacing:3px;color:var(--green);font-weight:600;margin-bottom:18px">CON RETICA</div>${datacard([['Riga 1', 'Vite M8 × 40'], ['Riga 2', 'Dado M8'], ['Riga 3', 'Rondella'], ['Riga 4', '…']], 440, 'Importato')}<div style="font-size:30px;margin-top:24px;color:#d9dcf5">Nel gestionale in automatico</div></div>`);

// ---------- A08 testimonial
add('A08_testimonianza_4x5', 1080, 1350, `${logo}
 <div style="position:absolute;left:64px;top:170px;font-size:150px;font-weight:800;color:var(--coral);line-height:1">2.500</div>
 <div style="position:absolute;left:64px;top:330px;font-size:40px;font-weight:600">ordini in PDF ogni mese</div>
 <div class="card" style="position:absolute;left:64px;top:450px;width:952px;padding:44px"><div style="font-size:72px;color:var(--coral);line-height:.6">“</div>
  <div style="font-size:36px;line-height:1.4;font-weight:500">Ogni mese riceviamo circa 2.500 ordini in PDF dai clienti, che venivano letti, verificati e inseriti manualmente nei nostri sistemi.</div>
  <div style="font-size:36px;line-height:1.4;font-weight:500;margin-top:26px">…un risparmio equivalente a una persona in ufficio.</div></div>
 <div style="position:absolute;left:64px;top:1070px;display:flex;gap:24px;align-items:center"><div style="width:90px;height:90px;border-radius:50%;background:var(--purple);display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:700">A</div><div><div style="font-size:32px;font-weight:600">Andrea Michelin</div><div style="font-size:26px;color:#aab0d6">EDP Manager · Gruppo Borghi Spa</div><div class="star" style="font-size:28px">★★★★★</div></div></div>`);

// ---------- A09 numeri
add('A09_numeri_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:160px;width:950px;font-size:64px">Un punto di riferimento per l'estrazione di dati dai documenti</div>
 <div style="position:absolute;left:64px;top:405px;width:952px;display:flex;flex-direction:column;gap:16px">
 ${[['6000+', 'scansioni giornaliere'], ['124', 'clienti attivi'], ['23', 'rivenditori e partner']].map(n => `<div class="card" style="display:flex;align-items:baseline;gap:30px;padding:22px 34px"><div style="font-size:104px;font-weight:800;color:var(--coral);min-width:360px;line-height:1.05">${n[0]}</div><div style="font-size:38px;font-weight:500">${n[1]}</div></div>`).join('')}</div>
 <div style="position:absolute;left:64px;bottom:56px;width:952px"><span class="star">★★★★★</span><div style="font-size:26px;color:#c9ccea;margin-top:4px">Recensioni di IT manager, responsabili EDP e CEO</div></div>`);

// ---------- A10 conversation
add('A10_conversation_4x5', 1080, 1350, `<div style="position:absolute;inset:0;background:#F3F2EF"></div>
 <div style="position:absolute;left:50px;top:50px;width:980px;height:1250px;background:#fff;border-radius:22px;box-shadow:0 10px 40px rgba(0,0,0,.12);color:#191919;overflow:hidden">
  <div style="display:flex;align-items:center;gap:22px;padding:28px 36px;border-bottom:2px solid #E6E6E6"><img src="${AVATAR}" style="width:90px;height:90px;border-radius:50%"><div><div style="font-size:34px;font-weight:600">[Nome Cognome] · Retica</div><div style="font-size:24px;color:#666">Messaggio sponsorizzato</div></div></div>
  <div style="padding:36px"><div style="background:#F1F5F9;border-radius:6px 26px 26px 26px;padding:30px 34px;font-size:32px;line-height:1.45;color:#191919">${byId.A10.intro_A.replace('{FirstName}', 'Marco').replace('Reggiolo (RE).', 'Reggiolo (RE).<br><br>').replace('E ti seguiamo', '<br><br>E ti seguiamo')}</div>
  <div style="margin-top:34px;display:flex;flex-direction:column;gap:18px;align-items:flex-start">${['Prenota la demo', 'Calcola il risparmio', 'Parla con un esperto'].map(b => `<div style="border:3px solid #0A66C2;color:#0A66C2;border-radius:999px;padding:18px 44px;font-size:30px;font-weight:600">${b}</div>`).join('')}</div>
  <div style="font-size:22px;color:#888;margin-top:40px">Mockup: nome del mittente e testo da confermare con il cliente. {FirstName} sostituito da "Marco" solo come esempio.</div></div></div>`);

// ---------- Feed frame
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
function feed(name, adId, imgFile, imgW, imgH, opts = {}) {
  const a = byId[adId];
  const hook = esc(a.hook_A);
  const W = 1120;
  const imgHt = Math.round(W * imgH / imgW);
  const author = opts.author || 'Retica';
  const avatar = opts.avatarHTML || `<img src="${AVATAR}" style="width:112px;height:112px;border-radius:50%">`;
  const sub = opts.sub || 'Sponsorizzato';
  const media = opts.mediaHTML || `<img src="file://${OUT}/${imgFile}" style="display:block;width:${W}px;height:${imgHt}px">`;
  const bar = opts.noBar ? '' : `<div style="background:#EEF3F8;padding:26px 36px;display:flex;align-items:center;justify-content:space-between;gap:24px"><div><div style="font-size:34px;font-weight:600;color:#191919;line-height:1.25;max-width:700px">${esc(a.headline_A)}</div><div style="font-size:26px;color:#666;margin-top:6px">retica.ai</div></div><div style="border:3px solid #0A66C2;color:#0A66C2;border-radius:999px;padding:16px 36px;font-size:30px;font-weight:600;white-space:nowrap">${esc(opts.cta || a.cta)}</div></div>`;
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}body{background:#F3F2EF;color:#191919}</style></head><body><div style="width:${W + 80}px;padding:40px;background:#F3F2EF">
  <div style="width:${W}px;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 0 0 2px #E0DFDC">
   <div style="display:flex;align-items:center;gap:24px;padding:30px 36px 20px">${avatar}<div style="flex:1"><div style="font-size:38px;font-weight:600">${esc(author)}</div><div style="font-size:26px;color:#666">${esc(sub)} · 🌐</div></div><div style="font-size:44px;color:#666;letter-spacing:4px">···</div></div>
   <div style="padding:0 36px 26px;font-size:34px;line-height:1.45">${hook}… <span style="color:#666">altro</span></div>
   ${media}${bar}
   <div style="display:flex;justify-content:space-around;padding:26px 20px;font-size:28px;color:#666;font-weight:600;border-top:2px solid #E6E6E6"><span>👍 Consiglia</span><span>💬 Commenta</span><span>↻ Diffondi</span><span>➤ Invia</span></div>
  </div></div></body></html>`;
  files[name] = { w: W + 80, h: 10, html, full: true };
}
feed('A01_feed', 'A01', 'A01_cover_4x5.png', 1080, 1350);
feed('A02_feed', 'A02', 'A02_quote_1x1.png', 1080, 1080, { author: '[Nome Cognome] · Founder, Retica', sub: 'Sponsorizzato · [DA CONFERMARE: referente]', avatarHTML: '<div style="width:112px;height:112px;border-radius:50%;background:#C9CED6;display:flex;align-items:center;justify-content:center;font-size:60px;color:#fff">👤</div>' });
feed('A03_feed', 'A03', 'A03_pagina1_copertina_4x5.png', 1080, 1350, { cta: 'Scarica' });
feed('A04_feed', 'A04', 'A04_calcolatore_1x1.png', 1080, 1080);
// carosello: 1 card + peek
{
  const a = byId.A05; const W = 1120;
  const strip = [1, 2, 3, 4, 5].map(i => `<img src="file://${OUT}/A05_card${i}_1x1.png" style="width:1000px;height:1000px;margin-right:16px;flex:none">`).join('');
  feed('A05_feed', 'A05', '', 1, 1, { noBar: false, mediaHTML: `<div style="width:${W}px;height:1000px;overflow:hidden;display:flex">${strip}</div><div style="background:#fff;padding:14px;text-align:center;font-size:24px;color:#666">● ○ ○ ○ ○ &nbsp; carosello · 5 card</div>` });
}
feed('A06_feed', 'A06', 'A06_integrazione_4x5.png', 1080, 1350);
feed('A07_feed', 'A07', 'A07_ddt_prima_dopo_1x1.png', 1080, 1080);
feed('A08_feed', 'A08', 'A08_testimonianza_4x5.png', 1080, 1350);
feed('A09_feed', 'A09', 'A09_numeri_1x1.png', 1080, 1080);

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ deviceScaleFactor: 1 });
  const order = Object.keys(files);
  // 1) creatività (non feed), 2) feed
  for (const pass of [false, true]) {
    for (const n of order) {
      const f = files[n]; if (!!f.full !== pass) continue;
      const fp = path.join(HTML, n + '.html'); fs.writeFileSync(fp, f.html);
      const p = await ctx.newPage(); await p.setViewportSize({ width: f.w, height: f.h });
      await p.goto('file://' + fp); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250);
      if (f.full) await p.screenshot({ path: path.join(OUT, n + '.png'), fullPage: true });
      else await p.screenshot({ path: path.join(OUT, n + '.png'), clip: { x: 0, y: 0, width: f.w, height: f.h } });
      await p.close(); console.log('ok', n);
    }
  }
  await b.close();
})();
