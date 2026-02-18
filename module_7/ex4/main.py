from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n===DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        6,
        "dragon_001"
    )

    wizard = TournamentCard(
        "Ice Wizard",
        4,
        "Rare",
        4,
        5,
        "wizard_001"
    )

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    dragon_info = dragon.get_rank_info()
    wizard_info = wizard.get_rank_info()

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon_info['rating']}")
    print(f"- Record: {dragon_info['record']}")

    print(f"\n{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard_info['rating']}")
    print(f"- Record: {wizard_info['record']}")

    print("\nCreating tournament match...")

    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")

    leaderboard = platform.get_leaderboard()

    for entry in leaderboard:
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} "
            f"({entry['wins']}-{entry['losses']})"
        )

    print("\nPlatform Report:")

    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()
