import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-outputclaude/85985d80-c67e-5fa8-a067-f42ebe7f77ad/scratchpad")
import numpy as np, cv2
from PIL import Image
from comp import *
W4="/home/user/outputclaude/work/r4"; k=float(sys.argv[1]); out=sys.argv[2]
a=cv2.imread(f"{W4}/socks_sam.png",0); b=cv2.imread(f"{W4}/socks_sam2.png",0)
m=np.maximum(a,b); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8)); cv2.imwrite(f"{W4}/socks_union.png",m)
def crop(p,box):
    im=Image.open(p).convert("RGBA").crop(box); bb=im.getchannel("A").getbbox(); return np.array(im.crop(bb)).astype(np.float32)/255
P=Image.open(f"{R}/print/A_socks.png"); w=P.width
hl=crop(f"{R}/print/A_socks.png",(0,0,w//2,P.height)); hr=crop(f"{R}/print/A_socks.png",(w//2,0,w,P.height))
base=f"{W4}/up.jpg" if k>1 else f"{W4}/base.png"
lay=[dict(print=hl,cx=800,cy=1730,scale=0.25,rot=8),dict(print=hr,cx=1285,cy=1690,scale=0.25,rot=-2)]
img,_,_=composite(base,f"{W4}/socks_union.png",lay,k,buttons=False,pip_allow=lambda x,y: y<-1)
cv2.imwrite(out,img,[cv2.IMWRITE_JPEG_QUALITY,93])
