# -*- coding: utf-8 -*-
"""Genera output/Retica_LinkedIn_Ads_Proposta.pptx (brand Propaganda Adv: nero, Poppins, blu #233DFF)."""
import json, re, os, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
MOCK = f'{ROOT}/output/mockup'
ADS = {a['id']: a for a in json.load(open(f'{ROOT}/analysis/ads.json', encoding='utf8'))}
BUD = json.load(open(f'{ROOT}/analysis/budget_results.json'))['results']
def bud(sc, case='Base'): return next(r for r in BUD if r['scenario'] == sc and r['case'] == case)

def rgb(h): return RGBColor.from_string(h.lstrip('#'))
BG, PANEL, PANEL2 = '05060A', '10121A', '181B27'
BLUE, BLUE2, WHITE, GREY, MUT = '233DFF', '5568FF', 'FFFFFF', 'B4B7C2', '8C8F99'
TAG = {'[VERIFICATO]': '39B54A', '[STIMA]': 'F5B83D', '[DA CONFERMARE]': 'FF6B8B'}
FONT = 'Poppins'

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
state = {'n': 0}

def box(s, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE, lw=1):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill: sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    else: sh.fill.background()
    if line: sh.line.color.rgb = rgb(line); sh.line.width = Pt(lw)
    else: sh.line.fill.background()
    sh.shadow.inherit = False
    return sh

def rrect(s, x, y, w, h, fill=PANEL, line=None, r=0.08):
    sh = box(s, x, y, w, h, fill, line, MSO_SHAPE.ROUNDED_RECTANGLE)
    sh.adjustments[0] = r
    return sh

def _runs(p, text, size, color, bold, font=FONT):
    parts = re.split(r'(\[VERIFICATO\]|\[STIMA\]|\[DA CONFERMARE\])', text)
    for part in parts:
        if not part: continue
        r = p.add_run(); r.text = part; f = r.font; f.name = font; f.size = Pt(size)
        if part in TAG: f.color.rgb = rgb(TAG[part]); f.bold = True; f.size = Pt(max(size - 1, 8))
        else: f.color.rgb = rgb(color); f.bold = bold

def text(s, x, y, w, h, paras, size=16, color=WHITE, bold=False, align='l', anchor='t', space=4, line=1.1, font=FONT):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame
    tf.word_wrap = True; tf.margin_left = tf.margin_right = Inches(0.02); tf.margin_top = tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = {'t': MSO_ANCHOR.TOP, 'm': MSO_ANCHOR.MIDDLE, 'b': MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(paras, str): paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {'l': PP_ALIGN.LEFT, 'c': PP_ALIGN.CENTER, 'r': PP_ALIGN.RIGHT}[align]
        p.space_after = Pt(space); p.line_spacing = line
        if isinstance(para, tuple):  # (testo, dict)
            t, o = para; _runs(p, t, o.get('size', size), o.get('color', color), o.get('bold', bold), o.get('font', font))
        else: _runs(p, para, size, color, bold, font)
    return tb

def bullets(s, x, y, w, items, size=15, color=WHITE, gap=7, dot=BLUE2, h=None):
    yy = y
    for it in items:
        box(s, x, yy + 0.085, 0.09, 0.09, dot, shape=MSO_SHAPE.OVAL)
        lines = max(1, int(len(re.sub(r'\[.*?\]', '', it)) * size * 0.0076 / (w - 0.3)) + 1)
        hh = lines * size * 0.0185 + 0.06
        text(s, x + 0.22, yy, w - 0.25, hh, it, size=size, color=color, space=0)
        yy += hh + gap / 72 * 1.0 + 0.04
    return yy

def new(kicker, title, source=None, title_size=28):
    s = prs.slides.add_slide(BLANK); state['n'] += 1
    bg = s.background.fill; bg.solid(); bg.fore_color.rgb = rgb(BG)
    box(s, 0.7, 0.62, 0.45, 0.035, BLUE)
    text(s, 1.25, 0.5, 8, 0.3, kicker.upper(), size=10, color=WHITE, bold=True)
    text(s, 0.7, 0.85, 11.9, 1.1, title, size=title_size, bold=True, line=1.0)
    if source: text(s, 0.7, 6.88, 10.8, 0.45, 'Fonte: ' + source, size=8.5, color=MUT, space=0)
    text(s, 11.2, 6.98, 1.5, 0.3, f'{state["n"]:02d}', size=9, color=MUT, align='r')
    return s

def pic(s, path, x, y, h=None, w=None):
    im = Image.open(path); ar = im.width / im.height
    if h: w = h * ar
    else: h = w / ar
    s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h)); return w, h

def big(s, x, y, w, num, label, color=WHITE, nsize=40, lsize=11, lh=0.6):
    text(s, x, y, w, 0.9, num, size=nsize, bold=True, color=color, space=0, line=1.0)
    text(s, x, y + nsize * 0.0195 + 0.12, w, lh, label, size=lsize, color=GREY, space=0)

def chip(s, x, y, t, w=None, fill=PANEL2, color=WHITE, size=11, h=0.36):
    w = w or (len(t) * size * 0.0098 + 0.4)
    rrect(s, x, y, w, h, fill, None, 0.5); text(s, x, y, w, h, t, size=size, color=color, align='c', anchor='m', space=0)
    return w

