# Related-Work-Analyse: Pourmajidi et al. (2025) + Gesamtvergleich
## Stand: 25.02.2026

---

# TEIL 1: Pourmajidi et al. (2025) — Einzelanalyse

## 1. Bibliographische Daten

| Feld | Details |
|------|---------|
| Titel | A Reference Architecture for Governance of Cloud Native Applications |
| Autoren | Pourmajidi, Zhang, Steinbacher, Erwin, Miranskyy |
| Venue | IEEE Transactions on Cloud Computing, Vol. 13, No. 3, Jul–Sep 2025 |
| Typ | **Journal-Artikel** (18 Seiten, peer-reviewed, Top-Venue) |
| DOI | 10.1109/TCC.2025.3578557 |
| Affiliationen | Toronto Metropolitan University + IBM Canada Lab + University of Maryland |
| Methode | Requirements-driven Design (funktionale + nicht-funktionale Anforderungen) |
| Artefakt | Referenzarchitektur für CNA Governance + Referenzimplementierung (AWS + IBM Cloud) |
| Kontext | Cloud-native Applikationen, regulierte Industrien, Multi-Cloud |

**Gewicht:** Das ist ein **A-Tier Journal-Paper** mit IBM-Praxisvalidierung — deutlich schwerer als Mahr (5-Seiten Conference Paper). Für dein Related Work ist das die wichtigste Abgrenzungsquelle.

---

## 2. Kernkonzepte von Pourmajidi et al.

### 2.1 Architektur-Struktur (Fig. 1 + Fig. 2)
Die Architektur besteht aus drei Ebenen:

**A) Resource Groups für CNAs (RG 1..n):**
- CNA-Komponenten (Containers, VMs, Serverless)
- Data Ingestion (Collector Agents + API Gateway)
- Fault-tolerant Data Bus

**B) RG-GOV-IMS (Governance: Ingestion, Manipulation, Storage):**
- Data Ingestion (zentral)
- Data Manipulation: Converter → Filter → Aggregator → Archiver
- Data Storage: **Immutable** + Mutable
- Fault-tolerant Data Bus (Primary + Auxiliary)

**C) RG-GOV-DA (Governance: Data Analytics):**
- Pluggable Analytics: Anomaly Detection, Drift Detection, SLA Breach Detection, **Compliance Breach Detection**, Synthetic Monitoring
- Eigener Data Storage (Immutable + Mutable)

### 2.2 End-to-End Continuous Governance (Sec. III-C6)
Vier Governance-Stufen im SDLC:
1. **Code-level governance** — Source Code gegen Standards prüfen
2. **CI-level governance** — Integration gegen Governance-Ziele verifizieren
3. **Pre-CD governance** — **Checkpoint vor Deployment** (ggf. manuelle Freigabe!)
4. **Post-CD governance** — Monitoring, Drift Detection, Korrekturmaßnahmen

### 2.3 Zentrale Design-Prinzipien
- Vendor-agnostic / Multi-Cloud
- XaC (Everything-as-Code) + IaC
- GitOps (Git = Single Source of Truth)
- DevSecOps
- "Battery-included" (Governance eingebaut, nicht nachgerüstet)
- Layered Architecture
- High Availability (Dual Data Bus, Heartbeat)

### 2.4 Compliance-Ansatz
- Referenziert NIST, FedRAMP, HIPAA, SOC2, C5
- CCM (Cloud Control Matrix) Mapping: 65% fully supported, 24% partially, 12% out of scope
- IBM SCC (Security and Compliance Center) als Praxis-Beispiel
- Immutable Storage für Evidenz-Authentizität (WORM)

---

## 3. Überlappungen mit Demir (2026) — WAS BEIDE HABEN

