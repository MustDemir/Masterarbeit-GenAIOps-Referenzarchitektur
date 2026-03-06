# Skill-Plan: Thesis-Writing-Workflows als Cowork-Skills

> **Erstellt:** 2026-03-06 | **Status:** Entwurf → User-Review
> **Kontext:** Formalisierung der 3 Prüf-Ebenen + Zusatz-Features als wiederverwendbare Skills

---

## 1. IST-Zustand vs. Best Practice

### IST: Was wir haben (PREFLIGHT_CHECK_WORKFLOW.md)

| Ebene | Was existiert | Status |
|-------|--------------|--------|
| **E1 Preflight** (P1–P6) | 6 Prüfinstanzen, Ausgabeformat, Workflow-Diagramm | ✅ Dokumentiert, manuell ausgeführt |
| **E2 Prüfprotokoll** (BELEG/CLAIM/MATCH) | Format, Regeln, Tools, Quellen-Fallback-Kette | ✅ Dokumentiert, manuell ausgeführt |
| **E3 Post-Session** (A–F) | 6-Punkte-Checklist, Ausgabeformat | ✅ Dokumentiert, manuell ausgeführt |
| **Save-Workflow** | save.py + reindex.py + chapter_state.yaml | ✅ Automatisiert (Scripts) |
| **Resume-Workflow** | resume.py → resume_context.txt + thesis_state.md | ✅ Automatisiert (Scripts) |
| **Zitations-Finder** | Skill existiert (zitations-finder) | ✅ Aktiver Skill |
| **Related-Work-Comparator** | Skill existiert (related-work-comparator) | ✅ Aktiver Skill |

### GAPS: Was fehlt (aus Session-Analyse + Best Practices)

| Gap | Problem | Best-Practice-Referenz |
|-----|---------|----------------------|
| **G1 Keine Skill-Automatisierung** | E1/E2/E3 werden manuell durchlaufen, Claude "vergisst" Schritte | SemanticCite: automatisierte Citation-Verification |
| **G2 Kein Cross-Chapter-Consistency-Check** | D in Kap. 4 kann Kap. 3 widersprechen, unentdeckt | Paperpal/Trinka: Terminology-Consistency-Scanner |
| **G3 Keine Terminologie-Enforcement** | Critical Definitions existieren, werden aber nicht automatisch geprüft | Writefull: NLP-basierte Terminology-Konsistenz |
| **G4 Session-Start ohne Preflight** | Claude beginnt oft zu schreiben ohne systematischen Check | Scribbr/UNC: Structured Pre-Writing Checklists |
| **G5 Entscheidungsregister nicht persistent** | 40+ Decisions in .memory/ (gitignored) | DSR: Decision-Traceability als Kernforderung |
| **G6 Kein Seitenbudget-Tracking** | Budget-Überschreitung erst spät erkannt | Thesis-Tracking-Tools: Word-Count-Gates |
| **G7 Kein Exposé-Drift-Monitoring** | Abweichungen vom Exposé nicht systematisch erfasst | Academic Writing QA: Scope-Drift-Detection |
| **G8 chapter_state Skelette** | Kap. 1, 2, 5–8 haben leere States | CI/CD: "Definition of Ready" vor Arbeitsbeginn |
| **G9 Keine Forward-Reference-Validation** | Verweise auf Kap. X.Y die nicht existieren | Software: Dead-Link-Checker Analogie |

---

## 2. Skill-Architektur: 5 Skills

### Übersicht