def table(s, x, y, colw, rows, head=True, size=11, rowh=0.5, hfill=BLUE, zebra=True):
    shp = s.shapes.add_table(len(rows), len(colw), Inches(x), Inches(y), Inches(sum(colw)), Inches(rowh * len(rows)))
    tbl = shp.table
    tblPr = shp._element.graphic.graphicData.tbl.tblPr; tblPr.set('firstRow', '0'); tblPr.set('bandRow', '0')
    for j, w in enumerate(colw): tbl.columns[j].width = Inches(w)
    for i, row in enumerate(rows):
        tbl.rows[i].height = Inches(rowh)
        for j, val in enumerate(row):
            c = tbl.cell(i, j); c.margin_left = c.margin_right = Inches(0.1); c.margin_top = c.margin_bottom = Inches(0.04)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.fill.solid(); c.fill.fore_color.rgb = rgb(hfill if (head and i == 0) else (PANEL if (i % 2 == 1 or not zebra) else PANEL2))
            tf = c.text_frame; tf.word_wrap = True; p = tf.paragraphs[0]
            _runs(p, val, size, WHITE, bool((head and i == 0) or j == 0))
    return tbl

# ============================================================ SLIDE 1 — cover
s = prs.slides.add_slide(BLANK); state['n'] += 1
bg = s.background.fill; bg.solid(); bg.fore_color.rgb = rgb(BG)
box(s, 0, 0, 13.333, 7.5, '0B0E22')
box(s, 8.6, -1.5, 7.5, 7.5, '233DFF', shape=MSO_SHAPE.OVAL).fill.fore_color.rgb = rgb('141C66')
pic(s, f'{ROOT}/assets/propaganda/logo_propaganda_ritagliato.png', 0.7, 0.5, h=0.55)
box(s, 0.7, 2.2, 0.45, 0.035, BLUE)
text(s, 1.25, 2.08, 9, 0.3, 'PROPOSTA · FASE PRELIMINARE', size=11, bold=True)
text(s, 0.7, 2.6, 10.5, 2.4, ['Propaganda Adv × Retica', ('LinkedIn Ads per portare demo qualificate', {'size': 30, 'bold': False, 'color': GREY})], size=54, bold=True, space=10, line=1.0)
text(s, 0.7, 5.6, 8, 0.8, ['19 novembre 2026', 'Documento di lavoro: nessuna campagna creata, nessuna spesa attiva.'], size=13, color=GREY, space=2)
pic(s, f'{ROOT}/assets/retica/logo_retica-3.png', 10.7, 6.3, h=0.55)

# ============================================================ SLIDE 2 — obiettivo e sintesi
s = new('Obiettivo e sintesi', 'Fare di LinkedIn un canale di demo per Retica',
        'Propaganda Adv, proposta di strategia; numeri di budget dal modello analysis/budget_model.py [STIMA].')
x = 0.7
for t in ['Lead', 'MQL', 'Demo fissata']:
    w = chip(s, x, 2.0, t, w=2.1, fill=BLUE if t == 'Demo fissata' else PANEL2, size=15, h=0.55); x += 2.1
    if t != 'Demo fissata': text(s, x, 2.0, 0.5, 0.55, '→', size=20, color=BLUE2, align='c', anchor='m'); x += 0.5
big(s, 0.7, 3.0, 2.8, '10', 'annunci pronti, con 2 varianti di copy ciascuno')
big(s, 3.7, 3.0, 2.8, '3', 'livelli di funnel: TOFU, MOFU, BOFU')
big(s, 6.7, 3.0, 2.8, '3', 'scenari di budget: 1.500 / 3.000 / 5.000 € al mese')
big(s, 9.7, 3.0, 2.8, '12', 'settimane di test minimo prima di giudicare')
bullets(s, 0.7, 4.75, 7.3, ['Target: operations, supply chain, amministrazione, IT/EDP e CEO di PMI italiane da 20 a 1.000 dipendenti.',
                           'Angolo: prima il beneficio (tempo e meno errori), poi la prova (124 clienti, 6.000+ scansioni al giorno).',
                           'Misuriamo lead, costo per lead e costo per demo, non solo clic.'], size=13, gap=6)
rrect(s, 8.4, 4.7, 4.25, 1.95, PANEL)
text(s, 8.6, 4.8, 3.9, 0.35, 'Attenzione', size=13, bold=True, color='FF6B8B')
text(s, 8.6, 5.2, 3.9, 1.4, "L'Ad Library di LinkedIn è bloccata dall'ambiente di lavoro: l'analisi di myBiros è incompleta. [DA CONFERMARE]", size=12, color=GREY)

# ============================================================ SLIDE 3 — mercato e problema
s = new('Il mercato e il problema', 'Ogni giorno qualcuno ricopia a mano ordini, DDT e fatture',
        'retica.ai: testimonianza Andrea Michelin, Gruppo Borghi Spa (27/08/2026) e sezione "I nostri numeri" [VERIFICATO].')
rrect(s, 0.7, 2.0, 5.3, 4.5, PANEL)
big(s, 1.0, 2.3, 4.8, '2.500', 'ordini in PDF al mese, letti e inseriti a mano prima di Retica: "un risparmio equivalente a una persona in ufficio" (Gruppo Borghi). [VERIFICATO]', color='FF8A73', nsize=66, lsize=13, lh=1.8)
for i, (t, d) in enumerate([('Tempo', 'Operatori dedicati a ordini, DDT, fatture e conferme d\'ordine.'),
                            ('Errori', 'Più righe articolo, più rischio di errore di battitura nel gestionale.'),
                            ('Persone', 'Risorse bloccate su attività ripetitive invece che di controllo.')]):
    rrect(s, 6.4, 2.0 + i * 1.2, 6.2, 1.05, PANEL)
    text(s, 6.65, 2.1 + i * 1.2, 1.7, 0.85, t, size=18, bold=True, color=BLUE2, anchor='m')
    text(s, 8.3, 2.1 + i * 1.2, 4.2, 0.85, d, size=13, color=WHITE, anchor='m')
