import pandas as pd, requests, re, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor
from html import unescape
df=pd.read_pickle('f0.pkl')
doms=sorted(df[df.f0.isin(['MATCH_NOME','MATCH_TESTO','MATCH_KW'])].domain_n.unique())
doms=[d for d in doms if d]
out='home_cache.jsonl'
done=set()
if os.path.exists(out): done={json.loads(l)['d'] for l in open(out)}
todo=[d for d in doms if d not in done]
print(len(doms),len(todo),flush=True)
H={'User-Agent':'Mozilla/5.0 (compatible; We4ListCheck/1.0)','Accept-Language':'it'}
def get(d):
    for u in ('https://'+d,'http://'+d):
        try:
            r=requests.get(u,headers=H,timeout=15,allow_redirects=True)
            t=r.text[:300000]
            title=re.search(r'<title[^>]*>(.*?)</title>',t,re.S|re.I)
            desc=re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',t,re.S|re.I) or re.search(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']',t,re.S|re.I)
            h=re.findall(r'<h[12][^>]*>(.*?)</h[12]>',t,re.S|re.I)[:4]
            cl=lambda s:re.sub(r'\s+',' ',unescape(re.sub(r'<[^>]+>','',s))).strip()
            return dict(d=d,ok=True,status=r.status_code,title=cl(title.group(1)) if title else '',desc=cl(desc.group(1)) if desc else '',h=[cl(x) for x in h])
        except Exception as e:
            err=str(e)[:100]
    return dict(d=d,ok=False,err=err)
with ThreadPoolExecutor(24) as ex, open(out,'a') as f:
    for i,r in enumerate(ex.map(get,todo)):
        f.write(json.dumps(r,ensure_ascii=False)+'\n'); f.flush()
        if i%100==0: print(i,flush=True)
