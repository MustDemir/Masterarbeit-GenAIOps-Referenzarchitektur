# Bewertungsbericht: Kap. 4 — Anforderungsanalyse

> **Datum:** 2026-03-08
> **Reviewer:** thesis-reviewer Skill v2.0
> **Pruefobjekt:** 00_workspace/Fulltext_Kapitel/Kapitel 4 Anforderungen.docx
> **Woerter:** 4.141 (~13,8 Seiten) | Budget: 14–15 Seiten (D_KAP4_BUDGET_FLEX)

---

## Gesamtscore

| Dimension | Score | Gewicht | Gewichtet |
|-----------|-------|---------|-----------|
| R1 Struktur | 4.0 | 10% | 0.40 |
| R2 Roter Faden | 3.5 | 30% | 1.05 |
| R3 Stil/Uni-Vorgaben | 4.0 | 20% | 0.80 |
| R4 Zitationen | 4.5 | 15% | 0.68 |
| R5 Definitions/Scope | 4.5 | 10% | 0.45 |
| R6 Gutachter-Bewertung | 3.5 | 15% | 0.53 |
| **GESAMT** | | | **3.9 / 5.0** |

**Note: Gut** — Solide Arbeit, gezielte Verbesserungen empfohlen.

---

## R1 Struktur: 4.0 / 5

### Absatzstruktur

| Abschnitt | Woerter | Seiten (~300W) | Absaetze | Topic Sentences | Bewertung |
|-----------|---------|---------------|----------|-----------------|-----------|
| 4.0 Einleitung | ~305 | 1.0 | 3 | ✅ Ja | Guter Einstieg, klare Logik |
| 4.1 Zielbild (4.1.1–4.1.6) | ~1.370 | 4.6 | 6 | ✅ Ja | Sehr gut strukturiert |
| 4.2 Lifecycle | ~695 | 2.3 | 4 | ✅ Ja | Kompakt, dicht |
| 4.3 Transformation | ~590 | 2.0 | 4 | ✅ Ja | Methodisch sauber |
| 4.4 Kontrollmechanismen | ~540 | 1.8 | 4 | ✅ Ja | Klar gegliedert |
| 4.5 Human Oversight | ~450 | 1.5 | 3 | ✅ Ja | Komprimiert aber vollstaendig |
| 4.6 Stub (MQG4AI + Goncalves) | ~191 | 0.6 | 2 | ⚠ Unvollstaendig | NUR Kurzreferenz, kein R-Katalog |

### Seitenbudget

- **IST:** ~4.141W / ~13,8 Seiten (ohne den ausstehenden 4.6-Hauptteil)
- **SOLL:** 14–15 Seiten
- **Delta:** -0,2 bis -1,2 Seiten → 4.6 hat noch ~1–4 Seiten Raum
- **Status:** ✅ Im Budget (mit 4.6 wird es passen)

### Gliederungstiefe

- Kap. 4.1 hat Sub-Punkte 4.1.1–4.1.6 = **3 Ebenen**
- Gliederung v3 erlaubt max. 4 Ebenen → ✅ Konform
- Aber: Kein anderer Abschnitt (4.2–4.5) hat Sub-Punkte. **Asymmetrie:** 4.1 ist durch 6 Sub-Abschnitte deutlich granularer als 4.2–4.5. Das ist inhaltlich begruendet (verschiedene Aspekte des Zielbilds), aber ein Gutachter koennte die Balance hinterfragen.

### Befund R1:
- ⚠ **4.6 ist unvollstaendig** — nur ein MQG4AI-Kurzreferenz-Stub (191W). Der eigentliche Requirements-Katalog (R-xx Tabelle) fehlt. Das ist die kritischste Luecke des Kapitels.
- ⚠ **4.1 dominiert** das Kapitel (~33% der Woerter). Das ist vertretbar (Zielbild legt Grundlagen), aber ein Gutachter koennte fragen ob Scope-Abgrenzung (4.1.2, 4.1.3) nicht straffer sein koennte.

---

## R2 Roter Faden: 3.5 / 5

### Bruecke rueckwaerts (Kap. 3 → Kap. 4):

**Kap. 3 endet mit:** Interviewdesign und Auswertung (3.8) — Mayring (2015), Guetekriterien, Triangulation. Kein expliziter Uebergangssatz zu Kap. 4.

**Kap. 4 beginnt mit:** "Dieses Kapitel operationalisiert die regulatorischen Anforderungen..." mit Verweis auf Artefaktkonstruktion und design-getriebene Logik.

