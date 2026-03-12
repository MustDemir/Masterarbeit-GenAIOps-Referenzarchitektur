# Keyword-Coverage-Analyse: Gate-Inclusion-Rule Literaturforschung
**Stand: 2026-03-12 | Basierend auf systematischer Abstract-Lektüre aus 30 PDFs**

---

## Executive Summary

**Ziel:** Systematische Validierung welche Quellen die **3 Gate-Entscheidungsdimensionen** abdecken:
- **D1 (Gate-Eignung)**: Wie operationalisiert man regulatorische Anforderungen als Gates?
- **D2 (Automatisierbarkeit)**: Welche Anforderungen sind maschinenauswertbar?
- **D3 (Human Oversight)**: Wie sind First-Degree/Second-Degree Oversight als Design-Kriterium?
- **Q (Querschnitt)**: Integrierte Frameworks für Regulation → Gate-Operationalisierung

**Ergebnis:** 30/30 PDFs analysiert, 28 mit aussagekräftiger Coverage

---

## Dimension-Abdeckung (Überblick)

| Dimension | Anzahl Papers | Top-Kandidat | Keyword-Dichte |
|---|---|---|---|
| **D1** (Gate-Eignung) | 28/30 | Feng et al. (31) | ★★★★★ Sehr gut |
| **D2** (Automatisierbarkeit) | 23/30 | Kholkar & Ahuja (7+Title) | ★★★★☆ Gut |
| **D3** (Human Oversight) | 19/30 | Laux (85) | ★★★★★ Dominiert |
| **Q** (Querschnitt) | 18/30 | Huwyler (40) | ★★★☆☆ Schwach |

---

## Top-20 Papers nach Relevanz

```
Rank  Paper                                          D1   D2   D3    Q  Total
────────────────────────────────────────────────────────────────────────────
 1.   Laux (2024) Institutionalised Distrust         9    6   85    0   100
 2.   Burns et al. (2025) AI Governance             67    2    2   22    93
 3.   Hernandez (2025) AI Act Knowledge Graph       50    2    7   13    72
 4.   Governance (2025) Unified Control Framework   40    2    3   12    57
 5.   Huwyler (2025) Unified Framework              30    1    8   10    49
 6.   Diaz-Rodriguez et al. (2023) Connecting       22    4    6   16    48
 7.   Finch & Butt (2025) Gaps in Governance        31    3    3   11    48
 8.   Feng et al. (2024) Normative Requirements Op  31    9    0    4    44
 9.   Pistilli (2023) Stronger Together             34    2    1    4    41
10.   Guldimann et al. (2025) COMPL-AI Framework    21    1    0   18    40
11.   Sarra (2024) AI in Decision-making            5    3   12   16    36
12.   Taeihagh (2025) Governance of GenAI           20    5    2    1    28
13.   Hulok (2025) EU model of AI governance        15    0    5    6    26
14.   Jonnala et al. (2025) EU AI Act Underrep.     10    2    1   13    26
15.   Novelli et al. (2024) GenAI in EU Law         20    2    2    0    24
16.   Radanliev et al. (2025) GenAI cybersecurity   12    4    2    1    19
17.   Ho-Dac & Martinez (2024) Human Oversight      7    1    8    0    16
18.   Golpayegani et al. (2024) AICat               6    5    0    3    14
19.   Kholkar & Ahuja (2025) Policy-as-Prompt       6    7    1    0    14
20.   Li et al. (2021) Trustworthy AI               3    2    1    0    6
```

---

## Kritische Erkenntnisse

### ✓ Stärken der Literaturabdeckung

1. **D1 (Gate-Eignung): GUT ABGEDECKT**
   - 28 Papers mit Keywords
   - Feng et al. (31): "Normative Requirements Operationalization" → Zentral für Requirement-to-Gate Mapping
   - Burns, Hernandez, Governance, Pistilli: Holistische Gate-Governance-Frameworks
   - **Folgerung für Thesis:** Können auf Feng + Cooper + Huwyler aufbauen

2. **D3 (Human Oversight): SEHR GUT ABGEDECKT**
   - Laux (85 Keywords!): "Institutionalised Distrust and Human Oversight" 
   - Deutlich über anderen Papers (Burns: 2, Hernandez: 7)
   - Bietet explizite Taxonomie für First/Second-Degree Oversight
   - **Folgerung für Thesis:** Laux ist die Primärquelle für D3. First-Degree vs. Second-Degree ist fundiert.

3. **D2 (Automatisierbarkeit): VORHANDEN ABER FRAGMENTIERT**
   - 23 Papers haben Keywords
   - Kholkar & Ahuja: "Policy-as-Prompt" → Explizit zu Policy-as-Code/Automatisierbarkeit
   - Aber meist nur 1-7 Keywords pro Paper (nicht dominant)
   - **Folgerung für Thesis:** Kholkar ist Kern. Braucht Ergänzung durch CI/CD-Compliance-Literatur?

