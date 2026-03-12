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
