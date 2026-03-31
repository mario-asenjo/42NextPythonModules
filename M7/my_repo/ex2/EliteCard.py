"""Multiple inheritance implementation for an elite card"""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Powerful card that combines base card behavior, combat abilities,
    and magical abilities
    """

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack_power: int,
            health: int,
            defense: int,
            mana: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self._attack_power = self.validate_positive_int(
            attack_power,
            "attack_power",
            True
        )
        self._health = self.validate_positive_int(health, "health", True)
        self._defense = self.validate_positive_int(defense, "defense")
        self._mana = self.validate_positive_int(mana, "mana")

    @staticmethod
    def validate_positive_int(value: int, field: str, negative: bool = False) -> int:
        """Validate that a value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{field} must be an integer")
        if negative and value <= 0:
            raise ValueError(f"{field} must be a positive integer")
        elif value < 0:
            raise ValueError(f"{field} must be non negative integer")
        return value

    def get_card_info(self) -> dict:
        """Return full elite card information"""
        card_info: dict = super().get_card_info()
        card_info["type"] = "Elite"
        card_info["attack_power"] = self._attack_power
        card_info["health"] = self._health
        card_info["defense"] = self._defense
        card_info["mana"] = self._mana
        return card_info

    def play(self, game_state: dict) -> dict:
        """Play the elite card on the battlefield"""
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": game_state.get(
                "effect",
                "Elite card deployed to battlefield"
            )
        }

    def attack(self, target: str) -> dict:
        """Perform a combat attack against a target"""

        target_name = target

        return {
            "attacker": self._name,
            "target": target_name,
            "damage": self._attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage using defense points"""
        validated_damage = self.validate_positive_int(
            incoming_damage,
            "incoming damage"
        )
        damage_blocked = min(self._defense, validated_damage)
        damage_taken = validated_damage - damage_blocked
        self._health -= damage_taken

        return {
            "defender": self._name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self._health > 0
        }

    def get_combat_stats(self) -> dict:
        """Return combat statistics"""
        return {
            "attack_power": self._attack_power,
            "health": self._health,
            "defense": self._defense
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell, consuming mana based on number of targets"""
        mana_used = max(1, len(targets) * 2)

        if mana_used > self._mana:
            return {
                "caster": self._name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": 0,
                "success": False,
                "reason": "Not enough mana"
            }
        self._mana -= mana_used
        return {
            "caster": self._name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used,
            "success": True
        }

    def channel_mana(self, amount: int) -> dict:
        """Increase internal mana pool"""
        validated_amount = self.validate_positive_int(amount, "amount")
        self._mana += validated_amount

        return {
            "channeled": validated_amount,
            "total_mana": self._mana
        }

    def get_magic_stats(self) -> dict:
        """Return magic statistics"""
        return {
            "mana": self._mana,
            "spellcasting": True
        }
