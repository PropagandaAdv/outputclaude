# -*- coding: utf-8 -*-
"""Contenuti strategici condivisi (docx + xlsx). Tutto in italiano."""

SEGMENTI = {
 'S1': 'Committenti privati (conto terzi)',
 'S2': 'Sviluppatori FV (EPC)',
 'S3': 'Proprietari terreni / agricole',
 'S4': 'Amministratori e condomini',
 'S5': 'PA – Conto Termico',
 'S6': 'Imprese da consorziare',
}

PERSONAS = [
 dict(id='S1', nome='Il Committente di grandi opere', ruolo='Decisore aziendale / sviluppatore immobiliare, logistica, fondo, imprenditore che costruisce o amplia capannoni e sedi. 40-65 anni, nazionale (focus Emilia-Romagna, Lombardia, Puglia).',
  obiettivi='Un\'opera consegnata nei tempi e nei costi previsti, con un solo referente dalla progettazione alla manutenzione. [DAL CLIENTE]',
  paure='Ritardi, costi extra, contenziosi in cantiere; impresa che non regge finanziariamente. [DAL CLIENTE]',
  obiezioni='"Un consorzio è affidabile e responsabile quanto un\'impresa unica?" [DAL CLIENTE]. Alternative provate: frammentare tra più imprese; grandi contractor poco flessibili e costosi. [DAL CLIENTE]',
  fiducia='Casi studio / prima e dopo, SOA, ISO 9001/45001/37001, EMAS, numeri (portafoglio lavori, anni di storia).',
  canale='Primario LinkedIn; secondario YouTube (video cantiere) e sito.', formati='Documento/carosello LinkedIn, time-lapse, video 60" con direttore di cantiere.',
  funnel='Consapevolezza → Considerazione (scelta del contractor). Ciclo lungo.',
  messaggio='Un solo interlocutore, dalla progettazione alla manutenzione: meno tempo a coordinare, più certezza su tempi e budget.',
  lead='Checklist "10 domande da fare a un general contractor prima di firmare" (PDF) + scheda di verifica requisiti dell\'impresa.',
  cta='"Scarica la checklist" → "Parliamo del tuo progetto (call 20 min)".'),
 dict(id='S2', nome='Lo Sviluppatore FV', ruolo='Sviluppatore/investitore con progetti autorizzati o in autorizzazione fino a 10 MWp in media tensione; cerca un EPC. 35-55 anni, nazionale.',
  obiettivi='Un impianto funzionante e monitorato, con manutenzione inclusa, entro le finestre di connessione e incentivo. [DAL CLIENTE]',
  paure='Perdere finestre di connessione o incentivi; EPC senza SOA OG9, senza capacità finanziaria o senza squadre per 10-15 ettari. [DAL CLIENTE]',
  obiezioni='"Non sapevo che faceste fotovoltaico / EPC." [DAL CLIENTE]. Installatori piccoli non strutturati per 10-15 ettari. [DAL CLIENTE]',
  fiducia='SOA OG9/OG11, ISO, ESCo UNI CEI 11352, referenze di impianti realizzati, cronoprogramma tipo, bancabilità.',
  canale='Primario LinkedIn (inserzioni per ruolo + contenuti tecnici); secondario email/outbound e newsletter di settore.', formati='Documenti LinkedIn "scheda tecnica", cronoprogramma tipo, video di cantiere FV, post con tecnici.',
  funnel='Considerazione → Decisione (richiesta offerta EPC).',
  messaggio='Edilizia, impianti e FV sotto un unico tetto: costruiamo il tuo parco FV, chiavi in mano, rispettando i tempi di connessione.',
  lead='Scheda "Checklist di selezione dell\'EPC FV (fino a 10 MWp MT)" + call di fattibilità costruttiva.',
  cta='"Richiedi la checklist" → "Prenota una call tecnica".'),
 dict(id='S3', nome='Il Proprietario di terreno', ruolo='Proprietario di terreni, azienda agricola o impresa con aree disponibili (aree compromesse, idonee o adatte all\'agrivoltaico). 45-70 anni, sedi e province di Imola, Milano, Bari e aree limitrofe.',
  obiettivi='Valorizzare l\'area con un impianto chiavi in mano senza dover coordinare progettisti e imprese.',
  paure='Vincoli autorizzativi, perdere il terreno agricolo, promesse non mantenute (inferenza dal contesto; non dichiarata dal cliente) [INFERENZA].',
  obiezioni='"Il mio terreno è adatto?"; "Chi si assume il rischio?"; "Non sapevo che faceste fotovoltaico" [DAL CLIENTE].',
  fiducia='Verifica gratuita di idoneità fatta da tecnici, esempi di impianti, certificazioni, linguaggio semplice.',
  canale='Primario Facebook (ads con targeting geografico/interessi agricoli); secondario Instagram.', formati='Grafiche con testo chiaro, caroselli "mito vs realtà", prima/dopo di impianti.',
  funnel='Consapevolezza → Considerazione.',
  messaggio='Il tuo terreno può diventare energia: lo verifichiamo insieme, gratis, e ci pensiamo noi dal progetto alla manutenzione.',
  lead='Verifica gratuita di idoneità del terreno (form con mappa/foglio-particella) [DAL CLIENTE].',
  cta='"Verifica gratis il tuo terreno".'),
 dict(id='S4', nome='L\'Amministratore di condominio', ruolo='Amministratore (35-60 anni) e condomini interessati a riqualificazione energetica, efficientamento e CER.',
  obiettivi='Ridurre le bollette del condominio con un percorso chiaro, senza ritrovarsi con assemblee conflittuali.',
  paure='Responsabilità verso i condòmini, imprese inaffidabili, detrazioni/incentivi poco chiari [INFERENZA: tipiche del ruolo].',
  obiezioni='Costi iniziali, complessità burocratica, fiducia nell\'impresa.',
  fiducia='Guida tecnica scritta con semplicità, esempi prima/dopo, certificazioni, ESCo, consulenza fiscale interna.',
  canale='Primario Facebook (ads e community); secondario LinkedIn per amministratori professionisti.', formati='Carosello guida, infografiche, video brevi "assemblea in 3 minuti".',
  funnel='Consapevolezza → Considerazione.',
  messaggio='Un percorso guidato dalla diagnosi all\'intervento, con finanza e fisco inclusi: meno rischi per l\'amministratore.',
  lead='Guida "Riqualificazione energetica e Servizio Energia in condominio" [DAL CLIENTE].',
  cta='"Scarica la guida" → "Richiedi una pre-diagnosi".'),
 dict(id='S5', nome='Il RUP / tecnico comunale', ruolo='Comuni ed enti con scuole, RSA ed edifici pubblici; RUP, responsabili ufficio tecnico, amministratori. 35-65 anni.',
  obiettivi='Edifici riqualificati e bollette ridotte a costo zero per l\'ente; presentare ai cittadini una scuola o RSA riqualificata. [DAL CLIENTE]',
  paure='Edifici energivori senza risorse proprie; procedura (GSE, PPP) complessa da gestire internamente. [DAL CLIENTE]',
  obiezioni='"È davvero a costo zero? È troppo complicato per il nostro ufficio tecnico." [DAL CLIENTE]',
  fiducia='Procedura spiegata passo-passo, ESCo certificata UNI CEI 11352, ISO 37001 (anticorruzione), casi di scuole/RSA riqualificate.',
  canale='Primario LinkedIn (ruoli PA) + eventi/webinar; secondario Facebook (pagine di enti, community comunali).', formati='Documenti LinkedIn "procedura in 4 step", webinar, FAQ video.',
  funnel='Considerazione → Decisione (valutazione PPP).',
  messaggio='Edifici pubblici più efficienti, con una procedura (GSE, PPP) che gestiamo insieme a voi. [Evitare "costo zero" come promessa: condizioni economiche da verificare caso per caso sulla norma vigente]',
  lead='Check-up gratuito di fattibilità di un edificio pubblico + "Guida Conto Termico per i Comuni".',
  cta='"Richiedi il check-up del tuo edificio".'),
 dict(id='S6', nome='L\'Imprenditore edile/impiantista', ruolo='Titolare di impresa edile, impiantistica, artigiana o di servizi tecnici; 40-65 anni.',
  obiettivi='Accedere a lavori più grandi grazie alla forza del consorzio. [DAL CLIENTE]',
  paure='Essere troppo piccoli o poco qualificati per accedere da soli agli appalti importanti. [DAL CLIENTE]',
  obiezioni='Perdita di autonomia, costi di adesione, fiducia nel consorzio [INFERENZA]. Attenzione: dopo il correttivo al Codice Appalti i consorzi stabili hanno limiti al cumulo dei requisiti; ogni claim su "le nostre certificazioni/SOA diventano tue" va validato dal legale di Opera [DA VERIFICARE].',
  fiducia='Testimonianze di consorziati (es. premio Hera a Nanni Srl, 15/06/2026 [VERIFICATO: sito operacg.com]), certificazioni condivise, supporto gare.',
  canale='Primario LinkedIn e Facebook (gruppi artigiani/edili); secondario passaparola associazioni.', formati='Interviste a consorziati, post "come funziona", scheda "chi può aderire".',
  funnel='Considerazione → Decisione.',
  messaggio='Più forti, insieme: assistenza alle gare, rete di imprese, certificazioni del sistema consortile [formula da validare con il legale]',
  lead='Guida "Come accedere agli appalti importanti restando una piccola impresa" + check requisiti di adesione.',
  cta='"Verifica se puoi aderire".'),
]

