# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import CAL, IDEAS
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
wb=Workbook(); ws=wb.active; ws.title="Calendario 4 settimane"
hdr=["Sett.","Giorno","Piattaforma","Pilastro","Formato","Hook","Copy breve","CTA","Obiettivo","Stato"]
fill=PatternFill("solid",fgColor="0E7C7B"); thin=Side(style="thin",color="C9DEDD")
ws.append(hdr)
for r in CAL: ws.append(r+["Da produrre"])
widths=[6,12,20,22,20,42,56,30,26,14]
for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
for c in ws[1]:
    c.fill=fill; c.font=Font(bold=True,color="FFFFFF"); c.alignment=Alignment(vertical="center",wrap_text=True)
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.alignment=Alignment(vertical="top",wrap_text=True); c.border=Border(top=thin,bottom=thin,left=thin,right=thin)
ws.freeze_panes="C2"; ws.auto_filter.ref=ws.dimensions
w2=wb.create_sheet("10 idee Reel-TikTok"); w2.append(["#","Per chi","Hook (primi 3 secondi)","Scaletta","CTA"])
for i,x in enumerate(IDEAS,1): w2.append([i,*x])
for i,w in enumerate([5,16,50,70,36],1): w2.column_dimensions[get_column_letter(i)].width=w
for c in w2[1]: c.fill=fill; c.font=Font(bold=True,color="FFFFFF")
for row in w2.iter_rows(min_row=2):
    for c in row: c.alignment=Alignment(vertical="top",wrap_text=True)
w3=wb.create_sheet("Note")
for l in ["Calendario di esempio 30/11/2026 – 27/12/2026 (Propaganda Adv).","Frequenza: 4 contenuti/settimana su Instagram (3 Reel + 1 carosello), gli stessi Reel su TikTok, 1 post LinkedIn/settimana, Stories quotidiane (benchmark 3–5/settimana: Hootsuite, Buffer).","Contenuti su bonus e salute: verificare sempre sulle fonti ufficiali prima della pubblicazione; nessun importo nei post.","Contenuti con professionisti: pubblicare solo con consenso scritto.","Le date sono indicative e vanno adattate al lancio effettivo."]:
    w3.append([l])
w3.column_dimensions["A"].width=140
wb.save("/home/user/outputclaude/output/calendario-editoriale.xlsx"); print("xlsx ok")