**Bewertung:** ⚠ **Mittelmässig.** Kap. 4 knuepft thematisch an Kap. 3 an (DSR Design Cycle Phase 1), aber der Uebergang ist **nicht nahtlos**:
- Kap. 3 endet bei der Evaluationsmethodik — der Leser erwartet danach die Ergebnisse
- Kap. 4 springt direkt in die Anforderungsanalyse ohne explizit zu sagen: "Die in Kap. 3 definierte Methodik wird nun angewendet"
- Der DSR-Rueckverweis kommt erst in 4.1 Absatz 1 ("im Sinne des Design-Science-Research-Paradigmas nach Hevner et al. (2004)"), nicht in der Kapiteleinleitung
- **Empfehlung:** In der Kapiteleinleitung (Abs. 1) einen Satz ergaenzen wie: "Die methodische Grundlage bildet das in Kapitel 3 dargestellte Design-Science-Research-Vorgehen nach Hevner et al. (2004) und Peffers et al. (2007), wobei das vorliegende Kapitel den Design Cycle — Phase 1 (Relevance → Design) realisiert."

### Argumentationskette innerhalb Kap. 4:

| Abschnitt | Argumentativer Beitrag | Uebergang zum naechsten | Bewertung |
|-----------|----------------------|------------------------|-----------|
| 4.0 Einleitung | Scope definieren, Logik ankuendigen | → 4.1: "Zielbild" | ✅ Klar |
| 4.1 Zielbild | Deployer-Scope, Art. 10, RAG, Enforcement, Accountability, Lifecycle | → 4.2: letzter Satz verweist auf Lifecycle-Modell | ✅ Nahtlos |
| 4.2 Lifecycle | Pre-Depl./Depl./Operation, Art. 25, Retirement-Out | → 4.3: "wann → nun: wie" | ✅ Hervorragend |
| 4.3 Transformation | Norm → Requirement → Gate, 4 Dekompositionsstrategien | → 4.4: implizit (Mechanismen) | ⚠ Kein expliziter Uebergangssatz |
| 4.4 Kontrollmechanismen | PaC, Monitoring, Audit, RegOps-Integration | → 4.5: implizit (Querschnitt) | ⚠ Kein expliziter Uebergangssatz |
| 4.5 Human Oversight | Sterz 4 Bedingungen, Laux Institutionalised Distrust | → 4.6: "konkrete Zuordnung erfolgt in 4.6" | ✅ Explizit |
| 4.6 Stub | MQG4AI-Kurzreferenz, Goncalves-Abgrenzung | → Kap. 5: erwahnt aber Stub | ❌ Unvollstaendig |

**Befund:** Die Argumentation **innerhalb** des Kapitels ist stark (4.1→4.2→4.3 insbesondere). Schwaechen:
- ⚠ Uebergaenge 4.3→4.4 und 4.4→4.5 sind nur implizit — kein Bruch, aber auch kein expliziter logischer Faden
- ❌ **4.6 als Stub bricht den Roten Faden ab.** Das Kapitel verspricht in der Einleitung einen "strukturierten Requirements-Katalog (R1–Rn)" — der Katalog existiert nicht. Das ist die groesste Schwaeche.

### Bruecke vorwaerts (Kap. 4 → Kap. 5):

**Kap. 4 verweist an 4 Stellen explizit auf Kap. 5:**
1. Einleitung: "Dieser Katalog dient als unmittelbare Eingangsgröße für Kapitel 5"
2. 4.3: "Zuordnung der Gate-Identifikatoren [...] erfolgt in Abschnitt 4.6, während die technische Realisierung als Policy-as-Code in Kapitel 5 behandelt wird"
3. 4.4: "technische Architektur ihrer Implementierung wird in Kapitel 5 behandelt"
4. 4.5: "Zuordnung dieser Oversight-Anforderungen zu den einzelnen Quality Gates erfolgt in Abschnitt 4.6"

**Kap. 5 Volltext:** Nahezu leer (119W) — nur eine Notiz zur 4.6/5.3 Abgrenzung.

**Bewertung:** ✅ Die Forward-References sind korrekt und konsistent. Die Bruecke zu Kap. 5 ist logisch vorbereitet. **Problem:** Alle vier Verweise setzen voraus, dass 4.6 den R-xx Katalog enthaelt — der fehlt.

