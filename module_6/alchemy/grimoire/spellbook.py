def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.validator import validate_ingredients

    result = validate_ingredients(ingredients)
    flag = result.split(" - ")
    if "VALID" in flag:
        s = f"Spell recorded: {spell_name} ({result})"
    else:
        s = f"Spell rejected: {spell_name} ({result})"
    return (s)
