"""

"""

import sys
import os
import site


def get_matrix_status(venv: str) -> str:
    """
    Return the matrix-themed status depending on environment isolation.
    :return: Status message
    """
    return (
        "You're still plugged in" if venv == "None detected"
        else "Welcome to the construct"
    )


def get_current_python() -> str:
    """
    Get the absolute path of the current Python interpreter
    :return: str: Interpreter path or a fallback message
    """
    try:
        return sys.executable
    except Exception:
        return "Python path unavailable"


def get_venv() -> str:
    """
    Detect the active virtual environment name
    :return: The virtual environment directory name, or
    "None detected" if no virtual environment is active.
    """
    try:
        venv_path: str | None = os.environ.get("VIRTUAL_ENV")
        if venv_path:
            return os.path.basename(venv_path)

        if hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix:
            return os.path.basename(sys.prefix)

        return "None detected"
    except (KeyError, Exception):
        return "None detected"


def get_path_from_venv(venv: str) -> str:
    """
    Get the full path of the active virtual environment
    :return: str: Full path to the environment, or an empty string
    if it cannot be determined
    """
    try:
        venv_path: str | None = os.environ.get("VIRTUAL_ENV")
        if venv_path:
            return venv_path

        if venv != "None detected":
            return sys.prefix

        return ""
    except (KeyError, Exception):
        return ""

def get_site_path(venv_path: str) -> str:
    """
    Get the site-packages path for the current environment
    :param venv_path: Path to venv
    :return: str: Site-packages path or a fallback message
    """
    try:
        site_packages: list[str] = site.getsitepackages()

        for path in site_packages:
            if venv_path and path.startswith(venv_path):
                return path

        if site_packages:
            return site_packages[0]

        return "Site-packages path unavailable"
    except Exception:
        return "Site-packages path unavailable"


def main() -> None:
    venv: str = get_venv()
    matrix_status: str = get_matrix_status(venv)
    print(f"MATRIX STATUS: {matrix_status}\n")

    current_python: str = get_current_python()
    print(f"Current Python: {current_python}")

    print(f"Virtual Environment: {venv}\n")

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
        print("The machines can see everything you install.\n")
        print("""
To enter the construct, run:
python3 -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate    # On Windows

Then run this program again.""".strip()
        )


if __name__ == "__main__":
    main()
