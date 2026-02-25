# Architekturvergleich: Demir (2026) vs. Mahr et al. (2024)
## Stand: 25.02.2026

---

## 1. Bibliographische Daten

| | **Demir (2026)** | **Mahr et al. (2024)** |
|---|---|---|
| Typ | Masterarbeit (DSR) | IEEE Conference Paper (5 S.) |
| Methode | Design Science Research (Hevner) | Nicht spezifiziert |
| Artefakt | Enterprise-Referenzarchitektur + Quality-Gate-Framework | Referenzarchitektur für LLM-Deployment |
| Kontext | Enterprise, cloud-native, reguliert | Industrie/Fertigung (Shopfloor + Office) |
| Beteiligte | SRH Hochschule | FAU Erlangen + Siemens AG |
| DOI | — | 10.1109/SIITME63973.2024.10814877 |

---

## 2. Architektur-Struktur im Direktvergleich (nach PDF-Analyse)

### Mahr et al. Fig. 1 — 5 vertikale Blöcke:
1. **Data Preparation:** Data Source → Knowledge Base → Chunks → Tokenizer → Vectors → Vector Database / Data Lake
2. **Model Strategies:** 5 Strategien (Development from scratch, Commercial Model, PEFT, Full Finetuning, RAG) — inkl. detaillierter RAG-Flow mit Retrieval Model + Similarity Search
3. **Model Evaluation:** Task-spezifisch (Question Answering, Text Generation, Summarization, Translation, Classification) mit qualitativen + quantitativen Metriken (BLEU, Perplexity, Social Bias, Truthfulness, ROUGE, METEOR, Precision/Recall/F1) → Passed Evaluation → Model Registry → Feedback Pipeline → Human Feedback → Reward Model
4. **Deployment Strategies:** 3 Ansätze (Local Prompting/vEdge, API Call Prompting/Edge→Cloud, Digital Workplace/Cloud) — Shopfloor vs. Office differenziert
5. **Prompt Engineering:** Zero-shot, One-shot, Few-shot

### Demir Fig. (Artifact Construction) — 4 vertikale Säulen:
1. **Architekturentwurf:** Methode + Prinzipien + Generisch/PoC → Schichten-/Modulmodell
2. **Quality-Gate-Framework (USP):** Gate-Template (Trigger→Kriterien→Evidenz→Entscheidung→Owner→Audit Trail→Waiver) + 3 Dimensionen
3. **Pipeline-Integration:** CI/CD/CT + GitOps + Supply-Chain-Security → Automatisierte Pipeline
4. **Compliance-Operationalisierung (USP):** AI-Act-Mapping + Evidence Store → Audit Trail

### Fundamentaler Strukturunterschied:
- **Mahr = WAS** (welche Komponenten braucht man für ein LLM-System?)
- **Demir = WIE + WANN + WARUM** (wie kontrolliert, automatisiert und auditiert man den Betrieb?)

Mahr beschreibt die **Bauteile** eines LLM-Systems. Demir beschreibt die **Betriebslogik** — wann wird geprüft, was passiert bei Fail, wie wird Compliance nachgewiesen.

---

## 3. Lifecycle-Phasen im Vergleich

| Phase | **Demir** | **Mahr et al.** | Diff |
|-------|-----------|-----------------|------|
| DATA (Datenvorbereitung) | ✅ konzeptionell | ✅ "Data Preparation" | 🟡 Beide vorhanden |
| MODEL (Training/Fine-Tuning) | ✅ konzeptionell | ✅ "Model Training" + LLM-Typen | 🟡 Beide vorhanden |
| EVAL (Evaluation) | ✅ **PoC-Scope** | ✅ "Model Evaluation" | 🟡 Beide vorhanden, unterschiedliche Tiefe |
| DEPLOY (Deployment) | ✅ **PoC-Scope** | ✅ "Model Deployment" (2 Locations) | 🟡 Mahr: Shopfloor vs. Office; Demir: K8s/GitOps |
| PROD (Betrieb/Monitoring) | ✅ **PoC-Scope** | ⚠️ Implizit (nicht als eigene Phase) | 🔴 **Demir hat PROD explizit** |
| RETIRE (Dekommissionierung) | ✅ konzeptionell | ❌ Nicht adressiert | 🔴 **Nur Demir** |
| Prompt Engineering | ⚠️ Nicht als Phase | ✅ Eigene Phase | 🔴 **Nur Mahr** |

