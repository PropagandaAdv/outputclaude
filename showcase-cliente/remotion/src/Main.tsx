import React from 'react';
import {AbsoluteFill, Easing, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {CameraMotionBlur} from '@remotion/motion-blur';
import {JOSEFIN_B64} from './fontData';
import {CONFIG, SHOTS} from './config';

// Font del sito (Josefin Sans, variabile) incorporato in base64: nessun fetch di rete in render
const fontFamily = 'JosefinLocal, "Josefin Sans", sans-serif';
const FontStyle: React.FC = () => (
  <style>{`@font-face{font-family:'JosefinLocal';src:url(data:font/woff2;base64,${JOSEFIN_B64}) format('woff2');font-weight:100 700;font-display:block;}`}</style>
);
const C = CONFIG.colors;
const FPS = CONFIG.fps;
const F = (s: number) => Math.round(s * FPS);
const easeInOut = Easing.bezier(0.65, 0, 0.35, 1);
const easeOut = Easing.out(Easing.cubic);
const prog = (f: number, a: number, b: number, e?: (t: number) => number) =>
  interpolate(f, [a, b], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: e});

// ---------- dimensioni mockup (viewport 1440x900 css -> 1000x625 px) ----------
const VW = 1000, VH = 625, BAR = 46, S = VW / 1440;
const STRIP_H: Record<string, number> = {lav: 2087, mat: 1062, met: 1245, con: 1177, mat_granito: 1062};
const HERO_LAST = 899;
const heroSrc = (i: number) => staticFile(`hero/h_${String(Math.max(0, Math.min(HERO_LAST, Math.round(i)))).padStart(4, '0')}.jpg`);

// ---------- sfondo ----------
const BG: React.FC<{heroIdx: number}> = ({heroIdx}) => (
  <AbsoluteFill style={{background: C.bg}}>
    <Img src={heroSrc(heroIdx)} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover',
      filter: 'blur(90px) saturate(1.15)', opacity: 0.42, transform: 'scale(1.35)'}} />
    <AbsoluteFill style={{background: 'radial-gradient(ellipse 90% 60% at 50% 48%, rgba(11,11,12,0) 0%, rgba(11,11,12,.75) 100%)'}} />
  </AbsoluteFill>
);

// ---------- testo ----------
type Tok = {w: string; accent: boolean; br?: boolean};
const tokenize = (text: string): Tok[] => text.split(' ').map((w) => {
  const accent = w.startsWith('*');
  return {w: w.replace(/\*/g, ''), accent};
});
const Words: React.FC<{text: string; size: number; weight?: number; start?: number; stagger?: number; firstVisible?: boolean; exitAt?: number; letter?: string}> =
({text, size, weight = 600, start = 0, stagger = 4, firstVisible = false, exitAt, letter = '-0.02em'}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const toks = tokenize(text);
  const exit = exitAt === undefined ? 0 : prog(f, exitAt, exitAt + 8);
  return (
    <div style={{fontFamily, fontSize: size, fontWeight: weight, letterSpacing: letter, color: C.stone, lineHeight: 1.04, textAlign: 'center',
      textShadow: '0 2px 30px rgba(0,0,0,.55)'}}>
      {toks.map((t, i) => {
        const p = firstVisible && i === 0 ? 1 : spring({frame: f - start - i * stagger, fps, config: {damping: 20, stiffness: 140}});
        return (
          <span key={i} style={{display: 'inline-block', marginRight: '0.28em', opacity: p * (1 - exit), color: t.accent ? C.accent : C.stone,
            transform: `translateY(${(1 - p) * 20 + exit * 10}px)`}}>{t.w}</span>
        );
      })}
    </div>
  );
};

// ---------- mockup browser ----------
const Mockup: React.FC<{children: React.ReactNode; cy: number; scale?: number; rotX?: number; x?: number; y?: number; opacity?: number}> =
({children, cy, scale = 1, rotX = 0, x = 0, y = 0, opacity = 1}) => (
  <div style={{position: 'absolute', inset: 0, perspective: 2600, opacity}}>
    <div style={{position: 'absolute', left: (1080 - VW) / 2, top: cy - (VH + BAR) / 2, width: VW, height: VH + BAR,
      transform: `translate3d(${x}px,${y}px,0) rotateX(${rotX}deg) scale(${scale})`, transformOrigin: '50% 50%',
      borderRadius: 24, overflow: 'hidden', background: '#14161a', border: '1px solid rgba(255,255,255,.09)',
      boxShadow: '0 70px 140px -30px rgba(0,0,0,.7), 0 14px 28px rgba(0,0,0,.55)'}}>
      <div style={{height: BAR, background: '#1a1d21', display: 'flex', alignItems: 'center', gap: 10, paddingLeft: 22}}>
        {[0, 1, 2].map((i) => <div key={i} style={{width: 13, height: 13, borderRadius: 13, background: '#3a3f46'}} />)}
      </div>
      <div style={{position: 'relative', width: VW, height: VH, overflow: 'hidden', background: C.ink}}>{children}</div>
    </div>
  </div>
);

