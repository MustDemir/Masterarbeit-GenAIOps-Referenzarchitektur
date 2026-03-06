# Preflight-Protokoll: Kap. 1.4 — Forschungsfragen

**Datum:** 2026-03-06 | **Gliederungs-SOT:** `1.4 Forschungsfragen (RQ1-RQ3, DSR-Cycle-Zuordnung)`

---

### Ergebnis P1 (Exposé): ✅ konsistent — verifiziert an Expose_v4.pdf S. 6
- **Exposé S. 6:** "Aus der Problemstellung und Zielsetzung werden drei Forschungsfragen abgeleitet, die den drei DSR-Zyklen (Relevance, Design, Rigor) nach Hevner et al. (2004) zugeordnet sind"
- RQ-Formulierungen im Exposé = identisch mit README.md ✅
- Exposé enthält nach RQ3 einen Evaluationsdetail-Absatz → gehört NICHT in 1.4 (→ Kap. 6)
- **Exposé-Struktur Kap. 1.4:** 1 Einleitungssatz + 3 RQs + 1 Evaluations-Absatz (~150W)

### Ergebnis P2 (Kapiteltexte):
- **DRAFT Kap. 1.3 letzter Satz:** "Die nachfolgenden Forschungsfragen operationalisieren diese Zielsetzung." → Brücke steht
- **Kap. 3 DOCX (Tabelle 2):** DSRM-Mapping vorhanden:
  - RQ1 → Design + Relevance Cycle → Kap. 4 (R-Katalog)
  - RQ2 → Design + Relevance Cycle → Kap. 5 (Referenzarchitektur + QG-Kontrollsystem)
  - RQ2 → Design Iter. 2 → Kap. 5.x (Azure-PoC)
  - RQ3 → Rigor Cycle → Kap. 6 (Coverage, Walkthrough, Expert-Reviews)
- **README.md — offizielle RQ-Formulierungen:**
  - **RQ1 (Relevance):** Welche regulatorischen, technischen und strategischen Anforderungen sind für eine verantwortungsnachweisbare Gestaltung von GenAI-Systemen im Enterprise-Kontext relevant und operationalisierbar?
  - **RQ2 (Design):** Wie kann eine Referenzarchitektur für GenAIOps gestaltet werden, die die erhobenen Anforderungen durch ein lifecycle-integriertes Quality-Gate-Kontrollsystem systematisch operationalisiert?
  - **RQ3 (Rigor):** Inwiefern ist die entwickelte Referenzarchitektur geeignet, regulatorische Anforderungen technisch durchzusetzen und auditierbar nachweisbar zu machen?
- **Terminologie aus 1.1–1.3:** PD1–PD3, S1–S4, Accountability-by-Design, Deployer-Scope, 3 Governance-Dimensionen, dreistufige Transformation

### Ergebnis P3 (Sessions/Files):
- **D_4.6_VS_5.3_SEPARATION:** RQ1 = WAS (Requirements R-xx), RQ2 = WIE (Gate-Specs G-xx) → DSR-logische Trennung
- **D_SCOPE_ART25_RETIREMENT:** Deployer-Scope Art. 26, Retirement ausgeschlossen
- **DSR-Cycle-Labels** (README): RQ1 = Relevance, RQ2 = Design, RQ3 = Rigor

### Ergebnis P4 (Entscheidungen):
- **Betroffene Decisions:** D_SCOPE_ART25_RETIREMENT, D_4.6_VS_5.3_SEPARATION
- **Neue Entscheidung nötig?** Nein — RQs sind stabil seit Exposé v4
- **Critical Definitions:** Deployer-Scope (Art. 26), Enforcement ≠ Dokumentation

