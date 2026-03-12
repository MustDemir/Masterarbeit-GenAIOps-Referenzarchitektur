# Recherchebericht Kapitel 4 — THEMENCLUSTER-Abgleich (ROT + ORANGE Tags)

**Datum:** 2026-03-05
**Quelle:** Lokale Sammlung `/THEMENCLUSTER/` (OneDrive), Finder-Tags ausgelesen
**Methode:** Alle PDFs mit REL_ROT_CORE + REL_ORANGE_HIGH Tags aus Clustern 00–03 gegen bereits verwendete Quellen in 4.1–4.5 abgeglichen
**Zweck:** Ungenutzte Paper für 4.6 + Verstärkung bestehender Abschnitte identifizieren

---

## Tag-System des Users

| Tag | Bedeutung | Anzahl |
|-----|-----------|--------|
| 🔴 REL_ROT_CORE | Kernquelle | 24 |
| 🟠 REL_ORANGE_HIGH | Hohe Relevanz | 25 |
| 🟡 REL_GELB_MEDIUM | Mittlere Relevanz | 40 |
| 🔵 REL_BLAU_CONTEXT | Kontext | 35 |

---

## Bereits in 4.1–4.5 verwendete Quellen (✅ ERLEDIGT)

| Quelle | Abschnitt | Tag | Status |
|--------|-----------|-----|--------|
| Huwyler (2024) | 4.1, 4.2 | 🔴 | ✅ Kernquelle |
| Buscemi et al. (2025) | 4.1, 4.3 | 🟠 | ✅ Kernquelle |
| Ray (2026) TRiSM Review | 4.2, 4.4 | 🔴 | ✅ Kernquelle |
| Butt et al. (2026) Policy→Pipeline | 4.2 | 🔴 | ✅ Kernquelle |
| Leon (2026) Lifecycle Governance | 4.2 | 🟡 | ✅ Konvergent |
| Kelly et al. (2024) | 4.3 | 🟠 | ✅ Kernquelle |
| Feng et al. (2024) | 4.3 | 🔵 | ✅ Kernquelle |
| Gallina et al. (2025) | 4.3 | 🔵 | ✅ Konvergent |
| Kovac et al. (2025) CERTAIN | 4.4 | 🟠 | ✅ Kernquelle |
| Romeo et al. (2025) ARPaCCino | 4.4 | 🔵 | ✅ Konvergent |
| Sardana et al. (2024) CaC 2.0 | 4.4 | 🟠 | ✅ Kernquelle |
| Sterz et al. (2024) | 4.5 | 🟡 | ✅ Kernquelle |
| Laux (2024) | 4.5 | 🟡 | ✅ Kernquelle |
| Enqvist (2023) | 4.5 | 🟠 | ✅ Kernquelle |
| Ooms et al. (2025) / ssrn-5196091 | 4.5 | 🟡 | ✅ Konvergent |
| Novelli et al. (2024) | 4.1 | 🟠 | ✅ Konvergent |
| NIST AI 100-1 | 4.1 | 🟠 | ✅ Primärquelle |
| Jonnala et al. (2025) | 4.1 | 🟠 | ✅ Konvergent |

**→ 18 Quellen bereits eingesetzt. Gute Abdeckung der ROT/ORANGE-Kernquellen.**

---

## UNGENUTZTE ROT + ORANGE Paper — Bewertung für Kap. 4

### Bewertungsskala (Eignung für Kap. 4.6 Requirements-Katalog)

| Symbol | Bedeutung |
|--------|-----------|
| ⭐⭐⭐ | **Muss rein** — Direkt für 4.6 relevant, Quality Gates / Requirements / Traceability |
| ⭐⭐ | **Sollte rein** — Stärkt bestehende Argumentation oder liefert konvergente Evidenz |
| ⭐ | **Kann rein** — Ergänzend, aber nicht zwingend für Kap. 4 Scope |
| ❌ | **Nicht für Kap. 4** — Anderes Kapitel oder außerhalb Scope |

---

### Gruppe A: Direkt relevant für 4.6 Requirements-Katalog (⭐⭐⭐)

