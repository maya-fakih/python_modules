def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args: (spell1(*args), spell2(*args))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args: base_spell(*args) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args: [s(*args) for s in spells]


if __name__ == '__main__':
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def get_damage(target):
        return 10

    def is_dragon(target):
        return target == "Dragon"

    print("Testing spell combiner:")
    combo = spell_combiner(fireball, heal)
    print(f"new combo: {combo("dragon")}")

    print("\n")

    print("testing aplifier:")
    amp = power_amplifier(get_damage, 10)
    print(f"amplified damage: {amp('Ghoblin')}")

    print("\n")

    print("test conditional caster:")
    dragon_slayer = conditional_caster(is_dragon, fireball)
    print(f"Against Dragon: {dragon_slayer('Dragon')}")
    print(f"Against Goblin: {dragon_slayer('Goblin')}")

    print("\n")

    print("testing spell sequence...")
    listed = [fireball, heal, fireball]
    sequence = spell_sequence(listed)
    print(sequence("me"))
