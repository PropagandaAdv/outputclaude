import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
import mediapipe as mp
from mediapipe.tasks import python as mpp
from mediapipe.tasks.python import vision
R="/home/user/outputclaude"
det=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=mpp.BaseOptions(model_asset_path=f"{R}/work/face_landmarker.task"),num_faces=1,min_face_detection_confidence=0.2))
def fc(path,pad=0.55):
    im=Image.open(path).convert("RGB"); sm=im.resize((im.width//2,im.height//2)); a=np.array(sm)
    r=det.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=a))
    if not r.face_landmarks: return im.crop((0,0,im.width,im.width))
    lm=np.array([[p.x*a.shape[1],p.y*a.shape[0]] for p in r.face_landmarks[0]])*2
    x0,y0=lm.min(0); x1,y1=lm.max(0); cx,cy=(x0+x1)/2,(y0+y1)/2; s=max(x1-x0,y1-y0)*(1+pad)
    return im.crop((int(cx-s/2),int(cy-s/2),int(cx+s/2),int(cy+s/2)))
refs=sys.argv[1].split(","); cands=sys.argv[2:]; S=340
f=ImageFont.truetype(f"{R}/work/fonts/Fredoka.ttf",24); f.set_variation_by_axes([500,100])
c=Image.new("RGB",((len(refs)+len(cands))*(S+8)+8,S+16),(255,255,255)); d=ImageDraw.Draw(c); x=8
for r in refs:
    im=Image.open(f"{R}/work/ref_face_{r}_white.png").convert("RGB"); im.thumbnail((S,S)); c.paste(im,(x+(S-im.width)//2,8+(S-im.height)//2)); d.text((x+6,10),f"rif {r}",font=f,fill=(30,40,70)); x+=S+8
for p in cands:
    im=fc(p).resize((S,S)); c.paste(im,(x,8)); d.text((x+6,10),p.split("/")[-1].replace(".png",""),font=f,fill=(255,255,255)); x+=S+8
c.save(f"{R}/work/r3/_grid.jpg",quality=90)