text(s, 6.4, 5.7, 6.2, 0.8, 'Retica oggi: 6.000+ scansioni al giorno · 124 clienti attivi · 23 rivenditori e partner [VERIFICATO]', size=13, color=GREY)

# ============================================================ SLIDE 4 — myBiros: verificato/bloccato
s = new('Analisi di myBiros su LinkedIn · 1/4', 'Cosa sappiamo di myBiros e cosa ci manca',
        'Screenshot research/mybiros/linkedin_blocco_cloudflare_19-11-2026.png; mybiros.com letto il 19/11/2026.')
rrect(s, 0.7, 2.0, 5.9, 4.6, PANEL)
text(s, 1.0, 2.15, 5.3, 0.4, 'Verificato [VERIFICATO]', size=15, bold=True)
bullets(s, 1.0, 2.7, 5.4, ['Sito mybiros.com: posizionamento, numeri, documenti e settori.',
                           'CTA: "Prenota demo" e "Parla con un esperto".',
                           'Recensioni Trustpilot mostrate in home.',
                           'Nessuna pagina LinkedIn di myBiros nei risultati di ricerca.'], size=15, gap=10)
rrect(s, 6.9, 2.0, 5.75, 4.6, PANEL)
text(s, 7.2, 2.1, 2.6, 1.2, '403', size=66, bold=True, color='FF6B8B', space=0, line=1.0)
text(s, 7.2, 3.35, 5.2, 0.8, 'Ad Library e pagina aziendale LinkedIn bloccate da Cloudflare. [VERIFICATO]', size=13, color=GREY)
bullets(s, 7.2, 4.2, 5.2, ['Annunci, formati, rotazione, impression DSA e targeting: non verificati. [DA CONFERMARE]',
                           'Non aggiriamo la protezione e non inventiamo dati: il CSV è vuoto.',
                           'Chiusura: 30–45 minuti di raccolta manuale, o un computer collegato.'], size=12, gap=5, dot='FF6B8B')

# ============================================================ SLIDE 5 — messaggi myBiros
s = new('Analisi di myBiros su LinkedIn · 2/4', 'myBiros parla di "oltre l\'OCR" a finanza, assicurazioni e utility',
        'mybiros.com (19/11/2026): numeri e settori come dichiarati da myBiros; non verificati nel merito [VERIFICATO come claim].')
for i, (n, l) in enumerate([('85%', 'tempo medio risparmiato'), ('98%', 'accuratezza media dei dati'), ('60%', 'risparmio costo operativo')]):
    rrect(s, 0.7 + i * 4.1, 2.0, 3.9, 1.7, PANEL); big(s, 1.0 + i * 4.1, 2.1, 3.4, n, l + ' (claim di myBiros)', color=BLUE2, nsize=44, lsize=12)
text(s, 0.7, 4.0, 5.5, 0.35, 'DOCUMENTI IN PRIMO PIANO', size=10, color=GREY, bold=True)
x = 0.7
for t in ['Bolletta', 'Busta paga', 'Carta d\'identità', 'Passaporto', 'Ricevuta']: x += chip(s, x, 4.4, t) + 0.12
text(s, 0.7, 5.0, 5.5, 0.35, 'SETTORI IN PRIMO PIANO', size=10, color=GREY, bold=True)
x = 0.7
for t in ['Assicurativo', 'Finanziario', 'Utility', 'Lending']: x += chip(s, x, 5.4, t) + 0.12
bullets(s, 6.7, 5.0, 6.0, ['Temi ricorrenti: "più di un OCR", AI trasparente, server europei e GDPR.', 'Retica non copia testi né claim: sfrutta lo spazio dei documenti di filiera.'], size=13)

# ============================================================ SLIDE 6 — stima investimento myBiros
s = new('Analisi di myBiros su LinkedIn · 3/4', 'Quanto investe myBiros? Senza impression reali non si può dire',
        'ZenABM (agg. 16/02/2026) e ClickMinded (agg. 08/07/2026). CPM 33,80 $ → 30,4 € e 59,15 $ → 53,2 € a cambio 0,90 [STIMA].')
rrect(s, 0.7, 2.0, 12.0, 1.0, PANEL)
text(s, 0.9, 2.05, 11.6, 0.9, 'Spesa mensile ≈ (impression al mese ÷ 1.000) × CPM    [STIMA]', size=22, bold=True, anchor='m')
rows = [['Impression al mese', 'CPM 30,4 € (Sponsored Content)', 'CPM 53,2 € (single image)'], ['50.000', '1.520 €', '2.660 €'], ['150.000', '4.560 €', '7.980 €'], ['400.000', '12.160 €', '21.280 €'], ['1.000.000', '30.400 €', '53.200 €']]
table(s, 0.7, 3.3, [3.0, 4.5, 4.5], rows, size=13, rowh=0.48)
text(s, 0.7, 5.85, 12, 0.9, 'La tabella mostra la scala, non la spesa di myBiros: le impression per annuncio (dati DSA) vanno lette in Ad Library. Nessun benchmark CPM specifico per l\'Italia trovato. [DA CONFERMARE]', size=12, color=GREY)