```
thesis-workflows/
├── thesis-preflight/          ← Skill 1: VOR dem Schreiben
│   ├── SKILL.md
│   ├── references/
│   │   ├── checklist_template.md
│   │   └── critical_definitions.md
│   └── scripts/
│       └── preflight_check.py
│
├── thesis-writer/             ← Skill 2: WÄHREND dem Schreiben
│   ├── SKILL.md
│   ├── references/
│   │   ├── pruefprotokoll_format.md
│   │   └── apa7_rules.md
│   └── scripts/
│       └── validate_citations.py
│
├── thesis-post-session/       ← Skill 3: NACH dem Schreiben
│   ├── SKILL.md
│   ├── references/
│   │   └── post_session_template.md
│   └── scripts/
│       └── consistency_check.py
│
├── thesis-consistency/        ← Skill 4: Übergreifender Konsistenz-Check
│   ├── SKILL.md
│   ├── references/
│   │   └── terminology_register.md
│   └── scripts/
│       └── cross_chapter_scan.py
│
└── thesis-session-manager/    ← Skill 5: Session Start/Ende Orchestrierung
    ├── SKILL.md
    └── scripts/
        └── session_orchestrator.py
```

---

## 3. Skill-Spezifikationen

### Skill 1: `thesis-preflight` — VOR dem Schreiben

**Trigger:** "preflight", "neuer abschnitt", "kap X.Y schreiben", "GO vorbereiten", "prüf erstmal"

**Was der Skill tut (Kern):**
- Erkennt Zielabschnitt (aus User-Input oder chapter_state.yaml)
- Durchläuft P1–P6 systematisch
- Liest automatisch die richtigen Dateien (SOT-Hierarchie)
- Erstellt Preflight-Protokoll im definierten Format
- Endet mit "Bereit für GO"

**Features aus Session-Analyse:**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| SOT-Hierarchie-Check | Session: "gliederung_v3 > Kap. 3 > Kap. 4 > Entscheidungsregister > Exposé" | Automatische Reihenfolge der Quellen-Prüfung |
| Exposé-Konsistenz | Session: "du nimmst meine expose garnicht wahr" | P1 liest Exposé und prüft Alignment |
| DRAFT-Kontinuität | Session: "Liest sich der neue Abschnitt nahtlos nach dem bisherigen DRAFT?" | Vorherigen Absatz lesen, Brücke prüfen |
| Pflicht-Zitate-Liste | Session: Quellen-Fallback-Kette (Zotero → Uploads → Elicit → Semantic Scholar) | Identifiziert Quellen die zitiert werden MÜSSEN |
| Seitenbudget-Prüfung | Session: "14-15 vs 13 Seiten Inkonsistenz" | gliederung_v3 Budget vs. IST-Wortanzahl |
| Entscheidungs-Scan | Session: "D_4.6_VS_5.3_SEPARATION affects Kap. 3 but not documented" | thesis_state.md nach relevanten D_xxx scannen |
| Negativ-Checklist | PREFLIGHT_CHECK_WORKFLOW.md | "Was darf NICHT in diesen Abschnitt" |
| Forward-Reference-Check | Session: "Keine verwaisten Verweise!" | Prüft ob Ziel-Abschnitte existieren oder geplant sind |

**Neue Features (Best Practices):**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| chapter_state "Definition of Ready" | CI/CD Best Practice | Prüft ob chapter_state.yaml ausgefüllt ist BEVOR geschrieben wird |
| DSR-Phasen-Mapping | Peffers (2007) | Prüft ob Abschnitt korrekt in DSR-Phase verortet ist |
| Argument-Flow-Vorabprüfung | Thesify: 7-Step Guide | Logischer Fluss der geplanten Absätze |
| Scope-Drift-Detection | Academic Writing QA | Vergleich: geplanter Inhalt vs. Exposé-Erwartung |

---

### Skill 2: `thesis-writer` — WÄHREND dem Schreiben

**Trigger:** "GO", "schreib absatz", "weiter schreiben", "nächster absatz", "FINAL"

**Was der Skill tut (Kern):**
- Absatz schreiben → Prüfprotokoll erstellen → MATCH bewerten
- Bei ⚠/❌ → Absatz korrigieren
- Wortanzahl tracken (Budget-Awareness)
- Prüfprotokoll SICHTBAR in DRAFT-Datei

