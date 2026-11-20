import pandas as pd, csv, os, time, json
from concurrent.futures import ThreadPoolExecutor
from piva import find_piva
df=pd.read_pickle('f0final.pkl')
doms=sorted(d for d in df[df.fase0=='OK'].domain_n.unique() if d)
out='progress.csv'
done=set()
if os.path.exists(out): done={r['dominio'] for r in csv.DictReader(open(out))}
todo=[d for d in doms if d not in done]
print(len(doms),len(todo),flush=True)
new=not os.path.exists(out)
f=open(out,'a',newline=''); w=csv.writer(f)
if new: w.writerow(['dominio','esito','partita_iva','url_piva','note'])
def job(d):
    try: p,u,e=find_piva(d)
    except Exception as ex: p,u,e=None,None,'errore: '+str(ex)[:80]
    return d,p,u,e
t0=time.time()
for b in range(0,len(todo),200):
    with ThreadPoolExecutor(12) as ex: res=list(ex.map(job,todo[b:b+200]))
    for d,p,u,e in res: w.writerow([d,'TROVATA' if p else 'NON_TROVATA',p or '',u or '',e])
    f.flush(); print(b+200,round(time.time()-t0),flush=True)
