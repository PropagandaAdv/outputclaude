# Analisi myBiros su LinkedIn (19/11/2026)

## 1. Fonti e cosa è stato possibile vedere

| Fonte | Esito |
|---|---|
| **Screenshot dell'Ad Library LinkedIn, pagina myBiros** (PDF fornito da Propaganda Adv, catturato il 19/11/2026 alle 18:49) — `adlibrary_myBiros_2026-11-19.pdf` | **Letto.** "35 ads match your search criteria", ordinati dal più recente. **25 annunci visibili** nella schermata, tutti catalogati. [VERIFICATO] |
| Schede "View details" di ogni annuncio (date, impression per fascia, paesi, targeting dichiarato) | **Non incluse** nello screenshot. [DA CONFERMARE] |
| Pagina aziendale LinkedIn di myBiros e Thought Leader Ads dei fondatori | Non verificati: l'accesso diretto a LinkedIn dal nostro ambiente è bloccato (Cloudflare 403, `linkedin_blocco_cloudflare_19-11-2026.png`). |
| Sito mybiros.com | Letto il 19/11/2026. [VERIFICATO] |

Il censimento è in `mybiros_ads.csv` (25 righe) con un ritaglio per ogni annuncio in `screens/`. I testi sono quelli mostrati in lista (spesso troncati con "…"). ID e link LinkedIn degli annunci non compaiono nella lista: ho assegnato ID interni `MB-01…MB-24` (MB-14 contiene due annunci identici sovrapposti, 14a e 14b).

## 2. Sintesi strategica (sui 25 annunci visibili su 35)

**Mix di formati** [VERIFICATO]
- **13 Document Ad** (52%) da 5 a 9 pagine; titoli del tipo "IDP nel settore utility…", "Lending finanziario: …".
- **11 immagini singole** (44%), con il pulsante dentro la creatività.
- **1** annuncio con anteprima non caricata (probabile video, non determinabile).
- Il formato "Document Ad" è dedotto dall'etichetta "Preview N of N pages" mostrata dall'Ad Library [etichetta VERIFICATA, formato STIMA]. Nessun Conversation Ad né Event Ad visibile. Tutti pubblicati dalla pagina "myBiros": nessun Thought Leader Ad nella lista (i post sponsorizzati da profili personali non compaiono qui).

**Temi e settori** [VERIFICATO]
- **20 su 25 sul credito (lending)**: l'idea portante è il **"Time-to-Yes"**, il tempo per arrivare all'approvazione.
- **5 su 25 sull'utility** (attivazioni, switching, bollette, documenti d'identità).
- **0 su 25 su logistica, DDT, ordini o listini fornitori.**

**Lead magnet e call to action** [VERIFICATO]
- Un solo lead magnet ricorrente: il **"one-pager"** (6 annunci: "Scarica il one-pager" / "Ottieni il one-pager").
- CTA "Scopri come" in 5 annunci, con la barra sotto l'immagine "Scopri come ora!" o "Scopri come L'AI può ottimizzare ogni fase del credito."
- I Document Ad non mostrano una CTA nella lista.
- Nessuna menzione di demo o call con esperto negli annunci visibili (restano le CTA del sito: "Prenota demo", "Parla con un esperto").

**Messaggi ricorrenti** [VERIFICATO]
- Apertura con una **domanda o un problema** ("Raccogli ancora informazioni manualmente?", "Qual è oggi il tuo time-to-yes?"), qualche emoji (❌ ⏱ 🧠 👇).
- **Numeri forti dichiarati da myBiros** (non verificati nel merito): fino a 5x più veloce, −70% sul Time-to-Yes, −40% sui costi, 3X la produttività dell'underwriting, "20,5% di switching" nel mercato utility, "oltre il 50% delle informazioni raccolto a mano", "mutui = 80% dei portafogli retail, ancora 30+ giorni".
- Termine "IDP" (Intelligent Document Processing) usato nei titoli dei Document Ad.
- **Non compaiono** nelle schermate: clienti citati, testimonianze, video, GDPR o sicurezza, "più di un OCR".