**Features aus Session-Analyse:**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| BELEG/CLAIM/MATCH | PREFLIGHT_CHECK_WORKFLOW.md Ebene 2 | Exakter Satz aus Quelle + Paraphrase + Bewertung |
| APA7 + Seitenangabe | Session: "Jedes Zitat braucht (Autor, Jahr, S. X)" | Enforced bei jedem Zitat |
| Zotero-Key Pflicht | Session: Zotero-Integration | Jede Zitation muss Zotero-Key enthalten |
| Quellen-Fallback-Kette | PREFLIGHT_CHECK_WORKFLOW.md | Zotero → Uploads → Elicit → Semantic Scholar → Consensus |
| Nummerierung max. 2. Ebene | Session: "Sub-Headings als Fettdruck" | Automatische Formatprüfung |
| SRH-Leitfaden-Check | Session: "Formales Vorgehen NICHT explizit beschreiben" | Prüft ob verbotene Formulierungen enthalten sind |
| Zitations-Finder-Integration | Bestehender Skill | Automatisch aufrufen bei jeder Zitation |
| Deployer-Scope-Guard | Session: "Art. 26, nicht Art. 16" | Warnt wenn Provider-Perspektive eingenommen wird |

**Neue Features (Best Practices):**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| Confidence-Scoring | SemanticCite Framework | 4-Klassen: Supported / Partially / Unsupported / Uncertain |
| Real-Time Word Count Gate | CI/CD: Build-Size-Check | Warnung bei Budgetüberschreitung pro Abschnitt |
| Terminology-Lock | Paperpal Consistency | Prüft ob neue Begriffe mit Critical Definitions übereinstimmen |
| Anti-Plagiat-Guard | Academic Writing Ethics | Kein Copy-Paste aus Quellen, nur Paraphrase + Beleg |

---

### Skill 3: `thesis-post-session` — NACH dem Schreiben

**Trigger:** "session ende", "post-session", "abschluss check", "fertig für heute", "save session"

**Was der Skill tut (Kern):**
- Checklist A–F durchlaufen
- DRAFT + Prüfprotokolle vorhanden?
- chapter_state.yaml aktualisiert?
- Session Summary erstellt (save.py)?
- Entscheidungsregister synchron?
- Konsistenz-Diff erstellen
- Exposé-Abweichungen dokumentieren

**Features aus Session-Analyse:**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| Delta-Report | PREFLIGHT_CHECK_WORKFLOW.md Ebene 3 | "Was war VOR der Session? Was ist NEU?" |
| chapter_state Vollständigkeits-Check | Session: "progress, status, done, next_steps" | Prüft ob alle Felder aktualisiert sind |
| Cross-Chapter-Impact-Check | Session: "D in Kap. X → Effekte in Kap. Y" | Prüft ob neue Decisions in andere States propagiert wurden |
| save.py Integration | Session: save-Workflow | Automatischer save.py Aufruf mit generiertem Summary |
| Git-Commit-Vorbereitung | Session: "commiten und pushen" | Staged Files + Commit-Message generieren |
| Verwaiste Forward-Refs | Session: "Verweis auf X.Y → existiert?" | Finaler Check auf tote Verweise |

**Neue Features (Best Practices):**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| Automated Diff Summary | CI/CD: Changelog-Generation | Git-Diff → menschenlesbares Delta |
| Quality Score | McGill Evaluation Framework | Numerischer Score pro Abschnitt (0–10) |
| Next-Session Briefing | Academic Writing Workflow | Generiert Startpunkt-Zusammenfassung für nächste Session |

---

### Skill 4: `thesis-consistency` — Übergreifender Konsistenz-Check

**Trigger:** "konsistenz prüfen", "cross-check", "terminologie check", "widersprüche finden", "alles konsistent?"

**Was der Skill tut (Kern):**
- Scannt ALLE chapter_state.yaml + DRAFT-Dateien
- Prüft Terminologie gegen Critical Definitions
- Findet widersprüchliche Decisions
- Prüft Seitenbudget-Gesamtrechnung
- Forward-Reference-Validation über alle Kapitel