### Konsistenz mit anderen Kapiteln:

- ✅ Kein Widerspruch zu Kap. 1 (Problemdimensionen, Forschungsfragen)
- ✅ Kein Widerspruch zu Kap. 3 (DSR-Rahmen, Artefaktdefinition)
- ✅ Deployer-Scope durchgehend konsistent
- ✅ Terminologie konsistent mit Critical Definitions
- ⚠ Kap. 4 Einleitung erwahnt NIST AI RMF als "strukturierenden Referenzrahmen zur Harmonisierung" — das muss mit D_NIST_CONVERGENCE in 5.1 abgestimmt sein (kein Widerspruch, aber Achtung bei 5.1-Formulierung)

---

## R3 Stil/Uni-Vorgaben: 4.0 / 5

### Gefundene Verstoesse:

| # | Typ | Stelle | Text | Fix |
|---|-----|--------|------|-----|
| 1 | PK-V1 | 4.1 Abs. 1 | "– im Folgenden als EU AI Act bezeichnet –" | ⚠ Grenzfall: Standard-Legaldefinition, kein Stilbruch. **Akzeptabel.** |
| 2 | PK-V4 | 4.1.2 | Abs. ueber Art. 10 Abs. 6 ist sehr detailliert | ⚠ Koennte straffer sein. Frage: Braucht der Leser die Art. 10 Abs. 1-5 Detailerklaerung oder reicht ein Satz? |
| 3 | PK-V5 | 4.1.3 | "Ein für generative KI-Anwendungen besonders relevanter Sonderfall **betrifft** die Klassifizierung" | Passiv-nah, aber akzeptabel |
| 4 | PK-V3 | 4.6 Stub | Wiederholt teilweise Inhalte aus 4.3 (Traceability-Kette) | ⚠ Redundanz mit 4.3 — bei Fertigstellung 4.6 beachten |

### Stil-Gebote:

- ✅ PK-G1: Jeder Absatz traegt zur Argumentation bei — kein erkennbarer Fuelltext
- ✅ PK-G2: Definitionen werden durch Related-Work-Abgrenzung kontextualisiert (besonders stark in 4.3)
- ✅ PK-G3: Text ist komprimiert — hohe Informationsdichte
- ✅ PK-G4: Bei Definitionen erst Quelle, dann Einordnung (z.B. 4.1.1 Deployer-Definition)
- ✅ PK-G5: Hohe Referenzierdichte — nahezu jeder Absatz mit Belegen
- ✅ PK-G6: Durchgehend Bezug zum Gesamtkontext (DSR, Forschungsfragen)

### SRH 50/30/20 Einschaetzung:

- **Inhalt (50%):** ⭐⭐⭐⭐ Problemdurchdringung erkennbar — nicht nur Zusammenfassung, sondern eigene Syntheseleistung (dreistufige Transformation, Lifecycle-Konsolidierung). Eigenstaendiger Beitrag klar.
- **Methodik (30%):** ⭐⭐⭐⭐ DSR-Phase erkennbar (Design Cycle Phase 1). Vorgehensweise nachvollziehbar. Hevner/Peffers-Verankerung vorhanden.
- **Formalia (20%):** ⭐⭐⭐⭐ APA7 durchgehend, Gliederungstiefe konform, Seitenbudget eingehalten. Einziger Abzug: 4.6 unvollstaendig.

### Blablameter-Check:

Kein Verdacht. Der Text ist durchgehend dicht argumentiert. Keine Fuellsaetze gefunden.

---

## R4 Zitationen: 4.5 / 5

### Zitationsstatistik:

| Metrik | Wert |
|--------|------|
| Zitationen gesamt | ~62 |
| Absaetze gesamt | ~30 |
| Dichte | ~2.1 Zitationen/Absatz |
| Einzigartige Quellen | ~20 |
| Gesetzestexte | EU AI Act (Art. 3, 9, 10, 11, 12, 13, 14, 15, 25, 26, 43, 72) |
| Grey Literature | EDPS TechSonar, NIST AI RMF, NIST AI 600-1, Microsoft GenAIOps |

### Quellen-Diversitaet:

