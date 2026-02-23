import alchemy.elements
from alchemy.potions import healing_potion as heal, strength_potion
from alchemy.elements import create_fire, create_water, create_earth

def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("\nMethod 2 - Specific function import:")
    print("create_water():", create_water())
    print("\nMethod 3 - Aliased import:")
    print("heal():", heal())
    print("\nMethod 4 - Multiple imports:")
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength_potion())
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()