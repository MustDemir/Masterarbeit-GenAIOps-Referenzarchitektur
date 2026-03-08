## Preflight-Protokoll: Kap. 2.2 — Generative KI und LLMs

**Erstellt:** 2026-03-08
**Ziel-DRAFT:** `02_rigor_theorie_stand_forschung/Kap2_Theoretische_Grundlagen_DRAFT.md`

---

### Ergebnis P1 (Exposé): ✅ konsistent

- Exposé v4 nennt Kap. 2.2 als "Generative KI und LLMs" ohne weitere Sub-Gliederung.
- Exposé-Fokus: "theoretische Grundlagen generativer KI-Systeme als Basis für die Anforderungsanalyse und Architekturentwicklung."
- Kein Scope-Drift: 2.2 vertieft die in 2.1 eingeführten Konzepte (LLM, Foundation Model, GenAI-System) um die technisch-konzeptionellen Eigenschaften, die Enterprise-Herausforderungen begründen.

### Ergebnis P2 (Kapiteltexte): Relevante Begriffe aus 2.1 übernehmen

- **Kontinuität:** Kap. 2.1 endet mit: "Die konzeptionelle Fundierung beider Konzepte für den GenAI-Kontext erfolgt in den Abschnitten 2.5 und 2.6." → 2.2 muss NICHT an diesen Satz anknüpfen (der verweist auf 2.5/2.6). Stattdessen knüpft 2.2 an die Gesamtlogik von 2.1 an: Die Begriffe LLM, Foundation Model, GenAI-System wurden definiert → jetzt werden die technischen Eigenschaften vertieft.
- **Begriffe aus 2.1 (bindend):** LLM (Vaswani), Foundation Model (Bommasani), GenAI-System (Fernández-Llorca), RAG (Lewis), Compound System (Xu). KEINE Re-Definition, nur Rückverweis.
- **Gliederung v3:** "2.2 Generative KI und LLMs" — keine Sub-Abschnitte, flacher Abschnitt.
- **Forward-References prüfen:** 2.2 muss Grundlage für 2.4.1 (MLOps→LLMOps) und 2.5 (Quality Gates) legen → Enterprise-Herausforderungen (Halluzinationen, Evaluation) motivieren spätere Kontrollmechanismen.

### Ergebnis P3 (Sessions/Files): Keine offenen Inhalte

- `chapter_state.yaml` Kap. 2: next_steps listet "2.2 Generative KI und LLMs" als nächsten Schritt.
- Keine Session Summaries mit spezifischem 2.2-Inhalt.
- SSOT-Workflow-Session (20260308) betrifft nur Infrastruktur (Keyword-Mapping), nicht Inhalt.

### Ergebnis P4 (Entscheidungen): Keine spezifischen D_xxx für 2.2

- **D_UNI_HINWEISE_SSOT** (bindend): Hohe Zitationsdichte, keine formalen Überleitungen, Blablameter-Check.
- **Critical Definitions aus 2.1:** LLM, Foundation Model, GenAI-System — konsistent verwenden, nicht re-definieren.
- **Deployer-Scope (Art. 26):** In 2.2 noch nicht direkt relevant (regulatorisch erst ab 2.4.2), aber Enterprise-Perspektive durchhalten.
- **NEUE Arbeitsregel (User, 2026-03-08):** "Ausgewogene Nutzung verschiedener Paper — nicht immer dasselbe zitieren." → Kap. 2.2 soll NEUE Quellen priorisieren, Kap. 2.1-Quellen nur bei echtem Rückverweis.
- Keine offene Entscheidung blockiert das Schreiben.

### Ergebnis P5 (Quellen): Pflicht-Quellen + Diversitätsprinzip

**Diversitätsprinzip (Prof. Prinz):** Kap. 2.1 nutzte 9 Quellen (Vaswani, Bommasani, Fernández-Llorca, Lewis, Xu, Kreuzberger, Tantithamthavorn, Cooper, Rebbana). Kap. 2.2 soll überwiegend NEUE Quellen einsetzen.

**Pflicht-Quellen für Kap. 2.2 (NEU, nicht in 2.1 verwendet):**

| Quelle | Zotero-Key | Thema | PDF-OFFSET |
|--------|-----------|-------|------------|
| Feuerriegel et al. (2024) | `MG9RVJ7N` | GenAI-Konzeptualisierung, Model/System/Application, generative vs. diskriminative Modellierung | 110 |
| Wei et al. (2022) | `74K4MFA9` | Emergent Abilities, Scaling, Phase Transition | 0 |
| Huang et al. (2024) | `RFHFUTCY` | Halluzination-Taxonomie (factuality vs. faithfulness), Ursachen (data/training/inference) | 0 |
| Shankar et al. (2024) | `F6AAPHUZ` | LLM-Evaluation, Validators-Problem | 0 |

**Optionale Ergänzung (wenn Wortbudget erlaubt):**

| Quelle | Zotero-Key | Thema | Einsatz |
|--------|-----------|-------|---------|
| Zhao et al. (2026) | `FFI6879V` | Comprehensive LLM Survey (Buch) | Training-Pipeline, Alignment |
| Bandi et al. (2023) | `BRNAUYVH` | GenAI Requirements, Evaluation Metrics | Alternative Survey-Referenz |

**Quellen aus 2.1 — nur Rückverweis (KEINE dominante Nutzung):**
- Bommasani et al. (2021) — Foundation Models, Emergence/Homogenization (max. 1× Rückverweis)
- Vaswani et al. (2017) — Transformer (max. 1× Rückverweis, da bereits in 2.1 definiert)

