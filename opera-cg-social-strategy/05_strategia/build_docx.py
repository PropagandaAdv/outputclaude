# -*- coding: utf-8 -*-
import sys, json; sys.path.insert(0, '.')
from docx_helpers import *
from content import *
import market_sections as MS

SC = json.load(open('scenari.json'))
doc = new_doc()
footer_pages(doc, 'Propaganda Adv  |  Analisi e strategia social – Opera Costruzioni Generali')

# ---------------- COPERTINA ----------------
for _ in range(5): doc.add_paragraph()
para(doc, 'PROPAGANDA ADV', 13, ARANCIO, WD_ALIGN_PARAGRAPH.CENTER)
para(doc, 'Proposta di Social Media Management', 12, GRIGIO, WD_ALIGN_PARAGRAPH.CENTER)
doc.add_paragraph()
p = para(doc, '**Analisi di mercato e strategia social**', 30, BLU, WD_ALIGN_PARAGRAPH.CENTER)
para(doc, 'per', 12, GRIGIO, WD_ALIGN_PARAGRAPH.CENTER)
para(doc, '**OPERA COSTRUZIONI GENERALI**', 24, ARANCIO, WD_ALIGN_PARAGRAPH.CENTER)
para(doc, 'Consorzio – Imola · Milano · Bari', 11, GRIGIO, WD_ALIGN_PARAGRAPH.CENTER)
for _ in range(6): doc.add_paragraph()
para(doc, 'Obiettivo: più visibilità del brand e +270 contatti qualificati in 6 mesi', 12, BLU, WD_ALIGN_PARAGRAPH.CENTER)
para(doc, '26 novembre 2026', 10, GRIGIO, WD_ALIGN_PARAGRAPH.CENTER)
para(doc, 'Documento riservato. Le analisi sono basate su fonti pubbliche consultate il 26/11/2026.', 8, GRIGIO, WD_ALIGN_PARAGRAPH.CENTER)
page_break(doc)

doc.add_heading('Indice', 1); add_toc(doc); page_break(doc)

# ---------------- 1 EXEC SUMMARY ----------------
doc.add_heading('1. Executive summary', 1)
box(doc, 'In sintesi', [
 '**Situazione**: Opera è un consorzio solido (certificazioni complete, 25 anni di storia, portafoglio lavori 100 M) ma percepito come "impresa edile": il sito non parla di fotovoltaico/EPC in home, i casi studio non esistono e i social sono quasi fermi (YouTube senza video dal 2020).',
 '**Opportunità**: la filiera completa "dal progetto alla manutenzione" non è presentata come claim unico dai competitor analizzati; Conto Termico, fotovoltaico/agrivoltaico e riqualificazione dei condomini sono temi con domanda reale.',
 '**Cosa proponiamo**: un presidio social su LinkedIn (primario B2B), Facebook/Instagram (terreni e condomini) e riattivazione di YouTube, con 6 pilastri di contenuto, 6 lead magnet (uno per segmento) e campagne a pagamento.',
 '**Risultati attesi**: con lo scenario consigliato (€5.000/mese di ads) stimiamo **~280 contatti in 6 mesi** (intervallo 205–427), in linea con l\'obiettivo di 270. Con il budget base (€2.500/mese) ci fermiamo a ~158: non basta.',
 '**Da decidere subito**: budget, priorità dei segmenti, claim, gestione dei lead, produzione di casi studio e video.'])
para(doc, '**Il punto di partenza.** Dal brief emerge un cliente con sei pubblici molto diversi: committenti privati di grandi opere, sviluppatori fotovoltaici, proprietari di terreni, amministratori di condominio, Pubblica Amministrazione e imprese da consorziare. Oggi il brand parla a tutti con lo stesso messaggio istituzionale. Il lavoro da fare è dare a ciascun pubblico un motivo preciso per fidarsi: un solo interlocutore, tempi e costi certi, certificazioni verificabili, esempi reali.')
para(doc, '**Cosa c\'è da sapere sui dati.** Instagram, Facebook e LinkedIn non sono leggibili senza accesso (login/blocchi): follower, frequenza e inserzioni attive del cliente e dei competitor sono quindi da rilevare manualmente. Lo diciamo con chiarezza nell\'appendice: non abbiamo stimato metriche che non potevamo vedere.')
page_break(doc)

