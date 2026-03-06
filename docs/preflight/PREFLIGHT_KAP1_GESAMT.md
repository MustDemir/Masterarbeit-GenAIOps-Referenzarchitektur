# Preflight-Protokoll: Kap. 1 — Einleitung (Gesamt + 1.1 + 1.2 retroaktiv)

> **Erstellt:** 2026-03-06 | **Typ:** Retroaktiv (1.1/1.2 bereits geschrieben) + Vorausschau (1.3–1.6)
> **Workflow:** PREFLIGHT_CHECK_WORKFLOW.md

---

## TEIL A: Kap. 1 Gesamtkapitel

### Ergebnis P1 (Exposé + README)

**✅ README/Exposé enthält vollständige Kap.-1-Struktur:**

| Exposé-Abschnitt | Thesis-Mapping | Status |
|---|---|---|
| Einleitung (PD1–PD3 + Synthese) | 1.1 + 1.2 | ✅ Geschrieben |
| Zielsetzung (S1–S4, DP1–DP5, Accountability-by-Design) | 1.3 | ❌ Offen |
| Forschungsfragen (RQ1–RQ3) | 1.4 | ❌ Offen |
| Methodik (DSR, Hevner/Peffers/vom Brocke, Evaluation) | 1.5 | ❌ Offen |
| Scope und Abgrenzung (Healthcare PoC, Azure, Out-of-Scope) | 1.6 | ❌ Offen |

**⚠ Abweichungen Exposé → Thesis:**
- D2: Beweislast-Asymmetrie (Novelli) fehlt im Exposé → **IN ARBEIT** (in 1.2 umgesetzt ✅)
- D3: MQG4AI nicht im Exposé → **GEPLANT** (Kurzreferenz in 1.3)
- D4: Human Oversight (4.5) nicht im Exposé → **AKZEPTIERT** (nicht in Kap. 1, sondern Kap. 4)
- Exposé hat DP1–DP5 inline in Zielsetzung → Thesis: komprimierter in 1.3, Detail in Kap. 3/5

### Ergebnis P2 (Kapiteltexte Kap. 3/4/5)

**Begriffe/Definitionen die in Kap. 1 konsistent sein MÜSSEN:**

| Begriff | Definition (SOT: Kap. 3/4) | In 1.1? | In 1.2? |
|---|---|---|---|
| GenAI | Feuerriegel (2024, S. 111) | ✅ | — |
| MLOps → LLMOps → GenAIOps | Joshi (2025, S. 7–8) | ✅ | ✅ |
| EU AI Act Art. 9–15 | Gesetzestext | ✅ | ✅ |
| PD1/PD2/PD3 | SOT: gliederung_v3.md / Kap. 3 | — | ✅ |
| Deployer (Art. 26) | D_SCOPE_ART25_RETIREMENT | — | ✅ |
| Beweislast-Asymmetrie | Novelli (2024, S. 10, 14) | — | ✅ |
| Art. 25 Eskalation | D_ART25_DEPTH | — | ✅ |
| Enforcement ≠ Dokumentation | Critical Definition Kap. 4.1 | — | Implizit (Claim → 1.3) |
| Quality Gate | Noch nicht definiert in Kap. 1 | — | Erwähnt |
| Dreistufige Transformation | Critical Definition Kap. 4.3 | — | — (→ 1.3) |

### Ergebnis P3 (Sessions + chapter_state)

**chapter_state Kap. 1:** Skelett — keine `done`, keine `decisions`, keine `key_sources`
**→ MUSS nach Abschluss Kap. 1 aktualisiert werden.**

**Relevante Session-Erkenntnisse für Gesamtkapitel:**
- Seitenbudget: 5–7 Seiten (~1.500–2.100 W), bisher ~845 W → ~650–1.250 W Rest für 1.3–1.6
- USP-Placement: Kap. 1.3 = Claim, Kap. 2 = Belegen, Kap. 4–5 = Umsetzen, Kap. 7 = Reflektieren
- Keine formalen Überleitungen (Uni-Regel)
- Nummerierung nur bis 2. Ebene

### Ergebnis P4 (Entscheidungen)

**Entscheidungen die Kap. 1 insgesamt betreffen:**

| Decision | Betrifft | Umgesetzt? |
|---|---|---|
| D_SCOPE_ART25_RETIREMENT | 1.2 (Art. 25 erwähnt), 1.6 (Scope) | ✅ 1.2 / ❌ 1.6 |
| D_MQG4AI_PLACEMENT | 1.3 (Kurzreferenz) | ❌ 1.3 |
| D_NIST_CONVERGENCE | 1.3 (max 1 Satz) | ❌ 1.3 |
| D_GOV_DIMENSIONS_HYBRID | 1.3 (3 Dimensionen erwähnen) | ❌ 1.3 |
| D_4.6_VS_5.3_SEPARATION | 1.3 (Artefaktbeschreibung) | ❌ 1.3 |
| D_RETIREMENT_OUT | 1.6 (Scope-Abgrenzung) | ❌ 1.6 |

