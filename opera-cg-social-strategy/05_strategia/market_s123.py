# -*- coding: utf-8 -*-
from docx_helpers import *

def s123(doc):
    box(doc, 'In sintesi', [
     'Il fotovoltaico cresce (+19% di nuova potenza nei primi 9 mesi del 2026) e la logistica ha un semestre record, ma le regole cambiano in continuo: aree idonee, FER X, connessioni.',
     'Finestra di comunicazione **dicembre 2026 – marzo 2027**: qualifica FER X (30/11), prima open season Terna (dic–gen, da verificare), KEY Rimini 10–12/03/2027.',
     'I portali primari GSE e MIMIT non erano raggiungibili: la normativa è letta da studi legali e testate (indicate come "sec."). **Ogni riferimento va confermato su GU/MASE/GSE prima di essere pubblicato.**'])
    doc.add_heading('Quadro normativo trasversale (stato al 26/11/2026)', 2)
    table(doc, ['Tema', 'Stato', 'Etichetta'], [
     ['Aree idonee: art. 11-bis D.Lgs. 190/2024 (DL 175/2025; L. 4/2026, GU 20/01/2026). Elenco ex lege: siti bonificati, cave dismesse, discariche chiuse, aree industriali/logistiche, parcheggi, aree ferroviarie/autostradali', 'In vigore. Regioni: solo aree aggiuntive, tetto SAU 0,8–3%, fascia 500 m dai beni tutelati', '[VERIFICATO] (sec.)'],
     ['Divieto di FV a terra in aree agricole, con eccezioni (CER, PNRR, agrivoltaico, modifiche di impianti esistenti)', 'In vigore; Corte cost. sent. 127/2026 (dep. 16/07/2026): questioni non fondate', '[VERIFICATO]'],
     ['Agrivoltaico: dichiarazione asseverata (≥80% della produzione lorda vendibile) e verifica del Comune per 5 anni', 'In vigore', '[VERIFICATO] (sec.)'],
     ['FER X (DM MASE, in vigore dal 07/08/2026): ≤1 MW accesso diretto; >1 MW aste; FV 80 €/MWh (tetto 95, min. 65), 20 anni, esercizio entro 36 mesi', 'In vigore; prima procedura: manifestazioni chiuse 06/11/2026, qualifica entro 30/11/2026; tariffa ARERA ≤1 MW non ancora pubblicata', '[VERIFICATO] (sec.)'],
     ['Connessioni: DM MASE 08/09/2026 "first permitted, first connected", open season trimestrali; art. 10-bis D.Lgs. 190/2024 (istanza entro 90 gg dall\'accettazione)', 'Firmato; prima open season attesa dic 2026–gen 2027', 'Decreto [VERIFICATO] (sec.); data [DA VERIFICARE]'],
     ['Richieste di connessione Terna al 31/05/2026: 9.204 pratiche, 318 GW FER', 'Dato Terna riportato da testata', '[VERIFICATO] (sec.)'],
     ['Impianti ≤10 MWp in media tensione', 'Il decreto saturazione riguarda la rete di trasmissione: effetto sulla MT non trovato', '[DA VERIFICARE]'],
    ], widths=[7.4, 6.6, 3], size=8.5)
    doc.add_heading('4.1 S1 – Committenti privati di grandi opere (general contractor)', 2)
    bullets(doc, [
     '**Logistica**: JLL H1 2026 – take-up ~1,6 mln mq (+72%), investimenti 1,25 mld € (+50%), vacancy ~4%, ~57% dello sviluppato in modalità speculativa [VERIFICATO]. Cushman & Wakefield: take-up oltre 1,5 mln mq (+59%) [VERIFICATO]. Milano ~60% dell\'assorbimento [VERIFICATO].',
     '**Costruzioni**: ANCE prevede +5,6% di investimenti nel 2026 trainati dalle opere pubbliche; il non residenziale privato nuovo è debole (-1,5% / -3%) [DA VERIFICARE: da snippet].',
     '**Lettura** [INFERENZA]: il 57% di sviluppo speculativo indica committenti che sono developer e fondi; contano tempi di consegna e certezza dei costi.',
     '**Incentivi**: iperammortamento 2026-2028 per impianti rinnovabili di autoproduzione [DA VERIFICARE: soglie discordanti]; Transizione 5.0 pregressa (DL 42/2026) [VERIFICATO sec.]. Le aree logistiche/industriali sono aree idonee per il FV: tema concreto per chi costruisce capannoni [VERIFICATO sec.].',
     '**Finestre**: CRESME 3/12/2026 [DA VERIFICARE]; MIPIM 16–19/03/2027 [DA VERIFICARE]; Logistics Hub Bergamo 19–20/05/2027 [VERIFICATO sec.]. I report broker escono a fine trimestre/semestre [INFERENZA].',
     '**Dove si informano**: Il Sole 24 Ore, ItaliaOggi, Trasporto Europa, Trans.info, JLL/Cushman/CBRE, ANCE [VERIFICATO l\'esistenza; peso sui decisori INFERENZA]. Gruppi LinkedIn: non verificabili con gli strumenti usati.',
     '**Non trovato**: valore in € del non residenziale privato; dati logistici regionali per Emilia-Romagna e Puglia.'])
    doc.add_heading('4.2 S2 – Sviluppatori FV fino a 10 MWp in media tensione (EPC)', 2)
    bullets(doc, [
     '**Mercato**: nuova potenza gen–set 2026 **4,83 GW** (+19% sul 2025), cumulato 48,35 GW; utility scale ≥1 MW 2,24 GW (~46%); nel solo Q3 il segmento 1–10 MW ha fatto **394 MW** (Italia Solare su dati Terna, via pv magazine) [VERIFICATO]. Emilia-Romagna 443 MW nei primi 9 mesi [VERIFICATO].',
     '**FER X** divide il target: sotto 1 MW incentivo diretto; tra 1 e 10 MW aste con cauzioni e penali; capex di riferimento 900 €/kW [VERIFICATO sec.]. [INFERENZA] molti sviluppatori valuteranno anche PPA/merchant e cercheranno EPC con costi e tempi certi.',
     '**Connessione**: rischio di perdita della soluzione (90 gg per PAS/AU) [VERIFICATO sec.]; prima open season dic 2026–gen 2027 [DA VERIFICARE].',
     '**Dove si informano**: QualEnergia, Rinnovabili.it, pv magazine, Staffetta Quotidiana; Italia Solare, ANIE Rinnovabili, GSE, Terna [VERIFICATO l\'esistenza]. Fiere: KEY Rimini 10–12/03/2027 [VERIFICATO sec.]; Intersolar Monaco 8–10/06/2027 [DA VERIFICARE].',
     '**Domande tipiche** [INFERENZA]: prezzo chiuso e data di energizzazione garantita; chi gestisce la connessione; rischio area idonea; garanzie bancabili; "perché un consorzio?".',
     '**Non trovato**: dati Elettricità Futura; valore del mercato EPC e prezzi €/Wp.'])
    doc.add_heading('4.3 S3 – Proprietari di terreni, aziende agricole, imprese con aree', 2)
    bullets(doc, [
     '**Agrisolare** (PNRR, tetti): 770,4 mln € concessi per ~505 MW a 7.409 imprese; Emilia-Romagna 633 progetti; **1.863 domande ammesse ma non finanziate** (187 mln €, ~170 MW) [VERIFICATO sec.]. [INFERENZA] bacino di potenziali lead da intercettare con contenuti dedicati.',
     '**Agrivoltaico PNRR**: nuove concessioni GSE da giugno 2026; esercizio entro 24 mesi [VERIFICATO sec.]. → cantieri tra 2027 e inizio 2028 [INFERENZA].',
     '**Regola chiave**: FV a terra in area agricola vietato con eccezioni; agrivoltaico ammesso se conforme (≥80% PLV, verifica 5 anni). [INFERENZA] Il target "aree compromesse/idonee" è più semplice da comunicare del terreno agricolo puro; sull\'agrivoltaico il rischio si sposta sul rispetto dei requisiti.',
     '**Regioni**: Emilia-Romagna con proposta di legge (tetto SAU 0,8% regionale / 2% comunale); esito finale e leggi di Puglia e Lombardia [DA VERIFICARE].',
     '**Dove si informano**: Coldiretti, Confagricoltura, CIA, Copagri; Agronotizie, Terra e Vita, L\'Informatore Agrario [INFERENZA/DA VERIFICARE]. Fieragricola Verona solo nel 2028; EIMA già svolta a novembre 2026.',
     '**Attenzione**: i contenuti su agrivoltaico, incentivi e idoneità vanno rivisti da un professionista prima della pubblicazione.',
     '**Non trovato**: numero di aziende con terreni idonei; canoni di affitto; stato PAC; testo vigente delle leggi regionali.'])
