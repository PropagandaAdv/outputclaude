#!/usr/bin/env python3
"""
save_apollo_search.py
Imposta su Apollo.io (#/people) la ricerca "Rossini - OW/Buyer", la salva e
stampa i conteggi Total / Net New.

ZERO CREDITI: lo script non clicca mai su Access email / Save contatto /
checkbox di selezione / Export. Ogni click passa da safe_click(), che rifiuta
elementi con testi vietati o contenuti dentro la tabella dei risultati.
"""
import re
import sys
from pathlib import Path

from playwright.sync_api import TimeoutError as PWTimeout
from playwright.sync_api import sync_playwright

APOLLO_URL = "https://app.apollo.io/#/people"
PROFILE_DIR = "./apollo_chrome_profile"
SEARCH_NAME = "Rossini - OW/Buyer"
SCREENSHOT = "rossini_search_saved.png"

JOB_TITLES = ["Owner", "Co-Owner", "Founder", "Co-Founder", "Proprietario", "Titolare",
              "Fondatore", "Gérant", "Inhaber", "Buyer", "Fashion Buyer", "Senior Buyer",
              "Head of Buying", "Buying Director", "Buying Manager", "Chief Buying Officer",
              "Responsabile Acquisti", "Acheteur", "Einkäufer"]

KEYWORDS_INCLUDE = ["multi-brand", "multibrand", "multi-brand boutique", "concept store",
                    "luxury concept store", "luxury retail", "luxury fashion", "luxury boutique",
                    "designer fashion", "contemporary fashion", "ready-to-wear", "luxury footwear",
                    "designer shoes", "shoe boutique", "department store", "luxury department store",
                    "boutique di lusso", "abbigliamento multimarca", "alta moda", "calzature",
                    "prêt-à-porter", "mode de luxe", "chaussures", "grand magasin", "Modehaus",
                    "Schuhhaus", "Luxusmode", "Kaufhaus"]

KEYWORDS_EXCLUDE = ["manufacturer", "wholesale", "factory", "textile", "private label", "B2B",
                    "second hand", "vintage", "outlet", "fast fashion"]

INDUSTRIES = ["Retail", "Apparel & Fashion", "Luxury Goods & Jewelry"]
LOOKALIKES = ["tessabit.com", "apropos-store.com", "giglio.com", "michardardillier.com",
              "galerieslafayette.com"]
LOCATIONS = ["Italy", "France", "Germany", "Switzerland"]

# Apollo usa fasce fisse (1-10, 11-20, 21-50, 51-100, 101-200, 201-500, 501-1000,
# 1001-2000, 2001-5000...). Se l'etichetta esatta non esiste, si selezionano le fasce che la compongono.
EMPLOYEE_RANGES = {
    "11-50": ["11-20", "21-50"],
    "51-200": ["51-100", "101-200"],
    "201-1000": ["201-500", "501-1000"],
    "1001-5000": ["1001-2000", "2001-5000"],
}

EXCLUDE_COMPANIES = ["michardardillier.com", "popandshoes.com", "upper-shoes.com",
                     "apropos-store.com", "jades24.com", "tessabit.com", "eleonorabonucci.com",
                     "giglio.com", "sorelleramonda.com", "spinnakerboutique.com", "tretter.com",
                     "globus.ch", "lagriffeausoni.ch", "galerieslafayette.com"]

# --- Guardia anti-crediti -------------------------------------------------
FORBIDDEN = re.compile(
    r"access\s+(email|mobile|phone)|export|unlock|reveal|get\s+(email|phone)|"
    r"add\s+to\s+(list|sequence)|save\s+(contact|to\s+list)|enrich|\bemail\b.*\bcredit",
    re.I)

results = {}  # step -> "ok" / messaggio


def safe_click(loc, what=""):
    """Click solo se l'elemento non è pericoloso e non sta nella tabella risultati."""
    el = loc.first
    el.wait_for(state="visible", timeout=5000)
    text = (el.inner_text(timeout=2000) or "") + " " + (el.get_attribute("aria-label") or "")
    if FORBIDDEN.search(text):
        raise RuntimeError(f"BLOCCATO (rischio crediti): {what or text.strip()!r}")
    in_table = el.evaluate("e => !!e.closest('table, [role=grid], [role=row], tbody')")
    if in_table:
        raise RuntimeError(f"BLOCCATO (dentro la tabella risultati): {what or text.strip()!r}")
    el.click(timeout=5000)


def step(name):
    def deco(fn):
        def wrapper(*a, **k):
            try:
                fn(*a, **k)
                results[name] = "ok"
                print(f"[OK]   {name}")
            except Exception as e:  # fallback: si prosegue senza errori fatali
                results[name] = f"SALTATO: {str(e).splitlines()[0][:120]}"
                print(f"[SKIP] {name} -> {results[name]}")
        return wrapper
    return deco


