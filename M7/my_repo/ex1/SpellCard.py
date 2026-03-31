"""
Concrete spell card implementation
"""
from ex0 import Card


class SpellCard(Card):
    """Concrete implementation of a spell card"""

    VALID_EFECTS = ("damage", "heal", "buff", "debuff")

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        try:
            self._effect_type = self.validate_effect(effect_type)
        except ValueError as e:
            raise ValueError("Could not create Spell, check effect spelling.")

    @staticmethod
    def validate_effect(effect: str) -> str:
        """Validate the spell effect type"""
        if effect not in SpellCard.VALID_EFECTS:
            raise ValueError(
                "Effect must be one of: damage, heal, buff or debuff"
            )
        return effect

    def get_card_info(self) -> dict:
        """Return spell-specific card information"""
        card_info: dict = super().get_card_info()
        card_info["type"] = "Spell"
        card_info["effect_type"] = self._effect_type
        return card_info

    def play(self, game_state: dict) -> dict:
        """Play the spell card, Spells are one-time effects"""
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": game_state.get("effect", "Spell effect resolved")
        }

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell effect on the provided targets"""
        return {
            "spell": self._name,
            "effect_type": self._effect_type,
            "targets": targets,
            "consumed": True
        }
