import React from 'react';
import { Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { COLORS } from './config';

export const pad = (n: number) => String(Math.max(0, Math.floor(n))).padStart(4, '0');
export const frameSrc = (dir: string, i: number) => staticFile(`${dir}/${pad(i)}.jpg`);

export const FONT = "'Chivo', 'Inter Tight', system-ui, sans-serif";

export const easeInOutCubic = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

// ---------- Sfondo: nero + glow dai colori medi del frame corrente (niente filtri pesanti) ----------
import bgcolors from './bgcolors.json';
const COLS = bgcolors as Record<string, string[][]>;
const hex2rgb = (h: string) => [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
const tint = (h: string, g: number) => {
  const [r, gg, b] = hex2rgb(h);
  const l = (r + gg + b) / 3;
  const sat = 1.5;
  const [r2, g2, b2] = [r, gg, b].map((v) => Math.max(0, Math.min(255, l + (v - l) * sat)));
  const ink = [10, 11, 13];
  return [r2, g2, b2].map((v, i) => Math.round(ink[i] * (1 - g) + v * g * 0.8));
};
export const Background: React.FC<{ src?: string; glow?: number }> = ({ src, glow = 0.5 }) => {
  let stops = 'transparent, transparent';
  const m = src && src.match(/((?:hero|mobile|shots\/s\d+))\/(\d{4})\.jpg/);
  if (m) {
    const arr = COLS[m[1]];
    const fr = arr && arr[Math.min(parseInt(m[2], 10), arr.length - 1)];
    if (fr) stops = fr.map((c, i) => { const [r, g, b] = tint(c, glow); return `rgb(${r},${g},${b}) ${(i / 7) * 100}%`; }).join(', ');
  }
  return (
    <div style={{ position: 'absolute', inset: 0, background: COLORS.ink, overflow: 'hidden' }}>
      <div style={{ position: 'absolute', inset: 0, background: `linear-gradient(180deg, ${stops})` }} />
      <div style={{ position: 'absolute', inset: 0, background: 'radial-gradient(ellipse at 50% 48%, rgba(10,11,13,0) 0%, rgba(10,11,13,0.72) 100%)' }} />
      <Grain />
    </div>
  );
};

// grana finissima animata (2-3%)
export const Grain: React.FC = () => {
  const f = useCurrentFrame();
  const seed = Math.floor(f / 2) % 7;
  return (
    <svg style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', opacity: 0.05, mixBlendMode: 'overlay', pointerEvents: 'none' }}>
      <filter id={`n${seed}`}>
        <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed={seed} />
      </filter>
      <rect width="100%" height="100%" filter={`url(#n${seed})`} />
    </svg>
  );
};

// ---------- Mockup browser minimale ----------
export const BAR = 40;
export const Mockup: React.FC<{ width?: number; children: React.ReactNode; aspect?: number; style?: React.CSSProperties }> = ({
  width = 1000, aspect = 1440 / 900, children, style,
}) => (
  <div
    style={{
      width, borderRadius: 24, overflow: 'hidden', background: '#0f1013',
      boxShadow: '0 60px 120px -20px rgba(0,0,0,0.65), 0 12px 24px rgba(0,0,0,0.55), 0 0 0 1px rgba(255,255,255,0.06)',
      ...style,
    }}
  >
    <div style={{ height: BAR, background: '#17181c', display: 'flex', alignItems: 'center', gap: 10, paddingLeft: 20 }}>
      {['#3a3c43', '#3a3c43', '#3a3c43'].map((c, i) => <div key={i} style={{ width: 12, height: 12, borderRadius: 6, background: c }} />)}
    </div>
    <div style={{ width, height: width / aspect, position: 'relative', overflow: 'hidden' }}>{children}</div>
  </div>
);

// ---------- Testo: entrata parola per parola ----------
export const Words: React.FC<{
  text: string; start: number; end?: number; size: number; weight?: number; accent?: string; color?: string;
  stagger?: number; align?: 'center' | 'left'; tracking?: string; upper?: boolean; lead?: number;
}> = ({ text, start, end, size, weight = 700, accent, color = COLORS.text, stagger = 4, align = 'center', tracking = '-0.02em', upper, lead = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const words = text.split(' ');
  return (
    <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: align === 'center' ? 'center' : 'flex-start', gap: `0 ${size * 0.28}px`, fontFamily: FONT, fontSize: size, fontWeight: weight, letterSpacing: tracking, lineHeight: 1.08, textTransform: upper ? 'uppercase' : 'none' }}>
      {words.map((w, i) => {
        const s = start + i * stagger - lead;
        const inP = spring({ frame: frame - s, fps, config: { damping: 20, mass: 0.7 } });
        let o = inP, y = (1 - inP) * 20;
        if (end !== undefined) {
          const outP = interpolate(frame, [end - 8 + i * 1, end + i * 1], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          o *= 1 - outP; y -= outP * 14;
        }
        const clean = w.replace(/[,.]/g, '');
        return (
          <span key={i} style={{ opacity: o, transform: `translateY(${y}px)`, color: accent && clean === accent ? COLORS.accent : color, display: 'inline-block' }}>{w}</span>
        );
      })}
    </div>
  );
};

// ---------- Didascalia (pillola) ----------
export const Caption: React.FC<{ text: string; from: number; dur: number; y?: number }> = ({ text, from, dur, y = 1400 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inP = spring({ frame: frame - from, fps, config: { damping: 20, mass: 0.6 } });
  const outP = interpolate(frame, [from + dur - 8, from + dur], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const o = inP * (1 - outP);
  if (frame < from || frame > from + dur) return null;
  return (
    <div style={{ position: 'absolute', left: 0, right: 0, top: y, display: 'flex', justifyContent: 'center', opacity: o, transform: `translateY(${(1 - inP) * 20 - outP * 10}px)` }}>
      <div style={{ fontFamily: FONT, fontWeight: 600, fontSize: 40, letterSpacing: '-0.01em', color: COLORS.text, padding: '16px 34px', borderRadius: 999, background: 'rgba(10,11,13,0.72)', border: '1px solid rgba(255,255,255,0.1)', backdropFilter: 'blur(14px)' }}>
        {text}
      </div>
    </div>
  );
};
