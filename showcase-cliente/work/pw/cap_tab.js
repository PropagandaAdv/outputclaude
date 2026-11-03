const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const p = await b.newPage({ignoreHTTPSErrors:true,viewport:{width:1440,height:900},deviceScaleFactor:2});
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(4000);
  await p.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  for(let y=6000;y<=10400;y+=400){ await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(200); }
  await p.evaluate(()=>window.scrollTo(0,10230)); await p.waitForTimeout(1500);
  const btn = p.getByText(/^granito$/i).first();
  await p.screenshot({path:'../tab/before.jpg',type:'jpeg',quality:90});
  await btn.click();
  await p.waitForTimeout(16);
  const n = await p.evaluate(()=>{const a=document.getAnimations();a.forEach(x=>x.pause());return a.length});
  console.log('animations paused',n);
  // step 
  const STEP=1000/60, FR=75;
  for(let i=0;i<FR;i++){
    await p.evaluate(ms=>{document.getAnimations().forEach(a=>{try{a.pause();a.currentTime=ms}catch(e){}})},i*STEP);
    await p.waitForTimeout(30);
    await p.screenshot({path:`../tab/t_${String(i).padStart(3,'0')}.jpg`,type:'jpeg',quality:92});
  }
  await b.close();
})();
