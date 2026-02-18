from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Legendary",
        power=5,
        health=8,
        mana=6,
        spells=["Fireball", "Heal", "Shield"]
    )

    enemy = EliteCard(
        name="Dark Knight",
        cost=4,
        rarity="Rare",
        power=4,
        health=6,
        mana=4,
        spells=["Lightning"]
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {arcane_warrior.name} (Elite Card):")

    # play_result = arcane_warrior.play(game_state)
    # print(f"Play result: {play_result}")

    print("\nCombat phase:")
    attack_result = arcane_warrior.attack(enemy)
    print(f"Attack result: {attack_result}")

    defend_result = arcane_warrior.defend(3)
    print(f"Defense result: {defend_result}")

    # combat_stats = arcane_warrior.get_combat_stats()
    # print(f"Combat stats: {combat_stats}")

    print("\nMagic phase:")
    spell_result = arcane_warrior.cast_spell("Fireball", [enemy])
    print(f"Spell cast: {spell_result}")

    # channel_result = arcane_warrior.channel_mana(3)
    # print(f"Mana channel: {channel_result}")

    magic_stats = arcane_warrior.get_magic_stats()
    print(f"Magic stats: {magic_stats}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
