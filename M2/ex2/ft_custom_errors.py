"""
This file shows the creation of own exceptions to handle specific errors in
our code.
"""


class GardenError(Exception):
    """General garden exception class"""
    pass


class PlantError(GardenError):
    """Extended GardenError exception to handle Plant errors."""
    pass


class WaterError(GardenError):
    """Extends GardenError to handle Water errors."""
    pass


def different_situations(error_type: str | None = None) -> None:
    """Tester for the different types of custom errors"""
    if error_type == "plant_error":
        raise PlantError("The tomato plant is wilting!")
    if error_type == "water_error":
        raise WaterError("Not enought ware in the tank!")
    if error_type == "garden1":
        raise PlantError("The tomato plant is wilting!")
    if error_type == "garden2":
        raise WaterError("Not enought ware in the tank!")


def main() -> None:
    """Entry point of the program."""
    print("=== Custom Garden Error Demo ===")
    try:
        print("\nTesting PlantError...")
        different_situations("plant_error")
    except PlantError as e:
        print("Caught PlantError:", e)
    try:
        print("\nTesting WaterError...")
        different_situations("water_error")
    except WaterError as e:
        print("Caught WaterError:", e)
    print("\nTesting catching all garden errors...")
    try:
        different_situations("garden1")
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        different_situations("garden2")
    except GardenError as e:
        print("Caught a garden error:", e)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
