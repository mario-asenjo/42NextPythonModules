"""
Tournament platform management system
"""

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """
    Platform that manages tournament cards and match results
    """

    def __init__(self) -> None:
        self._registered_cards: dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a tournament card and return its identifier
        """
        card_id = card.get_rank_info()["id"]
        self._registered_cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Create a match between two registered cards
        """
        if card1_id not in self._registered_cards:
            raise ValueError(f"Unknown card id: {card1_id}")
        if card2_id not in self._registered_cards:
            raise ValueError(f"Unknown card id: {card2_id}")
        if card1_id == card2_id:
            raise ValueError("A card cannot fight itself")

        card1 = self._registered_cards[card1_id]
        card2 = self._registered_cards[card2_id]

        card1_power = (
            card1.get_combat_stats()["attack_power"] +
            card1.get_combat_stats()["defense"]
        )
        card2_power = (
            card2.get_combat_stats()["attack_power"] +
            card2.get_combat_stats()["defense"]
        )

        if card1_power >= card2_power:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        self._matches_played += 1

        winner_info = winner.get_rank_info()
        loser_info = loser.get_rank_info()

        return {
            "winner": winner_info["id"],
            "loser": loser_info["id"],
            "winner_rating": winner_info["rating"],
            "loser_rating": loser_info["rating"],
        }

    def get_leaderboard(self) -> list:
        """
        Return registered cards ordered by rating descending
        """
        leaderboard = list(self._registered_cards.values())
        leaderboard.sort(
            key=lambda card: card.get_rank_info()["rating"],
            reverse=True
        )
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """
        Generate a tournament summary report
        """
        total_cards = len(self._registered_cards)
        total_rating = 0

        for card in self._registered_cards.values():
            total_rating += card.get_rank_info()["rating"]

        avg_rating = 0
        if total_cards > 0:
            avg_rating = total_rating // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
