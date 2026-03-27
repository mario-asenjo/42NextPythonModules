"""

"""
from M7.my_repo.ex0 import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health

    def get_card_info(self) -> dict:
        sup_dict = super().get_card_info()
        sup_dict["type"] = "Creature"
        sup_dict["attack"] = self._attack
        sup_dict["health"] = self._health
        return sup_dict

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": game_state["effect"]
        }

    def attack_target(self, target: Card) -> dict:
        return {
            "attacker": self._name,
            "target": target._name,
            "damage_dealt": self._attack,
            "combat_resolved": True
        }
