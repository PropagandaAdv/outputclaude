# -*- coding: utf-8 -*-
"""Contenuto unico per docx cliente (senza tag) e report interno (con tag).
Blocchi: ("h1",t) ("h2",t) ("p",t,tag) ("bul",[(t,tag),...]) ("tab",header,rows,tag,note) ("box",titolo,testo) ("pb",)
tag: D=[DATO] C=[CLIENTE] I=[INFERENZA] V=[DA VERIFICARE] None
"""

SOURCES = [
 ("ISTAT, Indicatori demografici 2025 (nascite, 0-14 anni, famiglie)", "https://www.istat.it/wp-content/uploads/2026/03/Report_Indicatori-demografici_Anno-2025.pdf"),
 ("DataReportal, Digital 2026 Italy", "https://datareportal.com/reports/digital-2026-italy"),
 ("DataReportal, Digital 2027 Italy", "https://datareportal.com/reports/digital-2027-italy"),
 ("EconomyUp, Osservatori PoliMi: e-commerce B2c 2025", "https://www.economyup.it/?p=219271"),
 ("Teleborsa, investimenti digitali degli studi professionali (2 luglio 2026)", "https://www.teleborsa.it/News/2026/07/02/professionisti-cresce-la-digitalizzazione-l-ia-traina-gli-investimenti-negli-studi-187.html"),
 ("LaPresse, carenza di pediatri di famiglia (4 giugno 2026)", "https://www.lapresse.it/salute/sanita/2026/06/04/pediatri-di-famiglia-introvabili-ne-mancano-quasi-500-l80-in-3-regioni-del-nord/"),
 ("Camera dei deputati, memoria su logopedisti (26/11/2024)", "https://documenti.camera.it/leg19/documentiAcquisiti/COM12/Audizioni/leg19.com12.Audizioni.Memoria.PUBBLICO.ideGes.51507.26-11-2024-10-45-28.553.pdf"),
 ("Quotidiano Sanità, professioni sanitarie: TNPEE", "https://www.quotidianosanita.it/lavoro-e-professioni/viaggio-nelle-professioni-sanitarie-i-terapisti-della-neuro-e-psicomotricit-dell-et-evolutiva-intervista-al-presidente-andrea-bonifacio/"),
 ("Superads, CPM Meta Italia", "https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/italy"),
 ("Superads, CPC Meta Italia", "https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/italy"),
 ("Superads, CPL Meta Italia", "https://www.superads.ai/facebook-ads-costs/cost-per-lead/italy"),
 ("Superads, costo per install Meta Italia", "https://www.superads.ai/facebook-ads-costs/cost-per-app-install/italy"),
 ("Influee, benchmark TikTok Ads 2025", "https://influee.co/it/blog/tiktok-ads-benchmarks"),
 ("Socialinsider, benchmark Instagram", "https://www.socialinsider.io/blog/instagram-benchmarks/"),
 ("Hootsuite, frequenza di pubblicazione", "https://blog.hootsuite.com/how-often-to-post-on-social-media/"),
 ("Buffer, frequenza su Instagram", "https://buffer.com/resources/how-often-to-post-on-instagram/"),
 ("Unbounce, tassi di conversione delle landing page", "https://unbounce.com/landing-pages/whats-a-good-conversion-rate/"),
 ("Sito FamiClick", "https://famiclick.it/"),
 ("Scheda Google Play FamiClick", "https://play.google.com/store/apps/details?id=it.famiclick.app"),
 ("Scheda App Store FamiClick", "https://apps.apple.com/it/app/famiclick/id6748250560"),
 ("Ubersuggest, analisi keyword e dominio famiclick.it (Italia, 23/11/2026)", "file data/keywords.csv"),
 ("MioDottore Pro, piani e prezzi", "https://pro.miodottore.it/pricing-landing"),
 ("Eventbrite Italia, prezzi per organizzatori", "https://www.eventbrite.it/organizer/pricing/"),
 ("NostroFiglio, esperti", "https://www.nostrofiglio.it/i-nostri-esperti"),
 ("PianetaMamma", "https://www.pianetamamma.it"),
 ("iMamma, App Store Italia", "https://apps.apple.com/it/app/imamma-gravidanza-e-beb%C3%A8/id482550469"),
 ("Heepsy, influencer famiglia Italia (aggiornato 1/11/2026)", "https://www.heepsy.com/it/trova-influencer/instagram/famiglia"),
 ("Ardo Informatica", "https://ardoinformatica.it"),
 ("Capterra Italia (fonte terza, prezzi Doctolib/MioDottore) e altri dettagli: vedere research/02b-concorrenti.md", "research/02b-concorrenti.md"),
 ("Elenco organizzazioni e canali per professionisti", "research/02d-canali-professionisti.md"),
]
# indici fonti (1-based) usati nel testo come [n]

DOC = []
A = DOC.append

# ---------------------------------------------------------------- 1 EXEC SUMMARY
A(("h1", "1. Executive summary"))
A(("p", "FamiClick ha un'idea chiara e un bisogno reale alle spalle: un'app gratuita che mette in un unico posto salute, attività per bambini, bonus e diritti, negozi e servizi locali. Per funzionare come marketplace ha però bisogno di una cosa prima di tutto: un catalogo ricco di professionisti. Per questo la nostra proposta mette al primo posto, nei primi quattro mesi, il lato offerta (specialisti, fotografi, organizzatori di eventi), e solo dopo l'attivazione dei genitori.", None))
A(("box", "I 3 insight più importanti", [
 "1. Oggi i professionisti non hanno un motivo né un percorso per iscriversi. Sul sito non esiste una pagina, una sezione o un invito all'azione a loro dedicati: l'unico accenno è una frase nella scheda dell'App Store («Se sei uno specialista, c'è posto anche per te!») [18][20].",
 "2. Il brand è la prima cosa da sistemare. Sul sito convivono «FamiClick» e «Familink» (icona del sito, modulo newsletter e link Instagram puntano a Familink) e negli store lo sviluppatore compare come persona fisica, mentre il sito cita ArdoInformatica [18][19][20]. In più mancano le prove sociali: 100+ download su Google Play e 2 valutazioni su App Store [19][20].",
 "3. I genitori cercano molto, i professionisti quasi per nulla. Su Google «assegno unico» ha circa 110.000 ricerche al mese, «congedo parentale» 74.000, «pediatra vicino a me» 4.400, mentre le ricerche dirette dei professionisti («come trovare clienti fotografo») sono 10 al mese [21]. I professionisti vanno quindi raggiunti con contatto diretto, social e associazioni di categoria, non aspettando che ci trovino da Google.",
]))
A(("p", "Cosa proponiamo, in sintesi:", None))
A(("bul", [
 ("Mese 1 – Fondamenta: un solo nome e un solo profilo, una landing page «Per i professionisti», bio e link in bio, kit grafico, calendario editoriale e report mensile.", None),
 ("Mesi 2–4 – Acquisizione professionisti: programma «Partner Fondatore» (primi 100 professionisti, in 1–2 città pilota), Reel e TikTok di presentazione, outreach diretto, associazioni di categoria, campagne a pagamento su Meta e TikTok.", None),
 ("Mesi 5–6 – Attivazione genitori: con un catalogo popolato, contenuti su bonus, eventi del weekend e specialisti vicino a te, e campagne di download.", None),
 ("Obiettivo a 6 mesi: 360 contatti qualificati (il dato indicato dal cliente) e circa 100 professionisti iscritti, con ipotesi di conversione esplicitate e da validare dal secondo mese.", "C"),
]))
A(("p", "Dove i dati non sono verificabili (follower dei profili social, recensioni testuali, numero attuale di professionisti iscritti) lo diciamo chiaramente e li indichiamo come primo passo di misurazione, senza stimarli.", None))
A(("pb",))

