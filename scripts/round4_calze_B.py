import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-outputclaude/85985d80-c67e-5fa8-a067-f42ebe7f77ad/scratchpad")
import numpy as np, cv2
from comp import *
W4="/home/user/outputclaude/work/r4"; k=float(sys.argv[1]); out=sys.argv[2]
tile=load_rgba(f"{R}/print/B_pattern_tile_calze.png"); PX,PY=1300,1500
pxcm=33; s_=pxcm*k/118.11
org_p=(PX/2*s_-560*k, PY/2*s_-700*k); org_s=(PX/2*s_-800*k, PY/2*s_-1720*k)
base=f"{W4}/up.jpg" if k>1 else f"{W4}/base.png"
u=cv2.imread(f"{W4}/all_union.png",0)
org_r=(PX/2*s_-1300*k, PY/2*s_-1650*k)
def run(org):
    return composite(base,f"{W4}/all_union.png",[],k,buttons=False,pip_allow=lambda x,y:(y>1280)&(y<1520),cylinder=True,tile=tile,pxcm=pxcm,tile_origin=org_p,tile_split=(f"{W4}/socks_union.png",org))[0]
imgL=run(org_s); imgR=run(org_r)
sm=cv2.imread(f"{W4}/socks_union.png",0)>127; H,W=imgL.shape[:2]; sm=cv2.resize(sm.astype(np.uint8),(W,H))>0
xx=np.arange(W)[None,:]*np.ones((H,1)); right=sm&(xx>1000*k)
r=cv2.GaussianBlur(right.astype(np.float32),(0,0),1.0)[...,None]
img=(imgL*(1-r)+imgR*r).astype(np.uint8)
cv2.imwrite(out,img,[cv2.IMWRITE_JPEG_QUALITY,93])
