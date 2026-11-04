import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
R="/home/user/outputclaude"; NAVY=(0x1F,0x2A,0x44); AZ=(0xBF,0xD7,0xEA)
DPI=(300,300)
# ---------- 1) matte of full photo (white background) ----------
im=cv2.imread(f"{R}/work/photo_full_upscaled.jpg"); H,W=im.shape[:2]; print("photo",W,H)
g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)
fg=(g<238).astype(np.uint8)*255
n,lab,st,_=cv2.connectedComponentsWithStats(fg); fg=np.where(lab==1+np.argmax(st[1:,4]),255,0).astype(np.uint8)
fg=cv2.morphologyEx(fg,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
# fill holes
ff=fg.copy(); mk=np.zeros((H+2,W+2),np.uint8); cv2.floodFill(ff,mk,(0,0),255); fg=fg|cv2.bitwise_not(ff)
core=cv2.erode(fg,np.ones((13,13),np.uint8))
# edge band: soft alpha from whiteness vs hair colour (~60)
soft=np.clip((255-g)/(255-70),0,1)
band=(fg>0)&(core==0)
alpha=np.where(core>0,1.0,np.where(band,soft,0.0)).astype(np.float32)
alpha=cv2.GaussianBlur(alpha,(0,0),1.0)
# decontaminate white fringe
a3=np.clip(alpha,0.05,1)[...,None]; bgr=im.astype(np.float32)
dec=np.clip((bgr-(1-a3)*255)/a3,0,255); bgr=np.where(band[...,None],dec,bgr)
# fade where the photo frame cuts the figure (sides/bottom)
yy,xx=np.mgrid[0:H,0:W]; d=np.minimum.reduce([xx,W-1-xx,H-1-yy]).astype(np.float32)
t=np.clip(d/(0.045*W),0,1); alpha*=t*t*(3-2*t)
fb=np.clip((H-1-yy)/(0.16*H),0,1); alpha*=fb*fb*(3-2*fb)
rgba=np.dstack([cv2.cvtColor(bgr.astype(np.uint8),cv2.COLOR_BGR2RGB),(alpha*255).astype(np.uint8)])
person=Image.fromarray(rgba,"RGBA"); person.save(f"{R}/work/photo_full_cutout.png",dpi=DPI)
bg=Image.new("RGBA",person.size,AZ+(255,)); bg.alpha_composite(person); bg.convert("RGB").resize((W//4,H//4)).save(f"{R}/work/photo_full_preview.jpg",quality=90)
# ---------- 2) variant A ----------
PW,PH=5000,6500   # printable body panel, 300 dpi (~42 x 55 cm)
def fit_h(img,h): return img.resize((round(img.width*h/img.height),h),Image.LANCZOS)
fr=Image.new("RGBA",(PW,PH),(0,0,0,0)); fig=fit_h(person,int(PH*0.45))
fr.alpha_composite(fig,((PW-fig.width)//2,int(PH*0.40)-fig.height//2)); fr.save(f"{R}/print/A_front.png",dpi=DPI)
# back: text
bk=Image.new("RGBA",(PW,PH),(0,0,0,0)); d=ImageDraw.Draw(bk)
font=ImageFont.truetype(f"{R}/work/fonts/Fredoka.ttf",400); font.set_variation_by_axes([700,100])  # wdth, wght
words=["Proprietà","privata"]
def meas(sz):
    f=ImageFont.truetype(f"{R}/work/fonts/Fredoka.ttf",sz); f.set_variation_by_axes([700,100])
    ws=[d.textlength(w_,font=f) for w_ in words]; return f,ws,sum(ws)+0.34*sz
for sz in range(300,900,10):
    font,ws,tot=meas(sz)
    if tot>PW*0.70: break
font,ws,tot=meas(sz-10); sz-=10; gap=0.34*sz; cy=int(PH*0.24); x=(PW-tot)/2
for w_,wl in zip(words,ws):
    d.text((x,cy),w_,font=font,fill=NAVY+(255,),anchor="ls"); x+=wl+gap
bk.save(f"{R}/print/A_back.png",dpi=DPI); print("font px",sz,"text w",tot)
# socks: head+hair of the photo, medium (~6.5 cm), outer side, ankle height
head=person.crop((0,0,W,int(H*0.60)))
ha=np.array(head)[...,3].astype(np.float32); yy2=np.arange(head.height)[:,None]
f=np.clip((head.height-yy2)/(0.12*head.height),0,1); head.putalpha(Image.fromarray((ha*f).astype(np.uint8)))
bb=head.getbbox(); head=head.crop(bb)
ha=np.array(head)[...,3].astype(np.float32); hh,ww=ha.shape; Y,X=np.mgrid[0:hh,0:ww]
rr=np.sqrt(((X-ww/2)/(ww/2))**2+((Y-hh*0.46)/(hh*0.54))**2); soft=np.clip((1.0-rr)/0.22,0,1); soft=soft*soft*(3-2*soft)
head.putalpha(Image.fromarray((ha*soft).astype(np.uint8))); head=head.crop(head.getchannel('A').getbbox()); hd=fit_h(head,780)
SW,SH=2400,4200   # each sock panel
sk=Image.new("RGBA",(SW*2+300,SH),(0,0,0,0))
for i,xo in enumerate((0,SW+300)):
    cxp=xo+SW//2+(-260 if i==0 else 260)   # outer side: left sock -> left, right sock -> right
    sk.alpha_composite(hd,(cxp-hd.width//2,int(SH*0.62)))
sk.save(f"{R}/print/A_socks.png",dpi=DPI)
# ---------- 3) variant B: half-drop polka tile ----------
oval=Image.open(f"{R}/work/face_cutout.png").convert("RGBA")
dot=fit_h(oval,531)   # ~4.5 cm tall @300dpi
PX,PY=700,800; TW,TH=2*PX,PY    # tile = 2 columns, 2nd column dropped by half
def build(bgcol):
    t=Image.new("RGBA",(TW,TH),bgcol)
    for cx,cy in ((PX//2,0),(PX//2+PX,PY//2)):
        for ox in (-TW,0,TW):
            for oy in (-TH,0,TH):
                t.alpha_composite(dot,(cx-dot.width//2+ox,cy-dot.height//2+oy)) if False else None
    # explicit wrapped pastes
    for cx,cy in ((PX//2,PY//2),(PX//2+PX,0),(PX//2+PX,PY)):
        for ox in (-TW,0,TW):
            for oy in (-TH,0,TH):
                x=cx-dot.width//2+ox; y=cy-dot.height//2+oy
                if x<TW and y<TH and x+dot.width>0 and y+dot.height>0: t.alpha_composite(dot,(x,y)) if (x>=0 and y>=0) else paste_clip(t,dot,x,y)
    return t
def paste_clip(t,s,x,y):
    x0,y0=max(x,0),max(y,0); x1,y1=min(x+s.width,t.width),min(y+s.height,t.height)
    if x1<=x0 or y1<=y0: return
    t.alpha_composite(s.crop((x0-x,y0-y,x1-x,y1-y)),(x0,y0))
tile=build(AZ+(255,)); tile.save(f"{R}/print/B_pattern_tile.png",dpi=DPI)
build((0,0,0,0)).save(f"{R}/print/B_pattern_tile_transparent.png",dpi=DPI)
big=Image.new("RGBA",(TW*3,TH*3))
for i in range(3):
    for j in range(3): big.paste(tile,(i*TW,j*TH))
big.convert("RGB").save(f"{R}/print/B_pattern_preview.png",dpi=DPI); print("tile",tile.size)