### Ergebnis P5 (Quellen):
- **Pflicht-Zitat:** Hevner et al. (2004) `YUERCAVB` → 3 Zyklen (Relevance, Design, Rigor) — Exposé S. 6 nutzt genau diese Zuordnung
- Peffers et al. (2007) `Y24UGDM7` → optional für DSRM-Prozess (bereits in 1.3 zitiert, reicht evtl. Rückverweis)
- **Keine weiteren Zitationen nötig** — RQs sind eigene Formulierungen, Cycle-Zuordnung ist methodische Eigenleistung gestützt auf DSR-Rahmen

### Ergebnis P6 (Uni):
- **Seitenbudget:** Restbudget ~355–955 W für 1.4–1.6
- **1.4 Zielgröße:** ~100–150 W (~0,5 Seiten) — RQs knapp präsentieren, DSR-Cycle-Zuordnung als Kurzübersicht
- **Format:** Nummerierung nur bis 2. Ebene, RQs als Fließtext (NICHT als Aufzählung — akademisch)

---

### Synthese — Argumentationsstruktur für Kap. 1.4:

**Brücke von Kap. 1.3:** "Die nachfolgenden Forschungsfragen operationalisieren diese Zielsetzung."

| Absatz | Argumentativer Move | Logik (Warum hier?) | Brücke zum nächsten |
|--------|---------------------|---------------------|---------------------|
| 1 | RQ1 einführen (Relevance): Anforderungserhebung | Ziel (1.3) → Erste Frage: WAS muss adressiert werden? | RQ1 liefert Input für → |
| 2 | RQ2 einführen (Design): Architekturgestaltung | Anforderungen (RQ1) → WIE werden sie architektonisch umgesetzt? | RQ2 braucht Bewertung → |
| 3 | RQ3 einführen (Rigor): Evaluation | Architektur (RQ2) → Ist sie geeignet? Nachweis nötig | Alle 3 RQs → DSR-Verortung |

**Alternative:** Alle 3 RQs in EINEM Absatz + Cycle-Zuordnung in einem zweiten. Empfehlung: **2 Absätze** (kompakter, passt zum Budget).

| Absatz | Argumentativer Move | Logik | Brücke |
|--------|---------------------|-------|--------|
| 1 | 3 RQs formulieren + jeweils DSR-Cycle zuordnen | Operationalisierung der Zielsetzung aus 1.3 | → leitet über zu methodischer Einbettung |
| 2 | DSR-Cycle-Logik erklären (Relevance→Design→Rigor als Sequenz) + Kapitelzuordnung | Zeigt dem Leser den roten Faden der Arbeit | → Brücke zu 1.5 (Forschungsmethodik) |

**Brücke zu Kap. 1.5:** Methodische Verortung (DSR als Rahmen → Kap. 3 als Detail)

### Synthese — Inhalts-Checklist für Kap. 1.4:
- ☐ RQ1 Formulierung (Relevance Cycle → Kap. 4)
- ☐ RQ2 Formulierung (Design Cycle → Kap. 5)
- ☐ RQ3 Formulierung (Rigor Cycle → Kap. 6)
- ☐ DSR-Cycle-Zuordnung (Hevner 3 Zyklen)
- ☐ Kapitel-Mapping (RQ → Kapitel)
- ☐ Brücke zu 1.5

### Negativ-Checklist — Was darf NICHT in Kap. 1.4:
- ❌ Keine ausführliche DSR-Methodenbeschreibung (→ 1.5 + Kap. 3)
- ❌ Keine R-xx oder G-xx Details (→ Kap. 4/5)
- ❌ Keine Wiederholung der Problemdimensionen PD1–PD3 (→ 1.2)
- ❌ Keine DP1–DP5 Designprinzipien (→ Kap. 5.1)
- ❌ Keine Evaluationsdetails (→ Kap. 6)
- ❌ Keine formale Überleitung ("Im folgenden Kapitel...")
- ❌ Elia-Zitation VERMEIDEN (bereits in 1.2 + 1.3 zitiert)

### Offene Fragen (vor Schreiben klären):
- Keine — RQs sind stabil, DSR-Zuordnung klar

→ Bereit für "GO"
