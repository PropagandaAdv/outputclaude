const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({args:['--no-sandbox']});
 const p=await (await b.newContext({viewport:{width:1440,height:810}})).newPage();
 await p.goto('https://cambridgecentre.vercel.app/',{waitUntil:'load'}); await p.waitForTimeout(4000);
 const info=await p.evaluate(()=>({H:document.documentElement.scrollHeight,secs:[...document.querySelectorAll('main > *, section, footer')].map(e=>({tag:e.tagName,id:e.id,cls:(e.className||'').toString().slice(0,40),top:Math.round(e.getBoundingClientRect().top+scrollY),h:Math.round(e.offsetHeight),txt:(e.innerText||'').slice(0,40).replace(/\n/g,' ')}))}));
 console.log(JSON.stringify(info,null,0).replace(/\},\{/g,'},\n{'));
 await b.close();})();
