# Preflight-Protokoll: Kap. 2.1 — Begriffsabgrenzung und Systemkontext

> **Erstellt:** 2026-03-08 | **Skill:** thesis-preflight | **Status:** Bereit fuer GO

---

## Ergebnis P1 (Exposé): ✅ konsistent

- Exposé v4 definiert Kap. 2 als Rigor Cycle (Hevner et al., 2004).
- gliederung_v3.md: "2.1 Begriffsabgrenzung und Systemkontext (LLM, GenAI-System, RAG, LLMOps, Quality Gate, Policy-as-Code)"
- Kein Scope-Drift: 6 Kernbegriffe, Arbeitsdefinitionen, Detail in späteren Abschnitten.
- Exposé-Formulierung "GenAIOps als übergeordnetes Paradigma" → 2.1 legt Arbeitsdefinition, 2.4.1 fundiert.

## Ergebnis P2 (Kapiteltexte): ⚠ K1-Redundanzrisiko beachten

**Relevante Begriffe/Definitionen aus geschriebenen Kapiteln:**
- Kap. 1: GenAI bereits definiert via Feuerriegel et al. (2024, S. 111) → 2.1 darf NICHT wiederholen, muss auf Systemebene vertiefen (K1).
- Kap. 1.2 PD3: RAG als Art. 25-Scope-Trigger erwähnt → 2.1 gibt Arbeitsdefinition.
- Kap. 1: GenAIOps als "übergeordnetes Paradigma" (Joshi, Tantithamthavorn) → 2.1 gibt Arbeitsdefinition.
- Kap. 4.1: "Gate-basierter Kontrollprozess" → 2.1 muss kompatible Arbeitsdefinition liefern.
- Kap. 4.4: OPA/Rego als PaC-Implementierung → 2.1 muss konzeptionelle Basis legen.

**Forward-References in 2.1:**
- Quality Gate → 2.5 (Detail) → existiert in Gliederung ✅
- Policy-as-Code → 2.6 (Detail) → existiert in Gliederung ✅
- LLMOps/GenAIOps → 2.4.1 (Detail) → existiert in Gliederung ✅

**Kontinuität:** Kap. 1.6 (Aufbau der Arbeit) → leitet direkt zu Kap. 2 über. Kein vorheriger 2.x-Abschnitt.

**Kein DRAFT vorhanden** — 2.1 wird erstmalig geschrieben.

## Ergebnis P3 (Sessions/States): ✅ chapter_state initialisiert

- chapter_state.yaml: 5% progress, current_focus = "2.1 Begriffsabgrenzung"
- next_steps[0] = "2.1 Preflight durchführen" ← dieses Dokument
- Definition of Ready: teilweise erfüllt (done, current_focus, key_sources vorhanden; cross_chapter_dependencies definiert)
- 4 Open Questions (OQ-2.1 bis OQ-2.4) — keine blockiert 2.1 direkt
- Keine Session Summaries für Kap. 2 vorhanden (erstes Schreiben)

## Ergebnis P4 (Entscheidungen): ⚠ 3 Decisions relevant

**Direkt betroffene Entscheidungen:**
1. **D_UNI_HINWEISE_SSOT** — Stil-Regeln bindend: hohe Zitationsdichte, keine formalen Überleitungen, kein Fülltext, Ergebnisse durch Abgrenzung kontextualisieren.
2. **D_MQG4AI_PLACEMENT** — Elia et al. (2025) in Kap. 2 Related Work + Kurzreferenz Kap. 4.6 → betrifft 2.5, NICHT 2.1.
3. **Critical Definition: Deployer-Scope** — nur Art. 26 Pflichten; Provider-Pflichten (Art. 16) ausgeschlossen. Für 2.1 relevant bei GenAI-System-Definition (System = Deployer-Perspektive).

**Keine offenen Entscheidungen blockieren 2.1.**

## Ergebnis P5 (Quellen): ✅ Alle in Zotero verifiziert

### Pflicht-Quellen aus INHALTSPLAN:
| Quelle | Zotero-Key | Thema | Status |
|---|---|---|---|
| Bommasani et al. (2021) | DGRT9VNW | Foundation Models → LLM/GenAI-System | ✅ |
| Vaswani et al. (2017) | PYTFTL7K | Transformer-Architektur → LLM-Basis | ✅ |
| Lewis et al. (2020) | J9GLG9IS | RAG Original-Paper | ✅ |
| Kreuzberger et al. (2023) | QY49ZYXB | MLOps Definition → Abgrenzung LLMOps | ✅ |
| Tantithamthavorn et al. (2025) | C755FHJK | MLOps/LLMOps/FMOps Taxonomie | ✅ |
| Xu et al. / RAGOps (2025) | P998PMS3 | RAGOps → GenAIOps-Teilmenge | ✅ |

