def ft_plant_age() -> None:
    days: int = int(input("Enter plant age in days: "))
    print("Plant is ready to harvest" if days > 60
          else "Plant needs more time to grow")
