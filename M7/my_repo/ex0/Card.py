"""
Abstract base class for all DataDeck cards
"""

from abc import ABC, abstractmethod


class Card(ABC):
    """
    Abstract base class that defines the common contract for all cards
    """
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name = name
        self._cost = cost
        self._rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Play the card using the current game state
        """
        raise NotImplementedError

    def get_card_info(self) -> dict:
        """
        Return the base information of the card
        """
        return {
            "name": self._name,
            "cost": self._cost,
            "rarity": self._rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Return True if the available mana is enough to play the card
        """
        return available_mana > self._cost
