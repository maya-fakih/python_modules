class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height  # in centimeters
        self.age = age        # in days
    
    plant_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
    ("Bamboo", 150, 60),
    ("Lavender", 30, 50),
    ("Bonsai", 10, 500),
    ("Lily", 40, 25),
    ("Pine", 120, 730)
    ]

    def grow_plant(self, height):
        self.height += height
    def age_plant(self, days):
        self.age += days
    def get_info(self):
        return f"{self.name}: {self.height} cm, {self.age} days old"
    
    def plant_factory(nb_of_plants: int):
        plants = []
        for i in range(nb_of_plants):
            name, height, age = Plant.plant_data[i % len(Plant.plant_data)]
            plants.append(Plant(name, height, age))
        return plants
        
def main():
    #number_of_plants = int(input("Enter number of plants to create: "))
    number_of_plants = 5
    plants = Plant.plant_factory(number_of_plants)
    print("\n=== Plant Factory Output ===\n")
    for plant in plants:
        print(f"Created: {plant.get_info()}")
    print(f"\nTotal plants created: {len(plants)}")

if __name__ == "__main__":
    main()