**Ritmo di rotazione** [VERIFICATO sui visual, resto STIMA]
- Pochi visual riusati con testi introduttivi diversi: lo stesso visual "Time-to-Yes / one-pager" compare in 4 annunci (MB-01, 06, 21, 23), "Lending: Accelera il Time-to-Yes" in 2 (MB-03, 09), un Document Ad utility è doppio (MB-07/08), uno sul lending in filiale è doppio (MB-14a/b). I 11 annunci a immagine singola usano solo 7 visual distinti: sembra una **strategia di test dei testi** su poche creatività. Il periodo di pubblicazione non è visibile.

**Settori e ruoli presi di mira** [STIMA dai contenuti]: responsabili del credito/lending e dell'underwriting (banche, fintech, intermediari), utility (B2C e B2B). I ruoli e il targeting dichiarato (DSA) non sono visibili.

## 3. Punti di forza e lacune sfruttabili da Retica

**Cosa fa bene myBiros (da imitare nella struttura, non nel contenuto):**
- una promessa sola, memorabile e misurabile ("Time-to-Yes");
- molti Document Ad (carosello di pagine): il formato più usato;
- un'esca semplice e ripetuta (il one-pager).

**Lacune** (sul campione visibile):
- **Nessun annuncio sulla logistica**, sui DDT, sui listini o sull'integrazione con il gestionale/magazzino.
- **Nessuna prova sociale visibile** (clienti, testimonianze): Retica ha Carraro e Le Messaggerie Nazionali.
- **Nessun video e nessun Thought Leader Ad visibile.**
- Nessuna demo come CTA diretta negli annunci.

## 4. Stima dell'investimento [STIMA] — ancora non calcolabile con dati reali

Date e impression per annuncio non sono nella lista. Ho però il numero di annunci: **35**.

Formula: `spesa ≈ (impression totali ÷ 1.000) × CPM`. CPM usato: 30,4 € (Sponsored Content, ClickMinded 08/07/2026, 33,80 $ × 0,90) – 53,2 € (single image, ZenABM 16/02/2026, 59,15 $ × 0,90). Nessun benchmark specifico per l'Italia. [DA CONFERMARE]

**Scala complessiva (tutta la vita dei 35 annunci), puramente illustrativa:**

| Impression per annuncio | Impression totali | Spesa con CPM 30,4 € | Spesa con CPM 53,2 € |
|---|---|---|---|
| 5.000 | 175.000 | 5.320 € | 9.310 € |
| 20.000 | 700.000 | 21.280 € | 37.240 € |
| 50.000 | 1.750.000 | 53.200 € | 93.100 € |

Non è una stima di myBiros: mostra la scala. Per trasformarla in un dato servono, per ciascun annuncio, la **fascia di impression** e le **date** della scheda "View details" (circa un minuto ad annuncio). Calcolo riproducibile: `python3 analysis/budget_model.py`.

## 5. Profilo da sito e fonti terze (invariato)

Sito mybiros.com: "Un'unica Piattaforma. Qualsiasi Documento. Dati pronti all'uso.", "Oltre l'OCR"; claim 85% tempo risparmiato, 98% accuratezza, 60% risparmio costi, 50+ clienti, 20 mln di documenti; documenti: bolletta, busta paga, carta d'identità, passaporto, ricevuta; settori: assicurativo, finanziario, utility, lending ("Lending myBiros" per banche, istituti di credito, fintech). Sede Roma e target SMB da fonte terza (idp-software.com).

**Fonti:** Ad Library LinkedIn (screenshot del 19/11/2026) · mybiros.com · [ZenABM](https://zenabm.com/blog/linkedin-ads-benchmarks-2026) · [ClickMinded](https://www.clickminded.com/linkedin-ads-benchmarks/).