CLAIMS = [
 ('"Costruiamo e alimentiamo il tuo futuro."', 'Unisce edilizia ed energia; caldo e istituzionale; richiama il payoff attuale "Il tuo futuro, il nostro presente".'),
 ('"Un solo partner, dal progetto alla manutenzione."', 'Mette al centro il beneficio dichiarato dal cliente (un interlocutore invece di dieci). È il claim consigliato come ombrello.'),
 ('"Edilizia, energia, efficienza: tutto sotto un unico tetto."', 'Più descrittivo, risolve l\'obiezione "non sapevo che faceste fotovoltaico".'),
]

CANALI = [
 ('LinkedIn', 'Primario', 'S1, S2, S5, S6 (secondario S4)', 'Fiducia + lead B2B', 'Decisori aziendali, RUP, sviluppatori e studi di progettazione sono presenti per ruolo e azienda; il targeting per mansione/settore è l\'unico modo di raggiungere gli sviluppatori FV. [INFERENZA]'),
 ('Facebook', 'Primario (ads) per S3/S4', 'S3, S4, S6, S5 (pagine enti)', 'Lead + awareness locale', 'Proprietari di terreni e amministratori sono pubblico adulto 45-70 anni, il più presente su Facebook; Meta Lead Ads con CPL più basso della media LinkedIn (Metadata 2026: FB 145 vs LI 202 USD). [INFERENZA + VERIFICATO benchmark]'),
 ('Instagram', 'Secondario', 'S3, S4, S1 (visual cantiere)', 'Brand awareness, vetrina visiva', 'Riutilizza gli stessi contenuti visivi di Facebook (Meta); utile per reel di cantiere e Stories con link al sito. [INFERENZA]'),
 ('YouTube', 'Da riattivare, ruolo archivio/seo video', 'S1, S2, S5', 'Fiducia e prova', 'Il canale conta 99 iscritti e 35 video; l\'ultimo video risale al 2020; il video più visto (Demolizione e ricostruzione) ha 39.278 visualizzazioni [VERIFICATO: pagina YouTube, 26/11/2026] → il formato cantiere/time-lapse funziona. Proposta: riattivare con 1-2 video/mese riadattati dai reel.'),
]

