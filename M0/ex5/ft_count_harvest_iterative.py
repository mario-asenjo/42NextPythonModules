def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    for i in range(days):
        print(f"Day {i + 1}")
    print("Harvest time!")
