# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import DOC, SOURCES
TAG={"D":"[DATO]","C":"[CLIENTE]","I":"[INFERENZA]","V":"[DA VERIFICARE]",None:""}
out=["# FamiClick – Report interno Propaganda Adv (con tag epistemici)","",
"*Versione per l'agenzia del 23/11/2026. Stessi contenuti del documento cliente, con tag `[DATO]` verificato da fonte, `[CLIENTE]` dichiarato dal cliente, `[INFERENZA]` deduzione nostra, `[DA VERIFICARE]` da confermare. Nelle tabelle il tag si applica all'intera tabella salvo diversa indicazione nel testo. Dati grezzi: `/data`; appunti: `/research`.*","",
"> Nota sui tag: i riferimenti `[n]` rimandano all'elenco fonti in fondo. Dove un testo del documento cliente è riformulato (\"dalla nostra analisi emerge…\") qui è marcato `[INFERENZA]`.","", "---",""]
for b in DOC:
    k=b[0]
    if k=="h1": out+= ["", "## "+b[1], ""]
    elif k=="h2": out+= ["", "### "+b[1], ""]
    elif k=="p":
        t=TAG[b[2]] if len(b)>2 else ""
        out+= [b[1]+(" "+t if t else ""), ""]
    elif k=="bul":
        for t,tag in b[1]: out.append("- "+t+(" "+TAG[tag] if tag else ""))
        out.append("")
    elif k=="tab":
        h,rows,tag,note=b[1],b[2],b[3],b[4]
        out.append("| "+" | ".join(x or " " for x in h)+" |"); out.append("|"+"---|"*len(h))
        for r in rows: out.append("| "+" | ".join(str(c).replace("|","/") for c in r)+" |")
        out.append("")
        out.append("*Tag tabella: "+(TAG[tag] or "—")+(". "+note if note else "")+"*"); out.append("")
    elif k=="box":
        body=b[2] if isinstance(b[2],list) else [b[2]]
        out.append("> **"+b[1]+"**"); out+= ["> "+x for x in body]; out.append("")
out+= ["","---","","## 12. Assunzioni fatte (lavoro in autonomia)","",
"1. **«Contatto» = lead professionista qualificato** (modulo, risposta a DM/email). Definizione non nota. `[DA VERIFICARE]`",
"2. **Conversione contatto→iscrizione 30%**, risposta al contatto diretto 20%, 75 contatti da canali organici: ipotesi mie, senza fonte; da validare nel mese 2. `[INFERENZA]`",
"3. **Costo per contatto 22,9 €** = mediana Meta Italia tutti i settori [11], conservativa rispetto a CPC 0,50 € [10] con conversione landing 2,2% (implicita). I benchmark landing 5,1%/6,6% [17] sono globali 2024. `[DATO]` + `[INFERENZA]`",
"4. **Budget scenari** 300/800/1.800 € al mese per mesi 2–6: proposte mie, il cliente non ha indicato cifre. `[CLIENTE: da definire]`",
"5. **Città pilota** non indicate: ipotesi area emiliana (sviluppatore a Reggio Emilia, sede legale persona fisica a Luzzara RE da scheda Play). `[DA VERIFICARE]`",
"6. **Programma Partner Fondatore, 100 iscritti, profilo gratuito a vita**: proposta mia, fattibilità commerciale non verificata (la scheda Play segnala acquisti in-app). `[DA VERIFICARE]`",
"7. **Periodo** dicembre 2026 – maggio 2027, con calendario dal 30/11/2026. `[INFERENZA]`",
"8. **Buyer persona** lato offerta: basate su ipotesi, non esistono dati pubblici verificati sul comportamento social dei professionisti italiani dell'infanzia. `[INFERENZA]`",
"9. **Misure bonus** (assegno, congedi): nel piano non vengono citati importi; da verificare ogni volta su fonti ufficiali. Nel CSV Ubersuggest il picco di gennaio è riferito alla keyword «bonus famiglia 2026»: per gennaio 2027 va controllata la keyword aggiornata. `[DA VERIFICARE]`",
"10. **Developer**: Apple e Google mostrano una persona fisica come sviluppatore; il sito indica ArdoInformatica. In `/research/01-audit-brand.md` ho evitato di riportare indirizzo ed email personali nel documento cliente.",
"",
"## 13. Cosa non è stato possibile verificare","",
"- Instagram @famiclick e @familinkapp: HTTP 429 anche da browser headless (Playwright). Follower, post, formati, engagement, highlights, bio: nessun dato. TikTok e Facebook non leggibili senza accesso. `[DA VERIFICARE]`",
"- Rating Google Play e recensioni testuali (solo «100+» download e ultimo aggiornamento 20/10/2026 letti dall'HTML). Su App Store: 5,0 con 2 valutazioni.",
"- Ricerca web su «famiclick»: nessun risultato pertinente (nessuna rassegna stampa, nessun profilo indicizzato).",
"- ISTAT/DataReportal: penetrazione Instagram/TikTok nella fascia 25–44 e tempo speso non trovati. Numero fotografi, animatori, centri sportivi, negozi infanzia, consulenti sonno/allattamento: non trovati. Adozione app di prenotazione e digitalizzazione dei professionisti sanitari: non trovate. Stime scartate perché non verificabili: 68% Doxa/PoliMi app prenotazione, 19% PMI digitali, 15.678 fotografi (CNA), TikTok 1h30 al giorno.",
"- Concorrenti: Doctolib.it, Superprof, Helpling, Instapro bloccano curl (403/405); prezzi solo da fonti terze (Capterra, snippet) e marcati da verificare. Parentu, WeMamma, Mamme in rete, Bimbo Cloud non trovati come app italiane attive. Follower dei creator: solo dati 2019 o Heepsy 2026 per Alice Campello.",
"- Hook, durata e frequenza dei contenuti dei creator: nessuna fonte; non attribuiti.",
"- Gruppi Facebook/LinkedIn di professionisti: nessun gruppo italiano verificato per nome.",
"- Unbounce (conversione landing 6,6%) letto da fonte secondaria (pagina originale 403); marcato come secondario.",
"",
"## 14. Dati grezzi e file di lavoro","",
"- `/data/market-data.json` (dati ISTAT, DataReportal, PoliMi, benchmark, con tag e URL)",
"- `/data/keywords.csv` (34 keyword, Ubersuggest, 23/11/2026) e `/research/02e-keyword.md`",
"- `/data/competitors.csv` e `/research/02b-concorrenti.md` (19 righe, comprese 2 non verificabili)",
"- `/data/accounts.csv` e `/research/02c-trend-contenuti.md` (15 account)",
"- `/research/02d-canali-professionisti.md` (associazioni e canali)",
"- `/research/01-audit-brand.md` (audit e scorecard)",
"- Calendario: `/output/calendario-editoriale.xlsx`",
"",
"## 15. Fonti","",]
for i,(t,u) in enumerate(SOURCES,1): out.append(f"{i}. {t} – {u} (consultato 23/11/2026)")
open("/home/user/outputclaude/output/report-interno.md","w").write("\n".join(out)+"\n")
print("md ok")
