# Elicit-Recherche-Bericht — Kapitel 4 (Anforderungsanalyse RQ1)

**Datum:** 2026-03-04
**Quelle:** Elicit API (138M+ Papers)
**Methode:** 8 gezielte Suchanfragen, 2023–2026, ~120 Papers gesichtet
**Zweck:** Neue Quellen pro Abschnitt 4.2–4.6 mit inhaltlicher Eignungsbewertung

---

## Bewertungsskala (Inhaltliche Eignung)

| Symbol | Bedeutung |
|--------|-----------|
| ⭐⭐⭐ | **Kernquelle** — Direkt zitierfähig, hohe methodische + inhaltliche Passung zum Thesis-Scope |
| ⭐⭐ | **Stützquelle** — Konvergente Evidenz, ergänzt bestehende Argumentation |
| ⭐ | **Randquelle** — Thematisch verwandt, aber eingeschränkte Passung (anderer Scope/Methodik) |
| ❌ | **Nicht geeignet** — Falsche Domäne, zu generisch, oder methodisch unbrauchbar |

**Scope-Filter:** Deployer-Perspektive, EU AI Act Art. 9–15, Quality Gates, CI/CD-Integration, GenAI-spezifisch.

---

## Abschnitt 4.2 — Lifecycle-Modell (Pre-Deployment / Deployment / Operation)

### Suchanfrage
`"generative AI system lifecycle model pre-deployment deployment post-deployment governance phases MLOps"`

### Top-Empfehlungen

| # | Quelle | Jahr | Cit. | Eignung | Begründung |
|---|--------|------|------|---------|------------|
| 1 | **Butt et al. — "From Policy to Pipeline: Governance Framework for AI Dev/Ops Pipelines"** | 2026 | 0 | ⭐⭐⭐ | Direkt passend: Governance-Framework für AI-Pipelines, verknüpft EU AI Act + NIST AI RMF + ISO 42001 mit CI/CD-Lifecycle. Deployer-nah. **Kern-Paper für 4.2.** |
| 2 | **Leon — "Lifecycle-Based Governance to Build Reliable Ethical AI Systems"** | 2026 | 0 | ⭐⭐⭐ | Umfassendes Framework: Trustworthiness × Lifecycle × Stakeholder. Case Vignettes aus Manufacturing, Finance, Healthcare. Direkt passend für Lifecycle-Phasen-Argumentation. |
| 3 | **Slupczynski et al. — "CAPTURE: Stakeholder-Centered Iterative MLOps Lifecycle"** | 2026 | 0 | ⭐⭐ | MLOps-Lifecycle mit Stakeholder-Zentrierung. Gut für Vergleich mit eigener Phasen-Einteilung. Einschränkung: nicht GenAI-spezifisch. |
| 4 | **Almagrabi & Khan — "Optimizing Secure AI Lifecycle Model Management"** | 2025 | 11 | ⭐⭐ | AI Lifecycle mit Security-Fokus. 11 Zitationen zeigen Relevanz. Ergänzend für Security-Dimension der Lifecycle-Phasen. |
| 5 | **Radanliev et al. — "Generative AI cybersecurity and resilience"** | 2025 | 11 | ⭐ | GenAI-spezifisch, aber Cybersecurity-Fokus. Nur als Randquelle für Risk-Management-Phase. |

### Nicht geeignet (aus derselben Query)
- Sfetcu (2024) — Rumänisch, rein deskriptiv, kein Framework → ❌
- Vilsmeier & Salehi (2025) — Digital Twin / Automotive, kein AI-Governance-Bezug → ❌
- Xu et al. (2025) — MBSE/Automotive, zu weit vom Thesis-Scope → ❌

### Bewertung für Kapitel 4.2
**Butt et al. (2026)** und **Leon (2026)** sind die stärksten neuen Funde. Butt et al. verbindet explizit Policy→Pipeline (EU AI Act + NIST + ISO 42001 in CI/CD), was exakt dem Thesis-Ansatz entspricht. Leon liefert die konzeptionelle Lifecycle-Governance-Systematik. Beide ergänzen die bestehenden Quellen (Huwyler 2025, Kovac et al. 2025) mit frischer 2026-Evidenz.

⚠ **Vorsicht:** Beide Papers sind 2026, keine Zitationen. Nur als konvergente Evidenz zu bestehenden Quellen verwenden, nicht als alleinige Stütze.

---

## Abschnitt 4.3 — Transformationsmethodik (Norm → Requirement → Gate)