# ---------------- 2 BRIEF ----------------
doc.add_heading('2. Il brief: obiettivi e target', 1)
box(doc, 'In sintesi', ['Obiettivo: visibilità del brand e richieste di contatto qualificate; target +270 contatti in 6 mesi (~45 al mese).', 'Pubblico: 35-70 anni, decisori e tecnici, in tutta Italia con maggiore presenza vicino alle sedi di Imola, Milano e Bari.', 'Piattaforme già usate: Instagram, Facebook, LinkedIn; formato preferito: immagini e grafiche chiare con testo.'])
table(doc, ['Tema', 'Dal brief del cliente [DAL CLIENTE]'], [
 ['Cliente ideale', '35-70 anni; decisori aziendali e tecnici, RUP e tecnici comunali, amministratori di condominio (35-60), proprietari di terreni e aziende agricole (45-70), studi di progettazione'],
 ['Localizzazione', 'Tutto il territorio nazionale, con maggiore presenza nelle aree delle tre sedi (Imola, Milano, Bari)'],
 ['Problema principale', 'Un interlocutore unico, solido e affidabile; EPC con SOA OG9 e capacità finanziaria; procedure GSE/PPP complesse per i Comuni; imprese troppo piccole per i grandi appalti'],
 ['Paure', 'Ritardi, costi extra, contenziosi; impresa non solida o senza certificazioni; perdere finestre di connessione o incentivi'],
 ['Alternative provate', 'Frammentare tra più imprese; grandi contractor poco flessibili e costosi; installatori FV piccoli non strutturati per impianti da 10-15 ettari'],
 ['3 punti di forza', 'Filiera completa; solidità e certificazioni (SOA OG1/OG9/OG11/OS6/OS28/OS30; ISO 9001/14001/45001/37001/50001; EMAS; SA8000; ESCo UNI CEI 11352); dimensione nazionale e oltre 25 anni, più di 500 addetti'],
 ['Obiezioni', '"Non sapevo che faceste fotovoltaico/EPC"; "Un consorzio è affidabile come un\'impresa unica?"; Comuni: "È davvero a costo zero? È troppo complicato"'],
 ['Rassicurazioni', 'Casi studio / Prima e Dopo; certificazioni o premi di settore'],
 ['Account/riviste seguiti', 'Nessuna risposta: ricostruiti con la ricerca (sezione 4)'],
 ['Budget ads', 'Da definire insieme, in base alla strategia (proposti 3 scenari alla sezione 8)'],
], widths=[3.5, 13.5])
doc.add_heading('I 6 segmenti', 2)
table(doc, ['Cod.', 'Segmento', 'Chi sono [DAL CLIENTE]'], [[k, SEGMENTI[k], PERSONAS[i]['ruolo']] for i, k in enumerate(SEGMENTI)], widths=[1.2, 4, 11.8])
page_break(doc)

# ---------------- 3 AUDIT ----------------
doc.add_heading('3. Audit del sito e dei canali social', 1)
box(doc, 'In sintesi', [
 'Il sito è solido sulle certificazioni e su Conto Termico/Associarsi, ma **non racconta FV/EPC** in home, **non ha casi studio** né landing per segmento.',
 'Tracciamenti: GTM e Meta Pixel presenti; Google Analytics fermo a Universal Analytics (dismesso); **LinkedIn Insight Tag non rilevato**.',
 'Social: **solo YouTube è leggibile** senza login: 99 iscritti, ultimo video del 2020. Instagram, Facebook, LinkedIn e Ad Library non consultabili da questa analisi.'])