# ---------------------------------------------------------------- 2 QUESTIONARIO
A(("h1", "2. Cosa ci hai detto: il questionario e la nostra lettura"))
A(("p", "Il questionario compilato il 19/11/2026 ci dice molto su cosa vuoi ottenere e meno su chi devi convincere. Qui sotto le risposte, con la nostra lettura.", None))
A(("tab", ["Tema", "La tua risposta", "La nostra lettura"], [
 ["Cliente ideale (domande 2–6)", "Donna, 33 anni, impiegata, in Italia, usa Instagram e TikTok ogni giorno", "È il genitore, cioè il lato domanda. Il professionista da acquisire, che è la priorità, non è ancora descritto: lo costruiamo noi con la ricerca (sez. 5)."],
 ["Parole su Google (8)", "«Specialista, evento, fotografo»", "Sono le categorie di professionisti su cui puntare per prime."],
 ["Formato preferito (9)", "Video brevi e dinamici (Reel/TikTok)", "Ne facciamo il cuore del piano."],
 ["Problema (10–11)", "Dare visibilità alla pagina e riempire l'app di persone che la usino come vetrina; timore che l'app non funzioni come dovrebbe", "È il problema di FamiClick, non quello del professionista. Per convincere il professionista dobbiamo parlare dei suoi problemi: trovare clienti, farsi vedere nella propria zona, spendere poco."],
 ["Soluzioni già provate (12)", "«Poca attenzione e costanza»", "Costanza, calendario e report mensili misurabili sono il punto centrale di questa proposta."],
 ["Risultato desiderato (13–15)", "Più download. Vita più semplice, meno tempo perso. Punti di forza: tutto a portata di click, meno tempo perso, più tempo a disposizione", "Il messaggio per i genitori è già chiaro. Per i professionisti serve un messaggio diverso (sez. 6)."],
 ["Obiezione (16)", "Poca conoscenza dell'app", "Rispondiamo con tutorial brevi («iscriviti in 2 minuti») e prove sociali."],
 ["Rassicurazioni e lead magnet (17–18)", "Non indicati", "Sono leve che proponiamo noi (sez. 9)."],
 ["Budget ads (19)", "Da definire insieme alla strategia", "Ti presentiamo tre scenari (sez. 9)."],
 ["Obiettivo contatti (20)", "Più di 360 in 6 mesi", "Lo trasformiamo in KPI. Ci serve capire se «contatto» significa professionista iscritto, lead, download o altro (sez. 11)."],
], "C", "Fonte: questionario cliente del 19/11/2026."))
A(("p", "Una nota di metodo: dalla tua risposta alla domanda 12 («poca attenzione e costanza») deduciamo che le esperienze precedenti non abbiano avuto continuità. Per questo nel piano la regolarità è un impegno misurabile, non una promessa.", "I"))

# ---------------------------------------------------------------- 3 AUDIT
A(("h1", "3. Audit di FamiClick oggi"))
A(("p", "Abbiamo analizzato sito, schede degli store e social il 23/11/2026. Dove un dato non era leggibile (Instagram blocca la lettura automatica, TikTok e Facebook non mostrano i profili senza accesso) lo segnaliamo come da verificare e non lo stimiamo.", None))
A(("h2", "3.1 Sito famiclick.it"))
A(("bul", [
 ("Pagina unica ben leggibile: titolo «FamiClick – L'app per genitori: supporto, info e community», quattro categorie (Healthcare, Sport e svago, Leggi e diritti, Utilities) e tre FAQ [18].", "D"),
 ("Tono caldo, rassicurante, con il «tu»: coerente con il claim «Sempre al tuo fianco» [18].", "D"),
 ("Nessuna pagina o invito all'azione per i professionisti: tutta la comunicazione parla al genitore [18].", "D"),
 ("Brand ambiguo: l'icona del sito e il modulo newsletter («Non perderti il lancio di Familink!») usano il nome Familink, e il link Instagram porta a @familinkapp [18].", "D"),
 ("Visibilità su Google quasi nulla: autorevolezza di dominio 2, 3 parole chiave posizionate (non pertinenti) e circa 1 visita al mese [21].", "D"),
 ("Il sito è realizzato da ArdoInformatica, web agency e software house di Reggio Emilia [18][28].", "D"),
]))
A(("h2", "3.2 Google Play e App Store"))
A(("tab", ["", "Google Play", "App Store"], [
 ["Descrizione breve", "«Il mondo dei genitori a portata di click!»", "Elenca specialisti, sport, bonus, eventi. Chiude con: «Se sei uno specialista, c'è posto anche per te!»"],
 ["Download", "100+", "Non pubblicati da Apple"],
 ["Valutazione", "Non letta (da verificare)", "5,0 su 5 con 2 valutazioni"],
 ["Ultimo aggiornamento", "20 ottobre 2026", "Non letto"],
 ["Prezzo", "Gratis, con indicazione «acquisti in-app»", "Gratis; richiede iOS 17 o successivo"],
 ["Sviluppatore mostrato", "Persona fisica", "Persona fisica"],
], "D", "Fonti: [19] [20], consultate il 23/11/2026. Le recensioni testuali non erano sufficienti per un'analisi del sentiment."))
A(("p", "Dalla nostra analisi emerge che la scheda App Store è l'unico punto in cui un professionista viene invitato a partecipare, ma senza spiegare come. E che la differenza tra il nome dello sviluppatore negli store e quello del sito può generare dubbi in chi valuta se fidarsi, soprattutto un professionista che deve inserire i propri dati.", "I"))
A(("p", "Il sito dichiara che l'app è gratuita e che «alcuni contenuti o servizi extra potranno essere opzionali», mentre Google Play segnala acquisti in-app: va chiarito cosa sia previsto per i professionisti, perché sarà la prima domanda che faranno.", "V"))
A(("h2", "3.3 Social"))
A(("bul", [
 ("Instagram @famiclick e @familinkapp: i profili non sono leggibili dall'esterno senza accesso, quindi follower, frequenza di pubblicazione, formati ed engagement vanno rilevati insieme a te nel primo mese.", "V"),
 ("TikTok e Facebook: non risulta verificabile una presenza ufficiale. Una ricerca web su «famiclick» non restituisce risultati pertinenti.", "V"),
]))
A(("h2", "3.4 Scorecard"))
A(("tab", ["Criterio", "Voto (1–5)", "Perché"], [
 ["Chiarezza della proposta per i genitori", "3", "Quattro aree chiare ma generiche; mancano esempi concreti e prove"],
 ["Chiarezza della proposta per i professionisti", "1", "Assente dal sito, una sola frase negli store"],
 ["Coerenza del brand", "2", "FamiClick e Familink convivono; sviluppatore diverso tra sito e store"],
 ["Presenza social", "da rilevare", "Profili non leggibili; il sito rimanda al profilo Familink"],
 ["Prova sociale", "1", "100+ download, 2 valutazioni, nessuna testimonianza"],
 ["Percorso di iscrizione dei professionisti", "1", "Nessuna pagina, modulo o invito all'azione trovato"],
 ["Visibilità su Google", "1", "Autorevolezza 2, circa 1 visita al mese"],
], "I", "Voti assegnati dal team Propaganda Adv sulla base degli elementi sopra."))
A(("pb",))

