"""
Demonstration script for Exercise 4: Tournament Platform
"""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """
    Demonstrate the tournament platform
    """
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    fire_dragon = TournamentCard(
        "dragon_001",
        "Fire Dragon",
        5,
        "Legendary",
        8,
        6,
        4,
        1200
    )
    ice_wizard = TournamentCard(
        "wizard_001",
        "Ice Wizard",
        4,
        "Epic",
        6,
        5,
        3,
        1150
    )

    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    dragon_rank = fire_dragon.get_rank_info()
    wizard_rank = ice_wizard.get_rank_info()

    print(f"{fire_dragon.get_card_info()['name']} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon_rank['rating']}")
    print(f"- Record: {dragon_rank['wins']}-{dragon_rank['losses']}")

    print(f"{ice_wizard.get_card_info()['name']} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard_rank['rating']}")
    print(f"- Record: {wizard_rank['wins']}-{wizard_rank['losses']}")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print("Match result:", match_result)

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for index, card in enumerate(leaderboard, start=1):
        rank_info = card.get_rank_info()
        print(
            f"{index}. {rank_info['name']} - Rating: {rank_info['rating']} "
            f"({rank_info['wins']}-{rank_info['losses']})"
        )

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