PILASTRI = [
 ('Cantieri e casi studio (prima/dopo)', 25, 'Mostra opere reali, tempi e numeri. Risponde alle paure di ritardi e costi.'),
 ('Competenza spiegata semplice (normativa e incentivi)', 25, 'Conto Termico, EPC, CER, aree idonee, come funziona un consorzio.'),
 ('Energia, fotovoltaico ed EPC', 20, 'Rende visibile l\'offerta FV/EPC e ESCo: risolve "non sapevo che faceste fotovoltaico".'),
 ('Solidità e certificazioni', 15, 'SOA, ISO, EMAS, SA8000, ESCo: rassicura sulla solidità del consorzio.'),
 ('Persone e squadre', 10, 'Tecnici, direttori di cantiere, consorziati: umanizza il consorzio.'),
 ('Opportunità per le imprese consorziate', 5, 'Reclutamento consorziate (S6) sui canali giusti.'),
]

RUBRICHE = [
 ('"Prima & Dopo"', 'Carosello / reel 30"', 'Quindicinale', 'Es. scuola o capannone: stato iniziale, intervento, risultato, tempi. [CASO STUDIO DA FORNIRE]'),
 ('"Il Conto Termico in 60 secondi"', 'Video breve + grafica', 'Mensile', 'Es. "Chi può accedere? 3 cose da sapere" (verificare dati sulla norma vigente).'),
 ('"Il cantiere di oggi"', 'Foto/Stories/Reel', 'Settimanale', 'Es. getto, montaggio strutture FV, posa pannelli. [FOTO DA FORNIRE]'),
 ('"Mito vs Realtà"', 'Carosello grafico', 'Mensile', 'Es. "Agrivoltaico = niente più agricoltura?" Mito vs realtà.'),
 ('"Volti di Opera"', 'Intervista video/foto', 'Mensile', 'Es. il direttore di cantiere racconta una giornata tipo. [INTERVISTA DA FARE]'),
 ('"Una certificazione, una garanzia"', 'Grafica semplice', 'Mensile', 'Es. cosa significa per te ISO 45001 / SOA OG9 / EMAS.'),
]

FORMATI = [
 ('Grafiche con testo chiaro (preferenza del cliente)', 'Base del piano: 40% dei contenuti. Singole grafiche con un messaggio e numeri; sempre con logo e CTA.'),
 ('Caroselli (IG/FB/LinkedIn)', 'Per spiegare procedure e "prima/dopo" in 5-8 slide; massimo tempo di lettura, alto salvataggio. [INFERENZA]'),
 ('Documenti LinkedIn (PDF scorrevole)', 'Per checklist e guide tecniche; nel benchmark Metadata i Document Ads sono il formato LinkedIn più economico per lead (142 USD vs 202 medio). [VERIFICATO benchmark]'),
 ('Reel / video brevi di cantiere, time-lapse', 'Il formato cantiere (demolizione/ricostruzione) è l\'unico che ha superato le 3.000 visualizzazioni su YouTube [VERIFICATO]. Riadattare in verticale.'),
 ('Video con i tecnici (60-90")', 'Per spiegare obiezioni (es. "è davvero a costo zero?"). Volti reali = fiducia. [INFERENZA]'),
]

