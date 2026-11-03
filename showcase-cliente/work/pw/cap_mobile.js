const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const ctx = await b.newContext({ignoreHTTPSErrors:true,viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true});
  const p = await ctx.newPage();
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(5000);
  await p.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  const H = await p.evaluate(()=>document.documentElement.scrollHeight);
  const pos = await p.evaluate(()=>Object.fromEntries(['top','lavorazioni','materioteca','metodo','contatti'].map(id=>{const e=document.getElementById(id);const r=e.getBoundingClientRect();return [id,[Math.round(r.top+scrollY),Math.round(r.height)]]})));
  console.log(H,JSON.stringify(pos));
  await p.screenshot({path:'../mobile/hero0.png'});
  for(let y=0;y<=H;y+=300){ await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(150); }
  await p.waitForTimeout(1200);
  // final hero state viewport
  await p.evaluate(y=>window.scrollTo(0,y),6900); await p.waitForTimeout(900);
  await p.screenshot({path:'../mobile/hero_end.png'});
  await p.addStyleTag({content:'header{visibility:hidden!important}'});
  for(const id of ['lavorazioni','materioteca','metodo','contatti']){
    const [top,h]=pos[id];
    await p.evaluate(y=>window.scrollTo(0,y),top); await p.waitForTimeout(700);
    await p.screenshot({path:`../mobile/${id}.png`,fullPage:true,clip:{x:0,y:top,width:390,height:Math.min(h,4600)}});
  }
  await b.close();
})();