# ---------------------------------------------------------------- 4 MERCATO
A(("h1", "4. Il mercato e i concorrenti"))
A(("h2", "4.1 Il contesto in numeri"))
A(("tab", ["Tema", "Dato", "Fonte"], [
 ["Nascite in Italia", "355.000 nel 2025 (−3,9% sul 2024); 1,14 figli per donna", "[1]"],
 ["Bambini 0–14 anni", "6,85 milioni (11,6% della popolazione) al 1/1/2026, 168.000 in meno in un anno", "[1]"],
 ["Famiglie", "26,6 milioni; le coppie con figli sono il 28,4%", "[1]"],
 ["Utenti social in Italia", "44,1 milioni a ottobre 2026 (74,9% della popolazione)", "[3]"],
 ["Instagram (pubblico raggiungibile con le inserzioni)", "28,2 milioni a fine 2026 (29,9 milioni a fine 2025)", "[2][3]"],
 ["TikTok (18+)", "23,5 milioni a fine 2026 (22,0 milioni a fine 2025)", "[2][3]"],
 ["E-commerce B2c Italia 2025", "62,3 miliardi di euro (+7%), di cui servizi 22,3 miliardi (+9%)", "[4]"],
 ["Pediatri di libera scelta", "6.284 attivi al 1/1/2025; carenza di almeno 497 nel 2026", "[6]"],
 ["Logopedisti", "13.982 iscritti (2023)", "[7]"],
 ["Terapisti neuro e psicomotricità dell'età evolutiva", "«Quasi 6.000» (dato 2021, approssimato)", "[8]"],
], "D", "Dati consultati il 23/11/2026. Non siamo riusciti a trovare fonti ufficiali per il numero di fotografi di famiglia, animatori ed organizzatori di eventi, centri sportivi per bambini, negozi per l'infanzia e consulenti del sonno: li stimeremo con la ricerca sul campo nelle città pilota."))
A(("p", "Cosa significa: il numero di bambini cala (−168.000 in un anno), quindi il pubblico dei genitori si restringe lentamente, pur restando ampio (6,85 milioni di bambini). Per FamiClick il vantaggio competitivo non sta nel volume ma nell'utilità locale: servire bene poche città.", "I"))
A(("p", "I professionisti sanitari dell'infanzia sono in affanno sul fronte della domanda: mancano pediatri di famiglia nelle regioni del Nord [6]. Per uno specialista in studio privato, farsi trovare dalle famiglie è un'esigenza concreta, non un lusso.", "I"))
A(("h2", "4.2 Concorrenti e alternative"))
A(("p", "Abbiamo guardato app e siti per genitori, marketplace di servizi e community. Riportiamo solo ciò che abbiamo letto su fonti pubbliche; dove un dato non era raggiungibile (per esempio prezzi ufficiali o follower attuali) non lo mostriamo.", None))
A(("tab", ["Concorrente", "Cosa offre", "Modello per i professionisti", "Spunto per FamiClick"], [
 ["MioDottore (Docplanner)", "Ricerca medico, prenotazione, recensioni", "Profilo Basic gratuito (senza prenotazioni online); Premium e First Class a pagamento; piano Pro a prezzo su richiesta [22]", "L'ingresso gratuito è lo standard del settore sanitario: FamiClick può farne il suo punto di forza"],
 ["Doctolib Italia", "Prenotazione visite, agenda, promemoria", "Listino ufficiale non pubblicato; fonti terze parlano di abbonamento [29]", "Terreno già occupato per la prenotazione: FamiClick punta sulla vetrina per la famiglia"],
 ["ProntoPro", "Richiesta di preventivi per servizi", "Registrazione gratuita; si pagano contatti a credito (fonti terze) [29]", "I professionisti conoscono già il costo per contatto: la vetrina gratuita è un vantaggio"],
 ["Superprof", "Lezioni e corsi", "Annuncio gratuito, Premium a pagamento (dati da verificare) [29]", "Conferma il modello «gratis + upgrade»"],
 ["Eventbrite Italia", "Eventi e biglietteria", "Eventi gratuiti senza costi; commissioni solo sui biglietti a pagamento [23]", "Per gli organizzatori di eventi gratuiti è il termine di paragone"],
 ["NostroFiglio", "Portale per genitori, contenuti e speciali", "14 esperti nel team editoriale, canale pubblicitario per brand [24]", "Non è un catalogo prenotabile: spazio libero per una directory locale"],
 ["PianetaMamma", "Community e contenuti per mamme", "Esperti editoriali; ingresso non chiaro [25]", "Idem"],
 ["iMamma", "App per gravidanza e primi mesi", "Non risulta uno spazio per professionisti dalla scheda store [26]", "4,6 su 5 con 32.000 valutazioni: è il riferimento per chi cerca un'app per genitori"],
 ["KidooMap", "App per luoghi family-friendly", "Non letto; abbonamento per gli utenti", "App giovane con pochissime valutazioni: nicchia vicina ma diversa"],
], "D", "Fonti nelle note; dettaglio e CSV completo in data/competitors.csv. Social e follower dei concorrenti non sono stati letti."))
A(("box", "Spazio libero sul mercato", "Dai concorrenti analizzati emerge che i grandi media per genitori usano i professionisti come «esperti» editoriali, mentre i marketplace di servizi non sono pensati per la famiglia. Non abbiamo trovato un catalogo locale, gratuito e dedicato alla famiglia con profili di professionisti. È lo spazio che FamiClick può presidiare, a patto di non partire a mani vuote: serve massa critica in poche città."))
A(("h2", "4.3 Cosa cercano le persone su Google"))
A(("tab", ["Parola chiave", "Ricerche al mese", "Difficoltà SEO", "Lato"], [
 ["assegno unico", "110.000", "24", "Genitori"],
 ["congedo parentale", "74.000", "24", "Genitori"],
 ["logopedista", "27.100", "17", "Professionisti / genitori"],
 ["pediatra", "9.900", "13", "Genitori"],
 ["pediatra vicino a me", "4.400", "17", "Genitori"],
 ["consultorio vicino a me", "4.400", "26", "Genitori"],
 ["bonus famiglia 2026", "2.400 (picco a gennaio: 9.900)", "17", "Genitori"],
 ["logopedista vicino a me", "1.900", "15", "Genitori"],
 ["fotografo famiglia", "1.600", "36", "Genitori"],
 ["psicomotricista", "1.600", "33", "Professionisti"],
 ["come trovare clienti", "110", "29", "Professionisti"],
 ["sito web per professionisti", "70", "30", "Professionisti"],
 ["fotografo newborn", "70", "25", "Genitori"],
 ["come trovare clienti fotografo", "10", "17", "Professionisti"],
 ["app per genitori", "20", "28", "Genitori"],
], "D", "Fonte: Ubersuggest, Italia, 23/11/2026 [21]. Per molte parole chiave (eventi per bambini nel weekend, animatore feste, attività sportive per bambini, vetrina gratuita per professionisti) lo strumento non restituisce volumi: non significa che nessuno le cerchi, ma che i dati non sono disponibili. Da validare con Search Console dopo il lancio."))
A(("p", "Due conseguenze pratiche. Primo: per i professionisti non c'è una domanda di ricerca da intercettare, quindi li dobbiamo andare a cercare noi (social, contatto diretto, associazioni). Secondo: per i genitori ci sono argomenti con molto volume e poca concorrenza SEO (bonus, pediatra e logopedista vicino a me): sono ottimi per i contenuti social e per la newsletter. Bonus, assegno e congedo hanno picchi a gennaio e a ottobre, quindi i contenuti vanno pubblicati già a dicembre.", "I"))
A(("h2", "4.4 Cosa funziona sui social"))
A(("p", "Dal punto di vista dei contenuti, i casi italiani che abbiamo individuato seguono tre schemi: il creator mamma/papà con video di vita quotidiana e ironia (per esempio Alice Campello, 3,5 milioni di follower su Instagram secondo Heepsy, dato aggiornato al 1/11/2026 [27]); il professionista che divulga (pediatri e logopediste che compaiono come ospiti o esperti); il fotografo di famiglia e di nascita che mostra storie e dietro le quinte. Non abbiamo trovato fonti pubbliche su durata, frequenza e hook dei loro video: per questo nel piano indichiamo format da testare e un metodo di analisi manuale dei profili (research/02c-trend-contenuti.md), senza attribuire dati che non possiamo documentare.", "I"))
A(("p", "Benchmark generali utili per la pianificazione: engagement medio di Instagram 0,48% per follower (Reel 0,52%, caroselli 0,55%) [14]; frequenza consigliata 3–5 contenuti a settimana su Instagram e TikTok [15][16].", "D"))
A(("pb",))

