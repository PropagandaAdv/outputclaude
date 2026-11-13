// =====================================================================
//  CONFIG — modifica qui testi, colori, tempi. Niente codice da toccare.
//  Tutti i tempi sono in FRAME a 30 fps (30 frame = 1 s, 15 frame = 1 beat a 120 BPM).
// =====================================================================
export const FPS = 30;
export const W = 1080;
export const H = 1920;

export const TEXT = {
  hook: ['Da Londra a Cambridge,', 'in un sito'],       // 6 parole
  hookAccent: 'Cambridge,',                                   // parola nel colore accento
  client: 'Cambridge Centre of English · Modena',            // dal <title> del sito
  captions: ['Percorsi chiari', 'Livelli in un click', 'Ogni dettaglio, curato'],
  signature: 'Web design · Giovanni Bertoni',                 // FIRMA_FINALE (da esempio del master prompt: verifica!)
  handle: '@giovannibertoni',                                 // HANDLE (da esempio del master prompt: verifica!)
  cta: 'Vuoi un sito così? Scrivimi',
};

export const COLORS = {
  bg: '#070D18',          // dark-cinematic
  glow: '#036AAC',        // blu del sito (theme-color)
  accent: '#FF4D6A',      // rosso/rosa del sito, schiarito per contrasto su scuro
  red: '#E4113A',
  text: '#FFFFFF',
  pill: 'rgba(7,13,24,0.72)',
};

// ---- Atto 1: hero integrale (hero.mp4 = scroll reale 1x, 376 frame) ----
export const HERO_FRAMES = 375;

// ---- Atto 2: montaggio. src = frame del file body.mp4 (scroll 7300→14094 px, 30fps) ----
// type: F speed-ramp | B crop 9:16 | C close-up | A mockup micro-scroll | D interazione reale | E stack
export type Shot =
  | {type: 'F'; dur: number; from: number; mid: number; to: number}
  | {type: 'B'; dur: number; still: string; x0: number}               // still = public/stills/<nome>.jpg (2880x1620), x0 = px sorgente
  | {type: 'C'; dur: number; still: string; x0: number; y0: number}   // regione 864x864
  | {type: 'A'; dur: number; src: number}
  | {type: 'D'; dur: number; srcSec: number}                          // esami.mp4, secondi
  | {type: 'E'; dur: number; srcs: number[]};

export const SHOTS: Shot[] = [
  {type: 'F', dur: 30, from: 40, mid: 130, to: 162},   // arrivo su "Non sai da dove iniziare?"
  {type: 'B', dur: 30, still: 'b1', x0: 1800},            // corsi: card
  {type: 'C', dur: 22, still: 'c1', x0: 1700, y0: 640},   // corsi: close-up card
  {type: 'A', dur: 23, src: 290},                      // esami: micro-scroll
  {type: 'C', dur: 15, still: 'c2', x0: 1130, y0: 330},    // esami: close-up livello
  {type: 'D', dur: 38, srcSec: 3.0},                   // esami: click reali sui livelli
  {type: 'B', dur: 22, still: 'b2', x0: 230},             // chi siamo: numeri
  {type: 'C', dur: 15, still: 'c3', x0: 270, y0: 80},    // scuole: titolo
  {type: 'A', dur: 15, src: 436},                      // aziende
  {type: 'E', dur: 30, srcs: [509, 660]},              // contatti + footer
];
// didascalie: [indice testo, frame inizio, frame fine] relativi all'inizio dell'Atto 2
export const CAPTION_SPANS: [number, number, number][] = [[0, 30, 82], [1, 105, 180], [2, 180, 240]];

export const MOBILE = {dur: 60, clips: [30, 75, 140]};      // 3 inquadrature da 20 frame (mobile.mp4)
export const FINAL_FRAMES = 90;
export const TOTAL = HERO_FRAMES + SHOTS.reduce((a, s) => a + s.dur, 0) + MOBILE.dur + FINAL_FRAMES;
