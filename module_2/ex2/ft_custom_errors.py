class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Tomato:
    def __init__(self, age):
        self.age = age
        self.name = "tomato plant"

    def check_health(self):
        if self.age > 10:
            raise PlantError(f"The {self.name} is wilting!")


def check_tank(liters):
    if liters < 10:
        raise WaterError("Not enough water in the tank!")


def main():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    my_tomato = Tomato(age=15)
    try:
        my_tomato.check_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    water_liters = 5
    try:
        check_tank(water_liters)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    try:
        my_tomato.check_health()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_tank(2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
