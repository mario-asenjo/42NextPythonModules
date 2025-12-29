"""
This program simulates an achievement tracker system.
"""
from hashlib import algorithms_available


def main() -> None:
    """
    Entry point of the program
    Demonstrates use of sets and operations on sets.
    Uses intersection() and difference() to find equal or different values
    inside the sets, and union() to join the sets into one.
    """
    print("=== Achievement Tracker System ===")
    alice_achievements: set = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }
    bob_achievements: set = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }
    charlie_achievements: set = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }
    print("Player alice achievements:", alice_achievements)
    print("Player bob achievements:", bob_achievements)
    print("Player charlie achievements:", charlie_achievements)
    print("\n=== Achievement Analysis ===")
    unique_achievements: set = alice_achievements.union(
        bob_achievements, charlie_achievements
    )
    print("All unique achievements:", unique_achievements)
    print("Total unique achievements:", len(unique_achievements))
    print("\nCommon to all players:", alice_achievements.intersection(
        bob_achievements, charlie_achievements)
    )
    exclusive_alice: set = alice_achievements.difference(
        bob_achievements.union(charlie_achievements)
    )
    exclusive_bob: set = bob_achievements.difference(
        alice_achievements.union(charlie_achievements)
    )
    exclusive_charlie: set = charlie_achievements.difference(
        alice_achievements.union(bob_achievements)
    )
    rare_achievements: set = exclusive_alice.union(
        exclusive_bob, exclusive_charlie
    )
    print("Rare achievements (1 player):", rare_achievements)
    alice_vs_bob_common: set = alice_achievements.intersection(
        bob_achievements
    )
    print("\nAlice vs Bob common:", alice_vs_bob_common)
    alice_unique_vs_bob: set = alice_achievements.difference(
        bob_achievements
    )
    print("Alice unique:", alice_unique_vs_bob)
    bob_unique_vs_alice: set = bob_achievements.difference(
        alice_achievements
    )
    print("Bob unique:", bob_unique_vs_alice)


if __name__ == "__main__":
    main()
