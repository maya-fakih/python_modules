class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height  # in centimeters
        self.age = age        # in days


def ft_garden_data():
    print("=== Garden Plant Registry ===\n")

    number_of_plants = 0
    plants = []

    while (number_of_plants < 3):
        print("You need at least 3 plants.")
        number_of_plants = int(input("Enter number of plants: "))

    print(f"--- Registering {number_of_plants} plants. ---\n")

    for i in range(number_of_plants):
        print(f"Enter information for plant {i + 1}\n")
        name = input("Plant name: ")
        height = float(input("Plant height (in cm): "))
        age = int(input("Plant age (in days): "))
        plant = Plant(name, height, age)
        plants.append(plant)

    print("\n=== Registered Plants ===\n")
    for i in range(number_of_plants):
        plant = plants[i]
        phight = plant.height
        page = plant.age
        pname = plant.name.capitalize()
        print(f"{pname}: {phight}cm, {page} days old")


if __name__ == "__main__":
    ft_garden_data()
