"""Load dependencies and analyse simulated Matrix data."""

import importlib
import sys
from typing import Any


DEPENDENCIES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def load_dependencies() -> dict[str, Any]:
    """Load dependencies and report packages that are unavailable."""
    loaded: dict[str, Any] = {}

    print("Checking dependencies:")
    for package_name, description in DEPENDENCIES.items():
        try:
            package = importlib.import_module(package_name)
        except ImportError:
            print(f"[MISSING] {package_name} - {description}")
            continue

        version = getattr(package, "__version__", "unknown")
        print(f"[OK] {package_name} ({version}) - {description}")
        loaded[package_name] = package

    missing = set(DEPENDENCIES) - set(loaded)
    if missing:
        print("\nSome dependencies are missing.")
        print("Install them with pip:")
        print(f"  {sys.executable} -m pip install -r requirements.txt")
        print("Or install them with Poetry:")
        print("  poetry install")

    return loaded


def compare_dependency_managers(packages: dict[str, Any]) -> None:
    """Compare pip and Poetry and show the versions currently available."""
    print("\nDependency management comparison:")
    print(
        "- pip reads requirements.txt and installs packages into the active "
        "environment."
    )
    print(
        "- Poetry reads pyproject.toml, resolves dependencies, and manages "
        "its environment."
    )
    print("Installed package versions:")
    for package_name in DEPENDENCIES:
        package = packages.get(package_name)
        version = getattr(package, "__version__", "not installed")
        print(f"  {package_name}: {version}")


def analyse_matrix_data(packages: dict[str, Any]) -> None:
    """Generate Matrix data with numpy, analyse it with pandas, and plot it."""
    numpy = packages["numpy"]
    pandas = packages["pandas"]
    matplotlib = packages["matplotlib"]

    print("\nAnalyzing Matrix data...")
    data = numpy.random.default_rng(42).normal(
        loc=100.0, scale=15.0, size=(1000, 2)
    )
    matrix_data = pandas.DataFrame(data, columns=["red_pill", "blue_pill"])
    matrix_data["difference"] = (
        matrix_data["red_pill"] - matrix_data["blue_pill"]
    )

    print(f"Processing {len(matrix_data)} data points...")
    print(f"Average difference: {matrix_data['difference'].mean():.2f}")

    matplotlib.use("Agg")
    pyplot = importlib.import_module("matplotlib.pyplot")
    print("Generating visualization...")
    figure = pyplot.figure(figsize=(8, 4))
    pyplot.plot(matrix_data.index, matrix_data["red_pill"], label="Red pill")
    pyplot.plot(matrix_data.index, matrix_data["blue_pill"], label="Blue pill")
    pyplot.title("Simulated Matrix data")
    pyplot.xlabel("Data point")
    pyplot.ylabel("Signal")
    pyplot.legend()
    figure.tight_layout()
    figure.savefig("matrix_analysis.png")
    pyplot.close(figure)
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    packages = load_dependencies()
    compare_dependency_managers(packages)

    if set(DEPENDENCIES) <= set(packages):
        analyse_matrix_data(packages)
    else:
        print(
            "\nAnalysis skipped until all required dependencies are installed."
        )


if __name__ == "__main__":
    main()