FREQUENZA = [
 ('LinkedIn', '3 post/settimana', 'Lun/mer/ven mattina; 1 documento o carosello a settimana'),
 ('Facebook', '3 post/settimana + ads', 'Mar/gio/sab; contenuti dedicati S3/S4'),
 ('Instagram', '3 post + Stories 3-5/settimana', 'Stesse creatività di Facebook adattate; Reel 1/settimana'),
 ('YouTube', '1-2 video/mese', 'Riadattamento dei reel; titoli e descrizioni SEO'),
]

DO_DONT = [
 ('Parla di benefici concreti ("un solo referente, tempi certi").', 'Non usare gergo tecnico non spiegato (EPC, PPP, OG9) senza una riga di chiarimento.'),
 ('Usa numeri reali e fonti (con data).', 'Non promettere "a costo zero" o risparmi senza condizioni e senza verifica della norma vigente.'),
 ('Mostra volti, cantieri, squadre.', 'Non usare solo stock photo o rendering generici.'),
 ('Grafiche pulite, una idea per post, palette del brand.', 'Non riempire la grafica di testo da brochure.'),
 ('Tono caldo, competente, rassicurante.', 'Non usare linguaggio aggressivo o da venditore ("offerta imperdibile").'),
]

LEAD_MAGNET = [
 dict(seg='S1', titolo='Checklist: 10 domande da fare a un general contractor prima di firmare', formato='PDF 4 pagine', promessa='Eviti ritardi e costi extra scegliendo un partner solido.', campi='Nome, azienda, ruolo, email, tipologia di opera (capannone/sede/altro), budget indicativo (range), consenso privacy', follow='Email 1 (subito): PDF; Email 2 (+3 gg): caso studio; Email 3 (+7 gg): invito call 20\''),
 dict(seg='S2', titolo='Checklist di selezione dell\'EPC FV (fino a 10 MWp, MT)', formato='PDF + scheda cronoprogramma tipo', promessa='Scegli un EPC con SOA, capacità finanziaria e squadre adeguate.', campi='Nome, società, ruolo, email, MWp, stato autorizzativo, regione, finestra di connessione prevista', follow='Email 1: PDF; call tecnica entro 48h se MWp ≥ 1'),
 dict(seg='S3', titolo='Verifica gratuita di idoneità del terreno', formato='Form + risposta tecnica entro 5 giorni lavorativi (promessa da validare con il cliente)', promessa='Scopri se il tuo terreno può ospitare un impianto FV/agrivoltaico.', campi='Nome, telefono, comune, foglio/particella, superficie (ha), uso attuale, vincoli noti', follow='Chiamata di un tecnico + report sintetico'),
 dict(seg='S4', titolo='Guida "Riqualificazione energetica e Servizio Energia in condominio"', formato='PDF 12 pagine', promessa='Capisci passo dopo passo come avviare l\'intervento e presentarlo in assemblea.', campi='Nome, email, telefono, n. condomini amministrati, n. unità del condominio più grande', follow='Email 1: guida; Email 2: checklist assemblea; Email 3: pre-diagnosi gratuita'),
 dict(seg='S5', titolo='Check-up di fattibilità per un edificio pubblico (scuola/RSA) + Guida Conto Termico per i Comuni', formato='Guida PDF + scheda check-up', promessa='Scopri quali interventi e quale quota di incentivo possono interessare l\'edificio (verifica caso per caso sulla norma vigente).', campi='Ente, ruolo, email PEC/ordinaria, tipologia di edificio, anno di costruzione, consumi (se noti)', follow='Chiamata tecnica entro 5 gg; invito a webinar'),
 dict(seg='S6', titolo='Guida "Come accedere agli appalti importanti restando una piccola impresa"', formato='PDF + check requisiti adesione', promessa='Capisci cosa puoi fare insieme al consorzio.', campi='Azienda, categorie SOA, fatturato indicativo, regione, email, telefono', follow='Email 1: guida; chiamata del responsabile associativi'),
]

FUNNEL = [
 ('S1 Committenti', 'Carosello "Prima/Dopo", video cantiere (LinkedIn)', 'Caso studio + "Come scegliere un general contractor"', 'Call 20 min / preventivo'),
 ('S2 Sviluppatori FV', 'Post "FV + edilizia sotto un tetto"', 'Documento "Checklist EPC", cronoprogramma tipo', 'Call tecnica / richiesta offerta'),
 ('S3 Terreni', 'Grafica "Il tuo terreno può produrre energia"', 'Mito vs realtà + esempi', 'Verifica idoneità'),
 ('S4 Condomini', 'Reel "Assemblea in 3 minuti"', 'Guida PDF + checklist assemblea', 'Pre-diagnosi gratuita'),
 ('S5 PA', 'Video "Conto Termico in 60 secondi"', 'Guida + procedura in 4 step + webinar', 'Check-up di fattibilità'),
 ('S6 Imprese', 'Intervista a un consorziato', 'Guida "Appalti per piccole imprese"', 'Verifica requisiti di adesione'),
]