| Aspekt | Pourmajidi | Demir | Bewertung |
|--------|-----------|-------|-----------|
| **Referenzarchitektur als Artefakt** | ✅ | ✅ | Gleicher Artefakttyp |
| **Governance als Kernfokus** | ✅ Monitoring + Observability + Compliance | ✅ Quality Gates + Compliance | Gleiche Intention, unterschiedliche Mechanismen |
| **Immutable Storage** | ✅ WORM, Blockchain-Alternative | ✅ Azure Blob Immutable | **Starke Überlappung** — gleiche technische Lösung |
| **GitOps / Git = SSoT** | ✅ explizit (Weaveworks-Prinzipien) | ✅ ArgoCD + Git | **Starke Überlappung** |
| **IaC / XaC** | ✅ Terraform, Chef, Ansible | ✅ Terraform/Bicep | **Starke Überlappung** |
| **CI/CD-Integration** | ✅ 4-Stufen-Governance im SDLC | ✅ GitHub Actions + ArgoCD | **Starke Überlappung** |
| **Pre-CD Checkpoint** | ✅ "essential checkpoint, potentially involving manual approval" | ✅ Quality Gate vor Deployment | **Konzeptionell sehr ähnlich!** |
| **Post-CD Monitoring** | ✅ Drift Detection, Korrekturmaßnahmen | ✅ PROD-Phase, Alert/Rollback | **Starke Überlappung** |
| **Compliance Frameworks** | ✅ NIST, FedRAMP, HIPAA, SOC2, C5, CCM | ✅ EU AI Act Art. 9–15 | Beide compliance-orientiert, unterschiedliche Frameworks |
| **Vendor-agnostic** | ✅ Multi-Cloud (AWS + IBM) | ✅ Generisch + Azure PoC | Gleiche Philosophie |
| **Layered Architecture** | ✅ | ✅ Schichten-/Modulmodell | Gleicher Ansatz |
| **Cloud-native** | ✅ K8s, Container, Serverless | ✅ K8s, Container, Microservices | **Starke Überlappung** |
| **Praxis-Implementierung** | ✅ AWS + IBM Referenzimplementierung | ✅ Azure PoC (geplant) | Beide haben Praxis-Validierung |
| **Data Pipeline** | ✅ Ingestion → Manipulation → Storage → Analytics | ⚠️ Implizit in Pipeline-Integration | Pourmajidi detaillierter |

---

## 4. Unterschiede — WAS NUR DEMIR HAT

| Aspekt | Details | Bedeutung für Thesis |
|--------|---------|---------------------|
| **Quality-Gate-Framework** | Formalisierte Kontrollpunkte: Trigger → Kriterien → Evidenz → Entscheidung → Owner → Audit Trail → Waiver | **USP 1** — Pourmajidi hat "Pre-CD checkpoint" aber KEIN formalisiertes Gate-Template |
| **3 Gate-Dimensionen** | Strategisch (Business) + Technisch (GenAI-Metriken) + Compliance (AI Act) | Pourmajidi trennt nicht in Dimensionen — hat nur generische "governance goals" |
| **GenAI-Spezifität** | Hallucination, Faithfulness, Toxicity, Model Card Checks | **Kernunterschied** — Pourmajidi ist CNA-generisch, nicht GenAI-spezifisch |
| **EU AI Act** | Art. 9–15 → maschinenprüfbare Controls | Pourmajidi referenziert US-Frameworks (NIST, FedRAMP, HIPAA) — kein EU AI Act |
| **Policy-as-Code (OPA/Rego)** | Deklarative Policies für automatisierte Entscheidungen | Pourmajidi erwähnt "policy enforcement" aber ohne konkreten Policy-Engine |
| **Supply-Chain-Security** | Sigstore/Cosign, SLSA Attestations | Nicht bei Pourmajidi |
| **LLM-Lifecycle** | 6 Phasen (DATA→MODEL→EVAL→DEPLOY→PROD→RETIRE) | Pourmajidi hat keinen AI/ML-Lifecycle |
| **Waiver-Mechanismus** | Dokumentierte Ausnahmen mit Begründung | Nicht bei Pourmajidi |
| **DSR-Methodik** | Hevner, Peffers, vom Brocke | Pourmajidi nutzt Requirements-Engineering, kein DSR |
| **Design-Prinzipien (DP1–DP6)** | Übertragbare Gestaltungsregeln als DSR-Beitrag | Pourmajidi hat "desired characteristics" aber nicht als formale DPs |

