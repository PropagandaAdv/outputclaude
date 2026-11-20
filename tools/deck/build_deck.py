# -*- coding: utf-8 -*-
"""Genera output/Retica_LinkedIn_Ads_Proposta.pptx: stessa presentazione del deck Claude (15 slide),
stile Propaganda Adv: blu #233DFF / nero / bianco, Poppins. Piano da 2.000 €/mese, niente video, niente lead magnet.
Coordinate in pixel su una tela 1920x1080 (1 px = 0,5 pt). Le note dell'oratore sono prese dai tag <aside> delle slide."""
import json, re, os
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
DECK = f'{ROOT}/tools/claude-deck/project'
MOCK = f'{ROOT}/output/mockup'
AS = f'{ROOT}/assets/propaganda/deck'
BUD = json.load(open(f'{ROOT}/analysis/budget_results.json'))['results']

BLUE, BLACK, WHITE, PAPER, LINE, SOFT, GREY, DGREY = '233DFF', '000000', 'FFFFFF', 'F9F7F3', 'E6E3DD', 'F1F2FF', '5E5E5E', '3D3D3D'
PX = 6350  # EMU per px (13,333in / 1920)

prs = Presentation(); prs.slide_width = Emu(1920 * PX); prs.slide_height = Emu(1080 * PX)
BLANK = prs.slide_layouts[6]

def rgb(h): return RGBColor.from_string(h)
def E(v): return Emu(int(v * PX))

def rect(s, x, y, w, h, fill=None, line=None, r=None, lw=2):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if r else MSO_SHAPE.RECTANGLE, E(x), E(y), E(w), E(h))
    if r: sh.adjustments[0] = min(0.5, r / min(w, h))
    if fill: sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    else: sh.fill.background()
    if line: sh.line.color.rgb = rgb(line); sh.line.width = Pt(lw)
    else: sh.line.fill.background()
    sh.shadow.inherit = False
    return sh

def fontname(weight):
    return {'light': 'Poppins Light', 'reg': 'Poppins', 'semi': 'Poppins SemiBold', 'bold': 'Poppins'}[weight]

