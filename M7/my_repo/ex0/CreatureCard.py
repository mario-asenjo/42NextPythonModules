"""
Concrete creature card implementation
"""

from ex0.Card import Card


class CreatureCard(Card):
    """Concrete implementation of a creature card"""

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        try:
            self._attack = self.validate_positive(attack, "attack")
            self._health = self.validate_positive(health, "attack")
        except (ValueError, TypeError) as e:
            raise ValueError("Cannot initialize, use positive integers for health and attack") from e

    @staticmethod
    def validate_positive(num: int, field_name: str) -> int:
        if not isinstance(num, int):
            raise TypeError(f"{field_name} must be an integer")
        if num <= 0:
            raise ValueError(f"{field_name} must be a positive integer")
        return num

    def get_card_info(self) -> dict:
        """Return creature-specific card information"""
        sup_dict = super().get_card_info()
        sup_dict["type"] = "Creature"
        sup_dict["attack"] = self._attack
        sup_dict["health"] = self._health
        return sup_dict

    def play(self, game_state: dict) -> dict:
        """Play the creature card"""
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": game_state.get(
                "effect",
                "Creature summoned to battlefield"
            )
        }

    def attack_target(self, target: Card) -> dict:
        """Attack another target card"""
        return {
            "attacker": self._name,
            "target": target.get_card_info()["name"],
            "damage_dealt": self._attack,
            "combat_resolved": True
        }
