const { chromium } = require('playwright');
const FPS=60, DUR=15.0, VEL=6484/14.583333, YMAX=6560;
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const p = await b.newPage({ignoreHTTPSErrors:true,viewport:{width:1440,height:900},deviceScaleFactor:1});
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(5000);
  await p.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  const N=Math.round(FPS*DUR); let maxErr=0;
  for(let i=0;i<N;i++){
    const t=i/FPS, y=Math.min(VEL*t,YMAX);
    await p.evaluate(y=>window.scrollTo({top:y,behavior:'instant'}),y);
    const exp=Math.min(t,14.5833);
    // wait until video time converges (video seeking done)
    for(let k=0;k<20;k++){
      const s=await p.evaluate(()=>{const v=document.querySelector('video');return [v.currentTime,v.seeking]});
      if(!s[1] && Math.abs(s[0]-exp)<0.03) break;
      await p.waitForTimeout(25);
    }
    await p.waitForTimeout(60);
    const s=await p.evaluate(()=>document.querySelector('video').currentTime);
    maxErr=Math.max(maxErr,Math.abs(s-exp));
    await p.screenshot({path:`../hero/h_${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:93});
    if(i%60==0) console.log(i,t.toFixed(2),s.toFixed(3),exp.toFixed(3));
  }
  console.log('done maxErr',maxErr);
  await b.close();
})();
