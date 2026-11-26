# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BLU = RGBColor(0x1F, 0x3A, 0x5F)
ARANCIO = RGBColor(0xE0, 0x7A, 0x1F)
GRIGIO = RGBColor(0x55, 0x55, 0x55)
HEX_BLU = '1F3A5F'; HEX_BOX = 'FFF4E5'; HEX_ALT = 'F2F5F9'

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexcolor)
    tcPr.append(shd)

def set_borders(table, color='BBBBBB'):
    tbl = table._tbl; tblPr = tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for e in ('top','left','bottom','right','insideH','insideV'):
        x = OxmlElement(f'w:{e}'); x.set(qn('w:val'),'single'); x.set(qn('w:sz'),'4'); x.set(qn('w:color'),color); b.append(x)
    tblPr.append(b)

def new_doc():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Cm(21); sec.page_height = Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2); sec.top_margin = Cm(2); sec.bottom_margin = Cm(2)
    st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
    st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.12
    for name, size, color in (('Heading 1', 20, BLU), ('Heading 2', 14, BLU), ('Heading 3', 11.5, ARANCIO)):
        h = doc.styles[name]; h.font.name = 'Calibri'; h.font.size = Pt(size); h.font.bold = True; h.font.color.rgb = color
        h.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri'); h.element.rPr.rFonts.set(qn('w:ascii'), 'Calibri'); h.element.rPr.rFonts.set(qn('w:hAnsi'), 'Calibri')
        h.paragraph_format.space_before = Pt(14 if name != 'Heading 3' else 8); h.paragraph_format.space_after = Pt(6)
        h.paragraph_format.keep_with_next = True
    return doc

def add_runs(p, text, size=None, color=None):
    """supporta **grassetto** inline"""
    parts = text.split('**')
    for i, t in enumerate(parts):
        if not t: continue
        r = p.add_run(t); r.bold = (i % 2 == 1)
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    return p

def para(doc, text, size=None, color=None, align=None, after=None):
    p = doc.add_paragraph(); add_runs(p, text, size, color)
    if align: p.alignment = align
    if after is not None: p.paragraph_format.space_after = Pt(after)
    return p

def bullets(doc, items, style='List Bullet'):
    for t in items:
        p = doc.add_paragraph(style=style); add_runs(p, t); p.paragraph_format.space_after = Pt(2)

def box(doc, title, lines):
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]; shade(c, HEX_BOX); set_borders(t, 'E07A1F')
    p = c.paragraphs[0]; r = p.add_run(title); r.bold = True; r.font.color.rgb = ARANCIO; r.font.size = Pt(11)
    for l in lines:
        q = c.add_paragraph(style='List Bullet'); add_runs(q, l, 10); q.paragraph_format.space_after = Pt(1)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def table(doc, header, rows, widths=None, size=9, zebra=True):
    t = doc.add_table(rows=1, cols=len(header)); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_borders(t); t.autofit = False
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]; shade(c, HEX_BLU); c.text = ''
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = RGBColor(255,255,255)
    # header ripetuto su ogni pagina
    trPr = t.rows[0]._tr.get_or_add_trPr(); th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); trPr.append(th)
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        cant = OxmlElement('w:cantSplit'); cant.set(qn('w:val'), 'true'); t.rows[-1]._tr.get_or_add_trPr().append(cant)
        for i, v in enumerate(row):
            cells[i].text = ''; p = cells[i].paragraphs[0]; p.paragraph_format.space_after = Pt(1)
            add_runs(p, str(v), size)
            if zebra and ri % 2 == 1: shade(cells[i], HEX_ALT)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths): row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

def add_toc(doc):
    p = doc.add_paragraph(); r = p.add_run()
    for kind, txt in (('begin', None), (None, 'TOC \\o "1-2" \\h \\z \\u'), ('separate', None), ('text', 'Fare clic con il tasto destro e scegliere "Aggiorna campo" per aggiornare l\'indice.'), ('end', None)):
        if kind in ('begin', 'separate', 'end'):
            f = OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'), kind); r._r.append(f)
        elif kind == 'text':
            t = OxmlElement('w:t'); t.text = txt; r._r.append(t)
        else:
            it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = txt; r._r.append(it)

def footer_pages(doc, text):
    sec = doc.sections[0]; p = sec.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text + '  |  pag. '); r.font.size = Pt(8); r.font.color.rgb = GRIGIO
    r2 = p.add_run(); r2.font.size = Pt(8)
    for kind in ('begin', 'instr', 'end'):
        if kind == 'instr':
            it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = 'PAGE'; r2._r.append(it)
        else:
            f = OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'), kind); r2._r.append(f)
