# Konsistenz-Überblick: Kap. 2 vs. geschriebene Kapitel (1, 3, 4, 5)

> **Stand:** 2026-03-07 | **Zweck:** Gesamtüberblick vor Literaturbasis-Erstellung
> **Methode:** Cross-Referencing aller DOCX-Inhalte (Kap. 1–5 + Exposé v4) gegen INHALTSPLAN_KAP2

---

## TABELLE 1: Begriffe — Wo eingeführt, wo genutzt, was Kap. 2 liefern MUSS

| Begriff / Konzept | Kap. 1 (Einleitung) | Kap. 3 (Methodik) | Kap. 4 (Anforderungen) | Kap. 5 (Architektur) | Kap. 2 Abschnitt | Status |
|---|---|---|---|---|---|---|
| GenAI (Generative KI) | ✅ Def. (Feuerriegel, S. 111) | erwähnt | verwendet | — | 2.1 + 2.2 | ⚠ Kap. 1 hat bereits Def. → 2.1 muss vertiefen, NICHT wiederholen |
| LLM (Large Language Model) | erwähnt, keine Def. | — | verwendet | — | 2.1 + 2.2 | ❗ Muss in 2.1 definiert werden (Arbeitsdefinition) |
| MLOps | ✅ erwähnt (Kreuzberger) | Wissensbasis-Domäne | — | — | 2.4.1 | ⚠ Kap. 1 nennt Kreuzberger → 2.4.1 muss Tiefe liefern |
| LLMOps | ✅ erwähnt (Diaz-De-Arcaya) | — | — | — | 2.4.1 | ⚠ Kap. 1 zitiert "rezent, keine einheitl. Def." → 2.4.1 muss konsolidieren |
| GenAIOps | ✅ erwähnt (Joshi, Tantithamthavorn) | — | — | — | 2.1 (Arbeitsdef.) + 2.4.1 (Detail) | ⚠ Kap. 1 nutzt als "übergeordnetes Paradigma" → 2.4.1 liefert Fundierung |
| RAG (Retrieval-Augmented Generation) | erwähnt (1.2 PD3: Art. 25) | — | ✅ 4.1.3 Klassifizierung | — | 2.1 (Arbeitsdef.) + 2.2 (Pattern) | ❗ Kap. 4.1.3 setzt RAG-Verständnis voraus → 2.1/2.2 MUSS vor 4 kommen |
| Quality Gate | ✅ erwähnt (Elia et al., 2025) | Tab. 1 + Grid | ✅ 4.1 "Gate-basierter Kontrollprozess" | ✅ 5: WIE-Ebene (G-xx) | 2.5 | ❗ Kernbegriff! 2.5 muss formale Definition + Abgrenzung liefern |
| Policy-as-Code / Compliance-as-Code | ✅ erwähnt (Titel + PD3) | DSR Grid | ✅ 4.4 (OPA/Rego) | — | 2.6 | ❗ Kap. 4.4 setzt PaC-Verständnis voraus → 2.6 MUSS vor 4.4 gelesen werden |
| EU AI Act (VO 2024/1689) | ✅ detailliert (Art. 9-15, 26, 99, 113) | Tab. 2 Mapping | ✅ 4.1-4.5 (Deployer-Fokus) | — | 2.4.2 | ⚠ Kap. 1 sehr detailliert → 2.4.2 muss ERGÄNZEN, nicht wiederholen |
| Deployer vs. Provider | ✅ 1.2 PD3 (Art. 3, 16, 25, 26) | — | ✅ 4.1.1 (architekton. Scope) | — | 2.4.2 | ⚠ Kap. 1 + Kap. 4 beide detailliert → 2.4.2 Grundlagen, keine Wiederholung |
| Art. 25 Provider-Aufstieg | ✅ 1.2 PD3 (Fine-Tuning/RAG) | — | ✅ 4.1 (D_SCOPE_ART25) | — | 2.4.2 | ✅ Scope-Grenze in Kap. 3 Decision registriert |
| Accountability-by-Design | — | ✅ Exposé: Zielsetzung | ✅ 4.1.5 | — | 2.5 oder 2.7 | ⚠ In Kap. 4.1.5 eingeführt — braucht Fundierung in Kap. 2 |
| NIST AI RMF | — | ✅ Kernel Theory (DSR Grid) | ✅ 4.1.1, 4.4, 4.5 | — | 2.4.2 (erwähnen) | ⚠ Kap. 3 + 4 nutzen NIST intensiv → 2.4.2 muss einordnen |
| Dreistufige Transformation (Norm→R→Gate) | — | — | ✅ 4.3 (Kern) | — | 2.5 + 2.7 | ⚠ Konzept aus Kap. 4 → Kap. 2.5 legt Grundlage (Gate-Konzept), 2.7 verweist |
| Human Oversight (Art. 14) | ✅ 1.1 erwähnt | — | ✅ 4.5 (Sterz, Laux) | — | 2.4.2 (erwähnen) | ⚠ Detail in 4.5, Grundlage in 2.4.2 |
| Cloud-native | ✅ im Titel | Wissensbasis-Domäne | — | — | 2.3 | ❗ Bisher kein einziges Kapitel definiert Cloud-native → 2.3 MUSS |
| CI/CD/CT | ✅ 1.1 erwähnt | DSR Grid | ✅ 4.4 (Pipeline) | ✅ 5: Pipeline-Integration | 2.3 + 2.4.1 | ⚠ Wird überall vorausgesetzt, nirgends definiert → 2.3 oder 2.4.1 |
| MQG4AI (Elia et al.) | ✅ 1.1 (PD2: "kein vergleichb. Ansatz") | — | D_MQG4AI_PLACEMENT | ✅ Kap. 2 Entwurf vorhanden | 2.5 | ✅ Entwurf in Kap. 2 DOCX bereits begonnen (154W) |
| PD1/PD2/PD3 | ✅ Definiert in 1.2 | — | erwähnt | — | 2.7 (Rückverweis) | ✅ Kap. 2.7 verweist auf PDs → keine Redefinition nötig |
| DP1–DP5 | — | ✅ Exposé: Zielsetzung | — | — | 2.7 (Vorgriff) | ⚠ DPs in Exposé/Kap.3 definiert → 2.7 darf nicht vorgreifen, nur Lücke zeigen |
| S1–S4 (Artefakt-Komponenten) | ✅ 1.3 (Exposé-konsistent) | ✅ DSR Grid | — | — | 2.7 | ✅ Bereits in Kap. 1 + 3 konsistent |

