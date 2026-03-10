# Bewertungsbericht: Kap. 2 — Theoretische Grundlagen und Stand der Forschung

> **Datum:** 2026-03-09
> **Reviewer:** thesis-reviewer Skill
> **Prüfobjekt:** `02_rigor_theorie_stand_forschung/Kap2_Theoretische_Grundlagen_DRAFT.md` (Fallback — DOCX-Integration ausstehend)
> **Wörter:** ~4062 (~13,5 Seiten) | Budget: ~4200W (~14 Seiten)

---

## Gesamtscore

| Dimension | Score | Gewicht | Gewichtet |
|-----------|-------|---------|-----------|
| R1 Struktur | 4.0 | 10% | 0.40 |
| R2 Roter Faden | 4.5 | 30% | 1.35 |
| R3 Stil/Uni-Vorgaben | 4.0 | 20% | 0.80 |
| R4 Zitationen | 3.5 | 15% | 0.53 |
| R5 Definitions/Scope | 4.5 | 10% | 0.45 |
| R6 Gutachter-Bewertung | 4.0 | 15% | 0.60 |
| **GESAMT** | | | **4.1 / 5.0** |

### Bewertungsskala
| Score | Note | Bedeutung |
|-------|------|-----------|
| 4.5–5.0 | Sehr gut | Abgabereif, minimale Korrekturen |
| **3.5–4.4** | **Gut** | **Solide, gezielte Verbesserungen empfohlen** |
| 2.5–3.4 | Befriedigend | Substanzielle Überarbeitung nötig |
| 1.5–2.4 | Ausreichend | Grundlegende Probleme |
| < 1.5 | Mangelhaft | Neu schreiben |

---

## R1 Struktur: 4.0 / 5

### Abschnitte und Budget

| Abschnitt | Wörter | Anteil | Absätze | Quellen | Bewertung |
|-----------|--------|--------|---------|---------|-----------|
| 2.1 Begriffsabgrenzung | 443 | 10,9% | 5 | 9+1 Gesetz | ✅ |
| 2.2 Generative KI/LLMs | 491 | 12,1% | 3 (2.2.1–2.2.3) | 6 | ✅ |
| 2.3 Cloud-native | 546 | 13,4% | 3 | 4 | ✅ |
| 2.4.1 MLOps→LLMOps | 588 | 14,5% | 3 | 7 | ✅ |
| 2.4.2 EU AI Act | 403 | 9,9% | 2 | 4+Gesetz | ✅ |
| 2.5 Quality Gates | 948 | **23,3%** | 5 | 11 | ⚠ überproportional |
| 2.6 Compliance-as-Code | 308 | **7,6%** | 2 | 3 | ⚠ knapp |
| 2.7 Synthese | 335 | 8,2% | 2 | 0 (Rückverweise) | ✅ |
| **Gesamt** | **4062** | **96,7%** | **25** | **~35 unique** | |

### Befunde

**Gliederungstiefe:** Max. 3 Ebenen (2.2.1, 2.2.2, 2.2.3 und 2.4.1, 2.4.2) — PK-F2 ✅ (≤ 4).

**Absatzstruktur:** Alle 25 Absätze folgen dem Muster Topic Sentence → Argument → Beleg → Schlussfolgerung. Kein Absatz hat < 3 oder > 8 Sätze. Jeder Absatz hat ein eingebettetes Prüfprotokoll mit BELEG/CLAIM/MATCH-Tabelle — vorbildliche Transparenz.

**Budget:** 4062W von 4200W genutzt (96,7%), 138W Reserve. Kein Budgetüberschreitung — PK-F3 ✅.

**Balance-Problem:** Kap. 2.5 Quality Gates (948W = 23,3%) ist 3× so lang wie Kap. 2.6 PaC (308W = 7,6%). Dies spiegelt zwar die inhaltliche Komplexität wider (2.5 behandelt Ursprung + CI/CD + KI-Übertragung + Governance + Lücke), erzeugt aber eine strukturelle Unwucht. **Empfehlung:** Akzeptabel, da 2.5 als Kern-Baustein für das USP-Artefakt (Quality-Gate-Kontrollsystem) fungiert und die inhaltliche Dichte dies rechtfertigt. Bei DOCX-Integration prüfen, ob 2.5 Abs. 4 (Governance-Perspektive) um ~50W gekürzt werden kann.

