import sys
import os
import site


def main():
    matrix_mode = False
    print()

    if sys.base_prefix != sys.prefix:
        print("MATRIX STATUS: Welcome to the construct")
        matrix_mode = True
    else:
        print("MATRIX STATUS: You're still plugged in")
        matrix_mode = False

    python_path = sys.executable
    print(f"Current Python: {python_path}")

    if matrix_mode:
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()
        print("Package installation path:")
        package_path = site.getsitepackages()
        print(package_path[0])
    else:
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print()
        print("Then run this program again.")
    pass


if __name__ == "__main__":
    main()
