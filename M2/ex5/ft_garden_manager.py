"""
Garden Management System demonstrating all error handling techniques
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

class GardenManager:
    """
    Garden manager which allows to add plants, water them and check their
    health using error handling techniques.
    """
    def __init__(self) -> None:
        """Creates a manager with no plants"""
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        """Tries to add a plant and prints a message upon success"""
        if plant_name == "":
            raise PlantError("Error adding a plant: Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        """
        Function that recieves a list of plant names, and prints
        Watering and the name of each plant, in case a name is None
        the function raises ValueError.
        """
        print("Opening watering system...")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError()
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self,
            plant_name: str | None = None,
            water_level: int | None = None,
            sunlight_hours: int | None = None
    ) -> str | None:
        """
        Function to check the plant_name, water_level and sunlight_hours,
        in case any value is wrong, raises ValueError with specific message
        """
        if plant_name is not None and plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        if water_level is not None and water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if water_level is not None and water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours is not None and sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours is not None and sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
        print(f"{plant_name} healthy (water: {water_level}, sun: {sunlight_hours})")

    def tank_failure_sim(self) -> None:
        """Simulates a water tank with not enough water failing"""
        raise WaterError("Not enought water in the tank")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    manager: GardenManager = GardenManager()
    print("\nAdding plants to garden...")
    for p_name in ["tomato", "lettuce", ""]:
        try:
            manager.add_plant(p_name)
        except PlantError as p_error:
            print(p_error)
    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as w_error:
        print(w_error)
    print("\nChecking plant health...")
    for p_name in ["tomato", "lettuce"]:
        try:
            manager.check_plant_health(p_name,
                                       5 if p_name == "tomato" else 15,
                                       8)
        except PlantError as p_error:
            print(f"Error checking {p_name}:", p_error)
    print("\nTesting error recovery...")
    try:
        manager.tank_failure_sim()
    except GardenError as e:
        print("Caught GardenError:", e)
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")