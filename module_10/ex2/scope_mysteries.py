def mage_counter() -> callable:
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power
    def accumulator(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator

def enchantment_factory(enchantment_type: str) -> callable:
    return lambda item_name: f"{enchantment_type} {item_name}"

def memory_vault() -> dict[str, callable]:
    vault = {}
    def store(key, value):
        vault[key] = value
    def recall(key):
        return vault.get(key, "Memory not found")
    return {"store": store, "recall": recall}

if __name__ == "__main__":
    print("mage test")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nspell accumulation")
    acc = spell_accumulator(100)
    print(f"Add 50: {acc(50)}")
    print(f"Add 25: {acc(25)}")

    print("\nfactory test")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))

    print("\nmemory vault test")
    vault = memory_vault()
    vault["store"]("mana", 100)
    print(f"Recall mana: {vault['recall']('mana')}")
    print(f"Recall health: {vault['recall']('health')}")
