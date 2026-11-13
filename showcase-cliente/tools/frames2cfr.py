import json,sys,subprocess,os
d,out,fps=sys.argv[1],sys.argv[2],sys.argv[3]
t=json.load(open(f"{d}/times.json"))
lines=[]
for i in range(len(t)):
    dur=(t[i+1]-t[i]) if i+1<len(t) else 1/30
    lines.append(f"file '{os.path.abspath(d)}/{i:05d}.jpg'\nduration {dur:.6f}")
lines.append(f"file '{os.path.abspath(d)}/{len(t)-1:05d}.jpg'")
open(f"{d}/list.txt","w").write("\n".join(lines))
subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"{d}/list.txt","-vf",f"fps={fps}","-c:v","libx264","-crf","14","-pix_fmt","yuv420p",out],check=True)
