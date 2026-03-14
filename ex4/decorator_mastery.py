import time
import functools
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    # @wraps(func) copies the name, docstring etc from the original
    # Without it, all decorated functions would be called "wrapper"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        elapsed = end - start
        print(f"Spell completed in {round(elapsed, 3)} seconds")

        return result
    return wrapper


# ─── power_validator ─────────────────────────────────────────────
# A decorator FACTORY — it takes min_power as argument and
# returns a decorator. This requires 3 levels of nesting:
# level 1: power_validator(min_power) → takes the argument
# level 2: decorator(func) → takes the function to wrap
# level 3: wrapper(*args, **kwargs) → the actual wrapped execution

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# ─── main ────────────────────────────────────────────────────────

def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power_validator...")

    @power_validator(min_power=20)
    def ice_blast(power: int, target: str) -> str:
        return f"Ice blast ({power}) hits {target}!"

    print(ice_blast(30, "dragon"))
    print(ice_blast(10, "dragon"))

    # Test retry_spell
    print("\nTesting retry_spell...")

    attempt_count = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise ValueError("Spell unstable!")
        return "Spell finally succeeded!"

    print(unstable_spell())

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Alice"))
    print(MageGuild.validate_mage_name("Al"))
    print(MageGuild.validate_mage_name("Al3x"))

    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))


if __name__ == "__main__":
    main()
