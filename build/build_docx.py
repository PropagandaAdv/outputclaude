# -*- coding: utf-8 -*-
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from content import DOC, SOURCES, CAL, IDEAS
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TEAL = RGBColor(0x0E, 0x7C, 0x7B)
CORAL = "F4A261"
DARK = RGBColor(0x26, 0x32, 0x38)
HEAD_FILL = "0E7C7B"
BOX_FILL = "E8F5F4"
ALT_FILL = "F6FAFA"

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2)
sec.top_margin, sec.bottom_margin = Cm(2.2), Cm(2.2)

st = doc.styles["Normal"]
st.font.name = "Calibri"; st.font.size = Pt(10.5); st.font.color.rgb = DARK
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.12
for name, size, color, before, after in [("Heading 1", 20, TEAL, 0, 10), ("Heading 2", 14, TEAL, 12, 4)]:
    h = doc.styles[name]
    h.font.name = "Calibri"; h.font.size = Pt(size); h.font.bold = True; h.font.color.rgb = color
    h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    h.element.rPr.rFonts.set(qn("w:ascii"), "Calibri"); h.element.rPr.rFonts.set(qn("w:hAnsi"), "Calibri")
    h.paragraph_format.space_before = Pt(before); h.paragraph_format.space_after = Pt(after)
    h.paragraph_format.keep_with_next = True

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    tcPr.append(shd)

def cell_margins(table, top=60, bottom=60, left=90, right=90):
    tblPr = table._tbl.tblPr
    m = OxmlElement("w:tblCellMar")
    for k, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement(f"w:{k}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); m.append(e)
    tblPr.append(m)

def borders(table, color="C9DEDD"):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for k in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{k}"); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4"); e.set(qn("w:space"), "0"); e.set(qn("w:color"), color); b.append(e)
    tblPr.append(b)

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    e = OxmlElement("w:tblHeader"); e.set(qn("w:val"), "true"); trPr.append(e)

def no_split(row):
    trPr = row._tr.get_or_add_trPr()
    e = OxmlElement("w:cantSplit"); e.set(qn("w:val"), "true"); trPr.append(e)

def add_runs(par, text, size=None, bold=False, color=None):
    # supporta **grassetto**? non usato. Evidenzia solo i riferimenti [n] in colore tenue
    parts = re.split(r"(\[\d+\](?:\[\d+\])*)", text)
    for p in parts:
        if not p: continue
        r = par.add_run(p)
        if size: r.font.size = Pt(size)
        r.bold = bold
        if re.fullmatch(r"(\[\d+\])+", p):
            r.font.size = Pt((size or 10.5) - 1); r.font.color.rgb = RGBColor(0x0E, 0x7C, 0x7B)
        elif color: r.font.color.rgb = color

def widths_for(header, rows):
    n = len(header)
    # larghezza proporzionale alla lunghezza media del contenuto, con minimo
    avg = []
    for i in range(n):
        l = [len(header[i])] + [len(str(r[i])) for r in rows]
        avg.append(max(8, min(60, sum(l) / len(l))))
    tot = sum(avg); W = 17.0
    w = [max(1.6, W * a / tot) for a in avg]
    s = sum(w); return [x * W / s for x in w]

def table(header, rows, note=None, fontsize=9):
    t = doc.add_table(rows=1, cols=len(header))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    borders(t); cell_margins(t)
    ws = widths_for(header, rows)
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]; shade(c, HEAD_FILL); c.width = Cm(ws[i])
        p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h); r.bold = True; r.font.size = Pt(fontsize); r.font.color.rgb = RGBColor(255, 255, 255)
    repeat_header(t.rows[0])
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        no_split(t.rows[-1])
        for i, v in enumerate(row):
            c = cells[i]; c.width = Cm(ws[i])
            if ri % 2 == 1: shade(c, ALT_FILL)
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.05
            add_runs(p, str(v), size=fontsize, bold=(i == 0 and len(header) > 2 and False))
            if i == 0 and header[0] != "":
                for r in p.runs: r.bold = True
    if note:
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3)
        add_runs(p, note, size=8.5, color=RGBColor(0x5F, 0x6F, 0x78))
        for r in p.runs: r.italic = True
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)

