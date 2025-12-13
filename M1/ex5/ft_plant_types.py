"""Entry-point program for Module 1 exercise 5

Specialized plant types in the garden!
"""


class Plant:
    """Base Plant class with basic info and getters and setters for
       age and height and also a method to retrieve basic info"""
    def __init__(self, name: str, height: int, age: int):
        """Initializes a Plant with name, height and age"""
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def get_name(self) -> str:
        """Getter for name attribute"""
        return self._name

    def get_age(self) -> int:
        """Getter for age attribute"""
        return self._age

    def set_age(self, age: int) -> None:
        """Setter with validations for age attribute"""
        if (age < 0):
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self) -> int:
        """Getter for height attribute"""
        return self._height

    def set_height(self, height: int) -> None:
        """Setter with validations for height attribute"""
        if height < 0:
            print(
                f"\nInvalid operation attempted: height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def grow(self) -> None:
        """Simulates a full day of growth"""
        self._height += 1
        self._age += 1

    def get_info(self, name: str | None = None) -> str:
        """Retrieves basic info of a plant"""
        return f"{self._name} ({name}): {self._height}cm, {self._age} days"


class Flower(Plant):
    """Flower class inherits Plant so all of its data belongs to Flower too"""
    def __init__(self, name: str, height: int, age: int, color: str):
        """Initializes a Plant with name, height and age, then sets color for
           the Flower
        """
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.get_info('Flower')}, {self.color} color")

    def bloom(self):
        """Prints the blooming of the Flower"""
        print(f"{self._name} is blooming beautifully!\n")


class Tree(Plant):
    """Tree class inherits Plant so all of its data belongs to Tree too"""
    def __init__(self, name: str, height: int, age: int):
        """Initializes a Plant with name, height and age, then sets
           trunk_diameter for the Tree.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = self.get_height() // 10
        print(f"{self.get_info('Tree')}, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        """Prints the shade this tree would produce"""
        radius: int = self.trunk_diameter // 10
        area: int = 31416 * radius**2
        print(
            f"{self._name} provides {area // 10000} square meters of shade\n"
        )


class Vegetable(Plant):
    """
    Vegetable class inherits Plant so all of its data belongs to Vegetable
    """
    def __init__(
            self, name: str, height: int,
            age: int, harvest_season: str, nutritional_value: str):
        """Initializes a Plant with name, height and age, then sets the
           harvest_season and nutritional values for Vegetable
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.get_info('Vegetable')}, {self.harvest_season} harvest")

    def print_nutritional_value(self):
        """Prints the nutritional value of the Vegetable"""
        print(f"{self.get_name()} is rich in {self.nutritional_value}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose: Flower = Flower("rose", 25, 30, "red")
    tulip: Flower = Flower("tulip", 40, 40, "blue")
    rose.bloom()
    tulip.bloom()

    oak: Tree = Tree("oak", 500, 1825)
    sparse: Tree = Tree("sparse", 500, 1825)
    oak.produce_shade()
    sparse.produce_shade()

    tomato: Vegetable = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    lettuce: Vegetable = Vegetable("lettuce", 80, 90, "summer", "vitamin C")
    tomato.print_nutritional_value()
    lettuce.print_nutritional_value()
