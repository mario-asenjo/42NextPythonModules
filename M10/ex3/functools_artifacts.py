"""
Demonstration of different approaches to complex problems using functools
"""

from collections.abc import Callable
from functools import reduce, partial, singledispatch
from operator import add, mul
from typing import Any

from anyio.functools import lru_cache


def spell_reducer(spells: list[int], operation: str) -> int:
    """

    :param spells:
    :param operation:
    :return:
    """
    if not spells:
        return 0

    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """

    :param base_enchantment:
    :return:
    """
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """

    :param n:
    :return:
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """

    :return:
    """
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def enchant(power: int, element: str, target: str) -> str:
    """

    :param power:
    :param element:
    :param target:
    :return:
    """
    return f"{element.capitalize()} enchantment cast on {target} with {power} power"


def main() -> None:
    """Main program CLI entrypoint for demonstration"""
    print("Testing spell reducer...")
    spell_powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(enchant)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))
    print(enchanters["lightning"]("Staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fireball", "heal", "shield"]))
    print(dispatch({"type": "mystery"}))


if __name__ == "__main__":
    main()
