import pandas as pd, re
df=pd.read_pickle('f0final.pkl')
NB=r"(?<![a-z0-9])(rai ?pubblicit[àa]?|publitalia|manzoni (&|e) c|sky ?media|mediamond|cairo pubblicit[àa]|cairo communication|piemme (spa|s\.p\.a|concessionaria)|igp ?decaux|decaux|wpp|publicis|omnicom|interpublic|havas|dentsu|stagwell|groupm|mindshare|wavemaker|omd|starcom|zenith (media|italia)|carat|ogilvy|mccann|saatchi|tbwa|ddb|leo burnett|young & rubicam|vmly|mediacom|mediaplus|italiaonline|sipra|gedi (gruppo|spa)|gruppo editoriale|mondadori|rcs (mediagroup|pubblicit|media)|rcs$|il sole 24 ore|24 ore|mediaset|rai |sky italia|speed (spa|s\.p\.a|srl)?$)(?![a-z0-9])"
def isnome(r):
    t=(str(r.company)+' '+r.domain_n).lower()
    return re.search(NB,t)
m=df.f0.eq('MATCH_NOME')
hit=df[m].apply(isnome,axis=1)
idx=hit[hit.notna()].index
df.loc[idx,'f0f']='ESCLUSO_MEDIA'; df.loc[idx,'motivo']='nome in lista network/concessionarie/editori: '+hit[idx].map(lambda x:x.group(0).strip())
# match testuali non confermati -> dubbio (tranne termini innocui)
safe=r"^company/domain: (brand|digital|agenzia)"
mt=(df.f0=='MATCH_TESTO')&(df.f0f=='OK')&~df.f0_motivo.str.contains(safe)&~df.company.fillna('').str.lower().str.contains('telecomunicazion|multimedia')&~df.domain_n.str.contains('telecomunicazion')
df.loc[mt,'f0f']='DUBBIO_MEDIA'; df.loc[mt,'motivo']='nome/dominio con termine media senza conferma da homepage | '+df.loc[mt,'f0_motivo']
# false positive 'nome lista' residui con OK: restano OK ma verifica
print(df.f0f.value_counts()); print(df.groupby('f0f').domain_n.nunique())
d=df[m].drop_duplicates('domain_n'); print(d[d.f0f=='OK'][['company','domain_n']].to_string())
df.to_pickle('f0final.pkl')
