"""

"""

import sys
import os
import site


def get_matrix_status(venv: str) -> str:
    return "You're still pluged in" if venv == "None detected" else "Welcome to the construct"


def get_current_python() -> str:
    return ""


def get_venv() -> str:
    if 'VIRTUAL_ENV' in os.environ:
        return f"{os.environ['VIRTUAL_ENV']}"
    return "None detected"


def get_path_from_venv(venv: str) -> str:
    return ""


def get_site_path(venv_path: str) -> str:
    return ""


def main() -> None:
    venv: str = get_venv()
    matrix_status: str = get_matrix_status(venv)
    print(f"MATRIX STATUS: {matrix_status}")

    current_python: str = get_current_python()
    print(f"Current Python: {current_python}")

    print(f"Virtual Environment: {venv}")

    if venv != "None detected":
        venv_path = get_path_from_venv(venv)
        print(f"Environment Path: {venv_path}\n")
        print(
            "SUCCESS: You're in an isolated environment!\nSafe to "
            "install packages without affecting the global system."
        )

        site_path = get_site_path(venv_path)
        print(f"\nPackage installation path:\n{site_path}")
    else:
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("""
To enter the construct, run:
python3 -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate    # On Windows

Then run this program again.
        """)


if __name__ == "__main__":
    main()
