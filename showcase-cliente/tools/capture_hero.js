const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = process.argv[2], secs = +process.argv[3];
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const ctx = await b.newContext({ viewport: { width: 1440, height: 810 }, deviceScaleFactor: 1 });
  const p = await ctx.newPage();
  await p.goto('https://cambridgecentre.vercel.app/', { waitUntil: 'load' });
  await p.waitForTimeout(4000);
  // chiudi eventuali cookie banner
  for (const t of ['Accetta','Accetto','Accept','OK']) { const l=p.getByRole('button',{name:t}).first(); if(await l.count()) { await l.click().catch(()=>{}); } }
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(300); // riparte il ciclo hero da zero
  const c = await ctx.newCDPSession(p);
  const times = []; let n = 0;
  c.on('Page.screencastFrame', async f => {
    fs.writeFileSync(`${out}/${String(n).padStart(5,'0')}.jpg`, Buffer.from(f.data, 'base64'));
    times.push(f.metadata.timestamp); n++;
    c.send('Page.screencastFrameAck', { sessionId: f.sessionId }).catch(()=>{});
  });
  await c.send('Page.startScreencast', { format: 'jpeg', quality: 95, everyNthFrame: 1 });
  await p.waitForTimeout(secs * 1000);
  await c.send('Page.stopScreencast');
  fs.writeFileSync(`${out}/times.json`, JSON.stringify(times));
  console.log('frames', n, 'span', times[times.length-1]-times[0]);
  await b.close();
})();
