def test_3():
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    gold = lead_to_gold()
    gem = stone_to_gem()
    print(f"lead_to_gold(): {gold}")
    print(f"stone_to_gem(): {gem}")

    print("\nTesting Relative Imports (from advanced.py):")
    from alchemy.transmutation.advanced import (philosophers_stone,
                                                elixir_of_life)
    stone = philosophers_stone()
    life = elixir_of_life()
    print(f"philosophers_stone(): {stone}")
    print(f"elixir_of_life(): {life}")

    print("\nTesting Package Access:")
    import alchemy.transmutation
    gold = alchemy.transmutation.lead_to_gold()
    stone2 = alchemy.transmutation.philosophers_stone()
    state = "[not the same]"
    if (stone == stone2):
        state = "[same as above]"
    print(f"alchemy.transmutation.lead_to_gold(): {gold}")
    print(f"alchemy.transmutation.philosophers_stone(): {state}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == '__main__':
    test_3()