OBIEZIONI = [
 ('"Non sapevo che faceste fotovoltaico / EPC" [DAL CLIENTE]', 'Serie "Opera fa anche questo": post mensile con cantiere FV reale; claim ombrello; pagina EPC rinnovata; video del direttore tecnico; campagne LinkedIn per ruolo (S2) e Meta per terreni (S3).', 'TOFU / MOFU'),
 ('"Un consorzio è affidabile e responsabile quanto un\'impresa unica?" [DAL CLIENTE]', 'Post "Come funziona la responsabilità in un consorzio" (con testo contrattuale da verificare); numeri (80 M fatturato, 100 M portafoglio, 170 contratti attivi – [VERIFICATO sito]); SOA/ISO/EMAS; casi di consegna puntuale; intervista al direttore.', 'MOFU / BOFU'),
 ('Comuni: "È davvero a costo zero? È troppo complicato per il nostro ufficio tecnico" [DAL CLIENTE]', 'Video "Conto Termico: cosa paga l\'ente e cosa no" (formula corretta sulla norma vigente); procedura in 4 step; FAQ; webinar con il GSE/esperto; checklist; check-up gratuito. Evitare "costo zero" come promessa assoluta finché non è confermata la formula.', 'MOFU / BOFU'),
]

KPI = [
 ('Awareness', 'Reach, impression, follower, visualizzazioni video >50%', 'Mensile', 'Meta Business Suite, LinkedIn Analytics'),
 ('Engagement', 'Engagement rate, salvataggi, click link', 'Mensile', 'Piattaforme nativee'),
 ('Lead', 'Contatti totali (target 45/mese), CPL, lead per segmento/lead magnet', 'Settimanale', 'GA4 + CRM + piattaforme'),
 ('Qualità', '% contatti qualificati (SQL), appuntamenti, preventivi richiesti', 'Mensile', 'CRM (HubSpot o equivalente)'),
 ('Business', 'Opportunità aperte e valore, costo per opportunità', 'Trimestrale', 'CRM + dati commerciali del cliente'),
]
SETUP_TRACK = [
 'Verificare/pulire GTM-NSGJS55 e passare a GA4 (nel sorgente compare solo UA-74420576-1, dismesso).',
 'Eventi di conversione GA4/Meta/LinkedIn su ogni form (Lead, click telefono, download).',
 'Installare LinkedIn Insight Tag (non rilevato nel sorgente).',
 'Meta Pixel presente (ID 528973914673613): verificare eventi e API conversioni.',
 'Consent Mode v2 con Cookiebot per misurare nel rispetto del GDPR.',
 'UTM standard per ogni link social e ad; CRM con campi segmento e lead magnet.',
 'Dashboard mensile (Looker Studio) e report PDF con raccomandazioni.',
]

# --- Piano editoriale 4 settimane (data inizio indicativa lunedì 11/01/2027) ---
import datetime as _dt
START = _dt.date(2027, 1, 11)
def d(w, g): return (START + _dt.timedelta(days=7*(w-1)+g)).strftime('%d/%m/%Y')