---

## TABELLE 2: Konsistenz-Probleme und Handlungsbedarf

| # | Problem | Betroffene Kapitel | Schwere | Lösung in Kap. 2 |
|---|---|---|---|---|
| K1 | **GenAI-Definition bereits in Kap. 1** (Feuerriegel, S. 111) — Kap. 2.1 darf NICHT wiederholen | Kap. 1 ↔ Kap. 2.1 | ⚠ Mittel | 2.1 verweist auf Kap. 1 Def., vertieft auf Systemebene (LLM + Infrastruktur) |
| K2 | **EU AI Act extrem detailliert in Kap. 1** (Art. 9-15, 26, 99, 113, Fristen, Strafen) — Redundanzgefahr mit 2.4.2 | Kap. 1 ↔ Kap. 2.4.2 | 🔴 Hoch | 2.4.2 fokussiert auf Risikoklassifizierung + Deployer-Architekturimplikationen, NICHT Artikelaufzählung |
| K3 | **Deployer-Scope doppelt definiert**: Kap. 1.2 PD3 + Kap. 4.1.1 — 2.4.2 muss Grundlage OHNE Wiederholung liefern | Kap. 1 + Kap. 4 ↔ Kap. 2.4.2 | 🔴 Hoch | 2.4.2 nur regulatorische Grundstruktur (Rollen, Scope-Trigger Art. 25), Details → Kap. 4 |
| K4 | **Cloud-native nirgends definiert** — Titel enthält "cloud-native", aber kein Kapitel definiert es | Alle ↔ Kap. 2.3 | 🔴 Hoch | 2.3 MUSS Cloud-native sauber definieren (CNCF + Plattformfähigkeiten) |
| K5 | **CI/CD/CT wird überall vorausgesetzt** — in Kap. 1, 3, 4 verwendet, nirgends eingeführt | Alle ↔ Kap. 2.3/2.4.1 | ⚠ Mittel | 2.3 (IaC/GitOps) oder 2.4.1 (CI/CD für GenAI) |
| K6 | **Quality Gate nur als Label** — Kap. 1 + 4 nutzen den Begriff, formale Definition fehlt | Kap. 1 + 4 ↔ Kap. 2.5 | 🔴 Hoch | 2.5 liefert formale Definition + Abgrenzung (≠ Milestone ≠ Review) |
| K7 | **PaC/CaC als Konzept nicht eingeführt** — Kap. 4.4 nutzt OPA/Rego, Grundlage fehlt | Kap. 4.4 ↔ Kap. 2.6 | 🔴 Hoch | 2.6 MUSS PaC-Konzept fundieren BEVOR Kap. 4.4 gelesen wird |
| K8 | **Accountability-by-Design in Kap. 4.1.5** — Konzept erscheint in Kap. 4 ohne Kap. 2-Fundierung | Kap. 4.1.5 ↔ Kap. 2 | ⚠ Mittel | Kurze Einordnung in 2.5 (als Designprinzip-Klasse) oder 2.7 |
| K9 | **NIST AI RMF Kernel Theory** — Kap. 3 DSR Grid nutzt NIST, aber 2.4.2 erwähnt es nicht im Plan | Kap. 3 ↔ Kap. 2.4.2 | ⚠ Mittel | 2.4.2 muss NIST AI RMF als komplementären Rahmen einordnen |
| K10 | **MQG4AI-Entwurf existiert bereits** — Kap. 2 DOCX hat 154W zur Abgrenzung. Passt zu 2.5, aber noch kein Abschnitt 2.5 geschrieben | Kap. 2 (DOCX) ↔ INHALTSPLAN 2.5 | ✅ Gering | Bestehenden Entwurf in 2.5 integrieren |