| # | Quelle | Jahr | Tag | Cluster | Kernbeitrag für Kap. 4.6 |
|---|--------|------|-----|---------|--------------------------|
| 1 | **Elia et al. — MQG4AI** | 2025 | 🔴 | 02 | Quality-Gate-Methodik für AI Lifecycle; RAI Knowledge Linking; Explanation Stage. **Hauptvergleichsquelle** — fast identischer Scope. Abgrenzung: MQG4AI = XAI/Medizin-Fokus, Thesis = Deployer-generisch + EU AI Act Art. 9–15 + PaC. |
| 2 | **Lucaj et al. — TechOps** | 2025 | 🔴 | 02 | Open-Source-Templates für AI-Act-Dokumentation (Daten, Modelle, Anwendungen). Traceability über gesamten Lifecycle. Direkt nutzbar für Evidenzartefakt-Definition in Gate-Design. |
| 3 | **Nellutla — MLOps 2.0** | 2025 | 🔴 | 01/04 | Referenzarchitektur CI/CD + Continuous Data Validation (CDV). Data Quality Gates (Schema, Semantic, Temporal, Distributional) an Build/Test/Release/Run Stages. SLO-aligned Promotion Criteria. Starke Parallele zu Quality-Gate-Konzept der Thesis. |

**→ Alle 3 sollten vor Schreiben von 4.6 als Fulltext gelesen werden.**

---

### Gruppe B: Stärkt bestehende Abschnitte / konvergente Evidenz (⭐⭐)

| # | Quelle | Jahr | Tag | Cluster | Zielabschnitt | Kernbeitrag |
|---|--------|------|-----|---------|---------------|-------------|
| 4 | **Gonçalves & Correia — XAI-Compliance-by-Design** | 2025 | 🔴 | 02 | 4.3/4.4 | Dual-Flow-Architektur: Upstream Technical Pipeline + Downstream Governance Pipeline + Compliance-by-Design Engine + Technical-Regulatory Correspondence Matrix (GDPR + AI Act + ISO 42001). Konvergent zu Thesis-Dreischritt. |
| 5 | **Finch & Butt — Gaps in AI-Compliant Governance** | 2025 | 🟠 | 02 | 4.4/4.6 | Systematic Review: Gaps in Enforceability, Proportionality, Auditability. Konzept "Compliance Asymmetry" — strukturelle Friktionen zwischen Regulierungsambition und institutioneller Kapazität. Stützt Deployer-Problematik. |
| 6 | **Billeter et al. — MLOps as Enabler of Trustworthy AI** | 2024 | 🔴 | 01/03 | 4.2/4.4 | Mapping TAI-Prinzipien → MLOps Lifecycle → MLOps Practices. Fairness, Reliability, Explainability, Safety als Lifecycle-integrierte Concerns. Konvergent zu Quality-Gate-als-TAI-Enabler-Argument. |
| 7 | **Slupczynski et al. — CAPTURE** | 2026 | 🔴 | 02 | 4.2 | 7-Phasen-Framework (Consult→Articulate→Protocol→Terraform→Utilize→Reify→Evolve) mit Decision Gates. Validiert via 5-Jahres-Case-Study + 10 Expert Interviews. Konvergent zu Lifecycle-Phasen mit Gate-Übergängen. |
| 8 | **Adetayo Adeyinka — PaC in Hybrid Cloud** | 2023 | 🔴 | 03 | 4.3/4.4 | PaC-Referenzarchitektur + Workflow für Continuous Compliance. Tool-Evaluation (OPA, Sentinel, Azure Policy). 4-Phasen: Inventory → Engineering → Integration → Monitoring. Konvergent zu Sardana/Rebbana. |
| 9 | **Rebbana — PaC for Cloud Data Platforms** | 2025 | 🟠 | 03 | 4.3 | PaC-Architektur: Policy Definition Languages + Enforcement Mechanisms + Attestation. 4-Phasen-Implementierung (Inventory → Engineering → Integration → Monitoring). Stärkt PaC-Evidenzkette in 4.3/4.4. |

---

### Gruppe C: Kontextuell relevant, nicht zwingend für Kap. 4 (⭐)

| # | Quelle | Jahr | Tag | Cluster | Einschätzung |
|---|--------|------|-----|---------|-------------|
| 10 | **Fernández-Llorca et al.** | 2025 | 🟠 | 02 | Terminologische Analyse (AI System vs. GPAI vs. Foundation Model). Relevant für Kap. 2 (Grundlagen), nicht direkt für Kap. 4. |
| 11 | **Hulok** | 2025 | 🟠 | 02 | EU AI Governance-Modell im Kontext breiterer Digital-Regulierung (GDPR, DSA, DMA). Eher Kap. 2 oder 4.1 Einleitung. |
| 12 | **Taeihagh** | 2025 | 🟠 | 02 | GenAI Governance: Risiken (Hallucination, Jailbreaking, Opacity) + Governance-Challenges. Guter Überblick, aber zu breit für spezifische 4.x-Abschnitte. Eher Kap. 2. |
| 13 | **Almagrabi & Khan** | 2025 | 🟠 | 02 | Secure AI Lifecycle mit GenAI-Strategien. Security-Fokus (Adversarial Attacks, Data Theft). Marginal für Kap. 4 Compliance-Scope. |
| 14 | **Radanliev et al.** | 2025 | 🟠 | 02 | GenAI Cybersecurity & Resilience. Rein Security-orientiert. Für Kap. 4 nicht direkt nutzbar. |
| 15 | **Antiya** | 2020 | 🟠 | 03 | Compliance-as-Code (2020). Historisch interessant, aber zu alt für aktuelle AI-Act-Diskussion. Eventuell als Ursprungs-Referenz für CaC-Konzept. |

