const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch(process.env.HTTPS_PROXY?{proxy:{server:process.env.HTTPS_PROXY}}:{});
  const p = await b.newPage({ignoreHTTPSErrors:true,viewport:{width:1440,height:900},deviceScaleFactor:1});
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(1500);
  const info = await p.evaluate(()=>({
    h: document.documentElement.scrollHeight,
    sections:[...document.querySelectorAll('section,header,footer,main>*')].map(e=>({tag:e.tagName,id:e.id,cls:String(e.className).slice(0,60),top:Math.round(e.getBoundingClientRect().top+scrollY),h:Math.round(e.getBoundingClientRect().height)})),
    fonts:[...new Set([...document.querySelectorAll('h1,h2,p,a')].slice(0,30).map(e=>getComputedStyle(e).fontFamily))],
    vids:[...document.querySelectorAll('video')].map(v=>({src:v.currentSrc,dur:v.duration,loop:v.loop}))
  }));
  console.log(JSON.stringify(info,null,1));
  for(let i=0;i<8;i++){ await p.screenshot({path:`h${i}.png`}); await p.waitForTimeout(1500);}
  await b.close();
})();
