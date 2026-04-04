"""
Demonstration of lambda expressions for transformations on data
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Orders using lambda by 'power' level descending
    :param artifacts: list of dict artifacts with: name, power and type
    :return: The sorted list
    """
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filters using lambda to find mages with power >= min_power
    :param mages: List of dict mages with: name, power and element
    :return: A list of filtered mages
    """
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Map using lambda to add '* ' prefix and ' *' suffix
    :param spells: A list of spell names
    :return: A list of transformed spell names
    """
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    Use lambdas to find most, least and average powerful mage's power level.
    :param mages: List of dict mages with: name, power and element
    :return: A dictionary with specified values
    """

    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_mage: dict = max(mages, key=lambda x: x['power'])
    min_mage: dict = min(mages, key=lambda x: x['power'])
    avg_power: float = round(sum(mage['power'] for mage in mages) / len(mages), 2)

    return {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "avg_power": avg_power
    }


def main() -> None:
    """Main CLI entrypoint for demonstration"""
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ice Wand", "power": 78, "type": "weapon"},
    ]

    mages = [
        {"name": "Alex", "power": 95, "element": "fire"},
        {"name": "Jordan", "power": 67, "element": "ice"},
        {"name": "Riley", "power": 82, "element": "wind"},
        {"name": "Casey", "power": 54, "element": "earth"},
    ]

    spells = ["fireball", "heal", "shield"]
    print("Testing artifact sorter...")
    sorted_artifacts: list[dict] = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting power filter...")
    print("Mages:", mages)
    strong_mages: list[dict] = power_filter(mages, 60)
    print("Stronger mages:", strong_mages)

    print("\nTesting spell transformer...")
    print("Spells:", spells)
    transformed_spells: list[str] = spell_transformer(spells)
    print("Transformed spells:", transformed_spells)

    print("\nTesting mage stats...")
    print(f"Mage Stats:\n{mage_stats(mages)}")


if __name__ == "__main__":
    main()
