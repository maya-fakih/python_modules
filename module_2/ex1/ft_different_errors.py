def garden_operations():
    print("=== Garden Error Types Demmo ===\n")

    print("Testing ValueError...")
    try:
        int("five")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        100 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        plant_dict = {"rose": "red", "sunflower": "yellow"}
        plant_dict["tulip"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("three")
        50 / 0
        with open("nonexistent_file.txt", "r") as file:
            file.read()
        plant_dict = {"lily": "white"}
        plant_dict["daisy"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("Alll error types tested sucessfully!")


if __name__ == "__main__":
    garden_operations()
