# Preflight-Protokoll: Kap. 1.3 — Zielsetzung

> **Erstellt:** 2026-03-06 | **Workflow:** PREFLIGHT_CHECK_WORKFLOW.md

---

## Ergebnis P1 (Exposé + README)

**✅ Konsistent — README enthält vollständige Zielsetzung aus Exposé v4:**

Das Exposé/README definiert für 1.3:
- **Zielformulierung:** "Entwicklung einer cloud-nativen Referenzarchitektur für GenAIOps, die regulatorische, technische und strategische Anforderungen [...] durch ein lifecycle-integriertes Quality-Gate-Kontrollsystem systematisch operationalisiert."
- **Accountability-by-Design:** "Verantwortungsnachweisbarkeit wird nicht als nachgelagerter Dokumentationsprozess verstanden, sondern als technisch erzwungene Eigenschaft des Systems."
- **4 Säulen:** S1 Architektur, S2 QG-Kontrollsystem (USP), S3 Pipeline-Integration, S4 Evidence/Audit (USP)
- **5 Design-Prinzipien:** DP1–DP5
- **Artefakttyp:** Model + Method + Instantiation
- **Evaluation:** 3-stufig (Requirements-Coverage, PoC-Walkthrough, Expert-Reviews n≥4)

**⚠ Abweichung:** Exposé-Zielsetzung enthält DP1–DP5 und 4 Säulen inline — in der Thesis-Einleitung gehören diese Details in Kap. 3 (Artefaktdefinition) und Kap. 5 (Architektur). Kap. 1.3 muss **komprimierter** sein.

---

## Ergebnis P2 (Kapiteltexte Kap. 3/4/5)

**Relevante Begriffe/Definitionen aus Kap. 3–5 für 1.3:**

| Quelle | Was | Relevanz für 1.3 |
|--------|-----|-------------------|
| Kap. 3.4 | DSR-Artefakt: Model (Architektur) + Method (Gate-Systematik + Traceability) + Instantiation (Azure PoC) | ✅ Muss erwähnt werden (Artefakttyp) |
| Kap. 3.7 | Evaluation: 3-stufig (Coverage-Matrix, Walkthrough, Expert-Reviews) | ✅ Muss erwähnt werden |
| Kap. 4.1 | Enforcement ≠ Dokumentation, Accountability-by-Design | ✅ Bereits in 1.1/1.2 angelegt → Forward-Ref |
| Kap. 4.3 | Dreistufige Transformation: Norm → R-xx → G-xx | ✅ USP — erwähnen |
| Kap. 5.1 | DP1–DP5, NIST/ISO-Konvergenznachweis | ⚠ Nur implizit in 1.3, Detail in Kap. 5 |
| Kap. 5.3 | Quality-Gate-Kontrollsystem S2 (USP) | ✅ Zentral — Gate-Template als Differenzierungsmerkmal |
| Kap. 5.5 | Evidence- und Audit-Logik S4 (USP) | ✅ Muss erwähnt werden |
| Kap. 5.6 | PoC Azure/Healthcare (Ambient AI Scribe) | ✅ Muss erwähnt werden |
| Kap. 6.3–6.4 | Walkthrough + Expert-Reviews | ✅ Muss erwähnt werden |
| Gliederung v3 | S1–S4 Subsystem-Zuordnung | ✅ Strukturgebend |

---

## Ergebnis P3 (Sessions + chapter_state + Dateien)

**chapter_state Kap. 1:** Skelett (keine Decisions, kein content).

**Relevante Session-Inhalte:**
- **USP-Analyse (20260302_034720):** 7 USPs identifiziert, dreidimensionale Taxonomie als Novum
- **Related Work (related_work_vergleich_kap4.md):** MQG4AI = XAI/Medizin, Provider-Perspektive, kein CI/CD, kein Evidence Store
- **Pourmajidi-Vergleich:** Demir = upper-right quadrant (GenAI-spezifisch + formalisierte Governance)
- **DSR-Session (20260227_011854):** Design Knowledge Kernsatz formuliert
- **Kap. 4.1 Session (20260304_003014):** Accountability-by-Design, 6 Guidelines

