"""
Program that simulates an analytics dashboard
"""


def retrieve_players_list() -> list[dict]:
    """Function that returns a list with players info in dicts"""
    return [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements":
                {
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "treasure_hunter",
                    "speed_demon"
                }
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements":
                {
                    "first_kill",
                    "level_10",
                    "collector"
                }
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements":
                {
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "speed_demon"
                }
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements":
                {
                    "level_10",
                    "boss_slayer"
                }
        }
    ]


def main() -> None:
    """Main function of the program that shows skills in analyzing data"""
    players: list[dict] = retrieve_players_list()
    high_scorers: list = [
        player["name"] for player in players if player["score"] > 2000
    ]
    scores_doubled: list = [player["score"] * 2 for player in players]
    active_players: list = [
        player["name"] for player in players if player["active"]
    ]
    player_scores: dict = {
        player["name"]: player["score"] for player in players
        if player["name"] in active_players
    }
    score_categories: dict = {
        "high": sum(1 for p in players if p["score"] >= 2050),
        "medium": sum(1 for p in players if 1800 <= p["score"] <= 2050),
        "low": sum(1 for p in players if p["score"] <= 1800),
    }
    achievement_count: dict = {
        player["name"]: len(player["achievements"]) for player in players
    }
    unique_players: set = {player["name"] for player in players}
    unique_achievements: set = {
        ach for player in players for ach in player["achievements"]
    }
    active_regions: set = {
        player["region"] for player in players if player["active"]
    }
    total_players: int = len(players)
    total_unique_achievements: int = sum(
        len(player["achievements"]) for player in players
    )
    average_score: float = sum(
        player["score"] for player in players
    ) / total_players
    top_performer: dict = [
        p for p in players if p["score"] == max(pl["score"] for pl in players)
    ][0]
    top_performer_stats: str = (f"{top_performer['name']} "
                                f"({top_performer['score']} points, "
                                f"{len(top_performer['achievements'])} "
                                f"achievements)")
    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples ===")
    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", scores_doubled)
    print("Active players:", active_players)
    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", player_scores)
    print("Score categories:", score_categories)
    print("Achievement counts:", achievement_count)
    print("\n=== Set Comprehension Examples ===")
    print("Unique players:", sorted(unique_players))
    print("Unique achievements:", sorted(unique_achievements))
    print("Active regions:", sorted(active_regions))
    print("\n=== Combined Analysis ===")
    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print("Top performer:", top_performer_stats)


if __name__ == "__main__":
    main()
