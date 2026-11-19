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

// ---------- A01 immagine singola (post sponsorizzato) — DDT, senza video
add('A01_static_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:960px;font-size:84px">Quante <span class="co">righe di DDT</span> ricopi ogni giorno?</div>
 <div style="position:absolute;left:260px;top:560px">${pile()}</div>
 <div style="position:absolute;left:64px;bottom:90px;font-size:34px;color:#c9ccea;width:950px;line-height:1.35">Retica legge i DDT e li porta nel gestionale.</div>`);

// ---------- A02 quote card (TLA) — unità di misura
add('A02_quote_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:950px;font-size:96px">10 colli o <span class="co">120 pezzi</span>?</div>
 <div style="position:absolute;left:64px;top:420px;display:flex;gap:30px;align-items:stretch">
  <div class="paper" style="width:440px;padding:34px"><div style="font-size:22px;color:#888;font-weight:600;letter-spacing:1px">DDT DEL FORNITORE</div><div class="bar" style="width:70%"></div><div style="font-size:30px;margin-top:20px;font-weight:600;color:#23253C;line-height:1.5">Quantità: <span style="outline:3px solid var(--blue);padding:2px 10px;border-radius:6px">10 colli</span><br>Confezione: <span style="outline:3px solid var(--coral);padding:2px 10px;border-radius:6px">12 pz</span></div></div>
  <div style="display:flex;align-items:center"><svg width="60" height="40"><polygon points="0,6 40,20 0,34" fill="#FF8A73"/></svg></div>
  <div class="paper" style="width:440px;padding:34px"><div style="font-size:22px;color:#888;font-weight:600;letter-spacing:1px">GESTIONALE (A MANO)</div><div class="bar" style="width:70%"></div><div style="font-size:30px;margin-top:20px;font-weight:600;color:#23253C;line-height:1.5">Quantità: <span style="outline:3px solid #F4524D;background:rgba(244,82,77,.14);padding:2px 10px;border-radius:6px;color:#F4524D">? pz</span><br>Unità: <span style="color:#716C80">pezzi</span></div></div>
 </div>
 <div style="position:absolute;left:64px;top:780px;width:950px;font-size:40px;line-height:1.35;color:#d9dcf5;font-weight:400">Ogni fornitore scrive l’unità di misura a modo suo.</div>
 <div style="position:absolute;left:64px;bottom:64px;font-size:30px;color:#9fa4cf">retica.ai</div>`);