**USP-Placement-Entscheidung (aus aktueller Session):**
- Kap. 1.3 = **Claim aufstellen** (was macht diese Arbeit anders)
- Kap. 2 = Claim belegen (Related Work Vergleich)
- Kap. 4–5 = Claim umsetzen
- Kap. 7 = Claim reflektieren

---

## Ergebnis P4 (Entscheidungen)

**Direkt betroffene Entscheidungen für Kap. 1.3:**

| Decision | Relevanz |
|----------|----------|
| D_SCOPE_ART25_RETIREMENT | Scope: Deployer (Art. 26), kein Provider, kein Retirement → muss in 1.3 implizit, explizit in 1.6 |
| D_4.6_VS_5.3_SEPARATION | WAS (4.6) vs. WIE (5.3) → Artefaktbeschreibung: "Requirements-Katalog (RQ1) + Gate-Spezifikation (RQ2)" |
| D_NIST_CONVERGENCE | Max. 1 Satz in 1.3: NIST/ISO-Konvergenz als Rigor-Anker erwähnen |
| D_GOV_DIMENSIONS_HYBRID | 3 Governance-Dimensionen (strategisch/technisch/compliance) als Strukturierungsmerkmal |
| D_MQG4AI_PLACEMENT | MQG4AI kurz erwähnen als Abgrenzung (1 Halbsatz) |

**Critical Definitions (einzuhalten):**
- Enforcement ≠ Dokumentation
- Deployer-Scope (Art. 26)
- Dreistufige Transformation (Norm → R → G)
- 3 Kontrollmechanismen (präventiv/reaktiv/retrospektiv)

---

## Ergebnis P5 (Quellen)

**Pflicht-Zitate für 1.3 (aus Exposé/Gliederung abgeleitet):**

| Quelle | Für | Zotero-Key |
|--------|-----|------------|
| EU AI Act VO 2024/1689 | Regulatorischer Rahmen | Gesetzestext |
| Hevner et al. (2004) | DSR-Methodik | `YUERCAVB` ✅ verifiziert |
| Peffers et al. (2007) | DSRM-Prozess | `NWMN9TFA` (Key aus Session-Historie) |
| Elia et al. (2025) | MQG4AI-Abgrenzung (1 Halbsatz) | `QRW95D4X` ✅ |
| Novelli et al. (2024) | Beweislast-Asymmetrie / Deployer | `YV4BV8CY` ✅ verifiziert |

**Optional (wenn Platz):**
- vom Brocke & Maedche (2019) für DSR Grid
- Tabassi (2023) / NIST AI RMF für Konvergenz-Verweis

---

## Ergebnis P6 (Uni-Anforderungen)

- **Seitenbudget:** Kap. 1.3 ≈ 250–350 Wörter (~1 Seite)
- **Gesamtbudget Kap. 1:** 5–7 Seiten, bisher ~845 Wörter (≈2,8 Seiten) → ~650–1.250 Wörter Rest für 1.3–1.6
- **Format:** Nummerierung bis 2. Ebene, Sub-Headings als **Fettdruck**, kein Aufzählungsstil
- **Zitationsdichte:** Hoch, aber in Zielsetzung etwas geringer als in 1.1/1.2 (weniger Belege, mehr Eigenaussagen)

---

## Synthese — Argumentationsstruktur für Kap. 1.3

**Brücke von Kap. 1.2:** Letzter Satz 1.2 fordert einen "integrativen, architekturbasierten Lösungsansatz" → 1.3 liefert genau diesen als Zielsetzung.

| Absatz | Argumentativer Move | Logik (Warum hier?) | Brücke zum nächsten |
|--------|---------------------|---------------------|---------------------|
| 1 — Zielformulierung | **Antwort auf 1.2**: Was soll gebaut werden? (DSR-Artefakt + Methodik benennen) | Schließt direkt an die 3 PDs an: PD1–PD3 → Ziel = Referenzarchitektur + QG-System | → Ziel ist abstrakt definiert → braucht Konkretisierung |
| 2 — Artefaktskizze + USP | **Konkretisierung**: Wie sieht das Artefakt aus? (S1–S4, 3 Dimensionen, Gate-Template, Abgrenzung MQG4AI) | Leser muss verstehen WAS genau gebaut wird und WARUM es neu ist | → Artefakt ist beschrieben → wie wird es validiert? |
| 3 — Instanziierung + Eval | **Validierung**: Wie wird bewiesen, dass es funktioniert? (PoC Azure + 3-stufige Evaluation) | Ohne Evaluation bleibt die Zielsetzung ein Versprechen | → Evaluation zeigt Rigor → was ist der Beitrag? |
| 4 — Beitrag + Anschluss | **So-What**: Warum ist das relevant? (Design Knowledge + Praxis + Wissenschaft) | Schließt den argumentativen Bogen: Problem → Lösung → Beweis → Impact | → Brücke zu 1.4 (Forschungsfragen als Operationalisierung) |