- ✅ Gute Breite: Huwyler, Buscemi, Kelly, Gallina, Feng, Sterz, Laux, Enqvist, Ooms, Kovac, Romeo, Sardana, Ray, Butt, Leon, Novelli, Goncalves, Elia
- ✅ Mix: Peer-reviewed (Kelly, Buscemi, Sterz, Laux), Preprints (Elia, Goncalves), Grey Lit (NIST, EDPS, Microsoft)
- ✅ Aktualitaet: Schwerpunkt 2024–2025
- ⚠ 2026-Quellen (Leon, Butt, Ray): Per D_2026_SOURCES nur als "konvergente Evidenz" — wird in Kap. 4.2 aber prominent als Lifecycle-Vergleich genutzt. Ist das noch "konvergente Evidenz" oder schon tragende Argumentation?

### Seitenangaben-Check:

| Quelle | Seitenangabe | Status |
|--------|-------------|--------|
| Huwyler (2025) | S. 3, S. 5, S. 5–8, S. 10, S. 3–4, S. 4 | ✅ |
| NIST (2023) | S. 5, S. 20, S. 10, S. 21 | ✅ |
| Buscemi et al. (2025) | S. 7–8, S. 5, S. 1, S. 2 | ✅ |
| Kelly et al. (2024) | S. 1 | ✅ |
| Novelli et al. (2024) | S. 9, S. 3–4 | ✅ |
| Sterz et al. (2024) | S. 4–5 (Def. 3.1–3.5, Figure 1) | ✅ |
| Laux (2024) | S. 2, S. 7–8 (Sztompka-Framework), S. 11 (6 Prinzipien Tabelle) | ✅ |
| Enqvist (2023) | S. 2, S. 4 (Analytical Framework), S. 12–14 (What/When/By whom) | ✅ |
| Ooms et al. (2025) | S. 5–6 (Policy Prototyping, Stakeholder-Feedback) | ✅ |
| Ray (2026) | S. 1–2 (TRiSM-Pillars), S. 6 (Lifecycle-Phasen), S. 28 (Stages) | ✅ |
| Leon (2026) | S. 2 (7-Stage Model), S. 7 (Table 3 ref), S. 8 (Figure 1, Guardrails) | ✅ |
| Butt et al. (2026) | S. 1–2 (GEAP-Framework, 5 Gates), S. 3 (Table 1) | ✅ |
| Sardana et al. (2024) | S. 1–2 (CaC 2.0 Konzept), S. 5 (Multi-Agent-Architektur) | ✅ |
| Romeo et al. (2025) | S. 1–3 (ARPaCCino, Rego-Generierung, Architektur) | ✅ |
| Kovac et al. (2025) | S. 1–3 (CERTAIN-Framework, RegOps Engine, Ontologie) | ✅ |
| Gallina et al. (2025) | S. 1 | ✅ |
| Feng et al. (2024) | S. 1–2 (RAINCOAT-Ansatz, SLEEC-Regeln) | ✅ |
| Goncalves & Correia (2025) | S. 1, S. 3 (XAI-CbD-Framework), S. 8–9 (Tables 2–3) | ✅ |
| EU AI Act Artikel | Artikel + Absatz | ✅ |

**Befund:** ✅ **Seitenangaben fuer alle Quellen ermittelt (Stand 2026-03-08).** PDF-Seitenzahlen per D_PDF_SEITENZAHLEN. Alle 12 zuvor fehlenden Quellen wurden via pdftotext-Extraktion verifiziert. Die Seitenangaben muessen noch in die DRAFT.md-Dateien und die Volltext-DOCX uebernommen werden.

---

## R5 Definitions/Scope: 4.5 / 5

### Critical Definitions Check:

| Definition | Korrekt verwendet? | Stelle |
|-----------|-------------------|-------|
| Enforcement ≠ Dokumentation | ✅ Explizit in 4.1.4 | Abschnitt traegt den Titel |
| Quality Gate = automatisiert + evidenzbasiert | ✅ Durchgehend konsistent | 4.2, 4.3, 4.4 |
| Dreistufige Transformation: Norm → R → Gate | ✅ In 4.3 formalisiert | Kernbeitrag |
| 3 Kontrollmechanismen (PaC, Monitoring, Audit) | ✅ In 4.4 ausfuehrlich | Exklusive Zuordnung |
| Human Oversight ≠ manuelle Pruefung | ✅ In 4.5 | Sterz + Laux |
| Deployer-Scope Art. 26 | ✅ Durchgehend | 4.1.1 explizit |
| Retirement Out-of-Scope | ✅ In 4.2 explizit | Letzter Absatz |

