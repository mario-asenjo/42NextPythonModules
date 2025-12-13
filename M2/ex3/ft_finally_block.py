"""
This file demonstrates the use of the finally block in try-except statements
"""


def open_system() -> None:
    print("Opening water system")


def close_system() -> None:
    print("Closing watering system (cleanup)")


def water_plants(plant_list: list[str]) -> None:
    open_system()
    for plant in plant_list:
        if (plant is None):
            raise ValueError
        print(f"Watering {plant}")
    close_system()
    print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    try:
        print("Testing normal watering...")
        names: list[str] = ["tomato", "lettuce", "carrots"]
        water_plants(names)
        print("Testing with error...")
        names = ["tomato", None]
        water_plants(names)
    except ValueError:
        print(f"Error: Cannot water {names[1]} - Invalid plant!")
    finally:
        close_system()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()