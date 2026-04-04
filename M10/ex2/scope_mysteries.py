"""
Demonstration of lexical scoping and where the environment values persist
"""

from collections.abc import Callable

def mage_counter() -> Callable:
    """Return a closure that counts how many times it has been called"""
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a function that accumulates power over time"""
    total_power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    """Create enchantment functions"""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a private memory system with store and recall functions"""
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object | str:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    """Demonstrate all required closure behaviors"""
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall  'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