### Scope-Verstoesse:
- ✅ Keine Provider-Perspektive (Art. 16) eingenommen
- ✅ Art. 25 als Scope-Grenze behandelt (nicht als Thema vertieft)
- ✅ Kein juristischer Kommentar — technisch-organisatorische Operationalisierung
- ✅ Retirement explizit ausgeschlossen mit Begruendung

### Decision-Alignment:
Alle relevanten Decisions (D_4.5_STRUCTURE, D_RETIREMENT_OUT, D_ART25_DEPTH, D_GATE_IDS_LOCATION, D_4.6_SCOPE, D_4.6_VS_5.3_SEPARATION) werden korrekt umgesetzt.

---

## R6 Gutachter-Bewertung: 3.5 / 5

### Top 3 Staerken:

1. **Eigene Syntheseleistung:** Die dreistufige Transformation (4.3) und das konsolidierte Lifecycle-Modell (4.2) sind genuine Beitraege, nicht nur Literaturzusammenfassungen. Die Konvergenz-Argumentation (4 Dekompositionsstrategien → gemeinsames Muster) ist ueberzeugend.

2. **Hohe Zitationsdichte und Quellen-Diversitaet:** ~62 Zitationen aus ~20 Quellen in ~4.100 Woertern. Jede Behauptung ist belegt. Die Quellenauswahl ist aktuell (Schwerpunkt 2024–2025) und umfasst verschiedene Disziplinen.

3. **Konsistente Scope-Disziplin:** Der Deployer-Scope wird durchgehend eingehalten. Art. 10, Art. 25 und Retirement werden sauber abgegrenzt. Keine Scope-Drift.

### Top 3 Schwaechen:

1. **4.6 Requirements-Katalog fehlt (KRITISCH).** Das Kapitel verspricht in der Einleitung "einen strukturierten Requirements-Katalog (R1–Rn)" — dieser existiert nicht. Der aktuelle Stub (MQG4AI-Kurzreferenz) ist keine Anforderungstabelle. Ohne 4.6 ist die Argumentationskette gebrochen: 4.1–4.5 bauen systematisch auf etwas auf, das dann nicht geliefert wird. Kap. 5 kann nicht beginnen ohne die R-xx Tabelle als Eingangsgroesse.

2. **Seitenangaben fehlen bei Kern-Quellen.** Sterz et al. (2024) — 4 Effektivitaetsbedingungen und Laux (2024) — 6 Designprinzipien / Taxonomie sind die theoretischen Fundamente von 4.5, aber ohne Seitenangaben. Bei einer Pruefung wuerde ein Gutachter hier nachfragen.

3. **Bruecke Kap. 3 → Kap. 4 zu schwach.** Kap. 3 endet bei Interviewdesign (3.8), Kap. 4 beginnt mit Anforderungsanalyse. Der DSR-Rueckverweis kommt erst in 4.1, nicht in der Kapiteleinleitung. Ein expliziter Satz wie "Die in Kapitel 3 dargestellte Phase 1 des Design Cycle wird nun realisiert" wuerde helfen.

### Priorisierte Empfehlungen:

1. **[KRITISCH] 4.6 Requirements-Katalog fertigstellen.** R-xx Tabelle mit: ID, Artikel-Referenz, Lifecycle-Phase, Governance-Dimension, Kontrollmechanismus, Verbindlichkeit. Ohne diesen Abschnitt ist Kap. 4 nicht abgabereif.

2. **[WICHTIG] Seitenangaben nachruestfen fuer:** Sterz et al. (2024), Laux (2024), Enqvist (2023), Ray (2026), Leon (2026), Butt et al. (2026), Romeo et al. (2025), Kovac et al. (2025), Sardana et al. (2024), Feng et al. (2024). Zotero-Fulltext nutzen oder `zitations-finder` Skill.

3. **[WICHTIG] Kapiteleinleitung staerken.** Den DSR-Rueckverweis von 4.1 in die Kapiteleinleitung verschieben oder dort duplizieren. Explizit: "Design Cycle Phase 1 → RQ1".

4. **[OPTIONAL] Uebergangssaetze 4.3→4.4 und 4.4→4.5 expliziter.** Aktuell implizit — ein Satz wie "Die Frage, welche operativen Mechanismen diese Gate-Kriterien durchsetzen, wird im folgenden Abschnitt adressiert" wuerde den Faden staerken.

5. **[OPTIONAL] 4.1 straffen.** 4.1.2 (Art. 10) und 4.1.3 (RAG) koennten um je 2-3 Saetze gekuerzt werden. Das waere reine Budgetoptimierung — der Inhalt ist korrekt.

