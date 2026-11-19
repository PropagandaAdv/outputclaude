import json,sys
sys.path.insert(0,'analysis')
from ads_data import ADS, LIM, hook
out=["# Copy annunci LinkedIn — Retica, focus LOGISTICA (proposta, nessuna campagna attiva)\n",
"Leve del messaggio: **DDT** (righe, codici, quantità), **unità di misura** (colli, pezzi, pallet) e **listini / prezzi**. Target principale: aziende di logistica, trasporti e magazzino.",
"Tutti i testi sono in italiano, con il \"tu\", prima il beneficio. I campi *Intro* e *Headline* usano **solo claim presenti su retica.ai** (verificati il 19/11/2026).",
"I conteggi tra parentesi sono caratteri, calcolati in codice. Limiti: intro text max 600 (i primi ~150 sono visibili prima di \"…altro\"), headline max 70, descrizione max 100, card carosello max 45; Conversation Ad: messaggio max 500, oggetto max 60.",
"Segnaposto: `{FirstName}` = nome del destinatario (campo dinamico LinkedIn).\n",
"> ## Cosa è verificato e cosa no sulle tre leve\n> - **DDT:** verificato. Pagina retica.ai/logistica; testimonianze Carraro (DDT in SAP), Le Messaggerie Nazionali (spedizioni), Edildelta (DDT fornitori) [VERIFICATO].\n> - **Unità di misura:** Retica estrae \"unità di misura o confezione\" dai listini (articolo del blog) [VERIFICATO]. La **conversione** (es. colli → pezzi) NON è dichiarata sul sito: potrebbe rientrare nel modulo \"Condizioni\" (trasformare i dati nel formato del gestionale) **[DA CONFERMARE]**.\n> - **Verifica prezzi:** l'articolo di Retica sui listini dice che Retica *non sostituisce il gestionale nelle verifiche* e che il confronto dei prezzi resta nell'ERP [VERIFICATO]. Una testimonianza (Gruppo Borghi) cita \"verifiche su prezzi e tempi richiesti\" sugli ordini. Una verifica prezzi fatta da Retica è **[DA CONFERMARE]**.\n> - Per questo le varianti A e B qui sotto non promettono conversione né verifica. Le versioni più forti stanno nel blocco **\"Solo se Retica conferma\"** di ogni annuncio: **non caricarle finché non c'è la conferma scritta.**\n",
"> **Prima del caricamento:** UTM, link di destinazione, testimonial con nome/azienda e persona del Thought Leader Ad sono **[DA CONFERMARE]**.\n","---\n"]
for a in ADS:
    out.append(f"## {a['id']} · {a['funnel']} · {a['angle']}\n")
    out.append(f"- **Leva:** {a['leva']}\n- **Formato:** {a['fmt']}\n- **Obiettivo Campaign Manager:** {a['obj']}\n- **CTA LinkedIn:** {a['cta']}\n- **Destinazione:** {a['dest']}\n- **Creatività:** {a['cover']} (file in `output/mockup/{a['id']}_*`)\n")
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
    sc=a.get('se_confermato')
    if sc:
        out.append(f"### ⚠ Solo se Retica conferma: {sc['claim']} **[DA CONFERMARE]**\n")
        out.append(f"**Intro text** ({len(sc['intro'])}):\n> {sc['intro']}\n")
        out.append(f"**Headline** ({len(sc['headline'])}): {sc['headline']}\n")
    out.append(f"**Note:** {a['notes']}\n\n---\n")
out.append("""## Lead Gen Form (per A03, A04, A07, A08, A09)
- **Nome form:** Richiedi demo Retica — logistica
- **Headline form (max 60):** Vediamo Retica sui tuoi DDT
- **Dettagli (max 160):** Lascia i tuoi dati: ti ricontattiamo entro 24 ore lavorative per fissare la demo.
- **Campi precompilati dal profilo LinkedIn:** nome, cognome, email di lavoro, azienda, ruolo, (telefono facoltativo)
- **Domande di qualifica (max 2):** 1) "Quanti DDT gestisci al mese?" (<500 / 500–2.000 / 2.000–10.000 / >10.000) · 2) "Quale gestionale/ERP usi?" (elenco + Altro)
- **Consenso privacy GDPR:** link all'informativa privacy di Retica + casella di consenso esplicita
- **Thank-you page:** conferma + pulsante "Prenota la demo" + link al calcolatore del risparmio [DA CONFERMARE strumento calendario]
- **Nota:** durata della demo e offerta "Analisi dei tuoi DDT" da confermare con il cliente.
""")
open('output/copy_annunci.md','w',encoding='utf8').write('\n'.join(out))
print('ok',len('\n'.join(out)))
