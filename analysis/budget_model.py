"""Modello di stima budget/KPI LinkedIn Ads per Retica — 2.000 €/MESE, SENZA LEAD MAGNET e SENZA VIDEO. Tutti i risultati sono [STIMA].
Percorso: notorietà (annunci sponsorizzati dalla pagina Retica) -> considerazione (retargeting con prove, verso landing) -> conversione (Lead Gen Form 'Richiedi demo').
Nessun contenuto scaricabile: i contatti sono SOLO richieste di demo (da landing o da Lead Gen Form).
Benchmark (USD) da:
 - ZenABM, "LinkedIn Ads Benchmarks: Real Data from 211 B2B Companies in 2026" (agg. 16/02/2026) https://zenabm.com/blog/linkedin-ads-benchmarks-2026
 - ClickMinded, "LinkedIn Ads Benchmarks 2026" (agg. 08/07/2026) https://www.clickminded.com/linkedin-ads-benchmarks/
Ipotesi richiesta demo -> demo svolta: NON da fonti, [DA CONFERMARE] con i dati storici Retica.
"""
import json
FX = 0.90          # EUR per USD  [STIMA, DA CONFERMARE]
WEEKS_PER_MONTH = 52/12

FMT = {  # (CPM USD, CTR) — ZenABM mediane
 'TLA':      dict(cpm=49.37, ctr=0.0268),
 'VIDEO':    dict(cpm=38.94, ctr=0.0024),
 'CAROUSEL': dict(cpm=45.28, ctr=0.0032),   # considerazione: carosello/Document Ad da leggere nel feed, verso la landing
 'IMG_LGF':  dict(cpm=59.15, ctr=0.0040),   # conversione: immagine singola con Lead Gen Form 'Richiedi demo'
}
LGF_RATE = 0.08      # ClickMinded: Lead Gen Form 8-15%: uso il minimo, perché qui il modulo è una richiesta di demo (non un download) [STIMA prudente]
LP_RATE  = 0.035     # ClickMinded: landing page / richieste demo 2-5% (punto medio)
REQ_TO_DEMO = 0.35   # richiesta di demo -> demo svolta [DA CONFERMARE]

SPLIT = {'Piano':(0.25,0.15,0.60)}   # notorietà / considerazione / conversione
BUDGET = {'Piano':2000}   # budget indicato dal cliente [DA CONFERMARE: al mese o in totale?]
CASES = {'Prudente':dict(cpm=1.25,ctr=0.75,conv=0.80),'Base':dict(cpm=1.0,ctr=1.0,conv=1.0),'Ottimistico':dict(cpm=0.85,ctr=1.25,conv=1.20)}

def run(sc, case):
    b=BUDGET[sc]; a,c,v=[b*x for x in SPLIT[sc]]; k=CASES[case]
    imp=lambda spend,f: spend/(FMT[f]['cpm']*FX*k['cpm'])*1000
    clk=lambda i,f: i*FMT[f]['ctr']*k['ctr']
    iA=imp(a,'TLA'); cA=clk(iA,'TLA')
    iC=imp(c,'CAROUSEL'); cC=clk(iC,'CAROUSEL'); lC=cC*LP_RATE*k['conv']
    iV=imp(v,'IMG_LGF'); cV=clk(iV,'IMG_LGF'); lV=cV*LGF_RATE*k['conv']
    req=lC+lV; demos=req*REQ_TO_DEMO
    impr=iA+iC+iV; clicks=cA+cC+cV
    return dict(scenario=sc,case=case,budget_eur=b,notorieta=a,considerazione=c,conversione=v,impressions=round(impr),clicks=round(clicks),
        requests_consideration=lC,requests_conversion=lV,requests=req,leads=req,cpl_eur=b/req if req else None,
        demos=demos,cost_per_demo_eur=b/demos if demos else None)

res=[run(s,c) for s in BUDGET for c in CASES]
for r in res:
    print(f"{r['scenario']:6}{r['case']:12} imp {r['impressions']:>8,} clic {r['clicks']:>5,} richieste {r['requests']:5.1f} €/rich {r['cpl_eur']:6.0f} demo {r['demos']:4.1f} €/demo {r['cost_per_demo_eur']:6.0f}")
json.dump(dict(params=dict(FX=FX,FMT=FMT,LGF_RATE=LGF_RATE,LP_RATE=LP_RATE,REQ_TO_DEMO=REQ_TO_DEMO,SPLIT=SPLIT),results=res),open('/home/user/outputclaude/analysis/budget_results.json','w'),indent=1,default=float)

print('12 settimane =', round(12/WEEKS_PER_MONTH,2),'mesi')
for r in res:
    if r['case']=='Base': print(r['scenario'],'spesa media 12 sett: €',round(r['budget_eur']*12/WEEKS_PER_MONTH))

# --- myBiros: formula e scala (invariato) ---
print('\nmyBiros: spesa ≈ (impression/1000) x CPM(EUR)')
CPM_EUR=[round(33.8*FX,1), round(59.15*FX,1)]
print('CPM EUR range', CPM_EUR)
N_ADS=35
print('35 annunci in Ad Library (19/11/2026); impression per annuncio e date NON visibili: valori illustrativi, NON una stima di myBiros')
for per_ad in (5_000,20_000,50_000):
    tot=N_ADS*per_ad
    print(f"{per_ad:>7,} imp/annuncio -> {tot:>9,} imp totali -> €{tot/1000*CPM_EUR[0]:,.0f} – €{tot/1000*CPM_EUR[1]:,.0f}")
