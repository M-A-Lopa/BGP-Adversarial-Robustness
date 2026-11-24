"""
detectors/ — Reimplementation of BGP anomaly detectors from the 13 SFU papers.

Modules:
    naive_bayes.py      GaussianNB          (Ding 2016, Li 2018b)
    decision_tree.py    DecisionTreeClassifier  (Ding 2016, Li 2018b)
    svm.py              SVC(kernel='linear')    (Batta 2018, Li 2018b)
    random_forest.py    RandomForestClassifier  (modern baseline)
    xgboost_det.py      XGBClassifier           (modern baseline)
    hmm.py              GaussianHMM via hmmlearn  (Li 2018b, Li 2019)
    elm.py              Extreme Learning Machine  (Li 2019, Li 2020)
    lstm.py             LSTM via PyTorch          (Li 2020, SMC 2020)
    gru.py              GRU via PyTorch           (Li 2020, SMC 2020)
    bls.py              Broad Learning System     (SFU BLS V1.0.1)
    base.py             Common interface all detectors implement
"""