### Suchanfragen
1. `"transforming regulatory requirements into technical specifications for AI systems compliance"`
2. `"norm to requirement transformation methodology legal technical operationalization AI governance"`

### Top-Empfehlungen

| # | Quelle | Jahr | Cit. | Eignung | Begründung |
|---|--------|------|------|---------|------------|
| 1 | **Kelly et al. — "Navigating the EU AI Act: A Methodology for Mapping AI System Compliance"** | 2024 | 17 | ⭐⭐⭐ | Exakt passend: Methodik zur Interpretation des EU AI Act via Product Quality Models. Direkte Transformation Norm→Technical Spec. **Kern-Paper für 4.3.** |
| 2 | **Buscemi et al. — "From Legal Requirements to Technical Verification"** | 2025 | (bekannt) | ⭐⭐⭐ | Bereits Kernquelle. Strukturiertes Mapping AI Act Artikel → Verification Activities. Bestätigt durch Elicit als Top-Ergebnis. |
| 3 | **Feng et al. — "Normative Requirements Operationalization with LLMs"** | 2024 | 18 | ⭐⭐⭐ | Hochrelevant: LLM-gestützte Operationalisierung normativer Anforderungen. Methodisch innovativ. 18 Zitationen. Direkt anwendbar auf Transformationsmethodik. |
| 4 | **Hernandez et al. — "Open Knowledge Graph-Based Approach for Mapping Concepts between AI Act and Standards"** | 2024 | 8 | ⭐⭐ | Knowledge-Graph-Ansatz für Mapping AI Act ↔ Standards. Ergänzend für systematische Zuordnung. |
| 5 | **Pistilli et al. — "Stronger Together: Articulating Ethical/Legal/Technical"** | 2023 | 25 | ⭐⭐ | Konzeptionelle Brücke Ethik→Recht→Technik. 25 Zitationen. Gut für Legitimierung des Transformationsansatzes. |
| 6 | **Golpayegani et al. — "AICat: AI Cataloguing for EU AI Act"** | 2024 | (tbd) | ⭐⭐ | Strukturierter Katalog-Ansatz für AI Act Requirements. Ergänzend für Systematisierung. |
| 7 | **Lucaj et al. — "TechOps: Technical Documentation Templates for AI Act"** | 2025 | 0 | ⭐⭐ | Templates für technische Dokumentation nach AI Act. Praktisch orientiert, stützt Operationalisierungs-Argument. |

### Nicht geeignet
- Bonner et al. (2023) — Siemens/ALM Traceability, industriell, kein Regulatory Mapping → ❌
- Ramos et al. (2024) — QA/ISO-Erweiterungen, zu generisch für Transformationsmethodik → ❌

### Bewertung für Kapitel 4.3
**Kelly et al. (2024)** ist der stärkste Neufund: 17 Zitationen, direkte Methodik für EU AI Act Compliance Mapping. Zusammen mit dem bereits bekannten **Buscemi et al. (2025)** und **Feng et al. (2024, 18 Zit.)** ergibt sich ein starkes Trio für die Transformationsmethodik. Pistilli et al. liefert die konzeptionelle Rahmung (Ethik-Recht-Technik-Artikulation).

**Empfohlenes Argument in 4.3:** Kelly et al. für die Methodik-Systematik, Feng et al. für LLM-gestützte Operationalisierung (als Vergleichsansatz), Buscemi et al. für das konkrete Verification-Mapping.

---

## Abschnitt 4.4 — Kontrollmechanismen (Policy-as-Code, Monitoring, Audit)

### Suchanfragen
1. `"policy as code compliance as code automated AI regulation enforcement CI/CD pipeline governance checks"`
2. `"AI system continuous monitoring post-market surveillance risk management auditing compliance verification"`

### Top-Empfehlungen

