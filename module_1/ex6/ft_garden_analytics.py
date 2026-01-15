class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height  # in cm
        self._age = age        # in days

    def grow(self, cm: float):
        self._height += cm

    def age_plant(self, days: int):
        self._age += days

    def get_info(self):
        return (f"{self._name}: {self._height} cm")

    def set_height(self, height):
        if (height < 0):
            raise ValueError("Height cannot be negative.")
        self._height = height
    
    def set_age(self, age):
        if (age < 0):
            raise ValueError("Age cannot be negative.")
        self._age = age


class FloweringPlant(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def get_info(self):
        super().get_info()
        n = self._name
        h = self._height
        c = self._color
        return f"{n}: {h}cm, {c} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: float, age: int, color: str, prize_points: str):
        super().__init__(name, height, age, color)
        self._prize_points = prize_points

    def get_info(self):
        super().get_info()
        n = self._name
        h = self._height
        c = self._color
        p = self._prize_points
        return f"{n}: {h}cm, {c} flowers (blooming), Prize Points: {p}"


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant._name} to {self.owner}'s garden.")

    def garden_report(self):
        print(f"=== {self.owner.capitalize()}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
    def garden_statistics(self):
        print(f"Plants added: {len(self.plants)}")
        total_growth = sum(plant._height for plant in self.plants)
        print(f"Total growth: {total_growth} cm")


class GardenManager:
    def __init__(self):
        self.gardens = []

    @classmethod
    def create_garden_network(cls):
        return cls()

    def grow_all_gardens(self, cm: float):
        for garden in self.gardens:
            print(f"{garden.owner} is helping all plants grow...")
            total_growth = 0
            for plant in garden.plants:
                plant.grow(cm)
                total_growth += cm
                print(f"{plant._name} grew {cm}cm")
            print(f"Total growth this round in {garden.owner}'s garden: {total_growth} cm")
            print(f"Plants affected: {len(garden.plants)}\n")