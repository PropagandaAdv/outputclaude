# Piano ottimizzazione ClickUp — Giovanni (2026-10-28)

Stato: **Fase 1 completata (sola lettura). Nessuna modifica eseguita.** In attesa del tuo "OK".
Backup: `backup/clickup-snapshot-2026-10-28.json` · Log: `backup/clickup-log-2026-10-28.md`

## ⚠️ Prima di tutto: il prompt è arrivato troncato

Il testo si interrompe a *"Punto 2 — Gerarchia: Rinomina ogni lista chiamata "List" con"*. Mancano:
- la regola di naming per le liste (cosa c'è dopo "con");
- i **punti 3, 4, 5, 6** (e la parte finale: report, checklist manuale).

Non li invento. Qui sotto pianifico solo ciò che è scritto; per il resto serve che reincolli il testo mancante.

## Verifiche Fase 1

| Voce | Esito |
|---|---|
| Workspace ID 9012437989 | Verificato |
| Space | 41 (39 con liste, `Resources` e `Task Sharing` senza liste) |
| Folder | 0 (confermato) |
| Liste chiamate "List" | 39 (confermato "quasi tutte"). Eccezioni: "Aggiornamenti Settimanali" |
| Campi personalizzati workspace | 0 (confermato). Livello Space/lista: **non verificato** |
| Task aperti | 71 (nessuna pagina successiva). Di cui **28 nei 3 Space template** (10 Social/SEO/ADV, 9 Siti Web, 9 Email Outreach) |
| Docs | 7 documenti (Resources, Task Sharing, 2 senza Space), nessuno in Space cliente |
| Dashboard | 4 (`Dashboard`, `Dashboard1`, `Dashboard2`, `Dashboard`), ultime modifiche ott. 2025 |
| Space "Personale" | **Non esiste.** Non esiste neanche uno strumento per creare Space |
| Limite dati | Task chiusi scaricati solo in parte (ultimi ~300 + 12 liste a bassa attività): le date sotto sono "ultimo aggiornamento osservato" |

## Punto 1 — Inbox unica

- **Cosa**: lista `📥 Inbox`, descrizione: "Tutto entra qui. Smistamento quotidiano verso lo Space del cliente o dell'area."
- **Dove**: Space personale. **Non esiste e non posso crearlo** → la lista **non viene creata** (regola 1.1).
- **Checklist manuale**: (a) crea lo Space "Personale"; (b) dimmi l'ID o rilancia e creo io la lista `📥 Inbox` al suo interno.
- **Commerciale - Propaganda**: nessuno spostamento. Nel report elencherò i task non commerciali. Anticipo (inferenza dai titoli, da confermare):

| Task (ID) | Perché sembra non commerciale | Dove andrebbe |
|---|---|---|
| Template Email Social/SEO/ADV (869e5nx8m), Template Email Outreach (869e5nw5q), Template Email Siti (869e5nw14) | Template interni | Space template / Resources |
| Remake sito propaganda (869er6x0v) | Progetto interno | Marketing - Propaganda |
| Cancellare dominio Econ Comunicazione (869f9r33x), Salmeri/Costa "cancellare dominio" | Gestione domini | Amministrazione - Propaganda |
| Propaganda - Cambiare password TeamSystem ID (869fhcw4n), Stripe SimpL (869feqeeh) | Amministrazione | Amministrazione - Propaganda |
| Leantech - Applicare modifiche al sito (869f1d85m), Leantech - rendering (869fawjzz), Cemis - go-live (869f31e9k), Regicode - dominio/cPanel (869ffnxjb), Tecnoradiant - DNS (869f755fz) | Delivery/progetto cliente | Space del cliente (Leantech, Cemis, Auto Technology, Tecnoradiant: nessuno Space) |
| Tutorial Claude - Refero design - Jet (869f82jt6) | Formazione interna | Resources |

## Punto 2 — Gerarchia (parziale: regola di naming mancante)

- **Cosa**: rinominare le 39 liste "List" (unica operazione di modifica ammessa, nessun task toccato).
- **Nome nuovo**: ⛔ non specificato nel prompt. **Proposta provvisoria** (da confermare): usare il nome dello Space, così le viste globali mostrano il cliente. Alternativa: "Attività" (identico ovunque, non risolve il problema delle viste globali).
- Log: per ogni lista salvo ID e nome precedente ("List") prima del rename → reversibile.

| Lista (ID) | Space | Nome attuale | Nome nuovo (provvisorio) |
|---|---|---|---|
| 901208256880 | Template Gestione Social/SEO/ADV | List | Template Gestione Social/SEO/ADV |
| 901208275574 | Template Sviluppo Siti Web | List | Template Sviluppo Siti Web |
| 901206273126 | Template Email Outreach | List | Template Email Outreach |
| 901208189038 | Commerciale - Propaganda | List | Commerciale - Propaganda |
| 901209768949 | Rinnovo Contratto | List | Rinnovo Contratto |
| 901208907007 | Marketing - Propaganda | List | Marketing - Propaganda |
| 901208229728 | Amministrazione - Propaganda | List | Amministrazione - Propaganda |
| 901215499098 | Lavoretti | List | Lavoretti |
| 901218104495 | Chiamate a freddo - Propaganda | List | Chiamate a freddo - Propaganda |
| 901207520157 | Noi Srl | List | Noi Srl |
| 901207909422 | Swifty | List | Swifty |
| 901208057119 | Assicurazioni CO | List | Assicurazioni CO |
| 901208275969 | AgriPM (Sito Web) | List | AgriPM (Sito Web) |
| 901208256959 | Pulkra/Nativus/Nord Resine | List | Pulkra/Nativus/Nord Resine |
| 901209465500 | Orangorenna | List | Orangorenna |
| 901209991236 | Implementa Group | List | Implementa Group |
| 901215766916 | Cemis Sistemi | List | Cemis Sistemi |
| 901210658014 | Noyfar | List | Noyfar |
| 901215271718 | Che Finestra | List | Che Finestra |
| 901211144124 | Global Expo | List | Global Expo |
| 901211160142 | Osteria Andes | List | Osteria Andes |
| 901212383673 | Velamp | List | Velamp |
| 901212791347 | Agrilombricoltura | List | Agrilombricoltura |
| 901213044797 | Gesam | List | Gesam |
| 901213625457 | Looking The Box | List | Looking The Box |
| 901215427556 | Studio Colombo | List | Studio Colombo |
| 901215503639 | Biochem Solutions | List | Biochem Solutions |
| 901215840175 | Mag Face | List | Mag Face |
| 901216077681 | Fiori Meccanica | List | Fiori Meccanica |
| 901216579579 | Gruppo Vis | List | Gruppo Vis |
| 901218772976 | BF Consulting | List | BF Consulting |
| 901219026790 | Auto Technology | List | Auto Technology |
| 901219073306 | Baschieri Costruzioni | List | Baschieri Costruzioni |
| 901219842382 | 3B Polirim | List | 3B Polirim |
| 901221294100 | Iride Acque | List | Iride Acque |
| 901222166842 | Pokertalk | List | Pokertalk |
| 901222232263 | We4 Comunicazione | List | We4 Comunicazione |
| 901222937836 | Leantech | List | Leantech |
| 901220021199 | Report & Andamento Progetti | List | Report & Andamento Progetti |

Rimane invariata: "Aggiornamenti Settimanali" (901220021201).
Non fattibile/da fare a mano: creare Folder per raggruppare (non richiesto nel testo ricevuto), spostare liste tra Space.

## Punti 3–6

⛔ **Testo non ricevuto.** Cosa creare, dove, con quali nomi e cosa resta manuale: da definire dopo che reincolli il resto del prompt. Strumenti che ho verificato come disponibili in generale: creare liste/folder, Docs, campi personalizzati (`field.create`), viste (`view.create`), task nuovi. Non disponibile: creare Space.

## Classificazione clienti (60 / 180 giorni, oggi 2026-10-28)

Basata sull'ultimo aggiornamento osservato (aperti + chiusi scaricati). Gli Space interni e i template sono in tabella a parte.

**ATTIVO (≤60 gg)** — Mag Face, Iride Acque, Leantech, Auto Technology, Che Finestra, Gesam, Assicurazioni CO, We4 Comunicazione (0–1 gg) · BF Consulting (6) · Swifty (6) · Gruppo Vis (9) · Cemis Sistemi (12) · Pokertalk (15) · Fiori Meccanica (15) · 3B Polirim (20) · Implementa Group (29) · Studio Colombo (30) · Baschieri Costruzioni (36)

**DORMIENTE (60–180 gg)** — Osteria Andes (61, al limite) · Noyfar (63) · Chiamate a freddo - Propaganda (162, interno) · Rinnovo Contratto (177, al limite)

**INATTIVO (>180 gg)** — Biochem Solutions (204) · Looking The Box (209) · Noi Srl (231) · AgriPM (259) · Agrilombricoltura (294) · Velamp (328) · Global Expo (470, con 2 task aperti scaduti da ott. 2025) · Orangorenna (485) · Pulkra/Nativus/Nord Resine (nessun task osservato: **non verificato**)

**Interni / altro** — Commerciale (0), Amministrazione (0), Marketing (16), Lavoretti (9): attivi. Report & Andamento Progetti (89 gg, un solo task di test): dormiente. Resources, Task Sharing: solo Docs. Template ×3: task aperti dal 2026-07, da escludere dalle viste globali.

Nota: la soglia "solo task scaduti da oltre 6 mesi" è verificabile solo per Global Expo; per gli altri INATTIVO deriva dalla data di aggiornamento. Nessun Space viene toccato da questa classificazione.

## Cosa mi serve per procedere

1. Il testo mancante del prompt (naming liste + punti 3–6 + report finale).
2. Conferma del nome nuovo delle liste (proposta: nome dello Space).
3. Il tuo **"OK"**. Fino ad allora non scrivo nulla su ClickUp.
