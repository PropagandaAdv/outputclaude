# Audit social - Opera Costruzioni Generali (Fase 2)
Data consultazione: 2026-11-26. Metodo: solo dati pubblici senza login. Legenda: [VERIFICATO] / [INFERENZA] / [DA VERIFICARE].

## Avviso sui limiti
Instagram, Facebook, LinkedIn e le due Ad Library NON sono leggibili senza login/da questo ambiente (nessun aggiramento tentato). Per questi canali non sono stati rilevati follower, post, frequenza, interazioni. Solo YouTube e il sito sono stati letti. Le tabelle indicano "non leggibile senza login" dove il dato manca. Serve un rilevamento manuale (15 minuti per canale) da un account agenzia.

## Tabella per canale
| Voce | Instagram | Facebook | LinkedIn | YouTube |
|---|---|---|---|---|
| URL | /operacostruzionigenerali/ | /operacostruzionigenerali/ | /company/consorzio-opera/ | channel UCMuoMMc... |
| Accessibilita' | HTTP 429 (WebFetch) e 302 verso login (curl) [VERIFICATO, 2026-11-26] | Schermata di login [VERIFICATO, 2026-11-26] | HTTP 403 [VERIFICATO, 2026-11-26] | Pagina e feed RSS pubblici [VERIFICATO] |
| Follower/iscritti | non leggibile senza login | non leggibile senza login | non leggibile senza login | 99 iscritti [VERIFICATO: youtube.com/channel/.../about, 2026-11-26] |
| Numero contenuti | non leggibile | non leggibile | non leggibile | 35 video, 61.082 visualizzazioni totali [VERIFICATO, stessa pagina] |
| Data ultimo post | non leggibile senza login | non leggibile senza login | non leggibile senza login | Ultimo video nel feed RSS: 2020-04-06 [VERIFICATO: feed RSS, 2026-11-26]. Canale fermo da oltre 6 anni [INFERENZA: nessun video piu' recente nel feed] |
| Frequenza ultimi 90 gg | non leggibile | non leggibile | non leggibile | 0 video negli ultimi 90 gg [VERIFICATO sul feed] |
| Bio / link | non leggibile | non leggibile | non leggibile | Descrizione canale non estratta [DA VERIFICARE] |
| Ultimi 20-30 contenuti (formato/tema/segmento/CTA/interazioni) | non leggibile | non leggibile | non leggibile | Feed: 15 video, 2017-2020, cantieri (demolizione/ricostruzione, lottizzazione Imola, CSE San Lazzaro, Info Point Imola, Hotel Donatello), nessuna descrizione/CTA rilevata nella maggior parte. Piu' visti: "Demolizione e ricostruzione" 39.278 views (2020), "Lavori di urbanizzazione" 13.364, "Time Lapse demolizione" 3.425. Altri sotto 1.200 [VERIFICATO: feed RSS]. Segmento: PA/privati/commerciale, nessun contenuto su fotovoltaico, ESCo, Conto Termico, condomini [INFERENZA: dai titoli] |
| Coerenza visiva/tono/hashtag | [DA VERIFICARE] | [DA VERIFICARE] | [DA VERIFICARE] | Titoli senza brand/hashtag, stile documentaristico [INFERENZA] |
| Ad Library | Meta Ad Library: HTTP 403 da curl [VERIFICATO]; ricerca inserzioni non consultabile da qui. LinkedIn Ad Library: HTTP 403 [VERIFICATO]. Inserzioni attive: [DA VERIFICARE] manualmente. | | | |

Discrepanza: il feed RSS elenca 15 video, la pagina ne dichiara 35 [VERIFICATO entrambi]. Possibili video non nel feed (es. Shorts, non in elenco) [DA VERIFICARE].

## Sito operacg.com (benchmark di coerenza)
- Posizionamento: general contractor con sedi Milano (legale, Via Cusago 96/A), Imola, Bari; progettazione, costruzione, ristrutturazione, energia/ESCo, relamping/revamping [VERIFICATO: operacg.com, 2026-11-26].
- Tagline "Il tuo futuro, il nostro presente"; tono formale, istituzionale, certificazioni (ISO 9001/14001/45001/37001/50001, EMAS, SA 8000, UNI CEI 11352, SOA) [VERIFICATO].
- Menu: Chi siamo, Associarsi, Conto Termico, Servizi, Case Histories, News, Contatti. Link social solo nel footer, non nell'header [VERIFICATO].
- Contatori dati chiave tutti a "0" (probabile malfunzionamento) [VERIFICATO, causa: INFERENZA].
- News: ultimo articolo 2026-07-06 (Registrazione EMAS; premio Best Supplier 2026 Hera a Nanni Srl). Nessuna news recente da 4+ mesi [VERIFICATO: operacg.com/news/]. Nessun hashtag sul sito [VERIFICATO].
- Fotovoltaico/EPC e condomini non emergono nel menu principale; Conto Termico si [VERIFICATO]. Il sito si descrive come "consorzio" ma usa "OPERA CG" mentre i social usano "operacostruzionigenerali" e LinkedIn "consorzio-opera": naming non uniforme [INFERENZA dagli URL].

## Sintesi
### Cosa funziona
- Tutti e quattro i canali sono linkati dal footer del sito [VERIFICATO].
- Contenuti di cantiere e time-lapse su YouTube hanno ottenuto piu' views (demolizione 39k) [VERIFICATO]: il formato video "prima/dopo" funziona.
- Asset di credibilita' pronti da raccontare: certificazioni, EMAS 2026, premio Hera [VERIFICATO sul sito].

### Cosa manca
- Visibilita' sullo stato reale di IG/FB/LinkedIn: dati non accessibili [limite].
- YouTube inattivo dal 2020, 99 iscritti [VERIFICATO]; nessun video su fotovoltaico/ESCo/condomini.
- Sito poco aggiornato (ultima news luglio 2026) e contatori a 0 [VERIFICATO].
- Nessun hashtag di brand, naming non uniforme tra canali [INFERENZA/DA VERIFICARE].
- Nessuna evidenza consultabile su campagne a pagamento [DA VERIFICARE].

### Opportunita' rapide
1. Rilevamento manuale di IG/FB/LinkedIn e Ad Library con account agenzia (15 min/canale) per completare questo audit.
2. Riutilizzare i top video YouTube (demolizione/ricostruzione) come reel/short con CTA verso operacg.com.
3. Pubblicare su LinkedIn/sito le notizie EMAS e Best Supplier (contenuto istituzionale gia' esistente).
4. Aggiornare header del sito con link social e correggere i contatori a 0.
5. Definire un nome handle/pagina coerente e un hashtag di brand.
6. Creare contenuti per segmenti oggi non presidiati (condomini/Conto Termico, fotovoltaico EPC).

## Rettifica (sessione principale, 26/11/2026)
I contatori a "0" in home non sono un malfunzionamento: sono contatori animati. I valori reali nel codice (`data-value`) sono: 80 (fatturato, M), 100 (portafoglio lavori, M), 170 (contratti attivi), 1000 (lavoratori occupati), 25 (anni di storia), 3,3 (patrimonio netto, M). Restano da verificare le incoerenze con il testo del sito (500 addetti; oltre 20 anni). Vedi `02_audit/audit_sito.md`.