---

## Zusammenfassung: Handlungsempfehlung

### Vor Schreiben von 4.6 zwingend lesen (Fulltext):
1. 🔴 **Elia et al. (2025) / MQG4AI** — Hauptabgrenzungsquelle
2. 🔴 **Lucaj et al. (2025) / TechOps** — Dokumentations-Templates
3. 🔴 **Nellutla (2025) / MLOps 2.0** — CI/CD Quality Gates Referenzarchitektur

### Für bestehende Abschnitte als Verstärkung einsetzen:
4. 🔴 **Gonçalves & Correia (2025)** → 4.3/4.4 (Dual-Flow konvergent)
5. 🟠 **Finch & Butt (2025)** → 4.4/4.6 (Compliance Asymmetry)
6. 🔴 **Billeter et al. (2024)** → 4.2/4.4 (TAI→MLOps Mapping)
7. 🔴 **Slupczynski et al. (2026)** → 4.2 (7-Phasen + Decision Gates)

### Nicht für Kap. 4 — für andere Kapitel vormerken:
8. Fernández-Llorca et al. (2025) → Kap. 2 (Terminologie)
9. Hulok (2025) → Kap. 2 (Regulierungslandschaft)
10. Taeihagh (2025) → Kap. 2 (GenAI Governance Überblick)

---

## Abgleich mit Recherche-Berichten (Consensus + Elicit)

| Quelle | Im Themencluster? | Im Consensus-Bericht? | Im Elicit-Bericht? | Status |
|--------|-------------------|-----------------------|--------------------|--------|
| Elia/MQG4AI (2025) | 🔴 Ja | Nein | ⭐⭐⭐ Ja | **Kern für 4.6** |
| Elia & Bauer (2023) | 🟡 Ja | Nein | ⭐⭐⭐ Ja | **Kern für 4.6** |
| Eisenberg/UCF (2025) | 🟡 Ja | 🔴 Ja | Nein | **Kern für 4.6** |
| Lucaj/TechOps (2025) | 🔴 Ja | Nein | ⭐⭐ Ja | **Kern für 4.6** |
| Nellutla/MLOps 2.0 (2025) | 🔴 Ja | Nein | Nein | **NEU — nur Cluster** |
| Gonçalves/XAI-CbD (2025) | 🔴 Ja | Nein | ⭐⭐ Ja | Stützquelle |
| Finch & Butt (2025) | 🟠 Ja | Nein | ⭐⭐ Ja | Stützquelle |
| Billeter et al. (2024) | 🔴 Ja | Nein | Nein | **NEU — nur Cluster** |
| Slupczynski/CAPTURE (2026) | 🔴 Ja | Nein | ⭐⭐ Ja | Stützquelle |
| Corrêa & Mönig (2024) | 🟡 Ja | Nein | ⭐⭐ Ja | Optional für 4.6 |

**→ 2 Paper sind NUR im Cluster, nicht in den Recherche-Berichten: Nellutla (2025) und Billeter et al. (2024). Beide ROT-getaggt. Verdienen Aufmerksamkeit.**

---

## Kritische Fragen

1. **Nellutla (2025)** — "MLOps 2.0" mit Data Quality Gates: Ist das peer-reviewed oder Grey Literature? Journal prüfen bevor als Quelle einsetzen.
2. **Gonçalves & Correia (2025)** hat ein "Dual-Flow"-Konzept (Technical + Governance Pipeline) das sehr nah an unserer Dreischritt-Transformation liegt — sollen wir das als konvergente Evidenz in 4.3 einbauen oder erst in 4.6 als Vergleich?
3. **Billeter et al. (2024)** mapped TAI-Prinzipien auf MLOps — ist das distinkt genug von Ray (2026), um als separate Quelle zu dienen, oder redundant?
