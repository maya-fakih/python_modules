class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant():
    def __init__(self, name: str, water: int, sun: int):
        if (name is None):
            raise ValueError("Plant name cannot be empty!")
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager():
    def __init__(self, tank: int):
        self.plants = []
        self.tank = tank

    def add_plants(self, plant):
        self.plants.append(plant)

    def water_plants(self):
        print("Opening watering system")
        try:
            for i in range(len(self.plants)):
                if (self.tank < 1):
                    raise WaterError("Not enough water in tank")
                self.plants[i].water += 1
                self.tank -= 1
                print(f"Watering {self.plants[i].name} - success")
        except GardenError as e:
            print(f"Caught Garden Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant):
        if plant.name is None:
            e = "Error: Plant name cannot be empty!"
            raise GardenError(e)
        elif plant.water > 10:
            e = f"Water level {plant.water} is too high (max 10)"
            raise GardenError(e)
        elif plant.sun < 2:
            e = f"Sunlight hours {plant.sun} is too low (min 2)"
            raise GardenError(e)
        else:
            w = plant.water
            s = plant.sun
            print(f"{plant.name}: healthy (water: {w}, sun: {s})")

    def plant_health(self):
        print("Checking plant health...")
        try:
            for i in range(len(self.plants)):
                self.check_plant_health(self.plants[i])
        except GardenError as e:
            print(f"Error checking {self.plants[i].name}: {e}")

    def check_tank(self):
        if (self.tank < 1):
            raise WaterError("Not enough water in tank")


def main():
    print("=== Garden Management System ===")
    garden = GardenManager(2)

    print("\nAdding plants to garden...")
    try:
        garden.add_plants(Plant("tomato", 4, 8))
        garden.add_plants(Plant("lettuce", 14, 5))
        garden.add_plants(Plant(None, 3, 3))
    except ValueError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")
    garden.plant_health()

    print("\nTesting error recovery...")
    try:
        garden.check_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == '__main__':
    main()
