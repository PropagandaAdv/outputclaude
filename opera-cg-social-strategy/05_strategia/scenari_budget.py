# Calcolo scenari budget. Assunzioni dichiarate nel documento.
# CPL indicativi (USD fonti terze, trattati ~ EUR 1:1 come ordine di grandezza):
#  LinkedIn: spend-weighted 202 (Metadata 2026), lead form 193, document ads 142 -> range 140-250
#  Meta (FB/IG) B2B: 138-145 (Metadata 2026); lead ads cross-industry 27.66 (WordStream 2025); costruzioni USA 53 (SuperAds)
#   -> targeting B2C-like (condomini/proprietari) 40-90 ; range Meta blend 50-110
S = {
 'Base':        dict(mese=2500, li=0.40),
 'Consigliato': dict(mese=5000, li=0.45),
 'Accelerato':  dict(mese=9000, li=0.45),
}
LI=(140,250); META=(50,110)
ORG=(3,6)   # contatti/mese da organico+sito+outbound social [INFERENZA, da validare]
RAMP=[0.5,1,1,1,1,1]  # mese1 setup/apprendimento -> 50% di efficienza spesa utile
penal={'Base':1.0,'Consigliato':1.0,'Accelerato':1.15}  # CPL +15% a scala maggiore
out={}
for k,v in S.items():
    tot=v['mese']*6; li=tot*v['li']; me=tot-li; p=penal[k]
    eff=sum(RAMP)/6  # quota di spesa "efficiente"
    def leads(b,r): return (b*eff/(r[1]*p), b*eff/(r[0]*p))
    l1=leads(li,LI); m1=leads(me,META)
    paid=(l1[0]+m1[0], l1[1]+m1[1])
    org=(ORG[0]*6, ORG[1]*6)
    tmin=paid[0]+org[0]; tmax=paid[1]+org[1]
    mid_li=li*eff/(sum(LI)/2*p); mid_me=me*eff/(sum(META)/2*p)
    mid=mid_li+mid_me+sum(ORG)/2*6
    out[k]=dict(tot=tot,li=li,me=me,li_leads=l1,me_leads=m1,paid=paid,org=org,tot_rng=(tmin,tmax),mid=mid,mid_li=mid_li,mid_me=mid_me)
    print(k,f"spesa6m={tot:,.0f} LI={li:,.0f} Meta={me:,.0f} | LI lead {l1[0]:.0f}-{l1[1]:.0f} Meta lead {m1[0]:.0f}-{m1[1]:.0f} | paid {paid[0]:.0f}-{paid[1]:.0f} + org {org[0]}-{org[1]} = {tmin:.0f}-{tmax:.0f} | centrale {mid:.0f} vs 270 -> {'OK' if mid>=270 else 'NO'}")
import json; json.dump(out,open('/home/user/outputclaude/opera-cg-social-strategy/05_strategia/scenari.json','w'),indent=1)
