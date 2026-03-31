"""Game engine orchestrator for DataDeck"""

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Coordinates card creation and turn simulation"""

    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list = []
        self._battlefield: list = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy
    ) -> None:
        """Configure the engine with a card factory and a strategy"""
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        """Simulate one game turn using the configured factory and strategy"""
        if self._factory is None or self._strategy is None:
            raise ValueError("Engine must be configured before simulation")

        self._hand = [
            self._factory.create_creature("dragon"),
            self._factory.create_creature("goblin"),
            self._factory.create_spell("fireball")
        ]
        self._cards_created += len(self._hand)

        actions = self._strategy.execute_turn(self._hand, self._battlefield)

        self._turns_simulated += 1
        self._total_damage += actions["damage_dealt"]

        hand_snapshot = [
            f"{card.get_card_info()['name']} ({card.get_card_info()['cost']})"
            for card in self._hand
        ]

        return {
            "strategy": self._strategy.get_strategy_name(),
            "hand": hand_snapshot,
            "actions": actions
        }

    def get_engine_status(self) -> dict:
        """Return a summary of the engine state"""
        strategy_name = "Not configured"
        if self._strategy is not None:
            strategy_name = self._strategy.get_strategy_name()

        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self._total_damage,
            "cards_created": self._cards_created
        }