---

## 5. Unterschiede — WAS NUR POURMAJIDI HAT

| Aspekt | Details | Relevanz für Demir |
|--------|---------|-------------------|
| **Telemetrie-Pipeline** | Detaillierte Ingestion → Converter → Filter → Aggregator → Archiver Pipeline | Könnte DP für Evidence-Pipeline inspirieren |
| **Fault-tolerant Data Bus** | Primary + Auxiliary Bus, Gossip-Protokoll | High-Availability-Aspekt — bei Demir nicht adressiert |
| **Multi-Cloud** | Explizit AWS + IBM, Multi-Region, Geo-Redundanz | Demir ist Azure-only im PoC |
| **Serverless Computing** | FaaS als Computing-Plattform für CNAs | Nicht im Demir-Scope |
| **Big Data Telemetrie (5Vs)** | Volume, Velocity, Variety, Veracity, Value | Könnte für Evidence Store-Skalierung relevant sein |
| **CCM Compliance Mapping** | 65% fully supported, 24% partially — systematisch evaluiert | Methodik für deine AI-Act-Mapping-Evaluation übertragbar! |
| **IBM-Praxisvalidierung** | Produktiv bei IBM Cloud eingesetzt (Dogfooding) | Stärkere Validierung als dein PoC — aber andere Domäne |
| **Heartbeat-Mechanismus** | Continuous Health Check der Governance-Komponenten | Nice-to-have, aber nicht dein Scope |
| **Pluggable Data Analytics** | Anomaly Detection, Drift Detection, SLA Breach als austauschbare Module | Architekturmuster übertragbar auf deine Gate-Checks |
| **Well-Architected Framework** | AWS WAF + IBM Cloud for Financial Services integriert | Könnte als Referenz für deine NFRs dienen |

---

## 6. Kritische Bewertung

### 6.1 Was Pourmajidi GUT macht (fair anerkennen):
- **Methodisch sauber:** Systematische Requirements-Analyse, CCM-Mapping, Real-World-Implementierung
- **Architektonisch ausgereift:** Layered, fault-tolerant, multi-cloud — produktionsreif
- **Immutable Storage als Governance-Grundlage:** Gleiche Erkenntnis wie du — Evidenz muss unveränderbar sein
- **End-to-End Governance im SDLC:** 4-Stufen-Modell ist konzeptionell ähnlich zu deinem Pipeline-Flow
- **Top-Venue:** IEEE TCC ist ein A-Tier Journal — das gibt deiner Abgrenzung Gewicht

### 6.2 Was Pourmajidi NICHT kann (= dein Beitrag):
- **Keine GenAI-Spezifität:** Die Architektur ist für JEDE CNA — kennt keine LLM-Metriken, kein Model Evaluation, keine AI-spezifischen Risiken
- **Kein Gate-Framework:** "Pre-CD checkpoint" ist ein Konzept-Satz, kein Template mit Trigger/Kriterien/Evidenz/Owner/Waiver
- **Kein EU AI Act:** Referenziert nur US-Compliance (NIST, FedRAMP, HIPAA, SOC2)
- **Keine Policy-as-Code-Engine:** Erwähnt "policy enforcement" ohne OPA/Rego oder äquivalente Engine
- **Keine Supply-Chain-Security:** Kein Sigstore, kein SLSA, keine Artefakt-Signierung
- **Kein AI-Lifecycle:** Kennt keinen Unterschied zwischen traditioneller Software und GenAI-Systemen

### 6.3 Synthese — wie ergänzen sich die Arbeiten:
> **Pourmajidi liefert die Governance-Infrastruktur (Telemetrie, Storage, Data Flow), Demir liefert die Governance-Logik für GenAI (was wird geprüft, wer entscheidet, wie wird Compliance nachgewiesen).**

Metapher: Pourmajidi baut die **Autobahn** (Daten fließen, werden gespeichert, analysiert). Demir definiert die **Verkehrsregeln speziell für GenAI-Fahrzeuge** (Quality Gates = Ampeln, EU AI Act = Straßenverkehrsordnung, Evidence Store = Dashcam-Aufzeichnung).

