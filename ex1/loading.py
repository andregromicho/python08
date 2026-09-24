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


def run_analysis() -> None:

    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    np.random.seed(42)
    signal = np.random.randn(1000)

    df = pd.DataFrame(signal)

    plt.figure(figsize=(10, 5))
    plt.plot(df, color="green")
    plt.title("Matrix Data Stream")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    if check_all_dependencies():
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...")
        run_analysis()
    else:
        print("\n[ERROR] Missing required dependencies!")
        print("To install using pip:")
        print("pip install -r requirements.txt")
        print("To install using Poetry:")
        print("poetry install")


if __name__ == "__main__":
    main()
