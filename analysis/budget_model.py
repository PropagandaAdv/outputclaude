"""Modello di stima budget/KPI LinkedIn Ads per Retica. Tutti i risultati sono [STIMA].
Benchmark (USD) da:
 - ZenABM, "LinkedIn Ads Benchmarks: Real Data from 211 B2B Companies in 2026" (agg. 16/02/2026)
   https://zenabm.com/blog/linkedin-ads-benchmarks-2026
 - ClickMinded, "LinkedIn Ads Benchmarks 2026" (agg. 08/07/2026)
   https://www.clickminded.com/linkedin-ads-benchmarks/
Ipotesi di conversione lead->MQL->demo: NON provengono da fonti, sono [DA CONFERMARE] con i dati storici Retica.
"""
import json
FX = 0.90          # EUR per USD  [STIMA, DA CONFERMARE alla data di lancio]
WEEKS_PER_MONTH = 52/12

# formato: (CPM USD, CTR)  — ZenABM mediane
FMT = {
 'TLA':      dict(cpm=49.37, ctr=0.0268),   # Thought Leader Ads
 'VIDEO':    dict(cpm=38.94, ctr=0.0024),
 'DOC_LGF':  dict(cpm=(45.28+59.15)/2, ctr=0.0043),  # CPM Document Ads non pubblicato: media carosello/single image; CTR Document 0.43%
 'CAROUSEL': dict(cpm=45.28, ctr=0.0032),
 'IMG_LGF':  dict(cpm=59.15, ctr=0.0040),   # single image
}
LGF_RATE_MOFU = 0.10   # ZenABM: media ~10% apertura->invio LGF
LGF_RATE_BOFU = 0.15   # ZenABM: "high performance 15%+" (ipotesi: pubblico caldo)  [STIMA]
LP_RATE = 0.035        # ClickMinded: landing page 2-5% (punto medio)
LEAD_TO_DEMO_MOFU = 0.40*0.25   # lead->MQL 40% x MQL->demo 25%  [DA CONFERMARE]
LEAD_TO_DEMO_BOFU = 0.35        # richiesta demo diretta -> demo fissata/svolta [DA CONFERMARE]

SPLIT = {'Start':(0.15,0.50,0.35),'Growth':(0.25,0.45,0.30),'Scale':(0.30,0.40,0.30)}
BUDGET = {'Start':1500,'Growth':3000,'Scale':5000}
CASES = {'Prudente':dict(cpm=1.25,ctr=0.75,conv=0.80),'Base':dict(cpm=1.0,ctr=1.0,conv=1.0),'Ottimistico':dict(cpm=0.85,ctr=1.25,conv=1.20)}

def run(sc, case):
    b=BUDGET[sc]; t,m,bo=[b*x for x in SPLIT[sc]]; k=CASES[case]
    def imp(spend,f): return spend/(FMT[f]['cpm']*FX*k['cpm'])*1000
    def clk(i,f): return i*FMT[f]['ctr']*k['ctr']
    out={}
    # TOFU 50% TLA / 50% video
    iT=imp(t/2,'TLA')+imp(t/2,'VIDEO'); cT=clk(imp(t/2,'TLA'),'TLA')+clk(imp(t/2,'VIDEO'),'VIDEO')
    # MOFU 65% Doc+LGF, 35% carosello->landing
    iD=imp(m*.65,'DOC_LGF'); cD=clk(iD,'DOC_LGF'); lD=cD*LGF_RATE_MOFU*k['conv']
    iC=imp(m*.35,'CAROUSEL'); cC=clk(iC,'CAROUSEL'); lC=cC*LP_RATE*k['conv']
    iB=imp(bo,'IMG_LGF'); cB=clk(iB,'IMG_LGF'); lB=cB*LGF_RATE_BOFU*k['conv']
    leadsM=lD+lC; demos=leadsM*LEAD_TO_DEMO_MOFU+lB*LEAD_TO_DEMO_BOFU
    leads=leadsM+lB; impr=iT+iD+iC+iB; clicks=cT+cD+cC+cB
    return dict(scenario=sc,case=case,budget_eur=b,tofu=t,mofu=m,bofu=bo,impressions=round(impr),clicks=round(clicks),
        ctr_blend=clicks/impr, leads_mofu=lD+lC, leads_bofu=lB, leads=leads, cpl_eur=b/leads if leads else None,
        demos=demos, cost_per_demo_eur=b/demos if demos else None, cpc_eur=b/clicks)

res=[run(s,c) for s in BUDGET for c in CASES]
for r in res:
    print(f"{r['scenario']:6}{r['case']:12} imp {r['impressions']:>8,} clic {r['clicks']:>5,} lead {r['leads']:5.1f} CPL €{r['cpl_eur']:6.0f} demo {r['demos']:4.1f} €/demo {r['cost_per_demo_eur']:6.0f}")
json.dump(dict(params=dict(FX=FX,FMT=FMT,LGF_RATE_MOFU=LGF_RATE_MOFU,LGF_RATE_BOFU=LGF_RATE_BOFU,LP_RATE=LP_RATE,LEAD_TO_DEMO_MOFU=LEAD_TO_DEMO_MOFU,LEAD_TO_DEMO_BOFU=LEAD_TO_DEMO_BOFU,SPLIT=SPLIT),results=res),open('/home/user/outputclaude/analysis/budget_results.json','w'),indent=1,default=float)

# --- myBiros: formula di stima (parametrica, NON un dato) ---
print('\nmyBiros: spesa mensile = impression_mese/1000 x CPM(EUR)')
CPM_EUR=[round(33.8*FX,1), round(59.15*FX,1)]  # 33,80$ Sponsored Content freddo (ClickMinded) -> 59,15$ single image (ZenABM)
print('CPM EUR range', CPM_EUR)
for impr in (50_000,150_000,400_000,1_000_000):
    print(f"{impr:>9,} imp/mese -> €{impr/1000*CPM_EUR[0]:,.0f} – €{impr/1000*CPM_EUR[1]:,.0f}")
# durata test
print('12 settimane =', round(12/WEEKS_PER_MONTH,2),'mesi')
for r in res:
    if r['case']=='Base': print(r['scenario'],'spesa media 12 sett: €',round(r['budget_eur']*12/WEEKS_PER_MONTH))