const StripView: React.FC<{name: string; scroll: number; header?: boolean; w?: number}> = ({name, scroll, header = true, w = VW}) => {
  const s = w / 1440;
  return (
    <>
      <Img src={staticFile(`strips/${name}.jpg`)} style={{position: 'absolute', left: 0, top: 0, width: w, transform: `translate3d(0,${-scroll * s}px,0)`}} />
      {header && <Img src={staticFile('strips/header.jpg')} style={{position: 'absolute', left: 0, top: 0, width: w}} />}
    </>
  );
};

// ---------- ATTO 1: hero integrale ----------
const HeroMockup: React.FC<{f: number}> = ({f}) => {
  const idx = Math.min(f, HERO_LAST);
  const rotX = 6 * (1 - prog(f, 0, 90, easeOut));
  const scale = 0.96 + 0.04 * prog(f, 0, F(CONFIG.heroSeconds));
  const floatY = Math.sin((f / (FPS * 8)) * Math.PI * 2) * 6;
  const ex = prog(f, F(CONFIG.heroExitStart), F(CONFIG.heroExitStart) + 12, Easing.in(Easing.cubic));
  return (
    <Mockup cy={940} scale={scale} rotX={rotX} y={floatY + ex * 2300}>
      <Img src={heroSrc(idx)} style={{position: 'absolute', left: 0, top: 0, width: VW, height: VH}} />
    </Mockup>
  );
};

const Hook: React.FC<{show: boolean}> = ({show}) => {
  if (!show) return null;
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: 285, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6}}>
      {CONFIG.hook.map((line, li) => (
        <Words key={li} text={line} size={90} weight={700} start={li * 12} stagger={5} firstVisible={li === 0} exitAt={F(14.45)} />
      ))}
    </div>
  );
};

// ---------- ATTO 2: inquadrature ----------
const ShotA: React.FC<{strip: string; from: number; to: number; frames: number; fOffset?: number; enter?: boolean}> = ({strip, from, to, frames, fOffset = 0, enter}) => {
  const f = useCurrentFrame() + fOffset;
  const sc = interpolate(prog(f, 0, frames), [0, 1], [from, to]);
  const e = prog(f, 0, frames, easeInOut);
  const scroll = from + (to - from) * e;
  void sc;
  const enterP = enter ? spring({frame: f, fps: FPS, config: {damping: 18, stiffness: 220}}) : 1;
  return (
    <Mockup cy={940} scale={0.985 + 0.015 * prog(f, 0, frames)} y={(1 - enterP) * -2000}>
      <StripView name={strip} scroll={scroll} />
    </Mockup>
  );
};

const FullBleed: React.FC<{strip: string; frames: number; a: {cx: number; cy: number; W: number}; b: {cx: number; cy: number; W: number}}> = ({strip, frames, a, b}) => {
  const f = useCurrentFrame();
  const p = prog(f, 0, frames, easeInOut);
  const L = (x: number, y: number) => x + (y - x) * p;
  const W = L(a.W, b.W);
  const H = (W * 16) / 9;
  const z = 1080 / W;
  const imgH = STRIP_H[strip];
  const cx = Math.max(W / 2, Math.min(1440 - W / 2, L(a.cx, b.cx)));
  const cy = Math.max(H / 2, Math.min(imgH - H / 2, L(a.cy, b.cy)));
  return (
    <AbsoluteFill style={{background: C.ink, overflow: 'hidden'}}>
      <Img src={staticFile(`strips/${strip}.jpg`)} style={{position: 'absolute', left: 0, top: 0, width: 1440 * z, transformOrigin: '0 0',
        transform: `translate3d(${540 - cx * z}px,${960 - cy * z}px,0)`}} />
    </AbsoluteFill>
  );
};

