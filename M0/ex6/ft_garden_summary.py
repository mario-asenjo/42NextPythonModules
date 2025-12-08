def _print_info(name: str, number: int) -> None:
    print("Garden:", name)
    print("Plants:", number)
    print("Status: Growing well!")


def ft_garden_summary() -> None:
    garden_name: str = input("Enter garden name: ")
    number_of_plants: int = int(input("Enter number of plants: "))
    _print_info(garden_name, number_of_plants)
