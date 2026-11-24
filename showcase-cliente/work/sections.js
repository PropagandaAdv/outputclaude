const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  await p.goto('https://inprotec-homepage.vercel.app', { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(5000);
  const total = await p.evaluate(() => document.documentElement.scrollHeight - innerHeight);
  fs.mkdirSync('cap/sec', { recursive: true });
  let k = 0;
  for (let y = 8700; y <= total + 1; y += 650) {
    await p.evaluate(y => scrollTo(0, y), Math.min(y, total));
    await p.waitForTimeout(900);
    await p.screenshot({ path: `cap/sec/${String(k++).padStart(2, '0')}_${y}.png` });
  }
  console.log('total', total);
  await b.close();
})();