// ---------- A04 listino fornitori
const listino = (w, rows, rot) => ddt(w, rows, rot, true).replace('DOCUMENTO DI TRASPORTO', 'LISTINO FORNITORE');
add('A04_listino_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:160px;width:950px;font-size:70px">Il listino arriva in PDF. Il gestionale vuole <span class="co">dati</span>.</div>
 <div style="position:absolute;left:64px;top:500px;display:flex;align-items:center;gap:6px">${listino(380, 7, 0)}${flowArrow(110)}${datacard([['Codice', 'VT-M8-40'], ['Descrizione', 'Vite M8 × 40'], ['Prezzo', '0,12 €'], ['Unità', 'CT · 12 pz']], 440)}</div>
 <div style="position:absolute;left:64px;bottom:70px;font-size:30px;color:#c9ccea">Codice articolo, descrizione, prezzo, unità di misura o confezione</div>`);

// ---------- A05 carosello 5 card
const cardsHTML = byId.A05.cards;
const card = (kick, title, rows, label) => `<div style="position:absolute;left:64px;top:170px;font-size:28px;letter-spacing:4px;color:var(--coral);font-weight:600">${kick}</div><div class="h" style="position:absolute;left:64px;top:225px;width:950px;font-size:76px">${title}</div><div style="position:absolute;left:100px;top:490px;display:flex;align-items:center;gap:6px">${label ? ddt(380, 6, 0, true).replace('DOCUMENTO DI TRASPORTO', label) : ddt(380, 6, 0, true)}${flowArrow(110)}${datacard(rows, 400)}</div>`;
const cardBody = [
  `<div class="h" style="position:absolute;left:64px;top:300px;width:950px;font-size:100px">Il DDT, <span class="co">riga per riga</span></div><div style="position:absolute;left:64px;bottom:90px;font-size:34px;color:#c9ccea">Scorri →</div>`,
  card('01 · RIGHE', cardsHTML[1], [['Codice', 'VT-M8-40'], ['Descrizione', 'Vite M8 × 40'], ['Quantità', '10']]),
  card('02 · UNITÀ', cardsHTML[2], [['Quantità', '10'], ['Unità', 'colli (CT)'], ['Confezione', '12 pz']]),
  card('03 · PREZZI', cardsHTML[3], [['Codice', 'VT-M8-40'], ['Prezzo', '0,12 €'], ['Unità', 'CT · 12 pz']], 'LISTINO FORNITORE'),
  `<div class="h" style="position:absolute;left:64px;top:280px;width:950px;font-size:92px">Prova Retica sui <span class="co">tuoi DDT</span></div><div style="position:absolute;left:64px;top:700px"><span class="pill">RICHIEDI DEMO</span></div>`,
];
cardBody.forEach((b, i) => add(`A05_card${i + 1}_1x1`, 1080, 1080, logo + b));

// ---------- A06 integrazione
const vArrow = `<svg width="40" height="70" viewBox="0 0 40 70"><line x1="20" y1="4" x2="20" y2="48" stroke="#FF8A73" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/><polygon points="8,46 20,66 32,46" fill="#FF8A73"/></svg>`;
add('A06_integrazione_4x5', 1080, 1350, `${logo}
 <div class="h" style="position:absolute;left:64px;top:170px;width:950px;font-size:78px">Dal DDT al tuo <span class="co">ERP</span>, senza trascrizioni</div>
 <div style="position:absolute;left:64px;top:420px;width:952px;display:flex;flex-direction:column;align-items:center;gap:0">
  <div style="display:flex;align-items:center;gap:26px">${ddt(300, 4, 0, true)}<div style="font-size:30px;color:#c9ccea;width:330px;line-height:1.3">PDF, immagini, scansioni<br><span style="color:var(--coral);font-weight:600">importati via API o FTP</span></div></div>
  ${vArrow}
  <div class="card" style="width:640px;text-align:center;padding:26px;border-color:var(--blue)"><img src="${LOGO_L}" style="height:64px"><div style="font-size:28px;color:#c9ccea;margin-top:10px">legge, etichetta, valida</div></div>
  ${vArrow}
  <div style="font-size:28px;color:var(--coral);font-weight:600;margin:-6px 0 12px">CSV · XML · JSON</div>
  <div style="display:flex;gap:18px;width:100%">${['ERP', 'Gestionale', 'Magazzino'].map(x => `<div class="card" style="flex:1;padding:22px 10px;text-align:center;font-weight:600;font-size:32px;border-color:var(--green)">${x}</div>`).join('')}</div></div>
 `);

// ---------- A07 DDT prima/dopo con unità
add('A07_ddt_prima_dopo_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:160px;width:950px;font-size:68px">Righe e unità di misura del DDT, <span class="co">nel gestionale</span></div>
 <div style="position:absolute;left:64px;top:470px;width:460px"><div style="font-size:26px;letter-spacing:3px;color:#aab0d6;font-weight:600;margin-bottom:18px">OGGI</div>${ddt(400, 6, -3, false)}<div style="font-size:30px;margin-top:24px;color:#d9dcf5">Riga per riga, a mano</div></div>
 <div style="position:absolute;left:560px;top:470px;width:460px"><div style="font-size:26px;letter-spacing:3px;color:var(--green);font-weight:600;margin-bottom:18px">CON RETICA</div>${datacard([['Riga 1', 'Vite M8 · 10 CT'], ['Riga 2', 'Dado M8 · 5 CT'], ['Riga 3', 'Rondella · 2 PLT'], ['Riga 4', '…']], 440, 'Importato')}<div style="font-size:30px;margin-top:24px;color:#d9dcf5">Righe e unità nel gestionale</div></div>`);