---

## Ergebnis: UEBERARBEITUNG EMPFOHLEN

**Hauptgrund:** 4.6 fehlt. Die Abschnitte 4.1–4.5 sind gut bis sehr gut (Score 4.0–4.5), aber ohne den Requirements-Katalog ist die Argumentationskette unvollstaendig. Nach Fertigstellung von 4.6 und Nachruesten der Seitenangaben waere das Kapitel abgabereif.

---

# Detailbewertung: Kap. 4.5 — Human Oversight

> **Pruefobjekt:** Abschnitt 4.5 innerhalb Kapitel 4 Anforderungen.docx
> **Woerter:** ~450 (~1,5 Seiten) | Budget: 1,5 Seiten (chapter_structure)

## Score Kap. 4.5

| Dimension | Score | Kommentar |
|-----------|-------|-----------|
| Struktur | 4.5 | 3 Absaetze, sauberer Aufbau: Normanalyse → Operationalisierung → Architektur-Implikation |
| Roter Faden | 4.0 | Verknuepfung zu 4.3 (Gate-Pruefung als Voraussetzung) gut. Verweis auf 4.6 explizit. Rueckverweis auf 4.1 (Enforcement) implizit. |
| Stil | 4.5 | Keine Verstoesse. Komprimiert, jeder Satz traegt. Keine Floskeln. |
| Zitationen | 3.5 | 4 Kernquellen (Sterz, Laux, Enqvist, Ooms), aber KEINE Seitenangaben |
| Scope | 5.0 | Deployer-Provider-Asymmetrie explizit adressiert. Keine Scope-Verletzung. |

### Staerken von 4.5:

1. **Sterz-Laux-Synthese ist stark.** Die Kombination individueller Effektivitaetsbedingungen (Sterz) mit institutionellem Governance-Rahmen (Laux) ist eine eigene intellektuelle Leistung. Kein anderes Paper im Korpus hat diese Synthese so gemacht.

2. **Mapping Art. 14 Abs. 4 → Sterz-Bedingungen ist ueberzeugend.** Massnahmen (a)–(e) werden systematisch den 4 Bedingungen zugeordnet. Die identifizierte Luecke (Fitting Intentions ohne Normtext-Entsprechung) ist ein genuin analytischer Beitrag.

3. **First-Degree vs. Second-Degree Oversight → Architektur-Mapping.** Pre-Deployment/Deployment-Gates = First-Degree, Post-Deployment = Second-Degree. Das ist elegant und architektonisch verwertbar.

### Schwaechen von 4.5:

1. **Seitenangaben fehlen komplett.** Sterz et al. (2024) und Laux (2024) werden intensiv referenziert, aber nie mit "S. X". Das ist bei einer Masterarbeit ein Problem — besonders wenn spezifische Konzepte (4 Bedingungen, 6 Designprinzipien, First/Second-Degree) zitiert werden. **Fix: Ueber Zotero Fulltext oder PDF die Seitenangaben nachruesten.**

2. **Ooms et al. (2025) erscheint nur als Stuetz-Zitat.** Der Beitrag von Ooms (Policy-Prototyping, "zu vage"-Bewertung) koennte staerker in die Argumentation eingebaut werden — er stuetzt die Operationalisierungsluecke, die Sterz dann schliesst.

3. **Kein Satz zu den Limitationen von Sterz/Laux.** Beide Frameworks haben Grenzen (Sterz: empirisch nicht validiert; Laux: demokratietheoretisch, nicht technisch). Ein halber Satz wie "Die empirische Validierung dieser Bedingungen steht noch aus (vgl. Kap. 7)" wuerde die wissenschaftliche Redlichkeit staerken.

### Empfehlungen fuer 4.5:

1. **[WICHTIG] Seitenangaben nachruestfen:** Sterz et al. — wo stehen die 4 Bedingungen? Laux — wo steht First/Second-Degree-Taxonomie? Wo stehen die 6 Designprinzipien?
2. **[OPTIONAL] Limitation andeuten:** Ein Halbsatz zur fehlenden empirischen Validierung der Sterz-Bedingungen (→ Kap. 7)
3. **[OPTIONAL] Ooms staerker einbinden:** Nicht nur "zu vage", sondern explizit als Motivation fuer Sterz' Operationalisierung

## Ergebnis Kap. 4.5: ABGABEREIF (nach Seitenangaben-Fix)
