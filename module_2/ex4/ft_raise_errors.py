def check_plant_health(name: str, water: int, sun: int):
    if name is None:
        e = "Error: Plant name cannot be empty!"
        raise ValueError(e)
    elif water > 10:
        e = f"Error: Water level {water} is too high (max 10)"
        raise ValueError(e)
    elif sun < 2:
        e = f"Error: Sunlight hours {sun} is too low (min 2)"
        raise ValueError(e)
    else:
        print(f"Plant '{name}' is healthy!")


def main():
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 7, 5)
    except ValueError as e:
        print(e)

    print("\ntesting empty plant name...")
    try:
        check_plant_health(None, 7, 5)
    except ValueError as e:
        print(e)

    print("\nTesting bas water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 7, 1)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == '__main__':
    main()
