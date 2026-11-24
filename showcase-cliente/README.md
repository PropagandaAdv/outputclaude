# Showcase INPROTEC — video verticale 9:16

Progetto Remotion (React + TypeScript). Output: 1080×1920, 60 fps, 26,2 s, senza audio.

## Modificare testi, colori, durate
Tutto sta in `src/config.ts`:
- `TEXT` — hook, didascalie, CTA, firma, handle.
- `COLORS` — sfondo e accento.
- `SHOTS` — elenco delle inquadrature del montaggio (tipo, durata in frame, regione di crop in px CSS del viewport 1440×900). Il beat a 120 BPM è `BEAT = 30` frame: tieni le durate su multipli di 15/30.
- `MOBILE_SHOTS`, `SIGN_FRAMES`, `HERO_FRAMES` — durate delle altre scene. `TOTAL_FRAMES` si ricalcola da solo.

## Ri-renderizzare
```bash
npm install
npx remotion studio                       # anteprima interattiva
npx remotion render src/index.ts Showcase out/showcase_inprotec_9x16.mp4 \
  --video-bitrate=20M --pixel-format=yuv420p --props='{"showText":true}'
npx remotion render src/index.ts Showcase out/showcase_inprotec_9x16_clean.mp4 \
  --video-bitrate=20M --pixel-format=yuv420p --props='{"showText":false}'
ffmpeg -i out/showcase_inprotec_9x16.mp4 -c copy -movflags +faststart out/final.mp4
```
Se Chrome non si scarica, aggiungi `--browser-executable=/percorso/chrome`.

## Frame sorgente (`public/`, non versionati)
`public/hero`, `public/shots/*`, `public/mobile` sono sequenze JPEG a 60 fps prodotte da `work/capture.js` e `work/shots.js` (Playwright/Chromium, senza UI del browser). Per rigenerarle:
```bash
node work/capture.js hero      # hero (scroll 0→fine, 11 s + 0,9 s di tenuta)
node work/capture.js mobile
node work/shots.js             # inquadrature del montaggio a DPR 2
```
poi sposta le cartelle in `public/`.

## Licenza
Remotion è gratuito per individui e piccole aziende; oltre una certa soglia di dipendenti serve una licenza commerciale: verifica su remotion.dev/license.
