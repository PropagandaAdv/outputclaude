import json, subprocess, re, os
os.chdir('/home/user/outputclaude/opera-cg-social-strategy/05_strategia')
if os.path.exists('toc.json'): os.remove('toc.json')
subprocess.run(['python3','build_docx.py'],check=True)
def pdf():
    subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir','/tmp/claude-0/pdfchk','../output/Opera_CG_Analisi_e_Strategia_Social.docx'],capture_output=True)
    out=subprocess.run(['pdftotext','-layout','/tmp/claude-0/pdfchk/Opera_CG_Analisi_e_Strategia_Social.pdf','-'],capture_output=True,text=True).stdout
    return out.split('\f')
pages=pdf(); H=json.load(open('headings.json')); toc=[]
for lvl,t in H:
    pg='?'
    for i,tx in enumerate(pages):
        if i<2: continue
        if any(l.strip()==t.strip() or (len(t)>40 and l.strip().startswith(t[:35])) for l in tx.split('\n')): pg=i+1; break
    toc.append((lvl,t,pg))
json.dump(toc,open('toc.json','w'),ensure_ascii=False)
subprocess.run(['python3','build_docx.py'],check=True)
pages=pdf(); print(len(pages)-1,'pagine'); print([t for t in toc if t[2]=='?'])
