"""Entry-point program of Module 1 exercise 3

Creation of several Plant and recording the ammount we created.
"""
class Plant:
    """Base Plant class with name, height and age, which records
       each time we create a new plant
    """
    total_plants_created: int = 0
    def __init__(self, name: str, height: int, age: int):
        self._name = name.capitalize()
        self._height = height
        self._age = age
        Plant.total_plants_created += 1
        print(f"Created: {self._name} ({self._height}cm, {self._age} days)")


    def age(self) -> int:
        """Getter for age attribute"""
        return self._age


    def grow(self) -> None:
        """Simulation of growth during a full day"""
        self._height += 1
        self._age += 1


    def get_info(self, name: str | None = None) -> str:
        """Retrieves basic info of a plant"""
        return f"{self._name} ({name}): {self._height}cm, {self._age} days"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose: Plant = Plant("Rose", 25, 30)
    oak: Plant = Plant("Oak", 200, 365)
    cactus: Plant = Plant("Cactus", 5, 90)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    fern: Plant = Plant("Fern", 15, 120)
    print(f"Total plants created: {Plant.total_plants_created}")
