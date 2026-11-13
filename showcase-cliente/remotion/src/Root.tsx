import React from 'react';
import {Composition} from 'remotion';
import {Main} from './Main';
import {FPS, W, H, TOTAL} from './config';

export const Root: React.FC = () => (
  <>
    <Composition id="Main" component={Main} durationInFrames={TOTAL} fps={FPS} width={W} height={H} defaultProps={{showText: true}} />
    <Composition id="Clean" component={Main} durationInFrames={TOTAL} fps={FPS} width={W} height={H} defaultProps={{showText: false}} />
  </>
);
