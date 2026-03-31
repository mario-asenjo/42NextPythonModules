"""
Abstract magic interface for DataDeck cards
"""

from abc import ABC, abstractmethod


class Magical(ABC):
    """Interface for cards with magical capabilities"""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on one or more targets"""
        raise NotImplementedError

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Increase available mana by channeling magical energy"""
        raise NotImplementedError

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return magic-related statistics"""
        raise NotImplementedError
