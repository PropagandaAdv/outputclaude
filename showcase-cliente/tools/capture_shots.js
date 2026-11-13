// node capture_shots.js outDir from to seconds fps [w h dpr isMobile]
const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{
 const [out,from,to,secs,fps,w=1440,h=810,dpr=2,mob=0]=process.argv.slice(2); 
 fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch({args:['--no-sandbox']});
 const ctx=await b.newContext({viewport:{width:+w,height:+h},deviceScaleFactor:+dpr,isMobile:!!+mob,hasTouch:!!+mob});
 const p=await ctx.newPage();
 await p.goto('https://cambridgecentre.vercel.app/',{waitUntil:'load'}); await p.waitForTimeout(4500);
 await p.evaluate(async()=>{for(let y=0;y<document.documentElement.scrollHeight;y+=300){scrollTo(0,y);await new Promise(r=>setTimeout(r,40));}});
 await p.waitForTimeout(1500);
 const N=Math.round(+secs*+fps); const sine=t=>-(Math.cos(Math.PI*t)-1)/2;
 for(let i=0;i<=N;i++){ const y=+from+(+to-+from)*sine(i/N); await p.evaluate(y=>scrollTo(0,y),y);
   await p.waitForTimeout(30);
   await p.screenshot({path:`${out}/${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:90}); }
 console.log('done',N+1); await b.close();})();
