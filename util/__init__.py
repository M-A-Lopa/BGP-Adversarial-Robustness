"""
util/ — Shared utilities across the project.

Modules:
    metrics.py          Evaluation metrics: F1, precision, recall, MCC,
                        false-alarm rate, attack success rate, defense cost.
                        All from sklearn.metrics + custom implementations.
    config.py           YAML-based experiment configuration loader.
    logger.py           Logging setup (console + file) with tqdm integration.
    reproducibility.py  Seed management, deterministic PyTorch/numpy settings.
    visualization.py    Common plotting functions (confusion matrix, SHAP
                        summary, ROC curves, metric comparison tables).
    timer.py            Training/inference timing utilities.
"""
