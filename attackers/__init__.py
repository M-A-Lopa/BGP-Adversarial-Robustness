"""
attackers/ — Adversarial attacks on BGP anomaly detectors.

Modules:
    backdoor.py         Training-time backdoor (trojan) attack — the core
                        novelty. Exploits time-window label weakness.
                        Variants: single-feature, multi-feature, temporal
                        spread, event-specific vs event-agnostic.
    poisoning.py        Data poisoning baseline — add fake "normal" samples
                        to shift the decision boundary.
    evasion.py          Test-time evasion baseline — perturb features during
                        a real anomaly to look normal. White-box and
                        black-box variants.
    trigger.py          Trigger design and injection logic for the backdoor.
    feasibility.py      Five-stage feasibility pipeline:
                          1. Define attacker AS position
                          2. Map feature controllability (37 features)
                          3. Generate protocol-valid BGP UPDATEs (Scapy)
                          4. Run real feature extractor on generated traffic
                          5. Quantify cost and detectability
    bgp_generator.py    Protocol-valid BGP UPDATE message generation using
                        scapy.contrib.bgp (BGPUpdate, BGPHeader, etc.)
    transfer.py         Cross-collector backdoor transfer experiments
                        (Route Views → RIPE and RIPE → Route Views)
"""
