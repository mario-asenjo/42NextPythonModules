"""Concrete aggressive game strategy"""

from ex0.Card import Card
from ex3 import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Strategy that prioritizes early pressure and direct damage"""

    TURN_MANA_LIMIT: int = 5

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Play as many low-cost aggressive cards as possible"""
        sorted_hand = sorted(
            hand,
            key=lambda my_card: my_card.get_card_info()["cost"]
        )
        mana_used = 0
        cards_played = []
        damage_dealt = 0
        targets_attacked = ["Enemy Player"]

        for card in sorted_hand:
            card_info = card.get_card_info()
            card_cost = card_info["cost"]
            card_type = card_info.get("type", "")

            if mana_used + card_cost > self.TURN_MANA_LIMIT:
                continue

            cards_played.append(card_info["name"])
            mana_used += card_cost

            if card_type == "Creature":
                damage_dealt += card_info.get("attack", 0)
                battlefield.append(card)
            elif card_type == "Spell":
                damage_dealt += 3
            elif card_type == "Artifact":
                damage_dealt += 0

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        """Return the strategy name"""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize enemy player first, then the remaining targets"""
        enemy_player = []
        others = []

        for target in available_targets:
            if target == "Enemy Player":
                enemy_player.append(target)
            else:
                others.append(target)

        return enemy_player + others