# ============================================================ SLIDE 7 — cosa verificare e dove inserirsi
s = new('Analisi di myBiros su LinkedIn · 4/4', 'Cosa verificare in Ad Library e dove Retica può inserirsi',
        'Checklist Propaganda Adv; spazi liberi dedotti dal sito myBiros (19/11/2026), da confermare con gli annunci.')
rrect(s, 0.7, 2.0, 5.9, 4.6, PANEL)
text(s, 1.0, 2.15, 5.3, 0.4, 'Da raccogliere in 45 minuti [DA CONFERMARE]', size=14, bold=True)
bullets(s, 1.0, 2.75, 5.4, ['Numero di annunci attivi e storici', 'Mix di formati e ritmo di rotazione', 'Lead magnet: demo, esperto, contenuti gated', 'Messaggi: numeri, prove sociali, GDPR', 'Impression, paesi e targeting dichiarato (DSA)', 'Thought Leader Ads dei fondatori'], size=15, gap=9)
rrect(s, 6.9, 2.0, 5.75, 4.6, PANEL)
text(s, 7.2, 2.15, 5.2, 0.4, 'Spazi liberi (ipotesi dal sito)', size=14, bold=True)
bullets(s, 7.2, 2.75, 5.2, ['Ordini, DDT, conferme d\'ordine: assenti dai documenti di myBiros', 'Logistica, manifattura, distribuzione e retail', 'Ruoli operativi: EDP, back office ordini, amministrazione', 'Integrazione con il gestionale e assistenza vicina'], size=15, gap=10, dot='39B54A')

# ============================================================ SLIDE 8 — posizionamento
s = new('Posizionamento', 'Dove Retica può vincere: i documenti di filiera',
        'retica.ai e mybiros.com, letti il 19/11/2026 [VERIFICATO]. Sede myBiros da idp-software.com (fonte terza). Ruoli myBiros: non verificati.')
rows = [['', 'Retica', 'myBiros'],
        ['Documenti', 'Ordini di acquisto, DDT, fatture, conferme d\'ordine, ricevute', 'Bollette, buste paga, carte d\'identità, passaporti, ricevute'],
        ['Settori', 'Logistica, manifattura, retail, servizi finanziari, HR', 'Assicurativo, finanziario, utility, lending'],
        ['Integrazione', 'CSV, XML, JSON; importazione via API o FTP', 'Esportazione e API verso ERP, CRM, RPA'],
        ['Prova sociale', '124 clienti attivi · 6.000+ scansioni al giorno', '50+ aziende clienti · 20 mln di documenti'],
        ['Vicinanza', 'Reggiolo (RE), supporto citato dai clienti', 'Roma (fonte terza)'],
        ['Ruoli target', 'IT manager, EDP, CEO nelle recensioni', '[DA CONFERMARE] in Ad Library']]
table(s, 0.7, 2.0, [2.0, 5.0, 5.0], rows, size=12, rowh=0.62)

# ============================================================ SLIDE 9 — Retica oggi
s = new('Retica oggi', 'Punti di forza e cose da sistemare prima di mandare traffico',
        'retica.ai, home letta e verificata via browser il 19/11/2026 [VERIFICATO].')
rrect(s, 0.7, 2.0, 5.9, 4.6, PANEL)
text(s, 1.0, 2.15, 5.3, 0.4, 'Punti di forza', size=15, bold=True, color='39B54A')
bullets(s, 1.0, 2.7, 5.4, ['Proposta chiara: automatizza l\'importazione di documenti sul gestionale', '6 moduli: importazione, data capture, validazione, condizioni, esportazione, analisi', 'Testimonianze 5 stelle di IT manager, EDP e CEO', 'Calcolatore del risparmio annuo e CTA "Richiedi demo"'], size=14, gap=9, dot='39B54A')
rrect(s, 6.9, 2.0, 5.75, 4.6, PANEL)
text(s, 7.2, 2.15, 5.2, 0.4, 'Da sistemare [DA CONFERMARE]', size=15, bold=True, color='FF6B8B')
bullets(s, 7.2, 2.7, 5.2, ['Menu laterale nascosto con segnaposto del template: New York, foton@qodeinteractive.com, telefono generico', 'Testi in inglese in cookie e moduli; "© 2023" nel footer', 'Nessuna landing dedicata alle campagne', 'Insight Tag e conversioni LinkedIn da installare'], size=14, gap=9, dot='FF6B8B')

# ============================================================ SLIDE 10 — pubblici
s = new('Pubblici target (Italia)', 'Chi raggiungiamo: ruoli operativi in aziende da 20 a 1.000 dipendenti',
        'Dimensione e logica di targeting: Propaganda Adv [STIMA]. Dimensione del pubblico: leggibile solo in Campaign Manager [DA CONFERMARE].')
cols = [('Funzioni', ['Operations, Supply Chain, Logistica', 'Amministrazione e Finance (CFO, ciclo passivo)', 'IT / EDP', 'Customer Service e back office ordini', 'CEO di PMI']),
        ('Settori', ['Logistica e trasporti', 'Manifattura', 'Distribuzione all\'ingrosso', 'Retail', 'Servizi finanziari'])]
for i, (h, items) in enumerate(cols):
    rrect(s, 0.7 + i * 4.1, 2.0, 3.9, 3.0, PANEL); text(s, 0.95 + i * 4.1, 2.1, 3.4, 0.4, h, size=15, bold=True, color=BLUE2)
    bullets(s, 0.95 + i * 4.1, 2.6, 3.5, items, size=11.5, gap=2)