PIANO = [
 # (settimana, giorno(0=lun), canale, segmento, pilastro, formato, titolo/gancio, CTA)
 (1,0,'LinkedIn','Tutti','Solidità','Grafica','Siamo Opera CG: edilizia, impianti ed energia sotto un unico tetto','Scopri cosa facciamo → sito'),
 (1,1,'Facebook','S3','Energia/FV','Grafica','Il tuo terreno può produrre energia? 3 domande per capirlo','Verifica gratis il tuo terreno'),
 (1,2,'LinkedIn','S1','Cantieri','Carosello','Prima/Dopo: [CASO STUDIO DA FORNIRE: capannone]','Parliamo del tuo progetto'),
 (1,2,'Instagram','S1','Cantieri','Reel','Il cantiere di oggi: [VIDEO DA FORNIRE]','Segui per altri cantieri'),
 (1,3,'Facebook','S4','Competenza','Carosello','5 domande da fare prima dell\'assemblea sull\'efficientamento','Scarica la guida'),
 (1,4,'LinkedIn','S2','Energia/FV','Documento','Come scegliere un EPC FV: 7 criteri (SOA OG9, finanza, squadre)','Scarica la checklist'),
 (2,0,'LinkedIn','S5','Competenza','Documento','Conto Termico per Comuni: la procedura in 4 step','Richiedi il check-up'),
 (2,1,'Facebook','S5','Competenza','Grafica','Scuole e RSA riqualificate: cosa possiamo fare insieme','Contattaci'),
 (2,2,'LinkedIn','S6','Opportunità','Intervista','Un consorziato racconta: perché sono entrato in OperaCG','Verifica se puoi aderire'),
 (2,3,'Instagram','S3','Competenza','Carosello','Agrivoltaico: miti e realtà','Verifica il tuo terreno'),
 (2,4,'Facebook','S6','Opportunità','Grafica','Le nostre certificazioni diventano anche tue','Richiedi informazioni'),
 (2,5,'YouTube','S1','Cantieri','Video','Time-lapse cantiere [VIDEO DA FORNIRE]','Iscriviti'),
 (3,0,'LinkedIn','S1','Solidità','Grafica','Cosa significa per te ISO 45001 + SOA OG1 su un cantiere','Leggi la guida'),
 (3,1,'Facebook','S4','Persone','Video','Il nostro tecnico risponde: cosa cambia con il Servizio Energia','Richiedi pre-diagnosi'),
 (3,2,'LinkedIn','S2','Cantieri','Carosello','Come si costruisce un impianto FV a terra: fasi e tempi [DATI DA FORNIRE]','Prenota una call tecnica'),
 (3,3,'Instagram','Tutti','Persone','Reel','Volti di Opera: il direttore di cantiere [INTERVISTA DA FARE]','Segui'),
 (3,4,'Facebook','S3','Energia/FV','Carosello','Aree idonee: cosa conta davvero [VERIFICARE NORMA VIGENTE]','Verifica gratuita'),
 (4,0,'LinkedIn','S5','Competenza','Video','Conto Termico: cosa paga l\'ente? (video del tecnico)','Check-up fattibilità'),
 (4,1,'Facebook','S1','Cantieri','Reel','Prima e Dopo di un capannone [CASO STUDIO]','Scrivici'),
 (4,2,'LinkedIn','S6','Opportunità','Documento','Come accedere agli appalti importanti restando una piccola impresa','Scarica la guida'),
 (4,3,'Instagram','S4','Competenza','Carosello','Condominio: 6 interventi che riducono le bollette','Scarica la guida'),
 (4,4,'LinkedIn','Tutti','Solidità','Grafica','EMAS 2026: cosa significa per i nostri clienti','Leggi di più'),
 (4,5,'YouTube','S5','Competenza','Video','FAQ Conto Termico: le 5 domande dei Comuni','Iscriviti'),
]