---

## TABELLE 3: Quellen-Mapping — Bereits zitierte Quellen → Kap. 2 Abschnitte

### Legende: ★ = Schlüsselquelle für diesen Abschnitt | ○ = Ergänzungsquelle | — = nicht relevant

| Quelle | Kap.1 | Kap.3 | Kap.4 | Exposé | → 2.1 | → 2.2 | → 2.3 | → 2.4.1 | → 2.4.2 | → 2.5 | → 2.6 | → 2.7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Feuerriegel et al. (2024) | ✅ S.111 | — | — | — | ○ | ★ | — | — | — | — | — | ○ |
| Kreuzberger et al. (2023) | ✅ | — | — | ✅ | ○ | — | — | ★ | — | — | — | ★ |
| Joshi (2025) | ✅ S.7-8 | — | — | ✅ S.8 | ○ | — | — | ★ | — | — | — | ★ |
| Tantithamthavorn et al. (2025) | ✅ S.27 | — | — | ✅ | ★ | — | — | ★ | — | — | — | ○ |
| Diaz-De-Arcaya et al. (2024) | ✅ S.1 | — | — | ✅ S.3 | — | — | — | ★ | — | — | — | ○ |
| EU AI Act (2024) | ✅ Art.9-15,26,99 | — | ✅ Art.3,9-15,26 | ✅ | — | — | — | — | ★ | — | — | ○ |
| Novelli et al. (2024) | ✅ S.10,14 | — | ✅ S.9 | — | — | — | — | — | ★ | — | — | ○ |
| Buscemi et al. (2025) | ✅ S.1 | — | ✅ S.7-8 | — | — | — | — | — | ○ | — | — | ★ |
| Guldimann et al. (2025) | ✅ S.1 | — | — | — | — | — | — | — | ○ | — | — | ○ |
| Elia et al. (2025) | ✅ S.3 | — | D_MQG4AI | — | — | — | — | — | — | ★ | — | ★ |
| Nellutla (2025) | ✅ S.1 | — | — | — | — | ○ | — | — | — | ○ | — | — |
| Billeter et al. (2024) | ✅ S.1 | — | — | — | — | — | — | — | — | — | — | ○ |
| Blancato (2024) | ✅ S.12 | — | — | — | — | — | ○ | — | ○ | — | — | — |
| Hevner et al. (2004) | — | ✅ S.75-83 | ✅ | ✅ | — | — | — | — | — | — | — | — |
| Peffers et al. (2007) | — | ✅ S.52-56 | — | ✅ | — | — | — | — | — | — | — | — |
| vom Brocke & Maedche (2019) | — | ✅ S.379-380 | — | ✅ | — | — | — | — | — | — | — | — |
| Huwyler (2025) | — | — | ✅ S.3 | — | — | — | — | — | ★ | — | — | ○ |
| Kelly et al. (2024) | — | — | ✅ | — | — | — | — | — | ★ | — | — | ○ |
| Laux et al. (2024) | — | — | ✅ 4.5 | — | — | — | — | — | ★ | — | — | ★ |
| Burns et al. (2025) | — | — | — | — | — | — | — | — | ★ | — | ★ | ○ |
| Pourmajidi et al. (2025) | — | — | — | — | — | — | ★ | — | — | — | ★ | ★ |
| Mahr et al. (2024) | — | — | — | — | — | — | — | ★ | — | ★ | — | ★ |
| Pahune & Akhtar (2025) | — | — | — | ✅ S.23 | — | — | — | ★ | — | — | — | ○ |
| Xu et al. / RAGOps (2025) | — | — | — | ✅ S.14-15 | ○ | ★ | — | ★ | — | — | — | ○ |
| Sinha et al. (2024) | — | — | — | ✅ S.1-2 | — | ○ | — | ○ | — | — | — | — |
| Sterz et al. (2024) | — | — | ✅ 4.5 | — | — | — | — | — | — | — | — | — |
| Leon (2026) | — | — | ✅ 4.2 | — | — | — | — | — | — | — | — | — |
| Ray (2026) | — | — | ✅ 4.2,4.4 | — | — | — | — | — | — | — | ○ | — |
| Romeo et al. (2025) | — | — | ✅ 4.4 | — | — | — | — | — | — | — | ○ | — |
| Kovac et al. (2025) | — | — | ✅ 4.4 | ✅ | — | — | — | — | — | — | ○ | ○ |
| Sardana et al. (2024) | — | — | ✅ 4.4 | — | — | — | — | — | — | — | ○ | — |
| Gallina et al. (2025) | — | — | ✅ 4.3 | — | — | — | — | — | — | — | — | ○ |
| Feng et al. (2024) | — | — | ✅ 4.3 | — | — | — | — | — | — | — | — | — |
| Díaz-Rodríguez et al. (2023) | — | — | — | — | — | — | — | — | — | ★ | — | ○ |

