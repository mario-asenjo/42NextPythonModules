"""
Deck management system for DataDeck
"""

import random

from ex0.Card import Card

class Deck:
    """Management class for deck implementations using Cards."""

    def __init__(self) -> None:
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck"""
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove the first card matching the given name"""
        for i, card in enumerate(self._cards):
            if card.get_card_info()["name"] == card_name:
                del self._cards[i]
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck in place"""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Draw the top ard from the deck"""
        if not self._cards:
            raise ValueError("Cannot draw from an empty deck")
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict:
        """Return statistics about the current deck"""
        total_cards: int = len(self._cards)
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        total_cost: int = 0

        for card in self._cards:
            card_info: dict = card.get_card_info()
            total_cost += card_info["cost"]
            card_type: str = card_info.get("type", "")
            if card_type == "Creature":
                creatures += 1
            elif card_type == "Spell":
                spells += 1
            elif card_type == "Artifact":
                artifacts += 1

        avg_cost = 0.0
        if total_cards > 0:
            avg_cost = total_cost / total_cards

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost.__round__(1)
        }