doc.add_heading('3.1 Sito operacg.com (consultato il 26/11/2026)', 2)
table(doc, ['Segmento', 'Dove è servito sul sito', 'Valutazione'], [
 ['S1 Committenti privati', 'Home + Attività (categorie senza casi)', 'Debole: nessun caso con numeri; "general contractor" solo nel title'],
 ['S2 Sviluppatori FV (EPC)', 'Pagina /epc/ (testo generico del 2023)', 'Debole: niente MWp, MT, SOA OG9, referenze'],
 ['S3 Proprietari terreni', 'Nessuna pagina', 'Assente'],
 ['S4 Condomini', 'Una riga in Servizi (crediti d\'imposta / CER)', 'Assente/debole'],
 ['S5 PA – Conto Termico', '/conto-termico/ (30/10/2025)', 'Buona base: procedura in 4 step, interventi per SOA'],
 ['S6 Imprese', '/associarsi/ (07/11/2025)', 'Buona: benefici chiari + form'],
], widths=[3.6, 6.4, 7])
bullets(doc, [
 '**Numeri in home** [VERIFICATO nel codice]: fatturato 80 M, portafoglio lavori 100 M, 170 contratti attivi, 1000 lavoratori occupati, 25 anni di storia, patrimonio netto 3,3 M. Sono contatori animati: a pagina caricata risultano "0" finché non si scorre (un lettore automatico li vede a zero).',
 '**Incoerenze da sanare** [DA VERIFICARE con il cliente]: "oltre 500 addetti" (testo) vs 1000 lavoratori (contatore); "oltre 20 anni" (Il gruppo) vs 25 anni (contatore).',
 '**Casi studio**: assenti. Le 9 pagine "Attività" sono categorie del 2022 senza progetti. **News**: solo 2 articoli (EMAS 06/07/2026; premio Hera a Nanni Srl 15/06/2026).',
 '**Contatti**: la sede di Bari non compare nella pagina Contatti (compaiono Milano e Imola).',
 '**FV/EPC non ha la stessa forza dell\'edilizia** [INFERENZA]: la home non cita mai "fotovoltaico" né "EPC"; ciò spiega l\'obiezione "non sapevo che faceste fotovoltaico".',
])
doc.add_heading('3.2 Tracciamenti [VERIFICATO nel sorgente della home]', 2)
table(doc, ['Strumento', 'Esito', 'Azione'], [
 ['Google Tag Manager', 'Presente (GTM-NSGJS55)', 'Verificare i tag al suo interno'],
 ['Google Analytics', 'Nel sorgente compare solo UA-74420576-1 (Universal Analytics, dismesso)', 'Verificare GA4 via GTM o attivarlo'],
 ['Meta Pixel', 'Presente (ID 528973914673613)', 'Verificare eventi Lead e API conversioni'],
 ['LinkedIn Insight Tag', 'Non rilevato', 'Installare (anche via GTM)'],
 ['Cookie consent', 'Cookiebot rilevato', 'Consent Mode v2; test dei tag con consenso'],
], widths=[3.6, 7.4, 6])
doc.add_heading('3.3 Canali social del cliente', 2)
MS.audit_social(doc)
page_break(doc)

