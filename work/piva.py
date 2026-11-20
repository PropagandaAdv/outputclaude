import re, requests
from html import unescape
H={'User-Agent':'Mozilla/5.0 (compatible; We4ListCheck/1.0)','Accept-Language':'it'}
PAT=re.compile(r'(?:p\.?\s?iva|partita\s+iva|vat(?:\s+(?:no|number|id|reg\w*))?|c\.?\s?f\.?|codice\s+fiscale)[^0-9A-Za-z]{0,25}(?:IT\s?)?(\d{11})\b',re.I)
def valid(p):
    if len(p)!=11 or not p.isdigit(): return False
    s=0
    for i,c in enumerate(p[:10]):
        n=int(c)
        if i%2: n*=2; n= n-9 if n>9 else n
        s+=n
    return (10-s%10)%10==int(p[10])
def text(html):
    html=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',html)
    return re.sub(r'\s+',' ',unescape(re.sub(r'<[^>]+>',' ',html)))
def fetch(u):
    try:
        r=requests.get(u,headers=H,timeout=15)
        return r.text[:600000] if r.status_code<400 else ''
    except Exception: return ''
def find_piva(d):
    base='https://'+d
    html=fetch(base)
    if not html: html=fetch('http://'+d); base='http://'+d
    if not html: return None,None,'sito non raggiungibile'
    pages=[(base,html)]
    cands=re.findall(r'href=["\']([^"\']+)["\']',html)
    keys=('privacy','contatt','contact','chi-siamo','about','legal','note-leg','imprint','cookie','azienda','societa','termini','policy')
    seen=set();extra=[]
    for h in cands:
        hl=h.lower()
        if any(k in hl for k in keys) and not hl.startswith(('mailto','tel','#','javascript')):
            if hl.startswith('http') and d.split('.')[0] not in hl: continue
            u=requests.compat.urljoin(base+'/',h)
            if u not in seen: seen.add(u); extra.append(u)
    for u in extra[:5]: pages.append((u,fetch(u)))
    for u,h in pages:
        t=text(h)
        for m in PAT.finditer(t):
            p=m.group(1)
            if valid(p): return p,u,''
    # fallback: qualsiasi 11 cifre valide vicino a 'iva'
    return None,None,'P.IVA non trovata sul sito'
