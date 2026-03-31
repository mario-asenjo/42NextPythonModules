"""
Concrete artifact card implementation
"""

from ex0 import Card


class ArtifactCard(Card):
    """Concrete implementation of an artifact card"""

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        try:
            self._durability: int = self.validate_durability(durability)
        except (TypeError, ValueError) as e:
            raise ValueError("Could not create Artifact, check durability")
        self._effect = effect

    @staticmethod
    def validate_durability(durability: int) -> int:
        """Validate artifact durability"""
        if not isinstance(durability, int):
            raise TypeError("durability must be an integer")
        if durability <= 0:
            raise ValueError("durability must be a positive integer")
        return durability

    def get_card_info(self) -> dict:
        """Return artifact-specific card information"""
        card_info: dict = super().get_card_info()
        card_info["type"] = "Artifact"
        card_info["durability"] = self._durability
        card_info["effect"] = self._effect
        return card_info

    def play(self, game_state: dict) -> dict:
        """Play the artifact card, artifacts remain in play"""
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": game_state.get("effect", self._effect)
        }

    def activate_ability(self) -> dict:
        """Activate the artifact's ongoing ability"""
        return {
            "artifact": self._name,
            "effect": self._effect,
            "durability": self._durability,
            "active": True
        }
