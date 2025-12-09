"""Entry-point program for Module 1 exercise 0.

Prints basic info about a plant in a garden.
"""
def main() -> None:
    """Main function, prints info about a single plant in a garden"""
    plant: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")

if __name__ == "__main__":
    main()