"""Copy degli annunci LinkedIn per Retica, focus LOGISTICA (DDT, unità di misura, listini/prezzi).
Piano per 2.000 €/mese: SENZA lead magnet (nessun contenuto da scaricare) e SENZA video. A03 (guida) ritirato.
Fonte unica: genera ads.json (mockup/deck) e output/copy_annunci.md.
Regola: i claim nei campi intro/headline sono SOLO quelli presenti su retica.ai (verificati 19/11/2026).
Il campo 'se_confermato' contiene varianti più forti (conversione unità, verifica prezzi): NON usarle finché Retica non conferma."""
import json, sys

LIM = dict(intro_total=600, intro_hook=150, headline=70, desc=100, card=45)

ADS = [
 dict(id="A01", funnel="TOFU", leva="DDT", fmt="Immagine singola 4:5 (post sponsorizzato)", obj="Visite al sito web", angle="DDT: il costo di riscrivere le righe",
  intro_A="Quante righe di DDT ricopia il tuo team ogni giorno? Retica le legge e le inserisce nel gestionale al posto suo.",
  intro_B="In logistica ogni minuto di magazzino conta. Eppure c'è ancora chi riscrive a mano i DDT. Esiste un'alternativa.",
  headline_A="DDT nel gestionale, senza riscrivere le righe",
  headline_B="Il magazzino non aspetta che qualcuno digiti",
  desc="Retica legge i DDT, qualunque sia il layout del fornitore.",
  cta="Scopri di più", dest="Landing dedicata alla logistica (o retica.ai/logistica) con UTM [DA CONFERMARE]",
  cover="Domanda a tutto schermo + pila di DDT",
  notes="Sostituisce il video del primo piano: con 2.000 €/mese non si investe in video all'inizio (il video resta una fase 2). La pagina retica.ai/logistica esiste già.",
  se_confermato=None),
 dict(id="A02", funnel="TOFU", leva="Unità di misura", fmt="Thought Leader Ad (post del founder/referente Retica)", obj="Visualizzazioni sito / Engagement", angle="Unità di misura: colli, pezzi, pallet",
  intro_A="Colli, pezzi, pallet, kg: ogni fornitore scrive l'unità di misura a modo suo. E ogni giorno qualcuno la ricontrolla riga per riga.",
  intro_B="Nel DDT c'è scritto 10 colli da 12 pezzi, il gestionale vuole i pezzi. Basta un errore di conto e il magazzino non torna. Come lo evitiamo?",
  headline_A="Quanto costa davvero il data entry manuale in azienda?",
  headline_B="Unità di misura scritte a modo loro: come uscirne",
  desc="Approfondimento dal blog di Retica.",
  cta="Scopri di più", dest="Blog Retica: 'Quanto costa davvero il data entry manuale' (A) · articolo sui listini fornitori (B), entrambi esistenti",
  cover="Quote card: 10 colli o 120 pezzi?",
  notes="Richiede un profilo persona (founder/referente) e il consenso a usarlo come Thought Leader Ad [DA CONFERMARE]. L'esempio 10×12 è solo aritmetica illustrativa. L'articolo sui listini cita 'unità di misura scritte in modo incoerente' (verificato).",
  se_confermato=dict(claim="Conversione automatica delle unità di misura (es. colli → pezzi) con le 'Condizioni' di Retica",
    intro="Colli, pezzi, pallet: Retica porta l'unità di misura del DDT in quella che il tuo gestionale si aspetta, con una regola che imposti una volta sola.",
    headline="Dall'unità del DDT a quella del tuo gestionale")),
 dict(id="A04", funnel="BOFU", leva="Listini / prezzi", fmt="Immagine singola 1:1 → Lead Gen Form", obj="Lead generation", angle="Listini fornitori: prezzi e unità in ordine",
  intro_A="Il listino arriva in PDF, con colonne che cambiano e unità scritte a modo loro. Retica lo legge e porta nel gestionale codici, prezzi e unità.",
  intro_B="Ogni listino nuovo è un copia-incolla da ricontrollare. Mandaci un tuo listino: in una demo lo vedi letto da Retica.",
  headline_A="Listini fornitori: dal PDF al gestionale, senza copia-incolla",
  headline_B="Prezzi e unità di misura del listino, già in ordine",
  desc="Codice articolo, descrizione, prezzo, unità di misura o confezione.",
  cta="Richiedi demo", dest="Lead Gen Form 'Richiedi demo'",
  cover="Listino PDF → dati: codice, prezzo, unità",
  notes="I campi estratti (codice articolo, descrizione, prezzo, unità di misura o confezione) sono quelli elencati nell'articolo sui listini di Retica [VERIFICATO]. Lo stesso articolo precisa che il confronto prezzi resta nel gestionale. Nessun contenuto da scaricare: si va dritti alla demo.",
  se_confermato=dict(claim="Verifica dei prezzi di listino (confronto col prezzo in uso, soglie di variazione) fatta da Retica",
    intro="Retica confronta i prezzi del nuovo listino con quelli in uso e segnala le variazioni oltre la soglia che imposti, prima dell'import.",
    headline="Verifica dei prezzi di listino, in automatico")),
 dict(id="A05", funnel="MOFU", leva="DDT + unità + prezzi", fmt="Carosello 5 card 1:1 (si legge nel feed, nessun download)", obj="Visite al sito web", angle="Il DDT riga per riga",
  intro_A="Ogni fornitore scrive il DDT a modo suo. Retica ne legge righe, codici, unità di misura e prezzi e li porta nel gestionale.",
  intro_B="Righe, unità di misura, prezzi: scorri e guarda cosa legge Retica in un DDT di magazzino.",
  headline_A="Il DDT cambia. Il risultato no.",
  headline_B="Righe, unità e prezzi: tutto nel gestionale",
  desc="DDT, fatture commerciali, certificati di origine e altri documenti di logistica.",
  cta="Richiedi demo", dest="Landing demo logistica con modulo breve",
  cards=["Il DDT, riga per riga","Righe e codici articolo","Unità: colli, pezzi, pallet","Prezzi: dal listino al gestionale","Prova Retica sui tuoi DDT"],
  cover="5 card: hook, righe, unità, prezzi, CTA",
  notes="I documenti elencati sono quelli della pagina retica.ai/logistica (documenti di trasporto, certificati di origine, fatture commerciali). Le card mostrano dati ESTRATTI, non convertiti.",
  se_confermato=dict(claim="Conversione unità e verifica prezzi",
    intro="Righe, unità di misura convertite, prezzi verificati: scorri e guarda cosa fa Retica su un DDT di magazzino.",
    headline="Righe, unità e prezzi: letti, convertiti, verificati")),
 dict(id="A06", funnel="MOFU", leva="DDT", fmt="Immagine singola 4:5", obj="Visite al sito web", angle="Integrazione con il tuo ERP / gestionale",
  intro_A="Il tuo gestionale resta quello che è. Retica gli porta i DDT già letti, in CSV, XML o JSON, con importazione via API o FTP.",
  intro_B="Non devi cambiare ERP per smettere di riscrivere i DDT. Retica è integrabile con qualsiasi ERP e prepara i dati nel formato che serve a te.",
  headline_A="Dal DDT al tuo ERP, senza trascrizioni",
  headline_B="Esporta i DDT in CSV, XML o JSON nel tuo gestionale",
  desc="Importazione via API o FTP, esportazione manuale o automatica.",
  cta="Scopri di più", dest="Pagina Integrazioni di retica.ai / landing demo logistica",
  cover="DDT → file CSV/XML/JSON → ERP/gestionale",
  notes="'Integrabile con qualsiasi ERP o CRM', API e FTP: dal sito [VERIFICATO]. Elenco WMS/ERP supportati da confermare.",
  se_confermato=None),
 dict(id="A07", funnel="BOFU", leva="DDT + unità di misura", fmt="Immagine singola 1:1 → Lead Gen Form", obj="Lead generation", angle="DDT con più unità di misura",
  intro_A="Colli, pezzi, pallet: ogni DDT ha le sue unità di misura. Mandaci alcuni tuoi DDT: in una demo vedi come Retica ne porta righe e unità nel gestionale.",
  intro_B="Un DDT con tante righe è tempo di digitazione e rischio di errore. Vedi come lo legge Retica, sui tuoi documenti e con il tuo gestionale.",
  headline_A="Vedi Retica sui tuoi DDT",
  headline_B="Righe e unità di misura del DDT, nel gestionale",
  desc="Richiedi la demo sui tuoi documenti.",
  cta="Richiedi demo", dest="Lead Gen Form 'Richiedi demo' (demo personalizzata sui DDT del prospect) [DA CONFERMARE fattibilità]",
  cover="Prima/dopo: DDT cartaceo vs righe e unità nel gestionale",
  notes="Settori: logistica, trasporti, magazzino. Demo personalizzata sui DDT del prospect: da confermare (tempi, numero di documenti, riservatezza).",
  se_confermato=dict(claim="Conversione automatica delle unità di misura",
    intro="Colli, pezzi, pallet: mandaci alcuni tuoi DDT e vedi Retica convertire le unità di misura in quelle del tuo gestionale.",
    headline="Unità di misura del DDT convertite in automatico")),
 dict(id="A08", funnel="BOFU", leva="DDT", fmt="Immagine singola 4:5 → Lead Gen Form", obj="Lead generation", angle="Prova sociale: DDT nell'ERP (Carraro)",
  intro_A="«Drastico abbattimento dei tempi di inserimento e degli errori umani.» Carraro ha digitalizzato l'inserimento dei DDT nel proprio ERP.",
  intro_B="I DDT della divisione ricambi di Carraro entrano nell'ERP quasi in automatico. La storia, in poche righe.",
  headline_A="DDT nell'ERP: meno tempo, meno errori",
  headline_B="La storia di Carraro con Retica",
  desc="Testimonianza di Dario Mazzocca, IT Manager.",
  cta="Richiedi demo", dest="Lead Gen Form 'Richiedi demo'",
  cover="Quote card con attribuzione (nome, ruolo, azienda)",
  notes="Testo dalla testimonianza sul sito (Dario Mazzocca, IT Manager, Carraro S.p.a., 13/05/2026). Serve il consenso a usare nome/azienda in un annuncio [DA CONFERMARE].",
  se_confermato=None),
 dict(id="A09", funnel="BOFU", leva="DDT", fmt="Immagine singola 1:1 (retargeting)", obj="Lead generation", angle="Prova sociale: logistica (Le Messaggerie Nazionali)",
  intro_A="Il data entry delle spedizioni era quasi tutto manuale. Le Messaggerie Nazionali l'hanno automatizzato e hanno migliorato l'efficienza del magazzino.",
  intro_B="Ti sei informato su Retica: ora vedila lavorare sui tuoi DDT. Più di 6.000 scansioni al giorno e 124 clienti attivi ci hanno già messo alla prova.",
  headline_A="Logistica: meno data entry, magazzino più efficiente",
  headline_B="Richiedi la tua demo di Retica",
  desc="Testimonianza di Federico Gatti, IT Manager.",
  cta="Richiedi demo", dest="Lead Gen Form 'Richiedi demo'",
  cover="Quote card logistica + 6.000+ scansioni · 124 clienti",
  notes="Testimonianza dal sito (Federico Gatti, IT Manager, Le Messaggerie Nazionali S.R.L., 17/12/2025). Consenso da confermare [DA CONFERMARE]. Numeri: sezione 'I nostri numeri'.",
  se_confermato=None),
 dict(id="A10", funnel="BOFU", leva="DDT", fmt="Conversation Ad (Message Ad)", obj="Lead generation", angle="Assistenza vicina / azienda italiana",
  intro_A="Ciao {FirstName}, ti scrivo da Retica, a Reggiolo (RE). Se in magazzino i DDT arrivano in PDF e le righe finiscono nel gestionale a mano, ti mostro in una demo come farle arrivare da sole. E ti seguiamo passo dopo passo nell'integrazione.",
  intro_B="Ciao {FirstName}, in Retica aiutiamo la logistica a smettere di riscrivere DDT e listini. Ti va di vedere come funziona sui tuoi documenti? Siamo a Reggiolo e ti seguiamo noi, dall'inizio.",
  headline_A="Una demo sui tuoi DDT?",
  headline_B="Smetti di riscrivere le righe dei DDT",
  desc="Oggetto del messaggio (max 60 caratteri).",
  cta="Prenota la demo | Parla con un esperto", dest="2 bottoni: calendario demo e Lead Gen Form",
  cover="Finestra di messaggio con 3 bottoni",
  notes="Mittente = persona reale di Retica [DA CONFERMARE]. 'Passo dopo passo' riprende le recensioni sul supporto. Frequenza (1 messaggio/utente/90 gg) da impostare in Campaign Manager.",
  se_confermato=None),
]