**Features:**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| Terminology Scanner | Session: "gleiche Begriffe, gleiche Definitionen" | Prüft ob "Enforcement ≠ Dokumentation" etc. konsistent verwendet |
| Decision Conflict Detector | Session: "D_4.6_VS_5.3_SEPARATION" | Findet widersprüchliche D_xxx über Kapitel hinweg |
| Budget Aggregator | Session: "14-15 vs 13 Seiten" | Summiert alle Kapitel-Wortanzahlen → Gesamtseitencheck |
| Exposé-Drift-Monitor | Session: "Exposé muss als Basis dienen" | Tracked kumulative Abweichungen vom Exposé |
| Cross-Ref Validator | Session: "Querverweise sicherstellen" | Prüft alle "(vgl. Kap. X.Y)" auf Existenz |
| DSR-Kohärenz | DSR Best Practice | Prüft ob Hevner/Peffers/vom Brocke Rahmen konsistent durchgehalten |

---

### Skill 5: `thesis-session-manager` — Session Start/Ende Orchestrierung

**Trigger:** "neue session", "session starten", "wo waren wir", "resume", "weiter machen"

**Was der Skill tut (Kern):**
- Bei Session-Start: resume.py ausführen, Kontext laden, Preflight vorschlagen
- Bei Session-Ende: Post-Session-Check triggern, save.py ausführen
- Orchestriert die anderen 4 Skills

**Features:**

| Feature | Quelle | Beschreibung |
|---------|--------|-------------|
| Auto-Resume | resume.py Integration | Lädt thesis_state.md + resume_context.txt |
| chapter_state Init-Check | Session: "Kap. 1, 2, 5–8 Skelette" | Warnt wenn Ziel-Kapitel chapter_state leer ist |
| Preflight-Trigger | Orchestrierung | Schlägt automatisch Preflight für nächsten Abschnitt vor |
| Save-Orchestrierung | save.py Integration | Automatisiert End-of-Session Workflow |
| Progress Dashboard | update_progress.py | Zeigt aktuellen Gesamtfortschritt |

---

## 4. Implementierungsplan

### Phase 1: Kern-Skills (Priorität HOCH)

| # | Skill | Aufwand | Begründung |
|---|-------|---------|------------|
| 1 | `thesis-preflight` | ~2h | Höchster Impact: verhindert Fehler VOR dem Schreiben |
| 2 | `thesis-writer` | ~2h | Zweithöchster Impact: Qualitätssicherung WÄHREND Schreiben |
| 3 | `thesis-post-session` | ~1h | Dritter: Konsistenz NACH dem Schreiben |

### Phase 2: Erweiterungs-Skills (Priorität MITTEL)

| # | Skill | Aufwand | Begründung |
|---|-------|---------|------------|
| 4 | `thesis-consistency` | ~2h | Cross-Chapter-Checks, ab Kap. 2+ relevant |
| 5 | `thesis-session-manager` | ~1h | Orchestrierung, optimiert Gesamtworkflow |

### Phase 3: Optimierung (Priorität NIEDRIG)

| # | Aktion | Aufwand |
|---|--------|---------|
| 6 | Eval-Sets erstellen + testen | ~2h |
| 7 | Description-Optimization (Triggering) | ~1h |
| 8 | Script-Bundling (validate_citations.py, consistency_check.py) | ~3h |

---

## 5. Kritische Fragen

1. **5 Skills oder 3?** — Die Architektur hat 5 Skills. Alternative: 3 Skills (preflight + writer + post-session) und consistency/session-manager als Features integrieren. Weniger Skills = weniger Triggering-Konfusion, aber weniger modular.

2. **Script-Automatisierung vs. Prompt-Only?** — Scripts (Python) für deterministische Checks (Wortanzahl, Forward-Refs, Terminologie) vs. reine Prompt-Instruktionen für alles. Scripts sind zuverlässiger aber aufwändiger.

3. **Sofort alle oder inkrementell?** — Phase-1-First (3 Kern-Skills) und dann iterieren, oder alle 5 auf einmal? Empfehlung: Phase 1 first, weil wir Kap. 2 bald schreiben und sofort profitieren.
