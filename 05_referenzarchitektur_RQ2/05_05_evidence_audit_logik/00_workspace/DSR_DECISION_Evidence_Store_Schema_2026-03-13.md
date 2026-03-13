# DSR-Entscheidung: Evidence Store PostgreSQL Schema als Artefakt

**Entscheidungsdatum:** 2026-03-13  
**Kapitel:** 5.5 (Evidence und Audit Logik, S4)  
**Status:** ✅ **APPROVED**

---

## 📋 Entscheidung

**Evidence Store PostgreSQL DDL-Schema wird als DSR-Artefakt in Kap. 5.5 spezifiziert.**

### Artefakt-Definition

Der Evidence Store besteht aus folgenden technischen Komponenten, die als Design Science Artifact formalisiert werden:

#### **1. Immutability-Trigger (SQL Funktion + Trigger)**
```sql
-- Trigger fuer Unveraenderlichkeit (Immutability / EU AI Act Beweispflicht)
CREATE OR REPLACE FUNCTION trg_prevent_delete_update()
RETURNS trigger LANGUAGE plpgsql AS $
BEGIN
    RAISE EXCEPTION 'EU AI Act Compliance: Modification or deletion of audit logs is strictly prohibited!';
END;
$;

CREATE TRIGGER make_evidence_immutable
BEFORE UPDATE OR DELETE ON quality_gate_results
FOR EACH ROW EXECUTE FUNCTION trg_prevent_delete_update();
```

**Design-Prinzip:** DP2 (Traceability) + DP5.3 (Immutability Sub-Extension)  
**Säule:** S4 (Evidence/Audit)  
**Evaluations-Kriterium:** Faelschungssicherheit durch SQL-Trigger-Enforcement (absolute Unveraenderlichkeit)

#### **2. Privacy-Views (SQL View für Datenschutz)**

Design-Prinzip für Daten-Abstraktion:
- Kein direkter Tabellenzugriff auf sensible Daten (weder RAG-System noch Compliance-Dashboard)
- SQL Views maskieren PII-Daten per Design

**Design-Prinzip:** DP1 (Compliance-Lifecycle) + DP4 (Governance-Trennung)  
**Säule:** S4 (Evidence/Audit)  
**Evaluations-Kriterium:** Privacy-by-Design durch View-Abstraktion

#### **3. Least-Privilege RBAC (Database Roles)**

Design für CI/CD-Pipelines (z.B. GitHub Actions):
- **CI/CD-Runner:** Nur `INSERT` auf `quality_gate_results`
- **NO UPDATE/DELETE:** In Kombination mit Immutability-Trigger doppelt abgesichert

**Design-Prinzip:** DP5 (Cloud-native Integrierbarkeit)  
**Säule:** S3 (Pipeline-Integration) + S4 (Evidence/Audit)  
**Evaluations-Kriterium:** Principle of Least Privilege enforcement durch DB-Rollen

#### **4. Composite Indexes (Performance + Compliance Reporting)**

```sql
CREATE INDEX idx_gate_reporting ON quality_gate_results (modell_name, gate_typ);
```

**Rationale:** Vermeidet Table Scans bei Millionen von Quality-Gate-Durchläufen  
**Design-Prinzip:** Operationalisierung für DP5.2 (Hash-Chain Performance)  
**Säule:** S4 (Evidence/Audit)  
**Evaluations-Kriterium:** Query-Performance für Audit-Reports < 100ms (SLO)

#### **5. PoC-Schema: quality_gate_results Table**