**Fazit Lifecycle:** Mahr hat 5 Phasen (linear), Demir hat 6 Phasen (zyklisch). Mahr endet bei Deployment, Demir geht weiter bis PROD und RETIRE. Mahr hat Prompt Engineering als eigene Phase — bei Demir ist das in EVAL/PROD eingebettet.

---

## 3. Architektur-Dimensionen im Vergleich

| Dimension | **Demir** | **Mahr et al.** |
|-----------|-----------|-----------------|
| **Säule 1: Architekturentwurf** | ✅ Cloud-native, K8s, IaC, Microservices | ⚠️ Implizit (Infrastruktur wird erwähnt, nicht formalisiert) |
| **Säule 2: Quality-Gate-Framework** | ✅ **USP** — Gate-Template mit 3 Dimensionen | ❌ **Nicht vorhanden** |
| **Säule 3: Pipeline-Integration** | ✅ CI/CD/CT, GitOps, Supply-Chain-Security | ❌ Keine Pipeline-Automatisierung beschrieben |
| **Säule 4: Compliance-Operationalisierung** | ✅ **USP** — AI-Act-as-Code, Evidence Store | ❌ **Nicht vorhanden** |

**Fazit Dimensionen:** Mahr deckt nur Teile von Säule 1 ab. Säulen 2–4 existieren bei Mahr nicht — das ist der Kern deiner Differenzierung.

---

## 4. Gemeinsamkeiten (was beide haben)

| Aspekt | Details |
|--------|---------|
| **Artefakttyp** | Beide entwickeln eine "Referenzarchitektur" für LLM-Systeme |
| **Lifecycle-Orientierung** | Beide strukturieren entlang von Phasen (Data → Train → Eval → Deploy) |
| **Model Evaluation** | Beide betonen Evaluation als kritische Phase |
| **Deployment-Herausforderung** | Beide adressieren die Komplexität des LLM-Deployments |
| **Standardisierung** | Beide wollen fragmentierte Prozesse vereinheitlichen |
| **Praxisbezug** | Demir: Azure PoC; Mahr: Siemens/Shopfloor |

---

## 5. Unterschiede (was nur Demir hat)

| Aspekt | **Nur Demir** | Bedeutung |
|--------|--------------|-----------|
| **Quality Gates** | Formalisierte Kontrollpunkte mit Trigger → Kriterien → Evidenz → Entscheidung → Owner → Audit Trail → Waiver | **USP 1** — konzeptionelle Neuheit |
| **3 Gate-Dimensionen** | Strategisch + Technisch + Compliance | Multidimensionale Prüfung statt nur technisch |
| **EU AI Act Integration** | Art. 9–15 → maschinenprüfbare Controls | **USP 2** — Compliance-as-Code |
| **Policy-as-Code** | OPA/Rego für automatisierte Prüfungen | Automatisierung statt manuelle Checklisten |
| **Evidence Store** | Immutable Evidenz, auditierbare Nachweiskette | **USP 6** — Auditierbarkeit-by-Design |
| **Supply-Chain-Security** | Sigstore/Cosign, SLSA Attestations | Manipulationsschutz für Artefakte |
| **GitOps/ArgoCD** | Deklaratives Deployment, Git = SSoT | Reproduzierbarkeit, Drift-Prevention |
| **DSR-Methodik** | Hevner, Peffers, vom Brocke — formal | Wissenschaftliche Rigorosität |
| **Design-Prinzipien** | DP1–DP6 (geplant) | Übertragbare Gestaltungsregeln |
| **PROD + RETIRE Phasen** | Betrieb, Monitoring, Dekommissionierung | Vollständiger Lifecycle |
| **Cloud-Agnostik + PoC** | Generische Architektur + Azure-Instanz | Transferierbarkeit |

---

## 6. Unterschiede (was nur Mahr hat)

