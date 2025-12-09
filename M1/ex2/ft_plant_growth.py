"""Entry-point program for Module 1 exercise 2

Simulation of plant growth ovew an entire week.
"""
class Plant:
    """Base class for a Plant with name, height and age"""
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def age(self) -> int:
        """Getter for age attribute"""
        return self._age

    def height(self) -> int:
        """Getter for height attribute"""
        return self._height

    def grow(self) -> None:
        """Simulates the growth of a full day."""
        self._height += 1
        self._age += 1

    def print_info(self) -> None:
        """Prints info about the plant created."""
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    height: int = rose.height()
    print("=== Day 1 ===")
    rose.print_info()
    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()
    print("=== Day 7 ===")
    rose.print_info()
    print(f"Growth this week: +{rose.height() - height}cm")
