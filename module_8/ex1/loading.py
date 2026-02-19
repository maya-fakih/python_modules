import importlib
from typing import Dict, Tuple

def check_package(package_name: str) -> Tuple[str, str]:
    try:
        module = importlib.import_module(package_name)
        if hasattr(module, '__version__'):
            version = module.__version__
        else:
            version = "Unknown"
        return "OK", version
    except ImportError:
        return "MISSING", None
    # except Exception:
    #     return "ERROR", None

def display_dependency_status(results: Dict) -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    package_order = ['pandas', 'requests', 'matplotlib']
    descriptions = {
        'pandas': 'Data manipulation ready',
        'requests': 'Network access ready',
        'matplotlib': 'Visualization ready'
    }

    for package in package_order:
        info = results[package]
        status = info['status']
        version = info['version']
        
        if status == "OK":
            print(f"[OK] {package} ({version}) - {descriptions[package]}")
        else:
            print(f"[{status}] {package} - NOT INSTALLED")

def analyze_matrix_data() -> None:
    print("Analyzing Matrix data...")
    
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        
        print("Processing 1000 data points...")
        np.random.seed(42)
        data = np.random.normal(loc=50, scale=10, size=1000)
        
        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.hist(data, bins=30, color='green', edgecolor='black')
        plt.title('Matrix Data Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.savefig('matrix_analysis.png')
        plt.close()
        
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
        
    except Exception as e:
        print(f"Error during analysis: {e}")

def show_installation_instructions() -> None:
    print("\nMissing dependencies detected!")
    print("To install with pip:")
    print("  pip install -r requirements.txt")
    print("\nTo install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")

def main() -> None:
    packages_to_check = ['pandas', 'numpy', 'matplotlib', 'requests']
    
    results = {}
    all_installed = True

    for package in packages_to_check:
        status, version = check_package(package)
        results[package] = {'status': status, 'version': version}
        if status != "OK":
            all_installed = False
    
    display_dependency_status(results)
    
    if all_installed:
        analyze_matrix_data()
    else:
        show_installation_instructions()

if __name__ == "__main__":
    main()