| Aspekt | **Nur Mahr** | Relevanz für Demir |
|--------|-------------|-------------------|
| **Shopfloor-Deployment** | Air-Gap-Szenarien, kein Internet, Edge | Nicht dein Scope — Enterprise/Cloud |
| **Prompt Engineering als Phase** | Eigene Lifecycle-Phase | Könnte als Diskussionspunkt in Kap. 7 erwähnt werden |
| **LLM-Typ-Taxonomie** | Klassifikation verschiedener LLM-Typen | Grundlagen — gehört ggf. in dein Kap. 2 |
| **Industrie-4.0-Kontext** | Fertigungsautomatisierung | Andere Domäne, aber gleiche Grundproblematik |

---

## 7. Positionierung für den Prof

### Elevator Pitch (30 Sekunden):
> „Mahr et al. (2024) zeigen, dass der Bedarf an LLM-Referenzarchitekturen in der Industrie anerkannt ist. Ihre Arbeit beschreibt die Phasen des LLM-Lifecycles, endet aber bei der Beschreibungsebene — es fehlen formalisierte Kontrollpunkte, automatisierte Compliance-Prüfungen und eine auditierbare Nachweiskette. Genau diese drei Lücken adressiert meine Arbeit mit dem Quality-Gate-Framework, AI-Act-Compliance-as-Code und dem Evidence Store."

### Argumentationskette:
1. **Mahr bestätigt den Bedarf** → Referenzarchitekturen für LLM werden gebraucht
2. **Mahr zeigt die Lücke** → Phasen beschreiben ≠ Phasen kontrollieren
3. **Demir schließt die Lücke** → Quality Gates + Compliance + Evidence

### Zitierfähiger Satz für Kap. 2:
> „Mahr et al. (2024) entwickeln eine Referenzarchitektur für LLM-Anwendungen in industriellen Umgebungen, die die Phasen Data Preparation, Model Training, Evaluation, Deployment und Prompt Engineering abdeckt. Die Architektur adressiert jedoch weder formalisierte Qualitätskontrollpunkte noch regulatorische Anforderungen — zwei Dimensionen, die für den Enterprise-Einsatz unter dem EU AI Act unverzichtbar sind und die die vorliegende Arbeit ergänzt."

---

## 8. Visualisierung: Gap-Analyse

```
                    Mahr et al. (2024)          Demir (2026)
                    ──────────────────          ────────────
Lifecycle-Phasen    ██████████░░ (5/6)          ████████████ (6/6)
Quality Gates       ░░░░░░░░░░░░ (0)           ████████████ (USP)
Compliance          ░░░░░░░░░░░░ (0)           ████████████ (USP)
Pipeline/CI-CD      ░░░░░░░░░░░░ (0)           ████████████ 
Policy-as-Code      ░░░░░░░░░░░░ (0)           ████████████
Evidence/Audit      ░░░░░░░░░░░░ (0)           ████████████ (USP)
Supply-Chain-Sec.   ░░░░░░░░░░░░ (0)           ████████████
DSR-Methodik        ░░░░░░░░░░░░ (0)           ████████████
Shopfloor/Edge      ████████████               ░░░░░░░░░░░░
Prompt Eng. Phase   ████████████               ░░░░░░░░░░░░
```

---

## 10. Komponentenvergleich (Detail-Ebene aus PDF)

