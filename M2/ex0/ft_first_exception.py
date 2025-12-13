def check_temperature(temp_str: str) -> int | None:
    try:
        num: int = int(temp_str)
        print(
            f"Error: {num}ºC is too cold for plants (min 0ºC)" if num < 0 else
            f"Error {num}ºC is too hold for plants (max 40ºC)" if num > 40
            else f"Temperature {num}ºC is perfect for plants!"
        )
        return num if 0 <= num <= 40 else None
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number.")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
