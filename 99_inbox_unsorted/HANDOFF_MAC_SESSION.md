# Handoff: Offene Tasks für Mac-Session (Claude Code CLI)

> Stand: 2026-03-08 | Erstellt von: Cowork-Session
> Kontext: SSOT-Literatur-Workflow Stabilisierung vor Kap2-Start

---

## Was wurde bereits erledigt (Cowork + vorherige Sessions)

1. **Classification Accuracy**: 7/7 Cluster, 7/7 Farbe (4 Iterationen)
2. **Keywords enriched**: +169 Keywords über 15 Cluster (alle Kapitel)
3. **Manual Overrides**: 14 Einträge (Vaswani, Bommasani, Huang, Lewis, Wei + 9 ältere)
4. **Relevanz-Thresholds**: ROT≥2.8, ORANGE≥2.1, GELB≥1.5 (vorher zu hoch)
5. **Cluster-Bonus**: 02_01-02_06 (+0.4) und 04_04-05_05 (+0.3) hinzugefügt
6. **Dry Run**: mapping_total=142 copied_views=316 decisions=7 — fehlerfrei
7. **Keyword-Audit**: Alle 15+ Cluster auf Gliederungs-Konsistenz geprüft

## Offene Tasks (benötigen Mac-Zugriff)

### Task 1: Regressionstest (Priorität: HOCH)
```bash
cd ~/.codex/skills/literatur-ssot-workflow
python3 scripts/classtest2b.py
```
Erwartetes Ergebnis: Cluster 7/7, Farbe 7/7 (wie Test #4)
Falls Regression: Score-Analyse in classtest2b.py ist eingebaut.

### Task 2: Outdated Markdown-Dateien aktualisieren (Priorität: MITTEL)
Dateien auf OneDrive unter `2. Literatur/SSOT_GLIEDERUNG_CLUSTER/`:
- `00_entscheidungsbericht.md` — referenziert "126 entries", soll "140 active" sein
- `00_taglogik.md` — gleiche veraltete Zahl
- `00_CLUSTER_LOGIK.md` — gleiche veraltete Zahl

### Task 3: Desktop-Script löschen (Priorität: NIEDRIG)
```bash
rm ~/Desktop/update_csv_new_sources.py
```
Dieses Script ist obsolet — Funktionalität ist in process_literatur_ssot_inbox.py integriert.

### Task 4: SSOT-Cluster-Bereinigung laut BEWERTUNG (Priorität: MITTEL)
Laut `02_rigor_theorie_stand_forschung/BEWERTUNG_CLUSTER_KAP2.md`:
- 8 Cluster-Fehlzuordnungen (Umzüge nötig)
- 30 Farb-Korrekturen
- 02_01 de facto leer (6 Primärquellen fehlen im Cluster)

## Dateipfade (Mac)

| Datei | Pfad |
|-------|------|
| Config | `~/.codex/skills/literatur-ssot-workflow/config/ssot_workflow.json` |
| Script | `~/.codex/skills/literatur-ssot-workflow/scripts/process_literatur_ssot_inbox.py` |
| Testscript | `~/.codex/skills/literatur-ssot-workflow/scripts/classtest2b.py` |
| CSV | OneDrive `2. Literatur/00_ssot_mapping.csv` |
| Inbox | OneDrive `2. Literatur/Inbox/Meine Bibliothek/files/` |
| Bewertung | Thesis-Repo `02_rigor_theorie_stand_forschung/BEWERTUNG_CLUSTER_KAP2.md` |
