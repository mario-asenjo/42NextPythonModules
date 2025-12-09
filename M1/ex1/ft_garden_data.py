"""Entry-point program for Module 1 exercise 1

Initialize 3 Plants and show their basic info.
"""
class Plant:
    """Plant class containing, name, height and age"""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a Plant with a name, heigh and age."""
        self.name = name
        self.height = height
        self.age = age


    def print_info(self) -> None:
        """Prints basic info about the plant created"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()
