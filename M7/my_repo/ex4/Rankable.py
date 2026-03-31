"""
Abstract ranking interface for tournament-enabled cards.
"""

from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Interface for entities that can be ranked in tournaments
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate the current rating of the entity
        """
        raise NotImplementedError

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the total number of wins
        """
        raise NotImplementedError

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the total number of losses
        """
        raise NotImplementedError

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Return ranking information
        """
        raise NotImplementedError
