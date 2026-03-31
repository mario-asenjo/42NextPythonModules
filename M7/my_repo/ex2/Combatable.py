"""
Abstract combat interface for DataDeck cards
"""

from abc import ABC, abstractmethod

from ex0 import Card


class Combatable(ABC):
    """
    Interface for cards with combat capabilities
    """

    @abstractmethod
    def attack(self, target: str) -> dict:
        """Attack a target"""
        raise NotImplementedError

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage"""
        raise NotImplementedError

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return combat-related statistics"""
        raise NotImplementedError
