import React from 'react';
import {AbsoluteFill, Easing, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {loadFont} from '@remotion/google-fonts/Manrope';
import {CAPTION_SPANS, COLORS, FINAL_FRAMES, HERO_FRAMES, MOBILE, SHOTS, TEXT, W, H, Shot} from './config';

const {fontFamily} = loadFont('normal', {weights: ['500', '600', '700', '800']});
const out = Easing.bezier(0.22, 1, 0.36, 1);
const clamp01 = (x: number) => Math.min(1, Math.max(0, x));
const prog = (f: number, a: number, len: number) => out(clamp01((f - a) / len));

const BODY = staticFile('body.mp4');
const MW = 1000;           // larghezza base mockup
const MH = MW * 9 / 16;    // 562.5
const BAR = 44;

/* ---------- elementi base ---------- */
const Mockup: React.FC<{children: React.ReactNode; scale?: number; x?: number; y?: number; rx?: number; rot?: number; opacity?: number}> =
  ({children, scale = 1, x = 0, y = 0, rx = 0, rot = 0, opacity = 1}) => (
  <div style={{position: 'absolute', left: (W - MW) / 2, top: 900 - (MH + BAR) / 2, width: MW, height: MH + BAR, opacity,
    transform: `perspective(1800px) translate(${x}px, ${y}px) rotateX(${rx}deg) rotateZ(${rot}deg) scale(${scale})`, transformOrigin: '50% 50%'}}>
    <div style={{width: MW, height: MH + BAR, borderRadius: 24, overflow: 'hidden', background: '#0d1424',
      boxShadow: '0 70px 140px rgba(0,0,0,.55), 0 16px 34px rgba(0,0,0,.65), 0 0 0 1px rgba(255,255,255,.12)'}}>
      <div style={{height: BAR, background: 'linear-gradient(#1b2336,#151c2d)', display: 'flex', alignItems: 'center', paddingLeft: 22, gap: 10}}>
        {[0, 1, 2].map((i) => <div key={i} style={{width: 14, height: 14, borderRadius: 7, background: 'rgba(255,255,255,.25)'}} />)}
      </div>
      <div style={{width: MW, height: MH, position: 'relative', overflow: 'hidden', background: '#fff'}}>{children}</div>
    </div>
  </div>
);

const Vid: React.FC<{src: string; start: number; rate?: number; w?: number; h?: number; left?: number; top?: number}> =
  ({src, start, rate = 1, w = MW, h = MH, left = 0, top = 0}) => (
  <OffthreadVideo src={src} startFrom={Math.round(start)} playbackRate={rate} muted
    style={{position: 'absolute', left, top, width: w, height: h, objectFit: 'cover'}} />
);

const Stage: React.FC = () => (
  <AbsoluteFill style={{background: `radial-gradient(900px 700px at 50% 42%, ${COLORS.glow}55, transparent 70%), radial-gradient(700px 500px at 80% 90%, ${COLORS.red}22, transparent 70%), ${COLORS.bg}`}} />
);

const Pill: React.FC<{text: string; f: number; dur: number}> = ({text, f, dur}) => {
  const a = Math.min(prog(f, 0, 8), 1 - clamp01((f - (dur - 6)) / 6));
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: 1330, display: 'flex', justifyContent: 'center', opacity: a, transform: `translateY(${(1 - a) * 24}px)`}}>
      <div style={{fontFamily, fontWeight: 700, fontSize: 38, letterSpacing: '-0.01em', color: COLORS.text, background: COLORS.pill,
        padding: '18px 38px', borderRadius: 60, border: '1px solid rgba(255,255,255,.16)', backdropFilter: 'blur(14px)'}}>{text}</div>
    </div>
  );
};

/* ---------- ATTO 1 ---------- */
const HeroBg: React.FC<{still: boolean}> = ({still}) => (
  <AbsoluteFill style={{overflow: 'hidden', background: COLORS.bg}}>
    <div style={{position: 'absolute', left: (W - 1440) / 2, top: (H - 810) / 2, width: 1440, height: 810, transform: 'scale(2.45)', filter: 'blur(34px) brightness(.62) saturate(1.35)'}}>
      {still ? <Img src={staticFile('hero0.jpg')} style={{width: 1440, height: 810}} /> : <OffthreadVideo src={staticFile('hero.mp4')} muted style={{width: 1440, height: 810}} />}
    </div>
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(7,13,24,.55) 0%, rgba(7,13,24,.15) 45%, rgba(7,13,24,.7) 100%)'}} />
  </AbsoluteFill>
);