### NOCH NICHT ZITIERT aber im INHALTSPLAN als Primärquellen:

| Quelle | Geplanter Abschnitt | Status |
|---|---|---|
| Bommasani et al. (2021) — Foundation Models | 2.1, 2.2 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Vaswani et al. (2017) — Transformer | 2.1 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Lewis et al. (2020) — RAG Paper | 2.1 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Wei et al. (2022) — Emergent Abilities | 2.2 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Huang et al. (2023) — Hallucination Survey | 2.2 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Shankar et al. (2024) — LLM Evaluation | 2.2 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| CNCF (2018) — Cloud-native Def. | 2.3 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Kratzke & Quint (2017) — Cloud-native | 2.3 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Burns et al. (2016) — Borg/Omega/K8s | 2.3 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Cooper (1990/2008) — Stage-Gate | 2.5 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Humble & Farley (2010) — Continuous Delivery | 2.5 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Stigler (2020) — Policy-as-Code | 2.6 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |
| Smuha (2021) — Risk-based AI Regulation | 2.4.2 | ❗ Nicht in Zotero gefunden — manuell hinzufügen |

---

## TABELLE 4: Argumentationsfluss Kap. 1 → Kap. 2 → Kap. 3/4/5

| Kap. 1 stellt fest... | Kap. 2 fundiert... | Kap. 3/4/5 operationalisiert... |
|---|---|---|
| PD1: Fragmentierung MLOps→GenAIOps | 2.4.1: Evolution MLOps→LLMOps→GenAIOps zeigen | Kap. 4: Lifecycle-Modell (4.2) |
| PD2: QA-Mechanismen inadäquat | 2.2: LLM-Risiken + 2.5: Quality Gates als Lösung | Kap. 4.3: Transformation + Kap. 5: Gate-Spezifikation |
| PD3: Compliance-Operationalisierungslücke | 2.4.2: EU AI Act Grundlagen + 2.6: PaC-Konzept | Kap. 4.1-4.5: Anforderungen + Kap. 5: Pipeline |
| Dreifache Lücke → integrierter Ansatz | 2.7: Synthese bestätigt Lücke aus Literatur | Kap. 4.6: R-Katalog → Kap. 5: Architektur |
| Cloud-native im Titel | 2.3: Cloud-native Plattformfähigkeiten | Kap. 5: Azure-basierter PoC |
| Deployer-Perspektive (Art. 26) | 2.4.2: Rollenverteilung Provider/Deployer | Kap. 4.1.1: Architektonischer Scope |
| S1-S4 Artefakt-Komponenten | 2.7: Related Work zeigt → kein vergleichbarer Ansatz | Kap. 5: Architekturentwicklung |

---

## TABELLE 5: Redundanz-Risiko-Matrix