| # | Quelle | Jahr | Cit. | Eignung | Begründung |
|---|--------|------|------|---------|------------|
| 1 | **Sardana et al. — "Compliance-as-Code 2.0: Agentic AI for Automated Governance"** | 2024 | 0 | ⭐⭐⭐ | Exakt passend: CaC 2.0 mit Agentic AI. Direkte Verbindung zu Policy-as-Code Konzepten. Cutting-edge Ansatz, der den Thesis-Beitrag kontextualisiert. **Kern-Paper für 4.4.** |
| 2 | **Romeo et al. — "ARPaCCino: Agentic-RAG for Policy as Code Compliance"** | 2025 | 1 | ⭐⭐⭐ | Agentic RAG + Policy-as-Code. Direkte Verbindung zu RAG-Thematik der Thesis + Compliance-Enforcement. Innovativer Ansatz. |
| 3 | **Kovac et al. — "CERTAIN Framework" (RegOps)** | 2025 | (bekannt) | ⭐⭐⭐ | Bereits Kernquelle. CI/CD-Compliance-Pipelines. Bestätigt durch Elicit als Top-Ergebnis. |
| 4 | **Gonçalves & Correia — "XAI-Compliance-by-Design"** | 2025 | 0 | ⭐⭐ | XAI als Compliance-Mechanismus by Design. Ergänzend für Transparency-Dimension. |
| 5 | **Butt et al. — "From Policy to Pipeline"** | 2026 | 0 | ⭐⭐ | Auch hier relevant (Cross-Referenz zu 4.2): Policy→Pipeline Governance in CI/CD. |
| 6 | **Finch & Butt — "Gaps in AI-Compliant Governance"** | 2025 | 0 | ⭐⭐ | Systematic Review zu Governance-Gaps. Gut für Problemstellung/Motivation der Kontrollmechanismen. |

### Monitoring & Audit (Query 2)

| # | Quelle | Jahr | Cit. | Eignung | Begründung |
|---|--------|------|------|---------|------------|
| 7 | **Radanliev et al. — "Generative AI cybersecurity and resilience"** | 2025 | 11 | ⭐ | Monitoring aus Security-Perspektive. Nur ergänzend. |
| 8 | **EU-weite Post-Market Surveillance Literatur** | — | — | ⭐ | Keine starke spezifische Quelle gefunden. → Primärquellen (Art. 72 AI Act, MDR-Analogie) bleiben besser. |

### Bewertung für Kapitel 4.4
**Sardana et al. (2024)** und **Romeo et al. (2025)** sind die wichtigsten Neufunde. Sardana liefert "CaC 2.0" als Weiterentwicklung des Policy-as-Code-Konzepts mit Agentic AI — perfekte Kontextualisierung für die Thesis. Romeo verbindet RAG + PaC, was direkt auf die RAG-Grauzone-Entscheidung (Entscheidung 2) aufsetzt.

**Empfohlenes Argument in 4.4:** Kovac et al. als RegOps-Basis, Sardana et al. als CaC-Evolution, Romeo et al. als RAG-PaC-Verbindung. Monitoring bleibt primärquellenbasiert (Art. 72 AI Act).

---

## Abschnitt 4.5 — Human Oversight (Art. 14)

### Suchanfrage
`"human oversight Article 14 EU AI Act high-risk AI systems technical implementation automated decision making intervention mechanisms"`

### Top-Empfehlungen

| # | Quelle | Jahr | Cit. | Eignung | Begründung |
|---|--------|------|------|---------|------------|
| 1 | **Laux — "Institutionalised Distrust and Human Oversight of AI"** | 2023 | 63 | ⭐⭐⭐ | **Höchstzitiert in allen Queries.** Grundlegendes Paper zu Human Oversight im EU AI Act. Konzept "institutionalised distrust" als theoretischer Rahmen. **Kern-Paper für 4.5.** |
| 2 | **Sterz et al. — "On the Quest for Effectiveness in Human Oversight"** | 2024 | 51 | ⭐⭐⭐ | 51 Zitationen. Systematische Analyse der Effektivität von Human Oversight. Direkt anwendbar auf Gate-Design (wann ist Oversight wirksam?). |
| 3 | **Enqvist — "'Human Oversight' in the EU AI Act"** | 2023 | 48 | ⭐⭐⭐ | Rechtswissenschaftliche Analyse des Art. 14 Begriffs. 48 Zitationen. Notwendig für normative Fundierung. |
| 4 | **Sarra — "AI in Decision-making: EU AI Act vs GDPR"** | 2025 | 6 | ⭐⭐ | Vergleich AI Act / GDPR bei automatisierter Entscheidungsfindung. Ergänzend für Abgrenzung Art. 14 vs. Art. 22 DSGVO. |
| 5 | **Ho-Dac & Martinez — "Human Oversight and Technical Standardisation"** | 2024 | 2 | ⭐⭐ | Verbindung Oversight ↔ Standardisierung (CEN/CENELEC). Relevant für technische Operationalisierung. |

### Bewertung für Kapitel 4.5
Die stärkste Ergebnisgruppe aller Queries. **Laux (2023, 63 Zit.)**, **Sterz et al. (2024, 51 Zit.)** und **Enqvist (2023, 48 Zit.)** bilden ein exzellentes Triangulierungstrio: Laux liefert den konzeptionellen Rahmen ("institutionalised distrust"), Enqvist die normative Analyse, Sterz et al. die Effektivitäts-Evaluation.