### Ergebnis P5 (Quellen — Gesamtkapitel)

**Quellen-Inventar Kap. 1:**

| Quelle | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
|---|---|---|---|---|---|---|
| Feuerriegel et al. (2024) | ✅ | — | — | — | — | — |
| Joshi (2025) | ✅ | ✅ | — | — | — | — |
| Tantithamthavorn et al. (2025) | ✅ | — | — | — | — | — |
| EU AI Act VO 2024/1689 | ✅ | ✅ | ✅ | — | — | ✅ |
| Guldimann et al. (2025) | ✅ | ✅ | — | — | — | — |
| Buscemi et al. (2025) | ✅ | ✅ | — | — | — | — |
| Kreuzberger et al. (2023) | ✅ | ✅ | — | — | — | — |
| Elia et al. (2025) | ✅ | ✅ | ✅ | — | — | — |
| Novelli et al. (2024) | — | ✅ | — | — | — | — |
| Diaz-De-Arcaya et al. (2024) | — | ✅ | — | — | — | — |
| Nellutla (2025) | — | ✅ | — | — | — | — |
| Billeter et al. (2024) | — | ✅ | — | — | — | — |
| Hevner et al. (2004) | — | — | ✅ | — | ✅ | — |
| Peffers et al. (2007) | — | — | ✅ | — | ✅ | — |
| NIST AI RMF (Tabassi, 2023) | — | — | ✅? | — | — | — |

### Ergebnis P6 (Uni-Anforderungen)

- **Seitenbudget:** 5–7 Seiten gesamt
- **Bisher:** ~845 W (1.1: ~315 W, 1.2: ~530 W) ≈ 2,8 Seiten
- **Restbudget:** ~650–1.250 W für 1.3–1.6
  - 1.3 Zielsetzung: ~250–350 W
  - 1.4 Forschungsfragen: ~150–200 W
  - 1.5 Methodik: ~150–200 W
  - 1.6 Scope: ~200–300 W
- **Format:** Nummerierung bis 2. Ebene, Fettdruck-Subheadings, keine Aufzählungen, keine formalen Überleitungen
- **Zitationsdichte:** Hoch in 1.1/1.2 (je ~7–9 Quellen), moderater in 1.3–1.6

---

## TEIL B: Kap. 1.1 — Retroaktiver Preflight

### P1-Check: Exposé-Konsistenz
✅ **Konsistent.** Exposé enthält PD1–PD3 als Treiber → 1.1 führt alle drei Dimensionen ein und verweist auf 1.2.

### P2-Check: Kapiteltext-Konsistenz
✅ **Konsistent mit Kap. 3/4.** Terminologie (GenAI, MLOps, LLMOps, GenAIOps) stimmt mit Kap. 3 Session-Summaries überein. PD-Bezeichnungen nicht in 1.1 (korrekt — erst 1.2).

### P3-Check: Session-Inhalte
✅ **Berücksichtigt.** Beweislast-Asymmetrie (Session-Thema) bewusst NICHT in 1.1, sondern in 1.2 (PD3).

### P4-Check: Entscheidungen
✅ **Keine Entscheidungskonflikte.** 1.1 ist thematisch vor den meisten Decisions.

### P5-Check: Quellen-Vollständigkeit
✅ **6 Quellen + 1 Gesetzestext, alle mit Seitenzahl, alle verifiziert (Prüfprotokoll vorhanden).**

**⚠ Potentielles Issue:** Elia (2025, S. 3) wird in 1.1 UND 1.2 zitiert mit ähnlichem Claim. Das ist akzeptabel (1.1 = Forschungslücke, 1.2 = PD2-Vertiefung), aber darauf achten, dass es in 1.3 nicht nochmal identisch kommt.

### P6-Check: Uni/Format
✅ ~315 Wörter ≈ 1 Seite. Keine Aufzählungen, keine formalen Überleitungen, 4 Absätze.

### Retroaktives Urteil Kap. 1.1: ✅ BESTANDEN

---

## TEIL C: Kap. 1.2 — Retroaktiver Preflight

### P1-Check: Exposé-Konsistenz
✅ **Konsistent.** Exposé benennt PD1–PD3 in der Problemdimensionen-Tabelle des README. Wortlaut weicht leicht ab (Thesis ist ausführlicher), Kern identisch.

**⚠ Abweichung D2:** Beweislast-Asymmetrie (Novelli) fehlt im Exposé, ist aber in 1.2 prominent. → **AKZEPTIERT** (stärkt Argumentation, Gutachter-kompatibel).

### P2-Check: Kapiteltext-Konsistenz