const Hook: React.FC<{f: number}> = ({f}) => {
  let i = 0;
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: 330, textAlign: 'center', fontFamily, fontWeight: 700, fontSize: 72, letterSpacing: '-0.02em', lineHeight: 1.12, color: COLORS.text}}>
      {TEXT.hook.map((line, li) => (
        <div key={li}>
          {line.split(' ').map((wd) => {
            const p = prog(f, i * 2, 12); i++;
            return <span key={i} style={{display: 'inline-block', marginRight: 18, opacity: 0.8 + 0.2 * p, transform: `translateY(${16 * (1 - p)}px)`,
              color: wd === TEXT.hookAccent ? COLORS.accent : COLORS.text}}>{wd}</span>;
          })}
        </div>
      ))}
    </div>
  );
};

const HeroStage: React.FC<{still?: boolean; showText: boolean}> = ({still = false, showText}) => {
  const cur = useCurrentFrame();
  const f = still ? 0 : cur;
  const scale = interpolate(f, [0, HERO_FRAMES], [0.96, 1.0]);
  const rx = interpolate(out(clamp01(f / 45)), [0, 1], [6, 0]);
  const fy = Math.sin((f / HERO_FRAMES) * Math.PI * 2) * 6;
  return (
    <AbsoluteFill>
      <HeroBg still={still} />
      {showText && <Hook f={f} />}
      <Mockup scale={scale} rx={rx} y={fy}>
        {still ? <Img src={staticFile('hero0.jpg')} style={{width: MW, height: MH}} /> : <Vid src={staticFile('hero.mp4')} start={0} />}
      </Mockup>
      {showText && (
        <div style={{position: 'absolute', left: 0, right: 0, top: 1275, textAlign: 'center', fontFamily, fontWeight: 600, fontSize: 24, letterSpacing: '0.12em', textTransform: 'uppercase', color: 'rgba(255,255,255,.72)'}}>
          {TEXT.client}
        </div>
      )}
    </AbsoluteFill>
  );
};

/* ---------- ATTO 2 ---------- */
const ShotView: React.FC<{s: Shot; idx: number}> = ({s, idx}) => {
  const f = useCurrentFrame();
  if (s.type === 'F') {
    const z = 1 + 0.95 * (1 - prog(f, 0, 12));      // zoom-through d'ingresso ("drop")
    const a = 15;
    return (
      <Mockup scale={z}>
        <Sequence from={0} durationInFrames={a}><Vid src={BODY} start={s.from} rate={(s.mid - s.from) / a} /></Sequence>
        <Sequence from={a} durationInFrames={s.dur - a}><Vid src={BODY} start={s.mid} rate={(s.to - s.mid) / (s.dur - a)} /></Sequence>
      </Mockup>
    );
  }
  if (s.type === 'B') {
    const k = H / 1620, push = 1 + 0.05 * (f / s.dur);
    return (
      <AbsoluteFill style={{overflow: 'hidden', background: '#fff'}}>
        <div style={{position: 'absolute', inset: 0, transform: `scale(${push})`, transformOrigin: '50% 50%'}}>
          <Img src={staticFile(`stills/${s.still}.jpg`)} style={{position: 'absolute', width: 2880 * k, height: 1620 * k, left: -s.x0 * k, top: 0}} />
        </div>
      </AbsoluteFill>
    );
  }
  if (s.type === 'C') {
    const k = 980 / 864, push = 1 + 0.04 * (f / s.dur), enter = prog(f, 0, 6);
    return (
      <div style={{position: 'absolute', left: 50, top: 780 - 490, width: 980, height: 980, borderRadius: 34, overflow: 'hidden', background: '#fff',
        transform: `scale(${0.96 + 0.04 * enter})`, boxShadow: '0 60px 120px rgba(0,0,0,.55), 0 14px 30px rgba(0,0,0,.6), 0 0 0 1px rgba(255,255,255,.12)'}}>
        <div style={{position: 'absolute', inset: 0, transform: `scale(${push})`}}>
          <Img src={staticFile(`stills/${s.still}.jpg`)} style={{position: 'absolute', width: 2880 * k, height: 1620 * k, left: -s.x0 * k, top: -s.y0 * k}} />
        </div>
      </div>
    );
  }
  if (s.type === 'A') {
    return <Mockup scale={0.98 + 0.02 * (f / s.dur)}><Vid src={BODY} start={s.src} /></Mockup>;
  }
  if (s.type === 'D') {
    return <Mockup><Vid src={staticFile('esami.mp4')} start={s.srcSec * 30} /></Mockup>;
  }
  // E: stack/cascata
  const e0 = prog(f, 0, 10), e1 = prog(f, 8, 10);
  return (
    <>
      <Mockup scale={0.86} y={-250 + (1 - e0) * 520} opacity={e0}><Vid src={BODY} start={s.srcs[0]} /></Mockup>
      <Mockup scale={0.86} x={24} y={120 + (1 - e1) * 620} opacity={e1}><Vid src={BODY} start={s.srcs[1]} /></Mockup>
    </>
  );
};

