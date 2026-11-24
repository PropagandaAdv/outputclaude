const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch();
  const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
  await p.goto('https://inprotec-homepage.vercel.app',{waitUntil:'domcontentloaded'});
  await p.waitForTimeout(5000);
  for (const y of [0,2000,4000,6000,8000]) { await p.evaluate(y=>scrollTo(0,y),y); await p.waitForTimeout(1500); await p.screenshot({path:`cap/s_${y}.png`}); }
  console.log(await p.evaluate(()=>{const v=document.querySelector('video');return v?[v.readyState,v.duration,v.currentTime,v.error&&v.error.code]:'novideo'}));
  await b.close();
})();
