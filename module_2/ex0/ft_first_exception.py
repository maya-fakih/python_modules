def check_temprature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: {temp_str} is not a valid number.")
    if (temp < 0):
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C).")
    elif (temp > 40):
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C).")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temprature_input():
    print("=== Garden Temprature Checker ===")
    print("\nTesting Temprature: 25")
    check_temprature("25")
    print("\nTesting Temprature: abc")
    check_temprature("abc")
    print("\nTesting Temprature: 100")
    check_temprature("100")
    print("\nTesting Temprature: -50")
    check_temprature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temprature_input()
