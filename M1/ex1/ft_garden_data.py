"""Entry-point program for Module 1 exercise 1

Initialize 3 Plants and show their basic info.
"""


class Plant:
    """Plant class containing, name, height and age"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant with a name, heigh and age."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


    def get_info(self, name: str | None = None) -> str:
        """Retrieves basic info of a plant"""
        return f"{self._name} ({name}): {self._height}cm, {self._age} days"


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(rose.get_info())
    print(sunflower.get_info())
    print(cactus.get_info())
