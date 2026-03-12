import time
import functools
from typing import Callable


# ─── spell_timer ─────────────────────────────────────────────────
# A simple decorator that:
# 1. prints "Casting func_name..." before the function runs
# 2. records how long the function takes
# 3. prints the elapsed time after
# 4. returns the original result

def spell_timer(func: Callable) -> Callable:
    # @wraps(func) copies the name, docstring etc from the original
    # Without it, all decorated functions would be called "wrapper"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        # time.time() gives current timestamp in seconds
        start = time.time()
        result = func(*args, **kwargs)    # call the original function
        end = time.time()

        elapsed = end - start
        print(f"Spell completed in {round(elapsed, 3)} seconds")

        return result   # return what the original function returned
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
            # The first argument to the decorated function is power
            # args[0] gives us the first positional argument
            power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            # Power is sufficient — run the original function normally
            return func(*args, **kwargs)
        return wrapper
    return decorator   # power_validator returns the decorator


# ─── retry_spell ─────────────────────────────────────────────────
# Another decorator factory.
# If the wrapped function raises an exception, try again.
# Keep trying up to max_attempts times.

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    # Try to call the function
                    return func(*args, **kwargs)
                except Exception:
                    # It raised an exception — print retry message
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            # If we get here, all attempts failed
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


# ─── MageGuild ───────────────────────────────────────────────────
# Demonstrates @staticmethod and using a decorator on an instance method.

class MageGuild:

    # @staticmethod: no 'self' parameter.
    # This function doesn't need any instance data —
    # it just checks whether a name string is valid.
    # Can be called as MageGuild.validate_mage_name("Alice")
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        # Valid if: at least 3 chars AND only letters and spaces
        # .replace(" ", "") removes spaces before checking isalpha()
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    # Instance method using @power_validator(min_power=10)
    # When called, wrapper checks args[0] which is 'power'
    # Note: 'self' is args[0] in a method... BUT the decorator is
    # applied to the unbound function, so self is args[0] here.
    # We need to check args[1] (power) instead.

    # To handle this cleanly, we use **kwargs for power:
    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# ─── main ────────────────────────────────────────────────────────

def main() -> None:
    # Test spell_timer
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)    # simulate a spell taking time
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    # Test power_validator standalone
    print("\nTesting power_validator...")

    @power_validator(min_power=20)
    def ice_blast(power: int, target: str) -> str:
        return f"Ice blast ({power}) hits {target}!"

    print(ice_blast(30, "dragon"))   # passes: 30 >= 20
    print(ice_blast(10, "dragon"))   # fails: 10 < 20

    # Test retry_spell
    print("\nTesting retry_spell...")

    attempt_count = [0]   # use list to mutate inside closure

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise ValueError("Spell unstable!")
        return "Spell finally succeeded!"

    print(unstable_spell())

    # Test MageGuild
    print("\nTesting MageGuild...")

    # validate_mage_name is static — called on the class directly
    print(MageGuild.validate_mage_name("Alice"))   # True
    print(MageGuild.validate_mage_name("Al"))      # False (too short)
    print(MageGuild.validate_mage_name("Al3x"))    # False (has digit)

    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))  # passes: 15 >= 10
    print(guild.cast_spell(5, "Lightning"))   # fails: 5 < 10


if __name__ == "__main__":
    main()