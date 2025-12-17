"""
This program demonstrates the use of raise reserved keyword
"""


def check_plant_health(
        plant_name: str | None = None,
        water_level: int | None = None,
        sunlight_hours: int | None = None
) -> str | None:
    """
    Function to check the plant_name, water_level and sunlight_hours,
    in case any value is wrong, raises ValueError with specific message
    """
    if plant_name is not None and plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level is not None and water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level is not None and water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours is not None and sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours is not None and sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def generic_plant_checker(
plant_name: str | None = None,
        water_level: int | None = None,
        sunlight_hours: int | None = None
) -> None:
    """
    Generic function with try/except structure to make test_plant_checks
    cleaner, and also DRY compliance.
    """
    try:
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print(f"Error: {e.args[0]}")

def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    generic_plant_checker(plant_name="tomato")
    print("\nTesting empty plant name...")
    generic_plant_checker(plant_name="")
    print("\nTesting bad water level...")
    generic_plant_checker(water_level=15)
    print("\nTesting bad sunlight hours...")
    generic_plant_checker(sunlight_hours=0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()