rrect(s, 8.9, 2.0, 3.75, 3.0, PANEL); text(s, 9.15, 2.1, 3.3, 0.4, 'Dimensione 20–1.000', size=15, bold=True, color=BLUE2)
text(s, 9.15, 2.6, 3.3, 2.3, ['Sotto i 20 dipendenti il volume di documenti raramente giustifica un software.', 'Oltre 1.000, cicli di acquisto lunghi e IT più strutturato.', 'Ipotesi da validare con i dati reali dei 124 clienti.'], size=11, color=GREY, space=5)
rrect(s, 0.7, 5.2, 5.9, 1.45, PANEL); text(s, 0.95, 5.27, 5.4, 0.35, 'Matched Audiences', size=13, bold=True, color=BLUE2)
text(s, 0.95, 5.65, 5.4, 1.0, 'Visitatori del sito (Insight Tag) · elenco ABM · video visto al 50% / 75% · Lead Form aperto e non inviato · lookalike', size=11, color=GREY)
rrect(s, 6.9, 5.2, 5.75, 1.45, PANEL); text(s, 7.15, 5.27, 5.3, 0.35, 'Esclusioni', size=13, bold=True, color='FF6B8B')
text(s, 7.15, 5.65, 5.3, 1.0, 'Clienti attuali · concorrenti · rivenditori e partner (liste da fornire) [DA CONFERMARE]', size=11, color=GREY)

# ============================================================ SLIDE 11 — funnel
s = new('Architettura del funnel', 'Tre livelli: farsi notare, farsi scaricare, farsi chiamare',
        'Struttura Propaganda Adv. Frequenze e quote di budget: pratica di settore, da calibrare sui dati [STIMA].')
rows = [['', 'TOFU · Consapevolezza', 'MOFU · Considerazione', 'BOFU · Conversione'],
        ['Obiettivo', 'Visualizzazioni video · visite al sito', 'Lead generation', 'Lead generation'],
        ['Formati', 'Video 15–30 s · Thought Leader Ad', 'Document Ad gated · carosello · calcolatore', 'Lead Gen Form · Conversation Ad · testimonianze'],
        ['Pubblico', 'Ruoli e settori, freddo', 'Freddo + video visto 50% + visitatori', 'Retargeting: visitatori, form aperto, video 75%'],
        ['Budget', '15–30%', '40–50%', '30–35%'],
        ['Durata', 'Sempre attiva', '12 settimane di test', '12 settimane di test'],
        ['Frequenza target', '1–2 a settimana', '2–3 a settimana', '3–4 a settimana, con tetto']]
table(s, 0.7, 2.0, [1.9, 3.3, 3.4, 3.4], rows, size=11.5, rowh=0.6)
text(s, 0.7, 6.3, 12, 0.5, 'Annunci: A01–A02 (TOFU) · A03–A06 (MOFU) · A07–A10 (BOFU)', size=12, color=GREY)

# ============================================================ creative slides
def copyblock(s, x, y, w, a, size=10.5):
    text(s, x, y, w, 0.3, f"{a['id']} · {a['funnel']} · {a['fmt'].split('(')[0].strip()}", size=11, bold=True, color=BLUE2)
    text(s, x, y + 0.32, w, 3.3, [f"Angolo: {a['angle']}", f"Gancio: {a['hook_A']}…", f"Headline: {a['headline_A']}", f"Variante B: {a['headline_B']}", f"CTA: {a['cta']}"], size=size, color=WHITE, space=4)

def feeds(s, ids, x0=0.7, gap=0.25, h=4.75, y=1.95):
    x = x0
    for i in ids:
        w, _ = pic(s, f'{MOCK}/{i}_feed.png', x, y, h=h); x += w + gap
    return x

s = new('Proposte creative · TOFU', 'Video e Thought Leader Ad: il problema prima della soluzione',
        'Copy e mockup: output/copy_annunci.md. Claim da retica.ai; mockup illustrativi; persona del Thought Leader [DA CONFERMARE].')
x = feeds(s, ['A01', 'A02'], h=4.75)
copyblock(s, x + 0.1, 2.0, 12.65 - x - 0.1, ADS['A01'], 10); copyblock(s, x + 0.1, 4.2, 12.65 - x - 0.1, ADS['A02'], 10)

s = new('Proposte creative · MOFU', 'Document Ad gated: la guida a DDT e ordini',
        'Contenuti della guida da produrre con il cliente [DA CONFERMARE]; i 4 passi sono quelli del "Come funziona" di retica.ai [VERIFICATO].')
x = feeds(s, ['A03'], h=4.75)
x2 = x + 0.1
for i, p in enumerate(['A03_pagina1_copertina_4x5', 'A03_pagina2_4passi_4x5', 'A03_pagina3_cta_4x5']):
    pic(s, f'{MOCK}/{p}.png', x2 + i * 1.75, 2.0, h=2.15)
text(s, x2, 4.2, 5.3, 0.3, 'Le 3 pagine di anteprima', size=9, color=MUT)
copyblock(s, x2, 4.55, 12.65 - x2, ADS['A03'], 10)

s = new('Proposte creative · MOFU', 'Calcolatore del risparmio e carosello "qualsiasi layout"',
        'Calcolatore: esiste su retica.ai [VERIFICATO]; versione LinkedIn e checklist [DA CONFERMARE]. Tipi di documento dal sito.')