**Empfohlenes Argument in 4.5:**
- Art. 14 Normtext als Basis
- Enqvist für rechtswissenschaftliche Auslegung
- Laux für theoretischen Rahmen
- Sterz et al. für Wirksamkeits-Anforderung → daraus Quality-Gate-Kriterium ableiten

⚠ **Alle drei sind 2023–2024**, also methodisch etabliert und breit zitiert. Stärkste Evidenzbasis aller Abschnitte.

---

## Abschnitt 4.6 — Requirements-Katalog (R1–Rn, Traceability)

### Suchanfragen
1. `"AI regulation requirements catalog EU AI Act compliance framework systematic"`
2. `"quality gates AI system lifecycle requirements traceability design principles"`

### Top-Empfehlungen

| # | Quelle | Jahr | Cit. | Eignung | Begründung |
|---|--------|------|------|---------|------------|
| 1 | **Elia et al. — "MQG4AI: Methodology based on Quality Gates for Responsible High-Risk AI"** | 2025 | 0 | ⭐⭐⭐ | **Exakt passend:** Quality-Gate-Methodik für AI Lifecycle, Responsible AI, regulatory demands. Direkte Parallele zur Thesis-Methodik. **Kern-Paper für 4.6.** |
| 2 | **Elia & Bauer — "Quality Gates for Certifiable AI in Medicine"** | 2023 | 3 | ⭐⭐⭐ | Vorgänger-Paper zu MQG4AI. Methodik: abstrakte Norm-Konzepte → konkrete Instructions via Quality Gates. Direkt zitierfähig für Transformationslogik. |
| 3 | **Corrêa & Mönig — "Catalog of General Ethical Requirements for AI Certification"** | 2024 | 2 | ⭐⭐ | Systematischer Requirements-Katalog für AI-Zertifizierung. Ergänzend für Katalog-Systematik. |
| 4 | **Lucaj et al. — "TechOps: Templates for AI Act"** | 2025 | 0 | ⭐⭐ | Dokumentations-Templates nach AI Act. Operationalisierungs-Evidenz. |
| 5 | **Golpayegani et al. — "AICat"** | 2024 | (tbd) | ⭐⭐ | AI-Cataloguing für EU AI Act. Strukturierter Ansatz. |

### Nicht geeignet
- Semenov et al. (2025) — Mathematisches Modell für Softwareentwicklung, zu weit entfernt → ❌
- Rangasamy (2026) — Generische QA/AI-Transformation, zu oberflächlich → ❌

### Bewertung für Kapitel 4.6
**Elia et al. (2025)** = MQG4AI ist der mit Abstand wichtigste Neufund: Quality Gates + AI Lifecycle + Responsible AI + Regulatory Demands — fast identischer Scope wie die Thesis. Zusammen mit dem Vorgänger **Elia & Bauer (2023)** ergibt sich eine direkte Methodik-Linie, die als Related Work und Abgrenzung dienen kann.

**Empfehlung:** MQG4AI als Hauptvergleichsquelle für den eigenen Requirements-Katalog. Abgrenzung: MQG4AI ist domänenspezifisch (Medizin/XAI), die Thesis-Architektur ist Deployer-generisch + Policy-as-Code.

---

## Gesamtübersicht — Top-12 Neufunde nach Eignung