| Komponente | **Mahr (Fig. 1)** | **Demir (Artifact Construction)** | Bewertung |
|------------|-------------------|----------------------------------|-----------|
| **Data Pipeline** | Detailliert: Source→KB→Chunks→Tokenizer→Vectors→VectorDB→Data Lake | Konzeptionell (DATA-Phase), nicht im PoC-Scope | Mahr detaillierter |
| **Model Strategy** | 5 Strategien: Scratch, Commercial, PEFT, Full FT, RAG — inkl. RAG-Flow | Nicht explizit — Modellstrategie ist Input, nicht Architektur-Scope | Mahr detaillierter |
| **Evaluation Metriken** | BLEU, Perplexity, Social Bias, Truthfulness, ROUGE, METEOR, F1 — task-spezifisch aufgeteilt | DeepEval-Framework: Faithfulness, Hallucination, Toxicity — als automatisierte Gate-Kriterien | **Unterschiedlicher Fokus**: Mahr = manuelle Auswahl; Demir = automatisierte CI/CD-Integration |
| **Model Registry** | ✅ "Model Repository" nach Passed Evaluation | ✅ Implizit (Artifact in Pipeline) + Sigstore-Signatur | Beide vorhanden, Demir + Supply-Chain-Security |
| **Human Feedback** | ✅ Feedback Pipeline → Reward Model (RLHF) | ⚠️ Human-in-the-Loop als Gate (Art. 14), nicht als Training-Loop | **Unterschiedlicher Zweck**: Mahr = Modellverbesserung; Demir = Compliance-Kontrolle |
| **Deployment** | 3 Strategien: Local/vEdge, API Call/Edge, Cloud/Digital Workplace | K8s + ArgoCD + GitOps — cloud-native, deklarativ | **Unterschiedliche Ebene**: Mahr = wo läuft es?; Demir = wie wird es sicher deployed? |
| **Prompt Engineering** | Eigener Block: Zero-shot, One-shot, Few-shot | Nicht als Phase — in EVAL/PROD eingebettet | Nur Mahr |
| **Quality Gates** | ❌ Nur "Passed Evaluation" (binär, 1 Stelle) | ✅ Formalisiertes Framework: Trigger→Kriterien→Evidenz→Entscheidung→Owner→Audit Trail→Waiver an **jeder Phase** | **NUR Demir** — Kernunterschied |
| **CI/CD Pipeline** | ❌ Nicht vorhanden | ✅ GitHub Actions + ArgoCD + Pipeline-as-Code | **NUR Demir** |
| **Policy-as-Code** | ❌ | ✅ OPA/Rego | **NUR Demir** |
| **Compliance/Regulierung** | ❌ | ✅ EU AI Act Art. 9–15, Compliance-as-Code | **NUR Demir** |
| **Evidence Store** | ❌ | ✅ Immutable Blob Storage, Audit Trail | **NUR Demir** |
| **Supply-Chain-Security** | ❌ | ✅ Sigstore/Cosign, SLSA | **NUR Demir** |
| **Drift Detection/Monitoring** | ❌ (kein PROD-Phase) | ✅ PROD-Phase mit Monitoring + Alert/Rollback | **NUR Demir** |

---

## 11. Kritische Beobachtungen aus dem PDF

### Was Mahr explizit als Lücke benennt (= Bestätigung für deine Thesis):
- S. 23: *"the evaluation is typically conducted at a surface level"* → bestätigt PD2 (fehlende Gate-Formalisierung)
- S. 23: *"the practical implementation into a real environment is subject of future research"* → kein PoC, keine Evaluation
- S. 20: Basiert auf MLOps Level 0 (Google, 2020) → niedrigstes Automatisierungslevel, kein CI/CD
- S. 22: Model Registry erwähnt, aber ohne Versionierung, Signierung, oder Audit

### Was Mahr GUT macht (fair anerkennen):
- RAG-Flow ist detaillierter als bei dir (Retrieval Model, Similarity Search, Search History)
- 5 Model-Strategien systematisch aufgefächert — das hast du nicht explizit
- Shopfloor/Air-Gap-Thematik ist real und relevant (aber nicht dein Scope)
- Evaluation-Metriken task-spezifisch aufgeteilt — differenzierter als "DeepEval-Metriken"

### Was du im Prof-Gespräch sagen kannst:
> „Mahr et al. liefern eine wertvolle Übersicht über die Komponenten eines LLM-Systems auf MLOps Level 0. Meine Arbeit setzt eine Ebene höher an: Ich formalisiere nicht die Bauteile, sondern die Betriebslogik — also wann und wie automatisiert geprüft wird, wer freigibt, und wie Compliance nachgewiesen wird. Mahr endet bei ‚Passed Evaluation' als binärer Entscheidung; mein Gate-Framework definiert die Entscheidungsstruktur selbst."

---

## 12. Empfehlung: Nächste Schritte

1. **PDF von Mahr hochladen** → Architektur-Abbildung direkt vergleichen
2. **2–3 weitere LLM-Referenzarchitektur-Paper suchen** → Abgrenzungstabelle erweitern
3. **Related-Work-Tabelle für Kap. 2** bauen: Demir vs. Mahr vs. X vs. Y (Feature-Matrix)
