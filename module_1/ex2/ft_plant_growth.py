class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height  # in centimeters
        self.age = age        # in days

    def grow_plant(self, height):
        self.height += height
    def age_plant(self, days):
        self.age += days
    def get_info(self):
        return f"{self.name}: {self.height} cm, {self.age} days old"
    
def ft_plant_growth():
    plant = Plant(name="tomato", height=30.0, age=20)
    print(plant.get_info())
    grow = int(input("Enter growth in cm: "))
    plant.grow_plant(grow)
    age = int(input("Enter additional age in days: "))
    plant.age_plant(age)
    print("Updated plant info:")
    print(plant.get_info())
    
if __name__ == "__main__":
    ft_plant_growth()