### Zusätzliche Pflicht-Quellen aus SSOT-Cluster 02_01:
| Quelle | Zotero-Key | Thema | Relevanz für 2.1 |
|---|---|---|---|
| Fernández-Llorca et al. (2025) | K5MIAY34 | EU AI Act Terminologie (AI system, GPAI, foundation model, GenAI) | ⭐⭐⭐ Zentral für GenAI-System-Definition — EU-Gesetzgeber-Perspektive |
| Kratzke & Quint (2017) | MM3ZHX5C | Cloud-Native Definition | ⭐ Eher 2.3, aber Cloud-native als Kontext-Stichwort in 2.1 möglich |
| Latona et al. (2024) | Y8AVSDTI | AI Review Lottery (LLM-assisted Peer Review) | ❌ Nicht relevant für 2.1 (Methodenkritik, nicht Begriffsabgrenzung) |

**Empfehlung:** Fernández-Llorca et al. (2025) als 7. Pflichtquelle für 2.1 aufnehmen — liefert die regulatorische Begriffssystematik (AI system → GPAI system → foundation model → generative AI), die direkt die GenAI-System-Definition informiert.

## Ergebnis P6 (Uni-Anforderungen): ✅ Budget kompatibel

- **Seitenbudget 2.1:** ~1,5 Seiten / ~450 Wörter (INHALTSPLAN)
- **Gesamtbudget Kap. 2:** ~14 Seiten / ~4.200 Wörter
- **SRH-Limit:** 60-80 Textseiten → Kap. 2 mit 14 Seiten im Rahmen
- **Gliederungstiefe:** 2.1 = 2. Ebene → OK (max. 4 Ebenen erlaubt)
- **DSR-Phase:** Rigor Cycle — Wissensbasis-Aufbau, keine Design-Entscheidungen
- **Scope-Drift:** keiner erkannt — 6 Arbeitsdefinitionen, Detail in Folgeabschnitten

**Prof. Prinz Stil-Checks:**
- ☐ Hohe Referenzierdichte: 7 Pflichtquellen für ~450W → mind. 1 Zitation/Absatz erreichbar
- ☐ Keine formalen Überleitungen ("Im Folgenden wird...")
- ☐ Auf Wesentliches reduziert — nur Arbeitsdefinitionen, keine Exkurse
- ☐ Ergebnisse durch Abgrenzung kontextualisieren (LLM ≠ klassisches ML, LLMOps ≠ MLOps)
- ☐ K1-Redundanz vermeiden: GenAI-Def. aus Kap. 1 referenzieren, nicht wiederholen

---

## Synthese — Argumentationsstruktur für Kap. 2.1:

**Brücke von Kap. 1.6:** Kap. 1.6 stellt den Aufbau der Arbeit vor und verweist auf Kap. 2 als theoretische Fundierung. → 2.1 beginnt ohne Überleitung direkt mit dem Definitionsbedarf.

| Absatz | Argumentativer Move | Logik | Brücke zum nächsten |
|--------|---------------------|-------|---------------------|
| 1 | **LLM definieren** — Transformer-basiert, Abgrenzung zu klassischem ML | Vaswani (2017) als Architektur-Basis, Bommasani (2021) als Capabilities/Risiko-Rahmen | → LLM allein ist kein System |
| 2 | **GenAI-System als Komposit** — LLM + Infrastruktur + Serving + Monitoring; EU-Begriffssystematik (AI system → GPAI → foundation model → generative AI) | Bommasani (2021) Foundation Model; Fernández-Llorca et al. (2025) EU-Terminologie | → GenAI-System-Betrieb erfordert Daten-Integration |
| 3 | **RAG als Enterprise-Pattern** — Retrieval-Augmented Generation, Abgrenzung: Pattern ≠ Produkt | Lewis et al. (2020) Original-Paper; Xu et al. (2025) RAGOps | → Betrieb solcher Systeme braucht Ops-Paradigma |
| 4 | **LLMOps/GenAIOps** — Arbeitsdefinition, Abgrenzung MLOps → LLMOps → GenAIOps (Erweiterungskette) | Kreuzberger et al. (2023) MLOps; Tantithamthavorn et al. (2025) Taxonomie | → Ops allein reicht nicht, braucht Kontrollmechanismen |
| 5 | **Quality Gate + Policy-as-Code** — Arbeitsdefinitionen als Kontrollkonzepte im GenAIOps-Lifecycle | Verweis auf 2.5 (Gate-Definition) und 2.6 (PaC-Fundierung) | → Brücke zu 2.2: technische Tiefe der LLM-Architektur |

