import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-outputclaude/85985d80-c67e-5fa8-a067-f42ebe7f77ad/scratchpad")
import numpy as np, cv2
from PIL import Image
from comp import *
W5="/home/user/outputclaude/work/r5"; k=float(sys.argv[1]); out=sys.argv[2]
im=Image.open(f"{R}/print/A_back.png").convert("RGBA"); bb=im.getchannel("A").getbbox(); txt=np.array(im.crop(bb)).astype(np.float32)/255
def neck(bgr,h,s,v,kk):
    yy_,xx_=np.mgrid[0:bgr.shape[0],0:bgr.shape[1]]; yy_=yy_/kk; xx_=xx_/kk
    zone=(yy_>650)&(yy_<800)&(np.abs(xx_-860)<260)&(h>=98)&(h<=135)
    m_=cv2.morphologyEx((zone&(s>85)&(v<110)).astype(np.uint8),cv2.MORPH_CLOSE,np.ones((int(5*kk)|1,)*2,np.uint8))
    return cv2.dilate(m_,np.ones((int(1*kk)|1,)*2,np.uint8))>0
base=f"{W5}/up.jpg" if k>1 else f"{W5}/base.png"
img,_,_=composite(base,f"{W5}/garment.png",[dict(print=txt,cx=875,cy=1190,scale=600/txt.shape[1],fold=0.3)],k,buttons=False,pip_allow=lambda x,y:y<-1,keep_extra=neck)
cv2.imwrite(out,img,[cv2.IMWRITE_JPEG_QUALITY,93])
