import React from 'react';
import { AbsoluteFill, Img, Sequence, interpolate, spring, useCurrentFrame, useVideoConfig, Easing } from 'remotion';
import { loadFont } from '@remotion/google-fonts/Chivo';
import {
  COLORS, TEXT, HERO_FRAMES, HERO_CAPTURED, SHOTS, Shot, MOBILE_SHOTS, MOBILE_FRAMES, SIGN_FRAMES, MONTAGE_FRAMES,
} from './config';
import { Background, Mockup, Words, Caption, frameSrc, FONT, BAR } from './ui';

loadFont('normal', { weights: ['400', '600', '700'], subsets: ['latin'] });

const clamp = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' } as const;
const outCubic = Easing.out(Easing.cubic);

const MOCK_W = 1000;
const MOCK_H = BAR + MOCK_W / (1440 / 900); // 665
const MOCK_CY = 990;

// ============ ATTO 1 — HERO INTEGRALE ============
const HeroAct: React.FC<{ showText: boolean }> = ({ showText }) => {
  const f = useCurrentFrame();
  const idx = Math.min(f, HERO_CAPTURED - 1);
  const src = frameSrc('hero', idx);
  const tilt = 0; // tilt 3D disattivato: instabile nel rendering software di Chromium
  let scale = interpolate(f, [0, HERO_FRAMES - 24], [0.96, 1.0], clamp);
  const floatY = Math.sin((f / 60) * ((Math.PI * 2) / 6)) * 6;
  // zoom-through finale (dopo la fine del ciclo, sul beat)
  const zt = interpolate(f, [HERO_FRAMES - 22, HERO_FRAMES], [0, 1], { ...clamp, easing: Easing.in(Easing.cubic) });
  scale *= 1 + zt * 3.2;
  const stageOpacity = 1 - interpolate(zt, [0.7, 1], [0, 1], clamp);
  return (
    <AbsoluteFill>
      <Background src={src} glow={0.42} />
      <AbsoluteFill style={{ opacity: stageOpacity, filter: `blur(${zt * 12}px)` }}>
        <div style={{ position: 'absolute', left: 40, top: MOCK_CY - MOCK_H / 2 + floatY,  }}>
          <Mockup width={MOCK_W} style={{ transform: `scale(${scale})`, transformOrigin: '50% 50%' }}>
            <Img src={src} style={{ width: '100%', height: '100%', display: 'block' }} />
          </Mockup>
        </div>
      </AbsoluteFill>
      {showText && (
        <AbsoluteFill style={{ opacity: 1 - zt }}>
          <div style={{ position: 'absolute', left: 70, width: 940, top: 330, display: 'flex', flexDirection: 'column', gap: 6, alignItems: 'center' }}>
            <Words text={TEXT.hook[0]} start={0} lead={40} size={76} end={HERO_FRAMES - 30} accent={TEXT.hookAccentWord} />
            <Words text={TEXT.hook[1]} start={16} lead={8} size={76} end={HERO_FRAMES - 30} accent={TEXT.hookAccentWord} />
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};

// ============ ATTO 2 — MONTAGGIO ============
const ShotView: React.FC<{ shot: Shot }> = ({ shot }) => {
  const f = useCurrentFrame();
  const dir = `shots/${shot.srcId ?? shot.id}`;
  const src = frameSrc(dir, (shot.from ?? 0) + f);
  const u = f / shot.frames;
  const push = (shot.pushIn ?? 0.03) * u;

  if (shot.type === 'B') {
    const r = shot.region!;
    const s = 1080 / 1012;
    return (
      <AbsoluteFill style={{ background: COLORS.ink, overflow: 'hidden' }}>
        <div style={{ position: 'absolute', inset: 0, transform: `scale(${1 + push})`, transformOrigin: '50% 50%' }}>
          <Img src={src} style={{ position: 'absolute', left: -r.x * 2 * s, top: -r.y * 2 * s, width: 2880 * s, height: 1800 * s }} />
        </div>
      </AbsoluteFill>
    );
  }
  if (shot.type === 'C') {
    const r = shot.region!;
    const w = r.w ?? 500, h = r.h ?? 550;
    const s = 1000 / (w * 2);
    return (
      <AbsoluteFill>
        <Background src={src} glow={0.4} />
        <div style={{ position: 'absolute', left: 40, top: 900 - (h * 2 * s) / 2, width: 1000, height: h * 2 * s, borderRadius: 28, overflow: 'hidden', boxShadow: '0 60px 120px -20px rgba(0,0,0,0.65), 0 12px 24px rgba(0,0,0,0.55), 0 0 0 1px rgba(255,255,255,0.07)' }}>
          <div style={{ position: 'absolute', inset: 0, transform: `scale(${1 + push})`, transformOrigin: '50% 50%' }}>
            <Img src={src} style={{ position: 'absolute', left: -r.x * 2 * s, top: -r.y * 2 * s, width: 2880 * s, height: 1800 * s }} />
          </div>
        </div>
      </AbsoluteFill>
    );
  }
  // A, D, F: sezione/interazione dentro il mockup
  const blur = shot.type === 'F' ? interpolate(f, [0, 18], [7, 0], { ...clamp, easing: outCubic }) : 0;
  return (
    <AbsoluteFill>
      <Background src={src} glow={0.45} />
      <div style={{ position: 'absolute', left: 40, top: 900 - MOCK_H / 2, transform: `scale(${1 + push})`, transformOrigin: '50% 50%' }}>
        <Mockup width={MOCK_W}>
          <Img src={src} style={{ width: '100%', height: '100%', display: 'block', filter: blur ? `blur(${blur}px)` : undefined }} />
        </Mockup>
      </div>
    </AbsoluteFill>
  );
};

const Montage: React.FC = () => {
  let at = 0;
  return (
    <AbsoluteFill>
      {SHOTS.map((s) => {
        const from = at; at += s.frames;
        return (
          <Sequence key={s.id} from={from} durationInFrames={s.frames}>
            <ShotView shot={s} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

// ============ MOBILE ============
const PHONE_W = 440, PHONE_H = (PHONE_W * 844) / 390; // 952
const Mobile: React.FC = () => {
  const f = useCurrentFrame();
  let at = 0, seg = MOBILE_SHOTS[0], local = f;
  for (const m of MOBILE_SHOTS) { if (f >= at && f < at + m.frames) { seg = m; local = f - at; } at += m.frames; }
  const src = frameSrc('mobile', seg.from + local);
  return (
    <AbsoluteFill>
      <Background src={src} glow={0.5} />
      <div style={{ position: 'absolute', left: 540 - (PHONE_W + 28) / 2, top: 895 - (PHONE_H + 28) / 2, width: PHONE_W + 28, height: PHONE_H + 28, borderRadius: 64, background: '#15161a', padding: 14, boxShadow: '0 60px 120px -20px rgba(0,0,0,0.7), 0 12px 24px rgba(0,0,0,0.55), 0 0 0 1.5px rgba(255,255,255,0.12)' }}>
        <div style={{ width: PHONE_W, height: PHONE_H, borderRadius: 50, overflow: 'hidden', position: 'relative' }}>
          <Img src={src} style={{ width: '100%', height: '100%', display: 'block' }} />
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ============ FIRMA + CTA (raccordo col frame 0) ============
const Signature: React.FC<{ showText: boolean }> = ({ showText }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const src = frameSrc('hero', 0);
  const shrink = spring({ frame: f, fps, config: { damping: 20, mass: 0.9 } });
  const back = interpolate(f, [SIGN_FRAMES - 30, SIGN_FRAMES - 1], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const sc = interpolate(shrink, [0, 1], [1, 0.6]) * (1 - back) + 0.96 * back;
  const cy = interpolate(shrink, [0, 1], [MOCK_CY, 560]) * (1 - back) + MOCK_CY * back;
  const tilt = 0;
  const textOut = interpolate(f, [SIGN_FRAMES - 48, SIGN_FRAMES - 34], [0, 1], clamp);
  return (
    <AbsoluteFill>
      <Background src={src} glow={0.42} />
      <div style={{ position: 'absolute', left: 40, top: cy - MOCK_H / 2,  }}>
        <Mockup width={MOCK_W} style={{ transform: `scale(${sc})`, transformOrigin: '50% 50%' }}>
          <Img src={src} style={{ width: '100%', height: '100%', display: 'block' }} />
        </Mockup>
      </div>
      {showText && (
        <AbsoluteFill style={{ opacity: 1 - textOut }}>
          <div style={{ position: 'absolute', left: 70, width: 940, top: 880, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4 }}>
            <Words text={TEXT.cta[0]} start={14} size={72} />
            <Words text={TEXT.cta[1]} start={24} size={72} accent={TEXT.cta[1]} />
          </div>
          <div style={{ position: 'absolute', left: 70, width: 940, top: 1170, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 14 }}>
            <Words text={TEXT.signature} start={42} size={36} weight={600} color={COLORS.textDim} tracking="0.01em" />
            <Words text={TEXT.handle} start={54} size={36} weight={600} color={COLORS.accent} tracking="0.01em" />
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};

export const Main: React.FC<{ showText: boolean }> = ({ showText }) => {
  const t1 = HERO_FRAMES;
  const t2 = t1 + MONTAGE_FRAMES;
  const t3 = t2 + MOBILE_FRAMES;
  return (
    <AbsoluteFill style={{ background: COLORS.ink, fontFamily: FONT }}>
      <Sequence from={0} durationInFrames={HERO_FRAMES}><HeroAct showText={showText} /></Sequence>
      <Sequence from={t1} durationInFrames={MONTAGE_FRAMES}>
        <Montage />
        {showText && (
          <>
            <Caption text={TEXT.caption1} from={20} dur={84} />
            <Caption text={TEXT.caption2} from={195} dur={84} />
          </>
        )}
      </Sequence>
      <Sequence from={t2} durationInFrames={MOBILE_FRAMES}>
        <Mobile />
        {showText && <Caption text={TEXT.captionMobile} from={14} dur={84} y={1400} />}
      </Sequence>
      <Sequence from={t3} durationInFrames={SIGN_FRAMES}><Signature showText={showText} /></Sequence>
    </AbsoluteFill>
  );
};
