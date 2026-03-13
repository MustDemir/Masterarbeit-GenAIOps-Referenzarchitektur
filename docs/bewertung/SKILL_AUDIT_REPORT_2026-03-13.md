# Skill-Audit-Report: Thesis-Workflow Plugin
> **Datum:** 2026-03-13
> **Scope:** Alle 6 Skills (session-manager, preflight, writer, reviewer, consistency, post-session)
> **Methode:** Vollständige Extraktion aller Datei-Referenzen aus SKILL.md → Existenz-Check gegen Repo

---

## Zusammenfassung

| Schweregrad | Anzahl | Beschreibung |
|-------------|--------|--------------|
| ⛔ KRITISCH | 6 | Skills brechen / finden Dateien nicht |
| ⚠️ HOCH | 4 | Silent Failures, fehlende Infrastruktur |
| 🔵 MITTEL | 4 | Verbesserungspotenzial, Inkonsistenzen |
| **GESAMT** | **14** | |

---

## ⛔ KRITISCH — Skills brechen ohne Fix

### F-01: Exposé-PDF existiert nicht am referenzierten Pfad
- **Betroffene Skills:** preflight (P1), reviewer (R2), consistency (K5)
- **Referenziert:** `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf`
- **Realität:** `docs/expose/` enthält nur README.md, chapter_state.yaml, legacy/ — **KEIN PDF**
- **Tatsächliches Exposé:** `00_admin/DMT_Demir_Exposé_2009670_final.pdf`
- **Impact:** 3 Skills können das Exposé nicht laden → P1, R2, K5 laufen ins Leere
- **Fix-Optionen:**
  - (A) Skills auf `00_admin/DMT_Demir_Exposé_2009670_final.pdf` updaten
  - (B) PDF nach `docs/expose/` kopieren mit erwartetem Namen
  - **Empfehlung:** Option A (Single Source of Truth beibehalten)

---

### F-02: Kap. 5 DOCX Name-Mismatch (`_v2` Suffix)
- **Betroffene Skills:** preflight (P2), reviewer (R1/R2), consistency (K1)
- **Referenziert:** `Kapitel 5 Architectur Entwicklung.docx`
- **Realität:** `Kapitel 5 Architectur Entwicklung_v2.docx`
- **Impact:** Alle Skills die Kap. 5 Volltext laden wollen finden die Datei nicht
- **Fix-Optionen:**
  - (A) Datei umbenennen → `Kapitel 5 Architectur Entwicklung.docx` (ohne _v2)
  - (B) Alle Skills auf `_v2` updaten
  - **Empfehlung:** Option A (kein Versionssuffix in Dateinamen — Git trackt Versionen)

---

### F-03: Reviewer hat falschen Kap. 2 Dateinamen
- **Betroffener Skill:** thesis-reviewer (R1, "Verfügbare Volltexte" + R2)
- **Referenziert:** `Kapitel 2 Problemstellung.docx`
- **Realität:** `Kapitel 2 Theoretische Grundlagen.docx`
- **Impact:** Reviewer findet Kap. 2 Volltext nicht → R1 + R2 für Kap. 2 fehlerhaft
- **Fix:** `thesis-reviewer/SKILL.md` korrigieren: "Problemstellung" → "Theoretische Grundlagen"

---

### F-04: Reviewer referenziert nicht-existierendes Exposé-DOCX
- **Betroffener Skill:** thesis-reviewer ("Verfügbare Volltexte")
- **Referenziert:** `Expose_v4_final_2026-02-28.docx` (in Fulltext-Liste)
- **Realität:** Exposé ist ein PDF in `00_admin/`, kein DOCX in `00_workspace/Fulltext_Kapitel/`
- **Impact:** Reviewer kann Exposé nie als DOCX laden (es existiert gar nicht als DOCX)
- **Fix:** Aus "Verfügbare Volltexte"-Liste entfernen, stattdessen in R2 auf PDF referenzieren

---

### F-05: ENTSCHEIDUNGSPAPIER_KAP5.md nicht in Skills referenziert
- **Datei:** `docs/ENTSCHEIDUNGSPAPIER_KAP5.md` (14.7 KB, gut befüllt)
- **Problem:** KEIN EINZIGER Skill referenziert es — alle verweisen nur auf `ENTSCHEIDUNGSPAPIER_KAP4.md`
- **Impact:** Kap. 5 (RQ2-Kern!) wird ohne seine eigenen Designentscheidungen geschrieben/reviewed
- **Betroffene Skills:** preflight (P4), writer (implizit), reviewer (R5), consistency (K2)
- **Fix:** Alle 4 Skills um `docs/ENTSCHEIDUNGSPAPIER_KAP5.md` ergänzen
- **Muster:** P4 sollte generisch `docs/ENTSCHEIDUNGSPAPIER_KAP{N}.md` laden (dynamisch)

