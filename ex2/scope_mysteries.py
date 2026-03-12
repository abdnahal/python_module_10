from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power: int):
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanter(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault() -> dict[str, Callable]:
    dic = {}

    def store(key: Any, value: Any):
        dic[key] = value

    def recall(key: Any):
        return dic.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    my_mage_counter = mage_counter()

    for i in range(4):
        print(my_mage_counter())
    print()
    accumulator = spell_accumulator(5)

    for i in range(4):
        print(accumulator(10))