x = feeds(s, ['A04', 'A05'], h=4.75)
copyblock(s, x + 0.1, 2.0, 12.65 - x - 0.1, ADS['A04'], 10); copyblock(s, x + 0.1, 4.2, 12.65 - x - 0.1, ADS['A05'], 10)

s = new('Proposte creative · MOFU / BOFU', 'Integrazione con l\'ERP e caso d\'uso DDT',
        'Formati e canali (CSV, XML, JSON, API, FTP) da retica.ai [VERIFICATO]; offerta "analisi gratuita" [DA CONFERMARE].')
x = feeds(s, ['A06', 'A07'], h=4.75)
copyblock(s, x + 0.1, 2.0, 12.65 - x - 0.1, ADS['A06'], 10); copyblock(s, x + 0.1, 4.2, 12.65 - x - 0.1, ADS['A07'], 10)

s = new('Proposte creative · BOFU', 'Prova sociale: una storia vera e i numeri di Retica',
        'Testimonianza Andrea Michelin e numeri da retica.ai [VERIFICATO]; uso di nome e azienda in annuncio [DA CONFERMARE].')
x = feeds(s, ['A08', 'A09'], h=4.75)
copyblock(s, x + 0.1, 2.0, 12.65 - x - 0.1, ADS['A08'], 10); copyblock(s, x + 0.1, 4.2, 12.65 - x - 0.1, ADS['A09'], 10)

s = new('Proposte creative · BOFU', 'Conversation Ad e piano di test A/B',
        'Mittente reale e testo [DA CONFERMARE]. Piano di test: Propaganda Adv.')
w, _ = pic(s, f'{MOCK}/A10_conversation_4x5.png', 0.7, 1.95, h=4.75)
copyblock(s, 0.7 + w + 0.3, 2.0, 3.6, ADS['A10'], 10)
rrect(s, 0.7 + w + 4.1, 2.0, 12.65 - (0.7 + w + 4.1), 4.6, PANEL)
text(s, 0.7 + w + 4.3, 2.1, 3.6, 0.35, 'Test A/B', size=14, bold=True, color=BLUE2)
bullets(s, 0.7 + w + 4.3, 2.6, 12.45 - (0.7 + w + 4.3), ['Una variabile alla volta: gancio (A/B), poi immagine, poi CTA', 'Almeno 2 settimane e un numero di clic sufficiente prima di decidere', 'Si ruotano le creatività ogni 3–4 settimane per limitare la fatica da frequenza'], size=11, gap=5)

# ============================================================ SLIDE 18 — video
s = new('Strategia video', 'Tre tagli dal video del cliente: 15, 30 e 60 secondi',
        'LinkedIn: circa 79% dei video nel feed guardato senza audio (LinkedIn Marketing Solutions, 2021). Il "85%" non ha fonte primaria. Storyboard: output/storyboard_video.md.')
for i, (d, t, u) in enumerate([('15″', 'Il costo del copia-incolla', 'TOFU · hook nei primi 3 secondi'), ('30″', 'Dal documento al gestionale', 'TOFU/MOFU · i 4 step in UI'), ('60″', 'Demo guidata', 'Solo retargeting · 50–75% del video')]):
    rrect(s, 0.7 + i * 4.1, 2.0, 3.9, 2.25, PANEL); text(s, 0.95 + i * 4.1, 2.05, 3.4, 0.9, d, size=40, bold=True, color=BLUE2, space=0)
    text(s, 0.95 + i * 4.1, 3.0, 3.4, 0.4, t, size=14, bold=True); text(s, 0.95 + i * 4.1, 3.5, 3.4, 0.7, u, size=11, color=GREY)
bullets(s, 0.7, 4.55, 7.4, ['Formati: 1:1 e 4:5 per il feed, 9:16 per mobile, 16:9 per sito; specifiche da ricontrollare in Campaign Manager.', 'Sottotitoli italiani incisi: obbligatori.', 'Video del cliente: cartella vuota, durata, audio e sottotitoli [DA CONFERMARE].'], size=12.5, gap=5)
pic(s, f'{MOCK}/A01_frame1_hook_4x5.png', 8.7, 4.35, h=2.3); pic(s, f'{MOCK}/A01_frame2_flusso_4x5.png', 10.4, 4.35, h=2.3)

# ============================================================ SLIDE 19 — LGF e flusso
s = new('Lead Gen Form e flusso lead → demo', 'Un form breve, e una risposta entro 24 ore',
        'Struttura Propaganda Adv. CRM e strumento di calendario non noti [DA CONFERMARE].')
steps = [('Annuncio', 'Lead Gen Form nativo'), ('Form', 'Campi precompilati + 2 domande'), ('CRM', 'Integrazione nativa o Zapier/Make'), ('Follow-up', 'Entro 24 ore'), ('Demo', 'Prenotazione su calendario')]
for i, (a, b) in enumerate(steps):
    rrect(s, 0.7 + i * 2.5, 2.0, 2.2, 1.5, BLUE if i == 4 else PANEL)
    text(s, 0.8 + i * 2.5, 2.1, 2.0, 0.45, a, size=15, bold=True, align='c'); text(s, 0.8 + i * 2.5, 2.6, 2.0, 0.85, b, size=10.5, color=GREY if i != 4 else WHITE, align='c')
    if i < 4: text(s, 2.9 + i * 2.5, 2.4, 0.3, 0.5, '→', size=16, color=BLUE2, align='c', anchor='m')
