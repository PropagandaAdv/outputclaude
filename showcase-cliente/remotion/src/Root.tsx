import React from 'react';
import {Composition, Still} from 'remotion';
import {Main} from './Main';
import {CONFIG} from './config';

export const Root: React.FC = () => (
  <>
    <Composition id="Showcase" component={Main} durationInFrames={Math.round(CONFIG.total * CONFIG.fps)}
      fps={CONFIG.fps} width={CONFIG.width} height={CONFIG.height} defaultProps={{showText: true}} />
    <Composition id="ShowcaseClean" component={Main} durationInFrames={Math.round(CONFIG.total * CONFIG.fps)}
      fps={CONFIG.fps} width={CONFIG.width} height={CONFIG.height} defaultProps={{showText: false}} />
  </>
);