# ---------------- 4 MERCATO ----------------
doc.add_heading('4. Analisi di mercato per segmento', 1)
MS.mercato(doc)
doc.add_heading('4.7 Ricerche su Google: cosa cercano davvero (Ubersuggest, Italia, 26/11/2026)', 2)
table(doc, ['Keyword', 'Segm.', 'Vol./mese', 'Difficoltà SEO', 'Lettura'], [
 ['conto termico 3.0', 'S5/S4', '49.500 (picchi 74.000)', '40', 'Interesse stagionale molto alto, pubblico generalista'],
 ['agrivoltaico', 'S3', '6.600', '42', 'Interesse alto; "su terreno agricolo" 170'],
 ['attestazione soa', 'S6', '4.400', '39', 'Domanda continua di imprese'],
 ['general contractor', 'S1', '2.900', '13', 'CPC alto (5,57 €); intento misto'],
 ['fotovoltaico condominiale', 'S4', '720', '15', 'Intento commerciale; ads costosi (PD 69)'],
 ['consorzio stabile', 'S6', '480', '11', 'Interesse costante'],
 ['aree idonee fotovoltaico', 'S3', '320', '18', 'Calante, ripresa a nov 2026'],
 ['epc fotovoltaico', 'S2', '140', '7', 'Poca ricerca, ma posizionabile'],
 ['conto termico comuni / scuole / enti pubblici', 'S5', '10–20', '9–16', 'Nicchia: il segmento PA non si cerca su Google'],
 ['costruzione impianti FV a terra; parco FV chiavi in mano; capannoni chiavi in mano', 'S1/S2', '0', '4', 'Nessun volume: usare come linguaggio, non come target SEO'],
], widths=[5.2, 1.4, 3.2, 2.2, 5])
para(doc, '**Cosa significa** [INFERENZA]: i clienti ad alto valore (sviluppatori, fondi, RUP) non si trovano con la ricerca Google: servono social e contatto mirato. Le keyword guidano i temi, non il canale.')
page_break(doc)

# ---------------- 5 COMPETITOR ----------------
doc.add_heading('5. Benchmark competitor e spazi di posizionamento', 1)
MS.competitor(doc)
page_break(doc)

# ---------------- 6 PERSONA ----------------
doc.add_heading('6. Buyer persona', 1)
box(doc, 'In sintesi', ['Una scheda per ciascuno dei 6 segmenti, con le parole del cliente dove possibile.', 'Il canale primario cambia: LinkedIn per S1, S2, S5, S6; Facebook per S3 e S4.'])
for P in PERSONAS:
    doc.add_heading(f"{P['id']} – {P['nome']}", 2)
    table(doc, ['Voce', 'Scheda'], [
     ['Ruolo e contesto', P['ruolo']], ['Obiettivi', P['obiettivi']], ['Paure', P['paure']], ['Obiezioni', P['obiezioni']],
     ['Fattori di fiducia', P['fiducia']], ['Canale', P['canale']], ['Formati preferiti', P['formati']], ['Momento del funnel', P['funnel']],
     ['Messaggio chiave', P['messaggio']], ['Lead magnet', P['lead']], ['CTA consigliata', P['cta']]], widths=[3.4, 13.6], size=9, zebra=False)
page_break(doc)

