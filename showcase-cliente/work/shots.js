// Cattura DPR2 delle inquadrature del montaggio (Atto 2). Output: cap/shots/<id>/NNNN.jpg a 60 fps
const { chromium } = require('playwright');
const fs = require('fs');
const URL = 'https://inprotec-homepage.vercel.app';
const FPS = 60;
const inOut = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
const outCubic = t => 1 - Math.pow(1 - t, 3);
const outQuart = t => 1 - Math.pow(1 - t, 4);

// id, y0, y1, frames, easing
const SCROLL_SHOTS = [
  ['s01', 9000, 9350, 60, inOut],
  ['s02', 9350, 9350, 60, inOut],
  ['s03', 9650, 10650, 60, outQuart],
  ['s07', 11950, 11950, 30, inOut],
  ['s08', 11950, 11950, 30, inOut],
  ['s09', 12100, 12500, 30, inOut],
  ['s10', 12600, 12600, 30, inOut],
  ['s11', 12700, 13250, 30, outCubic],
  ['s12', 13300, 13500, 30, inOut],
  ['s13', 13900, 13900, 30, inOut],
  ['s14', 13900, 13900, 30, inOut],
];

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.goto(URL, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(6000);
  const total = await p.evaluate(() => document.documentElement.scrollHeight - innerHeight);
  // prewarm: attiva le animazioni on-scroll
  for (let y = 8000; y <= total; y += 500) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(250); }
  await p.waitForTimeout(800);

  const only = process.argv.slice(2);
  for (const [id, y0, y1, n, ez] of SCROLL_SHOTS) {
    if (only.length && !only.includes(id)) continue;
    const dir = `cap/shots/${id}`;
    fs.mkdirSync(dir, { recursive: true });
    await p.evaluate(y => scrollTo(0, y), y0);
    await p.waitForTimeout(900);
    for (let i = 0; i < n; i++) {
      const u = n > 1 ? i / (n - 1) : 0;
      await p.evaluate(y => scrollTo(0, y), y0 + (y1 - y0) * ez(u));
      await p.waitForTimeout(30);
      await p.screenshot({ path: `${dir}/${String(i).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
    }
    console.log('done', id);
  }

  // Screencast in tempo reale: marquee (s04) e interazione tab (s05/s06)
  async function screencast(id, setup, actions, dur) {
    const dir = `cap/shots/${id}`;
    fs.mkdirSync(dir, { recursive: true });
    await setup();
    const client = await ctx.newCDPSession(p);
    const frames = [];
    client.on('Page.screencastFrame', async ({ data, metadata, sessionId }) => {
      frames.push({ t: metadata.timestamp, data });
      try { await client.send('Page.screencastFrameAck', { sessionId }); } catch (e) {}
    });
    await client.send('Page.startScreencast', { format: 'jpeg', quality: 92, maxWidth: 2880, maxHeight: 1800, everyNthFrame: 1 });
    const t0 = Date.now();
    await actions(() => (Date.now() - t0) / 1000);
    while ((Date.now() - t0) / 1000 < dur) await p.waitForTimeout(20);
    await client.send('Page.stopScreencast');
    await client.detach();
    if (!frames.length) { console.log('no frames', id); return; }
    const ts0 = frames[0].t;
    const N = Math.floor((frames[frames.length - 1].t - ts0) * FPS);
    let j = 0;
    for (let i = 0; i < N; i++) {
      const tt = ts0 + i / FPS;
      while (j + 1 < frames.length && frames[j + 1].t <= tt) j++;
      fs.writeFileSync(`${dir}/${String(i).padStart(4, '0')}.jpg`, Buffer.from(frames[j].data, 'base64'));
    }
    console.log('screencast', id, frames.length, 'raw ->', N, 'frames');
  }

  if (!only.length || only.includes('s04')) {
    await screencast('s04', async () => { await p.evaluate(y => scrollTo(0, y), 10650); await p.waitForTimeout(1200); }, async () => {}, 1.6);
  }
  if (!only.length || only.includes('s05')) {
    const top = await p.evaluate(() => document.getElementById('industries').getBoundingClientRect().top + scrollY);
    const tabs = await p.$$('#industries button');
    await screencast('s05', async () => {
      await p.evaluate(y => scrollTo(0, y), top + 330); await p.waitForTimeout(1500);
      await tabs[0].click(); await p.waitForTimeout(1200);
    }, async el => {
      const wait = async t => { while (el() < t) await p.waitForTimeout(10); };
      await wait(0.4); await tabs[1].click();
      await wait(1.6); await tabs[2].click();
    }, 3.0);
  }
  await b.close();
})();
