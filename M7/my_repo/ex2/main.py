"""
Demonstration script for Exercise 2: Ability system
"""

from ex2.EliteCard import EliteCard


def main() -> None:
    """Demonstrate multiple inheritance with Combatable and Magical"""
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    arcane_warrior: EliteCard = EliteCard(
        "Arcane Warrior",
        4,
        "Epic",
        5,
        10,
        3,
        8
    )
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    print("Attack result:", arcane_warrior.attack("Enemy"))
    print("Defense result:", arcane_warrior.defend(5), end="\n\n")
    print("Magic phase:")
    print(
        "Spell Cast:",
        arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    )
    print("Mana channel:", arcane_warrior.channel_mana(3))
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