---

# TEIL 2: Dreier-Vergleich — Demir vs. Mahr vs. Pourmajidi

## 7. Feature-Matrix

| Feature / Dimension | **Demir (2026)** | **Mahr et al. (2024)** | **Pourmajidi et al. (2025)** |
|---------------------|:---:|:---:|:---:|
| **Bibliographisch** | | | |
| Typ | Masterarbeit (DSR) | Conference Paper (5 S.) | Journal Article (18 S.) |
| Venue | SRH Hochschule | IEEE SIITME | IEEE Trans. Cloud Comp. |
| Methode | Design Science Research | Nicht spezifiziert | Requirements Engineering |
| Praxis-Validierung | Azure PoC (geplant) | Keine (theoretisch) | AWS + IBM (produktiv) |
| **Domäne** | | | |
| GenAI/LLM-spezifisch | ✅ | ✅ | ❌ (generische CNA) |
| Enterprise/Cloud-native | ✅ | ⚠️ (Industrie/Shopfloor) | ✅ |
| Regulierte Industrien | ✅ (EU AI Act) | ❌ | ✅ (NIST, HIPAA, SOC2) |
| **Architektur** | | | |
| Referenzarchitektur | ✅ | ✅ | ✅ |
| Layered / Modular | ✅ | ⚠️ (linear, 5 Blöcke) | ✅ |
| Cloud-agnostic | ✅ (generisch + Azure) | ⚠️ (implizit) | ✅ (AWS + IBM, Multi-Cloud) |
| Kubernetes/Container | ✅ | ❌ | ✅ |
| IaC (Terraform etc.) | ✅ | ❌ | ✅ |
| **Lifecycle** | | | |
| Data Preparation | ✅ (konzeptionell) | ✅ (detailliert) | ❌ (kein AI-Lifecycle) |
| Model Training/Strategy | ✅ (konzeptionell) | ✅ (5 Strategien) | ❌ |
| Model Evaluation | ✅ (PoC-Scope, DeepEval) | ✅ (task-spezifisch) | ❌ |
| Deployment | ✅ (GitOps/ArgoCD) | ✅ (3 Strategien) | ✅ (CI/CD, GitOps) |
| PROD/Monitoring | ✅ | ❌ | ✅ (Drift Detection etc.) |
| RETIRE | ✅ | ❌ | ❌ |
| Prompt Engineering | ⚠️ (eingebettet) | ✅ (eigene Phase) | ❌ |
| **Governance / Kontrolle** | | | |
| Quality Gates (formalisiert) | ✅ **USP** | ❌ | ⚠️ ("Pre-CD checkpoint") |
| Gate-Template (Trigger→…→Waiver) | ✅ **USP** | ❌ | ❌ |
| 3 Gate-Dimensionen | ✅ **USP** | ❌ | ❌ |
| End-to-End Governance | ✅ | ❌ | ✅ (4 Stufen) |
| Policy-as-Code (OPA/Rego) | ✅ | ❌ | ⚠️ (erwähnt, nicht instanziiert) |
| Compliance-as-Code | ✅ **USP** | ❌ | ⚠️ (Compliance erwähnt, nicht als Code) |
| **Compliance** | | | |
| EU AI Act | ✅ **USP** | ❌ | ❌ |
| NIST/FedRAMP/HIPAA/SOC2 | ❌ | ❌ | ✅ |
| CCM Mapping | ❌ | ❌ | ✅ |
| Regulatory-to-Technical Mapping | ✅ | ❌ | ⚠️ (implizit) |
| **Evidenz & Audit** | | | |
| Immutable Evidence Store | ✅ **USP** | ❌ | ✅ (WORM) |
| Audit Trail | ✅ | ❌ | ✅ (implizit) |
| Supply-Chain-Security (Sigstore) | ✅ | ❌ | ❌ |
| **Daten-Pipeline** | | | |
| Telemetrie-Pipeline | ⚠️ (implizit) | ❌ | ✅ (Ingestion→Manipulation→Storage→Analytics) |
| Fault-tolerant Data Bus | ❌ | ❌ | ✅ |
| Pluggable Analytics | ⚠️ (DeepEval als Plugin) | ❌ | ✅ (modular) |
| **Methodik** | | | |
| DSR (Hevner/Peffers) | ✅ | ❌ | ❌ |
| Design-Prinzipien | ✅ (DP1–DP6 geplant) | ❌ | ⚠️ ("desired characteristics") |
| Evaluation | ✅ (Walkthrough + Expert + PoC + Feature) | ❌ | ✅ (CCM + Implementierung) |

