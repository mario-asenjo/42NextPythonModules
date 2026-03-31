"""
Demo for the DataDeck deck builder system
"""
from ex0 import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def main() -> None:
    """Demonstrate the functionality of the deck builder exercise"""
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck: Deck = Deck()

    fire_dragon: CreatureCard = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )
    lightning_bolt: SpellCard = SpellCard(
        "Lightning bolt",
        3,
        "Rare",
        "damage"
    )
    mana_crystal: ArtifactCard = ArtifactCard(
        "Mana Crystal",
        2,
        "Uncommon",
        4,
        "Permanent: +1 mana per turn"
    )
    deck.add_card(fire_dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)

    print("Deck stats:", deck.get_deck_stats(), end="\n\n")

    print("Drawing and playing cards:\n")
    deck.shuffle()
    while True:
        try:
            drawn_card: Card = deck.draw_card()
            drawn_info: dict = drawn_card.get_card_info()

            print(f"Drew: {drawn_info['name']} ({drawn_info['type']})")

            if drawn_info["type"] == "Spell":
                game_state = {"effect": "Deal 3 damage to target"}
            elif drawn_info["type"] == "Artifact":
                game_state = {"effect": "Permanent: +1 mana per turn"}
            else:
                game_state = {"effect": "Creature summoned to battlefield"}

            print("Play result:", drawn_card.play(game_state), end="\n\n")
        except ValueError:
            break
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
