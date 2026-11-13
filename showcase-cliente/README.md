# Showcase 9:16 — Cambridge Centre of English

## Struttura
- `remotion/src/config.ts` — **tutto quello che si modifica**: testi (`TEXT`), colori (`COLORS`), durata hero (`HERO_FRAMES`), elenco shot (`SHOTS`, durata in frame a 30 fps, 15 frame = 1 beat a 120 BPM), didascalie (`CAPTION_SPANS`), scena mobile e finale.
- `remotion/public/` — sorgenti: `hero.mp4` (hero a 1×), `body.mp4` (resto del sito, 2880×1620), `esami.mp4` (click reali), `mobile.mp4`, `stills/` (fotogrammi fermi per crop/close-up), `hero0.jpg` (frame 0, usato per il loop).
- `tools/` — script Playwright usati per la ri-cattura pulita (nessuna UI del browser / widget / watermark).

## Rendering
```bash
cd remotion
npm install
npx remotion render src/index.ts Main  ../out/showcase_9x16.mp4       --video-bitrate 20M --muted
npx remotion render src/index.ts Clean ../out/showcase_9x16_clean.mp4 --video-bitrate 20M --muted
npx remotion still  src/index.ts Main  ../out/cover.jpg --frame=90
npx remotion studio   # anteprima interattiva
```
`remotion.config.ts` punta a `/opt/pw-browsers/chromium`: rimuovi quella riga sul tuo computer.

## Cambiare un testo / un colore / un taglio
Apri `src/config.ts`, modifica e ri-renderizza. Esempio: `TEXT.signature`, `TEXT.handle` (**verifica**: sono presi dagli esempi del master prompt), `COLORS.accent`. Per spostare un taglio cambia `dur` degli shot (la somma totale aggiorna da sola la durata del video).

## Ri-catturare il sito
`NODE_PATH=$(npm root -g) node tools/capture_scroll.js …` (hero, screencast 1×) e `tools/capture_shots.js …` (screenshot DPR 2 deterministici). Poi `tools/frames2cfr.py` e ffmpeg all-intra (`-g 1`).

## Licenza
Remotion è gratuito per individui e piccole aziende; oltre una certa soglia di dipendenti serve una licenza commerciale: verifica su https://www.remotion.dev/license.
