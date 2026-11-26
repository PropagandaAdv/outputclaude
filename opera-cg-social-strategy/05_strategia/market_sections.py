# -*- coding: utf-8 -*-
import glob, re
from docx_helpers import *
from market_sections_a import audit_social, competitor
from market_s123 import s123

def mercato(doc):
    s123(doc)
    doc.add_heading('4.4 S4 – Amministratori di condominio e condomini', 2)
    bullets(doc, [
     '**Mercato**: gli investimenti ENEA per Ecobonus + Bonus Casa sui lavori conclusi nel 2025 sono ~3,62 mld € (-42,5% sul 2024; -47,8% gli interventi); il 87,8% riguarda edifici residenziali; Lombardia 28%, Veneto 11,9%, Emilia-Romagna 10,3% [VERIFICATO, report ENEA via sintesi]. Condomini in Italia: ~1,2 milioni (stima Anaci, senza data) [DA VERIFICARE]; dato ISTAT non trovato.',
     '**Lettura** [INFERENZA]: dopo il Superbonus il mercato si è dimezzato ma resta di grandi volumi; il condominio che decide oggi pesa il costo netto → funzionano formule con finanziamento tramite terzi (ESCo/Servizio Energia) e lavori per fasi.',
     '**Detrazioni**: 2026 al 50% (abitazione principale) e 36% (altri casi) [VERIFICATO, L. 199/2025]; 2027 a legislazione vigente 36%/30%; il DDL bilancio 2027 propone 50%/36% ma **non è ancora legge** [VERIFICATO che il DDL lo preveda]. Nello stesso condominio convivono aliquote diverse (dipende dal singolo condomino).',
     '**Conto Termico 3.0 (DM 7/8/2025)**: i privati accedono agli interventi di efficienza sul solo terziario; per le rinnovabili termiche (pompe di calore, solare termico…) anche sul residenziale. Se il **condominio** sia soggetto ammesso e come: [DA VERIFICARE] (art. 4 del DM e FAQ GSE non letti). Conto Termico non cumulabile con altri incentivi statali per gli stessi interventi [VERIFICATO]: per un condominio può significare scegliere tra detrazione e Conto Termico [INFERENZA].',
     '**CER**: 3.315 configurazioni al 31/05/2026 (275,5 MW) [VERIFICATO, fonte secondaria su dati GSE]; altre fonti riportano numeri più alti e non confrontabili [DA VERIFICARE]. Tariffa incentivante fino al 31/12/2027 (proroga richiesta, da verificare).',
     '**Case green (EPBD)**: recepimento scaduto il 29/05/2026, non ancora recepita [DA VERIFICARE]: **oggi non c\'è un obbligo di riqualificazione per i condomini esistenti** → non costruire contenuti "dovete adeguarvi entro il 2030/2033".',
     '**Finestre**: iter della legge di bilancio 2027 (aliquote dal 1° gennaio); autunno-inverno = decisioni su riscaldamento; primavera-estate = esecuzione lavori [INFERENZA].',
     '**Dove si informano**: Anaci, Confedilizia, ANCE; Amministrare il Condominio, Condominioweb, FiscoeTasse, LavoriPubblici.it, QualEnergia [INFERENZA: ricorrenti nelle ricerche]; KEY Rimini 10–12/03/2027 [VERIFICATO]. Calendario Anaci 2027: non trovato.',
     '**Obiezione chiave** [INFERENZA]: "È davvero a costo zero?" Nessun incentivo oggi in vigore copre il 100% per un condominio privato: **evitare la parola "gratis/costo zero"** e spiegare cosa significa "senza anticipo" (finanziamento ESCo, canone legato al risparmio).'])
    doc.add_heading('4.5 S5 – Pubblica Amministrazione (Comuni, scuole, RSA)', 2)
    bullets(doc, [
     '**Conto Termico 3.0**: in vigore dal 25/12/2025; budget 900 mln €/anno; Portaltermico aperto il 02/02/2026, sospeso il 03/03/2026 con ~1,3 mld € di richieste, riaperto il 13/04/2026 solo in accesso diretto (a lavori finiti) [VERIFICATO da fonti secondarie e pagina GSE parziale; GSE e Gazzetta non leggibili: pagine 401/404].',
     '**Percentuali**: incentivo al 100% per i Comuni fino a 15.000 abitanti, le scuole e gli ospedali SSN; per gli altri 40–65% [VERIFICATO sec.]. Se il 100% valga anche per le RSA: [DA VERIFICARE]. Correttivo: intesa in Conferenza Unificata il 22/10/2026, non ancora in Gazzetta (la bozza porta i piccoli Comuni all\'80% dal secondo intervento) [VERIFICATO sec.].',
     '**Dato utile per Opera** (CRESME, luglio 2026): bandi di PPP per efficientamento: **231 gare e 4,4 mld €** nel primo semestre 2026 contro 3 gare e 261 mln € un anno prima; lavori tradizionali: bandi a 25,1 mld € contro 15,3 mld € [VERIFICATO sec.]. Mercato dei Comuni: da 12,4 mld € (2023) a 7 mld € (2025) [DA VERIFICARE].',
     '**PNRR**: la scadenza per ultimare i lavori era il 31/08/2026 [DA VERIFICARE] → per nuove opere è chiuso; il tema è il post-PNRR.',
     '**Cicli di bilancio**: previsione al 31/12 con frequenti differimenti a febbraio-marzo; DUP al 31/07 [VERIFICATO sec.]; le finestre commerciali per la PA sono ragionamenti [INFERENZA].',
     '**Dove si informano**: ANCI, ANCI Emilia-Romagna, GSE, LavoriPubblici.it, Il Sole 24 Ore, portali PA [INFERENZA]; eventi 2027 non trovati (Forum PA, assemblea ANCI).',
     '**Obiezioni** [DAL CLIENTE]: "È davvero a costo zero? È troppo complicato." Risposta: spiegare la procedura passo-passo e la quota di incentivo applicabile all\'ente **senza promettere il costo zero** finché la formula non è validata.'])
    doc.add_heading('4.6 S6 – Imprese edili e impiantistiche (consorzio)', 2)
    bullets(doc, [
     '**Domanda**: "attestazione SOA" 4.400 ricerche/mese, "consorzio stabile" 480 [VERIFICATO, Ubersuggest]: le imprese cercano come qualificarsi.',
     '**Rischio normativo da conoscere** [VERIFICATO sec.]: l\'art. 67 del D.Lgs. 36/2023 riscritto dal correttivo limita il cumulo alla rinfusa nei lavori: le consorziate designate devono avere i requisiti in proprio o tramite avvalimento (art. 104). **Il messaggio "usi la nostra SOA" è quindi a rischio: ogni claim su SOA e consorzio va validato dal legale di Opera.** Il testo vigente di subappalto e avvalimento dopo il correttivo non è stato letto [DA VERIFICARE].',
     '**Prova sociale esistente** [VERIFICATO sul sito]: premio Best Supplier Hera 2026 a Nanni Srl (consorziata); servizi di supporto gare e certificazioni condivise su /associarsi/.',
     '**Dove si informano**: associazioni artigiane e di categoria, ANCE, testate di settore; numero di imprese per categoria e di consorzi stabili: non trovato.'])
    para(doc, '**Lettura d\'insieme** [INFERENZA]: i temi con più domanda nei prossimi mesi sono Conto Termico/PPP (PA), FER X e connessioni (FV), aree idonee (terreni), detrazioni 2027 (condomini). Sono anche i temi dove le regole cambiano più in fretta: il calendario editoriale deve prevedere un controllo normativo prima di ogni pubblicazione.', 10)