# --- Idee post sviluppate (14) ---
IDEE = [
 dict(n=1, seg='S1', canale='LinkedIn', gancio='Hai mai dovuto coordinare dieci imprese per costruire una sede?', struttura='Carosello 6 slide: 1) Gancio; 2) Il problema (ritardi, costi, responsabilità spezzettate); 3) La soluzione: un solo referente; 4) Come lavoriamo (progettazione, costruzione, impianti); 5) [CASO STUDIO DA FORNIRE]; 6) CTA.', copy='Costruire una sede o un capannone non dovrebbe voler dire gestire dieci imprese diverse. Con OperaCG hai un solo referente, dalla progettazione alla consegna. Ti raccontiamo come, con un esempio reale.', cta='Parliamo del tuo progetto', hashtag='#generalcontractor #costruzioni #edilizia #industria'),
 dict(n=2, seg='S1', canale='LinkedIn/Instagram', gancio='Prima e dopo: [NOME OPERA]', struttura='Grafica doppia o reel 20": foto prima / foto dopo / 3 numeri (m², giorni, addetti) [DATI DA FORNIRE].', copy='[Opera], consegnata in [giorni]. Ecco com\'era e com\'è oggi.', cta='Scopri come lavoriamo', hashtag='#prima_e_dopo #cantiere #operacg'),
 dict(n=3, seg='S2', canale='LinkedIn', gancio='7 criteri per scegliere un EPC fotovoltaico fino a 10 MWp', struttura='Documento 8 pagine: 1 copertina; 2 SOA OG9/OG11; 3 capacità finanziaria; 4 squadre e mezzi; 5 tempi di connessione; 6 monitoraggio e manutenzione; 7 referenze; 8 CTA.', copy='Un impianto da 10-15 ettari non si improvvisa. Ecco 7 criteri per scegliere l\'EPC giusto, senza perdere le finestre di connessione.', cta='Scarica la checklist', hashtag='#fotovoltaico #EPC #rinnovabili #agrivoltaico'),
 dict(n=4, seg='S2', canale='LinkedIn', gancio='Non sapevi che facciamo anche fotovoltaico? Eccoci in cantiere', struttura='Video 45" di cantiere FV [VIDEO DA FORNIRE] + testo.', copy='Edilizia, impianti ed energia: costruiamo il tuo parco fotovoltaico chiavi in mano.', cta='Prenota una call tecnica', hashtag='#fotovoltaico #EPC #operacg'),
 dict(n=5, seg='S3', canale='Facebook/Instagram', gancio='Il tuo terreno può diventare energia?', struttura='Carosello 5 slide: 1 domanda; 2 tipi di aree (compromesse, idonee, agricole – [verificare norma vigente]); 3 cosa verifichiamo; 4 cosa ottieni; 5 CTA.', copy='Prima di decidere, verifica se il tuo terreno è adatto. Lo facciamo gratis.', cta='Verifica gratis il tuo terreno', hashtag='#agrivoltaico #terreni #energia #aziendaagricola'),
 dict(n=6, seg='S3', canale='Facebook', gancio='Agrivoltaico: 3 miti da sfatare', struttura='Grafica singola con 3 miti/realtà.', copy='"Non si può più coltivare." Davvero? Ti spieghiamo la differenza tra impianto a terra e agrivoltaico [VERIFICARE contenuti con tecnico].', cta='Chiedi la verifica', hashtag='#agrivoltaico #agricoltura'),
 dict(n=7, seg='S4', canale='Facebook', gancio='5 domande da fare prima dell\'assemblea', struttura='Carosello 6 slide con una domanda per slide e spiegazione semplice.', copy='Se amministri un condominio, ecco le domande che i condomini ti faranno sull\'efficientamento. E le risposte.', cta='Scarica la guida', hashtag='#condominio #amministratore #efficientamentoenergetico'),
 dict(n=8, seg='S4', canale='Instagram Reel', gancio='L\'assemblea in 3 minuti', struttura='Reel 45": tecnico spiega 3 punti.', copy='Ti serve una sintesi da portare in assemblea? Eccola.', cta='Richiedi una pre-diagnosi', hashtag='#condominio #riqualificazione'),
 dict(n=9, seg='S5', canale='LinkedIn', gancio='Conto Termico: la procedura in 4 step', struttura='Documento 6 pagine: 1 titolo; 2 prenotazione al GSE; 3 gara PPP; 4 validazione GSE; 5 realizzazione e svincolo; 6 CTA. [Basata sul testo di operacg.com/conto-termico/, VERIFICARE con la norma vigente]', copy='La procedura è più semplice di quanto sembri. In 4 passi, con noi accanto.', cta='Richiedi il check-up', hashtag='#contotermico #PA #efficientamento'),
 dict(n=10, seg='S5', canale='Facebook/LinkedIn', gancio='Quanto paga davvero l\'ente? Il Conto Termico spiegato senza giri di parole', struttura='Video 60" del tecnico che risponde ai dubbi: costo, tempi, ufficio tecnico.', copy='Spieghiamo cosa può coprire l\'incentivo e cosa resta a carico dell\'ente, senza promettere "gratis". [VERIFICARE su norma vigente: es. incentivo al 100% per piccoli Comuni, scuole e ospedali SSN secondo fonti da confermare]', cta='Richiedi il check-up', hashtag='#contotermico #scuole #RSA'),
 dict(n=11, seg='S6', canale='LinkedIn/Facebook', gancio='Le certificazioni del consorzio al servizio delle consorziate [formula da validare con il legale]', struttura='Grafica semplice con 3 vantaggi (certificazioni, appalti, supporto gare) [VERIFICATO sul sito /associarsi/].', copy='Se la tua impresa è troppo piccola per partecipare da sola ai grandi appalti, il consorzio può cambiare le regole del gioco.', cta='Verifica se puoi aderire', hashtag='#consorzio #imprese #appalti'),
 dict(n=12, seg='S6', canale='LinkedIn', gancio='"Con OperaCG ho vinto il premio Best Supplier Hera"', struttura='Post con foto + intervista a Nanni Srl [PREMIO VERIFICATO sul sito news 15/06/2026; CITAZIONE DA OTTENERE].', copy='Nanni Srl, consorziata, premiata da Hera per la sicurezza. Ci racconta cosa significa far parte del consorzio.', cta='Scopri come entrare', hashtag='#sicurezza #consorziate #premio'),
 dict(n=13, seg='S1', canale='LinkedIn', gancio='EMAS 2026: cosa cambia per chi costruisce con noi', struttura='Grafica + testo breve [VERIFICATO: registrazione EMAS annunciata nella news del 06/07/2026].', copy='La registrazione EMAS è un impegno concreto per l\'ambiente. Ecco cosa significa per i nostri clienti.', cta='Scopri le certificazioni', hashtag='#EMAS #sostenibilità #certificazioni'),
 dict(n=14, seg='Tutti', canale='Tutti', gancio='Volti di Opera: il direttore di cantiere', struttura='Intervista video 60" (3 domande) [INTERVISTA DA FARE].', copy='Chi c\'è dietro i nostri cantieri? Incontra [Nome], direttore di cantiere.', cta='Segui per altri volti', hashtag='#persone #cantiere #operacg'),
]

