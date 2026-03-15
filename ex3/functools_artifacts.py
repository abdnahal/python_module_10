from typing import Callable, List, Dict, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(lambda x, y: x if x > y else y, spells)
    elif operation == "min":
        return reduce(lambda x, y: x if x < y else y, spells)
    else:
        print("Invalid operator!")


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    fire_enchant = partial(base_enchantment, power=50, element="fire")
    ice_enchant = partial(base_enchantment, power=50, element="ice")
    lightning_enchant = partial(base_enchantment, power=50,
                                element="lightning")
    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(target: Any) -> str:
        return f"Unknown spell target type: {type(target)}"

    @cast.register(int)
    def _(target: int) -> str:
        return f"Damage spell: {target} points"

    @cast.register(str)
    def _(target: str) -> str:
        return f"Enchantment: {target}"

    @cast.register(list)
    def _(target: list) -> str:
        return f"Multi-cast on: {', '.join(t for t in target)}"

    return cast


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} enchantment \
(power {power}) on {target}"

    enchanters = partial_enchanter(base_enchantment)

    print(enchanters["fire_enchant"](target="Sword"))
    print(enchanters["ice_enchant"](target="Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(50))
    print(dispatcher("fireball"))
    print(dispatcher(["dragon", "goblin"]))


if __name__ == "__main__":
    main()