# ---------------------------------------------------------------- 5 PERSONA
A(("h1", "5. Chi vogliamo raggiungere: le buyer persona"))
A(("p", "Nota importante: non esistono dati pubblici sul comportamento dei professionisti italiani dell'infanzia sui social. Le persone qui sotto sono ipotesi costruite da ricerca di settore e dall'esperienza dell'agenzia; le validiamo con 8–10 brevi interviste ai primi professionisti contattati, nel mese 1–2.", "V"))
A(("h2", "5.1 Lato offerta (priorità assoluta)"))
A(("tab", ["", "Giulia, fotografa di famiglia", "Dott.ssa Elena, specialista età evolutiva", "Marco, organizzatore di feste ed eventi"], [
 ["Chi è", "35–45 anni, freelance, newborn/famiglia/eventi", "38–50 anni, logopedista, psicomotricista o pediatra con studio privato", "30–45 anni, animazione, feste, laboratori, eventi per famiglie"],
 ["Obiettivi", "Più prenotazioni nella sua zona, riempire i mesi bassi, farsi riconoscere come specialista", "Pazienti nuovi con continuità, essere trovata vicino a casa, immagine professionale e affidabile", "Calendario pieno nei weekend, farsi trovare per feste e eventi, più passaparola"],
 ["Frustrazioni", "Dipendenza dal passaparola e da Instagram; tempo sottratto al lavoro per fare social; spese per pubblicità", "Poco tempo, vincoli deontologici sulla pubblicità sanitaria, diffidenza verso chi promette «pazienti»", "Lavori stagionali, concorrenza sui prezzi, costo di piattaforme che vendono contatti"],
 ["Obiezioni", "«Un'altra app?», «ci sono già utenti?», «è davvero gratis?»", "«È affidabile? Chi c'è dietro?», «posso apparire senza fare pubblicità?»", "«Quanti genitori la usano?», «cosa devo pagare?»"],
 ["Dove si informa", "Instagram, TikTok, gruppi di colleghi, associazioni (es. TAU Visual)", "Associazioni e ordini (FLI, FIMP, ecc.), gruppi di colleghi, LinkedIn, Instagram", "Instagram, Facebook, passaparola, Eventbrite"],
 ["Cosa la convince in 2 minuti", "Profilo gratuito con portfolio, badge Partner Fondatore, un Reel di presentazione gratuito", "Profilo informativo e sobrio, verifica dell'identità, nessuna logica a pagamento per contatto", "Eventi pubblicati gratis in categoria, visibilità nella sua città, nessuna commissione sugli eventi gratuiti"],
], "I", "Ipotesi di lavoro sui professionisti da validare con interviste. L'elenco di associazioni e canali verificati è in research/02d-canali-professionisti.md. Per i professionisti sanitari occorre verificare le regole su informazione e pubblicità sanitaria dei rispettivi ordini."))
A(("h2", "5.2 Lato domanda: il genitore"))
A(("tab", ["", "Chiara, mamma impiegata"], [
 ["Dati dal questionario", "Donna, 33 anni, impiegata, vive in Italia, usa ogni giorno Instagram e TikTok, preferisce video brevi, cerca «specialista, evento, fotografo»"],
 ["Cosa cerca", "Semplicità e tempo: trovare in un posto solo il pediatra, l'attività per i figli, il fotografo, le informazioni su bonus e congedi"],
 ["Frustrazioni", "Troppe fonti, informazioni sui bonus complicate, fatica a capire a chi affidarsi"],
 ["Cosa la convince", "Profili di professionisti vicini a lei, verificati, con tutto chiaro (contatti, orari, età dei bambini); contenuti rapidi e pratici"],
 ["Segnali dalla ricerca", "Ogni mese in Italia ci sono circa 110.000 ricerche per «assegno unico» e 74.000 per «congedo parentale»; 4.400 per «pediatra vicino a me» [21]"],
], "C", "Dati anagrafici e preferenze: questionario cliente. Arricchimento: ricerca keyword."))
A(("h2", "5.3 Il problema dell'uovo e della gallina"))
A(("p", "Un professionista si iscrive se ci sono genitori, e i genitori scaricano l'app se ci sono professionisti. Proponiamo di rompere il cerchio dal lato offerta con queste leve:", None))
A(("bul", [
 ("Programma «Partner Fondatore»: profilo gratuito per i primi 100 professionisti, con badge dedicato e priorità nella propria categoria. Serve confermare con te cosa è possibile promettere nel tempo (es. «gratis a vita» sul profilo base).", "V"),
 ("Contenuto gratuito come incentivo: un Reel di presentazione del professionista realizzato dall'agenzia (con limite sui primi iscritti).", "I"),
 ("Focus geografico su 1–2 città pilota: meglio 50 professionisti in una città che 50 in tutta Italia. La scelta delle città va fatta con te; un'ipotesi di partenza è l'area emiliana in cui opera lo sviluppatore.", "V"),
 ("Verifica e fiducia: badge «profilo verificato» e pagina «Chi siamo» con volti e nomi.", "I"),
 ("Referral «porta un collega»: priorità di visibilità a chi invita altri professionisti.", "I"),
 ("Numeri trasparenti: mostrare ogni mese quanti professionisti e quante famiglie ci sono, per costruire prova sociale.", "I"),
]))
A(("pb",))

# ---------------------------------------------------------------- 6 SWOT
A(("h1", "6. SWOT e posizionamento"))
A(("tab", ["Punti di forza", "Punti di debolezza"], [
 ["App già pubblicata su Android e iOS, gratuita [19][20]", "Brand doppio: FamiClick / Familink [18]"],
 ["Quattro aree di valore chiare per il genitore [18]", "Nessun percorso per i professionisti [18]"],
 ["Tono caldo e «tu» già definito [18]", "Poca prova sociale: 100+ download, 2 valutazioni [19][20]"],
 ["Spazio libero: nessun catalogo locale dedicato alla famiglia trovato tra i concorrenti analizzati", "Sito quasi invisibile su Google (autorevolezza 2) [21]"],
 ["Sviluppatore locale (Reggio Emilia) con cui coordinarsi [28]", "Sviluppatore negli store diverso dal nome sul sito [18][19][20]"],
], "I", "Elaborazione di Propaganda Adv."))
A(("tab", ["Opportunità", "Minacce"], [
 ["Pediatri e specialisti in cerca di visibilità: carenza di pediatri in diverse regioni [6]", "Concorrenti con base utenti consolidata (es. iMamma, 32.000 valutazioni [26]; MioDottore, Doctolib)"],
 ["Domanda altissima su bonus, assegni, congedi [21]", "Calo delle nascite: −3,9% nel 2025 [1]"],
 ["Il modello «gratis» è la norma per l'ingresso dei professionisti (es. MioDottore Basic [22])", "Professionisti sanitari soggetti a regole sulla pubblicità: possibile diffidenza"],
 ["Video brevi su Instagram e TikTok: 28,2 e 23,5 milioni di utenti raggiungibili [3]", "Se il percorso di iscrizione in app non è fluido, l'investimento in pubblicità si disperde"],
], "I", "Elaborazione di Propaganda Adv."))
A(("h2", "6.1 Posizionamento in una frase"))
A(("box", "Per i professionisti", "«La vetrina gratuita dove le famiglie della tua città ti trovano.»"))
A(("box", "Per i genitori", "«Tutto per la tua famiglia, a portata di click: meno tempo perso, più tempo per voi.»"))
A(("p", "Il messaggio per i genitori riprende i tuoi tre punti di forza (tutto a portata di click, meno tempo perso, più tempo a disposizione) (domanda 15 del questionario). Il messaggio per i professionisti parte invece da un beneficio concreto (essere trovati) e da una promessa semplice (gratis).", "C"))
A(("pb",))

