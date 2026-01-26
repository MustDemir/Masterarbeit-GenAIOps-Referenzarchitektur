# Masterarbeit-Cloud-MLOps
Sepsis Early Warning System - MLOps Platform auf Azure Cloud

# Create comprehensive README.md
readme_content = """# 🏥 Sepsis Early Warning System - MLOps Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/Azure-Cloud-0078D4.svg)](https://azure.microsoft.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Masterarbeit**: Cloud-basierte prädiktive Analytik für Sepsis-Früherkennung  
> **Autor**: Mustafa  
> **Zeitraum**: Januar 2026 - Mai 2026  
> **Technologie-Stack**: Python, Azure, Kubernetes, FastAPI, Docker

---

## 📋 Projektübersicht

Dieses Projekt entwickelt eine **produktionsreife MLOps-Plattform** zur Früherkennung von Sepsis in Krankenhäusern. Die Lösung kombiniert maschinelles Lernen mit moderner Cloud-Architektur, um medizinischem Personal zeitnahe Risikovorhersagen bereitzustellen.

### 🎯 Projektziele

1. **Medizinischer Impact**: Sepsis-Risiko 6-12 Stunden vor klinischen Symptomen vorhersagen
2. **Technische Exzellenz**: Skalierbare, sichere und wartbare Cloud-Architektur
3. **Akademischer Beitrag**: Evaluation von MLOps-Praktiken im Healthcare-Kontext

### 🔬 Forschungsfragen

- Wie kann eine Cloud-native Architektur die Latenz und Skalierbarkeit von ML-Modellen in der Medizin verbessern?
- Welche MLOps-Praktiken sind für regulierte Healthcare-Umgebungen (DSGVO, MDR) geeignet?
- Wie lässt sich kontinuierliches Model-Retraining ohne Downtime implementieren?

---

## 🏗️ Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                     Azure Cloud Platform                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐      ┌──────────────┐      ┌───────────┐ │
│  │   FastAPI    │─────▶│  ML Model    │─────▶│  Azure    │ │
│  │   Container  │      │  (Scikit)    │      │  SQL DB   │ │
│  └──────────────┘      └──────────────┘      └───────────┘ │
│         │                      │                     │       │
│         ▼                      ▼                     ▼       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Azure Kubernetes Service (AKS)              │  │
│  │  - Auto-Scaling  - Load Balancing  - Health Checks  │  │
│  └──────────────────────────────────────────────────────┘  │
│                              │                              │
│                              ▼                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Monitoring & Logging                    │  │
│  │  - Azure Monitor  - Application Insights  - Grafana │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### 🛠️ Technologie-Stack

| Kategorie | Technologie | Zweck |
|-----------|-------------|-------|
| **ML Framework** | Scikit-Learn, Pandas, NumPy | Modelltraining & Feature Engineering |
| **API** | FastAPI, Uvicorn | REST-Endpunkte für Inferenz |
| **Datenbank** | Azure SQL Database | Patientendaten & Predictions |
| **Container** | Docker, Azure Container Registry | Containerisierung |
| **Orchestration** | Azure Kubernetes Service (AKS) | Container-Management |
| **IaC** | Bicep, Terraform | Infrastructure as Code |
| **CI/CD** | GitHub Actions | Automatisierte Deployments |
| **Monitoring** | Azure Monitor, Prometheus, Grafana | Observability |
| **Security** | Azure Key Vault, RBAC | Secrets & Access Management |

---

## 📁 Projektstruktur

```
sepsis-mlops-platform/
│
├── 📂 data/                          # Datensätze
│   ├── raw/                          # Rohdaten (MIMIC-III, Kaggle)
│   ├── processed/                    # Bereinigte Daten
│   └── synthetic/                    # Synthetische Testdaten
│
├── 📂 notebooks/                     # Jupyter Notebooks
│   ├── 01_exploratory_data_analysis/ # EDA & Visualisierungen
│   ├── 02_feature_engineering/       # Feature-Entwicklung
│   └── 03_model_training/            # Modell-Experimente
│
├── 📂 src/                           # Produktionscode
│   ├── data_processing/              # ETL-Pipeline
│   ├── model/                        # ML-Modell (Training & Inferenz)
│   ├── api/                          # FastAPI-Anwendung
│   └── utils/                        # Helper-Funktionen
│
├── 📂 infrastructure/                # Cloud-Infrastruktur
│   ├── bicep/                        # Azure Bicep Templates
│   ├── terraform/                    # Terraform Configs
│   └── kubernetes/                   # K8s Manifests (Deployments, Services)
│
├── 📂 docker/                        # Docker-Konfigurationen
│   ├── Dockerfile.api                # API-Container
│   ├── Dockerfile.training           # Training-Container
│   └── docker-compose.yml            # Lokale Entwicklung
│
├── 📂 .github/workflows/             # CI/CD Pipelines
│   ├── ci.yml                        # Tests & Linting
│   ├── cd-staging.yml                # Staging-Deployment
│   └── cd-production.yml             # Production-Deployment
│
├── 📂 tests/                         # Automatisierte Tests
│   ├── unit/                         # Unit-Tests
│   └── integration/                  # Integrationstests
│
├── 📂 docs/                          # Dokumentation
│   ├── thesis/                       # Masterarbeit (LaTeX)
│   ├── architecture/                 # Architektur-Diagramme
│   └── api/                          # API-Dokumentation
│
├── 📂 config/                        # Konfigurationsdateien
│   ├── model_config.yaml             # Hyperparameter
│   └── deployment_config.yaml        # Deployment-Settings
│
├── 📄 README.md                      # Diese Datei
├── 📄 requirements.txt               # Python-Dependencies
├── 📄 .gitignore                     # Git-Ignore-Regeln
└── 📄 LICENSE                        # MIT-Lizenz

```

---

## 🚀 Quick Start

### 1️⃣ Repository klonen

```bash
git clone https://github.com/mustafa/sepsis-mlops-platform.git
cd sepsis-mlops-platform
```

### 2️⃣ Virtuelle Umgebung erstellen

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### 3️⃣ Daten herunterladen

```bash
# Option A: Kaggle Sepsis Dataset
kaggle datasets download -d salikhussaini49/prediction-of-sepsis

# Option B: MIMIC-III (Zugang erforderlich)
# https://physionet.org/content/mimiciii/1.4/
```

### 4️⃣ Explorative Datenanalyse

```bash
jupyter notebook notebooks/01_exploratory_data_analysis/eda.ipynb
```

### 5️⃣ Modell trainieren

```bash
python src/model/train.py --config config/model_config.yaml
```

### 6️⃣ API lokal starten

```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

**API-Dokumentation**: http://localhost:8000/docs

---

## 📊 Datensatz

### Datenquellen

1. **MIMIC-III Clinical Database** (primär)
   - 40.000+ ICU-Aufenthalte
   - Vitaldaten, Laborwerte, Medikation
   - Zugang: https://physionet.org/

2. **Kaggle Sepsis Prediction Dataset** (sekundär)
   - 40.336 synthetische Patientenverläufe
   - 40 Features (Herzfrequenz, Temperatur, etc.)
   - Download: https://www.kaggle.com/datasets/salikhussaini49/prediction-of-sepsis

### Features (Beispiele)

| Feature | Beschreibung | Einheit |
|---------|--------------|---------|
| `HR` | Herzfrequenz | bpm |
| `Temp` | Körpertemperatur | °C |
| `MAP` | Mittlerer arterieller Druck | mmHg |
| `WBC` | Weiße Blutkörperchen | cells/µL |
| `Lactate` | Laktat-Wert | mmol/L |
| `SepsisLabel` | Sepsis-Diagnose | 0/1 (binär) |

---

## 🧪 Machine Learning Pipeline

### 1. Data Preprocessing

```python
# src/data_processing/preprocess.py
- Fehlende Werte imputation (KNN, MICE)
- Outlier-Behandlung (IQR-Methode)
- Feature-Skalierung (StandardScaler)
- Zeitreihen-Aggregation (Rolling Windows)
```

### 2. Feature Engineering

```python
# notebooks/02_feature_engineering/
- SOFA-Score Berechnung
- Zeitliche Trends (Delta-Features)
- Interaktions-Features (MAP × HR)
- Lag-Features (t-1, t-2, t-3)
```

### 3. Model Training

```python
# src/model/train.py
Algorithmen:
✅ Random Forest (Baseline)
✅ XGBoost (Hauptmodell)
✅ LightGBM (Geschwindigkeits-Optimierung)

Evaluation:
- AUROC (Area Under ROC Curve)
- Precision/Recall (Fokus auf Recall)
- F2-Score (gewichtet zugunsten Recall)
```

### 4. Model Deployment

```python
# src/api/main.py
FastAPI-Endpunkte:
- POST /predict: Einzelvorhersage
- POST /predict/batch: Batch-Vorhersagen
- GET /health: Health-Check
- GET /metrics: Prometheus-Metriken
```

---

## ☁️ Cloud-Deployment

### Azure-Ressourcen (via Bicep)

```bash
# infrastructure/bicep/main.bicep
az deployment group create \\
  --resource-group rg-sepsis-mlops \\
  --template-file infrastructure/bicep/main.bicep \\
  --parameters environment=production
```

**Erstellte Ressourcen:**
- Azure Kubernetes Service (AKS)
- Azure SQL Database
- Azure Container Registry (ACR)
- Azure Key Vault
- Virtual Network (VNET)
- Application Insights

### Kubernetes-Deployment

```bash
# infrastructure/kubernetes/
kubectl apply -f infrastructure/kubernetes/namespace.yaml
kubectl apply -f infrastructure/kubernetes/deployment.yaml
kubectl apply -f infrastructure/kubernetes/service.yaml
kubectl apply -f infrastructure/kubernetes/ingress.yaml
```

---

## 🔒 Security & Compliance

### DSGVO-Konformität

- ✅ Pseudonymisierung von Patientendaten
- ✅ Verschlüsselung at-rest (Azure SQL TDE)
- ✅ Verschlüsselung in-transit (TLS 1.3)
- ✅ Zugriffskontrolle (Azure RBAC)
- ✅ Audit-Logging (Azure Monitor)

### Secrets Management

```bash
# Secrets in Azure Key Vault
az keyvault secret set \\
  --vault-name kv-sepsis-mlops \\
  --name sql-connection-string \\
  --value "Server=tcp:..."
```

---

## 📈 Monitoring & Observability

### Metriken

```yaml
# Prometheus-Metriken
- prediction_latency_seconds (Histogram)
- prediction_total (Counter)
- model_accuracy (Gauge)
- api_requests_total (Counter)
```

### Dashboards

- **Grafana**: http://grafana.sepsis-mlops.com
- **Azure Monitor**: Logs, Metrics, Alerts
- **Application Insights**: Performance Profiler

---

## 🧪 Testing

### Unit-Tests

```bash
pytest tests/unit/ --cov=src --cov-report=html
```

### Integrationstests

```bash
pytest tests/integration/ --env=staging
```

### Load-Tests

```bash
locust -f tests/load/locustfile.py --host=https://api.sepsis-mlops.com
```

---

## 📚 Dokumentation

### Thesis-Kapitel (LaTeX)

```
docs/thesis/
├── 01_einleitung.tex
├── 02_grundlagen.tex
├── 03_methodik.tex
├── 04_implementierung.tex
├── 05_evaluation.tex
└── 06_fazit.tex
```

### API-Dokumentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🛣️ Roadmap

### Phase 1: Fundament (Woche 1-4) ✅
- [x] Projektstruktur erstellen
- [x] Daten explorieren
- [ ] Baseline-Modell trainieren

### Phase 2: Cloud-Infrastruktur (Woche 5-9)
- [ ] Azure-Ressourcen provisionieren
- [ ] Docker-Container erstellen
- [ ] AKS-Deployment

### Phase 3: MLOps-Pipeline (Woche 10-13)
- [ ] CI/CD mit GitHub Actions
- [ ] Monitoring-Setup
- [ ] Automated Retraining

### Phase 4: Finalisierung (Woche 14-16)
- [ ] Performance-Optimierung
- [ ] Thesis schreiben
- [ ] Präsentation vorbereiten

---

## 🤝 Kontakt

**Mustafa**  
📧 Email: mustafa@example.com  
💼 LinkedIn: [linkedin.com/in/mustafa](https://linkedin.com/in/mustafa)  
🐙 GitHub: [github.com/mustafa](https://github.com/mustafa)

---

## 📄 Lizenz

Dieses Projekt ist unter der **MIT-Lizenz** lizenziert. Siehe [LICENSE](LICENSE) für Details.

---

## 🙏 Danksagungen

- **velpTEC GmbH** für die Cloud-Architektur-Schulung
- **MIMIC-III Team** für den Datensatz
- **Azure Community** für Best Practices

---

## 📊 Projekt-Status

![Progress](https://progress-bar.dev/5/?title=Gesamtfortschritt&width=400)

**Letzte Aktualisierung**: 26. Januar 2026

---

**⭐ Wenn dir dieses Projekt gefällt, gib ihm einen Star auf GitHub!**
"""

# Write README.md
readme_path = os.path.join(base_path, "README.md")
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✅ README.md erstellt!")
print(f"📄 Datei: {readme_path}")
print(f"📏 Länge: {len(readme_content)} Zeichen")
print(f"📝 Zeilen: {len(readme_content.splitlines())} Zeilen")

