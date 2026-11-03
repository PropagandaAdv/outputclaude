const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const ctx = await b.newContext({ignoreHTTPSErrors:true,viewport:{width:1440,height:900},deviceScaleFactor:3});
  const p = await ctx.newPage();
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(4000);
  await p.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  // slow scroll through to trigger reveals / lazy images
  for(let y=6000;y<=13800;y+=300){ await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(250); }
  await p.waitForTimeout(1500);
  // header overlay
  await p.evaluate(()=>window.scrollTo(0,9000)); await p.waitForTimeout(800);
  await p.screenshot({path:'../strips/header.png',clip:{x:0,y:0,width:1440,height:86}});
  // hide header for strips
  await p.addStyleTag({content:'header{visibility:hidden!important}'});
  const secs=[['lav',8100,2087],['mat',10187,1062],['met',11249,1245],['con',12493,1177]];
  for(const [n,top,h] of secs){
    await p.evaluate(y=>window.scrollTo(0,y),top); await p.waitForTimeout(900);
    await p.screenshot({path:`../strips/${n}.png`,fullPage:true,clip:{x:0,y:top,width:1440,height:h}});
    console.log(n,top,h);
  }
  await b.close();
})();
