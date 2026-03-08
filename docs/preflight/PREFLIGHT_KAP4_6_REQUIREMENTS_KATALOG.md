# Preflight-Protokoll: Kap. 4.6 — Requirements-Katalog

**Datum:** 2026-03-08
**Zielabschnitt:** 4.6 Requirements-Katalog (R-xx Systematik)
**DSR-Phase:** Design Cycle Phase 1 — Anforderungsableitung (Peffers Phase 2: Define Objectives)

---

## Ergebnis P1 (Exposé): ✅ konsistent

- Exposé definiert Kap. 4 als "Anforderungsanalyse (RQ1)" mit Requirements-Katalog als Ergebnis
- Gliederung_v3 beschreibt 4.6 explizit: "R-xx Systematik, Governance-Dimensionen aus Norm-Analyse, Traceability Art. 9-15 → R-xx, WAS-Ebene"
- Keine Scope-Abweichung gegenüber Exposé
- Gate-Spezifikation WIE → 5.3 (klare Trennung D_4.6_VS_5.3_SEPARATION)

## Ergebnis P2 (Kapiteltexte): ✅ Brücken identifiziert

**Kontinuität:** 4.5 endet mit: "Die konkrete Zuordnung dieser Oversight-Anforderungen zu den einzelnen Quality Gates erfolgt in Abschnitt 4.6."
- Ebenso 4.4 letzter Satz: "Die konkrete Zuordnung der Kontrollmechanismen zu den einzelnen Requirements und Gate-Identifikatoren erfolgt in Abschnitt 4.6"
- 4.3 verweist ebenfalls auf 4.6 als Ziel der Transformationskette

**Begriffe/Definitionen aus 4.1–4.5 (BINDEND):**
- Dreistufige Transformation: Norm (Art. 9-15) → Requirement (R-xx) → Gate (G-xx) [4.3]
- 3 Kontrollmechanismen: PaC (präventiv), Monitoring (reaktiv), Audit Trails (retrospektiv) [4.4]
- 4 Effektivitätsbedingungen Human Oversight: Causal Power, Epistemic Access, Self-Control, Fitting Intentions [4.5]
- Lifecycle-Phasen: Pre-Deployment, Deployment, Operation [4.2]
- Enforcement ≠ Dokumentation [4.1]
- Deployer-Scope: Art. 26, kein Art. 16 [4.1, 4.2]

**Forward-References die 4.6 einlösen MUSS:**
- 4.4 → "Zuordnung der Kontrollmechanismen zu Requirements und Gate-IDs"
- 4.5 → "Zuordnung der Oversight-Anforderungen zu Quality Gates"
- 4.3 → "WAS-Ebene: Requirements R-xx als Ergebnis der Transformation"

**Brücke zu Kap. 5:**
- 5.1 erwartet: Governance-Dimensionen + NIST/ISO-Konvergenznachweis (D_GOV_DIMENSIONS_HYBRID)
- 5.3 erwartet: Gate-Spezifikation WIE (Template, Trigger, Decision-Logik G-xx)

## Ergebnis P3 (Sessions/Files): ✅ chapter_state ready

- chapter_state.yaml: current_focus = "4.6 Requirements-Katalog planen — Quellen lesen"
- 5 R-xx YAMLs existieren (R001–R005) als DRAFT v0.1 — müssen erweitert/verfeinert werden
- Session Summary 20260305: Quellenabdeckung 4.6 = Elia/MQG4AI, Eisenberg/UCF, Lucaj/TechOps, Goncalves/XAI-CbD
- D_4.6_SCOPE: "substanziell (~3-4 Seiten), zeigt systematische Anforderungsableitung"
- D_4.6_VS_5.3_SEPARATION: "4.6 = WAS (R-xx), 5.3 = WIE (G-xx)"

## Ergebnis P4 (Entscheidungen): ⚠ 3 relevante Decisions + 1 offene Frage

**Direkt betroffene Decisions:**
- **D_4.6_SCOPE:** 4.6 substanziell (~3-4 Seiten), systematische Anforderungsableitung → NICHT nur Tabelle
- **D_4.6_VS_5.3_SEPARATION:** WAS (R-xx) vs. WIE (G-xx) — strikt einhalten
- **D_GOV_DIMENSIONS_HYBRID:** Governance-Dimensionen (strategisch/technisch/regulatorisch) in 4.6 einführen als Ergebnis der Norm-Analyse, Konvergenz-Nachweis mit NIST/ISO erst in 5.1
- **D_GATE_IDS_LOCATION:** Gate-IDs (G-PRE-01 etc.) erst in 5.3, in 4.6 nur R-xx IDs
- **D_MQG4AI_PLACEMENT:** Kurzreferenz in 4.6 zur Abgrenzung (Provider-Methodik vs. Deployer-Architektur)
- **D_KONSOLIDIERUNG_AUFGELOEST:** Alter 4.5-Konsolidierung aufgelöst → Governance-Dimensionen → 4.6