rrect(s, 0.7, 3.8, 5.9, 2.85, PANEL); text(s, 0.95, 3.9, 5.4, 0.4, 'Campi e qualifica', size=14, bold=True, color=BLUE2)
bullets(s, 0.95, 4.4, 5.4, ['Nome, cognome, email di lavoro, azienda, ruolo', '"Quanti documenti gestisci al mese?"', '"Quale gestionale/ERP usi?"', 'Consenso privacy GDPR esplicito'], size=14, gap=6)
rrect(s, 6.9, 3.8, 5.75, 2.85, PANEL); text(s, 7.15, 3.9, 5.3, 0.4, 'Dopo l\'invio', size=14, bold=True, color=BLUE2)
bullets(s, 7.15, 4.4, 5.3, ['Thank-you page con pulsante "Prenota la demo"', 'Lead nel CRM con fonte e annuncio di origine', 'Definizione di MQL condivisa con il commerciale [DA CONFERMARE]'], size=14, gap=6)

# ============================================================ SLIDE 20 — budget
s = new('Budget: tre scenari', 'Start, Growth, Scale: da 1.500 a 5.000 € al mese di spesa media',
        'Modello analysis/budget_model.py: CPM e CTR ZenABM (2026), lead form ~10%, landing 2–5% ClickMinded; cambio 0,90 [STIMA]. Fee di agenzia escluso [DA CONFERMARE].')
hdr = ['', 'Start', 'Growth', 'Scale']
def f(n): return f'{n:,.0f}'.replace(',', '.')
rows = [hdr,
        ['Spesa media / mese', '1.500 €', '3.000 €', '5.000 €'],
        ['TOFU / MOFU / BOFU', '15% / 50% / 35%', '25% / 45% / 30%', '30% / 40% / 30%'],
        ['Impression / mese'] + [f(bud(k)['impressions']) for k in ('Start', 'Growth', 'Scale')],
        ['Clic / mese'] + [f(bud(k)['clicks']) for k in ('Start', 'Growth', 'Scale')],
        ['Lead / mese (prud.–ottim.)'] + [f"{bud(k, 'Prudente')['leads']:.0f} – {bud(k, 'Ottimistico')['leads']:.0f}  (base {bud(k)['leads']:.0f})" for k in ('Start', 'Growth', 'Scale')],
        ['Demo / mese (prud.–ottim.)'] + [f"{bud(k, 'Prudente')['demos']:.0f} – {bud(k, 'Ottimistico')['demos']:.0f}  (base {bud(k)['demos']:.1f})" for k in ('Start', 'Growth', 'Scale')],
        ['Spesa media in 12 settimane', '≈ 4.150 €', '≈ 8.300 €', '≈ 13.850 €']]
table(s, 0.7, 2.0, [3.3, 2.9, 2.9, 2.9], rows, size=11.5, rowh=0.52)
text(s, 0.7, 6.25, 12, 0.6, 'Sotto i 1.500 €/mese i volumi di impression sono scarsi (ZenABM): Start è un test del messaggio, non un canale a regime. [STIMA]', size=11.5, color=GREY)

# ============================================================ SLIDE 21 — KPI
s = new('KPI attesi', 'Quanto costa un lead e quanto una demo: ordini di grandezza [STIMA]',
        'ZenABM (16/02/2026): CPL Europa 120–150 $, lead form ~10%, CTR; ClickMinded (08/07/2026): lead form 8–15%, landing 2–5%. Ipotesi lead→demo [DA CONFERMARE].')
big(s, 0.7, 2.0, 3.0, f"€{bud('Growth')['cpl_eur']:.0f}", 'costo per lead, scenario Growth, caso base', color=BLUE2, nsize=44)
big(s, 3.9, 2.0, 3.0, f"€{bud('Growth')['cost_per_demo_eur']:.0f}", 'costo per demo, scenario Growth, caso base', color=BLUE2, nsize=44)
big(s, 7.1, 2.0, 2.9, '~10%', 'apertura→invio del Lead Gen Form (range 8–15%)', nsize=44)
big(s, 10.1, 2.0, 2.6, '0,4%', 'CTR di single image e Document Ads', nsize=44)
rows = [['KPI', 'Benchmark citato', 'Uso nel modello'],
        ['CTR', 'Single image 0,40–0,42% · Document 0,43% · video 0,24% · Thought Leader 2,68%', 'Per formato'],
        ['CPM', 'Video 38,94 $ · carosello 45,28 $ · Thought Leader 49,37 $ · single image 59,15 $', 'Per formato, ×0,90'],
        ['Lead Gen Form', '~10% medio, 15%+ alto (ZenABM) · 8–15% (ClickMinded)', '10% MOFU · 15% BOFU'],
        ['Lead → demo', 'Nessuna fonte: dati storici Retica [DA CONFERMARE]', 'MOFU 10% · BOFU 35%']]
table(s, 0.7, 3.65, [2.0, 7.2, 2.8], rows, size=11, rowh=0.6)

# ============================================================ SLIDE 22 — roadmap
s = new('Roadmap dei primi 90 giorni', 'Due settimane di setup, poi lancio, test e report ogni mese',
        'Piano Propaganda Adv. Tempi dipendono dalla consegna di accessi e materiali [DA CONFERMARE].')
