import numpy as np
from PIL import Image
R="/home/user/outputclaude"; AZ=(0xBF,0xD7,0xEA,255); DPI=(300,300); PPCM=118.11
oval=Image.open(f"{R}/work/face_cutout.png").convert("RGBA")
H_CM=9.5; dot_h=round(H_CM*PPCM); dot=oval.resize((round(oval.width*dot_h/oval.height),dot_h),Image.LANCZOS)
PX,PY=1600,1888                    # column pitch 13.5 cm, vertical period 16 cm
TW,TH=2*PX,PY                      # half-drop: 2nd column offset by PY/2
def paste_wrap(t,s,cx,cy):
    for ox in (-TW,0,TW):
        for oy in (-TH,0,TH):
            x=cx-s.width//2+ox; y=cy-s.height//2+oy
            x0,y0=max(x,0),max(y,0); x1,y1=min(x+s.width,TW),min(y+s.height,TH)
            if x1>x0 and y1>y0: t.alpha_composite(s.crop((x0-x,y0-y,x1-x,y1-y)),(x0,y0))
def build(bg):
    t=Image.new("RGBA",(TW,TH),bg)
    paste_wrap(t,dot,PX//2,PY//2); paste_wrap(t,dot,PX//2+PX,0)
    return t
tile=build(AZ); tile.save(f"{R}/print/B_pattern_tile.png",dpi=DPI); build((0,0,0,0)).save(f"{R}/print/B_pattern_tile_transparent.png",dpi=DPI)
big=Image.new("RGBA",(TW*3,TH*3))
for i in range(3):
    for j in range(3): big.paste(tile,(i*TW,j*TH))
big.convert("RGB").save(f"{R}/print/B_pattern_preview.png",dpi=DPI)
print("dot",dot.size,"tile",tile.size,"dot cm",dot.height/PPCM, dot.width/PPCM)
# seam check: difference between wrap-shifted halves (should be ~0 by construction)
a=np.array(tile.convert("RGB")).astype(int); print("edge L/R diff",np.abs(a[:,0]-a[:,-1]).mean().round(1),"edge T/B diff",np.abs(a[0]-a[-1]).mean().round(1))
