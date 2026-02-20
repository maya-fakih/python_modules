def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    stats = list(map(lambda x: x['power'], mages))
    minn = min(stats)
    maxx = max(stats)
    lenn = len(stats)
    avg = sum(stats) / lenn
    return {
        'max_power': maxx,
        'min_power': minn,
        'avg_power': round(avg)
    }


if __name__ == "__main__":
    artifacts = [{'name': 'Staff', 'power': 92}, {'name': 'Orb', 'power': 85}]
    print("Testing sorter:", artifact_sorter(artifacts))

    spells = ["fireball", "heal"]
    print("Testing spells:", spell_transformer(spells))

    mages = [{'name': 'A', 'power': 10}, {'name': 'B', 'power': 20}]
    print("Testing stats:", mage_stats(mages))
