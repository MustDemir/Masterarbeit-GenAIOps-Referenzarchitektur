# Evidence Store: Hybride Architektur (Blob Storage + SQL)

Stand: 2026-03-01
Kontext: PoC-Architektur fuer Ambient AI Scribe (Healthcare)

## Architektur-Entscheidung

Der Evidence Store folgt einem hybriden Ansatz:

| Komponente | Speicher | Inhalt |
|---|---|---|
| Unstrukturierte Artefakte | Azure Blob Storage (immutable) | Model Cards, Evaluierungsreports, verschluesselte Transkripte |
| Strukturierte Metadaten | Azure PostgreSQL (relationale DB) | Quality-Gate-Ergebnisse, Compliance-Metriken, Audit-Logs |

**Begruendung:** Blob Storage ist unstrukturiert — fuer performantes Compliance-Monitoring ueber Millionen von Gate-Durchlaeufen werden strukturierte, indizierte Metadaten benoetigt. Die relationale Datenbank ermoeglicht Echtzeit-Reporting fuer Auditoren.

## Healthcare-Kontext: Payload vs. Telemetrie

Im Ambient AI Scribe Szenario muessen medizinische Payload und regulatorische Telemetrie strikt getrennt werden:

- **Medizinische Payload** (Patienten-Transkripte): Verschluesselt im Azure Blob Storage. Auditoren duerfen diese niemals lesen.
- **Regulatorische Telemetrie** (Compliance-Metadaten): Strukturiert in der SQL-Datenbank. Auditoren pruefen ausschliesslich diese Daten.

Rechtsgrundlage: DSGVO Art. 9 (Verarbeitung besonderer Kategorien personenbezogener Daten)

## 4 SQL-Architektur-Bausteine

### 1. Immutable Evidence Store (DB-Trigger)

Regulatorische Nachweise muessen faelschungssicher (immutable) sein. Ein SQL-Trigger blockiert jegliche nachtraegliche Aenderung oder Loeschung von Audit-Logs.

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

**Kapitel-Zuordnung:** Kap. 5.5 (Evidence- und Audit-Logik, S4)

### 2. Data Privacy & Abstraktion (SQL Views)

Kein direkter Tabellenzugriff auf sensible Daten — weder fuer das RAG-System noch fuer das Compliance-Dashboard. SQL-Sichten (Views) maskieren PII-Daten per Design.

**Kapitel-Zuordnung:** Kap. 5.5 (Evidence Store), DP2 (Traceability)

### 3. Least Privilege Automation (DB-Rollen)

CI/CD-Pipelines (z.B. GitHub Actions), die Quality Gates ausfuehren, erhalten nur minimale Berechtigungen:

- CI/CD-Runner: Nur `INSERT` auf `quality_gate_results` (Schreiben von Evaluierungsergebnissen)
- Kein `UPDATE`, kein `DELETE` — in Kombination mit dem Immutability-Trigger doppelt abgesichert

**Kapitel-Zuordnung:** Kap. 5.4 (Pipeline-Integration, S3), DP5 (Cloud-native Integrierbarkeit)

### 4. Performance & Observability (Composite Indexes)

Zusammengesetzte Indizes fuer performantes Compliance-Reporting:

```sql
CREATE INDEX idx_gate_reporting ON quality_gate_results (modell_name, gate_typ);
```

Vermeidet Table Scans bei Millionen von Quality-Gate-Durchlaeufen.

**Kapitel-Zuordnung:** Kap. 5.5 (Evidence Store, S4)

## PoC-Schema (Referenz)

```sql
CREATE TABLE quality_gate_results (
    audit_id BIGSERIAL PRIMARY KEY,
    modell_name TEXT NOT NULL,
    gate_typ TEXT NOT NULL,        -- 'Strategisch', 'Technisch', 'Compliance'
    entscheidung TEXT NOT NULL,     -- 'PASS', 'FAIL'
    evidence_blob_url TEXT NOT NULL, -- Link zum Azure Blob (Payload)
    geprueft_am TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Zuordnung zu Expose-Gliederung

| Baustein | Kapitel | Design-Prinzip | Saeule |
|---|---|---|---|
| Immutability-Trigger | Kap. 5.5 | DP2 (Traceability) | S4 (Evidence/Audit) |
| Privacy-Views | Kap. 5.5 | DP1 (Compliance-Lifecycle) | S4 |
| Least-Privilege-Rollen | Kap. 5.4 | DP5 (Cloud-native) | S3 (Pipeline) |
| Composite Indexes | Kap. 5.5 | — | S4 |
| Payload/Telemetrie-Trennung | Kap. 5.5, Kap. 1.6 | DP4 (Governance-Trennung) | S4 |

## Verteidigungsargument (Kolloquium)

> Fuer den Ambient AI Scribe im medizinischen Umfeld (High-Risk KI) ist eine strikte Trennung zwischen medizinischer Payload und regulatorischer Telemetrie zwingend. Blob Storage ist unstrukturiert. Fuer ein effizientes Compliance-Monitoring ueber Millionen von Runs benoetigen wir strukturierte, indizierte Metadaten. Durch die relationale Datenbank mit Composite-Indizes gewaehrleisten wir performantes Reporting. Durch Sichten (Views) schuetzen wir die Patienten-Metadaten vor unbefugtem Zugriff. Und durch den Einsatz von Before-Triggern garantieren wir eine absolute Manipulationssicherheit (Immutability), die fuer forensische Beweise nach dem EU AI Act zwingend erforderlich ist.
