const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{
 const out='work/esami'; fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch({args:['--no-sandbox']});
 const ctx=await b.newContext({viewport:{width:1440,height:810},deviceScaleFactor:2});
 const p=await ctx.newPage();
 await p.goto('https://cambridgecentre.vercel.app/',{waitUntil:'load'}); await p.waitForTimeout(4500);
 await p.evaluate(async()=>{for(let y=0;y<document.documentElement.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,40));}});
 await p.evaluate(()=>scrollTo(0,10136-20)); await p.waitForTimeout(1500);
 const btns=await p.locator('#esami button').all(); console.log('buttons',btns.length, await Promise.all(btns.map(x=>x.innerText().then(t=>t.slice(0,25).replace(/\n/g,' ')))));
 const c=await ctx.newCDPSession(p); const times=[]; let n=0;
 c.on('Page.screencastFrame',async f=>{fs.writeFileSync(`${out}/${String(n).padStart(5,'0')}.jpg`,Buffer.from(f.data,'base64'));times.push(f.metadata.timestamp);n++;c.send('Page.screencastFrameAck',{sessionId:f.sessionId}).catch(()=>{});});
 await c.send('Page.startScreencast',{format:'jpeg',quality:92,everyNthFrame:1,maxWidth:2880,maxHeight:1620});
 await p.waitForTimeout(600);
 for(const b of btns.slice(0,6)){ await b.hover(); await p.waitForTimeout(250); await b.click(); await p.waitForTimeout(1100); }
 await c.send('Page.stopScreencast'); fs.writeFileSync(`${out}/times.json`,JSON.stringify(times)); console.log('frames',n);
 await b.close();})();
