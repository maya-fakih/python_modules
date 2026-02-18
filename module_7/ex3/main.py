from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported = factory.get_supported_types()
    simplified_supported = {
        'creatures': supported['creatures'][:2],
        'spells': supported['spells'][:1],
        'artifacts': supported['artifacts'][:1]
    }
    print(f"Available types: {simplified_supported}")

    print("\nSimulating aggressive turn...")

    dragon = factory.create_creature("Fire Dragon")
    dragon.cost = 5
    goblin = factory.create_creature("Goblin Warrior")
    goblin.cost = 2
    lightning = factory.create_spell("Lightning Bolt")
    lightning.cost = 3

    engine.hand = [dragon, goblin, lightning]

    hand_names = [f"{c.name} ({c.cost})" for c in engine.hand]
    print(f"Hand: {hand_names}")

    print("\nTurn execution:")
    result = engine.simulate_turn()
    print(f"Strategy: {strategy.get_strategy_name()}")

    actions_display = {
        'cards_played': result['cards_played'],
        'mana_used': result['mana_used'],
        'targets_attacked': result['targets_attacked'],
        'damage_dealt': result['damage_dealt']
    }
    print(f"Actions: {actions_display}")

    print("\nGame Report:")
    status = engine.get_engine_status()
    report_display = {
        'turns_simulated': status['turns_simulated'],
        'strategy_used': status['strategy_used'],
        'total_damage': status['total_damage'],
        'cards_created': status['cards_created']
    }
    print(report_display)

    s = "Maximum flexibility achieved!"
    print(f"\nAbstract Factory + Strategy Pattern: {s}")


if __name__ == "__main__":
    main()
