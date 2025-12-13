"""
This file shows the creation of own exceptions to handle specific errors in
our code.
"""


class GardenError(Exception):
    """General garden exception class"""
    def __init__(self, message: str) -> None:
        """Creates a GardenException object with message"""
        super().__init__()
        self.__message: str = message

    def get_message_cause(self) -> str:
        """Returns the cause of the exception"""
        return "Caught a garden error: " + self.__message
    
    def get_message_attr(self) -> str:
        """Getter for __message attribute"""
        return self.__message


class PlantError(GardenError):
    """Extended GardenError exception to handle Plant errors."""
    def __init__(self, message) -> None:
        """Creates a PlantError exception with message"""
        super().__init__(message)

    def get_message(self) -> str:
        """Returns the message of the exception"""
        return "Caught PlantError: " + super().get_message_attr()


class WaterError(GardenError):
    """Extends GardenError to handle Water errors."""
    def __init__(self, message) -> None:
        """Creates a WaterError exception with message"""
        super().__init__(message)

    def get_message(self) -> str:
        """Returns the cause of the exception"""
        return "Caught WaterError: " + super().get_message_attr()
    

def different_situations(error_type: str | None = None) -> None:
    """Tester for the different types of custom errors"""
    if (error_type == "plant_error"):
        raise PlantError("The tomato plant is wilting!")
    if (error_type == "water_error"):
        raise WaterError("Not enought ware in the tank!")
    if (error_type == "garden1"):
        raise PlantError("The tomato plant is wilting!")
    if (error_type == "garden2"):
        raise WaterError("Not enought ware in the tank!")


def main() -> None:
    """Entry point of the program."""
    print("=== Custom Garden Error Demo ===")
    print("Testing PlantError...")
    try:
        different_situations("plant_error")
        print("Testing WaterError...")
    except PlantError as e:
        print(e.get_message())
    try:
        different_situations("water_error")
        print("Testing catching all garden errors...")
    except WaterError as e:
        print(e.get_message())
    try:
        different_situations("garden1")
    except GardenError as e:
        print(e.get_message_cause())
    try:
        different_situations("garden2")
    except GardenError as e:
        print(e.get_message_cause())
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
