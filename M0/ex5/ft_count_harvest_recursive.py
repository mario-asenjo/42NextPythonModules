def _recursive_call(n: int) -> None:
    if n != 1:
        _recursive_call(n - 1)
    print(f"Day {n}")


def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    _recursive_call(days)
    print("Harvest time!")
