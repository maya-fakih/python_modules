from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:\n")

    try:
        creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

        print("CreatureCard Info:")
        info = creature.get_card_info()
        print(info)
        print()

        print("Playing Fire Dragon with 6 mana available:")
        print(f"Playable: {creature.is_playable(6)}")
        play_result = creature.play({})
        print(f"Play result: {play_result}")
        print()

        print("Fire Dragon attacks Goblin Warrior:")
        attack_result = creature.attack_target("Goblin Warrior")
        print(f"Attack result: {attack_result}")
        print()

        print("Testing insufficient mana (3 available):")
        print(f"Playable: {creature.is_playable(3)}")
        print()

        print("Abstract pattern successfully demonstrated!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
