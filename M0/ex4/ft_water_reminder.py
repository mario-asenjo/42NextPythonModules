def ft_water_reminder() -> None:
    days: int = int(input("Days since last watering: "))
    print("Water the plants!" if days > 2 else "Plants are fine")
