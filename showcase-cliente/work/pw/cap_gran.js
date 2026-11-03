const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch({proxy:{server:process.env.HTTPS_PROXY}});
  const p = await b.newPage({ignoreHTTPSErrors:true,viewport:{width:1440,height:900},deviceScaleFactor:3});
  await p.goto('https://tecnomarmi.vercel.app/',{waitUntil:'load',timeout:60000});
  await p.waitForTimeout(4000);
  await p.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  for(let y=6000;y<=10400;y+=400){ await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(200); }
  await p.evaluate(()=>window.scrollTo(0,10230)); await p.waitForTimeout(800);
  await p.getByText(/^granito$/i).first().click(); await p.waitForTimeout(2500);
  await p.addStyleTag({content:'header{visibility:hidden!important}'});
  await p.screenshot({path:'../strips/mat_granito.png',fullPage:true,clip:{x:0,y:10187,width:1440,height:1062}});
  const pal = await p.evaluate(()=>{const cs=getComputedStyle(document.documentElement);return ['--color-ink','--color-graphite','--color-stone','--color-accent','--color-bone','--color-gold','--color-brass'].map(k=>k+'='+cs.getPropertyValue(k).trim()).join(' ')+' | body bg '+getComputedStyle(document.body).backgroundColor+' color '+getComputedStyle(document.body).color});
  console.log(pal);
  const vars = await p.evaluate(()=>{const o=[];for(const s of document.styleSheets){try{for(const r of s.cssRules){if(r.selectorText===':root'||r.selectorText==='*, :before, :after'||(r.cssText||'').includes('--color-')){const m=r.cssText.match(/--color-[a-z0-9-]+:\s*[^;]+/g);if(m)o.push(...m)}}}catch(e){}}return [...new Set(o)].slice(0,30)});
  console.log(vars.join('\n'));
  await b.close();
})();
