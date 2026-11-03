# Showcase 9:16 — Tecnomarmi

Progetto Remotion (TypeScript). Tutto ciò che si modifica sta in `remotion/src/config.ts`.

## Cosa modificare
- **Testi**: `hook`, `captions`, `firma`, `handle`, `cta` (le parole tra `*asterischi*` prendono il colore accento).
- **Colori**: `colors` (letti dal sito: ink `#101214`, graphite `#2C3036`, stone `#EAEBEB`).
- **Durate/tempi**: `heroSeconds`, `mobileStart`, `firmaStart`, `total` e l'array `SHOTS` (start/dur in secondi, griglia 0,5 s = 120 BPM).
- **Versione senza testi**: composizione `ShowcaseClean`.

## Render
```bash
cd remotion
npm install
npx remotion studio                                   # anteprima interattiva
npx remotion render src/index.ts Showcase ../out/showcase_tecnomarmi_9x16.mp4 --codec=h264 --crf=14 --pixel-format=yuv420p
npx remotion render src/index.ts ShowcaseClean ../out/showcase_tecnomarmi_9x16_clean.mp4 --codec=h264 --crf=14 --pixel-format=yuv420p
npx remotion still src/index.ts Showcase ../out/cover.png --frame=<N>
```

## Origine dei media (`remotion/public`)
Catturati con Playwright dal sito pubblico (script in `work/pw/`): hero a 60 fps deterministici (1×), sezioni a DPR 3, click reale sul filtro, mobile 390×844 DPR 3. Per ricatturare: `node work/pw/cap_hero.js` ecc.

## Licenza
Remotion è gratuito per individui e piccole aziende; oltre una certa soglia di dipendenti serve una licenza commerciale. Verifica su https://www.remotion.dev/license.