# --- Login ----------------------------------------------------------------
def is_login_screen(page):
    if re.search(r"/login|/sign-?in", page.url, re.I):
        return True
    try:
        return page.locator("input[type=password]").first.is_visible(timeout=1500)
    except PWTimeout:
        return False


def ensure_logged_in(page):
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2500)
    if is_login_screen(page):
        input("Effettua il login manuale su Apollo nella finestra del browser, "
              "poi premi INVIO qui nel terminale per continuare...")
        page.goto(APOLLO_URL)
        page.wait_for_timeout(3000)
        if is_login_screen(page):
            sys.exit("Login non riuscito: riesegui lo script dopo aver effettuato l'accesso.")


# --- Helper sidebar ---------------------------------------------------------
def sidebar(page):
    return page.locator("[data-cy='filters-sidebar'], [class*='filters'], aside").first


def open_section(page, names):
    """Espande la sezione filtro (prova più etichette). Ritorna True se trovata."""
    for n in ([names] if isinstance(names, str) else names):
        hdr = page.get_by_text(re.compile(rf"^\s*{re.escape(n)}\s*$", re.I)).first
        try:
            hdr.wait_for(state="visible", timeout=3000)
        except PWTimeout:
            continue
        safe_click(hdr, f"sezione {n}")
        page.wait_for_timeout(500)
        return True
    return False


def find_input(page, placeholders):
    for p in placeholders:
        loc = page.get_by_placeholder(re.compile(p, re.I)).first
        try:
            loc.wait_for(state="visible", timeout=2500)
            return loc
        except PWTimeout:
            continue
    return None


def type_and_pick(page, inp, value, dropdown=True, enter_fallback=True):
    """Scrive il valore e sceglie l'opzione corrispondente dal dropdown dinamico."""
    inp.click()
    inp.fill("")
    inp.type(value, delay=25)
    page.wait_for_timeout(900)
    if dropdown:
        opt = page.get_by_role("option", name=re.compile(rf"^\s*{re.escape(value)}\s*$", re.I)).first
        try:
            opt.wait_for(state="visible", timeout=2500)
            safe_click(opt, f"opzione {value}")
            return True
        except PWTimeout:
            pass
        # fallback: voce del menu con testo uguale (non dentro la tabella)
        alt = page.locator("[role=listbox] *, [class*='dropdown'] *, [class*='menu'] *").get_by_text(
            re.compile(rf"^\s*{re.escape(value)}\s*$", re.I)).first
        try:
            alt.wait_for(state="visible", timeout=1500)
            safe_click(alt, f"voce {value}")
            return True
        except PWTimeout:
            pass
    if enter_fallback:
        inp.press("Enter")
        return True
    return False


def fill_multi(page, section, placeholders, values, dropdown=True):
    if not open_section(page, section):
        raise RuntimeError(f"sezione {section} non visibile")
    inp = find_input(page, placeholders)
    if inp is None:
        raise RuntimeError("campo di input non trovato")
    missed = [v for v in values if not type_and_pick(page, inp, v, dropdown)]
    if missed:
        print(f"       valori non confermati: {missed}")
    page.wait_for_timeout(600)


# --- Filtri ---------------------------------------------------------------
@step("Job Titles")
def f_titles(page):
    fill_multi(page, "Job Titles", [r"enter job titles", r"job titles?"], JOB_TITLES, dropdown=False)


@step("Company Keywords (include)")
def f_kw_inc(page):
    open_section(page, ["Industry & Keywords", "Industry and Keywords"])
    fill_multi(page, ["Company Keywords", "Keywords"], [r"include keywords", r"keywords"],
               KEYWORDS_INCLUDE, dropdown=False)


@step("Company Keywords (exclude)")
def f_kw_exc(page):
    inp = find_input(page, [r"exclude keywords"])
    if inp is None:
        raise RuntimeError("campo Exclude keywords non presente")
    for v in KEYWORDS_EXCLUDE:
        type_and_pick(page, inp, v, dropdown=False)


@step("Industry")
def f_industry(page):
    open_section(page, ["Industry & Keywords", "Industry and Keywords"])
    fill_multi(page, "Industry", [r"^industry|industries|search industr"], INDUSTRIES)


@step("Company Lookalikes")
def f_lookalikes(page):
    if not open_section(page, ["Company Lookalikes", "Lookalikes"]):
        raise RuntimeError("filtro non disponibile nel piano")
    inp = find_input(page, [r"lookalike|domain|company"])
    if inp is None:
        raise RuntimeError("campo bloccato/non disponibile")
    for d in LOOKALIKES:
        type_and_pick(page, inp, d)


