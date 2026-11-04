import sys, json; sys.path.insert(0,"/tmp/claude-0/-home-user-outputclaude/85985d80-c67e-5fa8-a067-f42ebe7f77ad/scratchpad")
import numpy as np, cv2
from PIL import Image
from comp import *
which=sys.argv[1]; k=float(sys.argv[2]); out=sys.argv[3]
W2="/home/user/outputclaude/work/r3"
G=dict(json.load(open(f"{W2}/geo.json")))
OVR=json.load(open(f"{W2}/override.json")) if __import__("os").path.exists(f"{W2}/override.json") else {}
def crop(p):
    im=Image.open(p).convert("RGBA"); bb=im.getchannel("A").getbbox(); return np.array(im.crop(bb)).astype(np.float32)/255
tile=load_rgba(f"{R}/print/B_pattern_tile.png"); PX,PY=1600,1888
def run(n,kind,dst):
    g=dict(G[n]); g.update(OVR.get(n,{})); y0,top,cx=g["y0"],g["top"],g["cx"]; L=top-y0; pxcm=L/68.0
    base=f"{W2}/up_{n}.jpg" if k>1 else f"{W2}/base_{n}.png"; sam=f"{W2}/garment_{n}.png"
    def neck(bgr,h,s,v,kk):
        yy_,xx_=np.mgrid[0:bgr.shape[0],0:bgr.shape[1]]; yy_=yy_/kk; xx_=xx_/kk
        zone=(yy_>y0-25)&(yy_<y0+0.17*L)&(np.abs(xx_-g.get("ncx",cx))<0.24*L)&(h>=98)&(h<=135)
        strong=(zone&(s>85)&(v<110)).astype(np.uint8)
        m_=cv2.morphologyEx(strong,cv2.MORPH_CLOSE,np.ones((int(5*kk)|1,)*2,np.uint8))
        n_,lab,st,_=cv2.connectedComponentsWithStats(m_)
        if n_>1:
            k_=1+int(np.argmax(st[1:,cv2.CC_STAT_AREA])); m_=(lab==k_).astype(np.uint8)
        m_=cv2.dilate(m_,np.ones((int(1*kk)|1,)*2,np.uint8))
        return m_>0
    allow=lambda x,y: (y<-1)
    if kind=="A_front":
        fig=crop(f"{R}/print/A_front.png"); cyf=y0+g.get("fy",0.43)*L
        img,_,_=composite(base,sam,[dict(print=fig,cx=cx,cy=cyf,scale=0.45*L/fig.shape[0])],k,buttons=False,pip_allow=allow,keep_extra=neck)
    elif kind=="A_back":
        txt=crop(f"{R}/print/A_back.png"); cyt=y0+g.get("fy",0.30)*L
        img,_,_=composite(base,sam,[dict(print=txt,cx=cx,cy=cyt,scale=g.get("tw",0.44)*L/txt.shape[1],fold=0.3,rot=g.get("rot",0))],k,buttons=False,pip_allow=allow,keep_extra=neck)
    else:
        s_=pxcm*k/118.11; fcx=cx; fcy=y0+0.46*L
        org=(PX/2*s_-fcx*k, PY/2*s_-fcy*k); org2=(PX/2*s_-fcx*k+PX*s_*0.5, PY/2*s_-(top+0.13*L)*k)
        img,_,_=composite(base,sam,[],k,buttons=False,pip_allow=allow,keep_extra=neck,cylinder=True,tile=tile,pxcm=pxcm,tile_origin=org,tile_rot=g.get("rot",0),tile_split=(f"{W2}/pantsmask_{n}.png",org2))
    cv2.imwrite(dst,img,[cv2.IMWRITE_JPEG_QUALITY,93]); print("wrote",dst)
jobs={"Afront":("A_front","A_pigiama_fronte.jpg"),"Aback":("A_back","A_pigiama_retro.jpg"),"Bfront":("B","B_pigiama_fronte.jpg"),
      "Bback":("B","B_pigiama_retro.jpg"),"Bcrown":("B","B_pigiama_fronte_coroncina.jpg")}
for n in which.split(","):
    kind,fn=jobs[n]; run(n,kind,out+fn)