phases = [('Settimane 1–2', 'Setup', ['Insight Tag e conversioni', 'Pubblici e liste ABM', 'Lead Gen Form e CRM', 'Landing e footer del sito']),
          ('Settimane 3–4', 'Lancio', ['TOFU e MOFU attivi', 'BOFU appena i pubblici sono sufficienti', 'Controllo del tracciamento']),
          ('Settimane 5–8', 'Test A/B', ['Gancio, immagine, CTA', 'Prima lettura di CPL e qualità lead', 'Rotazione creatività']),
          ('Settimane 9–12', 'Ottimizzazione', ['Budget verso ciò che porta demo', 'Report mensile con costo per demo', 'Decisione sullo scenario'])]
for i, (w, t, items) in enumerate(phases):
    x = 0.7 + i * 3.05
    box(s, x, 2.1, 2.9, 0.08, BLUE if i == 0 else BLUE2)
    text(s, x, 2.25, 2.9, 0.3, w.upper(), size=10, bold=True, color=GREY); text(s, x, 2.55, 2.9, 0.5, t, size=20, bold=True)
    rrect(s, x, 3.2, 2.9, 3.3, PANEL); bullets(s, x + 0.2, 3.4, 2.55, items, size=13, gap=8)

# ============================================================ SLIDE 23 — cosa serve
s = new('Cosa serve da Retica', 'Dodici cose per partire',
        'Elenco completo con motivazioni in output/note_da_confermare.md.')
items = ['Video originali e diritti d\'uso [DA CONFERMARE]', 'Accesso a Campaign Manager e alla Pagina LinkedIn [DA CONFERMARE]', 'Quale CRM usate e chi fa il follow-up in 24 ore [DA CONFERMARE]', 'Footer e menu del sito: via i segnaposto [DA CONFERMARE]',
         'Lead magnet: guida, checklist, calcolatore LinkedIn [DA CONFERMARE]', 'Persona per il Thought Leader Ad [DA CONFERMARE]', 'Consenso a usare testimonianze e nomi [DA CONFERMARE]', 'Liste: ABM, clienti, partner, concorrenti [DA CONFERMARE]',
         'Budget scelto e fee di agenzia [DA CONFERMARE]', 'Dati storici: chiusura demo, valore contratto [DA CONFERMARE]', 'Definizione di MQL e di demo fissata [DA CONFERMARE]', 'Accesso all\'Ad Library per myBiros [DA CONFERMARE]']
for i, it in enumerate(items):
    c, r = i // 6, i % 6
    rrect(s, 0.7 + c * 6.1, 2.0 + r * 0.78, 5.9, 0.68, PANEL); text(s, 0.95 + c * 6.1, 2.0 + r * 0.78, 5.5, 0.68, f'{i + 1}.  ' + it, size=11.5, anchor='m')

# ============================================================ SLIDE 24 — prossimi passi
s = new('Prossimi passi e contatti', 'Dal sì al primo lead in circa quattro settimane',
        'Contatti da propagandaadv.com (19/11/2026) [VERIFICATO]. Tempistica indicativa [STIMA].')
for i, (a, b) in enumerate([('1', 'Scegliete lo scenario di budget'), ('2', 'Ci inviate accessi e materiali'), ('3', 'Setup e approvazione degli annunci'), ('4', 'Lancio e report mensile')]):
    rrect(s, 0.7, 2.0 + i * 1.1, 6.6, 0.95, PANEL); text(s, 0.95, 2.0 + i * 1.1, 0.7, 0.95, a, size=30, bold=True, color=BLUE2, anchor='m')
    text(s, 1.75, 2.0 + i * 1.1, 5.4, 0.95, b, size=15, anchor='m')
rrect(s, 7.7, 2.0, 4.95, 4.2, BLUE)
text(s, 8.0, 2.2, 4.4, 3.9, [('Propaganda Adv', {'size': 20, 'bold': True}), ('Giovanni Bertoni', {'size': 13}), 'info@propagandaadv.com', 'commerciale@propagandaadv.com', '+39 351 397 3029', 'Via Giacomo Matteotti 102/e', '42046 Reggiolo (RE)', 'propagandaadv.com'], size=13, space=8)

# ============================================================ SLIDE 25 — fonti
s = new('Appendice', 'Fonti e metodo dei numeri', None)
bullets(s, 0.7, 2.0, 11.9, [
    '[VERIFICATO] retica.ai (home, testimonianze, numeri, codice della pagina) e mybiros.com, letti il 19/11/2026.',
    '[VERIFICATO] LinkedIn Ad Library e pagina aziendale myBiros: bloccate da Cloudflare (screenshot in research/mybiros/).',
    '[STIMA] Benchmark CPM, CTR, lead form: ZenABM "LinkedIn Ads Benchmarks: Real Data from 211 B2B Companies in 2026" (16/02/2026) e ClickMinded "LinkedIn Ads Benchmarks 2026" (08/07/2026). Sono articoli di agenzie, valori globali o EMEA: nessun dato specifico Italia.',
    '[STIMA] Cambio USD→EUR 0,90 e tassi di conversione lead→MQL→demo: ipotesi del modello, da sostituire con dati reali.',
    '[STIMA] 79% di video guardati senza audio: LinkedIn Marketing Solutions (2021). Il dato "85%" non ha una fonte primaria.',
    'Calcoli riproducibili: python3 analysis/budget_model.py. Testi e limiti di caratteri: analysis/ads_data.py.'], size=12.5, gap=8)

out = f'{ROOT}/output/Retica_LinkedIn_Ads_Proposta.pptx'
prs.save(out); print('salvato', out, state['n'], 'slide')