# ---------------------------------------------------------------- 7 STRATEGIA
A(("h1", "7. La strategia: obiettivi, fasi, pilastri, formati"))
A(("h2", "7.1 Obiettivi a 6 mesi (dicembre 2026 – maggio 2027)"))
A(("tab", ["Obiettivo", "Traguardo", "Come lo misuriamo"], [
 ["A. Professionisti iscritti", "100 «Partner Fondatore» con profilo completo, nelle 1–2 città pilota", "Iscrizioni in app (conteggio fornito dal cliente)"],
 ["B. Contatti qualificati", "360 nei 6 mesi (obiettivo del cliente), dove «contatto» = professionista che compila il modulo o risponde a un contatto diretto (definizione da confermare)", "Modulo sulla landing, DM e email tracciati nel CRM"],
 ["C. Presenza social", "Profilo unico e coerente su Instagram e TikTok, 4 post a settimana senza interruzioni", "Calendario rispettato (%) e report mensile"],
 ["D. Attivazione genitori", "Da mese 5, campagna download con obiettivo definito sul costo per download misurato nei mesi precedenti", "Download da store, costo per download"],
], "C", "Il traguardo «360 contatti» è l'obiettivo indicato nel questionario (domanda 20); gli altri traguardi sono proposte dell'agenzia da concordare. Follower e crescita social: baseline da misurare nel mese 1, poi target relativi."))
A(("h2", "7.2 Il funnel «all'indietro» (scenario Crescita)"))
A(("p", "Per arrivare a 360 contatti e circa 100 professionisti iscritti, la composizione che proponiamo è:", None))
A(("tab", ["Canale", "Volume", "Calcolo e ipotesi"], [
 ["Campagne Meta + TikTok (mesi 2–6)", "175 contatti", "800 €/mese × 5 mesi = 4.000 €; costo per contatto di riferimento 22,9 € (mediana Meta Italia, tutti i settori) [11] ⇒ circa 175 contatti. Con un CPC di 0,50 € [10] servono circa 8.000 clic, cioè una conversione della landing del 2,2%."],
 ["Contatto diretto (DM, email, telefono)", "110 contatti", "Ipotesi: 550 professionisti contattati con messaggio personalizzato e risposta/interesse del 20%. Da validare nel mese 2."],
 ["Organico, referral, associazioni", "75 contatti", "Reel, community, partnership con associazioni di categoria, «porta un collega». Ipotesi da validare."],
 ["Totale", "360 contatti", "Dall'iscrizione al modulo all'iscrizione completa in app: ipotesi del 30% ⇒ circa 108 professionisti (obiettivo 100)."],
], "I", "Dati sourced: CPL Meta Italia [11], CPC [10]. Ipotesi dell'agenzia (non fonti): risposta del 20% al contatto diretto; conversione contatto→iscrizione del 30%; 75 contatti da canali organici. Se la landing raggiungesse i tassi di conversione di riferimento (5,1% nel settore healthcare, 6,6% mediana generale [17], dato globale 2024), il costo per contatto scenderebbe a circa 7,6–9,8 €."))
A(("h2", "7.3 Piano in tre fasi"))
A(("tab", ["Fase", "Cosa facciamo", "Esito atteso"], [
 ["Mese 1 – Fondamenta (dicembre 2026)", "Decidere nome e profilo unico; rilevare lo stato dei social; bio, link in bio e highlights; landing «Per i professionisti» con modulo da 2 minuti; kit grafico; 8–10 interviste a professionisti; calendario e primi 16 contenuti; impostare pixel e misurazioni", "Brand coerente, pagina di iscrizione pronta, prime 10–20 iscrizioni dai contatti diretti"],
 ["Mesi 2–4 – Acquisizione professionisti (gennaio–marzo 2027)", "Campagne «Partner Fondatore» su Meta e TikTok; Reel «Conosci…» dei primi iscritti; outreach DM e email; partnership con associazioni; referral; newsletter ai professionisti", "Circa 70–80 professionisti iscritti e catalogo credibile nelle città pilota"],
 ["Mesi 5–6 – Attivazione genitori (aprile–maggio 2027)", "Contenuti su bonus, eventi del weekend, specialisti vicino a te; campagne download con budget diviso tra professionisti e genitori; micro-influencer genitori; raccolta recensioni", "Obiettivo 100 professionisti raggiunto e primi download di genitori dalle città pilota"],
], "I", "Date indicative, partenza subordinata a conferma."))
A(("h2", "7.4 Pilastri editoriali"))
A(("tab", ["Pilastro", "Cosa racconta", "Mese 1", "Mesi 2–4", "Mesi 5–6"], [
 ["1. Vetrina del professionista", "«Conosci [nome]»: storia e servizi del professionista iscritto", "5%", "30%", "20%"],
 ["2. Come funziona", "Tutorial di 15 secondi: «iscriviti in 2 minuti»; risponde all'obiezione «poca conoscenza dell'app»", "25%", "15%", "5%"],
 ["3. Valore per i genitori", "Bonus, diritti, eventi del weekend, salute", "15%", "10%", "35%"],
 ["4. Prova sociale", "Testimonianze dei primi professionisti, numeri di crescita", "0%", "15%", "20%"],
 ["5. Community e dietro le quinte", "Contenuti dei genitori e del team, UGC", "10%", "5%", "15%"],
 ["6. Consigli per professionisti", "Mini-guide su come farsi trovare dalle famiglie (valore gratuito)", "45%", "25%", "5%"],
], "I", "Ripartizione percentuale dei contenuti per fase, da calibrare sui risultati del primo mese."))
A(("h2", "7.5 Formati ripetibili, con priorità ai video brevi"))
A(("tab", ["Pilastro", "Format", "Hook (primi 3 secondi)", "Struttura e durata", "CTA"], [
 ["Vetrina", "Conosci…", "«Lei è Giulia e fotografa i primi giorni di vita»", "Domanda al professionista, 3 immagini del lavoro, dove trovarlo; 30–40 s", "«Trovala su FamiClick»"],
 ["Vetrina", "Un giorno con…", "«Cosa fa una logopedista prima di aprire lo studio?»", "Dietro le quinte, 3 momenti; 30 s", "«Scopri gli specialisti vicino a te»"],
 ["Vetrina", "Domanda ai genitori", "«A che età si porta il bambino dal logopedista?»", "Domanda e risposta breve del professionista; 40 s", "«Altri specialisti in app»"],
 ["Come funziona", "Iscriviti in 2 minuti", "«Il tuo profilo online in 2 minuti, gratis»", "Schermate in sequenza con timer; 15–20 s", "«Link in bio»"],
 ["Come funziona", "Prima e dopo", "«Prima: nessuno ti trova. Dopo: ti trovano le famiglie della tua zona»", "Confronto visivo; 15 s", "«Iscriviti come Partner Fondatore»"],
 ["Come funziona", "Domande frequenti", "«È davvero gratis? Sì, e ti spiego perché»", "Risposta a una domanda alla volta; 25 s", "«Scrivici in DM»"],
 ["Valore genitori", "Bonus in 30 secondi", "«Hai un figlio piccolo? Controlla questo bonus»", "Una misura alla volta, con link alla fonte ufficiale; 30 s", "«Tutti i bonus in app»"],
 ["Valore genitori", "Weekend con i bambini", "«3 cose da fare sabato con i bambini a [città]»", "Elenco da 3 eventi pubblicati; 30 s", "«Trova eventi vicino a te»"],
 ["Valore genitori", "Chiedilo a…", "«Quando portare il bambino dal pediatra?»", "Risposta di un professionista iscritto; 40 s", "«Trova uno specialista vicino a te»"],
 ["Prova sociale", "I numeri del mese", "«In un mese, 30 professionisti ci hanno scelto»", "Numeri + volti; 20 s", "«Entra anche tu»"],
 ["Prova sociale", "Testimonianza", "«Perché mi sono iscritta»", "Il professionista racconta in prima persona; 30 s", "«Iscriviti»"],
 ["Prova sociale", "Prima recensione", "«Prima recensione! Grazie a Marta»", "Screenshot e commento; 15 s", "«Scrivi la tua recensione»"],
 ["Community", "Domanda del giorno", "«Qual è la cosa che ti fa perdere più tempo da genitore?»", "Sticker domande nelle Stories", "«Rispondi qui»"],
 ["Community", "Dietro le quinte", "«Così nasce un'app per le famiglie»", "Il team al lavoro; 30 s", "«Seguici»"],
 ["Community", "Contenuti dei genitori", "«Cosa non può mancare nella tua borsa»", "Risposte raccolte dalla community; 30 s", "«Racconta la tua»"],
 ["Consigli professionisti", "3 errori", "«3 errori che ti fanno perdere clienti online»", "Elenco con esempi; 30 s", "«Scarica la guida»"],
 ["Consigli professionisti", "Il profilo perfetto", "«Come si scrive una bio che porta clienti»", "Esempio reale; 30 s", "«Crea il tuo profilo»"],
 ["Consigli professionisti", "Mini-guida", "«Farsi trovare dalle famiglie della tua zona»", "Carosello da 6–8 slide", "«Salva e condividi con un collega»"],
], "I", "Format da validare con i test del primo mese."))
A(("p", "Canali per i professionisti. Oltre a Instagram e TikTok, per i professionisti sanitari e i fotografi ha senso testare LinkedIn con un post a settimana e la partecipazione, con profilo trasparente e rispettando le regole dei gruppi, ai gruppi di categoria. Non abbiamo trovato gruppi Facebook o LinkedIn italiani verificati per nome: il primo mese li censiamo a mano.", "V"))
A(("pb",))