| Prüfpunkt | Ergebnis |
|---|---|
| PD1/PD2/PD3-Bezeichnungen SOT-konform? | ✅ Identisch mit gliederung_v3.md und Kap. 3 |
| Deployer-Scope (Art. 26) konsistent mit D_SCOPE_ART25_RETIREMENT? | ✅ Art. 26 Deployer-Pflichten korrekt dargestellt |
| Art. 25 Eskalation konsistent mit D_ART25_DEPTH? | ✅ 1 Satz am Ende PD3 (nicht eigener Sub-Abschnitt → Decision-konform) |
| Enforcement ≠ Dokumentation? | ⚠ Noch nicht explizit in 1.2 — wird in 1.3 eingeführt |
| Art. 10 Daten-Governance Abgrenzung? | ✅ In PD3 korrekt: Art. 10 erwähnt, aber Kap. 4 schließt Art. 10 Abs. 2 aus (Deployer-Scope) |

### P3-Check: Session-Inhalte
✅ **Alle Session-Themen berücksichtigt:**
- Beweislast-Asymmetrie ✅ (Novelli, 2024)
- GPAI/API-Asymmetrie ✅ (Art. 51 ff.)
- Art. 25 Deployer→Provider ✅
- Interdependenz PD1↔PD2↔PD3 ✅ (Schlussabsatz)

### P4-Check: Entscheidungen

| Decision | In 1.2 umgesetzt? |
|---|---|
| D_SCOPE_ART25_RETIREMENT | ✅ Art. 25 erwähnt, Retirement nicht erwähnt (korrekt — kommt in 1.6) |
| D_ART25_DEPTH | ✅ 1 Satz, kein eigener Abschnitt |
| D_RETIREMENT_OUT | ✅ Nicht erwähnt in 1.2 (korrekt — 1.6) |
| D_MQG4AI_PLACEMENT | ⚠ MQG4AI nicht namentlich in 1.2 — nur Elia (2025) als "kein vergleichbarer Ansatz". Akzeptabel: Name kommt in 1.3/2.7 |

### P5-Check: Quellen-Vollständigkeit
✅ **9 Quellen + 2 Gesetzestexte, alle mit Seitenzahl, alle verifiziert (Prüfprotokoll vorhanden).**

**Quellen-Analyse:**
- PD1: 3 Quellen (Kreuzberger, Diaz-De-Arcaya, Joshi) → ✅ Ausreichend
- PD2: 3 Quellen (Nellutla, Billeter, Elia) → ✅ Ausreichend
- PD3: 5 Quellen (EU AI Act, Novelli ×2, Guldimann, Buscemi) → ✅ Stark
- PD3 ist bewusst am längsten (zentrale Problemdimension) → ✅

### P6-Check: Uni/Format
✅ ~530 Wörter ≈ 1,8 Seiten. Fettdruck-Subheadings (PD1/PD2/PD3), keine Nummerierung 1.2.1, keine formalen Überleitungen.

**⚠ Längen-Asymmetrie:** PD3 (~220 W) > PD1 (~120 W) + PD2 (~120 W). Das ist bewusst: PD3 ist die zentrale Problemdimension (Beweislast-Asymmetrie als Kern-Argument). Aber prüfen ob Gutachter die Asymmetrie bemängelt → Ggf. in Revision PD1/PD2 leicht erweitern.

### Retroaktives Urteil Kap. 1.2: ✅ BESTANDEN (1 Minor ⚠)

**Minor ⚠:** PD3 ist ~2× so lang wie PD1/PD2. Akzeptabel für Erstfassung, ggf. in Revision ausgleichen.

---

## TEIL D: Synthese — Cross-Check 1.1 ↔ 1.2

| Prüfpunkt | Ergebnis |
|---|---|
| Terminologische Konsistenz 1.1 → 1.2 | ✅ Gleiche Quellen, gleiche Begriffe |
| Elia (2025) Doppelzitation 1.1 + 1.2 | ⚠ Akzeptabel: 1.1 = Forschungslücke, 1.2 = PD2. Unterschiedlicher Kontext. |
| Guldimann (2025) + Buscemi (2025) in beiden | ⚠ Akzeptabel: 1.1 = kurz eingeführt, 1.2 = PD3-Vertiefung |
| "Dreifache Lücke" aus 1.1 → PD1/PD2/PD3 in 1.2 | ✅ Saubere Brücke |
| Schlussabsatz 1.2 → Brücke zu 1.3 | ✅ "integrativen, architekturbasierten Lösungsansatz" → 1.3 Zielsetzung |
| Keine Forward-Refs zu nicht-existierenden Abschnitten | ✅ |

---

## Offene Punkte (bei Revision Kap. 1 adressieren)

1. **chapter_state.yaml Kap. 1** aktualisieren nach Fertigstellung 1.3–1.6
2. **PD-Längen-Asymmetrie** in Revision prüfen
3. **Enforcement ≠ Dokumentation** erst ab 1.3 explizit → sicherstellen dass Kap. 1 insgesamt konsistent
4. **Elia-Doppelzitation** in 1.3 NICHT nochmal mit identischem Claim verwenden
