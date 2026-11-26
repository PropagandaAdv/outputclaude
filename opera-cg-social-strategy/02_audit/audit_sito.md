# Fase 1 — Audit del sito operacg.com (consultato il 26/11/2026)

Metodo: download HTML delle pagine pubbliche (curl) + lettura codice sorgente + REST API WordPress pubblica. Nessun accesso a backend o analytics.

## 1. Mappa del sito [VERIFICATO]
Sito WordPress con tema Avada (sviluppato da e-mind). Pagine (da `wp-json/wp/v2/pages`): Home, Il gruppo, Attività (realizzazioni), Servizi (+ sottopagine ESCo, EPC, Consulenza fiscale, Servizi di ingegneria, Servizi per le imprese), Conto Termico, Certificazioni, Associarsi, News, Contatti, privacy/cookie.
- **Attività/Realizzazioni**: 9 categorie (Residenziale, Ristrutturazioni, Commerciale, Direzionale, Industriale, Infrastrutturale, Energie rinnovabili, Opere pubbliche, Aree verdi) create il 27/10/2022 e non aggiornate: sono schede di categoria, **nessun caso studio con nome cantiere, cliente, numeri o prima/dopo**.
- **News**: 2 articoli in tutto (EMAS 06/07/2026; premio Hera a consorziata 15/06/2026).
- **Certificazioni**: pagina aggiornata il 13/11/2026, con PDF scaricabili (ISO 9001/14001/45001/37001/50001, EMAS, SA8000, SOA, ESCo UNI CEI 11352) — punto forte.
- **Header title**: "OPERA CG – Building General Contractor"; payoff in Contatti: "Il contractor partner di cui puoi fidarti"; payoff in home: "Il tuo futuro, il nostro presente".

## 2. Chiarezza dell'offerta per i 6 segmenti
| Segmento | Dove è servito sul sito | Valutazione |
|---|---|---|
| 1. Committenti privati grandi opere (conto terzi) | Home + "Attività" (categorie senza casi) | **Debole**: dichiarato "general contractor" solo nel title; manca pagina "Per chi costruisce / Costruzione chiavi in mano" e casi con numeri |
| 2. Sviluppatori FV fino a 10 MWp (EPC) | Pagina /epc/ (testo generico "cos'è un EPC", aggiornata 2023) | **Debole**: non cita MWp, media tensione, SOA OG9, tempi di connessione, referenze, ettari. Nessuna landing dedicata |
| 3. Proprietari terreni / aziende agricole | Nessuna pagina | **Assente** (nessun cenno ad agrivoltaico o verifica idoneità terreno) |
| 4. Amministratori condominio | Voce "Acquisto crediti d'imposta" e "CER" in Servizi, un rigo | **Assente/debole**: nessuna pagina condomini, né Servizio Energia |
| 5. PA / Conto Termico | /conto-termico/ (aggiornata 30/10/2025) | **Buona base**: spiega procedura in 4 step, interventi per SOA (OG9, OG1, OS6, OS28, OS30, OG11) e claim "Costo Zero". Da verificare coerenza con Conto Termico 3.0 (vedi Fase 3) |
| 6. Imprese da consorziare | /associarsi/ (07/11/2025) | **Buona**: benefici chiari (certificazioni condivise, grandi appalti, supporto gare), elenco chi può aderire, form |

## 3. CTA, form e prove sociali
- **Form**: presenti in Contatti e Associarsi (campi email, telefono, scelta radio, checkbox privacy, reCAPTCHA). Home e Conto Termico contengono 1 elemento form ciascuno (da verificare se visibile/sostitutivo). **Non esistono form differenziati per segmento né lead magnet** [VERIFICATO: nessun download/ form dedicato nel codice delle pagine].
- **Contatti**: sede legale Milano (Via Cusago 96/A), operativa Imola (Via Allende 1), tel. 0542 642594, info@operacg.com. **La sede di Bari, citata dal cliente e in home ("3 sedi: Imola, Milano, Bari"), non compare nella pagina Contatti.**
- **Prove sociali**: numeri in home (contatori animati): fatturato **80 M**, portafoglio lavori **100 M**, **170** contratti attivi, **1000** lavoratori occupati, **25** anni di storia, patrimonio netto **3,3 M** [VERIFICATO: valori `data-value` nel codice; unità "M" da etichetta grafica, valuta non esplicitata].
- **Incoerenze da sanare prima di comunicare i numeri**: testo home "oltre **500** addetti" vs contatore "**1000** lavoratori occupati" (il cliente dichiara 500+); pagina Il gruppo "oltre **20** anni" vs contatore "**25** anni" (il cliente dichiara 25+). → [DA VERIFICARE con il cliente].
- Loghi clienti, testimonianze, casi studio: **assenti**.

## 4. Tracciamenti nel codice sorgente (home) [VERIFICATO]
| Strumento | Esito |
|---|---|
| Google Tag Manager | **Presente** (GTM-NSGJS55) |
| Google Analytics | Riferimento a **Universal Analytics UA-74420576-1** (dismesso da Google dal 2023) → GA4 eventualmente solo via GTM, non verificabile dal sorgente |
| Meta Pixel | **Presente** (`fbq('init')`, ID 528973914673613). Eventi di conversione (Lead/Contact) non verificabili senza test |
| LinkedIn Insight Tag | **Non rilevato** nel sorgente (potrebbe essere dentro GTM: da verificare) |
| Consenso cookie | Cookiebot rilevato (i tag vanno verificati in modalità "consenso accordato") |
| Form → conversione | Nessun evento dataLayer visibile nel sorgente: [DA VERIFICARE] in GTM |
→ **Conseguenza**: le campagne potranno misurare solo se GA4 + eventi form + Insight Tag vengono verificati/configurati nel setup (mese 1).

## 5. L'offerta FV/EPC è comunicata con la stessa forza dell'edilizia? [INFERENZA]
**No.** Ragionamento: la home non cita mai "fotovoltaico" né "EPC" (0 occorrenze nel testo della home); il title di sito è "Building General Contractor"; FV/EPC compare solo in /servizi/ (2 righe), in /epc/ (testo generico del 2023) e come voce nel Conto Termico. Questo spiega l'obiezione del cliente "non sapevo che faceste fotovoltaico / EPC".

## 6. Priorità sul sito (a supporto dei social)
1. Landing dedicate per segmento (EPC FV, Agrivoltaico/terreni, Conto Termico PA, Condomini, Costruzione chiavi in mano, Associarsi) con form e lead magnet.
2. Sezione "Casi studio / Prima e Dopo" con 5–8 schede reali (dati dal cliente).
3. Home: portare FV/EPC e ESCo nel messaggio principale e nei numeri.
4. Allineare numeri (500/1000 addetti; 20/25 anni) e aggiungere la sede di Bari in Contatti.
5. Tracciamenti: GA4 + eventi form + Meta Pixel (Lead) + LinkedIn Insight Tag + UTM e consent mode.
