from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined_spell(*args, **kwargs):
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiply_spell(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return multiply_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cond_cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"

    return cond_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_bulk(*args, **kwargs):
        lst = []
        for spell in spells:
            lst.append(spell(*args, **kwargs))
        return lst
    return spell_bulk


def main() -> None:

    print("Testing spell combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")

    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")

    def magic_bolt(power: int) -> int:
        return power

    original_result = magic_bolt(10)
    mega_bolt = power_amplifier(magic_bolt, 3)
    amplified_result = mega_bolt(10)

    print(f"Original: {original_result}, Amplified: {amplified_result}")

    print("\nTesting conditional caster...")

    def is_strong_enough(power: int) -> bool:
        return power >= 50

    def thunder(power: int) -> str:
        return f"Thunder strikes with {power} power!"

    safe_thunder = conditional_caster(is_strong_enough, thunder)

    print(safe_thunder(80))
    print(safe_thunder(20))

    print("\nTesting spell sequence...")

    def shield(target: str) -> str:
        return f"Shield covers {target}"

    def curse(target: str) -> str:
        return f"Curse hits {target}"

    def restore(target: str) -> str:
        return f"Restore heals {target}"

    full_combo = spell_sequence([fireball, shield, curse, restore])
    results = full_combo("Dragon")

    print("Sequence results:")
    for r in results:
        print(f"  {r}")


if __name__ == "__main__":
    main()