---

## R2 Roter Faden: 4.5 / 5

### Brücke rückwärts (Kap. 1 → Kap. 2)

**Kap. 1.6 (Scope) endet mit:** Deployer-Perspektive (Art. 26), Provider-Pflichten (Art. 16) explizit ausgeschlossen, rechtliche Analyse auf Art. 9–15 begrenzt.

**Kap. 2.1 beginnt mit:** LLM-Definition (Vaswani) → Foundation Models (Bommasani) → GenAI-System als Komposit → regulatorische Begriffe → RAG → LLMOps → Quality Gate → PaC.

**Befund:** ✅ Nahtloser Übergang. Kap. 1 definiert Scope → Kap. 2.1 definiert die zentralen Begriffe innerhalb dieses Scopes. Der Leser weiß nach Kap. 1 WAS untersucht wird, Kap. 2.1 klärt die WIE-Terminologie. Kein argumentativer Bruch.

### Argumentationskette innerhalb Kap. 2

| Übergang | Argumentativer Move | Logik | Bewertung |
|----------|---------------------|-------|-----------|
| 2.1 → 2.2 | Begriffe → technologische Tiefe (GenAI) | Begriffsdefinition → Funktionsweise | ✅ |
| 2.2 → 2.3 | Enterprise-Herausforderungen → Plattformanforderungen | Problem → Infrastruktur-Voraussetzung | ✅ |
| 2.3 → 2.4 | Plattform → Operationalisierung (MLOps/LLMOps + Regulation) | Infrastruktur → Prozesse + Regulierung | ✅ |
| 2.4 → 2.5 | Ops-Lücke + regulatorische Lücke → Kontrollmechanismus | Bedarf → Lösung (Quality Gates) | ✅ |
| 2.5 → 2.6 | QG konzeptionell, nicht enforced → Enforcement-Mechanismus | Lücke → Komplementärlösung (PaC) | ✅ |
| 2.6 → 2.7 | PaC infrastrukturell, nicht GenAI-spezifisch → dreifache Lücke | Letzte Lücke → Synthese | ✅ |

**5-Säulen-Struktur** ist klar erkennbar und konsistent mit roter_faden_tracker.md:
1. GenAI/LLMs (2.2) → neuartige Herausforderungen
2. Cloud-native (2.3) → Plattformfähigkeiten
3. Operationalisierung (2.4) → MLOps/LLMOps + EU AI Act
4. Quality Gates (2.5) → Kontrollmechanismus-Kandidat
5. Policy-as-Code (2.6) → Enforcement-Mechanismus

### Brücke vorwärts (Kap. 2 → Kap. 3)

**Kap. 2.7 Abs. 2 endet mit:** "Die Entwicklung eines solchen Artefakts erfordert einen konstruktiven Forschungsansatz, der theoretische Fundierung, iterative Artefaktkonstruktion und rigorose Evaluation systematisch verbindet."

**Kap. 3.1 beginnt mit:** "Wissenschaftliche Forschung in der Wirtschaftsinformatik bewegt sich im Spannungsfeld zweier komplementärer Paradigmen: Behavioral Science und Design Science."

**Befund:** ✅ Kap. 2.7 begründet den Bedarf an konstruktivem Forschungsansatz → 3.1 liefert exakt diesen Rahmen (DSR). Übergang ist inhaltlich motiviert, nicht formal ("Im Folgenden wird..."). Keine SRH-Regelverletzung.

### Konsistenz mit anderen Kapiteln

- Kap. 1 Problemdimensionen (PD1–PD3) korrespondieren implizit mit der dreifachen Forschungslücke in 2.7 ✅
- Kap. 3 DSR-Methodik knüpft an 2.7 Handlungsbedarf an ✅
- Forward-References auf Kap. 5.3 (Quality-Gate-Spezifikation) und 5.4.2 (PaC-Integration) sind inhaltlich plausibel, Texte dort aber noch nicht geschrieben → ⚠ Risiko toter Verweise bei Gliederungsänderung
- **Leichter Overlap:** 2.5 Abs. 5 identifiziert bereits die dreifache Lücke, 2.7 Abs. 1 wiederholt und verdichtet dies — akzeptabel für Synthese, aber ~2–3 Sätze Redundanz

---

## R3 Stil/Uni-Vorgaben: 4.0 / 5

