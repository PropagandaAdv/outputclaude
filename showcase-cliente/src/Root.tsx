import React from 'react';
import { Composition } from 'remotion';
import { Main } from './Main';
import { FPS, TOTAL_FRAMES } from './config';

export const Root: React.FC = () => (
  <>
    <Composition
      id="Showcase"
      component={Main}
      durationInFrames={TOTAL_FRAMES}
      fps={FPS}
      width={1080}
      height={1920}
      defaultProps={{ showText: true }}
    />
  </>
);
