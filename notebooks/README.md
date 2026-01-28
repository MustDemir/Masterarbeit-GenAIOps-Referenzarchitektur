# 📓 Notebooks Übersicht

Dieser Ordner enthält alle Jupyter Notebooks des Projekts, strukturiert nach Verwendungszweck.

## 📁 Struktur

### 🎓 `learning/`
**Zweck**: Grundlagen, Tutorials und Lern-Experimente

Notebooks in diesem Ordner dienen dem Lernen und Verstehen von:
- Python-Grundlagen und Data Science Libraries
- Machine Learning Konzepte
- Cloud-Services und APIs
- MLOps Best Practices

**Beispiele**:
- `01_python_basics.ipynb` - Python-Grundlagen und Syntax
- Weitere Lern-Notebooks folgen...

---

### 🔬 `experiments/`
**Zweck**: Model-Experimente und Feature Engineering

Hier werden verschiedene ML-Ansätze getestet:
- Feature Engineering
- Model Selection & Tuning
- Hyperparameter Optimization
- A/B Testing von Algorithmen

---

### 📊 `analysis/`
**Zweck**: Datenanalyse und explorative Statistik

Notebooks für:
- Explorative Datenanalyse (EDA)
- Statistische Tests
- Visualisierungen
- Reporting und Insights

---

### 📝 `Masterarbeit_Jupyter.ipynb`
**Hauptnotebook der Masterarbeit**

Das zentrale Notebook mit dem vollständigen Workflow:
1. Datenvorverarbeitung
2. Model Training
3. Evaluation
4. Deployment-Vorbereitung

---

## 🔄 Workflow

```
learning/ → experiments/ → analysis/ → Masterarbeit_Jupyter.ipynb
   ↓            ↓             ↓              ↓
Lernen    Testen/Validieren  Analysieren  Produktion
```

### Best Practices

✅ **Lern-Notebooks** (`learning/`):
- Können unstrukturiert sein
- Outputs dürfen committed werden (zum Nachvollziehen)
- Experimente und "Trial & Error" erlaubt

✅ **Experiment-Notebooks** (`experiments/`):
- Strukturiert mit klaren Sections
- Outputs werden durch `.gitattributes` entfernt (nbstripout)
- Versioniert, um Experimente nachzuvollziehen

✅ **Analyse-Notebooks** (`analysis/`):
- Reproduzierbar und dokumentiert
- Klare Markdown-Beschreibungen
- Visualisierungen als separate Dateien exportieren

✅ **Hauptnotebook** (`Masterarbeit_Jupyter.ipynb`):
- Production-ready Code
- Vollständig dokumentiert
- Kann in Python-Module überführt werden

---

## 🚀 Getting Started

### Notebook starten:

```bash
# Aktiviere virtuelle Umgebung
source venv/bin/activate  # macOS/Linux
# oder
.\venv\Scripts\activate   # Windows

# Starte Jupyter Lab
jupyter lab
```

### Neue Lern-Notebooks erstellen:

```bash
# Navigiere in den learning-Ordner
cd notebooks/learning/

# Erstelle ein neues Notebook
jupyter notebook 02_pandas_basics.ipynb
```

---

## 📚 Referenzen

- [Jupyter Best Practices](https://jupyter-notebook.readthedocs.io/)
- [nbstripout Documentation](https://github.com/kynan/nbstripout)
- [Azure ML Notebooks](https://learn.microsoft.com/azure/machine-learning/)
