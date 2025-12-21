"""
Program that shows the use of dictionaries data structures.
"""


def get_categories_info(inventory: dict) -> str:
    ret: list[str] = []
    for key in  inventory.keys():
        ret.append(key + f"({inventory.get(key).get("qty")})")
    return "".join(val+(", " if val != ret[-1] else "") for val in ret)


def print_inventory_info(inventory: dict) -> None:
    total_items: int = 0
    total_value: int = 0
    categories: dict = {}
    for g_ob in inventory.items():
        sub_dict: dict = g_ob[1]
        print(
            f"{g_ob[0]} ({sub_dict.get("category")},"
            f"{sub_dict.get("rarity")}): "
            f"{sub_dict.get("qty")}x @ {sub_dict.get("value")} gold each"
            f" = {sub_dict.get("qty") * sub_dict.get("value")} gold"
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
    if inv_from.get("potion").get("qty") < qty:
        return False
    inv_from["potion"]["qty"] -= qty
    try:
        inv_to["potion"]["qty"] += qty
    except KeyError:
        inv_to["potion"] = {"qty" : qty, "value" : 50, "category" : "consumable", "rarity" : "common"}
    return True

def main() -> None:
    alice_inventory: dict = {
        "sword" : {"qty" : 1, "value" : 500, "category" : "weapon", "rarity" : "rare"},
        "potion" : {"qty" : 5, "value" : 50, "category" : "consumable", "rarity" : "common"},
        "shield" : {"qty" : 1, "value" : 200, "category" : "armor", "rarity" : "rare"}
    }
    bob_inventory: dict = {
        "axe" : {"qty" : 1, "value" : 80, "category" : "weapon", "rarity" : "common"},
        "magic_ring": {"qty" : 1, "value" : 200, "category" : "armor", "rarity" : "rare"}
    }
    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")
    print_inventory_info(alice_inventory)
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successful!" if transfer_potions(alice_inventory, bob_inventory, 2)
          else "Transaction unsuccessful!")
    print("\n=== Updated Inventories ===")
    print("Alice potions:", alice_inventory["potion"].get("qty"))
    print("Bob potions:", bob_inventory["potion"].get("qty"))
    print("\n=== Inventory Analysis ===")
    



if __name__ == "__main__":
    main()