import sys


def create_inventory() -> dict:
    inventory = dict()
    try:
        for item in sys.argv[1:]:
            if ':' in item:
                key, value = item.split(':')
                inventory[key] = int(value)
            else:
                e = "Wrong format: Enter input as key:value"
                raise ValueError(e)
        if (len(inventory) == 0):
            raise ValueError("Empty inventory...")
    except ValueError as e:
        raise Exception("Couldnt convert value to int")
    return inventory


def system_analysis(inventory: dict) -> int:
    print("=== Inventory System Analysis ===")
    total = 0
    for key, value in inventory.items():
        try:
            v = int(value)
        except Exception:
            raise ValueError(f"Value for {key} is not an int")
        total += v
    print(f"Total items in inventory: {total}")
    print(f"Unique item types = {len(inventory)}")
    return (total)


def current_inventory(inventory: dict, total: int):
    print("\n=== Current Inventory ===")
    p = 0
    try:
        for key, value in inventory.items():
            p = int(value) / total * 100
            print(f"{key}: {value} units ({p:.1f}%)")
    except ZeroDivisionError:
        raise ZeroDivisionError("Couldnt calculate % (invalid div by 0)")


def inventory_stats(inventory: dict):
    print("\n=== Inventory Statistics ===")
    max = -1
    min = 10000000
    for key, value in inventory.items():
        if (int(value) > max):
            max = int(value)
            most = key
        if int(value) < min:
            min = int(value)
            least = key
    
    print(f"Most abundant: {most} ({max} units)")
    print(f"Least abundant: {least} ({min} units)")


def categories(inventory: dict):
    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}

    for key, value in inventory.items():
        if (int(value) > 4):
            moderate.update({key: value})
        else:
            scarce.update({key: value})
    
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def managment_suggestions(inventory: dict):
    print("\n=== Management Suggestions ===")

    suggestions = {}
    for key, value in inventory.items():
        if (int(value) == 1):
            suggestions.update({key: value})
    print(f"Restock needed: {suggestions.keys()}")


def properties(inventory: dict):
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")

    found = inventory.get("sword")
    if (found is not None):
        found = "True"
    if (found is None):
        found = "False"
    print(f"Sample lookup - 'sword' in inventory: {found}")


def main():
    try:
        inventory = create_inventory()
        total = system_analysis(inventory)
        current_inventory(inventory, total)
        inventory_stats(inventory)
        categories(inventory)
        managment_suggestions(inventory)
        properties(inventory)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