```sql
CREATE TABLE quality_gate_results (
    audit_id BIGSERIAL PRIMARY KEY,
    modell_name TEXT NOT NULL,
    gate_typ TEXT NOT NULL,        -- 'Strategisch', 'Technisch', 'Compliance'
    entscheidung TEXT NOT NULL,    -- 'PASS', 'FAIL'
    evidence_blob_url TEXT NOT NULL, -- Link zu Azure Blob (Medical Payload)
    geprueft_am TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Semantik:**
- `audit_id`: Eindeutige, unveraenderliche Evidence-Referenz
- `gate_typ`: Klassifikation nach D_GATE_INCLUSION_RULE v3.0
- `evidence_blob_url`: Referenz zu Blob Storage (encrypted medical payload)
- `geprueft_am`: Immutable Timestamp für Forensics

---

## 🎯 **Mapping zu Design-Prinzipien (DP)**

| DSR-Komponente | Design-Prinzip | Säule | Evidenz-Kriterium |
|---|---|---|---|
| Immutability-Trigger | DP2 (Traceability) | S4 | Forensic-Sicherheit, EU AI Act Beweispflicht |
| Privacy Views | DP1 (Compliance-Lifecycle), DP4 (Governance) | S4 | PII-Schutz, DSGVO Art. 9 Compliance |
| Least-Privilege RBAC | DP5 (Cloud-native) | S3, S4 | Automatisierte Zugriffskontrolle |
| Composite Indexes | DP5.2 (Hash-Chain Performance) | S4 | Query-Performance SLO < 100ms |
| quality_gate_results Table | DP2 (Traceability), DP1 (Compliance) | S4 | Centralized Audit Log, Conformity Bundle |

---

## 📍 **Zuordnung im Thesis-Text (Kapitel 5.5)**

### Absatz-Level Mapping

| Absatz | Titel | DSR-Komponenten | Quellen |
|---|---|---|---|
| **Abs. 2** | Compliance-Lifecycle & Governance | Privacy Views | Pistilli et al. 2023 |
| **Abs. 3** | CAC-Differenzierung (Evidence Backbone) | Immutability-Trigger, quality_gate_results | Kholkar & Ahuja 2025, Butt et al. 2026 |
| **Abs. 4** | Decision Logs & Audit Trails | Composite Indexes, RBAC | Kholkar & Ahuja 2025, Burns et al. (Dynamo) |
| **Abs. 5** | Hash-Chain & Forensic Integrity | Immutability-Trigger (DP5.3) | PoC-Architektur aus evidence_store_architektur.md |
| **Abs. 6** | Payload/Telemetrie-Trennung (R3) | Privacy Views, Blob Storage Design | Kap. 5.5 Technical Deep Dive |

---

## ✅ **Validierung gegen SRH Uni-Anforderungen**

- **50/30/20 Regel:** DSR-Artefakte = konkreter Technical Design (20% Design Artifacts)
- **Relevanz:** Direkt zu RQ2 (Referenzarchitektur) und DP-Operationalisierung
- **Neuheit:** Evidence Store Schema mit Immutability-Enforcement ist PoC-Level Innovation
- **Evaluierbarkeit:** Trigger-Funktionalität, View-Privacy, RBAC-Enforcement sind testbar

---

## 🔄 **Nächste Schritte**

1. ✅ DSR-Entscheidung dokumentiert (dieses Dokument)
2. 🔄 Preflight-Protokoll für Kap. 5.5 aktualisieren (mit DSR-Artefakt-Spezifikation)
3. 🔄 5-Seiten-Budget Assessment durchführen (Scope vs. Page Limit)
4. 🔄 FINAL-Schreiben triggern (Abs. 1–6)

---

## 📝 **Entscheidungs-Rationale**

Die Spezifikation des PostgreSQL Evidence Store als DSR-Artefakt ist gerechtfertigt, weil:

1. **Rigor:** DDL ist formale, testbare Spezifikation (kein pseudo-code)
2. **Design:** Integriert alle 5 DP-Prinzipien (Compliance, Traceability, Governance, Cloud-Native)
3. **Relevance:** Direkt zu RQ2 (Architektur) und DP-Operationalisierung
4. **Evaluierbarkeit:** Trigger, Views, RBAC, Indexes sind im PoC implementierbar und prüfbar

---

**Gültig ab:** 2026-03-13  
**Dokumenter:** Mustafa Demir  
**Status:** APPROVED ✅