| Thema | Kap. 1 (Umfang) | Kap. 2 (geplant) | Kap. 4 (geschrieben) | Redundanz-Risiko | Abgrenzungsstrategie |
|---|---|---|---|---|---|
| EU AI Act Artikel | ~400W (Art. 9-15, 26, 99, 113) | 2.4.2: ~600W | 4.1-4.5: ~3000W | 🔴 HOCH | Kap. 2 = Struktur + Rollen; Kap. 4 = funktionale Transformation; Kap. 1 = Problemkontext |
| Deployer-Pflichten | ~200W (PD3) | 2.4.2: Teil davon | 4.1.1: ~500W | 🔴 HOCH | Kap. 2 = regulatorische Grundlage; Kap. 4 = architektonischer Scope-Entscheid |
| Quality Gates | ~50W (Elia-Verweis) | 2.5: ~450W | 4.3: Transformation | ⚠ MITTEL | Kap. 2 = Konzept + Definition; Kap. 4 = Anwendung auf EU AI Act |
| MLOps/LLMOps/GenAIOps | ~150W (Evolution) | 2.4.1: ~600W | — | ✅ GERING | Kap. 2 hat Monopol auf dieses Thema |
| RAG | ~80W (Art. 25) | 2.1+2.2: ~150W | 4.1.3: ~300W | ⚠ MITTEL | Kap. 2 = Pattern-Definition; Kap. 4 = regulatorische Klassifizierung |
| Cloud-native | ~0W (nur Titel) | 2.3: ~450W | — | ✅ GERING | Kap. 2 hat Monopol |
| PaC/CaC | ~20W (erwähnt) | 2.6: ~450W | 4.4: ~650W | ⚠ MITTEL | Kap. 2 = Konzept; Kap. 4 = Kontrollmechanismus-Anwendung |

---

## DIAGNOSE: 3 Kritische Findings

### Finding 1: EU AI Act Redundanz-Dreieck (K2 + K3)
Kap. 1 hat bereits ~400 Wörter zu EU AI Act Artikeln, Fristen, Strafen. Kap. 4 hat ~3000 Wörter zur funktionalen Transformation. **Kap. 2.4.2 hat nur ~600W Budget** und DARF NICHT wiederholen.

→ **Strategie:** 2.4.2 fokussiert exklusiv auf:
  1. Risikoklassifizierung (4 Stufen — in Kap. 1 + 4 nicht systematisch dargestellt)
  2. Rollenarchitektur Provider/Deployer (Grundstruktur — Detail in 4.1.1)
  3. Art. 25 Scope-Trigger (Kurzfassung — Detail in 4.1.1)
  4. NIST AI RMF als komplementärer Rahmen (→ Kap. 3 nutzt als Kernel Theory)

### Finding 2: 13 Quellen fehlen in Zotero
Der INHALTSPLAN listet 13 Primärquellen die NICHT in Zotero gefunden wurden (Bommasani, Vaswani, Lewis, Wei, Huang, Shankar, CNCF, Kratzke, Burns 2016, Cooper, Humble/Farley, Stigler, Smuha). Diese müssen manuell in Zotero importiert werden BEVOR mit dem Schreiben begonnen wird.

→ **Aktion:** Zotero-Bibliothek mit diesen 13 Quellen ergänzen (DOIs bekannt, Import via DOI möglich)

### Finding 3: Cloud-native + CI/CD/CT Definitionslücke (K4 + K5)
Der Titel der Arbeit enthält "cloud-native", aber KEIN geschriebenes Kapitel definiert diesen Begriff. CI/CD/CT wird in Kap. 1, 3, 4 und Exposé vorausgesetzt. Kap. 2.3 ist die EINZIGE Stelle wo diese Grundlagen gelegt werden.

→ **Priorität:** 2.3 ist architekturkritisch — ohne 2.3 hängen alle Cloud-native-Bezüge in der Luft.

---

## NÄCHSTE SCHRITTE

1. **Zotero-Auffüllung:** 13 fehlende Quellen manuell importieren
2. **Schreibreihenfolge:** Option A (sequenziell 2.1→2.7) — bestätigt durch Konsistenz-Analyse
3. **Pro Abschnitt:** Preflight → Quellen-Selektion aus TABELLE 3 → GO → Writer-Skill
4. **Redundanz-Kontrolle:** Bei jedem Abschnitt TABELLE 5 konsultieren → Abgrenzungsstrategie einhalten
5. **Offene Entscheidung:** Budget-Verteilung + Tiefe 2.7 (OQ-2.1 + OQ-2.2 aus chapter_state)
