def mage_counter():
    """Return a function that counts calls"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter


def spell_accumulator(initial_power):
    """Return a function that accumulates power"""
    total = initial_power
    
    def accumulator(amount):
        nonlocal total
        total += amount
        return total
    
    return accumulator


def enchantment_factory(enchantment_type):
    """Create enchantment functions that remember their type"""
    def enchanter(item):
        return f"{enchantment_type} {item}"
    
    return enchanter


def memory_vault():
    """Create private memory storage with store/recall functions"""
    memory = {}
    
    def store(key, value):
        nonlocal memory
        memory[key] = value
        return f"Stored: {key}"
    
    def recall(key):
        return memory.get(key, "Memory not found")
    
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    counter = mage_counter()
    print("Testing mage counter...")
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    
    accumulator = spell_accumulator(50)
    print("\nTesting spell accumulator...")
    print(f"Add 10: {accumulator(10)}")
    print(f"Add 20: {accumulator(20)}")
    print(f"Add 5: {accumulator(5)}")
    
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    
    print("\nTesting memory vault...")
    vault = memory_vault()
    print(vault['store']('spell', 'fireball'))
    print(f"Recall: {vault['recall']('spell')}")
    print(f"Recall missing: {vault['recall']('unknown')}")