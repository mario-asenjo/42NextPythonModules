"""
Program that shows the use of dictionaries data structures.
"""


def get_categories_info(inventory: dict) -> str:
    """Returns comma separated categories info of the inventory received"""
    ret: list[str] = []
    for key in inventory.keys():
        ret.append(key + f"({inventory.get(key).get('qty')})")
    return ", ".join(val for val in ret)


def print_inventory_info(inventory: dict) -> None:
    """Prints the inventory received with a specified format"""
    total_items: int = 0
    total_value: int = 0
    categories: dict = {}
    for g_ob in inventory.items():
        sub_dict: dict = g_ob[1]
        print(
            f"{g_ob[0]} ({sub_dict.get('category')}, "
            f"{sub_dict.get('rarity')}): "
            f"{sub_dict.get('qty')}x @ {sub_dict.get('value')} gold each"
            f" = {sub_dict.get('qty') * sub_dict.get('value')} gold"
        )
        total_items += sub_dict.get("qty")
        total_value += sub_dict.get("qty") * sub_dict.get("value")
        categories[sub_dict.get("category")] = sub_dict.get("qty")
    print(
        f"\nInventory value: {total_value} gold"
        f"\nItem count: {total_items} items"
        f"\nCategories: {get_categories_info(inventory)}"
    )


def transfer_potions(inv_from: dict, inv_to: dict, qty: int) -> bool:
    """Function to transfer potions from one inventory to another"""
    if inv_from.get("potion").get("qty") < qty:
        return False
    inv_from["potion"]["qty"] -= qty
    try:
        inv_to["potion"]["qty"] += qty
    except KeyError:
        inv_to["potion"] = {
            "qty": qty,
            "value": 50,
            "category": "consumable",
            "rarity": "common"
        }
    return True


def most_valuable_info(inventories: dict) -> str:
    """
    Returns a format with information of the most
    valuable player in the inventory given
    """
    player_name: str = ""
    value: int = 0
    for name in inventories.keys():
        calc_val: int = 0
        inv: dict = inventories.get(name)
        for obj in inv.keys():
            attr: dict = inv.get(obj)
            calc_val += attr.get("qty") * attr.get("value")
            if calc_val > value:
                value = calc_val
                player_name = name
    return f"{player_name.capitalize()} (%d gold)" % value


def most_items_info(inventories: dict) -> str | None:
    """
    Returns a format with information of the
    player with most items in the inventory received
    """
    player_name: str = ""
    items: int = 0
    for name in inventories.keys():
        calc_val: int = 0
        inv: dict = inventories.get(name)
        for obj in inv.keys():
            attr: dict = inv.get(obj)
            calc_val += attr.get("qty")
            if calc_val > items:
                items = calc_val
                player_name = name
        return f"{player_name.capitalize()} (%d items)" % items
    return None


def retrieve_rarest_items(inventories: dict) -> str:
    """Retrieves a format with the rarest items on the inventory received"""
    rarest_objects: list[str] = []
    for name in inventories.keys():
        inv: dict = inventories.get(name)
        for obj in inv.keys():
            attr: dict = inv.get(obj)
            if attr.get("rarity") == "rare":
                rarest_objects.append(obj)
    return ", ".join(
        obj for obj in rarest_objects
    )


def main() -> None:
    """Main function of the program that generates data and calls functions"""
    alice_inventory: dict = {
        "sword": {
            "qty": 1,
            "value": 500,
            "category": "weapon",
            "rarity": "rare"
        },
        "potion": {
            "qty": 5,
            "value": 50,
            "category": "consumable",
            "rarity": "common"
        },
        "shield": {
            "qty": 1,
            "value": 200,
            "category": "armor",
            "rarity": "uncommon"
        }
    }
    bob_inventory: dict = {
        "axe": {
            "qty": 1,
            "value": 80,
            "category": "weapon",
            "rarity": "common"
        },
        "magic_ring": {
            "qty": 1,
            "value": 200,
            "category": "armor",
            "rarity": "rare"
        }
    }
    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")
    print_inventory_info(alice_inventory)
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successful!"
          if transfer_potions(alice_inventory, bob_inventory, 2)
          else "Transaction unsuccessful!")
    print("\n=== Updated Inventories ===")
    print("Alice potions:", alice_inventory["potion"].get("qty"))
    print("Bob potions:", bob_inventory["potion"].get("qty"))
    inventories: dict = {"alice": alice_inventory, "bob": bob_inventory}
    print("\n=== Inventory Analysis ===")
    print("Most valuable player:", most_valuable_info(inventories))
    print("Most items:", most_items_info(inventories))
    print("Rarest items:", retrieve_rarest_items(inventories))


if __name__ == "__main__":
    main()