@step("Company Locations")
def f_locations(page):
    open_section(page, "Company")
    open_section(page, "Locations") or open_section(page, "Company Location")
    inp = find_input(page, [r"enter locations?|locations?|city, state"])
    if inp is None:
        raise RuntimeError("campo Locations non trovato")
    for loc in LOCATIONS:
        type_and_pick(page, inp, loc)


@step("# Employees")
def f_employees(page):
    if not open_section(page, ["# Employees", "Employees", "Number of Employees"]):
        raise RuntimeError("sezione non visibile")
    for label, parts in EMPLOYEE_RANGES.items():
        for cand in [label] + parts:
            row = page.get_by_text(re.compile(rf"^\s*{re.escape(cand)}\s*$")).first
            try:
                row.wait_for(state="visible", timeout=1500)
                safe_click(row, f"fascia {cand}")
                if cand == label:
                    break
            except PWTimeout:
                continue


@step("Exclude Companies")
def f_exclude_companies(page):
    if not open_section(page, ["Company", "Companies"]):
        raise RuntimeError("sezione non visibile")
    toggle = page.get_by_text(re.compile(r"is not any of|exclude|not any of", re.I)).first
    try:
        safe_click(toggle, "toggle esclusione")
    except Exception:
        pass
    inp = find_input(page, [r"enter companies|company name|domain"])
    if inp is None:
        raise RuntimeError("opzione di esclusione aziende non disponibile")
    for d in EXCLUDE_COMPANIES:
        type_and_pick(page, inp, d)


# --- Conteggi e salvataggio -------------------------------------------------
def wait_results(page):
    page.wait_for_load_state("networkidle", timeout=30000)
    page.wait_for_timeout(3500)


def read_counts(page):
    body = page.locator("body").inner_text()
    out = {}
    for label in ("Total", "Net New"):
        m = re.search(rf"{label}\s*[\n:]*\s*([\d][\d.,]*\s*[KkMm]?)", body)
        out[label] = m.group(1).strip() if m else "n/d"
    return out


def save_search(page):
    btn = page.get_by_role("button", name=re.compile(r"save as new search", re.I)).first
    try:
        btn.wait_for(state="visible", timeout=4000)
    except PWTimeout:
        # fallback: icona/pulsante "Save" del salvataggio ricerca (fuori dalla tabella)
        btn = page.get_by_role("button", name=re.compile(r"^save( search| view)?$", re.I)).first
    safe_click(btn, "Save as new search")
    page.wait_for_timeout(800)
    # se c'è un menu con "Save as new search", sceglilo
    opt = page.get_by_text(re.compile(r"^\s*save as new search\s*$", re.I)).first
    try:
        if opt.is_visible(timeout=1200):
            safe_click(opt, "Save as new search (menu)")
    except PWTimeout:
        pass
    name_in = page.get_by_role("dialog").get_by_role("textbox").first
    try:
        name_in.wait_for(state="visible", timeout=5000)
    except PWTimeout:
        name_in = page.get_by_placeholder(re.compile(r"name", re.I)).first
        name_in.wait_for(state="visible", timeout=5000)
    name_in.fill(SEARCH_NAME)
    confirm = page.get_by_role("dialog").get_by_role("button", name=re.compile(r"^(save|create|confirm)", re.I)).last
    safe_click(confirm, "conferma salvataggio ricerca")
    page.wait_for_timeout(2500)


def main():
    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(PROFILE_DIR, headless=False,
                                                    viewport={"width": 1500, "height": 950})
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        try:
            page.goto(APOLLO_URL)
            ensure_logged_in(page)
            page.wait_for_selector("text=/search filters|filters/i", timeout=30000)

            for f in (f_titles, f_kw_inc, f_kw_exc, f_industry, f_lookalikes,
                      f_locations, f_employees, f_exclude_companies):
                f(page)

            wait_results(page)
            counts = read_counts(page)
            print(f"\n=== Contatti trovati da Apollo ===\nTotal:   {counts['Total']}\n"
                  f"Net New: {counts['Net New']}\n")

            save_search(page)
            results["Salvataggio ricerca"] = "ok"
            print(f'[OK]   Ricerca salvata come "{SEARCH_NAME}"')

            page.screenshot(path=SCREENSHOT, full_page=False)
            print(f"Screenshot: {Path(SCREENSHOT).resolve()}")
        except Exception as e:
            print(f"[ERRORE] {e}")
            page.screenshot(path="apollo_error.png")
        finally:
            print("\nRiepilogo filtri:")
            for k, v in results.items():
                print(f"  - {k}: {v}")
            ctx.close()


if __name__ == "__main__":
    main()
