"""
This program simulates an achievement tracker system.
"""


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice_achievements: set = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob_achievements: set = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie_achievements: set = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}
    print("Player alice achievements:", alice_achievements)
    print("Player bob achievements:", bob_achievements)
    print("Player charlie achievements:", charlie_achievements)
    print("\n=== Achievement Analysis ===")
    unique_achievements: set = alice_achievements.union(bob_achievements, charlie_achievements)
    print("All unique achievements:", unique_achievements)
    print("Total unique achievements:", len(unique_achievements))
    print("\nCommon to all players:", alice_achievements.intersection(bob_achievements, charlie_achievements))
    rare_achievements: set = set()
    print("Rare achievements (1 player):", rare_achievements)


if __name__ == "__main__":
    main()