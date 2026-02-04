def method_1():
    print("Method 1 - Full module import:")
    import alchemy.elements
    fire = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire}\n")


def method_2():
    print("Method 2 - Specific function import:")
    from alchemy.elements import create_water
    water = create_water()
    print(f"create_water: {water}\n")


def method_3():
    print("Method 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    healing = heal()
    print(f"heal(): {healing}\n")


def method_4():
    print("Method 4 - Multiple imports:")
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    earth = create_earth()
    fire = create_fire()
    strength = strength_potion()
    print(f"create_earth(): {earth}")
    print(f"create_fire(): {fire}")
    print(f"strength_potion(): {strength}\n")


def test_2():
    print("\n=== Import Transmutation Mastery ===\n")

    method_1()

    method_2()

    method_3()

    method_4()

    print("All import transmutation methods mastered!")


if __name__ == '__main__':
    test_2()