### Ergebnis P6 (Uni-Anforderungen + DSR)

- **Seitenbudget:** Kap. 2 gesamt ~4.200W (~14 Seiten). Kap. 2.1 verbraucht ~443W (~1,5 Seiten). Restbudget 2.2–2.7: ~3.757W (~12,5 Seiten). → **Kap. 2.2 Ziel: ~500–600W (~2 Seiten).** 2.2 ist ein Grundlagen-Abschnitt, nicht der Kern-Beitrag.
- **Formatvorgaben:** Nummerierung nur bis 2. Ebene → keine Sub-Abschnitte in 2.2, Fließtext mit Absätzen.
- **DSR-Phase:** Rigor Cycle → Knowledge Base aufbauen. 2.2 liefert die technischen Grundlagen, die in 2.4/2.5 für die Ops- und Gate-Perspektive benötigt werden.
- **Scope-Drift-Check:** ✅ kein Drift. 2.2 behandelt GenAI/LLM-Grundlagen, NICHT Regulierung (→ 2.4.2), NICHT Ops (→ 2.4.1), NICHT Gates (→ 2.5).

---

### Synthese — Argumentationsstruktur für Kap. 2.2:

**Brücke von Kap. 2.1:** Kap. 2.1 definierte LLM als Transformer-basiertes Sprachmodell und GenAI-Systeme als Verbund aus Modell, Infrastruktur und Governance. → 2.2 vertieft nun die technischen Eigenschaften, die diese Systeme für den Enterprise-Betrieb herausfordernd machen.

| Absatz | Argumentativer Move | Logik | Brücke zum nächsten |
|--------|---------------------|-------|---------------------|
| 1 | GenAI als Modellierungsparadigma: generativ vs. diskriminativ, Modalitäten | Feuerriegel: Konzeptualisierung auf Model/System/Application-Ebene. Abgrenzung zu 2.1: dort Definition, hier technische Vertiefung | → Foundation Models als spezielle Ausprägung |
| 2 | Foundation Models: Scaling, Emergence, Homogenization | Wei: Emergent Abilities als Phasenübergang. Bommasani (Rückverweis): Emergence + Homogenization als Schlüsseleigenschaften | → Enterprise-Implikationen: Was bedeutet Emergence für Qualitätssicherung? |
| 3 | Enterprise-Herausforderungen: Halluzinationen, Evaluation, Nicht-Determinismus | Huang: Halluzination-Taxonomie. Shankar: Evaluation-Validität. Diese Risiken begründen Quality Gates und Monitoring | → Überleitung zu 2.3 (Cloud-native Plattform als Betriebsgrundlage) |

**Brücke zu Kap. 2.3:** Der letzte Satz sollte auf die Plattformanforderungen überleiten: Die genannten Herausforderungen erfordern eine leistungsfähige Betriebsumgebung → 2.3 Cloud-native Plattformfähigkeiten.

### Inhalts-Checklist:
☐ Generative Modellierung: Definition, Abgrenzung diskriminativ (Feuerriegel)
☐ Modalitäten (Text, Bild, Code) — kurz, da nicht Fokus der Arbeit
☐ Foundation Models: Emergence + Homogenization (Wei, Bommasani-Rückverweis)
☐ Training-Paradigma: Pre-Training + Fine-Tuning + RLHF — max. 1-2 Sätze
☐ Halluzinationen als Kernrisiko (Huang: factuality vs. faithfulness)
☐ Evaluations-Herausforderung (Shankar: Who Validates the Validators)
☐ Enterprise-Implikation: Warum diese Eigenschaften Quality Gates erfordern

### Negativ-Checklist — Was darf NICHT in Kap. 2.2:
- ❌ RAG-Details (bereits in 2.1 behandelt, Vertiefung optional in 2.4)
- ❌ MLOps/LLMOps-Praktiken (→ 2.4.1)
- ❌ EU AI Act / Regulierung (→ 2.4.2)
- ❌ Quality-Gate-Definitionen (→ 2.5, bereits in 2.1 eingeführt)
- ❌ Cloud-native Infrastruktur (→ 2.3)
- ❌ Policy-as-Code (→ 2.6, bereits in 2.1 eingeführt)
- ❌ Provider-Perspektive (Art. 16) — Deployer-Scope beachten
- ❌ Re-Definition von Begriffen aus 2.1 (LLM, Foundation Model, GenAI-System)
- ❌ Übermäßige Beispiel-Aufzählungen (GPT-4, Claude, etc.) — akademisch bleiben

### Pflicht-Zitate:
- Feuerriegel et al. (2024) — GenAI-Konzeptualisierung, generative Modellierung (S. 112)
- Wei et al. (2022) — Emergent Abilities Definition (S. 2)
- Huang et al. (2024) — Halluzination-Taxonomie (S. 1:2)
- Shankar et al. (2024) — LLM-Evaluation Validitätsproblem

### Diversitäts-Tracking:
| Kapitel | Quellen (Erstverwendung) |
|---------|-------------------------|
| 2.1 | Vaswani, Bommasani, Fernández-Llorca, Lewis, Xu, Kreuzberger, Tantithamthavorn, Cooper, Rebbana |
| **2.2** | **Feuerriegel, Wei, Huang, Shankar** (+Bommasani Rückverweis) |

### Offene Fragen (vor Schreiben klären):
- Keine — alle Prüfinstanzen bestanden. Quellenlage ist ausreichend.

→ **Bereit für "GO"**