**Legende:** ✅ = vorhanden/adressiert | ⚠️ = teilweise/implizit | ❌ = nicht vorhanden

---

## 8. Positionierungsmatrix (2 Achsen)

```
                        GenAI-spezifisch
                              ▲
                              │
                              │  ★ DEMIR (2026)
                              │  GenAI + Governance + Compliance
                              │
                              │
            ● Mahr (2024)     │
            GenAI + Lifecycle │
            (keine Governance)│
                              │
         ─────────────────────┼──────────────────────────► Governance-Tiefe
           Beschreibend       │              Formalisiert + Automatisiert
                              │
                              │        ● Pourmajidi (2025)
                              │        CNA + Governance + Compliance
                              │        (nicht GenAI-spezifisch)
                              │
                              ▼
                        Generisch/CNA
```

**Demir sitzt im oberen rechten Quadranten** — die einzige Arbeit die GenAI-Spezifität UND formalisierte Governance kombiniert.

---

## 9. Wie die Papers in die Thesis-Gliederung passen

### Kap. 2 — Related Work / Stand der Forschung:

| Paper | Funktion in Kap. 2 | Abschnitt |
|-------|-------------------|-----------|
| **Mahr et al. (2024)** | **Abgrenzung Lifecycle:** Zeigt, dass LLM-Referenzarchitekturen existieren, aber bei Beschreibung enden — keine Kontrolle, keine Compliance | 2.x "LLM-Referenzarchitekturen" |
| **Pourmajidi et al. (2025)** | **Abgrenzung Governance:** Zeigt, dass CNA-Governance-Architekturen existieren, aber nicht GenAI-spezifisch sind — keine LLM-Metriken, kein AI Act | 2.x "Cloud-Native Governance" |
| **Beide zusammen** | **Gap-Identifikation:** Die Lücke zwischen LLM-Lifecycle (Mahr) und CNA-Governance (Pourmajidi) ist EXAKT der Raum, den Demir füllt | 2.x "Forschungslücke" |

### Kap. 3 — Anforderungen:
- Pourmajidis **"desired characteristics"** (Sec. III) als Validierung für deine Design-Prinzipien
- Pourmajidis **CCM-Mapping-Methodik** als Vorbild für dein EU-AI-Act-Mapping

### Kap. 4 — Architekturentwurf:
- Pourmajidis **Telemetrie-Pipeline** (Ingestion→Manipulation→Storage→Analytics) als Referenz für deine Evidence-Pipeline
- Pourmajidis **Immutable Storage** als Bestätigung deines Evidence-Store-Designs (DP2)

### Kap. 5 — Quality Gates:
- Pourmajidis **"Pre-CD checkpoint"** als Ausgangspunkt, den du formalisierst und erweiterst
- Unterschied: Pourmajidi = 1 Checkpoint (Pre-CD), Demir = n Gates an jeder Phase mit 3 Dimensionen

### Kap. 7 — Diskussion:
- Direkter Vergleich: Dein Gate-Framework vs. Pourmajidis 4-Stufen-Governance
- Trade-off-Diskussion: Generische Governance (Pourmajidi) vs. domänenspezifische Governance (Demir)

---

## 10. Argumentationskette für den Prof

