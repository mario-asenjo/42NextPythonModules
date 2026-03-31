"""Concrete factory-themed card factory"""
from ex0 import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Factory that creates fantasy-themed cards"""

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a fantasy creature card"""
        if isinstance(name_or_power, str):
            if name_or_power == "dragon":
                return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            if name_or_power == "goblin":
                return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        if isinstance(name_or_power, int):
            if name_or_power >= 6:
                return CreatureCard("Ancient Dragon", 6, "Epic", 8, 6)
            return CreatureCard("Goblin Raider", 2, "Common", 2, 1)
        return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a fantasy spell card"""
        if isinstance(name_or_power, str):
            if name_or_power == "fireball":
                return SpellCard("Lightning Bolt", 3, "Rare", "damage")
            if name_or_power == "ice":
                return SpellCard("Ice Barrier", 2, "Uncommon", "buff")

        if isinstance(name_or_power, int):
            if name_or_power >= 4:
                return SpellCard("Meteor Strike", 4, "Epic", "damage")
            return SpellCard("Minor Heal", 1, "Common", "heal")

        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> ArtifactCard:
        """
        Create a fantasy artifact card.
        """
        if isinstance(name_or_power, str):
            if name_or_power == "mana_ring":
                return ArtifactCard(
                    "Mana Ring",
                    2,
                    "Rare",
                    5,
                    "Permanent: +1 mana per turn"
                )
            if name_or_power == "staff":
                return ArtifactCard(
                    "Wizard Staff",
                    3,
                    "Epic",
                    4,
                    "Permanent: spells gain +1 power"
                )
        if isinstance(name_or_power, int):
            if name_or_power >= 4:
                return ArtifactCard(
                    "Ancient Relic",
                    4,
                    "Legendary",
                    6,
                    "Permanent: boost battlefield control"
                )
            return ArtifactCard(
                "Mana Crystal",
                2,
                "Uncommon",
                4,
                "Permanent: +1 mana per turn"
            )
        return ArtifactCard(
            "Mana Ring",
            2,
            "Rare",
            5,
            "Permanent: +1 mana per turn"
        )

    def create_themed_deck(self, size: int) -> dict:
        """Create a fantasy-themed deck and return both the deck and its stats"""
        if size <= 0:
            raise ValueError("size must be a positive integer")

        deck = Deck()

        for index in range(size):
            if index % 3 == 0:
                deck.add_card(self.create_creature())
            elif index % 3 == 1:
                deck.add_card(self.create_spell())
            else:
                deck.add_card(self.create_artifact())

        return {
            "deck": deck,
            "stats": deck.get_deck_stats()
        }

    def get_supported_types(self) -> dict:
        """Return the themed types supported by this factory"""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
