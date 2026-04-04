"""
Demonstration of functions being subjects of other functions!
"""

from collections.abc import Callable


def heal(target: str, power: int) -> str:
    """Example healing spell"""
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    """Example fireball spell"""
    return f"Fireball hits {target} for {power} damage"


def shield(target: str, power: int) -> str:
    """Example shield spell"""
    return f"Shield saves {target} for {power} incoming damage"


def high_power_only(target: str, power: int) -> bool:
    """Allow casting only for sufficiently strong spells"""
    return power >= 15


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a spell that casts both spells with the same arguments"""
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Returns a spell that multiplies power before casting"""
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Returns a spell that only casts when condition is True"""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Returns a function that casts all spells in order"""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def main() -> None:
    """Main CLI entrypoint for demonstration"""
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined("Dragon", 10)
    spell1_res, spell2_res = combined_result
    print(f"Combined spell result: {spell1_res}, {spell2_res}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(high_power_only, fireball)
    print(safe_fireball("Goblin", 8))
    print(safe_fireball("Goblin", 80))

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, shield])
    for result in combo("Knight", 12):
        print(result)


if __name__ == "__main__":
    main()