# ---------------------------------------------------------------- 8 CALENDARIO + IDEE
A(("h1", "8. Calendario editoriale di esempio e 10 idee video"))
A(("p", "Il calendario copre quattro settimane (30 novembre – 27 dicembre 2026) e privilegia i contenuti per i professionisti. Frequenza: 4 contenuti a settimana su Instagram (3 Reel e 1 carosello), gli stessi Reel su TikTok, 1 post su LinkedIn e Stories quotidiane, in linea con la frequenza di 3–5 contenuti a settimana indicata dai benchmark [15][16]. La versione completa è nel file Excel allegato.", None))

CAL = [
 # settimana, giorno, piattaforma, pilastro, formato, hook, copy, CTA, obiettivo
 [1,"Lun 30/11","Instagram + TikTok","Come funziona","Reel 20 s","Il tuo profilo online in 2 minuti, gratis","Mostriamo schermata per schermata come ci si iscrive. Gratis, senza carta di credito.","Link in bio: iscriviti","Iscrizioni professionisti"],
 [1,"Mar 1/12","LinkedIn","Consigli professionisti","Post testo + immagine","3 errori che ti fanno perdere clienti online","Tre errori comuni, con un esempio, e un rimando alla guida gratuita.","Scarica la guida","Contatti qualificati"],
 [1,"Mer 2/12","Instagram + TikTok","Consigli professionisti","Reel 30 s","Come si scrive una bio che porta clienti","Una bio prima e dopo, con tre regole semplici.","Crea il tuo profilo","Contatti qualificati"],
 [1,"Gio 3/12","Instagram","Valore genitori","Carosello 6 slide","Bonus famiglia: cosa controllare a dicembre","Elenco delle misure con rinvio alle fonti ufficiali. Senza importi, per evitare errori.","Tutti i bonus in app","Download genitori / salvataggi"],
 [1,"Ven 4/12","Instagram + TikTok","Community","Reel 15 s + Stories","Cosa ti fa perdere più tempo da genitore?","Domanda aperta alla community, risposte nelle Stories.","Rispondi in Stories","Interazioni"],
 [2,"Lun 7/12","Instagram + TikTok","Vetrina","Reel 35 s","Conosci [nome]: la fotografa dei primi giorni","Intervista al primo Partner Fondatore (con consenso).","Trovala su FamiClick","Prova sociale"],
 [2,"Mar 8/12","LinkedIn","Come funziona","Post con screenshot","Perché abbiamo scelto la vetrina gratuita","Spieghiamo il programma Partner Fondatore e i limiti.","Iscriviti","Contatti qualificati"],
 [2,"Mer 9/12","Instagram + TikTok","Come funziona","Reel 25 s","È davvero gratis? Sì, e ti spiego perché","Risposta chiara alla prima obiezione, con le condizioni.","Scrivici in DM","Contatti qualificati"],
 [2,"Gio 10/12","Instagram","Consigli professionisti","Carosello 8 slide","Farsi trovare dalle famiglie della tua zona","Mini-guida in 8 passi.","Salva e condividi con un collega","Referral"],
 [2,"Ven 11/12","Instagram + TikTok","Valore genitori","Reel 30 s","Chiedilo a: quando portare il bambino dal pediatra?","Risposta di uno specialista iscritto, tono informativo.","Trova uno specialista vicino a te","Download genitori"],
 [3,"Lun 14/12","Instagram + TikTok","Prova sociale","Reel 20 s","I numeri del primo mese","Professionisti iscritti, città, categorie.","Entra anche tu","Prova sociale"],
 [3,"Mar 15/12","LinkedIn","Consigli professionisti","Post testo","Il profilo perfetto in 10 minuti: lista di controllo","Checklist scaricabile.","Scarica","Contatti qualificati"],
 [3,"Mer 16/12","Instagram + TikTok","Vetrina","Reel 30 s","Un giorno con una logopedista","Dietro le quinte dello studio.","Scopri gli specialisti","Prova sociale"],
 [3,"Gio 17/12","Instagram","Valore genitori","Carosello 5 slide","3 idee per le vacanze di Natale con i bambini","Eventi inseriti in app dagli organizzatori.","Trova eventi vicino a te","Interazioni / eventi"],
 [3,"Ven 18/12","Instagram + TikTok","Come funziona","Reel 15 s","Prima: nessuno ti trova. Dopo: ti trovano le famiglie","Prima e dopo del profilo.","Iscriviti come Partner Fondatore","Iscrizioni professionisti"],
 [4,"Lun 21/12","Instagram + TikTok","Community","Reel 30 s","Gli auguri della squadra: così nasce un'app per le famiglie","Dietro le quinte, volti del team.","Seguici","Fiducia nel brand"],
 [4,"Mar 22/12","LinkedIn","Prova sociale","Post con foto","Il bilancio di dicembre e cosa arriva nel 2027","Numeri e prossimi passi.","Iscriviti","Contatti qualificati"],
 [4,"Mer 23/12","Instagram + TikTok","Vetrina","Reel 30 s","Testimonianza: perché mi sono iscritto","Professionista racconta in prima persona.","Iscriviti","Prova sociale"],
 [4,"Gio 24/12","Instagram","Valore genitori","Carosello 5 slide","Bonus e congedi: cosa cambia a gennaio","Anticipazione, con rimando alle fonti ufficiali.","Salva il post","Download genitori / salvataggi"],
 [4,"Dom 27/12","Instagram (Stories)","Community","Stories","Il tuo proposito per il 2027: meno tempo perso?","Sondaggio nelle Stories.","Rispondi","Interazioni"],
]
A(("tab", ["Sett.", "Giorno", "Piattaforma", "Pilastro", "Formato", "Hook", "CTA", "Obiettivo"],
   [[str(r[0]), r[1], r[2], r[3], r[4], r[5], r[7], r[8]] for r in CAL], "I",
   "Per il copy completo e le note di pubblicazione vedere il file Excel allegato. Le misure su bonus vanno verificate sulle fonti ufficiali prima di ogni pubblicazione."))

