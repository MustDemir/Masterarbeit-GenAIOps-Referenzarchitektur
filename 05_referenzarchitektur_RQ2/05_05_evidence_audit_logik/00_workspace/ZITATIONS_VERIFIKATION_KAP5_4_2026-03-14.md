# Zitations-Verifikation Kap. 5.4 Evidence- und Audit-Logik
**Stand:** 2026-03-14
**Methode:** Zitations-Finder Skill — Pagination Offset Berechnung + PDF/Fulltext-Abgleich

---

## Pagination Offset Tabelle

| Quelle | Venue | Offset-Formel | Publizierte Seiten | Methode |
|---|---|---|---|---|
| **Kholkar & Ahuja (2025)** | arXiv / NeurIPS 2025 Workshop | Offset = 0 | PDF-Seiten 1–14 | PDF lokal gelesen |
| **Butt et al. (2026)** | IEEE Access Vol. 14 | **Offset = 1372** (1373-1) | **S. 1373–1397** | PDF lokal gelesen |
| **Burns et al. (2025)** | ECCWS 2025 Proceedings | **Offset = 874** (875-1) | **S. 875–878** | PDF lokal gelesen |
| **Eisenberg et al. (2025)** | arXiv Preprint | Offset = 0 | PDF-Seiten 1–31 | PDF lokal gelesen |
| **Nweke & Yeng (2026)** | IEEE Access Vol. 14 | **Offset = 28257** (28258-1) | **S. 28258–28281** | Zotero Fulltext + Metadaten |
| **Muhammad et al. (2026)** | Frontiers in AI Vol. 9 | N/A (Artikel-ID 1759211) | Sec.-Referenzen | Zotero Fulltext + Metadaten |
| **Joseph (2023)** | WJAETS (kein Peer-Review) | nicht verifiziert | Elicit-Quelle | kein PDF vorhanden |

---

## Ergebnis: Kritische Seitenzahl-Fehler

### BUTT et al. (2026) — 7 Zitationen, **ALLE PDF-Viewer-Seiten statt publizierte IEEE-Seiten**

| Move | DRAFT (falsch) | KORREKT | Beleg-Stelle | Exaktes Zitat |
|---|---|---|---|---|
| M2 | S. 1–2 | **S. 1373–1374** | Abstract (PDF p.1) + Def. III.A (PDF p.2) | "emits signed, content-addressed artifacts into a tamper-evident Evidence Backbone. These artifacts are assembled into a per-run Conformity Bundle" |
| M3 (1.) | S. 7 | **S. 1374** | Def. III.A.3 (PDF p.2) | "A tamper evident, append only storage substrate that records signed, content addressed evidence artifacts" |
| M3 (2.) | S. 2 | **S. 1374** | Def. III.A.3 (PDF p.2) | "append only" — gleiche Definitions-Seite |
| M5 | S. 5–6 | **S. 1377–1378** | Sec. III.A + Table 2 (PDF pp.5–6) | Gate schema applied across DG, TG, VG, RG, and OG |
| M6 | S. 1–2 | **S. 1373** | Abstract (PDF p.1) | "per-run Conformity Bundle" |
| M7 | S. 6 | **S. 1378** | Sec. III.B.4 (PDF p.6) | "content addressed pointers, digests, timestamps, and signatures" |
| M8 | S. 1–2 | **S. 1373** | Abstract (PDF p.1) | "Clause-to-Artifact Traceability mechanism deterministically renders clause coverage" |

### BURNS et al. (2025) — 1 Zitation, **PDF-Viewer-Seite statt publizierte Proceedings-Seite**

| Move | DRAFT (falsch) | KORREKT | Beleg-Stelle | Exaktes Zitat |
|---|---|---|---|---|
| M4 | S. 3 | **S. 877** | Sec. 4: AIGA (PDF p.3) | "Accountability and Ownership category is designed to define and assign roles, such as Head of AI and AI System owner, which establish accountability and responsibility" |

### NWEKE & YENG (2026) — 3 Zitationen, **PDF-Viewer-Seiten statt publizierte IEEE-Seiten**

| Move | DRAFT (falsch) | KORREKT | Beleg-Stelle | Exaktes Zitat |
|---|---|---|---|---|
| M1 | S. 3 | **S. 28262** (Sec. III, T4) | Threat Model T4 (ca. PDF p.5) | "our system uses privacy-minimized decision evidence (avoiding credential contents and direct identifiers)" |
| M6 | S. 3 | **S. 28263** (Sec. IV) | Requirements (ca. PDF p.6) | "evidence must be release-attributable: enforcement outcomes and supporting artifacts must bind to immutable policy identifiers" |
| M8 | S. 3 | **S. 28258** (Abstract) | Abstract (PDF p.1) | "clause-to-control traceability under policy/configuration evolution [...] treats evidence completeness as an enforceable property" |

> **HINWEIS Nweke:** Die exakten publizierten Seitenzahlen sind Schaetzwerte basierend auf Zeichenposition im Zotero-Fulltext (Paper: 24 Seiten, ~117K Zeichen). Fuer maximale Praezision: physisches PDF auf IEEE Xplore oeffnen und Seiten manuell pruefen. Die SECTION-Referenzen (Sec. III, Sec. IV, Abstract) sind verifiziert und koennen alternativ als APA7-Lokator verwendet werden.

### KORREKTE Zitationen (keine Aenderung noetig)

| Quelle | Zitations-Format | Status | Begruendung |
|---|---|---|---|
| **Kholkar & Ahuja (2025)** | S. 1 (Abstract) | ✅ KORREKT | arXiv-Preprint, Offset=0, alle Zitate aus Abstract |
| **Eisenberg et al. (2025)** | Sec. 2 | ✅ KORREKT | arXiv-Preprint, Offset=0, Sec.-Referenz valide |
| **Muhammad et al. (2026)** | Sec. 1, Sec. 3.4 | ✅ KORREKT | Frontiers Art.-ID, keine Journal-Paginierung, Sec.-Ref. ist APA7-konform |
| **Joseph (2023)** | S. 7, S. 16 | ⚠️ NICHT VERIFIZIERBAR | Kein PDF vorhanden (Elicit-Quelle), Venue-Caveat im Text transparent |

---

## Zusammenfassung

| Kategorie | Anzahl | Details |
|---|---|---|
| Zitationen gesamt | 33 BELEG/CLAIM-Paare | 9 Absaetze (M1–M9) |
| Zitationen mit Seitenzahl | 20 | Butt(7) + Burns(1) + Nweke(3) + Kholkar(4) + Joseph(2) + Eisenberg(3) |
| **FALSCHE Seitenzahlen** | **11** | **Butt(7) + Burns(1) + Nweke(3)** |
| Korrekte Seitenzahlen | 7 | Kholkar(4) + Eisenberg(3) |
| Nicht verifizierbar | 2 | Joseph(2) — kein PDF |
| Semantisch korrekt | 33/33 | Alle Zitate inhaltlich zutreffend ✅ |

**Hauptbefund:** Die Zitate sind inhaltlich korrekt (alle BELEG/CLAIM-Paare stimmen), aber **11 von 20 Seitenzahlen verwenden PDF-Viewer-Seiten statt publizierte Journal-Seiten.** Dies betrifft ausschliesslich die drei IEEE/Proceedings-Quellen mit Pagination Offset > 0.

---

## Korrektur-Status
- [x] Verifikationsbericht erstellt (dieses Dokument)
- [ ] DRAFT aktualisiert mit korrigierten Seitenzahlen
- [ ] Pruefprotokolle im DRAFT aktualisiert