### Gefundene Verstöße

| # | Typ | Stelle | Text | Fix |
|---|-----|--------|------|-----|
| 1 | PK-V1 | 2.4.1 Abs. 3 Ende | "...für die **im folgenden Abschnitt** behandelte regulatorische Rahmensetzung durch den EU AI Act." | Streichen: "...für die regulatorische Rahmensetzung durch den EU AI Act (Kap. 2.4.2)." |
| 2 | PK-V1 (borderline) | 2.5 Abs. 1 Ende | "...für die **nachfolgende** Einordnung von Quality Gates..." | Umformulieren: "...für die Einordnung von Quality Gates in automatisierte CI/CD-Pipelines." |
| 3 | PK-V1 (borderline) | 2.4.2 Abs. 2 Ende | "...die **im weiteren Verlauf** dieser Arbeit über Quality Gates (Kap. 2.5) und Policy-as-Code-Ansätze (Kap. 2.6) adressiert wird." | Akzeptabel — inhaltlich motivierter Forward-Reference, nicht formale Überleitung |

### Prof. Prinz Stil-Gebote

| Gebot | Befund | Bewertung |
|-------|--------|-----------|
| PK-G1 Argumentation | Jeder Absatz trägt zur Gesamtargumentation bei; kein Füllmaterial | ✅ |
| PK-G2 Abgrenzung | Begriffe werden systematisch abgegrenzt (LLM vs. GenAI-System, MLOps vs. LLMOps vs. GenAIOps, QG vs. PaC) | ✅ |
| PK-G3 Kompression | Text ist dicht; Informationsgehalt pro Satz hoch | ✅ |
| PK-G4 Definitionen | Jede Definition wird über Primärliteratur belegt und kontextualisiert | ✅ |
| PK-G5 Referenzierdichte | ~35 unique Quellen auf 25 Absätze = 1,4 Quellen/Abs. (Minimum: ~1.0) | ✅ |
| PK-G6 Gesamtbezug | DSR-Rigor-Cycle-Einbettung klar; Kap. 2 = Wissensbasis | ✅ |

### Passiv-Konstruktionen

Moderate Verwendung passiver Formulierungen, aber fast immer mit erkennbarem Akteur (z.B. "Elia und Bauer systematisieren...", "Cooper beschreibt..."). Kein systematisches PK-V5-Problem.

### Blablameter-Einschätzung

Niedrig. Text ist fakten- und belegdicht. Kein unnötiger Hintergrund, keine Allgemeinplätze.

### SRH 50/30/20 Einschätzung

- **Inhalt (50%):** Hohe Problemdurchdringung — 5 Grundlagen-Säulen werden systematisch aufgebaut und zur dreifachen Forschungslücke verdichtet. Eigenständiger Beitrag erkennbar (GenAIOps als Arbeitsdefinition, dreifache Lücke als originäre Synthese).
- **Methodik (30%):** Kap. 2 = Rigor Cycle — Rolle im DSR klar. Quellenarbeit systematisch (Systematic Mappings referenziert, Literaturauswahl nachvollziehbar).
- **Formalia (20%):** APA7 durchgehend. Budget eingehalten. Gliederung sauber. 2 leichte PK-V1-Verstöße.

---

## R4 Zitationen: 3.5 / 5

### Zitationsstatistik

| Metrik | Wert |
|--------|------|
| Gesamtzitationen (unique Quellen) | ~35 |
| Absätze mit Zitationen | 23/25 (2.7 = reine Rückverweise) |
| Zitationsdichte (Quellen/Absatz) | ~1,5 |
| Quellen 2024–2026 | ~20 (~57%) |
| Quellen mit Zotero-Key | ~30/35 (~86%) |
| Sekundärzitationen ("zitiert nach") | 2 (Paula, Flohr — via Elia & Bauer) |
| Prüfprotokolle | 15 (alle Absätze) |
| MATCH-Ergebnisse | ~55× ✅, ~5× ⚠, 0× ❌ |

### Problematische Zitationen

