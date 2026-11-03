// ============================================================
//  CONFIG — modifica qui testi, colori, durate e timecode.
//  Tutti i tempi sono in SECONDI (griglia ritmica: 120 BPM = 0,5 s).
// ============================================================
export const CONFIG = {
  width: 1080,
  height: 1920,
  fps: 60,
  showText: true, // false => versione "clean" senza testi

  cliente: 'Tecnomarmi',
  settore: 'laboratorio di marmo, pietra e granito (Altivole, TV)',

  colors: {
    bg: '#0B0B0C',
    ink: '#101214', // colori letti dal sito reale
    graphite: '#2C3036',
    stone: '#EAEBEB',
    accent: '#C8D2DA', // marmo freddo, una sola parola accentata per scritta
  },

  // Le parole tra *asterischi* usano il colore accento
  hook: ['Un sito scolpito', 'come il *marmo*'],
  hookAlternatives: ['Dal blocco di marmo al sito web', 'Il sito di un laboratorio di marmo'],

  captions: [
    { text: 'Lavorazioni su *misura*', from: 15.25, to: 18.0 },
    { text: 'Scegli la *materia*', from: 20.0, to: 22.5 },
    { text: 'Ogni dettaglio, *curato*', from: 23.0, to: 25.5 },
  ],

  firma: 'Web design · Giovanni Bertoni',
  handle: '@giovannibertoni',
  cta: 'Vuoi un sito così? *Scrivimi*',

  // ---- Tempi -------------------------------------------------
  heroSeconds: 15.0, // ciclo hero completo (14,58 s di video) + 0,42 s di tenuta finale
  heroExitStart: 14.75, // il mockup lascia la scena solo dopo la fine del ciclo
  mobileStart: 25.5,
  firmaStart: 27.5,
  total: 30.5,
  loopTail: 0.4, // ultimi secondi: ritorno al frame 0 per il loop
};

export type ShotKind = 'A' | 'B' | 'C' | 'D' | 'E' | 'F';
// start = secondo di inizio, dur = durata. Nessuna inquadratura > 1,5 s.
export const SHOTS: {id: string; kind: ShotKind; start: number; dur: number}[] = [
  {id: 's1', kind: 'A', start: 15.0, dur: 1.0}, // Lavorazioni — sezione nel mockup
  {id: 's2', kind: 'B', start: 16.0, dur: 1.0}, // crop 9:16 card Bagni → Cucine
  {id: 's3', kind: 'C', start: 17.0, dur: 1.0}, // close-up card Contract
  {id: 's4', kind: 'E', start: 18.0, dur: 1.0}, // cascata 3 sezioni
  {id: 's5', kind: 'F', start: 19.0, dur: 1.0}, // speed ramp scroll
  {id: 's6', kind: 'A', start: 20.0, dur: 1.0}, // Materioteca nel mockup
  {id: 's7', kind: 'D', start: 21.0, dur: 1.0}, // click reale sul filtro Granito
  {id: 's8', kind: 'C', start: 22.0, dur: 0.5}, // close-up texture granito
  {id: 's9', kind: 'B', start: 22.5, dur: 0.5}, // crop scheda materiale
  {id: 's10', kind: 'A', start: 23.0, dur: 0.5}, // Metodo nel mockup
  {id: 's11', kind: 'C', start: 23.5, dur: 0.5}, // close-up passi
  {id: 's12', kind: 'B', start: 24.0, dur: 0.5}, // crop sezione metodo + pilastri
  {id: 's13', kind: 'A', start: 24.5, dur: 0.5}, // Contatti nel mockup
  {id: 's14', kind: 'C', start: 25.0, dur: 0.5}, // close-up CTA form
];
