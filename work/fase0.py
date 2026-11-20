import pandas as pd, re
df=pd.read_excel('original_copy.xlsx',sheet_name='Foglio1',dtype=str)
df['domain_n']=df.domain.fillna('').str.lower().str.strip().str.replace(r'^https?://','',regex=True).str.replace(r'^www\.','',regex=True).str.rstrip('/')
df['ind_n']=df.industries.fillna('').str.lower().str.strip()
CERT={'marketing & advertising','public relations & communications','media production','online media','broadcast media','publishing','newspapers'}
DUB={'design','graphic design','events services','printing','entertainment','market research'}
names=r"raipubblicit|publitalia|manzoni|sky ?media|mediamond|cairo pubblicit|piemme|igpdecaux|decaux|\bwpp\b|publicis|omnicom|\bipg\b|havas|dentsu|stagwell|groupm|mindshare|wavemaker|\bomd\b|\bphd\b|starcom|zenith|\bcarat\b|ogilvy|mccann|saatchi|tbwa|ddb|leo burnett|young & rubicam|\bvmly|mediacom|mediaplus|italiaonline|rai pubb|sipra|sole 24 ore|gedi|mondadori|rcs|mediaset"
terms=r"pubblicit|advertis|\badv\b|comunicazion|communicat|media|agenzia|concessionari|marketing|\bpr\b|\bbrand|\bweb agency|\bcreativ|\bdigital\b"
kwterms=r"pubblicit|advertis|agenzia di (comunicazion|marketing|pubblicit|pr)|concessionaria|centro media|media agency|public relations|branding agency|marketing agency|communication agency|agenzia pubblicit|media planning|media buying|ufficio stampa"
def txt(r): return ' '.join(str(r[c]).lower() for c in ['company','keywords'] if pd.notna(r[c]))+' '+r['domain_n']
def f(r):
    if r.ind_n in CERT: return 'ESCLUSO_MEDIA','industries: '+r.ind_n
    t=txt(r)
    m=re.search(names,t)
    if m: return 'MATCH_NOME','nome lista: '+m.group(0)
    # solo company+domain per il match "debole"; keywords separate
    cd=(str(r.company).lower()+' '+r.domain_n)
    m=re.search(terms,cd)
    if m: return 'MATCH_TESTO','company/domain: '+m.group(0)
    m=re.search(kwterms,str(r.keywords).lower()) if pd.notna(r.keywords) else None
    if m: return 'MATCH_KW','keywords: '+m.group(0)
    if r.ind_n in DUB: return 'DUBBIO_MEDIA','industries: '+r.ind_n
    return 'OK',''
res=df.apply(f,axis=1,result_type='expand'); df['f0']=res[0]; df['f0_motivo']=res[1]
df.to_pickle('f0.pkl')
df.loc[(df.f0=='MATCH_NOME')&df.company.fillna('').str.lower().str.fullmatch(r'speed( s\.?p\.?a\.?)?'),'f0']='MATCH_NOME'
print(df.f0.value_counts()); print(df.groupby('f0').domain_n.nunique())
for k in ['MATCH_NOME','MATCH_TESTO','MATCH_KW']:
    print(k);print(df[df.f0==k].drop_duplicates('domain_n')[['company','domain_n','industries','f0_motivo']].sample(12,random_state=1).to_string())
