"""
Demonstration on decorator creation and usage
"""
import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """
    Decorator that measures the execution time of a spell
    :param func: The spell to be executed
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """
    Decorator factory that validates the first argument as power
    :param min_power: The power to check for the function to be called
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None:
                if len(args) >= 1 and isinstance(args[0], int):
                    power = args[0]
                elif len(args) >= 3 and isinstance(args[2], int):
                    power = args[2]
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """
    Decorator factory that retries a spell if it raises an exception
    :param max_attempts: Attempts to be made at most
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying..."
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
        return wrapper
    return decorator


class MageGuild:
    """Represent a guild of mages"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Return True if name is at least 3 chars and only letters/spaces
        """
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Cast a spell if enough power is available
        """
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Example spell used to demonstrate timing"""
    time.sleep(0.1)
    return "Fireball cast!"


def unstable_spell_factory(success_on_attempt: int) -> Callable[[], str]:
    """Create a spell that succeeds on a specific attempt"""
    attempts = 0

    @retry_spell(3)
    def unstable_spell() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < success_on_attempt:
            raise RuntimeError("Spell Failed")
        return "Waaaaaagh spelled !"

    return unstable_spell


def main() -> None:
    """Demonstrate all required decorators and MageGuild class"""
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")
    print("\nTesting retrying spell...")
    always_fail_spell = unstable_spell_factory(10)
    print(always_fail_spell())
    eventually_successful_spell = unstable_spell_factory(3)
    print(eventually_successful_spell())
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
