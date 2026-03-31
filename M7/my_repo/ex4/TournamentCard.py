"""
Tournament-ready card implementation using multiple inheritance
"""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Card with combat and ranking capabilities for tournament play
    """

    BASE_RATING = 1200

    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        defense: int,
        base_rating: int = BASE_RATING
    ) -> None:
        super().__init__(name, cost, rarity)
        self._card_id = card_id
        self._attack_power = self._validate_positive_int(
            attack_power,
            "attack_power"
        )
        self._health = self._validate_positive_int(health, "health")
        self._defense = self._validate_non_negative_int(defense, "defense")
        self._wins = 0
        self._losses = 0
        self._rating = self._validate_positive_int(base_rating, "base_rating")

    @staticmethod
    def _validate_positive_int(value: int, field_name: str) -> int:
        """
        Validate that a value is a positive integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{field_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{field_name} must be a positive integer")
        return value

    @staticmethod
    def _validate_non_negative_int(value: int, field_name: str) -> int:
        """
        Validate that a value is a non-negative integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{field_name} must be an integer")
        if value < 0:
            raise ValueError(f"{field_name} must be a non-negative integer")
        return value

    def get_card_info(self) -> dict:
        """
        Return full card information for tournament mode
        """
        card_info = super().get_card_info()
        card_info["id"] = self._card_id
        card_info["type"] = "Tournament"
        card_info["attack_power"] = self._attack_power
        card_info["health"] = self._health
        card_info["defense"] = self._defense
        return card_info

    def play(self, game_state: dict) -> dict:
        """
        Play the tournament card
        """
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": game_state.get(
                "effect",
                "Tournament card deployed to battlefield"
            ),
        }

    def attack(self, target) -> dict:
        """
        Attack a target during a tournament match
        """
        if hasattr(target, "get_card_info"):
            target_name = target.get_card_info().get("name", "Unknown")
        else:
            target_name = str(target)

        return {
            "attacker": self._name,
            "target": target_name,
            "damage": self._attack_power,
            "combat_type": "tournament_duel",
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage
        """
        validated_damage = self._validate_non_negative_int(
            incoming_damage,
            "incoming_damage"
        )
        damage_blocked = min(self._defense, validated_damage)
        damage_taken = validated_damage - damage_blocked
        remaining_health = max(0, self._health - damage_taken)

        return {
            "defender": self._name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": remaining_health > 0,
        }

    def get_combat_stats(self) -> dict:
        """
        Return combat statistics
        """
        return {
            "attack_power": self._attack_power,
            "health": self._health,
            "defense": self._defense,
        }

    def calculate_rating(self) -> int:
        """
        Calculate rating based on current tournament record
        """
        self._rating = self.BASE_RATING + (self._wins * 16) - (self._losses * 16)
        return self._rating

    def update_wins(self, wins: int) -> None:
        """
        Add wins and recalculate rating
        """
        validated_wins = self._validate_non_negative_int(wins, "wins")
        self._wins += validated_wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        """
        Add losses and recalculate rating
        """
        validated_losses = self._validate_non_negative_int(losses, "losses")
        self._losses += validated_losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        """
        Return ranking information
        """
        return {
            "id": self._card_id,
            "name": self._name,
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses,
        }

    def get_tournament_stats(self) -> dict:
        """
        Return combined tournament information
        """
        return {
            "card_info": self.get_card_info(),
            "combat_stats": self.get_combat_stats(),
            "rank_info": self.get_rank_info(),
        }
