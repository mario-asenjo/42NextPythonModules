"""
Abstract Strategy interface for DataDeck
"""

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    Abstract interface for turn-execution strategies
    """

    @abstractmethod
    def execute_turn(self, hand: list, battefield: list) -> dict:
        """
        Execute one turn using the cards available in hand and battlefield
        """
        raise NotImplementedError

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the strategy name"""
        raise NotImplementedError

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Return targets ordered by priority"""
        raise NotImplementedError
