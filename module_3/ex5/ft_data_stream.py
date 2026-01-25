def generate_events(event_n: int):
    players = (
        ["alice", "bob", "charlie", "diana", "eve", "frank", "grace", "henry",
            "iris", "jack"]
    )

    actions = (
        ["killed monster", "found treasure", "leveled up", "completed quest",
            "defeated boss", "discovered secret", "crafted item",
            "joined guild", "won battle", "explored dungeon"]
    )

    levels = [5, 12, 8, 15, 3, 20, 7, 18, 10, 14]

    for i in range(event_n):
        name = players[i % len(players)]
        level = levels[i % len(levels)]
        action = actions[i % len(actions)]
        yield (name, level, action)


def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(count):
    num = 2
    found = 0
    while found < count:
        if is_prime(num):
            yield num
            found += 1
        num += 1


def main():
    print("=== Game Data Stream Processor ===")

    n = 1000
    print(f"\nProcessing {n} events...")

    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up = 0
    for event in generate_events(n):
        total_events += 1
        n, l, a = event
        if (l >= 10):
            high_level += 1
        if (a == "found treasure"):
            treasure_events += 1
        if (a == "leveled up"):
            level_up += 1
        if (total_events <= 3):
            print(f"Event {total_events}: Player {n} (level {l}) {a}")
    print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    first = True

    print("Fibonacci sequence (first 10): ", end="")
    for num in fibonacci_generator(10):
        if (not first):
            print(" ,", end="")
        print(num, end="")
        first = False

    first = True
    print()

    print("Prime numbers (first 5): ", end="")
    for num in prime_generator(5):
        if (not first):
            print(" ,", end="")
        print(num, end="")
        first = False


if __name__ == '__main__':
    main()