| # | Zitation | Problem | Schwere | Empfehlung |
|---|----------|---------|---------|------------|
| 1 | Humble & Farley (2010) | **NICHT in Zotero**, keine Seitenangabe | 🔴 KRITISCH | Zotero-Eintrag anlegen + Seitenangabe nachtragen (Standardwerk "Continuous Delivery", Kap. 5) |
| 2 | Kratzke (2023) | **NICHT in Zotero** (Buch "Cloud-native Computing, 2. Aufl.") | 🔴 KRITISCH | Zotero-Eintrag anlegen (chapter_state vermerkt dies bereits) |
| 3 | Corrêa & Mönig (2024, S. 4/5) | Seitenzahlen aus Textmarkern rekonstruiert | 🟡 MITTEL | Verifizierung gegen Whitepaper-PDF empfohlen |
| 4 | Guldimann et al. (2025, S. 3/12) | Seitenzahlen geschätzt | 🟡 MITTEL | Verifizierung gegen Preprint-PDF empfohlen |
| 5 | Billeter et al. (2024) | Offset-Korrektur (S.2 = Table I, offset=35) — bereits notiert | 🟢 GERING | Im DRAFT korrekt verwendet (S. 1, S. 2) |

### Zitationsqualität

- **Stärke:** Hohe Diversität — Systematic Mappings (Díaz-de-Arcaya, Kreuzberger), DSR-Methodik (Elia et al.), Regulierungsanalysen (Novelli, Guldimann), Seminal Works (Vaswani, Bommasani, Cooper, Lewis). Mix aus CS, IS und Legal.
- **Stärke:** Fast alle Zitationen mit PDF-Seitenangaben (D_PDF_SEITENZAHLEN)
- **Schwäche:** 2 Quellen fehlen in Zotero — muss vor Abgabe behoben werden
- **Schwäche:** 2 Quellen mit geschätzten Seitenangaben — Verifizierung ausstehend

---

## R5 Definitions/Scope: 4.5 / 5

### Critical Definitions Check

| Definition | Verwendung in Kap. 2 | Korrekt? |
|---|---|---|
| Enforcement ≠ Dokumentation | 2.5 Abs. 5: "integriert keine automatisierte Enforcement-Logik"; 2.6: PaC als Enforcement | ✅ |
| Deployer-Scope (Art. 26) | 2.1 Abs. 2: "aus der Deployer-Perspektive (Art. 26)"; 2.4.2: durchgehend Deployer | ✅ |
| Retirement out-of-scope | Nicht erwähnt — korrekt | ✅ |
| Dreistufige Transformation | In 2.7 implizit (Norm → technisch prüfbar) — noch nicht explizit mit R-xx/G-xx (gehört in Kap. 4) | ✅ |
| GenAIOps = Arbeitsdefinition | 2.4.1 Abs. 3: explizit als "Arbeitsdefinition" markiert, "bislang nicht als kanonischer Terminus etabliert" | ✅ |
| Quality Gate = 4 Konzepte | 2.5 Abs. 1: Criteria, Gatekeeper, Scoring System, Scope (Elia & Bauer, 2023, S. 3) | ✅ |

### Scope-Verstöße

Keine. Der Text bleibt durchgehend in der Deployer-Perspektive. Provider-spezifische Aspekte werden korrekt als Abgrenzung verwendet (z.B. "MQG4AI adressiert explizit die Provider-Perspektive des EU AI Act (Art. 17 QMS)" → als Lücke, nicht als eigener Beitrag).

### Decision-Alignment

| Decision | Eingehalten? |
|---|---|
| D_PDF_SEITENZAHLEN | ✅ (mit 2 Ausnahmen: Humble/Farley ohne Seite, Corrêa/Guldimann geschätzt) |
| D_KAP2_2_SUBSTRUKTUR | ✅ (2.2.1–2.2.3 vorhanden) |
| D_UNI_HINWEISE_SSOT | ✅ (Stil-Vorgaben beachtet, 2 leichte PK-V1-Verstöße) |

### Stale Metadata (prozedural, nicht textbezogen)

- `thesis_state.md` zeigt Kap. 2 bei 50% → chapter_state.yaml bei 85% → **Stale**
- `roter_faden_tracker.md` zeigt 50% → **Stale**
- Empfehlung: Bei nächstem `save.py`-Lauf aktualisieren

---

## R6 Gutachter-Bewertung: 4.0 / 5

### Top 3 Stärken