IDEAS = [
 ("Professionisti","«Il tuo profilo online in 2 minuti, gratis»","Apri l'app → Crea profilo → inserisci nome, categoria, città → carica 3 foto → pubblica. Timer a schermo.","«Link in bio, iscriviti oggi»"),
 ("Professionisti","«Fotografi: 3 modi per essere trovati dalle famiglie della tua zona»","Tre esempi con schermate: scheda con portfolio, categoria, zona. Il terzo è l'app.","«Iscriviti come Partner Fondatore»"),
 ("Professionisti","«Sei un pediatra o un logopedista? Una domanda»","Pone la domanda: «come ti trovano i nuovi pazienti oggi?». Poi mostra il profilo informativo, sobrio e verificato.","«Scrivici per il tuo profilo»"),
 ("Professionisti","«Organizzatori di eventi: pubblica il tuo evento in 60 secondi»","Dal calendario dell'app al post dell'evento, con foto e data. Mostra come appare ai genitori.","«Pubblica il primo evento gratis»"),
 ("Professionisti","«Perché abbiamo deciso di non farti pagare»","Il fondatore spiega in 30 secondi il programma Partner Fondatore e cosa dà in cambio.","«Entra tra i primi 100»"),
 ("Genitori","«Hai un figlio piccolo? Controlla questo bonus prima di gennaio»","Tre misure, un secondo per ognuna, con rinvio alle fonti ufficiali. Nessun importo.","«Tutti i bonus in app»"),
 ("Genitori","«Sabato con i bambini: 3 idee a [città]»","Tre eventi pubblicati in app, con età consigliata e luogo.","«Trova gli eventi vicino a te»"),
 ("Genitori","«Pediatra vicino a te in 20 secondi»","Dalla ricerca al profilo: categoria Healthcare, zona, scheda.","«Scarica FamiClick»"),
 ("Genitori","«Mamma, papà: quanto tempo perdi a cercare il fotografo giusto?»","Scena in cui il genitore scorre decine di profili; poi la ricerca per categoria in app.","«Trova un fotografo vicino a te»"),
 ("Genitori","«Congedo parentale: le 3 domande che tutti fanno»","Tre domande con risposta sintetica e rimando alle fonti ufficiali.","«Il resto è nella sezione Leggi e diritti»"),
]
A(("h2", "8.1 Dieci idee di Reel e TikTok già scritte"))
A(("tab", ["#", "Per chi", "Hook (primi 3 secondi)", "Scaletta", "CTA"], [[str(i+1), a, b, c, d] for i,(a,b,c,d) in enumerate(IDEAS)], "I", "Prima di ogni pubblicazione sui temi bonus e salute verifichiamo i contenuti sulle fonti ufficiali. I contenuti con professionisti si pubblicano solo con loro consenso scritto."))
A(("pb",))

# ---------------------------------------------------------------- 9 LEAD MAGNET E PAID
A(("h1", "9. Lead magnet, offerte di ingresso e paid social"))
A(("h2", "9.1 Lead magnet e offerte di ingresso per i professionisti"))
A(("tab", ["Proposta", "Cosa è", "Perché funziona"], [
 ["Guida «10 modi per farti trovare dalle famiglie della tua zona»", "PDF di 8–10 pagine, scaricabile compilando il modulo", "Dà valore prima di chiedere l'iscrizione; raccoglie contatti"],
 ["Reel di presentazione gratuito", "Un video realizzato dall'agenzia per i primi iscritti (numero limitato da concordare)", "Incentivo concreto, produce contenuto per il profilo social"],
 ["Badge «Partner Fondatore»", "Distintivo sul profilo e priorità nella categoria per i primi 100", "Scarsità e riconoscimento"],
 ["Checklist «Il profilo perfetto in 10 minuti»", "Lista da compilare", "Riduce l'attrito dell'iscrizione"],
 ["Mini-webinar «Farsi trovare dalle famiglie»", "Sessione di 30 minuti con domande", "Costruisce fiducia con specialisti più scettici"],
], "I", "Il modulo di raccolta contatti richiede informativa privacy e consenso chiari; da condividere con chi cura la privacy dell'app."))
A(("h2", "9.2 Paid social: tre scenari (mesi 2–6)"))
A(("p", "Il budget è da definire insieme; ti presentiamo tre scenari. I valori di riferimento vengono da benchmark dichiarati e servono a dimensionare, non a promettere: i costi variano molto da mese a mese e per settore.", "C"))
A(("tab", ["", "Base", "Crescita (consigliato)", "Accelerazione"], [
 ["Budget mensile", "300 €", "800 €", "1.800 €"],
 ["Totale mesi 2–6", "1.500 €", "4.000 €", "9.000 €"],
 ["Ripartizione piattaforme", "Meta 70% / TikTok 30%", "Meta 70% / TikTok 30%", "Meta 60% / TikTok 40%"],
 ["Ripartizione per obiettivo", "Mesi 2–4: 100% professionisti; mesi 5–6: 70/30", "Mesi 2–4: 100% professionisti; mesi 5–6: 50/50 professionisti/genitori", "Mesi 2–4: 100% professionisti; mesi 5–6: 40/60"],
 ["Contatti attesi (CPL 22,9 €)", "circa 65", "circa 175", "circa 390"],
 ["Iscritti da pubblicità (ipotesi 30%)", "circa 20", "circa 52", "circa 118"],
 ["Pubblici", "Interessi su lavoro/professione e attività legate a famiglia e infanzia; lookalike sugli iscritti quando saranno almeno 100", "Come Base + pubblici personalizzati di chi interagisce con i Reel e chi visita la landing", "Come Crescita + test su più creatività e città"],
 ["Creatività", "3 Reel di prova + 1 carosello", "6 Reel + 2 caroselli + testimonianze", "10 Reel + testimonianze + test A/B"],
], "I", "Riferimenti: CPM Meta Italia circa 10,5 € [9]; CPC circa 0,50 € [10]; CPL mediano 22,9 € [11] (tutti i settori, Italia, luglio 2025–luglio 2026). Benchmark globale TikTok: CPM 13,26 $, CTR 1,77% [13]. Il costo per install di Meta in Italia è troppo instabile per una previsione (0,43 € di mediana su tutti i settori, 33,8 € di media per la categoria «marketplace», con pochi mesi di dati [12]): per la fase download genitori fisseremo il target dopo un test."))
A(("bul", [
 ("Targeting dei professionisti: Meta e TikTok non permettono sempre di selezionare per professione; useremo interessi collegati, pubblici personalizzati e lookalike. La disponibilità effettiva va verificata in piattaforma.", "V"),
 ("Per le inserzioni sanitarie valgono regole specifiche delle piattaforme e dei codici deontologici: le creatività per medici e specialisti saranno informative e senza promesse di risultati.", "V"),
 ("Reportistica di campagna: costo per contatto, iscrizioni completate, costo per iscrizione, frequenza, creatività che funzionano.", None),
]))
A(("h2", "9.3 Tattiche non a pagamento per i professionisti"))
A(("bul", [
 ("Contatto diretto: messaggi e email personalizzati, per categoria, con una proposta chiara (profilo gratuito + Reel). Nel rispetto delle norme su email commerciali e privacy.", "I"),
 ("Associazioni di categoria: abbiamo individuato organizzazioni attive e raggiungibili (per esempio TAU Visual per i fotografi, FLI per i logopedisti, FIMP per i pediatri, Confprofessioni). Si propone una collaborazione, non uno scambio forzato. Elenco in research/02d-canali-professionisti.md.", "D"),
 ("Micro-influencer genitori nelle città pilota, per portare i genitori quando il catalogo è pronto (mesi 5–6).", "I"),
 ("Referral «porta un collega»: priorità in categoria per chi invita.", "I"),
 ("Eventi locali e presenza nei luoghi frequentati da famiglie (negozi per l'infanzia, centri sportivi): flyer con QR code.", "I"),
]))
A(("pb",))

