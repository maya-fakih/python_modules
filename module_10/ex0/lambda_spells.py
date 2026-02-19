def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power level descending"""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages with power >= min_power"""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Add '* ' prefix and ' *' suffix to each spell"""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate max, min, and avg power of mages"""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'scrying'},
        {'name': 'Dragon Amulet', 'power': 99, 'type': 'protection'}
    ]
    
    mages = [
        {'name': 'Gandalf', 'power': 95, 'element': 'fire'},
        {'name': 'Saruman', 'power': 88, 'element': 'lightning'},
        {'name': 'Radagast', 'power': 72, 'element': 'nature'}
    ]
    
    spells = ['fireball', 'heal', 'shield']
    
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for a in sorted_artifacts[:2]:
        print(f"{a['name']} ({a['power']} power) ", end="")
    print()
    
    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(' '.join(transformed))
    
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']}, Avg: {stats['avg_power']}")
