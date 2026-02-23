"""

"""
from M6 import alchemy
from M6.alchemy.transmutation import basic, advanced


def main() -> None:
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold():", basic.lead_to_gold())
    print("stone_to_gem():", basic.stone_to_gem())
    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone():", advanced.philosophers_stone())
    print("elixir_of_life():", advanced.elixir_of_life())
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold():", alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone():", alchemy.transmutation.philosophers_stone())
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()