# ---------------- 7 STRATEGIA ----------------
doc.add_heading('7. Strategia: posizionamento, canali, pilastri, rubriche, formati', 1)
box(doc, 'In sintesi', ['Da "impresa edile" a **partner unico per costruzione ed energia**.', 'Canali: LinkedIn (primario B2B), Facebook/Instagram (terreni e condomini), YouTube (riattivato come archivio video).', '6 pilastri, 6 rubriche, grafiche chiare con testo come base.'])
doc.add_heading('7.1 Posizionamento e messaggio ombrello', 2)
para(doc, 'Oggi Opera si presenta come "Building General Contractor" e il payoff è "Il tuo futuro, il nostro presente". La proposta è affermare ciò che il cliente ha detto essere il vero valore: **una filiera completa sotto un unico tetto**, con un solo referente. Tre claim alternativi:')
table(doc, ['#', 'Claim', 'Perché'], [[str(i+1), a, b] for i, (a, b) in enumerate(CLAIMS)], widths=[0.8, 6.5, 9.7])
para(doc, '**Consigliato**: il n. 2, perché risponde alla paura principale (coordinare molte imprese) e rende naturale parlare di fotovoltaico, ESCo e manutenzione senza contraddire l\'edilizia.')
doc.add_heading('7.2 Ruolo di ogni canale', 2)
table(doc, ['Canale', 'Priorità', 'Segmenti', 'Obiettivo', 'Motivazione'], [list(r) for r in CANALI], widths=[2, 2.2, 3, 2.6, 7.2], size=8.5)
para(doc, '**Nota**: l\'ipotesi LinkedIn per B2B/PA e Facebook per amministratori e proprietari di terreni è coerente col brief ma va confermata con i dati di targeting e con i primi 60 giorni di campagna.')
doc.add_heading('7.3 Pilastri di contenuto', 2)
table(doc, ['Pilastro', '%', 'Cosa racconta'], [[a, f'{b}%', c] for a, b, c in PILASTRI], widths=[6, 1.4, 9.6])
doc.add_heading('7.4 Rubriche ricorrenti', 2)
table(doc, ['Rubrica', 'Formato', 'Frequenza', 'Esempio'], [list(r) for r in RUBRICHE], widths=[3.6, 3.2, 2.2, 8])
doc.add_heading('7.5 Formati', 2)
table(doc, ['Formato', 'Perché'], [list(r) for r in FORMATI], widths=[5, 12])
doc.add_heading('7.6 Frequenza, tono di voce e visual', 2)
table(doc, ['Canale', 'Frequenza', 'Note'], [list(r) for r in FREQUENZA], widths=[3, 4.5, 9.5])
para(doc, '**Tono di voce**: caldo, chiaro, professionale; frasi brevi; benefici prima, tecnica dopo. **Visual**: grafiche pulite con palette Opera, foto reali di cantiere, una sola idea per creatività.')
table(doc, ['Fai', 'Evita'], [list(r) for r in DO_DONT], widths=[8.5, 8.5], zebra=False)
doc.add_heading('7.7 Gestione delle obiezioni via contenuto', 2)
table(doc, ['Obiezione', 'Contenuti che la smontano', 'Fase'], [list(r) for r in OBIEZIONI], widths=[4.5, 10.5, 2])
page_break(doc)

# ---------------- 8 FUNNEL / LEAD / ADS ----------------
doc.add_heading('8. Funnel, lead magnet e campagne a pagamento', 1)
box(doc, 'In sintesi', ['Un lead magnet per segmento, con landing e form dedicati.', 'Tre scenari di budget: **Base €2.500/mese**, **Consigliato €5.000/mese**, **Accelerato €9.000/mese**.', 'Solo lo scenario Consigliato (~280 contatti, intervallo 205–427) e quello Accelerato superano i 270 contatti; il Base si ferma a ~158.'])
doc.add_heading('8.1 Funnel per segmento', 2)
table(doc, ['Segmento', 'TOFU (scoperta)', 'MOFU (considerazione)', 'BOFU (conversione)'], [list(r) for r in FUNNEL], widths=[3, 4.7, 4.7, 4.6])
doc.add_heading('8.2 Lead magnet', 2)
table(doc, ['Seg.', 'Titolo e formato', 'Promessa', 'Campi del form', 'Follow-up'], [[x['seg'], f"**{x['titolo']}** – {x['formato']}", x['promessa'], x['campi'], x['follow']] for x in LEAD_MAGNET], widths=[1, 4.4, 3.6, 4.2, 3.8], size=8.5)
para(doc, 'I lead magnet di S3 e S4 sono quelli suggeriti dal cliente. [DAL CLIENTE]')
doc.add_heading('8.3 Scenari di budget e calcolo dei contatti', 2)
para(doc, '**Metodo (trasparente)**: contatti = budget efficace ÷ CPL. Assunzioni:')
bullets(doc, [
 '**CPL LinkedIn 140–250**: benchmark Metadata 2026 (153 inserzionisti, 57,6 M USD di spesa 2025): costo per lead medio ponderato 202 USD; lead form 193; Document Ads 142 [VERIFICATO: metadata.io, consultato 26/11/2026]. Valute: trattati 1 USD ≈ 1 EUR come ordine di grandezza [INFERENZA].',
 '**CPL Meta (Facebook/Instagram) 50–110**: nello stesso dataset Facebook 145 USD e Instagram 138 USD (B2B); su lead ads cross-industry WordStream 2025 indica 27,66 USD; per le costruzioni USA SuperAds riporta ~53 USD [VERIFICATO come benchmark di terze parti, non specifici per l\'Italia]. Intervallo scelto perché i target S3/S4 sono meno "B2B puri" [INFERENZA].',
 '**Mese 1 al 50%** di efficacia (setup e fase di apprendimento) [INFERENZA].',
 '**Accelerato**: CPL +15% per saturazione dell\'audience a scala maggiore [INFERENZA].',
 '**Contatti organici/sito/outbound**: 3–6 al mese, ipotesi prudenziale da validare con la baseline (non disponibile) [INFERENZA].',
 'I benchmark sono **intervalli indicativi, non promesse**. Metadata stessa avverte di non usare 202 USD come target.'])
