def ft_harvest_total() -> None:
    total: int = 0
    for i in 0, 1, 2:
        total += int(input(f"Day {i + 1} harvest: "))
    print("Total harvest:", total)
