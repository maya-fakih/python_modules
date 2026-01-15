class Plant:
    def __init__(self, name: str, height: float, age: int):
        
        if(self.validate_plant(height, age) == True):
            self.__name = name
            self.__height = height     # in centimeters
            self.__age = age           # in days
        
    def validate_plant(self, height : float, age: int):
        if(height < 0 or age < 0):
            if(height < 0):
                print(f"Invalid operation attempted: height {height}cm [REJECTED]")
                print(f"Security: Negative hight rejected")
            if(age < 0):
                print(f"Invalid operation attempted: age {age} days [REJECTED]")
                print(f"Security: Negative age rejected")

            return False
        
        return True

    def print_security_state(self):
        print(f"Plant created: {self.__name}")
        print(f"Height updated: {self.__height} cm [OK]")
        print(f"Age updated: {self.__age} days [OK]")
    
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
        self.__height += height

    def age_plant(self, days):
        self.__age += days

    def get_info(self):
        return f"{self.__name}: {self.__height} cm, {self.__age} days old"

    def set_height(self, height):
        if (height < 0):
            print("Invalid hight. Setting height to 0.")
            self.__height = 0
        else:
            self.__height = height

    def set_age(self, age):
        if (age < 0):
            print("Invalid age. Setting age to 0.")
            self.__age = 0
        else:   
            self.__age = age

    def get_hight(self):
        return self.__height
    
    def get_age(self):
        return self.__age

    def plant_factory(nb_of_plants: int):
        plants = []
        for i in range(nb_of_plants):
            name, height, age = Plant.plant_data[i % len(Plant.plant_data)]
            plants.append(Plant(name, height, age))
        return plants

class PlantType(Plant):
    def __init__(self, name: str, height: float, age: int, plant_type: str):
        super().__init__(name, height, age)
        self.plant_type = plant_type  # e.g., "Flower", "Tree", "Succulent"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Type: {self.plant_type}"
    
    