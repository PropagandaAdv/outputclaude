#!/bin/bash
cd /home/user/outputclaude/showcase-cliente/remotion
npx remotion render src/index.ts Showcase ../out/showcase_tecnomarmi_9x16.mp4 --codec=h264 --crf=10 --pixel-format=yuv420p --h264-profile=high --muted --timeout=90000 > ../work/render_final.log 2>&1
npx remotion render src/index.ts ShowcaseClean ../out/showcase_tecnomarmi_9x16_clean.mp4 --codec=h264 --crf=10 --pixel-format=yuv420p --h264-profile=high --muted --timeout=90000 > ../work/render_clean.log 2>&1
echo ALLDONE > ../work/render_done.flag
