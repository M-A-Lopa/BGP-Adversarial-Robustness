"""
defense/ — Defenses against adversarial attacks on BGP detectors.

Modules:
    feature_selection.py    Hard-to-fake feature selection — keep features
                            that are useful AND costly for the attacker to
                            move. Based on adversarial feature selection
                            (Zhang et al. 2020) and conserved features
                            (Xiao et al. 2017).
    robust_training.py      Robust/trimmed training — downweight or remove
                            extreme training points. From Byzantine-robust
                            learning (Blanchard et al. 2017, Krum).
    adversarial_training.py Adversarial training — augment training with
                            attacker-like perturbations so the model learns
                            to resist them. (Madry et al. 2018, PGD-AT)
    two_collector.py        Two-collector agreement — require both Route
                            Views and RIPE to agree before classifying a
                            minute as normal. BGP-specific defense.
    backdoor_cleaning.py    Post-training backdoor detection and removal:
                            - Activation Clustering (Chen et al. 2018)
                            - Spectral Signatures (Tran et al. 2018)
                            - Neural Cleanse (Wang et al. 2019)
                            Uses ART library implementations where available.
    generalization.py       Defense-generalization study — test each defense
                            across all attack types and both collectors,
                            measuring security–utility trade-offs.
"""