| Rang | Quelle | Abschnitt | Eignung | Zitationen | Zentrale Relevanz |
|------|--------|-----------|---------|------------|-------------------|
| 1 | Laux (2023) | 4.5 | ⭐⭐⭐ | 63 | "Institutionalised distrust" — theoretischer Rahmen Human Oversight |
| 2 | Sterz et al. (2024) | 4.5 | ⭐⭐⭐ | 51 | Effektivität Human Oversight — Gate-Kriterium |
| 3 | Enqvist (2023) | 4.5 | ⭐⭐⭐ | 48 | Normative Analyse Art. 14 |
| 4 | Feng et al. (2024) | 4.3 | ⭐⭐⭐ | 18 | LLM-gestützte Normoperationalisierung |
| 5 | Kelly et al. (2024) | 4.3 | ⭐⭐⭐ | 17 | EU AI Act Compliance Mapping Methodik |
| 6 | Elia et al. (2025) / MQG4AI | 4.6 | ⭐⭐⭐ | 0 | Quality Gates + AI Lifecycle (Hauptvergleich) |
| 7 | Sardana et al. (2024) | 4.4 | ⭐⭐⭐ | 0 | Compliance-as-Code 2.0 mit Agentic AI |
| 8 | Romeo et al. (2025) | 4.4 | ⭐⭐⭐ | 1 | RAG + Policy-as-Code (ARPaCCino) |
| 9 | Butt et al. (2026) | 4.2 | ⭐⭐⭐ | 0 | Policy→Pipeline Governance (EU AI Act + NIST + ISO 42001) |
| 10 | Leon (2026) | 4.2 | ⭐⭐⭐ | 0 | Lifecycle-Based Governance Framework |
| 11 | Elia & Bauer (2023) | 4.6 | ⭐⭐⭐ | 3 | Quality Gates for Certifiable AI (Vorgänger MQG4AI) |
| 12 | Pistilli et al. (2023) | 4.3 | ⭐⭐ | 25 | Ethik-Recht-Technik Artikulation |

---

## Abgrenzung zu bestehenden Kernquellen

| Bestehende Quelle | Status | Bestätigt durch Elicit? |
|---|---|---|
| Buscemi et al. (2025) | ✅ Kernquelle | Ja — Top-Ergebnis in 4.3 + 4.6 Queries |
| Kovac et al. (2025) / CERTAIN | ✅ Kernquelle | Ja — Top-Ergebnis in 4.4 Query |
| Jonnala et al. (2025) | ✅ Konvergent | Nicht direkt gefunden (spezifische Gap-Analyse) |
| Huwyler (2025) | ✅ Kernquelle | Nicht gefunden (Deployment-Governance Nische) |
| EU AI Act / NIST AI RMF | ✅ Primärquellen | Vielfach referenziert in gefundenen Papers |

**Interpretation:** Elicit bestätigt die bestehende Quellenbasis und ergänzt sie signifikant. Huwyler und Jonnala bleiben Nischenquellen, die nicht über Elicit auffindbar sind — das stützt ihre Rolle als spezifische, manuell identifizierte Beiträge.

---

## Empfohlene Zotero-Importe (Priorität)

### Sofort importieren (🔴 HOCH)
1. **Laux (2023)** — DOI: tbd, 63 Zitationen → Kap. 4.5
2. **Sterz et al. (2024)** — DOI: tbd, 51 Zitationen → Kap. 4.5
3. **Enqvist (2023)** — DOI: tbd, 48 Zitationen → Kap. 4.5
4. **Kelly et al. (2024)** — DOI: tbd, 17 Zitationen → Kap. 4.3
5. **Elia et al. (2025) / MQG4AI** — DOI: 10.48550/arXiv.2502.11889 → Kap. 4.6
6. **Elia & Bauer (2023)** — DOI: 10.5220/0012121300003538 → Kap. 4.6

### Bei Bedarf importieren (🟡 MITTEL)
7. **Feng et al. (2024)** — 18 Zitationen → Kap. 4.3
8. **Sardana et al. (2024)** — CaC 2.0 → Kap. 4.4
9. **Romeo et al. (2025)** — ARPaCCino → Kap. 4.4
10. **Butt et al. (2026)** — Policy→Pipeline → Kap. 4.2
11. **Pistilli et al. (2023)** — 25 Zitationen → Kap. 4.3

### Optional (🟢 NIEDRIG)
12. **Leon (2026)** → Kap. 4.2
13. **Corrêa & Mönig (2024)** → Kap. 4.6
14. **Gonçalves & Correia (2025)** → Kap. 4.4

---

## Kritische Fragen vor Weiterschreiben

1. **MQG4AI-Abgrenzung:** Elia et al. (2025) hat fast identischen Scope (Quality Gates + AI Lifecycle). Wie grenzt sich die Thesis ab? → Vorschlag: MQG4AI = domänenspezifisch (Medizin/XAI-Fokus), Thesis = Deployer-generisch + Policy-as-Code + EU AI Act Art. 9–15 vollständig.

2. **Human Oversight Tiefe:** Mit Laux/Sterz/Enqvist gibt es jetzt 162 kumulative Zitationen für 4.5. Soll 4.5 ein eigener Abschnitt werden oder in den Requirements-Katalog (4.6) integriert?

3. **2026-Quellen:** Butt et al. und Leon sind beide 2026 mit 0 Zitationen. Als konvergente Evidenz zu bestehenden Quellen OK, aber nicht als alleinige Stütze. Einverstanden?
