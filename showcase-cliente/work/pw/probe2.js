const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const p = await b.newPage({ignoreHTTPSErrors:true,viewport:{width:1440,height:900}});
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(4000);
  for(let y=0;y<=8200;y+=500){
    await p.evaluate(y=>window.scrollTo(0,y),y);
    await p.waitForTimeout(900);
    const t = await p.evaluate(()=>{const v=document.querySelector('video');return {t:v&&v.currentTime, rs:v&&v.readyState, h1:(document.querySelector('h1')||{}).innerText}});
    console.log(y,JSON.stringify(t));
    await p.screenshot({path:`s${String(y).padStart(5,'0')}.jpg`,quality:60,type:'jpeg'});
  }
  const html = await p.evaluate(()=>document.querySelector('#top').outerHTML.slice(0,3500));
  console.log(html);
  await b.close();
})();
