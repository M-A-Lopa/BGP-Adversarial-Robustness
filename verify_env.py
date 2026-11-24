#!/usr/bin/env python3
"""
verify_env.py — Check that all required packages are installed and importable.

Usage:
    python verify_env.py          # check all packages
    python verify_env.py --fix    # attempt pip install for missing ones

Exit codes:
    0  — all required packages found
    1  — one or more required packages missing
"""

import importlib
import subprocess
import sys
import shutil

# ───────────────────────────────────────────────────────────────
# Registry: (import_name, pip_name, min_version, purpose)
# ───────────────────────────────────────────────────────────────
REQUIRED = [
    # Core scientific stack
    ("numpy",       "numpy",       "1.24.0",  "Array operations, linear algebra"),
    ("scipy",       "scipy",       "1.10.0",  "Scientific computing, sparse matrices"),
    ("pandas",      "pandas",      "2.0.0",   "Data loading and preprocessing"),

    # Classical ML detectors (SFU papers: NB, DT, SVM, RF)
    ("sklearn",     "scikit-learn","1.3.0",   "Naive Bayes, Decision Tree, SVM, Random Forest"),

    # XGBoost (modern baseline)
    ("xgboost",     "xgboost",     "2.0.0",   "XGBoost gradient-boosted trees"),

    # Hidden Markov Model (SFU papers: HMM detector)
    ("hmmlearn",    "hmmlearn",    "0.3.0",   "Hidden Markov Model detector"),

    # Extreme Learning Machine (SFU papers: ELM detector)
    ("hpelm",       "hpelm",       "1.0.10",  "Extreme Learning Machine detector"),

    # Deep learning (SFU papers: LSTM, GRU; also BLS custom impl)
    ("torch",       "torch",       "2.0.0",   "PyTorch — LSTM, GRU, adversarial training"),

    # Explainability
    ("shap",        "shap",        "0.46.0",  "SHAP feature importance analysis"),

    # Adversarial ML
    ("art",         "adversarial-robustness-toolbox", "1.18.0",
     "ART — backdoor, poisoning, evasion attacks & defenses"),

    # BGP data parsing
    ("mrtparse",    "mrtparse",    "2.0.0",   "MRT-format BGP update parser"),

    # BGP message crafting
    ("scapy",       "scapy",       "2.6.0",   "BGP UPDATE message generation (feasibility gate)"),

    # Visualization
    ("matplotlib",  "matplotlib",  "3.7.0",   "Plotting and figures"),
    ("seaborn",     "seaborn",     "0.13.0",  "Statistical visualization"),

    # Experiment management
    ("tqdm",        "tqdm",        "4.65.0",  "Progress bars"),
    ("yaml",        "pyyaml",      "6.0",     "YAML config files"),
    ("jsonlines",   "jsonlines",   "4.0.0",   "JSONL experiment logs"),

    # Testing
    ("pytest",      "pytest",      "7.4.0",   "Unit tests"),
]

OPTIONAL = [
    # pybgpstream needs C library — not pip-installable alone
    ("_pybgpstream", "pybgpstream", "2.0.0",
     "BGPStream (requires libBGPStream C library)"),

    # Jupyter
    ("jupyter",     "jupyter",     "1.0.0",   "Jupyter notebook support"),

    # BGP simulation
    # ("bgpy",        "bgpy-pkg",    "7.0.0",   "BGP/ROV simulation"),
]


def get_version(module):
    """Try common version attributes."""
    for attr in ("__version__", "VERSION", "version"):
        v = getattr(module, attr, None)
        if v is not None:
            return str(v)
    # fallback: importlib.metadata
    try:
        import importlib.metadata as meta
        return meta.version(module.__name__)
    except Exception:
        return "unknown"


def parse_version(v_str):
    """Parse version string into tuple of ints for comparison."""
    try:
        parts = v_str.split(".")
        return tuple(int(x) for x in parts[:3])
    except (ValueError, AttributeError):
        return (0, 0, 0)


def check_package(import_name, pip_name, min_version, purpose):
    """Check a single package. Returns (status, message)."""
    try:
        mod = importlib.import_module(import_name)
        installed_ver = get_version(mod)
        if parse_version(installed_ver) >= parse_version(min_version):
            return "OK", f"{pip_name} {installed_ver}"
        else:
            return "OLD", f"{pip_name} {installed_ver} (need >={min_version})"
    except ImportError:
        return "MISSING", f"{pip_name} not installed"


def main():
    fix_mode = "--fix" in sys.argv

    print("=" * 65)
    print("  BGP Adversarial Robustness — Environment Verification")
    print("=" * 65)
    print(f"  Python:   {sys.version}")
    print(f"  Platform: {sys.platform}")

    # Check pip
    pip_ok = shutil.which("pip") or shutil.which("pip3")
    print(f"  pip:      {'found' if pip_ok else 'NOT FOUND'}")
    print("=" * 65)

    all_ok = True
    missing = []

    print("\n  REQUIRED PACKAGES\n")
    for import_name, pip_name, min_ver, purpose in REQUIRED:
        status, msg = check_package(import_name, pip_name, min_ver, purpose)
        icon = {"OK": "✓", "OLD": "⚠", "MISSING": "✗"}[status]
        color_start = {"OK": "\033[92m", "OLD": "\033[93m", "MISSING": "\033[91m"}[status]
        color_end = "\033[0m"
        print(f"  {color_start}{icon}{color_end}  {msg:<50s}  {purpose}")
        if status != "OK":
            all_ok = False
            missing.append((pip_name, min_ver))

    print("\n  OPTIONAL PACKAGES\n")
    for import_name, pip_name, min_ver, purpose in OPTIONAL:
        status, msg = check_package(import_name, pip_name, min_ver, purpose)
        icon = {"OK": "✓", "OLD": "~", "MISSING": "-"}[status]
        color_start = {"OK": "\033[92m", "OLD": "\033[93m", "MISSING": "\033[90m"}[status]
        color_end = "\033[0m"
        print(f"  {color_start}{icon}{color_end}  {msg:<50s}  {purpose}")

    print("\n" + "=" * 65)

    if all_ok:
        print("  ✓ All required packages installed and up to date.")
        print("=" * 65)
        return 0

    print(f"  ✗ {len(missing)} required package(s) missing or outdated.")

    if fix_mode and pip_ok:
        print("\n  Attempting to install missing packages...\n")
        for pip_name, min_ver in missing:
            spec = f"{pip_name}>={min_ver}"
            print(f"    pip install {spec}")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", spec],
                capture_output=True,
            )
        # Re-check
        print("\n  Re-checking...\n")
        still_missing = 0
        for import_name, pip_name, min_ver, purpose in REQUIRED:
            status, msg = check_package(import_name, pip_name, min_ver, purpose)
            if status != "OK":
                still_missing += 1
                print(f"    ✗ Still missing: {pip_name}")
        if still_missing == 0:
            print("  ✓ All required packages now installed.")
            return 0
        else:
            print(f"\n  ✗ {still_missing} package(s) could not be installed.")
            print("    Try:  pip install -r requirements.txt")
            return 1
    else:
        print("\n  To install missing packages, run:")
        print("    pip install -r requirements.txt")
        print("  Or run this script with --fix:")
        print("    python verify_env.py --fix")
        print("=" * 65)
        return 1


if __name__ == "__main__":
    sys.exit(main())