rows = []
for k in ('Base', 'Consigliato', 'Accelerato'):
    s = SC[k]; mese = s['tot'] // 6
    rows.append([k, f"€{mese:,}".replace(',', '.'), f"€{s['tot']:,}".replace(',', '.'), f"LinkedIn €{s['li']:,.0f} · Meta €{s['me']:,.0f}".replace(',', '.'),
                 f"{s['li_leads'][0]:.0f}–{s['li_leads'][1]:.0f}", f"{s['me_leads'][0]:.0f}–{s['me_leads'][1]:.0f}", f"{s['org'][0]}–{s['org'][1]}",
                 f"**{s['tot_rng'][0]:.0f}–{s['tot_rng'][1]:.0f}**", f"**{s['mid']:.0f}**", 'Sì' if s['mid'] >= 270 else 'No'])
table(doc, ['Scenario', 'Ads/mese', 'Ads 6 mesi', 'Ripartizione', 'Lead LinkedIn', 'Lead Meta', 'Organico', 'Totale (min–max)', 'Valore centrale', '≥270?'], rows, widths=[1.9, 1.5, 1.7, 3.3, 1.5, 1.4, 1.3, 2, 1.5, 1.0], size=8)
para(doc, '**Esempio di calcolo (Consigliato)**: spesa 6 mesi €30.000; LinkedIn 45% = €13.500, Meta 55% = €16.500. Budget efficace = spesa × (0,5+5)/6 = 91,7%. Lead LinkedIn = 13.500×0,917 ÷ 250…140 = 50–88; lead Meta = 16.500×0,917 ÷ 110…50 = 138–302; organico 18–36; totale 205–427. Valore centrale (CPL 195 su LinkedIn e 80 su Meta): ' + f"{SC['Consigliato']['mid_li']:.0f} + {SC['Consigliato']['mid_me']:.0f} + 27 organico = {SC['Consigliato']['mid']:.0f}" + ' contatti.')
para(doc, '**Verifica di coerenza con l\'obiettivo di 270**: il Base **non** lo raggiunge (centrale ~158, massimo 240); il Consigliato lo raggiunge con margine ridotto (~280, minimo 205); l\'Accelerato lo supera (~422). Si tratta di **contatti**, non di clienti: la percentuale di contatti qualificati va misurata nei primi 90 giorni [DA VERIFICARE].')
para(doc, 'Il costo di gestione social e produzione contenuti è separato dal budget media e verrà definito nella proposta economica.')
doc.add_heading('8.4 Ripartizione indicativa per segmento (scenario Consigliato)', 2)
table(doc, ['Segmento', '% budget media', 'Canale'], [
 ['S2 Sviluppatori FV', '20%', 'LinkedIn'], ['S5 PA – Conto Termico', '20%', 'LinkedIn + Facebook'], ['S3 Terreni', '25%', 'Facebook/Instagram'],
 ['S4 Condomini', '15%', 'Facebook/Instagram'], ['S1 Committenti privati', '10%', 'LinkedIn'], ['S6 Imprese', '10%', 'LinkedIn + Facebook']], widths=[6, 3.5, 7.5])