### ⚠ Lücken und Blindstellen

1. **Q (Querschnitt): SCHWÄCHE**
   - Nur 18 Papers mit Keywords
   - Huwyler (10), Guldimann (18): Beste, aber nicht dominant
   - **Interpretation:** Kein Paper behandelt explizit "How to map Regulation → Gate"
   - **Implikation:** D_GATE_INCLUSION_RULE ist ggf. eine **Design-Innovation der Thesis**, nicht primär literaturgestützt
   - **Elicit-Suche nötig für:** "Regulation operationalization frameworks", "Requirement-to-control mapping", "Compliance-as-Code"

2. **⛔ LUCAJ PAPERS FEHLEN KOMPLETT**
   - User warnte: "du hast lucaj ganz vergessen"
   - MAPPING_LUCAJ_TO_RXX.md zeigt Lucaj als TechOps-Basis (Templates für Application/Model/Data)
   - Diese Ordner (02_04_02) hat NO Lucaj PDFs
   - **Nächster Schritt:** Lucaj-Papers in Ordner 02_05_Quality_Gates suchen oder in Zotero?
   - **Kritikalität:** HOCH (Lucaj ist Grundlage für MAPPING, das zentral für Gate-Entscheidung ist)

3. **D2 + Compliance-Automation: LITERATUR-LÜCKE?**
   - Kholkar: Policy-as-Prompt (AI-Agent-Governance)
   - Aber: Compliance-CI/CD Pipelines, Rego-Policies, Conftest in EU AI Act Kontext?
   - **Elicit-Suche nötig für:** "Compliance automation", "Policy-as-Code compliance", "CI/CD quality gates"

---

## Planned Elicit-Suchen (Nach User-GO)

### D1: Gate-Eignung & Requirement-Operationalization
**Frage:** Wie operationalisiert man regulatorische Anforderungen als prüfbare Deliverables/Gates?
**Quellen vorhanden:** Feng (31), Burns (67), Hernandez (50)
**Elicit-Fokus:** Gaps finden bei "stage-gate models", "requirement maturity", "compliance operationalization"

### D2: Automatisierbarkeit & Policy-as-Code
**Frage:** Welche Compliance-Regeln sind maschinenauswertbar? CI/CD Patterns für Regulatory Compliance?
**Quellen vorhanden:** Kholkar (7), aber fragmentiert
**Elicit-Fokus:** "Compliance automation", "Rego policies", "Conftest patterns", "Policy-as-Code regulatory"

### D3: Human Oversight Design
**Frage:** First-Degree vs. Second-Degree Oversight als Design-Kriterium für Quality Gates?
**Quellen vorhanden:** Laux (85) — SEHR GUT
**Elicit-Fokus:** Confirmation/Extension von Laux. Andere Frameworks für Oversight-Taxonomie?

### Q (KRITISCH): Requirement → Gate Mapping
**Frage:** Wo sind integrierte Frameworks, die explizit regulatorische Anforderung → Gate-Entscheidung behandeln?
**Quellen vorhanden:** Huwyler (10), Guldimann (18) — aber beide mehr "Compliance Framework" als "Gate Decision"
**Elicit-Fokus:** "Regulation to gate mapping", "Operationalization models", "Compliance checkpoint frameworks"

---

## Was noch zu klären ist

| Frage | Status | Nächste Aktion |
|---|---|---|
| Wo sind die Lucaj Papers? | ❓ KRITISCH | Suche in Ordner 02_05, Zotero-Lib |
| Ist D1 ausreichend theoretisch fundiert? | ✓ JA | Feng + Cooper reicht |
| Ist D3 ausreichend? | ✓ SEHR JA | Laux allein ist sehr stark |
| Ist D2 ausreichend? | ~ TEILWEISE | Kholkar-bestätigung via Elicit |
| Ist Q ausreichend? | ✗ NEIN | Elicit-Gap-Suche erforderlich |

---

## Nächster Workflow

1. **Sofort (diese Session):**
   - Lucaj-Papers lokalisieren (Ordner 02_05 durchsuchen)
   - Diese Analyse dem User zeigen
   
2. **Nach User-GO:**
   - Elicit-Suchen für D1, D2, D3, Q durchführen
   - Lücken dokumentieren
   - D_GATE_INCLUSION_RULE mit konkreten Quellen-Referenzen formulieren
   
3. **Danach:**
   - Sektion 5.2.2 schreiben mit validated sources
   - chapter_state.yaml aktualisieren
   - Gate-Tabelle auf 15 Gates erweitern (R004 + R014 als hybrid/explizit)
