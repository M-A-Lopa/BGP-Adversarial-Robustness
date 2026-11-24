"""
dataset/ — SFU/IEEE DataPort BGP routing-records dataset management.

Modules:
    loader.py           Load and return Slammer, WannaCrypt, Moscow CSV files
    preprocess.py       Clean missing values, drop zero-variance features,
                        z-score normalize, fix labels (-1 → 0 for PyTorch)
    splitter.py         Implement the three honest splits:
                          - Unseen event (leave-one-event-out)
                          - Cross-collector (Route Views ↔ RIPE)
                          - Time-order (chronological within event)
    label_analysis.py   Analyze time-window label quality, estimate
                        mislabeled minutes near event boundaries
    stats.py            Dataset statistics and summary tables

Note:
    Raw CSV files are NOT committed to git (see .gitignore).
    Place them in dataset/raw/ after downloading from IEEE DataPort.
    Columns: 1-4 time, 5-41 features, 42 label (-1 or 1).
"""
