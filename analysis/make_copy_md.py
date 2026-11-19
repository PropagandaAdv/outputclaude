import json,sys
sys.path.insert(0,'analysis')
from ads_data import ADS, LIM, hook
out=["# Copy annunci LinkedIn — Retica (proposta, nessuna campagna attiva)\n",
"Tutti i testi sono in italiano, con il \"tu\", prima il beneficio. Claim usati: solo quelli presenti su retica.ai (verificati il 19/11/2026) o da confermare con il cliente.",
"I conteggi tra parentesi sono caratteri, calcolati in codice. Limiti usati: intro text max 600 (i primi ~150 sono quelli visibili prima di \"…altro\"), headline max 70, descrizione max 100, card carosello max 45; Conversation Ad: messaggio max 500, oggetto max 60.",
"Segnaposto: `{FirstName}` = nome del destinatario (campo dinamico LinkedIn).\n",
"> **Prima del caricamento:** UTM, link di destinazione, testimonial con nome/azienda e persona del Thought Leader Ad sono **[DA CONFERMARE]**.\n","---\n"]
for a in ADS:
    out.append(f"## {a['id']} · {a['funnel']} · {a['angle']}\n")
    out.append(f"- **Formato:** {a['fmt']}\n- **Obiettivo Campaign Manager:** {a['obj']}\n- **CTA LinkedIn:** {a['cta']}\n- **Destinazione:** {a['dest']}\n- **Creatività:** {a['cover']} (file in `output/mockup/{a['id']}_*`)\n")
    for v in 'AB':
        t=a['intro_'+v]; h=a['headline_'+v]
        out.append(f"### Variante {v}\n")
        out.append(f"**Intro text** ({len(t)}):\n> {t}\n")
        out.append(f"*Gancio visibile (primi ~150 car.):* {hook(t)}…\n")
        out.append(f"**Headline** ({len(h)}): {h}\n")
        if v=='A':
            out.append(f"**Descrizione** ({len(a['desc'])}): {a['desc']}\n")
    if a.get('cards'):
        out.append("**Card carosello:** "+' · '.join(f"{i+1}) {c} ({len(c)})" for i,c in enumerate(a['cards']))+"\n")
    out.append(f"**Note:** {a['notes']}\n\n---\n")
out.append("""## Lead Gen Form (per A03, A04, A07, A08, A09)
- **Nome form:** Richiedi demo Retica
- **Headline form (max 60):** Vediamo Retica sui tuoi documenti
- **Dettagli (max 160):** Lascia i tuoi dati: ti ricontattiamo entro 24 ore lavorative per fissare la demo.
- **Campi precompilati dal profilo LinkedIn:** nome, cognome, email di lavoro, azienda, ruolo, (telefono facoltativo)
- **Domande di qualifica (max 2):** 1) "Quanti documenti gestisci al mese?" (<500 / 500–2.000 / 2.000–10.000 / >10.000) · 2) "Quale gestionale/ERP usi?" (elenco + Altro)
- **Consenso privacy GDPR:** link all'informativa privacy di Retica + casella di consenso esplicita
- **Thank-you page:** messaggio di conferma + pulsante "Prenota la demo" (link al calendario) [DA CONFERMARE strumento]
- **Nota:** la durata della demo e l'offerta "Analisi dei tuoi documenti" sono da confermare con il cliente.
""")
open('output/copy_annunci.md','w',encoding='utf8').write('\n'.join(out))
print('ok',len('\n'.join(out)))
