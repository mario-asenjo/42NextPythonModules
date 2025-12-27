"""

"""


def main() -> None:
    players: list[dict] = [
        {
            "name": "alice", "score": 2000, "active": True, "region": "north",
            "achievements": {"first_kill", "level_10", "boss_slayer", "treasure_hunter", "speed_demon"}
        },
        {
            "name": "bob", "score": 1800, "active": True, "region": "east",
            "achievements": {"first_kill", "level_10", "collector"}
        },
        {
            "name": "charlie", "score": 2150, "active": True, "region": "central",
            "achievements": {"first_kill", "level_10", "boss_slayer", "explorer", "crafter", "speed_demon", "sharpshooter"}
        },
        {
            "name": "diana", "score": 2050, "active": False, "region": "north",
            "achievements": {"level_10", "boss_slayer"}
        }
    ]


if __name__ == "__main__":
    main()