import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-outputclaude/85985d80-c67e-5fa8-a067-f42ebe7f77ad/scratchpad")
import numpy as np, cv2
from PIL import Image
from comp import *
which=sys.argv[1]; k=float(sys.argv[2]); sfx=sys.argv[3]; dst=sys.argv[4]   # sfx: base file suffix; dst: output dir/prefix
def crop(p,box=None):
    im=Image.open(p).convert("RGBA")
    if box: im=im.crop(box)
    bb=im.getchannel("A").getbbox(); return np.array(im.crop(bb)).astype(np.float32)/255
FRONT_OK=lambda x,y: (((y<1560)&(x>720)&(x<1230))|((y>1440)&(y<1620)&((x<720)|(x>1120)))|(y>2350))
SOCKS_OK=lambda x,y: (y>900)&(y<1130)
BACK_OK=lambda x,y: (y<640)|(y>1600)
tile=load_rgba(f"{R}/print/B_pattern_tile.png")
B=f"{R}/work/base"
def bp(n): return f"{B}/base_{n}.png" if sfx=="1x" else f"{B}/up_{n}.jpg"
if which=="front":
    fig=crop(f"{R}/print/A_front.png"); sam=f"{B}/sam_front_all.png"
    a,_,_=composite(bp("front"),sam,[dict(print=fig,cx=907,cy=1013,scale=465/fig.shape[0])],k,pip_allow=FRONT_OK)
    cv2.imwrite(f"{dst}A_pigiama_fronte.jpg",a,[cv2.IMWRITE_JPEG_QUALITY,93])
    b,_,_=composite(bp("front"),sam,[],k,pip_allow=FRONT_OK,cylinder=True,tile=tile,pxcm=14.5,tile_origin=(37,11))
    cv2.imwrite(f"{dst}B_pigiama_fronte.jpg",b,[cv2.IMWRITE_JPEG_QUALITY,93])
if which=="back":
    txt=crop(f"{R}/print/A_back.png"); sam=f"{B}/sam_back.png"
    a,_,_=composite(bp("back"),sam,[dict(print=txt,cx=905,cy=937,scale=450/txt.shape[1],fold=0.3)],k,pip_allow=BACK_OK)
    cv2.imwrite(f"{dst}A_pigiama_retro.jpg",a,[cv2.IMWRITE_JPEG_QUALITY,93])
    b,_,_=composite(bp("back"),sam,[],k,pip_allow=BACK_OK,cylinder=True,tile=tile,pxcm=14.5,tile_origin=(91,53))
    cv2.imwrite(f"{dst}B_pigiama_retro.jpg",b,[cv2.IMWRITE_JPEG_QUALITY,93])
if which=="socks":
    P=Image.open(f"{R}/print/A_socks.png"); w=P.width
    hl=crop(f"{R}/print/A_socks.png",(0,0,w//2,P.height)); hr=crop(f"{R}/print/A_socks.png",(w//2,0,w,P.height))
    sam=f"{B}/sam_socks.png"; sc=0.28; src=bp("socks_a") if sfx=="1x" else bp("socks")
    a,_,_=composite(src,sam,[dict(print=hl,cx=683,cy=1440,scale=sc,rot=5),dict(print=hr,cx=1117,cy=1345,scale=sc,rot=8)],k,buttons=False,pip_allow=SOCKS_OK)
    cv2.imwrite(f"{dst}A_calze.jpg",a,[cv2.IMWRITE_JPEG_QUALITY,93])
    b,_,_=composite(src,sam,[],k,cylinder=True,tile=tile,pxcm=33,tile_origin=(23,71),buttons=False,pip_allow=SOCKS_OK)
    cv2.imwrite(f"{dst}B_calze.jpg",b,[cv2.IMWRITE_JPEG_QUALITY,93])
