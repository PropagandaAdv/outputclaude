import pandas as pd, time, random
from concurrent.futures import ThreadPoolExecutor
from piva import find_piva
df=pd.read_pickle('f0final.pkl'); t=df[(df.fase0=='OK')&(df.domain_n!='')].drop_duplicates('domain_n')
random.seed(7); s=t.sample(30,random_state=7)
t0=time.time()
with ThreadPoolExecutor(10) as ex: res=list(ex.map(find_piva,s.domain_n))
print('tempo',round(time.time()-t0),'s')
s=s.assign(piva=[r[0] for r in res],piva_url=[r[1] for r in res],err=[r[2] for r in res])
print(s[['company','domain_n','company_country','Employees','piva','err']].to_string())
print('P.IVA trovate',s.piva.notna().sum(),'/30')
s.to_pickle('pilot30.pkl')