### Elevator Pitch (45 Sekunden):
> „In der Literatur existieren zwei relevante Stränge: Mahr et al. (2024) entwickeln eine Referenzarchitektur für den LLM-Lifecycle, adressieren aber keine Governance — es gibt keine Kontrollpunkte, keine Compliance, keine Evidenz. Pourmajidi et al. (2025) entwickeln eine ausgereite Governance-Architektur für Cloud-Native Applications mit Immutable Storage und CI/CD-Integration, aber ohne jede GenAI-Spezifität — keine LLM-Metriken, keinen AI Act, kein domänenspezifisches Gate-Framework. Meine Arbeit schließt exakt die Lücke zwischen diesen beiden Strängen: Ich verbinde den GenAI-Lifecycle mit formalisierter Governance und EU-AI-Act-Compliance."

### Dreisatz für jedes Gespräch:
1. **Mahr** zeigt den LLM-Lifecycle → aber keine Governance
2. **Pourmajidi** zeigt CNA-Governance → aber nicht für GenAI
3. **Demir** verbindet beides → GenAI-Lifecycle + formalisierte Governance + EU AI Act

---

## 11. Zitierfähige Sätze für Kap. 2

### Zu Pourmajidi:
> „Pourmajidi et al. (2025) entwickeln eine Referenzarchitektur für die Governance von Cloud-Native Applications, die Monitoring, Observability und Compliance über eine mehrstufige Telemetrie-Pipeline mit Immutable Storage integriert. Die Architektur definiert vier Governance-Stufen im Software Development Lifecycle (Code-level, CI-level, Pre-CD, Post-CD) und wurde auf AWS und IBM Cloud implementiert. Allerdings ist die Architektur domänenagnostisch und adressiert weder die spezifischen Herausforderungen von GenAI-Systemen (z.B. Hallucination Detection, Model Evaluation) noch regulatorische Anforderungen wie den EU AI Act."

### Zur Forschungslücke:
> „Die Analyse der bestehenden Literatur zeigt eine Lücke an der Schnittstelle von GenAI-Lifecycle-Management und formalisierter Governance: Existierende LLM-Referenzarchitekturen (Mahr et al., 2024) beschreiben die Phasen des Lebenszyklus, ohne Kontrollmechanismen zu definieren. Existierende CNA-Governance-Architekturen (Pourmajidi et al., 2025) formalisieren Governance-Prozesse, ohne GenAI-spezifische Anforderungen zu berücksichtigen. Die vorliegende Arbeit adressiert diese Lücke durch ein Quality-Gate-Framework, das domänenspezifische GenAI-Kontrollen mit automatisierter EU-AI-Act-Compliance verbindet."

---

## 12. Was du von Pourmajidi LERNEN kannst (methodisch)

1. **CCM-Mapping als Vorbild:** Pourmajidi mapped seine Architektur systematisch gegen CCM (65%/24%/12%). Du kannst das GLEICHE mit EU AI Act Art. 9–15 machen → "Art. 9: fully supported, Art. 10: partially supported, …"
2. **"Desired Characteristics" Struktur:** Pourmajidis Sec. III (NFRs, Architectural Reqs, Construction Reqs, Components) ist ein gutes Template für dein Kap. 3
3. **Telemetrie-Pipeline-Pattern:** Ingestion → Manipulation → Storage → Analytics ist übertragbar auf: Evidence Collection → Evidence Processing → Evidence Storage → Compliance Analysis
4. **Dual Data Bus:** Primary + Auxiliary für Fault Tolerance — könnte als Design-Prinzip für deinen Evidence Store relevant sein
5. **Real-World-Instanziierung:** Pourmajidi trennt sauber zwischen Referenzarchitektur (generisch) und Instanziierung (AWS + IBM). Du machst das gleiche: Generisch + Azure PoC

---

## 13. Nächste Schritte

1. **Pourmajidi in Zotero aufnehmen** (falls noch nicht geschehen)
2. **Feature-Matrix (Sec. 7) als LaTeX-Tabelle** für Kap. 2 vorbereiten
3. **Positionierungsmatrix (Sec. 8)** als Abbildung für Kap. 2
4. **2–3 weitere Papers suchen** um die Tabelle zu erweitern (z.B. Shankar et al. — MLOps; EU AI Act Operationalisierung)
5. **Zitierfähige Sätze (Sec. 11)** in Kapitel-Outline einbauen