**Brücke zu Kap. 2.2:** Letzter Satz markiert, dass die Arbeitsdefinitionen nun technisch fundiert werden müssen — 2.2 liefert die LLM-Architektur und ihre Qualitätsimplikationen.

---

## Inhalts-Checklist:

- ☐ LLM-Definition (Transformer-basiert, Abgrenzung klassisches ML)
- ☐ GenAI-System als Komposit (LLM + Infrastruktur + Serving + Monitoring)
- ☐ EU-Begriffssystematik referenzieren (Fernández-Llorca → AI system, GPAI, foundation model, generative AI)
- ☐ RAG-Arbeitsdefinition (Pattern, nicht Produkt)
- ☐ LLMOps/GenAIOps Arbeitsdefinition + Abgrenzung zu MLOps
- ☐ Quality Gate Arbeitsdefinition (Forward-Reference → 2.5)
- ☐ Policy-as-Code Arbeitsdefinition (Forward-Reference → 2.6)
- ☐ Deployer-Perspektive: GenAI-System = Deployer-Sicht (Art. 26), nicht Provider-Interna

## Negativ-Checklist — Was darf NICHT in Kap. 2.1:

- ❌ Keine ausführliche LLM-Architektur (Attention, Layers → 2.2)
- ❌ Keine EU AI Act Artikeldetails (Risikoklassen, Pflichten → 2.4.2)
- ❌ Keine MLOps-Geschichte oder Framework-Vergleich (→ 2.4.1)
- ❌ Keine Quality-Gate-Taxonomie oder Gate-Template (→ 2.5 + 5.3)
- ❌ Keine PaC-Tool-Vergleiche (OPA, Kyverno → 2.6)
- ❌ Keine Wiederholung der GenAI-Definition aus Kap. 1 (Feuerriegel, S. 111)
- ❌ Keine Provider-Perspektive (Art. 16) — nur Deployer-Scope (Art. 26)
- ❌ Keine formalen Überleitungen ("Im Folgenden wird...", "Abschließend...")
- ❌ Kein Retirement-Thema (Out-of-Scope per D_RETIREMENT_OUT)

## Pflicht-Zitate:

| Quelle | Zotero-Key | Für |
|---|---|---|
| Bommasani et al. (2021) | DGRT9VNW | Foundation Models / GenAI-System-Komposit |
| Vaswani et al. (2017) | PYTFTL7K | Transformer-Architektur → LLM-Basis |
| Lewis et al. (2020) | J9GLG9IS | RAG-Definition |
| Kreuzberger et al. (2023) | QY49ZYXB | MLOps-Definition → Abgrenzung |
| Tantithamthavorn et al. (2025) | C755FHJK | LLMOps/FMOps/GenAIOps-Taxonomie |
| Xu et al. / RAGOps (2025) | P998PMS3 | RAGOps als GenAIOps-Teilmenge |
| Fernández-Llorca et al. (2025) | K5MIAY34 | EU AI Act Begriffssystematik (AI system → GPAI → GenAI) |

## Offene Fragen (vor Schreiben klären):

1. **Fernández-Llorca Integration:** Soll die EU-Begriffssystematik (AI system → GPAI system → foundation model → generative AI) als eigenständiger Mini-Absatz in 2.1 stehen oder in den GenAI-System-Absatz integriert werden? → Empfehlung: Integration in Absatz 2 (GenAI-System als Komposit).
2. **Wortbudget-Verteilung:** 450W für 5 Absätze = ~90W/Absatz. Realistisch für 7 Pflichtquellen? → Ja, wenn Arbeitsdefinitionen kompakt bleiben (2-3 Sätze pro Begriff).
3. **Kratzke & Quint:** In 2.1 erwähnen (Cloud-native als Kontextbegriff) oder komplett in 2.3 belassen? → Empfehlung: in 2.3 belassen, 2.1 nur "cloud-native" als Attribut ohne Definition.

---

→ **Bereit für "GO"**
