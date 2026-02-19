*This project has been created as part of the 42 curriculum by mfakih.*

FuncMage: Functional Programming Mastery
A journey through Python's functional programming paradigms

Overview
Five exercises that progressively build mastery in functional programming concepts, from basic lambdas to advanced decorators and closures.

Exercise 0: Lambda Sanctum - lambda_spells.py
Core concept: Anonymous functions for quick transformations

Function	What it does	Lambda used for
artifact_sorter()	Sort artifacts by power	key=lambda x: x['power']
power_filter()	Filter mages by min power	filter(lambda m: m['power'] >= min_power)
spell_transformer()	Format spell names	map(lambda s: f"* {s} *")
mage_stats()	Calculate power stats	map() + max/min/sum
Lambda syntax: lambda args: expression (no return needed)

Exercise 1: Higher Realm - higher_magic.py
Core concept: Functions that return functions (higher-order functions)

Function	What it returns	Example usage
spell_combiner()	Function that calls two spells	combined = spell_combiner(fire, heal)
power_amplifier()	Function that multiplies result	mega = power_amplifier(damage, 3)
conditional_caster()	Function that checks condition first	conditional = conditional_caster(is_powerful, spell)
spell_sequence()	Function that runs multiple spells	sequence = spell_sequence([spell1, spell2])
Key insight: Functions are first-class citizens — can be passed around like variables

Exercise 2: Memory Depths - scope_mysteries.py
Core concept: Closures — functions that remember their creation environment

Function	What it remembers	Key keyword
mage_counter()	Call count between invocations	nonlocal count
spell_accumulator()	Running total of power	nonlocal total
enchantment_factory()	Enchantment type string	closure capture
memory_vault()	Private memory dictionary	closure + returned functions
Closure pattern:

python
def outer(x):
    def inner(y):
        return x + y  # inner "remembers" x
    return inner
nonlocal = allows modifying captured variables (not just reading them)

Exercise 3: Ancient Library - functools_artifacts.py
Core concept: Built-in functional programming tools

Tool	Function	Purpose
reduce()	spell_reducer()	Combine all values into one
partial()	partial_enchanter()	Pre-fill some arguments
lru_cache	memoized_fibonacci()	Cache results for performance
singledispatch	spell_dispatcher()	Function overloading by type
Key imports: functools, operator

Memoization magic:

python
@functools.lru_cache(maxsize=None)
def fib(n):
    # Results cached automatically
Exercise 4: Master's Tower - decorator_mastery.py
Core concept: Decorators — functions that modify other functions

Decorator	What it adds	Type
@spell_timer	Execution time logging	Simple decorator
@power_validator(min_power)	Power validation	Parameterized decorator
@retry_spell(max_attempts)	Retry on failure	Parameterized decorator
@staticmethod	Class method without self	Built-in
Decorator pattern:

python
def decorator(func):
    @functools.wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper
@staticmethod vs instance method:

@staticmethod: No self access, utility function in class namespace

Instance method: Has self, can access/modify instance

Quick Reference
Functional Programming Toolbox
Concept	Module	Use case
Lambda	builtins	Quick one-liners
Map/Filter	builtins	Transform/filter collections
Reduce	functools	Aggregate collections
Partial	functools	Fix function arguments
LRU Cache	functools	Memoization
Single Dispatch	functools	Type-based dispatch
Closures	builtins	Stateful functions
Decorators	builtins	Function modification
Progression Path
Lambda → transform data

Higher-order → transform functions

Closures → functions with memory

Functools → battle-tested tools

Decorators → ultimate function power