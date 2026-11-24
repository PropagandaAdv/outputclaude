// ============================================================
// CONFIG — modifica qui testi, colori e durate (niente codice).
// ============================================================
export const FPS = 60;

export const COLORS = {
  ink: '#0A0B0D',        // sfondo (dal sito)
  accent: '#E5395B',     // rosso INPROTEC schiarito per contrasto AA su nero
  text: '#F4F2EE',
  textDim: 'rgba(244,242,238,0.72)',
};

export const TEXT = {
  // Hook scelto (alternative: vedi caption.txt)
  hook: ['Dal pozzo alla pompa,', 'in un sito'],
  hookAccentWord: 'sito',
  caption1: 'Design su misura',
  caption2: 'Ogni dettaglio, curato',
  captionMobile: 'Anche su mobile',
  cta: ['Vuoi un sito così?', 'Scrivimi'],
  signature: 'Web design · Giovanni Bertoni',
  handle: '@giovannibertoni',
};

// ---- Durate (in frame a 60 fps) ----
export const HERO_FRAMES = 720;           // 12,0 s: ciclo hero integrale (11 s scroll + 0,9 s hold + zoom-through)
export const HERO_CAPTURED = 714;         // frame catturati in public/hero
export const BEAT = 30;                   // 120 BPM -> un beat = 0,5 s = 30 frame

// ---- Montaggio (Atto 2) ----
// type: A sezione nel mockup | B crop 9:16 | C close-up | D interazione reale | F speed ramp
// region: x,y in px CSS del viewport 1440x900 (solo B e C)
export type Shot = {
  id: string; type: 'A' | 'B' | 'C' | 'D' | 'F'; frames: number;
  srcId?: string; from?: number;   // cartella sorgente e frame di partenza (per clip condivise)
  region?: { x: number; y: number; w?: number; h?: number };
  pushIn?: number;
};
export const SHOTS: Shot[] = [
  { id: 's01', type: 'A', frames: 60 },
  { id: 's02', type: 'C', frames: 60, region: { x: 182, y: 45, w: 580, h: 520 }, pushIn: 0.08 },
  { id: 's03', type: 'F', frames: 60 },
  { id: 's04', type: 'B', frames: 30, region: { x: 760, y: 0 }, pushIn: 0.05 },
  { id: 's05', type: 'D', frames: 60, from: 18 },
  { id: 's06', type: 'C', frames: 30, srcId: 's05', from: 96, region: { x: 150, y: 140, w: 580, h: 330 }, pushIn: 0.06 },
  { id: 's07', type: 'B', frames: 30, region: { x: 150, y: 0 }, pushIn: 0.05 },
  { id: 's08', type: 'C', frames: 30, region: { x: 170, y: 410, w: 500, h: 300 }, pushIn: 0.06 },
  { id: 's09', type: 'A', frames: 30 },
  { id: 's10', type: 'B', frames: 30, region: { x: 150, y: 0 }, pushIn: 0.05 },
  { id: 's11', type: 'F', frames: 30 },
  { id: 's12', type: 'A', frames: 30 },
  { id: 's13', type: 'C', frames: 30, region: { x: 660, y: 360, w: 580, h: 520 }, pushIn: 0.06 },
  { id: 's14', type: 'B', frames: 30, region: { x: 170, y: 0 }, pushIn: 0.05 },
];
export const MONTAGE_FRAMES = SHOTS.reduce((a, s) => a + s.frames, 0); // 540 = 9,0 s

// Mobile: 3 inquadrature (frame di partenza nella cattura mobile, durata)
export const MOBILE_SHOTS = [
  { from: 0, frames: 60 }, { from: 60, frames: 30 }, { from: 90, frames: 30 },
];
export const MOBILE_FRAMES = 120;
export const SIGN_FRAMES = 192;           // 3,2 s
export const TOTAL_FRAMES = HERO_FRAMES + MONTAGE_FRAMES + MOBILE_FRAMES + SIGN_FRAMES; // 1572 = 26,2 s