ADS = [
 dict(titolo='Concept 1 — EPC fotovoltaico (LinkedIn Ads)', pubblico='Sviluppatori e investitori FV, responsabili tecnici e CEO di società di sviluppo; Italia; settori Energia e Rinnovabili; seniority Manager+. Retargeting visitatori /epc/.', visual='Documento a scorrimento: copertina "7 criteri per scegliere un EPC FV" con foto di cantiere FV reale [FOTO DA FORNIRE].', testo='Hai un progetto FV fino a 10 MWp in media tensione? Scegli un EPC con SOA OG9, capacità finanziaria e squadre per 10-15 ettari. Scarica la checklist di selezione di OperaCG.', lm='Checklist EPC FV (S2)', note='Formato scelto perché Document Ads è il formato LinkedIn con CPL più basso nel benchmark Metadata 2026 (142 USD).'),
 dict(titolo='Concept 2 — Verifica terreno (Meta Lead Ads: Facebook + Instagram)', pubblico='Facebook/IG: 40-70 anni, aree vicine alle sedi (province di Bologna, Milano, Bari e limitrofe) + interessi agricoltura/proprietà terreni; lookalike su lista contatti del cliente.', visual='Immagine con mappa e il testo "Il tuo terreno può produrre energia?" + foto di impianto/terreno reale [FOTO DA FORNIRE].', testo='Hai un terreno o un\'azienda agricola? Scopri gratis se è adatto a un impianto fotovoltaico o agrivoltaico. Lo verifichiamo noi e ci pensiamo anche per progetto e costruzione.', lm='Verifica gratuita idoneità terreno (S3)', note='Lead Ads con form precompilato; campi extra (foglio/particella) per qualificare.'),
 dict(titolo='Concept 3 — Conto Termico per i Comuni (LinkedIn + Facebook)', pubblico='LinkedIn: mansioni RUP, responsabile ufficio tecnico, dirigenti comunali, sindaci/assessori (se targettizzabili); Facebook: pagine/lookalike ruoli PA. Regioni Emilia-Romagna, Lombardia, Puglia.', visual='Grafica con scuola/RSA riqualificata [FOTO DA FORNIRE] + titolo "Scuole e RSA più efficienti, senza complicazioni".', testo='La procedura GSE e il PPP sembrano complicati? La gestiamo insieme. Richiedi un check-up gratuito di fattibilità per un edificio pubblico del tuo Comune.', lm='Check-up edificio pubblico (S5)', note='Verificare con il cliente la formula "costo zero" prima di usarla nel testo.'),
]

ROADMAP = [
 ('Mese 1 (Dic/Gen)', 'Setup e fondamenta', 'Audit accessi, GA4/GTM/Pixel/Insight Tag, UTM, CRM; brand kit social; raccolta foto/video/casi; landing + form dei 2 primi lead magnet (S2, S5); calendario 1°-2° mese.', '15 contatti'),
 ('Mese 2', 'Lancio contenuti e prime campagne', 'Avvio pubblicazione (3 post/sett per canale); campagne LinkedIn S2/S5 e Meta S3/S4; lead magnet 3 e 4.', '30 contatti'),
 ('Mese 3', 'Ottimizzazione', 'Analisi primo ciclo: CPL, qualità lead; A/B creatività; riattivazione YouTube; webinar Conto Termico.', '45 contatti'),
 ('Mese 4', 'Scala', 'Aumento budget sui segmenti con CPL migliore; casi studio e video con i tecnici; lead magnet 5 e 6.', '55 contatti'),
 ('Mese 5', 'Consolidamento', 'Retargeting, email nurturing, nuovi casi, eventi di settore; ottimizzazioni landing.', '60 contatti'),
 ('Mese 6', 'Consuntivo e piano successivo', 'Report 6 mesi, analisi lead qualificati e opportunità, proposta anno 2.', '65 contatti'),
]
# somma 15+30+45+55+60+65 = 270

DAL_CLIENTE = [
 'Accessi in sola lettura/amministratore a Instagram, Facebook, LinkedIn, YouTube e agli account pubblicitari (Business Manager, Campaign Manager).',
 'Foto e video di cantieri (alta risoluzione), droni, time-lapse; foto di impianti FV reali.',
 '5-8 casi studio con dati: cliente (se autorizzato), luogo, metri quadri/MWp, tempi, importo indicativo, prima/dopo.',
 'Referenti interni: un responsabile tecnico per validare i contenuti, un commerciale per gestire i lead entro 24h.',
 'Conferma dei dati del sito (500 o 1000 addetti? 20 o 25 anni?).',
 'Autorizzazioni (privacy) per volti e nomi di clienti/consorziati.',
 'Dati su lead e vendite attuali (CRM, form, telefonate) per misurare la baseline.',
 'Conferma della formula "a costo zero" per i Comuni e del processo del Conto Termico 3.0 applicabile.',
]

DECISIONI = [
 'Scenario di budget (consigliato: €5.000/mese di ads + gestione social).',
 'Priorità dei segmenti nei primi 3 mesi (proposta: S2, S5, S3 poi S4).',
 'Claim ombrello (proposta: "Un solo partner, dal progetto alla manutenzione").',
 'Gestione e SLA dei lead (chi risponde e in quanto tempo) + scelta del CRM.',
 'Produzione contenuti: shooting in cantiere / video con i tecnici e casi studio.',
]
