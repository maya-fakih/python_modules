def lists(players):
    print("\n=== List Comprehension Examples ===")
    high_score = [n for n, s, _ in players if s > 2000]
    scores_doubled = [s * 2 for _, s, _ in players]
    active_players = [n for n, _, a in players if a is True]

    print(f"High scores: {high_score}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")


def dicts(players, achievments):
    print("\n=== Dict Comprehension Examples ===")
    player_dict = {n: s for n, s, a in players if a is True}
    score_category = {}
    a_count = {}

    for _, score in player_dict.items():
        if (score < 2000):
            c = "low"
        elif (score < 2200):
            c = "medium"
        else:
            c = "high"
        score_category[c] = score_category.get(c, 0) + 1

    for name, _ in achievments:
        a_count[name] = a_count.get(name, 0) + 1

    print(f"Player scores: {player_dict}")
    print(f"Score categories: {score_category}")
    print(f"Achievment counts: {a_count}")


def combined_analysis(players, achievements):
    print("\n=== Combined Analysis ===")
    total_players = len(players)
    unique_a = {a for _, a in achievements}
    total_a = len(unique_a)
    scores = [s for _, s, _ in players]
    avg_scores = sum(scores) / len(scores)
    t_s = max(scores)
    player = {s: n for n, s, _ in players}
    t_p = player[t_s]
    t_a = 0
    for n, _ in achievements:
        if n == t_p:
            t_a += 1
    print(f"Total players: {total_players}")
    print(f"Total unique achievments: {total_a}")
    print(f"Avarage score: {avg_scores}")
    print(f"Top performer: {t_p} ({t_s} points, {t_a} achievements)")


def sets(achievements):
    print("\n=== Set Comprehension Examples ===")

    player_regions = [
        ("alice", "north"),
        ("bob", "east"),
        ("charlie", "central"),
        ("diana", "north"),
        ("alice", "east")
    ]
    unique_name = {name for name, _ in achievements}
    unique_achievements = {a for _, a in achievements}
    unique_regions = {region for _, region in player_regions}
    print(f"Unique players: {unique_name}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {unique_regions}")


def main():
    print("=== Game Analytics Dashboard ===")

    achievements = [
        ("alice", "killed boss"),
        ("alice", "found treasure"),
        ("alice", "leveled up"),
        ("alice", "completed quest"),
        ("alice", "explored dungeon"),
        ("bob", "killed boss"),
        ("bob", "found treasure"),
        ("bob", "leveled up"),
        ("charlie", "killed boss"),
        ("charlie", "found treasure"),
        ("charlie", "leveled up"),
        ("charlie", "completed quest"),
        ("charlie", "explored dungeon"),
        ("charlie", "defeated boss"),
        ("charlie", "crafted item")
    ]

    players = [
        ("alice", 2300, True),
        ("charlie", 2150, True),
        ("diana", 2050, False),
        ("bob", 1800, True)
    ]

    lists(players)

    dicts(players, achievements)

    sets(achievements)

    combined_analysis(players, achievements)


if __name__ == '__main__':
    main()
