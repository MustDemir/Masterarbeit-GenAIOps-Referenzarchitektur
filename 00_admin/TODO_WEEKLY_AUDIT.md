# TODO: Weekly Audit Agent einrichten

> Erstellt: 2026-03-03 | Status: Offen

## Was gemacht werden muss

### 1. Neue Dateien erstellen

| Datei | Zweck |
|-------|-------|
| `.github/workflows/weekly-audit.yml` | GitHub Actions Workflow (Sonntag 07:00 UTC + manuell) |
| `scripts/weekly_audit.py` | Python-Skript mit allen Checks (~400 Zeilen) |

### 2. GitHub Labels anlegen (einmalig)

```bash
gh label create audit --repo MustDemir/Masterarbeit-GenAIOps-Referenzarchitektur --color 0075ca
gh label create "audit:errors" --repo MustDemir/Masterarbeit-GenAIOps-Referenzarchitektur --color d73a4a
```

### 3. Was der Audit pruefen soll

**Struktur & Konventionen:**
- session_summaries/ nur YAML-Dateien
- Expose-Datei (*_encrypted.pdf) vorhanden
- Bilder in images/final/ mit _vNN.png Suffix
- _status.yml Schema (kapitel, progress, status)
- .gitignore Sicherheitsregeln intakt

**Security:**
- Keine unverschluesselten PDFs in docs/expose/
- Keine Secrets (.env, *.key, *.pem) in Git getrackt

**Artefakt-Qualitaet:**
- R*.yaml (Requirements): Felder ausgefuellt vs. leer
- G*.yaml (Quality Gates): Felder ausgefuellt vs. leer
- Traceability: R<->G Links pruefen

**Freshness:**
- Stale _status.yml Erkennung (14 Tage Schwelle)
- .memory/blob_sync_state.json Alter
- ai-context-vault Scripts Syntax (nur lokal)

### 4. Ergebnis

- Automatisch GitHub Issue jeden Sonntag
- Labels: audit (blau), audit:errors (rot bei Fehlern)
- Lokal ausfuehrbar: `python scripts/weekly_audit.py`

## Technische Details

- Keine bestehenden Workflows werden geaendert
- Dependencies: Nur pyyaml + stdlib (nichts Neues)
- Permissions: contents:read + issues:write
- Zweiphasig: Checks → JSON → Issue posten

## Detaillierter Plan

Vollstaendiger Implementierungsplan liegt unter:
`~/.claude/plans/swift-gathering-cake.md`

---

## Zukunft: Inhaltspruefer-Agent (v2)

> Status: Idee / Spaeter umsetzen

### Was er kann (Konzept)

Ein LLM-gestuetzter Agent der prueft, ob die **Implementierung** (PoC-Code, Policy-as-Code)
tatsaechlich die **Anforderungen** der Thesis erfuellt:

- Liest fixe Referenzdokumente als Kontext:
  - `docs/positioning/USP_ANALYSE_EXPERTENBEWERTUNG.md` (USP & Positionierung)
  - `00_admin/gliederung_v3.md` (Methodik & Kapitelstruktur)
  - `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf` (Expose — nach Entschluesselung)
  - `04_anforderungsanalyse_RQ1/requirements/R*.yaml` (Anforderungskatalog)
  - `05_referenzarchitektur_RQ2/05_03_quality_gates/G*.yaml` (Gate-Definitionen)
- Prueft PoC-Code (`poc/`) gegen diese Anforderungen
- Beispiel-Check: "Implementiert `poc/opa-policies/` tatsaechlich Art. 9 Risikomanagement wie in R003 definiert?"
- Ergebnis: Requirements-Coverage-Report als GitHub Issue

### Voraussetzungen

- Methodik, Positioning, Expose und Anforderungen muessen inhaltlich fix sein
- PoC-Implementierung muss begonnen haben
- Benoetigt LLM-API (Claude) als Backend → Kosten pro Ausfuehrung
- Komplexer als v1 — eigenes Projekt