**⚠ Offene Frage:** Wie viele Requirements R-xx insgesamt? Derzeit R001–R005, aber die Abschnitte 4.2–4.5 legen nahe dass ~8-12 Requirements pro Art. 9-15 nötig sein könnten. Muss VOR dem Schreiben geklärt werden: kompaktes Set (~7-10) oder granulares Set (~12-15)?

## Ergebnis P5 (Quellen): ✅ alle in Zotero

**Pflicht-Zitate für 4.6:**

| Quelle | Zotero-Key | Rolle in 4.6 |
|--------|------------|--------------|
| EU AI Act Art. 9-15 | (Primärquelle) | Normative Basis aller R-xx |
| Eisenberg et al. (2025) UCF | JUK36XAW | Vergleichskandidat: 42 Controls, Colorado AI Act → Abgrenzung (EU AI Act + Deployer-Scope = Lücke) |
| Elia et al. (2025) MQG4AI | QRW95D4X | Abgrenzung: Provider-Methodik, XAI-Fokus, kein CI/CD vs. Deployer-Architektur |
| Lucaj et al. (2025) TechOps | 5Y79UTJ9 | Dokumentations-Templates als Requirements-Input für R-xx (Art. 11) |
| Goncalves & Correia (2025) XAI-CbD | AR9CXH43 | Compliance-by-Design Konzept, XAI-Module → stützt Transparenz-Requirements |
| Buscemi et al. (2025) | JQNQWSV3 | Verification Space R1-R8 → Mapping zu eigenen R-xx |
| Hevner et al. (2004) | — | DSR-Verankerung: Relevance→Design Übergang |
| Peffers et al. (2007) | — | Phase 2: Define Objectives of a Solution |

**Ergänzend (konvergente Evidenz, nicht alleinig):**
- Ray (2026) — TRiSM Lifecycle + PaC-Taxonomie
- Kovac et al. (2025) — CERTAIN/RegOps Controls
- Huwyler (2024/2025) — Lifecycle-Governance

## Ergebnis P6 (Uni-Anforderungen + DSR): ⚠ Budget-Spannung

**Seitenbudget:**
- Kap. 4 gesamt: D_KAP4_PAGES = ~13 Seiten (D_KAP4_BUDGET_FLEX = 14-15 erlaubt)
- 4.1–4.5 aktuell: ~3.696 Wörter ≈ 12,3 Seiten (bei ~300 W/Seite)
- **Restbudget 4.6:** ~600–900 Wörter (2-3 Seiten) bei 14-15S Flex-Budget
- D_4.6_SCOPE sagt "~3-4 Seiten" → ⚠ Spannung! Entweder Budget erhöhen oder 4.6 kompakter

**DSR-Phase-Mapping:**
- 4.6 = Peffers Phase 2 (Define Objectives) → Phase 3 (Design & Development) Übergang
- Hevner: Relevance Cycle → Design Cycle Übergang
- 4.6 ist der Bridge-Artefakt: konsolidiert alle Requirements aus 4.1-4.5 in R-xx Systematik

**Formatvorgaben:**
- Hohe Zitationsdichte (Prof. Prinz)
- Keine formalen Überleitungen
- Ergebnisse kontextualisieren
- Nummerierung nur bis 2. Ebene (4.6, kein 4.6.1)

---

## Synthese — Argumentationsstruktur für Kap. 4.6

**Brücke von Kap. 4.5:** "Die konkrete Zuordnung dieser Oversight-Anforderungen zu den einzelnen Quality Gates erfolgt in Abschnitt 4.6."