---

### F-06: Root README.md fehlt
- **Betroffener Skill:** session-manager (S1 "Zusätzlich lesen: README.md")
- **Realität:** Root-`README.md` existiert nicht. Vorhanden: `00_admin/README.md` (16 KB), `docs/README.md` (209 B)
- **Impact:** Session-Start hat unvollständigen Projektkontext
- **Fix-Optionen:**
  - (A) `00_admin/README.md` nach Root symlinken/kopieren
  - (B) Session-Manager auf `00_admin/README.md` updaten
  - **Empfehlung:** Option B (00_admin ist der richtige Ort für Admin-Dateien)

---

## ⚠️ HOCH — Silent Failures

### F-07: `docs/expose/expose_deltas.yaml` fehlt
- **Betroffene Skills:** reviewer (R5), consistency (K5)
- **Referenziert:** `docs/expose/expose_deltas.yaml` — Exposé-Drift-Tracking
- **Realität:** Datei existiert nicht, wurde nie angelegt
- **Impact:** Exposé-Drift wird nicht systematisch getrackt; Skills ignorieren den Schritt still
- **Fix:** Leeres YAML-Template erstellen mit Header-Struktur

---

### F-08: DRAFT-Pfade inkonsistent zwischen Kapiteln
- **Betroffene Skills:** writer ("In DRAFT-Datei speichern"), post-session (A)
- **Writer erwartet:** `{kapitel_ordner}/Kap{N}_*_DRAFT.md` (direkt im Kapitel-Root)
- **Realität:**

| Kapitel | DRAFT-Pfad | Tiefe | Namenschema |
|---------|-----------|-------|-------------|
| Kap. 1 | `01_.../arbeitsmaterial/drafts/Kap1_Einleitung_DRAFT.md` | 2 Ebenen | `Kap{N}_*_DRAFT.md` |
| Kap. 2 | `02_.../arbeitsmaterial/drafts/Kap2_Theoretische_Grundlagen_DRAFT.md` | 2 Ebenen | `Kap{N}_*_DRAFT.md` |
| Kap. 3 | **KEIN DRAFT** | — | Nur DOCX in Fulltext_Kapitel |
| Kap. 4 | `04_.../KAPITEL_4_GESAMT_DRAFT.md` + `legacy/04_0X/4_X_*_DRAFT.md` | Mixed (Root + 2 Ebenen) | `KAPITEL_{N}_GESAMT` + `{N}_{M}_*` |
| Kap. 5 | `05_.../05_02_.../arbeitsmaterial/drafts/Kap5_*_DRAFT.md` | **3 Ebenen** | `Kap{N}_{M}_*_DRAFT.md` |

- **Impact:** Writer + Post-Session können Drafts nicht zuverlässig via Glob finden
- **Fix:** Einheitliches Schema definieren: `{kapitel_ordner}/arbeitsmaterial/drafts/Kap{N}_*_DRAFT.md`

---

### F-09: Skill-interne Referenz-Dateien werden nicht aktiv geladen
- **Betroffene Skills:** ALLE (die `references/` Ordner haben)
- **Vorhandene Referenz-Dateien (nie explizit in SKILL.md referenziert):**

| Skill | Referenz-Datei | In SKILL.md erwähnt? |
|-------|---------------|---------------------|
| thesis-consistency | `references/terminology_register.md` | ❌ Nein |
| thesis-preflight | `references/critical_definitions.md` | ❌ Nein |
| thesis-preflight | `references/checklist_template.md` | ❌ Nein |
| thesis-writer | `references/apa7_rules.md` | ❌ Nein |
| thesis-writer | `references/pruefprotokoll_format.md` | ❌ Nein |
| thesis-post-session | `references/post_session_template.md` | ❌ Nein |

- **Impact:** Diese Referenz-Dateien wurden erstellt aber werden von keinem Skill geladen → toter Code
- **Fix:** Jede SKILL.md um explizite Lade-Anweisung ergänzen: "Lade zuerst `references/*.md`"

---