**Brücke zu Kap. 1.4:** Absatz 4 formuliert den Beitrag → 1.4 operationalisiert diesen als konkrete Forschungsfragen (RQ1–RQ3).

**Argumentativer Gesamtbogen Kap. 1.3:** `Problem (1.2) → Ziel → Artefakt → Beweis → Impact → Operationalisierung (1.4)`

---

## Synthese — Inhalts-Checklist für Kap. 1.3

### Absatz 1 — Zielformulierung (~80 Wörter)
☐ Zielaussage aus Exposé (komprimiert): Cloud-native Referenzarchitektur + QG-Kontrollsystem
☐ DSR als Methodik benennen (Hevner, Peffers) → Artefakttyp: Model + Method + Instantiation
☐ PD1–PD3 als Motivation rückverweisen (Brücke zu 1.2)
☐ Accountability-by-Design als Leitprinzip

### Absatz 2 — Artefaktskizze + USP-Claim (~80 Wörter)
☐ S1–S4 Subsysteme benennen (S2 + S4 als USP markieren)
☐ 3 Governance-Dimensionen (strategisch/technisch/compliance)
☐ Gate-Template (Trigger, Kriterien, Evidence, Decision, Owner, Audit Trail, Waiver)
☐ Dreistufige Transformation (Norm → R-xx → G-xx) als Differenzierungsmerkmal
☐ MQG4AI-Abgrenzung (1 Halbsatz: "Im Unterschied zu...")
☐ Policy-as-Code + Evidence Store als Automatisierungsebene

### Absatz 3 — Instanziierung + Evaluation (~70 Wörter)
☐ PoC auf Azure (AKS, Azure OpenAI Service) im Healthcare-Szenario (Ambient AI Scribe)
☐ 3-stufige Evaluation: Requirements-Coverage-Matrix + PoC-Walkthrough + Expert-Reviews (n≥4)
☐ DSR-Iteration: Iter. 1 konzeptuell, Iter. 2 Instanziierung

### Absatz 4 — Beitrag + Anschluss (~70 Wörter)
☐ Design Knowledge: übertragbare Muster/Prinzipien für GenAI-Governance
☐ Praxisbeitrag: sofort einsetzbare Gate-Templates für Deployer-Organisationen
☐ Wissenschaftlicher Anschluss: NIST AI RMF + ISO 42001 + EU AI Act Konvergenz (1 Satz)
☐ Deployer-Perspektive (Art. 26) explizit als Scope-Entscheidung

---

## Negativ-Checklist — Was darf NICHT in Kap. 1.3

- ❌ DP1–DP5 als Auflistung (gehört in Kap. 5.1)
- ❌ Vollständige Gate-Spezifikation oder Gate-Template-Felder (gehört in Kap. 5.3)
- ❌ Implementierungsdetails Azure/AKS/Services (gehört in Kap. 5.6)
- ❌ Requirements-Katalog R-01 ff. (gehört in Kap. 4.6)
- ❌ Elia et al. (2025) mit identischem Claim wie in Kap. 1.2 (Doppelzitation! → In 1.3 nur als Abgrenzung "Im Unterschied zu…", NICHT nochmal Provider-Fokus-Argument)
- ❌ Detaillierte Evaluationsmethodik (gehört in Kap. 3.7)
- ❌ Formale Überleitungen ("Im folgenden Kapitel wird…")

---

## Offene Fragen (vor Schreiben klären)

1. **Keine** — alle Entscheidungen sind FINAL, Struktur ist klar. Zotero-Keys verifiziert.

---

→ **Bereit für "GO"**