# ---------------------------------------------------------------- 10 KPI
A(("h1", "10. KPI e reporting"))
A(("p", "Il report arriva il 5 di ogni mese, sempre nello stesso formato, e confronta il mese con quello precedente e con l'obiettivo. È la risposta concreta al tema «poca attenzione e costanza».", None))
A(("tab", ["KPI", "Perché", "Fonte dati", "Baseline"], [
 ["Professionisti iscritti (totale e nuovi)", "KPI principale dei mesi 1–4", "Dati app forniti dal cliente", "Da rilevare (mese 1)"],
 ["Contatti qualificati (modulo, DM, email)", "KPI cliente: 360 in 6 mesi", "Modulo, CRM", "0"],
 ["Visite alla landing e tasso di compilazione", "Misura l'efficacia della pagina", "Analytics", "Da rilevare"],
 ["Clic dalla bio e dai contenuti", "Misura l'interesse verso la landing", "Instagram/TikTok", "Da rilevare"],
 ["Follower, copertura, interazioni (per Reel/caroselli)", "Salute dei profili", "Instagram/TikTok", "Da rilevare (profili non leggibili da noi)"],
 ["Costo per contatto e per iscrizione", "Efficienza delle campagne", "Meta/TikTok Ads", "—"],
 ["Download app (Android/iOS)", "KPI dei mesi 5–6", "Console degli store", "100+ su Android [19]"],
 ["Valutazioni e recensioni", "Prova sociale", "Store", "2 valutazioni su App Store [20]"],
 ["Rispetto del calendario (%)", "Costanza", "Agenzia", "—"],
], "I", ""))
A(("pb",))

# ---------------------------------------------------------------- 11 PROSSIMI PASSI
A(("h1", "11. Rischi, prossimi passi e domande aperte"))
A(("h2", "11.1 Le 5 azioni da fare subito (impatto/sforzo)"))
A(("tab", ["#", "Azione", "Impatto", "Sforzo"], [
 ["1", "Decidere il nome (FamiClick o Familink), allineare nome, icona, profili social, newsletter e nome sviluppatore negli store", "Alto", "Basso"],
 ["2", "Pubblicare una landing «Per i professionisti» sul sito, con modulo da 2 minuti e offerta Partner Fondatore", "Alto", "Medio"],
 ["3", "Verificare che l'iscrizione in app per un professionista funzioni davvero (tempi, passaggi, cosa vede il genitore) prima di portare traffico", "Alto", "Basso"],
 ["4", "Rifare bio, link in bio e highlights; aprire o allineare il profilo TikTok; kit grafico di base", "Medio", "Basso"],
 ["5", "Raccogliere le prime recensioni vere dai primi utenti e professionisti, senza incentivi sulla valutazione", "Medio", "Basso"],
], "I", ""))
A(("h2", "11.2 Rischi"))
A(("bul", [
 ("L'app potrebbe non essere pronta ad accogliere i professionisti (percorso di iscrizione, profilo, moderazione): se il primo contatto è deludente, la pubblicità lo amplifica.", "I"),
 ("Rebranding Familink in corso: cambiare nome a campagne avviate costa tempo e visibilità.", "V"),
 ("Poche recensioni: ogni valutazione negativa pesa molto, finché sono 2.", "I"),
 ("Professionisti sanitari: regole su informazione e pubblicità sanitaria; la comunicazione deve restare informativa.", "V"),
 ("Dati e privacy: raccolta contatti e profili di professionisti devono rispettare GDPR e norme sulle comunicazioni commerciali.", "V"),
 ("Titolarità dell'app negli store (persona fisica) rispetto al brand: da chiarire per fiducia e contratti.", "V"),
]))
A(("h2", "11.3 Domande per la prossima call"))
A(("bul", [
 ("Cosa intendi per «contatto» nel tuo obiettivo di 360 in 6 mesi: professionista iscritto, lead, download o altro?", None),
 ("Qual è oggi il numero di professionisti iscritti e di utenti attivi?", None),
 ("Qual è lo stato di Familink: nome definitivo, nuovo prodotto o rebranding? E chi è il titolare dell'account negli store?", None),
 ("Quali città o province vuoi presidiare per prime?", None),
 ("Esiste già un percorso di iscrizione per i professionisti? Quanto tempo richiede? Cosa vedono?", None),
 ("Cosa è gratuito per i professionisti e per quanto tempo (cosa significano gli «acquisti in-app»)?", None),
 ("Chi gestisce profili, password e pubblicità oggi? Abbiamo accesso agli insight di Instagram?", None),
 ("Quali sono i KPI di successo per te a 3 e 6 mesi, e il budget pubblicitario indicativo?", None),
 ("Puoi indicarci account o brand che segui (domanda 7 del questionario) e rassicurazioni disponibili (domanda 17)?", None),
]))
A(("h2", "11.4 Cosa non abbiamo potuto verificare"))
A(("bul", [
 ("Follower, frequenza e engagement dei profili Instagram, TikTok e Facebook: non leggibili dall'esterno.", None),
 ("Valutazione e recensioni testuali su Google Play.", None),
 ("Numero di fotografi, animatori, centri sportivi per bambini, negozi per l'infanzia e consulenti del sonno: nessuna fonte ufficiale reperita.", None),
 ("Prezzi ufficiali di Doctolib, ProntoPro e Superprof: letti solo da fonti terze o non raggiungibili.", None),
 ("Gruppi Facebook e LinkedIn di professionisti: non verificati per nome.", None),
]))
A(("pb",))
