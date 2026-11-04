import numpy as np, cv2, math
from PIL import Image
R="/home/user/outputclaude"; AZ=np.array([0xBF,0xD7,0xEA],np.float32)/255
def s2l(x): x=np.clip(x,0,1); return np.where(x<=0.04045,x/12.92,((x+0.055)/1.055)**2.4)
def l2s(x): x=np.clip(x,0,1); return np.where(x<=0.0031308,x*12.92,1.055*x**(1/2.4)-0.055)
def load_rgba(p):
    im=np.array(Image.open(p).convert("RGBA")).astype(np.float32)/255; return im
def region(bgr,sam_path,k,buttons=True,pip_allow=None):
    H,W=bgr.shape[:2]
    m=cv2.resize(cv2.imread(sam_path,0),(W,H),interpolation=cv2.INTER_CUBIC)>127
    m=cv2.erode(m.astype(np.uint8),np.ones((int(1*k)+1,)*2,np.uint8)).astype(bool)
    hsv=cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV); h,s,v=[hsv[...,i].astype(int) for i in range(3)]
    button=cv2.dilate((((h<60)|(h>150))&(s>22)&(v>70)).astype(np.uint8),np.ones((int(3*k)+1,)*2,np.uint8)).astype(bool)
    bluish=~button if buttons else np.ones_like(button)
    vv=cv2.GaussianBlur(v.astype(np.uint8),(0,0),0.8*k)
    bh=cv2.morphologyEx(vv,cv2.MORPH_BLACKHAT,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(int(14*k)|1,)*2)).astype(int)
    dark=((bh>26)&(v<120)&(s>45)&(h>=90)&(h<=135)).astype(np.uint8)       # thin dark lines only
    dark=cv2.morphologyEx(dark,cv2.MORPH_CLOSE,np.ones((int(3*k)|1,)*2,np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(dark,connectivity=8)
    md=np.maximum(st[:,cv2.CC_STAT_WIDTH],st[:,cv2.CC_STAT_HEIGHT]).astype(np.float32)
    pip=(md>28*k); pip[0]=False                                          # long = piping, short = noise
    navy=cv2.dilate(np.isin(lab,np.where(pip)[0]).astype(np.uint8),np.ones((int(3*k)+1,)*2,np.uint8)).astype(bool)
    r=(m&bluish).astype(np.float32)
    if pip_allow is not None:
        yy_,xx_=np.mgrid[0:bgr.shape[0],0:bgr.shape[1]]; navy=navy&pip_allow(xx_/k,yy_/k)
    navy_soft=cv2.GaussianBlur((navy&m).astype(np.float32),(0,0),0.9*k)
    r=cv2.morphologyEx(r,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    return cv2.GaussianBlur(r,(0,0),0.9*k), cv2.morphologyEx(m.astype(np.uint8),cv2.MORPH_CLOSE,np.ones((int(15*k)|1,)*2,np.uint8)), navy_soft
def shading(bgr,reg):
    rgb=bgr[...,::-1].astype(np.float32)/255; Y=(s2l(rgb)*np.array([0.2126,0.7152,0.0722],np.float32)).sum(2)
    ref=np.median(Y[reg>0.95]); sh=np.clip(Y/ref,0.25,1.8)**1.05; sh=cv2.GaussianBlur(sh,(0,0),0.7); sh=np.where(sh>1,1+0.45*(sh-1),sh); return sh,ref
def foldshift(sh,k,amp,reg):
    w=(reg>0.5).astype(np.float32)
    Ls=cv2.GaussianBlur(sh*w,(0,0),5*k)/np.maximum(cv2.GaussianBlur(w,(0,0),5*k),1e-3)
    bg=cv2.GaussianBlur(sh*w,(0,0),30*k)/np.maximum(cv2.GaussianBlur(w,(0,0),30*k),1e-3)
    hp=(Ls-bg)*w
    gx=cv2.Sobel(hp,cv2.CV_32F,1,0,ksize=3); gy=cv2.Sobel(hp,cv2.CV_32F,0,1,ksize=3)
    n=np.percentile(np.hypot(gx,gy)[w>0.5],95)+1e-6
    return np.clip(gx/n,-1,1)*amp*k, np.clip(gy/n,-1,1)*amp*k
def cyl(reg,k,strength=0.8):
    m=(reg>0).astype(np.uint8); d=cv2.distanceTransform(m,cv2.DIST_L2,5)
    sc=4; ds=cv2.resize(d,None,fx=1/sc,fy=1/sc,interpolation=cv2.INTER_AREA)
    wh=cv2.dilate(ds,np.ones((int(260*k/sc)|1,)*2,np.uint8)); wh=cv2.GaussianBlur(wh,(0,0),6)
    wh=cv2.resize(wh,(d.shape[1],d.shape[0]),interpolation=cv2.INTER_LINEAR)+1e-3
    dg=cv2.GaussianBlur(d,(0,0),10*k); gx=-cv2.Sobel(dg,cv2.CV_32F,1,0,ksize=5); gy=-cv2.Sobel(dg,cv2.CV_32F,0,1,ksize=5)
    nn=np.hypot(gx,gy)+1e-6; ox,oy=gx/nn,gy/nn
    r=np.clip(1-d/wh,0,0.95); delta=wh*(np.arcsin(r)-r)*strength
    return ox*delta,oy*delta
def sample(print_rgba,mapx,mapy,wrap=False):
    pm=print_rgba.copy(); pm[...,:3]*=pm[...,3:4]
    if wrap:
        h,w=pm.shape[:2]; big=np.tile(pm,(3,3,1)); mapx=(mapx%w)+w; mapy=(mapy%h)+h
        out=cv2.remap(big,mapx.astype(np.float32),mapy.astype(np.float32),cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
    else:
        out=cv2.remap(pm,mapx.astype(np.float32),mapy.astype(np.float32),cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT,borderValue=(0,0,0,0))
    a=out[...,3:4]; rgb=np.where(a>1e-4,out[...,:3]/np.maximum(a,1e-4),0); return rgb,a[...,0]
def composite(base_path,sam_path,layers,k,buttons=True,pip_allow=None,fold_amp=5,cylinder=False,wrap_scale=None,tile=None,pxcm=None,tile_origin=(0,0),tile_rot=0.0):
    """layers: list of dict(print=rgba array, cx,cy (image coords centre, 1x), scale (print px->image px, 1x units), rot_deg)
       or tile mode: pattern from `tile` rgba, scale = pxcm/118 (300dpi)."""
    bgr=cv2.imread(base_path); H,W=bgr.shape[:2]
    reg,full,nv=region(bgr,sam_path,k,buttons,pip_allow); sh,_=shading(bgr,reg*(1-nv))
    fx,fy=foldshift(sh,k,fold_amp,reg)
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
    cx_,cy_=(0,0)
    if cylinder:
        cxs,cys=cyl(full,k); fx=fx+cxs; fy=fy+cys
    base_lin=s2l(bgr[...,::-1].astype(np.float32)/255)
    fab=np.broadcast_to(s2l(AZ),(H,W,3))*sh[...,None]
    col=fab.copy()
    def place(pr,cx,cy,sc,rot):
        # image px -> print px (in downscaled print domain)
        th=math.radians(rot); c,s=math.cos(th),math.sin(th)
        X=xx+fx-cx*k; Y=yy+fy-cy*k
        u=( c*X+s*Y)/(sc*k); v=(-s*X+c*Y)/(sc*k)
        return u+pr.shape[1]/2, v+pr.shape[0]/2
    if tile is not None:
        s=pxcm*k/118.0; t=cv2.resize(tile,None,fx=s,fy=s,interpolation=cv2.INTER_AREA)
        th=math.radians(tile_rot); c,sn=math.cos(th),math.sin(th)
        X=xx+fx+tile_origin[0]; Y=yy+fy+tile_origin[1]
        u=c*X+sn*Y; v=-sn*X+c*Y
        rgb,a=sample(t,u,v,wrap=True)
        ink=(s2l(rgb)*0.95+0.01)*np.clip(sh[...,None],0.2,1.1)**1.15; col=col*(1-a[...,None])+ink*a[...,None]
    for L in layers:
        sc=L["scale"]; pr=cv2.resize(L["print"],None,fx=sc*k if False else 1,fy=1,interpolation=cv2.INTER_AREA) if False else L["print"]
        f=sc*k; prs=cv2.resize(pr,(max(1,int(pr.shape[1]*f)),max(1,int(pr.shape[0]*f))),interpolation=cv2.INTER_AREA)
        th=math.radians(L.get("rot",0)); c,s=math.cos(th),math.sin(th)
        fm=L.get("fold",1.0); X=xx+fx*fm-L["cx"]*k; Y=yy+fy*fm-L["cy"]*k
        u=c*X+s*Y+prs.shape[1]/2; v=-s*X+c*Y+prs.shape[0]/2
        rgb,a=sample(prs,u,v)
        a=a*L.get("opacity",1.0); ink=(s2l(rgb)*0.93+0.012)*np.clip(sh[...,None],0.2,1.08)**1.2; col=col*(1-a[...,None])+ink*a[...,None]
    rgbf=bgr[...,::-1].astype(np.float32)/255; Yb=(s2l(rgbf)*np.array([0.2126,0.7152,0.0722],np.float32)).sum(2)
    sel=nv>0.5; refn=np.median(Yb[sel]) if sel.any() else 1.0
    nav=np.broadcast_to(s2l(np.array([0x1F,0x2A,0x44],np.float32)/255),(H,W,3))*np.clip(Yb/refn,0.35,1.5)[...,None]
    col=col*(1-nv[...,None])+nav*nv[...,None]
    out_lin=base_lin*(1-reg[...,None])+col*reg[...,None]
    out=(l2s(out_lin)*255).astype(np.uint8)[...,::-1]
    return out,reg,sh
