import pandas as pd, json, re
df=pd.read_pickle('f0.pkl')
H={}
for l in open('home_cache.jsonl'):
    r=json.loads(l); H[r['d']]=r
strong=r"agenzia di (comunicazion|marketing|pubblicit|pr\b|social)|agenzia (creativa|pubblicit|di comunicazione|media)|communication agency|marketing agency|advertising agency|digital agency|creative agency|web agency|media agency|centro media|concessionaria|raccolta pubblicitaria|media planning|media buying|branding|public relations|ufficio stampa|brand identity|social media (marketing|manager)|pubblicit[àa]|advertising|casa editrice|editore|testata|quotidiano|giornale|emittente|radio |televisi|\btv\b|web marketing|digital marketing|comunicazione integrata|network di comunicazione|holding di comunicazione|publisher|magazine|editoria|content creation|video production|produzione video|produzione audiovisiv"
def cls(d):
    h=H.get(d)
    if not h or not h['ok']: return 'DUBBIO_MEDIA','sito non raggiungibile: match testuale non verificabile'
    t=' '.join([h['title'],h['desc']]+h['h']).lower()
    hits=sorted({x.group(0) for x in re.finditer(strong,t)})
    if len(hits)>=2: return 'ESCLUSO_MEDIA','homepage: '+', '.join(hits[:4])+' | '+h['title'][:80]
    if len(hits)==1: return 'DUBBIO_MEDIA','homepage ambigua: '+hits[0]+' | '+h['title'][:80]
    return 'OK','homepage senza indicatori media | '+h['title'][:60]
m=df.f0.isin(['MATCH_NOME','MATCH_TESTO','MATCH_KW'])
res=df[m].domain_n.map(lambda d: cls(d) if d else ('DUBBIO_MEDIA','dominio mancante'))
df['f0f']=df.f0; df['motivo']=df.f0_motivo
df.loc[m,'f0f']=[x[0] for x in res]
# nomi lista certi (grandi network): escludi anche se homepage non lo dice
df.loc[m,'motivo']=df.loc[m,'f0_motivo']+' || '+pd.Series([x[1] for x in res],index=df[m].index)
df.loc[df.f0f=='ESCLUSO_MEDIA','motivo']=df.motivo
df.to_pickle('f0final.pkl')
print(df.f0f.value_counts()); print(df.groupby('f0f').domain_n.nunique())
d=df[m].drop_duplicates('domain_n')
for k in ['ESCLUSO_MEDIA','DUBBIO_MEDIA','OK']:
    print(k); print(d[d.f0f==k][['company','domain_n','motivo']].sample(10,random_state=2).to_string(max_colwidth=110))
print(d[d.f0.eq('MATCH_NOME')][['company','f0f']].to_string())
