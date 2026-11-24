# Cross-Collector Adversarial Robustness in ML-Based BGP Anomaly Detection

Adversarial robustness study of machine-learning-based BGP anomaly detectors built on the SFU/IEEE DataPort dataset (Trajkovic et al.).

## Research Questions

- **RQ1.** Can a protocol-realizable BGP UPDATE injection create a trigger learned by minute-level, feature-based BGP anomaly detectors?
- **RQ2.** Does a backdoor learned on one collector remain effective on another?
- **RQ3.** Which trigger properties explain cross-collector transfer success/failure?
- **RQ4.** Which defenses reduce backdoor success while preserving clean detection, and do they generalize?

## Project Structure

```
bgp-adversarial-robustness/
├── detectors/       # Reimplemented detectors from 13 SFU papers
│   ├── naive_bayes.py, decision_tree.py, svm.py
│   ├── random_forest.py, xgboost_det.py
│   ├── hmm.py, elm.py
│   ├── lstm.py, gru.py, bls.py
│   └── base.py      # Common detector interface
├── collectors/      # BGP data collection and feature extraction
│   ├── mrt_parser.py, feature_extractor.py
│   ├── routeviews.py, ripe_ris.py
│   └── downloader.py
├── dataset/         # Data loading, preprocessing, splitting
│   ├── loader.py, preprocess.py, splitter.py
│   ├── label_analysis.py, stats.py
│   └── raw/         # CSV files (not committed — see .gitignore)
├── attackers/       # Adversarial attacks
│   ├── backdoor.py, poisoning.py, evasion.py
│   ├── trigger.py, feasibility.py
│   ├── bgp_generator.py, transfer.py
│   └── __init__.py
├── defense/         # Defense mechanisms
│   ├── feature_selection.py, robust_training.py
│   ├── adversarial_training.py, two_collector.py
│   ├── backdoor_cleaning.py, generalization.py
│   └── __init__.py
├── util/            # Shared utilities
│   ├── metrics.py, config.py, logger.py
│   ├── reproducibility.py, visualization.py
│   └── __init__.py
├── requirements.txt # All Python dependencies (annotated by paper)
├── verify_env.py    # Check all packages are installed
├── .gitignore
└── README.md
```

## Setup

```bash
# 1. Clone
git clone https://github.com/<your-username>/bgp-adversarial-robustness.git
cd bgp-adversarial-robustness

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify installation
python verify_env.py
```

## Dataset

Download from [IEEE DataPort](https://ieee-dataport.org/open-access/bgp-features-anomaly-detection):
- `Slammer.csv` — 869 anomaly minutes (Jan 2003)
- `WannaCrypt.csv` — 5,760 anomaly minutes (May 2017)
- `Moscow_blackout.csv` — 130 anomaly minutes (May 2005)

Place in `dataset/raw/`.

## Key Dependencies (by paper source)

| Package | Source Papers | Purpose |
|---------|--------------|---------|
| scikit-learn | SFU [1]-[7] | NB, DT, SVM, RF detectors |
| PyTorch | SFU SMC 2020 | LSTM, GRU detectors |
| hmmlearn | SFU [4]-[5] | HMM detector |
| hpelm | SFU [5]-[6] | ELM detector |
| xgboost | Modern baseline | XGBoost detector |
| SHAP | Motaali 2026 | Feature importance |
| ART | NIST AML taxonomy | Attacks & defenses |
| mrtparse | SFU dataset docs | MRT BGP parsing |
| Scapy | SynthBGP 2026 | BGP UPDATE crafting |

## Supervisor

Dr. Md. Sakir Hossain — BRAC University