def appendice(doc):
    box(doc, 'In sintesi', ['Tutte le fonti sono state consultate il 26/11/2026. Elenco completo in `01_fonti/fonti.md` (circa 130 voci).',
                            'Limiti principali: social non leggibili senza login, Ad Library non consultabili, portali GSE/MIMIT/Gazzetta non raggiungibili (normativa da fonti secondarie).'])
    doc.add_heading('12.1 Metodologia', 2)
    bullets(doc, [
     '**Etichette**: [VERIFICATO] = dato letto da fonte consultata; [DAL CLIENTE] = dal questionario; [INFERENZA] = deduzione con ragionamento; [DA VERIFICARE] = plausibile ma non confermato. "(sec.)" = fonte secondaria (studio legale/testata).',
     '**Sito**: download delle pagine pubbliche e lettura del sorgente e delle API pubbliche WordPress.',
     '**Keyword**: Ubersuggest (Italia, lingua italiana): sono stime dello strumento.',
     '**Mercato e competitor**: ricerca web e lettura di pagine pubbliche tramite quattro analisti automatizzati in parallelo; consolidamento e controlli a cura del team.',
     '**Benchmark CPL/CTR**: solo intervalli indicativi con fonte; non sono promesse.',
     '**Budget e contatti**: calcolo riproducibile in `05_strategia/scenari_budget.py`.'])
    doc.add_heading('12.2 Limiti dell\'analisi', 2)
    bullets(doc, [
     '**Social del cliente**: Instagram (HTTP 429/login), Facebook (login), LinkedIn (HTTP 403) non leggibili: follower, frequenza, interazioni e coerenza visiva sono da rilevare con un account agenzia. Non abbiamo aggirato login o blocchi.',
     '**Ad Library** Meta e LinkedIn: non consultabili da questa analisi (403/404): inserzioni del cliente e dei competitor da verificare a mano.',
     '**Competitor**: nessuna metrica social leggibile; Medil (sito non individuato) e Renovit (sito in JavaScript) solo da fonti terze.',
     '**Normativa**: i portali GSE, MIMIT e Gazzetta Ufficiale non erano raggiungibili; le norme sono lette da studi legali e testate. **Prima di pubblicare qualsiasi riferimento normativo, importo o percentuale va confermato su GU, MASE o GSE.** Fonti discordanti: ripartizione 450/450 (DD 72/2026) vs 500/400 (DM) sul Conto Termico; numeri CER; data di pubblicazione del correttivo appalti.',
     '**Benchmark CPL**: fonti di terze parti prevalentemente USA/globali; nessun benchmark specifico per l\'Italia nel settore costruzioni. Valute: 1 USD ≈ 1 EUR come ordine di grandezza [INFERENZA].',
     '**Contenuti S3 (agrivoltaico)** e S6 (consorzio/SOA): da far rivedere a un professionista/legale prima della pubblicazione.',
     '**Dati non trovati**: valore in € dei mercati EPC e non residenziale privato; dati Elettricità Futura; numero di condomini ISTAT; gruppi LinkedIn rilevanti; date 2027 di diverse fiere.'])
    doc.add_heading('12.3 Fonti principali', 2)
    para(doc, 'Selezione delle fonti più rilevanti (l\'elenco completo, con data e cosa se ne è ricavato, è in `01_fonti/fonti.md`).', 9)
    rows = [
     ['Sito del cliente e API pubbliche', 'https://www.operacg.com/ (+ /epc/, /servizi/, /conto-termico/, /associarsi/, /certificazioni/, /news/, wp-json)', '26/11/2026'],
     ['YouTube del cliente', 'https://www.youtube.com/channel/UCMuoMMcarCJH2ZdZMYH7fQQ/about e feed RSS', '26/11/2026'],
     ['Keyword', 'Ubersuggest MCP (Italia)', '26/11/2026'],
     ['Benchmark CPL LinkedIn/Meta', 'https://metadata.io/resources/blog/what-linkedin-ads-cost; WordStream Facebook Ads Benchmarks 2025; SuperAds', '26/11/2026'],
     ['Mercato FV', 'Italia Solare su dati Terna (via pv magazine), GSE, MASE', '26/11/2026'],
     ['Logistica', 'JLL H1 2026 (28/07/2026), Cushman & Wakefield H1 2026', '26/11/2026'],
     ['Aree idonee e agrivoltaico', 'D.Lgs. 190/2024 art. 11-bis (sintesi studi legali); Corte costituzionale sent. 127/2026', '26/11/2026'],
     ['Conto Termico 3.0, detrazioni, CER', 'DM 7/8/2025 (via ANCE e riviste), ENEA, Agenzia Entrate, piattaforma PNIEC/GSE, CRESME', '26/11/2026'],
     ['Competitor', 'Siti ufficiali di Webuild, Pizzarotti, Aiem, Greenergy, CEC, Edison Next; fonti terze per Renovit e Medil', '26/11/2026'],
    ]
    table(doc, ['Tema', 'Fonte', 'Consultazione'], rows, widths=[4, 10.2, 2.8], size=8.5)