1. **Systematische Belegführung:** Jeder der 25 Absätze hat ein vollständiges Prüfprotokoll mit Zitat-Verbatim, Zotero-Key und MATCH-Bewertung. 55× ✅, 0× ❌. Dies ist für eine Masterarbeit ungewöhnlich rigoros und schafft vollständige Nachprüfbarkeit. Ein Gutachter kann jede Behauptung direkt in der Quelle verifizieren.

2. **Kohärente 5-Säulen-Argumentation:** Die Gliederung baut systematisch fünf Grundlagen-Stränge auf (GenAI → Cloud-native → Ops/Regulation → QG → PaC) und verdichtet sie in 2.7 zu einer dreifachen Forschungslücke, die direkt zum Artefakt-Bedarf überleitet. Der rote Faden ist von 2.1 bis 2.7 durchgehend erkennbar.

3. **Aktualität und Quellenqualität:** ~57% der Quellen stammen aus 2024–2026. Mix aus Systematic Mappings, DSR-Arbeiten, Regulierungsanalysen und Seminal Works. Keine erfundenen Quellen — alle über Prüfprotokolle verifiziert.

### Top 3 Schwächen

1. **Sektions-Balance:** Kap. 2.5 Quality Gates (948W = 23%) dominiert strukturell und ist dreimal so lang wie Kap. 2.6 PaC (308W). Der Leser könnte den Eindruck gewinnen, dass Quality Gates der alleinige Fokus sind, obwohl PaC als Enforcement-Schicht gleichwertig zum USP beiträgt. Kap. 2.6 könnte ~100W mehr vertragen (z.B. ein Absatz zu PaC-Tooling: OPA/Rego, Kyverno), was aber das Budget sprengen würde.

2. **Fehlende Zotero-Einträge:** Humble & Farley (2010) und Kratzke (2023) fehlen in Zotero. Humble & Farley hat zusätzlich keine Seitenangabe. Dies sind formale Pflichtvoraussetzungen für die Abgabe (PK-Z2). Dringend nachtragen.

3. **Geschätzte Seitenangaben:** Corrêa & Mönig (S. 4/5) und Guldimann et al. (S. 3/12) haben geschätzte bzw. rekonstruierte Seitenzahlen. Dies ist für D_PDF_SEITENZAHLEN nicht ausreichend — Verifizierung gegen die PDFs erforderlich.

### Priorisierte Empfehlungen

1. **[KRITISCH]** Humble & Farley (2010) → Zotero-Eintrag anlegen, Seitenangabe nachtragen (Kap. 5 "Deployment Pipeline" des Standardwerks "Continuous Delivery"). Ohne dies ist die Zitation APA7-inkonform.

2. **[KRITISCH]** Kratzke (2023) → Zotero-Eintrag anlegen. Quelle wird in 2.3 dreimal zitiert und ist Grundlage der Cloud-native-Argumentation.

3. **[WICHTIG]** PK-V1-Verstöße beheben: (a) "im folgenden Abschnitt" in 2.4.1 Abs. 3 → ersetzen durch direkten Kapitel-Verweis; (b) "nachfolgende" in 2.5 Abs. 1 → streichen oder umformulieren.

4. **[WICHTIG]** Seitenangaben verifizieren: Corrêa & Mönig (S. 4/5) und Guldimann et al. (S. 3/12) gegen PDF-Volltext prüfen.

5. **[OPTIONAL]** Stale Metadata: thesis_state.md und roter_faden_tracker.md auf 85% aktualisieren (prozedural, via save.py).

6. **[OPTIONAL]** 2.5 Abs. 5 / 2.7 Abs. 1 Overlap: Prüfen ob die Gap-Identifikation in 2.5 Abs. 5 um 1–2 Sätze gekürzt werden kann, da 2.7 dies vollständig aufnimmt.

---

## Ergebnis: ÜBERARBEITUNG EMPFOHLEN

**Gesamtnote: 4.1 / 5.0 — Gut.**

Das Kapitel ist strukturell und argumentativ solide. Die 5-Säulen-Struktur mit dreifacher Forschungslücke ist überzeugend aufgebaut. Die systematische Belegführung via Prüfprotokolle ist vorbildlich. Vor der Abgabe müssen die 2 fehlenden Zotero-Einträge, 2 geschätzten Seitenangaben und 2 PK-V1-Formulierungen bereinigt werden. Nach diesen gezielten Korrekturen (geschätzter Aufwand: ~30–45 min) ist das Kapitel abgabereif.
