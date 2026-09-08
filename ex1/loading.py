import sys
import importlib


def check_dependency(
        module_name: str, purpose: str
        ) -> tuple[bool, str | None, str]:
    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, "__version__", "desconhecida")
        return True, version, f"[OK] {module_name} ({version}) - {purpose}"
    except ImportError:
        return False, None, f"[X] {module_name} - MISSING"


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    required_modules = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready")
    ]

    missing_packages = []
    loaded_modules = {}

    for mod_name, purpose in required_modules:
        success, version, msg = check_dependency(mod_name, purpose)
        print(msg)
        if not success:
            missing_packages.append(mod_name)
        else:
            loaded_modules[mod_name] = version

    if missing_packages:
        print("\n[ERROR] Missing required dependencies!")
        print("\nTo install using pip:")
        print("  pip install -r requirements.txt")
        print("\nTo install using Poetry:")
        print("  poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")

    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    num_points = 1000
    print(f"Processing {num_points} data points...")

    np.random.seed(42)
    signal = np.random.normal(loc=10.0, scale=2.0, size=num_points)
    noise = np.random.exponential(scale=1.5, size=num_points)
    matrix_value = signal + noise

    df = pd.DataFrame({
        "Signal": signal,
        "Noise": noise,
        "MatrixValue": matrix_value
    })

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(
        df["MatrixValue"],
        label="Matrix Signal",
        alpha=0.7, color="green"
    )
    plt.axhline(df["MatrixValue"].mean(), color="red", linestyle="--",
                label=f"Mean: {df['MatrixValue'].mean():.2f}")
    plt.title("Matrix Data Stream Analysis")
    plt.xlabel("Data Points")
    plt.ylabel("Signal Amplitude")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