const MobileScene: React.FC = () => {
  const f = useCurrentFrame();
  const sc = 0.92 + 0.08 * prog(f, 0, 10);
  return (
    <div style={{position: 'absolute', left: (W - 500) / 2, top: 900 - 530, width: 500, height: 1060, transform: `scale(${sc})`}}>
      <div style={{width: 500, height: 1060, borderRadius: 66, background: '#0a0f1a', boxShadow: '0 70px 140px rgba(0,0,0,.55), 0 0 0 2px rgba(255,255,255,.22), inset 0 0 0 8px #141b2b', position: 'relative'}}>
        <div style={{position: 'absolute', left: 16, top: 16, width: 468, height: 1028, borderRadius: 52, overflow: 'hidden', background: '#fff'}}>
          {MOBILE.clips.map((c, i) => (
            <Sequence key={i} from={i * 20} durationInFrames={20}>
              <Vid src={staticFile('mobile.mp4')} start={c} w={468} h={1028} />
            </Sequence>
          ))}
        </div>
      </div>
    </div>
  );
};

/* ---------- FINALE ---------- */
const FinalScene: React.FC<{showText: boolean}> = ({showText}) => {
  const f = useCurrentFrame();
  const m = prog(f, 0, 22);
  const cross = clamp01((f - 62) / 20);
  const t = (a: number) => prog(f, a, 12);
  return (
    <AbsoluteFill>
      <Stage />
      <div style={{opacity: 1 - cross}}>
        <Mockup scale={1 - 0.38 * m} y={-200 * m}>
          <Img src={staticFile('hero0.jpg')} style={{width: MW, height: MH}} />
        </Mockup>
        {showText && (
          <div style={{position: 'absolute', left: 0, right: 0, top: 1000, textAlign: 'center', fontFamily, color: COLORS.text}}>
            <div style={{fontWeight: 700, fontSize: 46, letterSpacing: '-0.01em', opacity: t(16), transform: `translateY(${(1 - t(16)) * 20}px)`}}>{TEXT.signature}</div>
            <div style={{fontWeight: 600, fontSize: 36, marginTop: 14, color: COLORS.accent, opacity: t(22), transform: `translateY(${(1 - t(22)) * 20}px)`}}>{TEXT.handle}</div>
            <div style={{display: 'inline-block', marginTop: 44, fontWeight: 700, fontSize: 38, padding: '22px 44px', borderRadius: 70, background: COLORS.red,
              opacity: t(30), transform: `translateY(${(1 - t(30)) * 20}px)`}}>{TEXT.cta}</div>
          </div>
        )}
      </div>
      <div style={{opacity: cross}}><HeroStage still showText={showText} /></div>
    </AbsoluteFill>
  );
};

/* ---------- MAIN ---------- */
export const Main: React.FC<{showText: boolean}> = ({showText}) => {
  let t = HERO_FRAMES;
  const shotEls = SHOTS.map((s, i) => {
    const el = <Sequence key={i} from={t} durationInFrames={s.dur}><ShotView s={s} idx={i} /></Sequence>;
    t += s.dur;
    return el;
  });
  const montEnd = t;
  const mobileFrom = t;
  const finalFrom = t + MOBILE.dur;
  return (
    <AbsoluteFill style={{background: COLORS.bg}}>
      <Sequence from={0} durationInFrames={HERO_FRAMES}><HeroStage showText={showText} /></Sequence>
      <Sequence from={HERO_FRAMES} durationInFrames={montEnd - HERO_FRAMES + MOBILE.dur}><Stage /></Sequence>
      {shotEls}
      <Sequence from={mobileFrom} durationInFrames={MOBILE.dur}><MobileScene /></Sequence>
      {showText && CAPTION_SPANS.map(([ti, a, b]) => (
        <Sequence key={ti} from={HERO_FRAMES + a} durationInFrames={b - a}>
          <CapInner text={TEXT.captions[ti]} dur={b - a} />
        </Sequence>
      ))}
      <Sequence from={finalFrom} durationInFrames={FINAL_FRAMES}><FinalScene showText={showText} /></Sequence>
    </AbsoluteFill>
  );
};

const CapInner: React.FC<{text: string; dur: number}> = ({text, dur}) => <Pill text={text} f={useCurrentFrame()} dur={dur} />;
