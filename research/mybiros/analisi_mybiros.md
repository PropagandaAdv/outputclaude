# Analisi myBiros — stato della ricerca (19/11/2026)

## 1. Esito dell'accesso a LinkedIn — BLOCCATO

| Risorsa | Esito | Evidenza |
|---|---|---|
| LinkedIn Ad Library (`/ad-library/search?accountOwner=myBiros`) | **HTTP 403 – Cloudflare "Sorry, you have been blocked"** (browser Chromium reale, locale it-IT) | `linkedin_blocco_cloudflare_19-11-2026.png` [VERIFICATO] |
| Pagina aziendale `linkedin.com/company/mybiros/` | **403 – verifica di sicurezza Cloudflare** | stesso screenshot [VERIFICATO] |
| Thought Leader Ads dei fondatori | Non verificabili (dipendono dall'accesso a LinkedIn) | — |
| Ricerca web "myBiros LinkedIn" | Nessuna pagina LinkedIn di myBiros restituita dal motore di ricerca | [VERIFICATO] |

L'ambiente cloud usato per il lavoro è bloccato da LinkedIn. **Non ho aggirato la protezione** (sarebbe contro i termini del servizio) e **non ho inventato nessun annuncio**: `mybiros_ads.csv` contiene solo l'intestazione delle colonne richieste, senza righe.

**Cosa NON posso dire oggi:** numero di annunci attivi e storici, formati, periodi, copy, CTA, destinazioni, impression DSA, paesi, targeting dichiarato, ritmo di rotazione. Tutto ciò che nelle slide riguarda questi punti è marcato **[DA CONFERMARE]**.

**Come chiuderlo (circa 30–45 minuti, da un computer normale):**
1. Aprire l'Ad Library con il link dato, filtrare per inserzionista "myBiros" e paese Italia/UE.
2. Per ogni annuncio: salvare screenshot, copiare ID/link, e dalla scheda "Dettagli" i dati DSA (impression per range, paesi, targeting).
3. Compilare `mybiros_ads.csv` e rilanciare il calcolo in `analysis/budget_model.py` (sezione myBiros) con le impression reali.
In alternativa: collegare un computer a questa sessione di lavoro e rieseguo io la raccolta.

## 2. Cosa è VERIFICATO: sito mybiros.com (letto il 19/11/2026)

Fonte: https://www.mybiros.com/ (testo e screenshot `mybiros_sito_home.png`).

- **Posizionamento:** "Un'unica Piattaforma. Qualsiasi Documento. Dati pronti all'uso." Idea chiave: "Oltre l'OCR" — Small Language Models + OCR + Computer Vision. [VERIFICATO]
- **CTA principali:** "Prenota demo" e "Parla con un esperto". Prova sociale: recensioni Trustpilot (stelle mostrate in home). [VERIFICATO]
- **Numeri dichiarati:** 85% tempo medio risparmiato · 98% accuratezza media · 60% risparmio costo operativo · 10+ anni di R&D in AI · 50+ aziende clienti · 20 mln di documenti processati. [VERIFICATO come claim di myBiros; non verificati nel merito]
- **Documenti in primo piano:** bolletta, busta paga, carta d'identità, passaporto, ricevuta, personalizzato. [VERIFICATO]
- **Settori in primo piano:** assicurativo, finanziario, utility, lending (soluzione dedicata "Lending myBiros"). Citati anche manifattura, sanità, logistica in una frase generica. [VERIFICATO]
- **Loghi clienti in home** (es. Siglacredit, Comparetech, Ajò Energia, Revo, Fluida, Italsoft, Prestivalore, Freekar): coerenti con finance/utility/lending. [VERIFICATO]
- **Temi ricorrenti:** "più di un OCR", AI trasparente (confidence score), server europei, GDPR, "ridurre costi", errori del data entry manuale ("fino a 20 volte più errori"), dati non strutturati (80–90%). [VERIFICATO]
- **Profilo da fonti terze:** piattaforma no-code di IDP con sede a Roma, target SMB, validazione human-in-the-loop (idp-software.com); in Italia, azienda di ~5 anni (CB Insights). [fonte terza, non verificato direttamente]

## 3. Implicazioni strategiche (dedotte dal SITO, non dagli annunci)

Sono **ipotesi** da verificare con l'Ad Library: se gli annunci seguono il sito, myBiros parla soprattutto a **banche, assicurazioni, utility e lending** con documenti di identità e bollette.

**Spazio libero per Retica** [STIMA qualitativa, da confermare con l'Ad Library]:
- documenti **di filiera**: ordini d'acquisto, DDT, conferme d'ordine (logistica, manifattura, distribuzione, retail) — assenti dall'elenco documenti di myBiros;
- ruoli **operativi** (EDP/IT, back office ordini, amministrazione ciclo passivo, CEO di PMI);
- **integrazione col gestionale/ERP** e supporto vicino (clienti Retica citano la disponibilità del team);
- numeri di scala **più alti** dichiarati sul sito: 124 clienti attivi e 6.000+ scansioni al giorno (Retica) contro 50+ aziende clienti e 20 mln di documenti totali (myBiros) — metriche diverse, non direttamente confrontabili: non usarle in un confronto diretto negli annunci.

Retica non copia né cita claim, testi o creatività di myBiros.

## 4. Stima dell'investimento LinkedIn di myBiros — [STIMA] NON CALCOLABILE CON DATI REALI

LinkedIn non pubblica la spesa. Il metodo corretto parte dalle **impression DSA per annuncio**, oggi non accessibili.

**Formula:** `spesa mensile ≈ (impression/mese ÷ 1.000) × CPM`

**CPM usato (fonti recenti, USD → EUR a 0,90 [STIMA, DA CONFERMARE]):**
- Sponsored Content, traffico freddo: circa 33,80 USD (≈ 30,4 €) — ClickMinded, agg. 08/07/2026;
- single image ZenABM (211 aziende B2B, feb 2026): 59,15 USD (≈ 53,2 €); video 38,94 USD; carosello 45,28 USD; Thought Leader 49,37 USD;
- altri Paesi europei ZenABM: Paesi Bassi 50,08 USD, UK 56,62 USD; ClickMinded (lug 2026): range 30–90 USD.
- Nessun benchmark specifico per l'Italia trovato: **[DA CONFERMARE]** con dati reali di campagna.

**Tabella di sensibilità (non è la spesa di myBiros, mostra solo la scala):**

| Impression/mese | Spesa con CPM 30,4 € | Spesa con CPM 53,2 € |
|---|---|---|
| 50.000 | 1.520 € | 2.660 € |
| 150.000 | 4.560 € | 7.980 € |
| 400.000 | 12.160 € | 21.280 € |
| 1.000.000 | 30.400 € | 53.200 € |

Calcolo riproducibile: `python3 analysis/budget_model.py`.

**Fonti:** [ZenABM](https://zenabm.com/blog/linkedin-ads-benchmarks-2026) · [ClickMinded](https://www.clickminded.com/linkedin-ads-benchmarks/).