| Absatz | Argumentativer Move | Logik | Brücke zum nächsten |
|--------|---------------------|-------|---------------------|
| 1 | **Synthese-Eröffnung:** 4.1-4.5 haben Anforderungsdimensionen identifiziert → jetzt Konsolidierung in prüfbare R-xx | Schließt Forward-References aus 4.3-4.5 ein | → Einführung der Governance-Dimensionen |
| 2 | **Governance-Dimensionen einführen:** regulatorisch / technisch / strategisch als Ergebnis der Norm-Analyse in 4.1-4.5 | D_GOV_DIMENSIONS_HYBRID — Konvergenz-Nachweis kommt in 5.1 | → Verweis auf Vergleichsansätze |
| 3 | **Abgrenzung Related Work:** UCF (Eisenberg, 42 Controls) + MQG4AI (Elia, Provider-Methodik) → Positionierung: EU AI Act + Deployer + Lifecycle-Phase + Gate-Mapping = Beitrag | D_MQG4AI_PLACEMENT | → Requirements-Tabelle |
| 4–5 | **Requirements-Tabelle R-xx:** Systematische Zuordnung Art. 9-15 → R-xx mit Lifecycle-Phase, Governance-Dimension, Kontrollmechanismus | Kern des Abschnitts, löst Traceability-Versprechen ein | → Brücke zu Kap. 5 |
| 6 | **Überleitung Kap. 5:** R-xx = WAS-Ebene, Kap. 5 operationalisiert als WIE (Gate-Specs G-xx, Design Principles, Architektur) | D_4.6_VS_5.3_SEPARATION | → Kap. 5.1 |

**Brücke zu Kap. 5.1:** "Die folgende Architekturentwicklung überführt die hier spezifizierten Requirements in Designprinzipien und Gate-Spezifikationen."

---

## Inhalts-Checklist

- ☐ Synthese der Anforderungsdimensionen aus 4.1-4.5
- ☐ Governance-Dimensionen einführen (regulatorisch/technisch/strategisch) — D_GOV_DIMENSIONS_HYBRID
- ☐ Abgrenzung UCF (Eisenberg) + MQG4AI (Elia) → USP-Positionierung
- ☐ Requirements-Tabelle: R-xx mit ID, Titel, Art.-Referenz, Lifecycle-Phase, Governance-Dimension, Kontrollmechanismus-Typ
- ☐ Traceability zeigen: Norm → R-xx (Forward: → G-xx in 5.3)
- ☐ DSR-Rückverweis auf Kap. 3.5/3.6 (Traceability-Kette)
- ☐ Überleitung zu Kap. 5

## Negativ-Checklist — Was darf NICHT in Kap. 4.6

- ❌ Keine Gate-IDs (G-PRE-01 etc.) — erst in 5.3 (D_GATE_IDS_LOCATION)
- ❌ Keine Gate-Spezifikation (Trigger, Kriterien, Decision-Logik) — das ist WIE → 5.3
- ❌ Keine Provider-Perspektive (Art. 16) — Deployer-Scope Art. 26
- ❌ Keine NIST/ISO-Konvergenz-Argumentation — kommt in 5.1 (D_NIST_CONVERGENCE)
- ❌ Kein Retirement — explizit Out-of-Scope (D_RETIREMENT_OUT)
- ❌ Keine formalen Überleitungssätze (Prof. Prinz)
- ❌ Keine vollständige MQG4AI-Analyse — nur Kurzreferenz (D_MQG4AI_PLACEMENT)

## Pflicht-Zitate

- EU AI Act (VO 2024/1689) Art. 9-15 — Normative Basis
- Eisenberg et al. (2025) — UCF-Abgrenzung (42 Controls, Colorado AI Act)
- Elia et al. (2025) — MQG4AI-Abgrenzung (Provider, XAI-Fokus)
- Buscemi et al. (2025) — Verification Space Mapping
- Hevner et al. (2004) — DSR-Verankerung
- Lucaj et al. (2025) — TechOps Templates (Art. 11)
- Goncalves & Correia (2025) — XAI-CbD (Transparenz-Requirements)

## Offene Fragen (vor Schreiben klären)

1. **⚠ Budget-Spannung:** D_4.6_SCOPE sagt 3-4 Seiten, aber Restbudget = ~2-3 Seiten bei Flex-Budget 14-15S. Option A: 4.6 kompakt (~600-800W, 2-3S), Option B: Budget auf 15-16S erhöhen
2. **⚠ Granularität R-xx:** Aktuell 5 Requirements (R001-R005). Reicht das für systematische Art. 9-15 Abdeckung? Vorschlag: ~8-12 Requirements, aber das beeinflusst Tabellengröße
3. **Tabellen-Format:** Kompakte Tabelle (1 Zeile pro R-xx) oder ausführlich mit Beschreibung?

---

→ **Bereit für "GO"** — nach Klärung der 3 offenen Fragen
