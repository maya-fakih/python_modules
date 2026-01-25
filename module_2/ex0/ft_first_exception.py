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
    try:
        check_temprature("25")
    except Exception as e:
        print(e)

    print("\nTesting Temprature: abc")
    try:
        check_temprature("abc")
    except Exception as e:
        print(e)

    print("\nTesting Temprature: 100")
    try:
        check_temprature("100")
    except Exception as e:
        print(e)

    print("\nTesting Temprature: -50")
    try:
        check_temprature("-50")
    except Exception as e:
        print(e)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temprature_input()
