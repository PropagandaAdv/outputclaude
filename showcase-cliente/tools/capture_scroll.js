// uso: node capture_scroll.js outDir '[{"from":0,"to":6800,"dur":10,"hold0":1,"hold1":1.2,"ease":"io"}]' [dpr]
const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{
 const out=process.argv[2], seg=JSON.parse(process.argv[3]), dpr=+(process.argv[4]||1);
 fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch({args:['--no-sandbox']});
 const ctx=await b.newContext({viewport:{width:1440,height:810},deviceScaleFactor:dpr});
 const p=await ctx.newPage();
 await p.goto('https://cambridgecentre.vercel.app/',{waitUntil:'load'}); await p.waitForTimeout(4500);
 // prima passata: attiva animazioni on-scroll / precarica
 await p.evaluate(async()=>{for(let y=0;y<document.documentElement.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,40));} scrollTo(0,0);});
 await p.waitForTimeout(2500);
 await p.mouse.move(1430,805);
 const c=await ctx.newCDPSession(p); const times=[]; let n=0;
 c.on('Page.screencastFrame',async f=>{fs.writeFileSync(`${out}/${String(n).padStart(5,'0')}.jpg`,Buffer.from(f.data,'base64'));times.push(f.metadata.timestamp);n++;c.send('Page.screencastFrameAck',{sessionId:f.sessionId}).catch(()=>{});});
 await c.send('Page.startScreencast',{format:'jpeg',quality:92,everyNthFrame:1,maxWidth:1440*dpr,maxHeight:810*dpr});
 await p.evaluate(async(seg)=>{
  const io=t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2, sine=t=>-(Math.cos(Math.PI*t)-1)/2;
  for(const s of seg){
   const f=s.ease==='io'?io:s.ease==='sine'?sine:(t=>t);
   scrollTo(0,s.from); await new Promise(r=>setTimeout(r,(s.hold0||0)*1000));
   await new Promise(res=>{const t0=performance.now();(function step(now){const t=Math.min(1,(now-t0)/(s.dur*1000));scrollTo(0,s.from+(s.to-s.from)*f(t));t<1?requestAnimationFrame(step):res();})(t0);});
   await new Promise(r=>setTimeout(r,(s.hold1||0)*1000));
  }},seg);
 await c.send('Page.stopScreencast');
 fs.writeFileSync(`${out}/times.json`,JSON.stringify(times));
 console.log('frames',n,'span',(times.at(-1)-times[0]).toFixed(2));
 await b.close();})();