const ShotD: React.FC = () => {
  const f = useCurrentFrame();
  const LEAD = 15;
  const src = f < LEAD ? 'tab/before.jpg' : `tab/t_${String(Math.min(74, f - LEAD)).padStart(3, '0')}.jpg`;
  const cp = prog(f, 0, LEAD - 2, easeInOut);
  const cx = 1290 + (1111 - 1290) * cp, cy = 620 + (404 - 620) * cp;
  const ripple = prog(f, LEAD - 2, LEAD + 14);
  return (
    <>
      <Mockup cy={940}>
        <Img src={staticFile(src)} style={{position: 'absolute', left: 0, top: 0, width: VW, height: VH}} />
        {ripple > 0 && ripple < 1 && (
          <div style={{position: 'absolute', left: 1111 * S - 40 * ripple - 6, top: 404 * S - 40 * ripple - 6, width: 80 * ripple + 12, height: 80 * ripple + 12,
            borderRadius: 999, border: '3px solid rgba(255,255,255,.8)', opacity: 1 - ripple}} />
        )}
        <svg width="34" height="34" viewBox="0 0 24 24" style={{position: 'absolute', left: cx * S - 3, top: cy * S - 2, filter: 'drop-shadow(0 3px 6px rgba(0,0,0,.6))',
          transform: `scale(${1 - 0.15 * (ripple > 0 && ripple < 0.3 ? 1 : 0)})`}}>
          <path d="M5 2 L5 19 L9.5 15 L12.5 21.5 L15 20.4 L12 14 L18 14 Z" fill="#fff" stroke="#111" strokeWidth="1.3" strokeLinejoin="round" />
        </svg>
      </Mockup>
    </>
  );
};

const ShotE: React.FC = () => {
  const f = useCurrentFrame();
  const panels = [{n: 'lav', s: 0, y: 470}, {n: 'mat', s: 40, y: 790}, {n: 'met', s: 0, y: 1110}];
  const drift = -60 * prog(f, 0, 60);
  return (
    <>
      {panels.map((p, i) => {
        const e = spring({frame: f - i * 9, fps: FPS, config: {damping: 19, stiffness: 120}});
        return (
          <div key={p.n} style={{position: 'absolute', left: 40, top: p.y - VH / 2 + drift + (1 - e) * 1300, width: VW, height: VH, borderRadius: 22, overflow: 'hidden',
            background: C.ink, border: '1px solid rgba(255,255,255,.1)', boxShadow: '0 -20px 60px rgba(0,0,0,.55), 0 30px 70px rgba(0,0,0,.6)'}}>
            <StripView name={p.n} scroll={p.s} header={false} />
          </div>
        );
      })}
    </>
  );
};

const ShotF: React.FC = () => {
  const f = useCurrentFrame();
  const p = prog(f, 0, 60);
  const e = 1 - Math.pow(1 - p, 3.5);
  const scroll = 120 + (1187 - 120) * e;
  const speed = Math.pow(1 - p, 2.5);
  return (
    <Mockup cy={940}>
      <div style={{position: 'absolute', inset: 0, filter: `blur(${speed * 3.5}px)`}}><StripView name="lav" scroll={scroll} /></div>
    </Mockup>
  );
};

const Shot: React.FC<{id: string; frames: number}> = ({id, frames}) => {
  switch (id) {
    case 's1': return <ShotA strip="lav" from={0} to={260} frames={frames} fOffset={F(0.45)} />;
    case 's2': return <FullBleed strip="lav" frames={frames} a={{cx: 470, cy: 690, W: 720}} b={{cx: 1010, cy: 690, W: 640}} />;
    case 's3': return <FullBleed strip="lav" frames={frames} a={{cx: 1000, cy: 1090, W: 480}} b={{cx: 1010, cy: 1070, W: 400}} />;
    case 's4': return <ShotE />;
    case 's5': return <ShotF />;
    case 's6': return <ShotA strip="mat" from={0} to={150} frames={frames} />;
    case 's7': return <ShotD />;
    case 's8': return <FullBleed strip="mat_granito" frames={frames} a={{cx: 430, cy: 640, W: 470}} b={{cx: 440, cy: 630, W: 380}} />;
    case 's9': return <FullBleed strip="mat_granito" frames={frames} a={{cx: 1115, cy: 531, W: 590}} b={{cx: 1115, cy: 531, W: 540}} />;
    case 's10': return <ShotA strip="met" from={0} to={330} frames={frames} />;
    case 's11': return <FullBleed strip="met" frames={frames} a={{cx: 1045, cy: 470, W: 640}} b={{cx: 1055, cy: 450, W: 580}} />;
    case 's12': return <FullBleed strip="met" frames={frames} a={{cx: 1014, cy: 622, W: 700}} b={{cx: 1014, cy: 622, W: 660}} />;
    case 's13': return <ShotA strip="con" from={0} to={270} frames={frames} />;
    case 's14': return <FullBleed strip="con" frames={frames} a={{cx: 770, cy: 700, W: 420}} b={{cx: 760, cy: 700, W: 340}} />;
    default: return null;
  }
};

