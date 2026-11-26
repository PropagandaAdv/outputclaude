# -*- coding: utf-8 -*-
from docx_helpers import *

def audit_social(doc):
    para(doc, '**Limite dichiarato**: Instagram, Facebook, LinkedIn e le due Ad Library (Meta, LinkedIn) non sono leggibili senza accesso (HTTP 429 / login / 403). Non abbiamo aggirato blocchi né stimato dati: i campi sono indicati come "non leggibile senza login". Serve un rilevamento manuale (circa 15 minuti per canale) con un account agenzia.')
    table(doc, ['Voce', 'Instagram', 'Facebook', 'LinkedIn', 'YouTube'], [
     ['Accessibilità (26/11/2026)', 'HTTP 429 / login', 'Login', 'HTTP 403', 'Pagina e feed RSS pubblici'],
     ['Follower / iscritti', 'non leggibile senza login', 'non leggibile senza login', 'non leggibile senza login', '**99** iscritti [VERIFICATO]'],
     ['Contenuti', 'non leggibile', 'non leggibile', 'non leggibile', '35 video, 61.082 visualizzazioni totali [VERIFICATO]'],
     ['Ultimo post', 'non leggibile', 'non leggibile', 'non leggibile', '**06/04/2020** (feed RSS: 15 video 2017-2020) [VERIFICATO]'],
     ['Frequenza ultimi 90 gg', 'non leggibile', 'non leggibile', 'non leggibile', '0 video [VERIFICATO]'],
     ['Temi', 'non leggibile', 'non leggibile', 'non leggibile', 'Cantieri (demolizione/ricostruzione, lottizzazione Imola, CSE San Lazzaro); nessun video su FV, ESCo, Conto Termico, condomini [INFERENZA dai titoli]'],
     ['Video più visti', '–', '–', '–', 'Demolizione e ricostruzione 39.278; Lavori di urbanizzazione 13.364; Time lapse demolizione 3.425; altri < 1.200'],
     ['CTA / descrizioni', 'non leggibile', 'non leggibile', 'non leggibile', 'Quasi assenti nei video [VERIFICATO]'],
     ['Inserzioni (Ad Library)', '[DA VERIFICARE] manualmente', '[DA VERIFICARE]', '[DA VERIFICARE]', '–'],
    ], widths=[3, 3, 2.6, 2.6, 5.8], size=8.5)
    para(doc, 'La differenza tra 15 video del feed e i 35 dichiarati dalla pagina è da verificare (Shorts o video non elencati).', 9)
    doc.add_heading('Sintesi: cosa funziona, cosa manca, opportunità rapide', 3)
    table(doc, ['Cosa funziona', 'Cosa manca', 'Opportunità rapide'], [[
     '• I 4 canali sono linkati dal footer del sito\n• I video di cantiere/time-lapse hanno attirato più visualizzazioni (39k)\n• Asset di credibilità pronti: certificazioni, EMAS 2026, premio Hera',
     '• Dati su IG/FB/LinkedIn non accessibili\n• YouTube fermo dal 2020, nessun video su FV/ESCo/condomini\n• Sito poco aggiornato (ultima news 06/07/2026)\n• Naming non uniforme (operacostruzionigenerali / consorzio-opera / OPERA CG) [INFERENZA dagli URL]',
     '• Rilevamento manuale dei canali + Ad Library\n• Riusare i video di demolizione come reel con CTA\n• Pubblicare EMAS e premio Hera su LinkedIn/Facebook\n• Link social nell\'header del sito\n• Handle e hashtag di brand coerenti']], widths=[5.6, 5.8, 5.6], size=8.5, zebra=False)

