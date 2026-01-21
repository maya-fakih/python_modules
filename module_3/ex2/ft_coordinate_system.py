import math


def d(p0, p1) -> float:
    x0, y0, z0 = p0
    x1, y1, z1 = p1

    dx = (x1 - x0)*(x1 - x0)
    dy = (y1 - y0)*(y1 - y0)
    dz = (z1 - z0)*(z1 - z0)

    d = 0.00 + math.sqrt(dx + dy + dz)
    return d


def split_to_touple(p1: str) -> tuple[int, int, int]:
    temp = []
    for item in p1.split(','):
        temp.append(int(item))
    return tuple(temp)


def main():
    print("=== Game Coordinate System ===")

    p0 = (0, 0, 0)

    p1 = (10, 20, 5)
    print(f"\nPosition created: {p0}")
    print(f"Distance between {p0} and {p1}: {d(p0, p1)}")

    p2 = "3, 4, 0"
    print(f"\nParsing coordinates: {p2}")
    try:
        p2 = split_to_touple(p2)
        print(f"Parsed position: {p2}")
        print(f"Distance between {p0} and {p2}: {d(p0, p2)}")
    except Exception:
        e = "invalid literal for int() with base 10: '{item}'"
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e}")

    p3 = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: {p3}")
    try:
        p3 = split_to_touple(p3)
        print(f"Parsed position: {p3}")
        print(f"Distance between {p0} and {p3}: {d(p0, p3)}")
    except Exception:
        e = "invalid literal for int() with base 10: '{item}'"
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e}")

    print("\nUnpacking demonstration:")
    x, y, z = p2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == '__main__':
    main()
