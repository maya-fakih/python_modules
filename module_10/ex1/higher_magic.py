def spell_combiner(spell1, spell2):
    """Combine two spells into one that returns both results"""
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell, multiplier):
    """Amplify spell result by multiplier"""
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition, spell):
    """Cast spell only if condition is True"""
    def conditional(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells):
    """Cast multiple spells and return all results"""
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


# Test it
if __name__ == "__main__":
    # Sample spells
    def fireball(target):
        return f"Fireball hits {target}"
    
    def heal(target):
        return f"Heals {target}"
    
    def damage_spell():
        return 10
    
    # Test spell_combiner
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")
    
    # Test power_amplifier
    amplified = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell()}, Amplified: {amplified()}")
    
    # Test conditional_caster
    def is_powerful(power):
        return power > 50
    
    def cast_spell(power):
        return f"Spell cast with power {power}"
    
    conditional = conditional_caster(is_powerful, cast_spell)
    print(f"Power 30: {conditional(30)}")
    print(f"Power 80: {conditional(80)}")
    
    # Test spell_sequence
    def spell1(x): return f"Spell1: {x}"
    def spell2(x): return f"Spell2: {x}"
    sequence = spell_sequence([spell1, spell2])
    print(f"Sequence result: {sequence('test')}")