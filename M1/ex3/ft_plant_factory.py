class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name.capitalize()
        self._height = height
        self._age = age
        print(f"Created: {self._name} ({self._height}cm, {self._age} days)")


    def age(self) -> int:
        return self._age


    def grow(self) -> None:
        self._height += 1
        self._age += 1


    def print_info(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    oak: Plant = Plant("Oak", 200, 365)
    cactus: Plant = Plant("Cactus", 5, 90)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    fern: Plant = Plant("Fern", 15, 120)
    print("\nTotal plants created: 5")