def competitor(doc):
    box(doc, 'In sintesi', [
     'Analizzati 8 competitor su 4 fronti: general contractor (Webuild, Pizzarotti), EPC FV (Aiem, Greenergy), consorzi stabili (CEC, Medil), ESCo con la PA (Renovit, Edison Next).',
     'Dati pubblici letti: sito, claim, casi, lead magnet. **Follower, frequenza e inserzioni non leggibili**: [DA VERIFICARE] per tutti.',
     'Spazio libero principale: **"un solo interlocutore dal progetto alla manutenzione"** con casi studio numerici.'])
    para(doc, '**Criterio di scelta**: nessun competitor copre l\'intera filiera di Opera, quindi si confrontano i quattro "fronti" in cui Opera si presenta ai committenti, privilegiando operatori italiani con presenza digitale verificabile, target sovrapposti e scale diverse (Webuild come "tetto", gli altri più vicini a Opera). Aiem e Greenergy sono stati scelti come EPC FV sulla base di autodichiarazioni raccolte da Solare B2B [INFERENZA: non esiste una classifica indipendente per MW costruiti].')
    table(doc, ['Competitor', 'Fronte', 'Social linkati dal sito', 'Casi studio', 'Lead magnet', 'Messaggio chiave'], [
     ['Webuild', 'GC', 'LinkedIn, IG, YouTube, FB, X', 'Sì (per area, video)', 'Newsletter, Library, modulo Ponte Stretto', '"Grandi opere per costruire il futuro del Paese"'],
     ['Pizzarotti', 'GC', 'LinkedIn, IG, YouTube', 'Progetti in home', 'Non rilevati', '"Progettazione e costruzione di grandi opere"; ESG e persone'],
     ['Aiem', 'EPC FV/MEP', 'LinkedIn, FB', 'Logo-wall clienti', 'Company profile PDF', '"Energy transition and sustainable progress"; EPC e main contractor'],
     ['Greenergy', 'EPC FV', 'LinkedIn, FB, IG, YouTube, TikTok', '**Sì, con cliente e MW**', 'Solo policy PDF', 'Progettazione, costruzione e gestione FV; sedi anche a Bari'],
     ['CEC', 'Consorzio stabile', 'Nessuno linkato', 'Rimando a "Lavori"', 'Nessuno', 'Consorzio stabile; sede operativa a Milano; **FV non menzionato**'],
     ['Medil', 'Consorzio stabile', 'non verificabile', 'non verificabile', 'non verificabile', 'Sito ufficiale non individuato; solo fonti terze'],
     ['Renovit', 'ESCo', 'non verificabile', 'non verificabile', 'non verificabile', 'Sito non leggibile (JavaScript); solo fonti terze'],
     ['Edison Next', 'ESCo', 'LinkedIn', 'Sì (Michelin, ASST Cremona)', 'Newsletter, white paper, Next Journal', '"Diventiamo l\'energia che cambia tutto"; pagina PA dedicata'],
    ], widths=[2.1, 2, 3, 2.7, 3.2, 4], size=8)
    para(doc, 'Fonte: siti ufficiali consultati il 26/11/2026 (dettaglio in appendice e in 04_competitor/benchmark_competitor.md). Follower, frequenza di pubblicazione, formati social e inserzioni attive: [DA VERIFICARE] per tutti i competitor.', 9)
    doc.add_heading('Best practice da cui ispirarsi', 3)
    bullets(doc, [
     '**Edison Next** (energia B2B): hub editoriale con articoli lunghi su temi normativi (es. Conto Termico 3.0, 14/07/2026), white paper e newsletter bimestrale. Spunto per Opera: trasformare le novità normative in contenuti riutilizzabili su LinkedIn, aggiungendo la raccolta contatti che lì manca.',
     '**Schneider Electric Italia** (industriale, fuori settore): contenuti segmentati per ruolo del decisore (professionisti, partner, formazione). Spunto: schede diverse per RUP, direttore tecnico, CFO d\'impresa. Performance social non verificate.',
     '**Greenergy** (FV): casi nel formato "cliente + MW + tipologia + territorio" (es. Buzzi 128 MW, Progressum 15,5 MW in Puglia). Spunto: stesso schema per edilizia e impianti di Opera.'])
    doc.add_heading('Spazi di posizionamento liberi per Opera [INFERENZA dal confronto]', 3)
    bullets(doc, [
     '**Un solo interlocutore dal progetto alla manutenzione**: nessuna home letta presenta la filiera completa come claim unico.',
     '**Casi studio con numeri** anche per edilizia e impianti, non solo per il fotovoltaico.',
     '**Presidio territoriale** Emilia-Romagna / Lombardia / Puglia.',
     '**Contenuti educational per la PA** (procedura, ESCo, PPP) più accessibili di quelli dei grandi gruppi.',
     '**Persone e cantiere** come prova di credibilità del consorzio.',
     '**Lead magnet pratici** (checklist incentivi, guida CER, check-up edificio): rari tra GC, EPC e consorzi letti.'])