// ---------- mobile ----------
const PW = 520, PH = 1125, BEZ = 14;
const Phone: React.FC<{children: React.ReactNode; x: number}> = ({children, x}) => (
  <div style={{position: 'absolute', left: (1080 - PW) / 2 - BEZ + x, top: 930 - PH / 2 - BEZ, width: PW + BEZ * 2, height: PH + BEZ * 2, borderRadius: 70,
    background: '#0a0a0b', border: '2px solid #2a2d32', boxShadow: '0 70px 140px -30px rgba(0,0,0,.75), 0 14px 28px rgba(0,0,0,.55)'}}>
    <div style={{position: 'absolute', left: BEZ, top: BEZ, width: PW, height: PH, borderRadius: 58, overflow: 'hidden', background: C.ink}}>{children}</div>
    <div style={{position: 'absolute', left: '50%', top: BEZ + 14, width: 110, height: 28, marginLeft: -55, borderRadius: 20, background: '#000'}} />
  </div>
);
const MobileInner: React.FC = () => {
  const f = useCurrentFrame();
  const enter = spring({frame: f, fps: FPS, config: {damping: 20, stiffness: 130}});
  const sImg = (n: string, scroll: number) => (
    <Img src={staticFile(`mobile/${n}.jpg`)} style={{position: 'absolute', left: 0, top: 0, width: PW, transform: `translate3d(0,${-scroll * (PW / 390)}px,0)`}} />
  );
  let inner: React.ReactNode;
  if (f < 30) inner = sImg('hero0', 0);
  else if (f < 60) inner = sImg('lavorazioni', 250 + 700 * prog(f, 30, 60, easeInOut));
  else inner = sImg('materioteca', 60 + 500 * prog(f, 60, 120, easeInOut));
  return <Phone x={(1 - enter) * 1100}>{inner}</Phone>;
};
const MobileScene: React.FC = () => {
  const f = useCurrentFrame();
  const inner = <MobileInner />;
  return f < 24 ? <CameraMotionBlur samples={6} shutterAngle={220}>{inner}</CameraMotionBlur> : inner;
};

// ---------- firma + CTA + loop ----------
const FirmaScene: React.FC<{showText: boolean}> = ({showText}) => {
  const f = useCurrentFrame();
  const total = F(CONFIG.total - CONFIG.firmaStart);
  const tail = total - F(CONFIG.loopTail);
  const shrink = spring({frame: f, fps: FPS, config: {damping: 22, stiffness: 100}});
  const back = prog(f, tail - 6, total, easeInOut);
  const scale = (1 - (1 - 0.66) * shrink) * (1 - back) + 0.96 * back;
  const sc = 1 + (0.66 - 1) * shrink; // 1 -> .66
  const finalScale = sc * (1 - back) + 0.96 * back;
  void scale;
  const cy = (940 + (690 - 940) * shrink) * (1 - back) + 940 * back;
  const rot = 6 * back;
  const textOut = 1 - prog(f, tail - 22, tail - 8);
  const hookWord0 = prog(f, tail + 2, total - 2);
  return (
    <>
      <Mockup cy={cy} scale={finalScale} rotX={rot}>
        <Img src={heroSrc(0)} style={{position: 'absolute', left: 0, top: 0, width: VW, height: VH}} />
      </Mockup>
      {showText && (
        <>
          <div style={{position: 'absolute', left: 0, right: 0, top: 1010, opacity: textOut, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 26}}>
            <Sequence from={8} layout="none"><Words text={CONFIG.firma} size={44} weight={600} stagger={4} letter="0" /></Sequence>
            <Sequence from={14} layout="none"><div style={{fontFamily, fontSize: 36, fontWeight: 400, letterSpacing: '0.04em', color: C.accent, textAlign: 'center'}}>{CONFIG.handle}</div></Sequence>
            <Sequence from={26} layout="none"><div style={{marginTop: 34}}><Words text={CONFIG.cta} size={62} weight={700} stagger={5} /></div></Sequence>
          </div>
          {/* raccordo col frame 0: la prima parola dell'hook riappare identica */}
          <div style={{position: 'absolute', left: 0, right: 0, top: 285, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6, opacity: hookWord0}}>
            {CONFIG.hook.map((line, li) => (
              <div key={li} style={{fontFamily, fontSize: 90, fontWeight: 700, letterSpacing: '-0.02em', color: C.stone, lineHeight: 1.04, textShadow: '0 2px 30px rgba(0,0,0,.55)'}}>
                {tokenize(line).map((t, i) => (
                  <span key={i} style={{display: 'inline-block', marginRight: '0.28em', opacity: li === 0 && i === 0 ? 1 : 0}}>{t.w}</span>
                ))}
              </div>
            ))}
          </div>
        </>
      )}
    </>
  );
};

