"""Entry-point for Module 1 exercise 4

Secure the access to members inside Plant class.
"""
class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        """Initialize a Plant with name, height and age."""
        self._name = name.capitalize()
        self._height = height
        self._age = age
        print(f"Plant created: {self._name}")


    def get_age(self) -> int:
        """Getter for age attribute"""
        return self._age


    def set_age(self, age: int) -> None:
        """Setter for age, handles invalid numbers as negative numbers"""
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")


    def get_height(self):
        """Getter for height attribute"""
        return self._height


    def set_height(self, height: int) -> None:
        """Setter for height attribute, handles invalid numbers
           as negative numbers
        """
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def grow(self) -> None:
        """Simulates a full day growth on a Plant."""
        self._height += 1
        self._age += 1


    def print_info(self) -> None:
        """Prints basic info of the plant created."""
        print(f"Current plant: {self._name} ({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: SecurePlant = SecurePlant("Rose", 0, 0)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.print_info()