def text(s, x, y, w, h, paras, size=30, color=BLACK, weight='reg', align='l', anchor='t', lh=1.35, after=0, spacing=None):
    """paras: str o lista; '**x**' = grassetto, '{x}' = blu semibold (accento)."""
    tb = s.shapes.add_textbox(E(x), E(y), E(w), E(h)); tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {'t': MSO_ANCHOR.TOP, 'm': MSO_ANCHOR.MIDDLE, 'b': MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(paras, str): paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {'l': PP_ALIGN.LEFT, 'c': PP_ALIGN.CENTER, 'r': PP_ALIGN.RIGHT}[align]
        p.line_spacing = lh; p.space_after = Pt(after * 0.5)
        for part in re.split(r'(\*\*.*?\*\*)', para):
            if not part: continue
            bold = part.startswith('**'); t = part.strip('*') if bold else part
            r = p.add_run(); r.text = t; f = r.font
            f.size = Pt(size * 0.5); f.color.rgb = rgb(color)
            f.name = fontname('bold' if bold else weight); f.bold = bool(bold) or weight == 'bold'
            if spacing:
                r._r.get_or_add_rPr().set('spc', str(int(spacing * 50)))  # px -> centesimi di pt
    return tb

def pic(s, path, x, y, w=None, h=None):
    im = Image.open(path); iw, ih = im.size
    if w and h:  # contiene (object-fit: contain)
        sc = min(w / iw, h / ih); pw, ph = iw * sc, ih * sc
        x += (w - pw) / 2; y += (h - ph) / 2; w, h = pw, ph
    elif w: h = w * ih / iw
    else: w = h * iw / ih
    return s.shapes.add_picture(path, E(x), E(y), E(w), E(h))

def aside(name):
    t = open(f'{DECK}/slides/{name}.html', encoding='utf8').read()
    m = re.search(r'<aside>(.*?)</aside>', t, re.S)
    return re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else ''

def new(name, kind='blue', kicker=None, title=None, size=88, sub=None):
    s = prs.slides.add_slide(BLANK)
    light = kind == 'light'
    bg = s.background.fill; bg.solid(); bg.fore_color.rgb = rgb(PAPER if light else BLUE)
    fg = BLACK if light else WHITE
    pic(s, f'{AS}/logo_blu.png' if light else f'{AS}/logo_bianco.png', 1612, 48, w=180)
    if kicker:
        rect(s, 128, 126, 56, 4, BLUE if light else WHITE)
        text(s, 204, 112, 1200, 36, kicker.upper(), size=24, color=fg, weight='semi', spacing=4)
    if title:
        text(s, 128, 178, 1664, size * 1.1 * (title.count('\n') + 1), title.split('\n'), size=size, color=fg, weight='light', lh=1.04, spacing=-2)
    s.notes_slide.notes_text_frame.text = aside(name)
    s.light = light
    return s

def foot(s, txt):
    text(s, 128, 1000, 1664, 40, txt, size=22, color=GREY if s.light else WHITE, weight='light', anchor='b', lh=1.2)

def card(s, x, y, w, h, hl=False, light=True):
    if light: return rect(s, x, y, w, h, SOFT if hl else WHITE, BLUE if hl else LINE, r=28)
    return rect(s, x, y, w, h, WHITE, BLUE if hl else WHITE, r=28)

def badge(s, x, y, n):
    rect(s, x, y, 64, 64, BLUE, r=16)
    text(s, x, y, 64, 64, n, size=26, color=WHITE, weight='bold', align='c', anchor='m', lh=1)

def chip(s, x, y, w, label, kind='ok'):
    fill, fg, ln = {'ok': (BLUE, WHITE, None), 'st': (SOFT, BLUE, BLUE), 'cf': (BLACK, WHITE, None)}[kind]
    rect(s, x, y, w, 52, fill, ln, r=26)
    text(s, x, y, w, 52, label, size=24, color=fg, weight='semi', align='c', anchor='m', lh=1)

# ---------------------------------------------------------------- 1 cover
s = new('cover', 'blue')
pic(s, f'{AS}/logo_retica_chiaro.png', 128, 112, h=70)
text(s, 128, 300, 1300, 40, 'MARKETING CHE PORTA CLIENTI.', size=24, weight='semi', color=WHITE, spacing=4)
text(s, 128, 360, 1500, 260, ['Più demo per Retica,', 'da LinkedIn.'], size=100, weight='light', color=WHITE, lh=1.04, spacing=-2)
text(s, 128, 680, 1100, 130, 'Un piano per portare aziende di logistica a chiedere una dimostrazione.', size=32, weight='light', color=WHITE, lh=1.45)
text(s, 128, 980, 1500, 40, 'Novembre 2026 · Documento preliminare: nessuna campagna è ancora attiva.', size=24, weight='light', color=WHITE)

# ---------------------------------------------------------------- 2 piano
s = new('piano', 'light', '01 · Il piano', '**Tre mosse,** una demo.')
text(s, 128, 296, 1500, 50, 'Accompagniamo chi lavora in logistica dal primo sguardo fino alla richiesta di demo.', size=32, weight='light', color=DGREY, lh=1.4)
cards = [('01', 'Ci notano', 'Due annunci di Retica parlano del loro problema di tutti i giorni: riscrivere i DDT a mano.'),
         ('02', 'Ci contattano', 'Proponiamo di risolvere il loro problema in modo semplice.'),
         ('03', 'Ci chiamano', 'Un modulo di due domande, una demo prenotata e una risposta entro 24 ore.')]
for i, (n, h, p) in enumerate(cards):
    x = 128 + i * 560
    card(s, x, 430, 520, 460, hl=(i == 2)); badge(s, x + 40, 470, n)
    text(s, x + 40, 570, 440, 60, h, size=38, weight='semi', lh=1.2)
    text(s, x + 40, 640, 440, 220, p, size=28, color=DGREY, lh=1.45)

# ---------------------------------------------------------------- 3 problema
s = new('problema', 'blue', '02 · Il problema', 'In logistica, i **DDT**\nsi riscrivono ancora a mano.')
rows = [('01', 'DDT', 'Righe, codici e quantità copiati a mano nel gestionale.', 'Retica li legge e li inserisce.'),
        ('02', 'Unità di misura', 'Colli, pezzi, pallet: ogni fornitore li scrive a modo suo.', 'Retica li converte automaticamente'),
        ('03', 'Listini e prezzi', 'I prezzi arrivano in PDF e vanno portati nel gestionale.', 'Retica li controlla')]
for i, (n, h, p, r_) in enumerate(rows):
    x = 128 + i * 560
    card(s, x, 520, 520, 420, light=False); badge(s, x + 40, 556, n)
    text(s, x + 40, 650, 440, 56, h, size=38, weight='semi', lh=1.2)
    text(s, x + 40, 716, 440, 110, p, size=26, color=DGREY, lh=1.4)
    text(s, x + 40, 836, 440, 90, r_, size=26, color=BLUE, weight='semi', lh=1.35)
foot(s, 'Fonte: retica.ai/logistica, articolo di Retica sui listini fornitori, testimonianze Carraro e Le Messaggerie Nazionali')

# ---------------------------------------------------------------- 4 concorrente
s = new('concorrente', 'light', '03 · Il concorrente', 'La **logistica**\nè ancora libera.')
text(s, 128, 440, 880, 130, 'myBiros ha 35 annunci su LinkedIn. Ne abbiamo letti 25: nessuno parla di DDT, listini o logistica.', size=30, weight='light', color=DGREY, lh=1.45)
stats = [('20', 'sul credito, il tema principale'), ('5', 'sull’utility: bollette e attivazioni'), ('0', 'sulla logistica')]
for i, (n, t) in enumerate(stats):
    y = 600 + i * 120
    text(s, 128, y, 190, 100, n, size=84, weight='bold', color=BLACK if i < 2 else BLUE, lh=1, spacing=-2, anchor='m')
    text(s, 330, y, 700, 100, t, size=28, color=DGREY, anchor='m', lh=1.3)
pic(s, f'{AS}/MB-03.png', 1130, 300, w=300, h=620)
pic(s, f'{AS}/MB-05.png', 1470, 300, w=300, h=620)
text(s, 1130, 930, 640, 40, 'Dall’Ad Library · annunci letti: 25 su 35', size=22, color=GREY, align='c')
foot(s, 'Fonte: LinkedIn Ad Library, pagina myBiros, 19/11/2026')

# ---------------------------------------------------------------- 5 concorrente-come
s = new('concorrente-come', 'blue', '03 · Il concorrente', 'Cosa **dicono,** cosa no.')
rows = [('01', 'Una promessa sola', '«Time-to-Yes»: arrivare prima al sì del credito. Numeri forti: fino a 5x più veloce, −70% di tempi, −40% di costi.'),
        ('02', 'Un’esca sola', 'Un «one-pager» da scaricare e il pulsante «Scopri come». Pochi visual, riusati con testi diversi. Oltre metà sono Document Ad.'),
        ('03', 'Cosa non si vede', 'Nessun cliente citato, nessun video, nessuna demo come invito diretto. Date e diffusione: da guardare nelle schede.')]
for i, (n, h, p) in enumerate(rows):
    x = 128 + i * 560
    card(s, x, 400, 520, 520, light=False); badge(s, x + 40, 440, n)
    text(s, x + 40, 540, 440, 60, h, size=38, weight='semi', lh=1.2)
    text(s, x + 40, 616, 440, 280, p, size=28, color=DGREY, lh=1.45)
foot(s, 'I numeri sono dichiarati da myBiros e non verificati. Fonte: LinkedIn Ad Library, 19/11/2026 (25 annunci su 35)')

# ---------------------------------------------------------------- 6 pubblico
s = new('pubblico', 'blue', '04 · A chi parliamo', 'Chi gestisce\n**DDT e listini.**')
pic(s, f'{AS}/grid_panel.jpg', 1400, 0, h=1080)
rows = [('Le persone', 'Responsabili di magazzino e logistica, ufficio acquisti, amministrazione, IT e titolari di PMI.'),
        ('I settori', 'Solo logistica, trasporti e magazzino all’inizio: con 2.000 € al mese restiamo concentrati. Distribuzione e manifattura, più avanti.'),
        ('Le dimensioni', 'Aziende da 20 a 1.000 dipendenti: sotto i 20, il volume di DDT raramente giustifica un software.')]
for i, (h, p) in enumerate(rows):
    y = 520 + i * 170
    rect(s, 128, y, 1180, 150, WHITE, r=24)
    text(s, 168, y, 300, 150, h, size=30, weight='semi', color=BLUE, anchor='m')
    text(s, 480, y, 800, 150, p, size=26, color=DGREY, anchor='m', lh=1.35)
# il logo resta sopra l'immagine: lo ridisegniamo
pic(s, f'{AS}/logo_bianco.png', 1612, 48, w=180)

# ---------------------------------------------------------------- 7 strategia
s = new('strategia', 'light', '05 · La strategia', '**Concentrati** sulla demo.')
text(s, 128, 296, 1300, 110, 'Con 2.000 € al mese niente video e niente contenuti da scaricare: si passa dalla fiducia alla richiesta di demo.', size=32, weight='light', color=DGREY, lh=1.45)
cards = [('01', 'Farsi notare', 'Due annunci della pagina Retica, sui DDT e sulle unità di misura, per chi lavora in logistica e ancora non ci conosce.', '500 € al mese'),
         ('02', 'Convincere', 'Un carosello da leggere nel feed e come Retica si collega al gestionale, per chi ci ha già visti o è venuto sul sito.', '300 € al mese'),
         ('03', 'Chiedere la demo', 'Annunci con un modulo di due domande e le testimonianze di Carraro e Le Messaggerie Nazionali.', '1.200 € al mese')]
for i, (n, h, p, c) in enumerate(cards):
    x = 128 + i * 560
    card(s, x, 440, 520, 520, hl=(i == 2)); badge(s, x + 40, 476, n)
    text(s, x + 40, 570, 440, 60, h, size=38, weight='semi', lh=1.2)
    text(s, x + 40, 640, 440, 220, p, size=26, color=DGREY, lh=1.4)
    chip(s, x + 40, 880, 260, c)
foot(s, 'Ripartizione: 25% notorietà, 15% considerazione, 60% richiesta di demo. Stima Propaganda Adv')

# ---------------------------------------------------------------- 8 ads-notare
s = new('ads-notare', 'light', '06 · Gli annunci · 1 di 3', '**Prima** ci notano.', size=80)
pic(s, f'{MOCK}/A01_feed.png', 128, 330, w=400, h=640)
pic(s, f'{MOCK}/A02_feed.png', 568, 330, w=420, h=640)
for i, (lab, q) in enumerate([('ANNUNCIO · IMMAGINE', '«Quante righe di DDT ricopia il tuo team ogni giorno?»'),
                              ('ANNUNCIO · UNITÀ DI MISURA', '«10 colli o 120 pezzi? Ogni fornitore scrive l’unità di misura a modo suo.»')]):
    y = 350 + i * 270
    card(s, 1060, y, 732, 240)
    text(s, 1100, y + 34, 660, 36, lab, size=24, weight='semi', color=BLUE, spacing=3)
    text(s, 1100, y + 84, 660, 140, q, size=34, weight='semi', lh=1.3)
text(s, 1060, 900, 732, 50, 'Parliamo del problema, non del prodotto.', size=28, color=DGREY)

# ---------------------------------------------------------------- 9 ads-convincere
s = new('ads-convincere', 'blue', '06 · Gli annunci · 2 di 3', 'Poi li **convinciamo.**', size=80)
items = [('A05_feed.png', 'Carosello da leggere nel feed: il DDT, riga per riga'),
         ('A04_feed.png', 'Listini fornitori: dal PDF al gestionale'),
         ('A06_feed.png', 'Dal DDT al tuo ERP, senza trascrizioni')]
for i, (f, cap) in enumerate(items):
    x = 128 + i * 560
    pic(s, f'{MOCK}/{f}', x, 320, w=520, h=560)
    text(s, x, 895, 520, 90, cap, size=24, align='c', lh=1.35)
foot(s, 'Nessun contenuto da scaricare: tutto si legge nel feed')

# ---------------------------------------------------------------- 10 ads-chiamare
s = new('ads-chiamare', 'light', '06 · Gli annunci · 3 di 3', 'Infine **chiedono** la demo.', size=80)
items = [('A07_feed.png', 'Vedi Retica sui tuoi DDT: richiedi la demo'),
         ('A08_feed.png', 'Carraro: DDT nell’ERP, meno tempo e meno errori'),
         ('A09_feed.png', 'Le Messaggerie Nazionali: meno data entry')]
for i, (f, cap) in enumerate(items):
    x = 128 + i * 560
    pic(s, f'{MOCK}/{f}', x, 320, w=520, h=560)
    text(s, x, 895, 520, 90, cap, size=24, color=DGREY, align='c', lh=1.35)
foot(s, 'Un modulo breve, nessun contenuto da scaricare. Nomi e testimonianze: serve il permesso dei clienti')

# ---------------------------------------------------------------- 11 richiesta
s = new('richiesta', 'blue', '07 · Dalla richiesta alla demo', 'Una **risposta** entro 24 ore.')
steps = [('01', 'Annuncio', 'Chi è interessato tocca «Richiedi demo».'),
         ('02', 'Modulo', 'Nome, mail e azienda già pronti, più due domande: quanti DDT al mese e quale gestionale.'),
         ('03', 'CRM', 'La richiesta arriva subito al vostro CRM.'),
         ('04', 'Richiamo', 'Un commerciale risponde entro 24 ore.'),
         ('05', 'Demo', 'Una dimostrazione sui loro documenti.')]
for i, (n, h, p) in enumerate(steps):
    x = 128 + i * 335
    card(s, x, 400, 311, 520, hl=(i == 4), light=False); badge(s, x + 28, 436, n)
    text(s, x + 28, 530, 260, 50, h, size=34, weight='semi', lh=1.2)
    text(s, x + 28, 596, 260, 300, p, size=24, color=DGREY, lh=1.4)
foot(s, 'Il CRM di Retica e chi richiama: da confermare. Nessun contenuto da scaricare in cambio dei dati')

# ---------------------------------------------------------------- 12 budget
s = new('budget', 'light', '08 · L’investimento', 'Tutto su **2.000 €** al mese.')
nums = [('circa 8', 'richieste di demo al mese', False), ('2–3', 'demo svolte al mese', True), ('5.500 €', 'spesi in 12 settimane', False)]
for i, (n, l, hl) in enumerate(nums):
    x = 128 + i * 560
    card(s, x, 330, 520, 250, hl=hl)
    text(s, x + 40, 360, 440, 110, n, size=84, weight='bold', color=BLACK, lh=1, spacing=-2, anchor='m')
    text(s, x + 40, 490, 440, 70, l, size=28, color=DGREY, lh=1.3)
chip(s, 128, 616, 140, 'Stima', 'st')
text(s, 292, 616, 1500, 52, 'Valori medi. Richieste da 4 a 14, demo da 1 a 5. Compenso dell’agenzia escluso.', size=26, color=DGREY, anchor='m')
card(s, 128, 710, 1664, 220)
text(s, 168, 738, 1500, 50, 'Cosa non facciamo ora', size=32, weight='semi')
text(s, 168, 800, 1580, 110, 'Video e contenuti da scaricare: li valutiamo dopo i primi mesi. Con questi numeri servono 3–4 mesi per capire cosa funziona.', size=26, color=DGREY, lh=1.4)
foot(s, 'Stime da benchmark 2026 (ZenABM, ClickMinded). Da richiesta a demo svolta: ipotesi 35%, da verificare')

# ---------------------------------------------------------------- 13 roadmap
s = new('roadmap', 'blue', '09 · I primi 90 giorni', 'Si parte in **due settimane.**')
pic(s, f'{AS}/stairs.jpg', 1500, 380, h=700)
phases = [('SETTIMANE 1–2', 'Prepariamo tutto', 'Tracciamento, pubblici, moduli, CRM e pagina sul sito.'),
          ('SETTIMANE 3–4', 'Partiamo', 'Due annunci di notorietà, poi la richiesta di demo.'),
          ('SETTIMANE 5–8', 'Rinforziamo', 'Retargeting per chi ci ha già visti. Due messaggi a confronto.'),
          ('SETTIMANE 9–12', 'Puntiamo sul meglio', 'Più budget dove arrivano le demo. Report ogni mese. Valutiamo il video.')]
for i, (lab, h, p) in enumerate(phases):
    x = 128 + (i % 2) * 640; y = 340 + (i // 2) * 320
    card(s, x, y, 600, 290, light=False)
    text(s, x + 36, y + 32, 520, 36, lab, size=24, weight='semi', color=BLUE, spacing=3)
    text(s, x + 36, y + 84, 530, 56, h, size=34, weight='semi', lh=1.2)
    text(s, x + 36, y + 150, 530, 120, p, size=26, color=DGREY, lh=1.4)
foot(s, 'I tempi dipendono da accessi e materiali di Retica')

# ---------------------------------------------------------------- 14 servono
s = new('servono', 'light', '10 · Cosa ci serve', 'Sei cose **da Retica** per partire.')
items = ['Chi approva testi e immagini degli annunci di Retica', 'L’accesso a LinkedIn e al vostro CRM', 'Un sito pulito: via i testi di prova dal menu',
         'Il via libera a citare Carraro e Le Messaggerie Nazionali', '2.000 €: al mese o in totale? Per quanto tempo?', None]
for i, t in enumerate(items):
    x = 128 + (i % 3) * 560; y = 380 + (i // 3) * 290
    key = t is None
    card(s, x, y, 520, 260, hl=key); badge(s, x + 40, y + 36, f'{i + 1:02d}')
    if key:
        text(s, x + 120, y + 48, 380, 36, 'DOMANDA CHIAVE', size=22, weight='semi', color=BLUE, spacing=3)
        t = 'Retica converte le unità di misura e controlla i prezzi?'
    text(s, x + 40, y + 120, 440, 130, t, size=28, weight='semi', lh=1.3)
foot(s, 'L’elenco completo è nel file note_da_confermare.md')

# ---------------------------------------------------------------- 15 prossimi
s = new('prossimi', 'blue')
text(s, 128, 330, 1300, 36, 'MARKETING CHE PORTA CLIENTI.', size=24, weight='semi', spacing=4, color=WHITE)
text(s, 128, 390, 1500, 150, 'Partiamo?', size=120, weight='light', lh=1.04, spacing=-2, color=WHITE)
text(s, 128, 580, 1200, 150, 'Confermiamo i 2.000 € al mese e partiamo: la prima richiesta di demo arriva in circa quattro settimane.', size=32, weight='light', lh=1.45, color=WHITE)
rect(s, 128, 780, 420, 90, WHITE, r=14)
text(s, 128, 780, 420, 90, 'Scriviamoci →', size=30, color=BLUE, weight='semi', align='c', anchor='m', lh=1)
text(s, 600, 780, 1000, 90, ['Giovanni Bertoni · Propaganda Adv', 'commerciale@propagandaadv.com · +39 351 397 3029'], size=26, weight='light', anchor='m', lh=1.4, color=WHITE)

out = f'{ROOT}/output/Retica_LinkedIn_Ads_Proposta.pptx'
prs.save(out); print('ok', out, len(prs.slides._sldIdLst), 'slide')