def box(title, body):
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    borders(t, "0E7C7B"); cell_margins(t, 120, 120, 180, 180)
    c = t.rows[0].cells[0]; shade(c, BOX_FILL); c.width = Cm(17)
    p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(4)
    r = p.add_run(title); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = TEAL
    items = body if isinstance(body, list) else [body]
    for it in items:
        q = c.add_paragraph(); q.paragraph_format.space_after = Pt(3)
        add_runs(q, it, size=10)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def field(par, instr):
    r = par.add_run()
    for t, txt in (("begin", None), (None, instr), ("end", None)):
        if t:
            e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), t); r._r.append(e)
        else:
            e = OxmlElement("w:instrText"); e.set(qn("xml:space"), "preserve"); e.text = txt; r._r.append(e)
    return r

# ---------------- cover
sec.different_first_page_header_footer = True
for _ in range(5): doc.add_paragraph()
p = doc.add_paragraph(); r = p.add_run("ANALISI DI MERCATO E STRATEGIA SOCIAL"); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = RGBColor(0xE7, 0x6F, 0x51)
p = doc.add_paragraph(); r = p.add_run("FamiClick"); r.bold = True; r.font.size = Pt(44); r.font.color.rgb = TEAL
p = doc.add_paragraph(); r = p.add_run("Come riempire l'app di professionisti e, poi, di famiglie"); r.font.size = Pt(18); r.font.color.rgb = DARK
for _ in range(10): doc.add_paragraph()
p = doc.add_paragraph(); r = p.add_run("a cura di Propaganda Adv"); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = TEAL
p = doc.add_paragraph(); r = p.add_run("23 novembre 2026"); r.font.size = Pt(11)
p = doc.add_paragraph(); r = p.add_run("Documento riservato. Dati consultati il 23/11/2026; le fonti sono elencate in appendice."); r.font.size = Pt(9); r.italic = True
doc.add_page_break()

# ---------------- indice
h = doc.add_paragraph(); r = h.add_run("Indice"); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = TEAL
h1s = [b[1] for b in DOC if b[0] == "h1"] + ["12. Fonti"]
for t in h1s:
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(5)
    r = p.add_run(t); r.font.size = Pt(12)
p = doc.add_paragraph()
add_runs(p, "Le note numerate tra parentesi quadre rimandano all'elenco fonti nell'ultima sezione.", size=9, color=RGBColor(0x5F, 0x6F, 0x78))
doc.add_page_break()

# ---------------- corpo
CLIENT_V = "Da confermare: "
for b in DOC:
    k = b[0]
    if k == "h1": doc.add_heading(b[1], level=1)
    elif k == "h2": doc.add_heading(b[1], level=2)
    elif k == "p":
        p = doc.add_paragraph()
        txt = b[1]
        if len(b) > 2 and b[2] == "V" and not txt.lower().startswith(("nota", "il sito dichiara")):
            r = p.add_run("Da confermare insieme. "); r.bold = True; r.font.color.rgb = RGBColor(0xE7, 0x6F, 0x51)
        add_runs(p, txt)
    elif k == "bul":
        for t, tag in b[1]:
            p = doc.add_paragraph(style="List Bullet"); p.paragraph_format.space_after = Pt(3)
            if tag == "V":
                r = p.add_run("Da confermare: "); r.bold = True; r.font.color.rgb = RGBColor(0xE7, 0x6F, 0x51)
            add_runs(p, t)
    elif k == "tab": table(b[1], b[2], b[4] or None)
    elif k == "box": box(b[1], b[2])
    elif k == "pb": doc.add_page_break()

# ---------------- fonti
doc.add_heading("12. Fonti", level=1)
p = doc.add_paragraph(); add_runs(p, "Tutte le fonti sono state consultate il 23/11/2026. Per gli elementi non leggibili o non trovati, il documento lo dichiara nel testo.", size=9.5)
for i, (t, u) in enumerate(SOURCES, 1):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2); p.paragraph_format.left_indent = Cm(0.8); p.paragraph_format.first_line_indent = Cm(-0.8)
    r = p.add_run(f"[{i}]  "); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = TEAL
    r = p.add_run(t + " – "); r.font.size = Pt(9)
    r = p.add_run(u); r.font.size = Pt(8.5); r.font.color.rgb = RGBColor(0x1F, 0x5F, 0x9F)

# ---------------- header/footer
sec = doc.sections[0]
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run("Propaganda Adv  ·  FamiClick, analisi di mercato e strategia social  ·  pag. "); r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x6B, 0x7C, 0x85)
rr = field(fp, "PAGE"); rr.font.size = Pt(8)

out = "/home/user/outputclaude/output/FamiClick_Analisi_Mercato_Strategia_Social.docx"
doc.save(out); print("ok", out)
