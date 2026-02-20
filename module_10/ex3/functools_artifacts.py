import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": functools.partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": functools.partial(base_enchantment, power=50, element="lightning")
    }

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatcher(spell):
        return "Unknown spell"

    @dispatcher.register(int)
    def _(spell):
        return f"Damage spell: {spell}"

    @dispatcher.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


if __name__ == "__main__":
    powers = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")
    def base_enchant(target, power=0, element=""):
        return f"{element.capitalize()} {target} (Power: {power})"
    
    enchanters = partial_enchanter(base_enchant)
    print(enchanters['fire_enchant']("Sword"))
    print(enchanters['ice_enchant']("Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nwell dispatching")
    dispatch = spell_dispatcher()
    print(dispatch(100))
    print(dispatch("Fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(5.5)) 