para(doc, 'La ripartizione verrà riequilibrata ogni mese in base al CPL e alla qualità dei contatti.')
page_break(doc)

# ---------------- 9 ESEMPI ----------------
doc.add_heading('9. Esempi di contenuto e piano editoriale', 1)
box(doc, 'In sintesi', ['Piano editoriale di 4 settimane (23 contenuti) – anche in Excel modificabile.', '14 idee di post sviluppate (almeno 2 per segmento) e 3 concept di campagna.', 'I segnaposto [ ] indicano materiali da fornire: non abbiamo inventato casi o numeri.'])
doc.add_heading('9.1 Piano editoriale – 4 settimane (indicativo da lunedì 11/01/2027)', 2)
table(doc, ['Data', 'Canale', 'Seg.', 'Pilastro', 'Formato', 'Titolo / gancio', 'CTA'], [[d(w, g), c, s, p, f, t, cta] for (w, g, c, s, p, f, t, cta) in PIANO], widths=[1.9, 1.9, 1.1, 2, 1.8, 5.8, 2.5], size=8)
doc.add_heading('9.2 Idee di post sviluppate', 2)
for I in IDEE:
    doc.add_heading(f"Idea {I['n']} – {I['seg']} – {I['canale']}", 3)
    table(doc, ['Voce', 'Dettaglio'], [['Gancio', I['gancio']], ['Struttura della grafica / carosello', I['struttura']], ['Bozza di copy', I['copy']], ['CTA', I['cta']], ['Hashtag', I['hashtag']]], widths=[3.6, 13.4], size=8.5, zebra=False)
doc.add_heading('9.3 Tre concept di campagna ads', 2)
for A in ADS:
    doc.add_heading(A['titolo'], 3)
    table(doc, ['Voce', 'Dettaglio'], [['Pubblico', A['pubblico']], ['Visual', A['visual']], ['Testo inserzione', A['testo']], ['Lead magnet', A['lm']], ['Note', A['note']]], widths=[3.2, 13.8], size=8.5, zebra=False)
page_break(doc)

# ---------------- 10 KPI ----------------
doc.add_heading('10. Misurazione e KPI', 1)
box(doc, 'In sintesi', ['KPI per ogni fase del funnel, con contatti e contatti qualificati come metrica principale.', 'Setup tracciamenti nel mese 1; report mensile con raccomandazioni.'])
table(doc, ['Fase', 'KPI', 'Frequenza', 'Strumento'], [list(r) for r in KPI], widths=[2.4, 7.6, 2.4, 4.6])
doc.add_heading('Setup tracciamenti necessari', 2)
bullets(doc, SETUP_TRACK)
page_break(doc)

# ---------------- 11 ROADMAP ----------------
doc.add_heading('11. Roadmap a 6 mesi e prossimi passi', 1)
box(doc, 'In sintesi', ['Mese 1 di setup, lancio dal mese 2, ottimizzazione e scala dal mese 3.', 'Obiettivi intermedi di contatti: 15–30–45–55–60–65 = 270.'])
table(doc, ['Mese', 'Focus', 'Attività', 'Obiettivo contatti'], [list(r) for r in ROADMAP], widths=[2.4, 3.2, 9, 2.4])
para(doc, 'Il percorso intermedio è un obiettivo di lavoro: nello scenario Consigliato i mesi 2-3 sono quelli a maggior rischio di scostamento, perché contengono la fase di apprendimento delle campagne [INFERENZA].')
doc.add_heading('Cosa serve dal cliente', 2); bullets(doc, DAL_CLIENTE)
doc.add_heading('Le 5 decisioni da prendere insieme', 2); bullets(doc, DECISIONI, 'List Number')
page_break(doc)

# ---------------- 12 APPENDICE ----------------
doc.add_heading('12. Appendice: fonti, metodologia, limiti', 1)
MS.appendice(doc)

doc.save('../output/Opera_CG_Analisi_e_Strategia_Social.docx')
print('docx salvato')
