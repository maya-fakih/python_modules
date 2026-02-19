# functools_artifacts.py

import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spells using specified operation"""
    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }
    
    if operation in ['add', 'multiply']:
        return functools.reduce(ops[operation], spells)
    else:
        return ops[operation](spells)


def partial_enchanter(base_enchantment):
    """Create partial applications for different elements"""
    elements = ['fire', 'ice', 'lightning']
    
    return {
        f'{elem}_enchant': functools.partial(base_enchantment, power=50, element=elem)
        for elem in elements
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate fibonacci with memoization"""
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher():
    """Create single dispatch function for spells"""
    @functools.singledispatch
    def cast_spell(arg):
        return f"Unknown spell type: {type(arg)}"
    
    @cast_spell.register(int)
    def _(arg):
        return f"Damage spell: {arg} points"
    
    @cast_spell.register(str)
    def _(arg):
        return f"Enchantment spell: {arg}"
    
    @cast_spell.register(list)
    def _(arg):
        return f"Multi-cast: {', '.join(str(x) for x in arg)}"
    
    return cast_spell


# Test it
if __name__ == "__main__":
    # Test spell_reducer
    spells = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    
    # Test memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")
    
    # Test partial_enchanter
    def enchant(power, element, target):
        return f"{element.upper()} {target} with power {power}"
    
    enchanters = partial_enchanter(enchant)
    print("\nTesting partial enchanter...")
    print(enchanters['fire_enchant'](target="Dragon"))
    print(enchanters['ice_enchant'](target="Frozen"))
    
    # Test spell_dispatcher
    dispatcher = spell_dispatcher()
    print("\nTesting spell dispatcher...")
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))