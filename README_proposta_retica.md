# Proposta LinkedIn Ads — Retica (Propaganda Adv)

| Cosa | Dove |
|---|---|
| Presentazione (modificabile / PDF) | `output/Retica_LinkedIn_Ads_Proposta.pptx` · `.pdf` (25 slide) |
| Mockup annunci (creatività + cornice feed) | `output/mockup/*.png` |
| Copy di tutti gli annunci, con varianti A/B | `output/copy_annunci.md` |
| Domande aperte per il cliente | `output/note_da_confermare.md` |
| Strategia video e storyboard con timecode | `output/storyboard_video.md` |
| Ricerca myBiros (blocco Ad Library, sito, stima) | `research/mybiros/` |
| Asset brand Retica / Propaganda | `assets/retica/` · `assets/propaganda/` |
| Calcoli (budget, KPI) e copy sorgente | `analysis/budget_model.py` · `analysis/ads_data.py` |
| Generatori (mockup, deck) | `tools/mockup/` · `tools/deck/` |

Rigenerare: `python3 analysis/ads_data.py && python3 analysis/budget_model.py && node tools/mockup/build_mockups.js && python3 tools/deck/build_deck.py`.
Il deck usa il font Poppins (installarlo per aprire il .pptx con rendering identico).
