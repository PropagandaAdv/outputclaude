const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch();
  const ctx = await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1,recordVideo:{dir:'work/cap',size:{width:1440,height:900}}});
  const p = await ctx.newPage();
  await p.goto('https://inprotec-homepage.vercel.app',{waitUntil:'networkidle'});
  await p.mouse.move(1400,880);
  await p.waitForTimeout(14000);
  await p.screenshot({path:'work/cap/last.png'});
  await ctx.close(); await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
