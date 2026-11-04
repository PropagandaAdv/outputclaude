import numpy as np, cv2
from PIL import Image
import mediapipe as mp
from mediapipe.tasks import python as mpp
from mediapipe.tasks.python import vision
R="/home/user/outputclaude"
img=cv2.imread(f"{R}/input/selfie.jpg"); H,W=img.shape[:2]
det=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
  base_options=mpp.BaseOptions(model_asset_path=f"{R}/work/face_landmarker.task"),num_faces=1))
res=det.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)))
lm=np.array([[p.x*W,p.y*H] for p in res.face_landmarks[0]])
chin=lm[152]; fw=lm[:,0].max()-lm[:,0].min(); cx=(lm[234,0]+lm[454,0])/2
# foreground = not white background
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); fgm=(g<225).astype(np.uint8)*255
n,lab,st,_=cv2.connectedComponentsWithStats(fgm); fgm=np.where(lab==1+np.argmax(st[1:,4]),255,0).astype(np.uint8)
fgm=cv2.morphologyEx(fgm,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
ys=np.where(fgm.any(1))[0]; hair_top=ys.min()
bottom=chin[1]+0.03*(chin[1]-hair_top)
cy=(hair_top+bottom)/2; b=(bottom-hair_top)/2; a=fw*0.66
ell=np.zeros((H,W),np.uint8); cv2.ellipse(ell,(int(cx),int(cy)),(int(a),int(b)),0,0,360,255,-1)
m=cv2.bitwise_and(fgm,ell)
m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((7,7),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(m); m=np.where(lab==1+np.argmax(st[1:,4]),255,0).astype(np.uint8)
mm=cv2.GaussianBlur(m,(0,0),3); m=(mm>127).astype(np.uint8)*255
alpha=cv2.GaussianBlur(m,(0,0),1.5)
yy,xx=np.where(m>0); p=12; x0,x1,y0,y1=xx.min()-p,xx.max()+p,yy.min()-p,yy.max()+p
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
out=np.dstack([rgb,alpha])[y0:y1,x0:x1]
Image.fromarray(out,"RGBA").save(f"{R}/work/face_cutout_lowres.png")
# upscale input: fill outside with inpaint to avoid halo
fill=cv2.inpaint(img,cv2.dilate(255-m,np.ones((3,3),np.uint8)),6,cv2.INPAINT_TELEA)
cv2.imwrite(f"{R}/work/face_for_upscale.png",fill[y0:y1,x0:x1])
o=Image.fromarray(out,"RGBA"); bg=Image.new("RGBA",o.size,(191,215,234,255)); bg.alpha_composite(o)
bg.convert("RGB").save(f"{R}/work/face_cutout_preview.jpg",quality=92); print(o.size)
