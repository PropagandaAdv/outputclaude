const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const p = await b.newPage({ignoreHTTPSErrors:true,viewport:{width:1440,height:900}});
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(3000);
  const r = await p.evaluate(()=>{
    const out=[];
    for (const e of document.querySelectorAll('h2,h3,[role=tab],button,form,a[href^="#"]')) {
      const b=e.getBoundingClientRect(); out.push([e.tagName,(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,40).replace(/\n/g,' '),Math.round(b.top+scrollY),Math.round(b.left),Math.round(b.width),Math.round(b.height)].join('|'));
    }
    return out;
  });
  console.log(r.join('\n'));
  await b.close();
})();
