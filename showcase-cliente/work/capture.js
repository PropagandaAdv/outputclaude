const { chromium } = require('playwright');
const fs = require('fs');
const URL = 'https://inprotec-homepage.vercel.app';
const ease = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
const FPS = 60;

async function grab(p, dir, n, setY, wait = 45) {
  fs.mkdirSync(dir, { recursive: true });
  for (let i = 0; i < n; i++) {
    await setY(i / (n - 1));
    await p.waitForTimeout(wait);
    await p.screenshot({ path: `${dir}/${String(i).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
  }
}

(async () => {
  const b = await chromium.launch();
  const mk = async (vw, vh, dsf, mobile) => {
    const c = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dsf, isMobile: !!mobile, hasTouch: !!mobile });
    const p = await c.newPage();
    await p.goto(URL, { waitUntil: 'domcontentloaded' });
    await p.waitForTimeout(6000);
    return p;
  };
  const mode = process.argv[2];

  if (mode === 'hero') {
    const p = await mk(1440, 900, 1);
    const H = await p.evaluate(() => document.getElementById('hero').offsetHeight - innerHeight);
    console.log('H', H);
    const N = 11 * FPS, HOLD = Math.round(0.9 * FPS);
    await grab(p, 'cap/hero', N + HOLD, async u => {
      const t = Math.min(1, u * (N + HOLD - 1) / (N - 1));
      await p.evaluate(y => scrollTo(0, y), (0.08 * t + 0.92 * ease(t)) * H);
    });
  }

  if (mode === 'site') {
    const p = await mk(1440, 900, 1);
    const total = await p.evaluate(() => document.documentElement.scrollHeight - innerHeight);
    const start = await p.evaluate(() => document.getElementById('hero').offsetHeight);
    const y0 = start - 900;
    await p.evaluate(y => scrollTo(0, y), y0);
    await p.waitForTimeout(1500);
    await grab(p, 'cap/site', 14 * FPS, async u => {
      await p.evaluate(y => scrollTo(0, y), y0 + (total - y0) * (0.1 * u + 0.9 * ease(u)));
    }, 40);
  }

  if (mode === 'tabs') {
    const p = await mk(1440, 900, 1);
    const top = await p.evaluate(() => document.getElementById('industries').getBoundingClientRect().top + scrollY);
    await p.evaluate(y => scrollTo(0, y), top - 40);
    await p.waitForTimeout(1500);
    const tabs = await p.$$('#industries button');
    console.log('tabs', tabs.length, await Promise.all(tabs.map(t => t.innerText())));
    fs.mkdirSync('cap/tabs', { recursive: true });
    let i = 0;
    const shots = async n => {
      for (let k = 0; k < n; k++) {
        await p.waitForTimeout(30);
        await p.screenshot({ path: `cap/tabs/${String(i++).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
      }
    };
    await shots(30);
    for (const t of tabs.slice(1, 3)) { await t.hover(); await t.click(); await shots(70); }
  }

  if (mode === 'mobile') {
    const p = await mk(390, 844, 2, true);
    const tops = await p.evaluate(() => ['solutions', 'industries', 'contact'].map(id => document.getElementById(id).getBoundingClientRect().top + scrollY));
    const total = await p.evaluate(() => document.documentElement.scrollHeight - innerHeight);
    console.log('mobile tops', tops, total);
    for (let y = 0; y <= total; y += 400) { await p.evaluate(y => scrollTo(0, y), y); await p.waitForTimeout(150); }
    const segs = [[0, 0, 60, 0], [1, -40, 30, 220], [2, -60, 30, 160]];
    let k = 0;
    fs.mkdirSync('cap/mobile', { recursive: true });
    for (const [ti, off, n, dy] of segs) {
      const y0 = Math.max(0, tops[ti] + off);
      await p.evaluate(y => scrollTo(0, y), y0); await p.waitForTimeout(900);
      for (let i = 0; i < n; i++) {
        const u = i / (n - 1);
        await p.evaluate(y => scrollTo(0, y), y0 + dy * (u < .5 ? 4*u*u*u : 1 - Math.pow(-2*u+2,3)/2));
        await p.waitForTimeout(40);
        await p.screenshot({ path: `cap/mobile/${String(k++).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
      }
    }
  }

  await b.close();
})();