// ---------- A08 testimonianza Carraro (DDT in SAP)
add('A08_testimonianza_4x5', 1080, 1350, `${logo}
 <div style="position:absolute;left:64px;top:180px;font-size:120px;font-weight:800;color:var(--coral);line-height:1">DDT → ERP</div>
 <div style="position:absolute;left:64px;top:320px;font-size:38px;font-weight:600">Divisione ricambi · Carraro S.p.a.</div>
 <div class="card" style="position:absolute;left:64px;top:450px;width:952px;padding:44px"><div style="font-size:72px;color:var(--coral);line-height:.6">“</div>
  <div style="font-size:35px;line-height:1.4;font-weight:500">…l’inserimento dei DDT nel nostro ERP (SAP) richiedeva molto tempo ed era soggetto a frequenti errori.</div>
  <div style="font-size:35px;line-height:1.4;font-weight:500;margin-top:26px">…drastico abbattimento dei tempi di inserimento e degli errori umani.</div></div>
 <div style="position:absolute;left:64px;top:1070px;display:flex;gap:24px;align-items:center"><div style="width:90px;height:90px;border-radius:50%;background:var(--purple);display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:700">D</div><div><div style="font-size:32px;font-weight:600">Dario Mazzocca</div><div style="font-size:26px;color:#aab0d6">IT Manager · Carraro S.p.a.</div><div class="star" style="font-size:28px">★★★★★</div></div></div>`);

// ---------- A09 logistica: Le Messaggerie Nazionali + numeri
add('A09_numeri_1x1', 1080, 1080, `${logo}
 <div class="h" style="position:absolute;left:64px;top:160px;width:950px;font-size:66px">Logistica: meno data entry, <span class="co">magazzino più efficiente</span></div>
 <div class="card" style="position:absolute;left:64px;top:430px;width:952px;padding:36px"><div style="font-size:60px;color:var(--coral);line-height:.5">“</div>
  <div style="font-size:33px;line-height:1.4;font-weight:500">Nel nostro settore la velocità e la precisione sono fondamentali.</div>
  <div style="font-size:33px;line-height:1.4;font-weight:500;margin-top:16px">…migliorare l’efficienza del magazzino e offrire un servizio ancora più rapido ai nostri clienti.</div>
  <div style="font-size:26px;color:#aab0d6;margin-top:20px">Federico Gatti, IT Manager · Le Messaggerie Nazionali</div></div>
 <div style="position:absolute;left:64px;top:860px;display:flex;gap:24px;width:952px">${[['6000+', 'scansioni al giorno'], ['124', 'clienti attivi'], ['23', 'rivenditori e partner']].map(n => `<div class="card" style="flex:1;padding:20px 22px"><div style="font-size:60px;font-weight:800;color:var(--coral);line-height:1.05">${n[0]}</div><div style="font-size:24px;font-weight:500;color:#d9dcf5">${n[1]}</div></div>`).join('')}</div>`);

// ---------- A10 conversation
add('A10_conversation_4x5', 1080, 1350, `<div style="position:absolute;inset:0;background:#F3F2EF"></div>
 <div style="position:absolute;left:50px;top:50px;width:980px;height:1250px;background:#fff;border-radius:22px;box-shadow:0 10px 40px rgba(0,0,0,.12);color:#191919;overflow:hidden">
  <div style="display:flex;align-items:center;gap:22px;padding:28px 36px;border-bottom:2px solid #E6E6E6"><img src="${AVATAR}" style="width:90px;height:90px;border-radius:50%"><div><div style="font-size:34px;font-weight:600">[Nome Cognome] · Retica</div><div style="font-size:24px;color:#666">Messaggio sponsorizzato</div></div></div>
  <div style="padding:36px"><div style="background:#F1F5F9;border-radius:6px 26px 26px 26px;padding:30px 34px;font-size:32px;line-height:1.45;color:#191919">${byId.A10.intro_A.replace('{FirstName}', 'Marco').replace('Reggiolo (RE).', 'Reggiolo (RE).<br><br>').replace('E ti seguiamo', '<br><br>E ti seguiamo')}</div>
  <div style="margin-top:34px;display:flex;flex-direction:column;gap:18px;align-items:flex-start">${['Prenota la demo', 'Parla con un esperto'].map(b => `<div style="border:3px solid #0A66C2;color:#0A66C2;border-radius:999px;padding:18px 44px;font-size:30px;font-weight:600">${b}</div>`).join('')}</div>
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
feed('A01_feed', 'A01', 'A01_static_4x5.png', 1080, 1350);
feed('A02_feed', 'A02', 'A02_quote_1x1.png', 1080, 1080, { author: '[Nome Cognome] · Founder, Retica', sub: 'Sponsorizzato · [DA CONFERMARE: referente]', avatarHTML: '<div style="width:112px;height:112px;border-radius:50%;background:#C9CED6;display:flex;align-items:center;justify-content:center;font-size:60px;color:#fff">👤</div>' });
feed('A04_feed', 'A04', 'A04_listino_1x1.png', 1080, 1080);
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
