# decorator_mastery.py

import time
import functools

def spell_timer(func):
    """Time execution decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power):
    """Parameterized decorator to validate power levels"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(power, *args, **kwargs):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts):
    """Retry decorator for failed spells"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
                    if attempt == max_attempts:
                        return f"Spell casting failed after {max_attempts} attempts"
            return None
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate mage name: at least 3 chars, only letters/spaces"""
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)
    
    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """Cast a spell with validated power"""
        return f"Successfully cast {spell_name} with {power} power"


# Test it
if __name__ == "__main__":
    # Test spell_timer
    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"
    
    print("Testing spell timer...")
    print(fireball())
    
    # Test MageGuild
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))  # True
    print(guild.validate_mage_name("A"))        # False
    print(guild.validate_mage_name("Gandalf123"))  # False
    
    # Test cast_spell with validator
    print(guild.cast_spell(15, "Lightning"))    # Valid
    print(guild.cast_spell(5, "Spark"))         # Invalid
    
    # Test retry_spell
    @retry_spell(max_attempts=3)
    def unstable_spell():
        import random
        if random.random() < 0.7:  # 70% chance of failure
            raise ValueError("Spell misfired!")
        return "Spell succeeded!"
    
    print("\nTesting retry spell...")
    print(unstable_spell())