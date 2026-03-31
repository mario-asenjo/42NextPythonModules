"""
Demo for Card and CreatureCard implementations.
"""


from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Demonstrate the functionality of the abstract card foundation"""
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    fire_dragon_card: CreatureCard = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )
    print("CreatureCard Info:")
    print(fire_dragon_card.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", fire_dragon_card.is_playable(6))
    game_state: dict = {
        "available_mana": 6,
        "effect": "Creature summoned to battlefield"
    }
    print("Play result:", fire_dragon_card.play(game_state))
    goblin_warrior_card: CreatureCard = CreatureCard(
        "Goblin Warrior",
        5,
        "Common",
        5,
        4
    )
    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_dragon_card.attack_target(goblin_warrior_card))
    print("\nTesting insufficient mana (3 available):")
    print("Playable:", fire_dragon_card.is_playable(3))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
