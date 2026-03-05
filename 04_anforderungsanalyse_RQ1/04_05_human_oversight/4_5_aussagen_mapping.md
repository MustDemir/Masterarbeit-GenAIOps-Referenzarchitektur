# 4.5 Aussagen-Quellen-Mapping — Human Oversight

## Qualitätsbewertung der Quellen

| Quelle | Venue | Indexierung | Rolle |
|--------|-------|-------------|-------|
| Sterz et al. (2024) | ACM FAccT'24 | ACM DL, Scopus | **Primär-Anker** (4 Effektivitätsbedingungen) |
| Laux (2024) | AI & SOCIETY, Vol. 39(6), pp. 2853–2866, Springer | Scopus/WoS | **Primär-Anker** (Institutionalised Distrust) |
| Enqvist (2023) | Law, Innovation and Technology, Vol. 15(2), pp. 508–535, Taylor & Francis | Scopus/WoS | **Primär** (normative Art.-14-Analyse) |
| Ooms et al. (2025) | SSRN / Knowledge Centre Data & Society | — | Konvergent (Policy Prototyping, empirische Validierung) |
| EU AI Act (2024) | Normtext VO (EU) 2024/1689 | — | Normative Grundlage |

**Datums-Korrektur**: chapter_state listet "Laux (2023)" — korrekt ist **Laux (2024)**, publiziert 12/2024, AI & SOCIETY Vol. 39(6).

## Aussagen-Mapping

### These 1: Art. 14 als Querschnittsanforderung mit Effektivitätsgebot
**Behauptung**: Art. 14 Abs. 1 verlangt, dass Hochrisiko-KI-Systeme so konzipiert werden, dass sie wirksam von Menschen beaufsichtigt werden können — die Verordnung definiert jedoch nicht, was "wirksam" konkret bedeutet.
- **Primär**: Sterz et al. (2024), Zeile 521–544: Art. 14(1) "effectiveness [...] serves as a foundational principle that requires oversight measures to be capable of achieving their risk mitigation objective"
- **Primär**: Enqvist (2023), S. 519 [Zeile 130–134]: Art. 14(4)(a–e) listet Provider-Pflichten, aber "none of them includes obligations that stretch beyond the provider"
- **Konvergent**: Ooms et al. (2025), Zeile 84: "Certain terms in the obligations were considered overly vague and non-concrete leading to a lack of understandability"
- **Normativ**: EU AI Act Art. 14 Abs. 1–2

### These 2: Vier Effektivitätsbedingungen als Operationalisierungsrahmen
**Behauptung**: Sterz et al. definieren vier notwendige Bedingungen für effektive Human Oversight: Causal Power, Epistemic Access, Self-Control und Fitting Intentions.
- **Primär**: Sterz et al. (2024), Def. 3.1–3.5 (Zeile 255–337): "An oversight person is effective in their human oversight if and only if they have causal power, epistemic access, self-control, and fitting intentions"
- **Konvergent**: Enqvist (2023), S. 528 [Zeile 186–194]: "the competence (know-how) as well as authority (powers) of the human overseers will affect the reasonable expectations" → kongruent mit Causal Power + Epistemic Access
- **Konvergent**: Laux (2024), Zeile 82: "meaningful oversight requires that someone has the 'authority and competence to change the decision'" → kongruent mit Causal Power + Epistemic Access

### These 3: Mapping Art. 14(4)(a–e) auf die vier Bedingungen
**Behauptung**: Die fünf Maßnahmen aus Art. 14 Abs. 4 lassen sich systematisch auf die vier Effektivitätsbedingungen abbilden.
- **Primär**: Sterz et al. (2024), Zeile 607–632: (d)+(e) → Causal Power + Self-Control; (a)+(c) → Epistemic Access; (b) → Epistemic Access + Self-Control (Automation Bias); Fitting Intentions hat "little direct equivalent in the legal text"
- **Konvergent**: Enqvist (2023), S. 519–521 [Zeile 130–152]: Art. 14(4)(a–c) als "relational transparency" → Epistemic Access; (d)+(e) als "human interference" capabilities → Causal Power

### These 4: Institutionalised Distrust als Governance-Rahmen
**Behauptung**: Die sechs Prinzipien der Institutionalised Distrust (Laux) adressieren systematisch die Kompetenz- und Anreizprobleme von Oversight-Akteuren.
- **Primär**: Laux (2024), Zeile 107–141: Sechs Prinzipien: (1) Legitimacy/Justification, (2) Periodical Mandates, (3) Collective Decisions, (4) Limited Competence of Institutions, (5) Justiciability and Accountability, (6) Transparency
- **Primär**: Laux (2024), Tabelle 3 (Zeile 138–141): 2×2-Matrix (Kompetenz/Anreize × First-/Second-Degree) → alle 4 Bereiche adressiert
- **Konvergent**: Sterz et al. (2024), Table 1 (Zeile 472): Facilitators/Inhibitors entlang der 4 Bedingungen → komplementäre Operationalisierung

### These 5: First-/Second-Degree Oversight-Taxonomie
**Behauptung**: First-Degree Oversight (konstitutiv, counterfactual influence auf Output) und Second-Degree Oversight (korrektiv, nachträgliche Prüfung) erfordern unterschiedliche Governance-Mechanismen.
- **Primär**: Laux (2024), Zeile 76–82: "first-degree human oversight" = constituent; "second-degree human oversight" = corrective
- **Konvergent**: Enqvist (2023), S. 525–527 [Zeile 172–181]: Art. 14 differenziert nicht explizit zwischen Echtzeit-Monitoring und Output-Review → Lücke
- **Konvergent**: Ooms et al. (2025), Zeile 83: "A lack of expertise by the user to correctly perform the oversight" als Feasibility-Problem

### These 6: Geteilte Verantwortung Provider-Deployer und Deployer-Lücke
**Behauptung**: Art. 14 weist die Gestaltungspflicht dem Provider zu, während der Deployer die Ausführung verantwortet — die Verordnung lässt jedoch einen erheblichen Ermessensspielraum beim Deployer.
- **Primär**: Enqvist (2023), S. 517–519 [Zeile 125–139]: "the AIA thus vests much trust in providers to secure the sufficient human oversight infrastructure all the way to the user's end"
- **Primär**: Enqvist (2023), S. 529 [Zeile 194]: "The AIA's fairly sparse regulatory detail on the competency issues in human oversight is, in my view, a risk and flaw of the Regulation"
- **Konvergent**: Laux (2024), Zeile 135–136: "human oversight is a shared responsibility between AI developers and users"
- **Konvergent**: Ooms et al. (2025), Zeile 84: "proportionality of the measures was difficult to determine and might lead to providers taking the 'path of least resistance'"

## Entscheidungen-Check
- D_4.5_STRUCTURE: 4.5 als eigener Abschnitt → ✓
- D_2026_SOURCES: Keine 2026-Quellen in 4.5 → nicht relevant → ✓
- D_GATE_IDS_LOCATION: Keine Gate-IDs in 4.5, erst 4.6 → ✓
- Laux-Datum: Korrektur von 2023 → 2024 → ✓
- Ooms (SSRN): Nur konvergent, nie alleinige Quelle → ✓
