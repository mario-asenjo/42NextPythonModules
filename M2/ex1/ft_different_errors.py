def garden_operations() -> None:
    """
    Tries to efectuate several operations that might fail, in each case
    if an error is encountered, the program handles it correctly.
    """
    try:
        print("\nTesting ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\nTesting ZeroDivisionError...")
        num: int = 25 // 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\nTesting FileNotFoundError...")
        open('missing.txt', 'r')
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print("\nTesting KeyError...")
        my_dict: dict[str, int] = {'plant1': 1}
        my_dict.pop('missing\\_plant')
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    try:
        print("\nTesting multiple errors together...")
        int("12")
        num: int = 12 // 3
        open("missing.txt")
        my_dict: dict[str, int] = {'plant1': num}
        my_dict.pop('plant1')
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    """
    Function to test all operations in garden
    """
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