def check():
    errs=[]
    for a in ADS:
        for v in 'AB':
            t=a['intro_'+v]; h=a['headline_'+v]
            lim_int = 500 if a['id']=='A10' else LIM['intro_total']
            if len(t)>lim_int: errs.append((a['id'],'intro'+v,len(t)))
            lim_h = 60 if a['id']=='A10' else LIM['headline']
            if len(h)>lim_h: errs.append((a['id'],'headline'+v,len(h)))
        if len(a['desc'])>LIM['desc']: errs.append((a['id'],'desc',len(a['desc'])))
        for c in a.get('cards',[]):
            if len(c)>LIM['card']: errs.append((a['id'],'card',len(c)))
        sc=a.get('se_confermato')
        if sc:
            if len(sc['intro'])>LIM['intro_total']: errs.append((a['id'],'sc_intro',len(sc['intro'])))
            if len(sc['headline'])>LIM['headline']: errs.append((a['id'],'sc_headline',len(sc['headline'])))
    return errs

def hook(t, n=150):
    if len(t)<=n: return t
    return t[:n].rsplit(' ',1)[0]

if __name__=='__main__':
    errs=check()
    print('ERRORI LIMITI:',errs or 'nessuno')
    for a in ADS:
        a['hook_A']=hook(a['intro_A']); a['hook_B']=hook(a['intro_B'])
    json.dump(ADS,open('/home/user/outputclaude/analysis/ads.json','w'),ensure_ascii=False,indent=1)
    for a in ADS:
        print(f"{a['id']} introA={len(a['intro_A'])} introB={len(a['intro_B'])} hA={len(a['headline_A'])} hB={len(a['headline_B'])} desc={len(a['desc'])}")
    sys.exit(1 if errs else 0)
