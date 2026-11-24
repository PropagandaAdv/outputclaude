const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch();
  const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
  await p.goto('https://inprotec-homepage.vercel.app',{waitUntil:'domcontentloaded'});
  await p.waitForTimeout(2000);
  const info = await p.evaluate(()=>({h:document.documentElement.scrollHeight, sticky:[...document.querySelectorAll('*')].filter(e=>getComputedStyle(e).position==='sticky').map(e=>e.tagName+'.'+e.className+' '+Math.round(e.parentElement.getBoundingClientRect().height)).slice(0,8), secs:[...document.querySelectorAll('section')].map(s=>[s.id,s.className.slice(0,30),Math.round(s.getBoundingClientRect().top+scrollY),Math.round(s.getBoundingClientRect().height)])}));
  console.log(JSON.stringify(info,null,1));
  await b.close();
})();
