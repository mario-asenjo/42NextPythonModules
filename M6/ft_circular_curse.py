"""

"""


from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("\n=== Circular Curso Breaking ===")
    print("Testing ingredient validation:")
    print('validate_ingredients("fire air"):', validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):', validate_ingredients("dragon scales"))
    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"):', record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):', record_spell("Dark Magic", "shadow"))
    print("\nTesting late import technique:")
    print('record_spell("Lightning", "air"):', record_spell("Lightning", "air"))
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()