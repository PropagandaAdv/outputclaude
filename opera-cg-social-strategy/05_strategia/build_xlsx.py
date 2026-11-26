import sys; sys.path.insert(0,'.')
from content import *
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
wb=Workbook(); ws=wb.active; ws.title='Piano 4 settimane'
H=['Data','Giorno','Canale','Segmento','Pilastro','Formato','Titolo / gancio','CTA','Stato','Note / materiale da fornire']
ws.append(H)
GG=['Lun','Mar','Mer','Gio','Ven','Sab','Dom']
for (w,g,c,s,p,f,t,cta) in PIANO:
    ws.append([d(w,g),GG[g],c,s,p,f,t,cta,'Da produrre','Materiale cliente richiesto' if '[' in t else ''])
fill=PatternFill('solid',fgColor='1F3A5F'); thin=Side(style='thin',color='BBBBBB')
for c in ws[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=fill; c.alignment=Alignment(vertical='center',wrap_text=True)
for r in ws.iter_rows(min_row=2):
    for c in r: c.alignment=Alignment(vertical='top',wrap_text=True); c.border=Border(top=thin,bottom=thin,left=thin,right=thin)
for col,w in zip('ABCDEFGHIJ',[12,7,12,10,14,12,52,28,14,30]): ws.column_dimensions[col].width=w
ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
dv=DataValidation(type='list',formula1='"Da produrre,In lavorazione,Da approvare,Approvato,Pubblicato"',allow_blank=True); ws.add_data_validation(dv); dv.add(f'I2:I{ws.max_row}')
ws2=wb.create_sheet('Legenda')
for r in [['Segmenti']]+[[k,v] for k,v in SEGMENTI.items()]+[[],['Note'],['Date indicative: lancio ipotizzato lunedì 11/01/2027, da riallineare dopo setup.'],['I titoli con [ ] indicano materiale da fornire dal cliente (casi studio, foto, video).'],['Ogni riferimento normativo va verificato sulla norma vigente prima della pubblicazione.']]: ws2.append(r)
ws2.column_dimensions['A'].width=14; ws2.column_dimensions['B'].width=60
wb.save('../output/Piano_editoriale_4_settimane.xlsx'); print('ok',ws.max_row-1,'righe')
