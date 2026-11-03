const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const p = await b.newPage({ignoreHTTPSErrors:true,viewport:{width:1440,height:900}});
  p.on('response',r=>{const u=r.url(); if(/media|\.mp4|\.webm/.test(u)) console.log('RES',r.status(),u,r.headers()['content-length'])});
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(5000);
  const lenis = await p.evaluate(()=>!!window.lenis || !!document.querySelector('.lenis') || getComputedStyle(document.documentElement).scrollBehavior);
  console.log('lenis/scrollBehavior',lenis);
  for (const y of [1000,1001,3000]) {
    await p.evaluate(y=>window.scrollTo(0,y),y);
    for (const w of [50,150,400]) { await p.waitForTimeout(w); console.log(y,w, await p.evaluate(()=>document.querySelector('video').currentTime)); }
  }
  const t0=Date.now(); for(let i=0;i<10;i++){await p.screenshot({type:'jpeg',quality:90});} console.log('ms/shot',(Date.now()-t0)/10);
  await b.close();
})();