const Captions: React.FC = () => (
  <>
    {CONFIG.captions.map((c, i) => {
      const from = F(c.from), dur = F(c.to - c.from);
      return (
        <Sequence key={i} from={from} durationInFrames={dur} layout="none">
          <div style={{position: 'absolute', left: 0, right: 0, top: 1345, display: 'flex', justifyContent: 'center'}}>
            <div style={{padding: '18px 34px', borderRadius: 999, background: 'rgba(11,11,12,.55)', backdropFilter: 'blur(14px)', border: '1px solid rgba(255,255,255,.12)'}}>
              <Words text={c.text} size={42} weight={600} stagger={4} letter="0" exitAt={dur - 9} />
            </div>
          </div>
        </Sequence>
      );
    })}
  </>
);

// ---------- Main ----------
export const Main: React.FC<{showText: boolean}> = ({showText}) => {
  const f = useCurrentFrame();
  const heroEnd = F(CONFIG.heroSeconds);
  const bgIdx = f < F(CONFIG.mobileStart) ? Math.min(f, HERO_LAST) : f >= F(CONFIG.firmaStart) ? 0 : HERO_LAST;
  const tStart = F(CONFIG.heroExitStart);
  const tEnd = F(15.45);
  return (
    <AbsoluteFill style={{background: C.bg}}>
      <FontStyle />
      <BG heroIdx={bgIdx} />

      {/* Atto 1 — hero senza tagli */}
      <Sequence from={0} durationInFrames={tStart} layout="none"><HeroMockup f={f} /></Sequence>
      {/* transizione: hero scende (slide + spring) mentre la sezione entra dall'alto, con motion blur */}
      <Sequence from={tStart} durationInFrames={tEnd - tStart} layout="none">
        <CameraMotionBlur samples={6} shutterAngle={200}>
          <TransitionStage />
        </CameraMotionBlur>
      </Sequence>
      <Sequence from={tEnd} durationInFrames={heroEnd + F(1.0) - tEnd} layout="none">
        <ShotsFromS1 />
      </Sequence>

      {SHOTS.filter((s) => s.id !== 's1').map((s) => (
        <Sequence key={s.id} from={F(s.start)} durationInFrames={F(s.dur)} layout="none"><Shot id={s.id} frames={F(s.dur)} /></Sequence>
      ))}

      <Sequence from={F(CONFIG.mobileStart)} durationInFrames={F(CONFIG.firmaStart - CONFIG.mobileStart)} layout="none"><MobileScene /></Sequence>
      <Sequence from={F(CONFIG.firmaStart)} durationInFrames={F(CONFIG.total - CONFIG.firmaStart)} layout="none"><FirmaScene showText={showText} /></Sequence>

      {showText && <Sequence from={0} durationInFrames={heroEnd} layout="none"><Hook show /></Sequence>}
      {showText && <Captions />}
    </AbsoluteFill>
  );
};

const TransitionStage: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <>
      <HeroMockup f={f + F(CONFIG.heroExitStart)} />
      {/* la sezione entra dall'alto a 15,0 s: offset negativo = parte 0,25 s dopo l'inizio della transizione */}
      <ShotA strip="lav" from={0} to={260} frames={F(1.15)} fOffset={-(F(14.85) - F(CONFIG.heroExitStart))} enter />
    </>
  );
};
const ShotsFromS1: React.FC = () => <ShotA strip="lav" from={0} to={260} frames={F(1.15)} fOffset={F(15.45) - F(14.85)} />;
