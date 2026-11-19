# Strategia video LinkedIn — Retica (storyboard con timecode)

> **FASE 2 — non in programma all'inizio.** Con un budget di 2.000 € al mese non si investe in video nella fase iniziale: gli annunci di partenza usano solo immagini e post del fondatore. Questo storyboard resta pronto per quando i primi risultati lo giustificheranno.

**Stato dei materiali [DA CONFERMARE]:** la cartella `assets/video-retica/` è **vuota** (verificato il 19/11/2026). Non ho quindi durata, formato, sottotitoli e audio dei video del cliente, e non è stato possibile produrre anteprime con ffmpeg (ffmpeg è disponibile nell'ambiente, ma non c'è sorgente da tagliare).
Sul sito retica.ai è incorporato un video introduttivo YouTube ("Scopri Retica!", id `fTL-2IPMevU`) [VERIFICATO la presenza]; durata e diritti d'uso per i tagli sono da confermare.

**Scheda da compilare per ogni video consegnato:** nome file · durata · risoluzione e rapporto (16:9 / 1:1 / 4:5 / 9:16) · audio sì/no (voce, musica) · sottotitoli sì/no e lingua · sorgenti editabili (progetto, schermate pulite).

## Regole di montaggio
- **Hook nei primi 3 secondi:** una domanda o un problema visibile ("Quante righe di DDT ricopi ogni giorno?"), non il logo.
- **Sottotitoli italiani incisi (burned-in) obbligatori.** Motivo: LinkedIn indica che circa il **79%** dei video nel feed viene guardato senza audio ([LinkedIn, "4 Tips for Better Video Ads on LinkedIn in 2021", 03/07/2021](https://www.linkedin.com/business/marketing/blog/linkedin-ads/4-tips-for-better-video-ads-on-linkedin-in-2021)). Il dato "85%" circola solo su blog di terzi e **non ha una fonte primaria**: non lo cito nelle slide.
- **Formati:** 1:1 e 4:5 per il feed (più spazio su mobile); 9:16 per la visualizzazione mobile; 16:9 per YouTube/sito. Verificare le specifiche aggiornate in Campaign Manager prima del montaggio [DA CONFERMARE].
- Brand: logo nei primi/ultimi secondi, palette Retica (navy #23253C, corallo #FF8A73, blu #5580FF), font Poppins. Interfaccia reale di prodotto e documenti stilizzati, niente foto stock.

## Taglio 15 secondi — "Il costo del copia-incolla" (TOFU, 1:1 / 4:5 / 9:16)
| Tempo | Immagine | Sottotitolo / testo a schermo |
|---|---|---|
| 0:00–0:03 | Pila di DDT che cresce. **Hook** | "Quante righe di DDT ricopi ogni giorno?" |
| 0:03–0:08 | Un DDT: Retica evidenzia righe, codici, quantità e unità di misura (clip UI [DA CONFERMARE]) | "Retica legge il documento, qualunque sia il layout" |
| 0:08–0:12 | I dati fluiscono verso ERP/gestionale | "…e i dati arrivano nel tuo gestionale" |
| 0:12–0:15 | Logo + CTA | "Richiedi una demo · retica.ai" |

## Taglio 30 secondi — "Dal documento al gestionale" (TOFU/MOFU)
| Tempo | Immagine | Sottotitolo |
|---|---|---|
| 0:00–0:03 | Hook: operatore che digita, schermo diviso con PDF | "Il tuo team non è nato per ricopiare documenti" |
| 0:03–0:09 | Documenti di logistica che scorrono: DDT, listini fornitori, fatture commerciali, certificati di origine | "DDT e listini: ogni layout è diverso" |
| 0:09–0:18 | I 4 step in UI: identifica · etichetta · salva · crea modello | "Retica impara il tuo documento in 4 passi" |
| 0:18–0:24 | Export CSV/XML/JSON → ERP | "Esporta nel formato che legge il tuo gestionale" |
| 0:24–0:28 | Numeri: 6.000+ scansioni/giorno · 124 clienti attivi | "Già scelta da 124 aziende" |
| 0:28–0:30 | CTA | "Calcola il tuo risparmio su retica.ai" |

## Taglio 60 secondi — "Demo guidata" (MOFU/BOFU, retargeting su chi ha visto il 50%)
| Tempo | Contenuto |
|---|---|
| 0:00–0:05 | Hook problema + costo del data entry manuale (rimando al calcolatore) |
| 0:05–0:20 | Caricamento di un DDT reale (o di esempio) → data capture → etichette |
| 0:20–0:35 | Validazione e modello: conferma/modifica del modello di lettura |
| 0:35–0:45 | Condizioni ed esportazione verso il gestionale; tracciamento dei documenti elaborati |
| 0:45–0:53 | Testimonianza in sovrimpressione (testo dal sito; consenso da confermare) |
| 0:53–0:60 | CTA "Richiedi demo" + calcolatore del risparmio |

## Utilizzo nella struttura del funnel
- 15 s → TOFU, ottimizzazione su visualizzazioni, creazione dei pubblici "ha visto il 50% / 75%".
- 30 s → TOFU/MOFU, prova di due hook (A/B).
- 60 s → solo retargeting (50%/75% dei video brevi, visitatori del sito).
- Estrazione di 3 frame fissi per annunci a immagine e copertine (esempi in `output/mockup/A01_*`).

## Se arrivano i video: comandi pronti (ffmpeg)
```bash
# taglio 15 s dal secondo 0, 1:1 centrato, con sottotitoli incisi da .srt
ffmpeg -ss 0 -t 15 -i input.mp4 -vf "crop='min(iw,ih)':'min(iw,ih)',scale=1080:1080,subtitles=sub_it.srt" -c:a aac out_15s_1x1.mp4
# 4:5 (1080x1350)
ffmpeg -ss 0 -t 15 -i input.mp4 -vf "scale=1080:-2,pad=1080:1350:(ow-iw)/2:(oh-ih)/2:color=0x23253C,subtitles=sub_it.srt" -c:a aac out_15s_4x5.mp4
```
