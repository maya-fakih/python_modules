from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main():
    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    ing1 = "fire air"
    ing2 = "dragon scales"
    check = "validate_ingredients"
    print(f"{check}({ing1}): {validate_ingredients(ing1)}")
    print(f"{check}({ing2}): {validate_ingredients(ing2)}")

    print("\nTesting spell recording with validation:")
    n1 = "Fireball"
    in1 = "fire air"
    n2 = "Dark Magic"
    in2 = "shadow"
    check = "record_spell"
    print(f"{check}({n1}, {in1}): {record_spell(n1, in1)}")
    print(f"{check}({n2}, {in2}): {record_spell(n2, in2)}")

    print("\nTesting late import technique:")
    n3 = "Lightning"
    in3 = "air"
    print(f"{check}({n3}, {in3}): {record_spell(n3, in3)}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == '__main__':
    main()
