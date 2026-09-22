import importlib


def check_dependencies(module_name: str) -> tuple[bool, str]:
    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, "not installed"


def check_all_dependencies() -> bool:
    packages = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready"),
    ]
    print("Checking dependencies:")
    all_ok = True

    for package, description in packages:
        check, version = check_dependencies(package)
        if check:
            print(f"[OK] {package} ({version}) - {description}")
        else:
            all_ok = False
            print(f"[MISSING] {package} - Not installed")

    return all_ok


def run_analysis () -> None:

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    signal = np.random.randn(1000)

    