### F-10: Reviewer "Verfügbare Volltexte"-Liste ist statisch und veraltet
- **Betroffener Skill:** thesis-reviewer
- **Problem:** SKILL.md listet Volltexte statisch auf — diese Liste ist bereits falsch (F-02, F-03, F-04)
- **Impact:** Bei jedem neuen Kapitel oder Umbenennung muss SKILL.md manuell gepatcht werden
- **Fix:** Statische Liste durch dynamische Anweisung ersetzen:
  `"Scanne 00_workspace/Fulltext_Kapitel/*.docx und verwende alle gefundenen Dateien"`

---

## 🔵 MITTEL — Verbesserungspotenzial

### F-11: Zwei `.memory/` Ordner mit ähnlichen Dateien
- `genaiops-thesis/.memory/`: resume_context.txt, index.json, entscheidungsregister.md, blob_sync_state.json
- `ai-context-vault/.memory/`: resume_context.txt, index.json, blob_sync_state.json
- Session-Manager referenziert nur `ai-context-vault/.memory/`
- `genaiops-thesis/.memory/` wird von KEINEM Skill referenziert
- **Fix:** Klären: Ist genaiops-thesis/.memory/ noch in Benutzung? Falls ja: in Skills referenzieren. Falls nein: aufräumen.

---

### F-12: `chapter_state.yaml` Skelette (Kap. 6, 7, 8)
- Kap. 6: 169 B, Kap. 7: 159 B, Kap. 8: 169 B — wahrscheinlich leere Skelette
- Session-Manager S4 prüft "Definition of Ready" → diese Kapitel würden FAIL geben
- **Fix:** Nicht dringend (Kapitel noch nicht in Arbeit), aber bei Beginn initialisieren

---

### F-13: Kein Skill referenziert `ENTSCHEIDUNGSPAPIER_KAP{N}` dynamisch
- Alle Skills haben `ENTSCHEIDUNGSPAPIER_KAP4.md` hardcoded
- Es gibt bereits `ENTSCHEIDUNGSPAPIER_KAP5.md` (F-05)
- Weitere werden kommen (Kap. 6, 7)
- **Fix:** Dynamisches Pattern in Skills: `docs/ENTSCHEIDUNGSPAPIER_KAP{N}.md` (wobei N = Zielkapitel)

---

### F-14: Kap. 3 hat keinen DRAFT aber wird als Fallback erwartet
- `Kapitel_3_Forschungsdesign_und_Methodik.docx` existiert ✅
- Kein `Kap3_*_DRAFT.md` irgendwo im Repo
- Writer-Skill Fallback "wenn DOCX nicht lesbar → DRAFT.md" greift nie für Kap. 3
- **Fix:** Klarstellen in Skills dass Kap. 3 nur als DOCX existiert (ist unkritisch)

---

## Fix-Priorisierung (empfohlene Reihenfolge)

| # | Fix | Aufwand | Impact |
|---|-----|---------|--------|
| 1 | **F-01** Exposé-Pfad in 3 Skills korrigieren | 5 min | ⛔ 3 Skills gefixt |
| 2 | **F-02** Kap. 5 DOCX umbenennen (kein _v2) | 1 min | ⛔ 3 Skills gefixt |
| 3 | **F-03** Reviewer Kap. 2 Name korrigieren | 1 min | ⛔ 1 Skill gefixt |
| 4 | **F-04** Reviewer Exposé-DOCX aus Liste entfernen | 2 min | ⛔ 1 Skill gefixt |
| 5 | **F-05** + **F-13** Entscheidungspapiere dynamisch machen | 10 min | ⛔ 4 Skills gefixt |
| 6 | **F-06** Session-Manager README-Pfad korrigieren | 1 min | ⛔ 1 Skill gefixt |
| 7 | **F-10** Reviewer Fulltext-Liste dynamisch machen | 5 min | ⚠️ Zukunftssicher |
| 8 | **F-07** expose_deltas.yaml Template erstellen | 3 min | ⚠️ Feature aktiviert |
| 9 | **F-09** Referenz-Dateien in Skills einbinden | 15 min | ⚠️ 6 Dateien aktiviert |
| 10 | **F-08** DRAFT-Pfad-Schema vereinheitlichen | 20 min | ⚠️ Konsistenz |
| 11 | **F-11** .memory/ Duplikation klären | 5 min | 🔵 Aufräumen |
| 12 | **F-12** Skelett-chapter_states initialisieren | 10 min | 🔵 Bei Bedarf |
| 13 | **F-14** Kap. 3 DRAFT-Hinweis in Skills | 2 min | 🔵 Dokumentation |
