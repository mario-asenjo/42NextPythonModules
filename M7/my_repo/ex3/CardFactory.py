"""Abstract factory interface for card creation"""

from abc import ABC, abstractmethod

from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating themed cards"""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card"""
        raise NotImplementedError

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card"""
        raise NotImplementedError

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card"""
        raise NotImplementedError

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a deck with cards following the factory theme"""
        raise NotImplementedError

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return supported types by this factory"""
        raise NotImplementedError
