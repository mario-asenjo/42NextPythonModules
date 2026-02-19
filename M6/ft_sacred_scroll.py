"""
Check that imports work at module level and package level.
"""
from typing import Callable

import alchemy
import alchemy.elements


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): " + alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): " + alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): " + alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): " + alchemy.elements.create_air() + "\n")
    print("Testing package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): " + alchemy.create_fire())
    print("alchemy.create_water(): " + alchemy.create_water())
    try:
        foo: Callable = alchemy.create_earth()
        msg: str = foo()
    except AttributeError:
        msg = "AttributeError - not exposed"
    print("alchemy.create_earth(): " + msg)
    try:
        foo: Callable = alchemy.create_air()
        msg = foo()
    except AttributeError:
        msg = "AttributeError - not exposed"
    print("alchemy.create_air(): " + msg)
    print("\nPackage metadata:")
    print("Version: " + alchemy.__version__)
    print("Author: " + alchemy.__author__)


if __name__ == "__main__":
    main()