class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age


    def age(self) -> int:
        return self._age


    def grow(self) -> None:
        self._height += 1
        self._age += 1


    def print_info(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    age: int = rose.age()
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
    print(f"Growth this week: +{rose.age() - age}cm")
