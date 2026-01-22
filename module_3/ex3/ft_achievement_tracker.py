class Player():
    def __init__(self, name: str):
        self.name = name
        self.achievements = set()

    def add_achievement(self, achievement: set[str]):
        self.achievements.update(achievement)


def main():
    print("=== Achievement Tracker System ===\n")

    players = []

    player1 = Player("alice")
    player2 = Player("bob")
    player3 = Player("charlie")
    players.append(player1)
    players.append(player2)
    players.append(player3)

    a1 = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    a2 = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    a3 = (
        set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
             'perfectionist'])
    )
    player1.add_achievement(a1)
    player2.add_achievement(a2)
    player3.add_achievement(a3)

    for player in players:
        print(f"Player {player.name} achievements: {player.achievements}")

    print("\n=== Achievement Analysis ===")
    unique_achievements = a1.union(a2).union(a3)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    common = a1.intersection(a2).intersection(a3)
    i = (a1.intersection(a2) | a2.intersection(a3) | a1.intersection(a3))
    rare = (unique_achievements - i)
    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements (only one player): {rare}")

    print("\n=== Alice VS Bob ===")
    print(f"{player1.name.capitalize()} vs {player2.name.capitalize()} common:\
        {a1.intersection(a2)}")
    alice_unique = a1.difference(a2)
    bob_unique = a2.difference(a1)
    print(f"{player1.name.capitalize()} unique: {alice_unique}")
    print(f"{player2.name.capitalize()} unique: {bob_unique}")


if __name__ == '__main__':
    main()
