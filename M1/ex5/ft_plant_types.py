class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def	get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self):
        return self._height

    def set_height(self, height: int) -> None:
        if (height < 0):
            print(
                f"\nInvalid operation attempted: height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def grow(self) -> None:
        self._height += 1
        self._age += 1

    def get_info(self, name: str | None = None) -> str:
        return f"{self._name} ({name}): {self._height}cm, {self._age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.get_info("Flower")}, {self.color} color")

    def bloom(self):
        print(f"{self._name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.trunk_diameter: int = self.get_height() // 10
        print(f"{self.get_info("Tree")}, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        area: int = 3.1416 * (self.trunk_diameter // 10) **2
        print(f"{self._name} provides {area.__floor__()} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.get_info("Vegetable")}, {self.harvest_season} harvest")

    def print_nutritional_value(self):
        print(f"{self.get_name()} is rich in {self.nutritional_value}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose: Flower = Flower("rose", 25, 30, "red")
    tulip: Flower = Flower("tulip", 40, 40, "blue")
    rose.bloom()
    tulip.bloom()

    oak: Tree = Tree("oak", 500, 1825)
    spurse: Tree = Tree("spurse", 500, 1825)
    oak.produce_shade()
    spurse.produce_shade()

    tomato: Vegetable = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    lettuce: Vegetable = Vegetable("lettuce", 80, 90, "summer", "vitamin C")
    tomato.print_nutritional_value()
    lettuce.print_nutritional_value()
