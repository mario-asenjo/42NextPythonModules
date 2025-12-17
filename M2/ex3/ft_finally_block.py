"""
This file demonstrates the use of the finally block in try-except statements
"""


def open_system() -> None:
    """This function opens the watering system"""
    print("Opening watering system")


def close_system() -> None:
    """This function closes watering system for cleanup"""
    print("Closing watering system (cleanup)")


def water_plants(plant_list: list[str]) -> None:
    """
    Function that recieves a list of plant names, and prints
    Watering and the name of each plant, in case a name is None
    the function raises ValueError.
    """
    open_system()
    for plant in plant_list:
        if plant is None:
            raise ValueError
        print(f"Watering {plant}")
    close_system()
    print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Function to test water_plants function and demonstrate:
    The use of try/except/finally structure.
    """
    print("=== Garden Watering System ===")
    names: list[str] = []
    try:
        print("\nTesting normal watering...")
        names = ["tomato", "lettuce", "carrots"]
        water_plants(names)
        print("\nTesting with error...")
        names = ["tomato", None]
        water_plants(names)
    except ValueError:
        print(f"Error: Cannot water {names[1]} - invalid plant!")
    finally:
        close_system()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()