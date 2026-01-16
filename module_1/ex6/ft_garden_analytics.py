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
    def __init__(self, name: str, height: float, age: int, color: str,
                 prize_points: str):
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

    def garden_info(self):
        info = f"{self.owner}'s Garden Report:\n"
        print("Plants in the garden:")
        for plant in self.plants:
            info += f" - {plant.get_info()}\n"
        return info


class GardenManager:
    def __init__(self):
        self.gardens = []

    @classmethod
    def create_garden_network(cls):
        return cls()

    def grow_all_gardens(self, cm: float):
        for garden in self.gardens:
            print(f"{garden.owner} is helping all plants grow...")
            h = 0
            for plant in garden.plants:
                plant.grow(cm)
                h += cm
                print(f"{plant._name} grew {cm}cm")
            GardenManager.GardenStats.record_growth(garden, h)

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)
        print(f"Added {garden.owner}'s garden to the network.")

    class GardenStats:
        _growth_log = {}

        @staticmethod
        def record_growth(garden: Garden, height: float):
            name = garden.owner
            if name not in GardenManager.GardenStats._growth_log:
                GardenManager.GardenStats._growth_log[name] = 0.0
            GardenManager.GardenStats._growth_log[name] += height

        @staticmethod
        def plants_added(garden: Garden) -> int:
            return len(garden.plants)

        @staticmethod
        def total_growth(garden: Garden) -> float:
            name = garden.owner
            return GardenManager.GardenStats._growth_log.get(name, 0.0)

        @staticmethod
        def plant_types(garden: Garden) -> str:
            r = 0
            f = 0
            p = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    p += 1
                elif isinstance(plant, FloweringPlant):
                    f += 1
                else:
                    r += 1
            w = f"Plant Types: {r} regular, {f} flowering, {p} prize flowers"
            return (w)

        @staticmethod
        def validate_heights(manager: "GardenManager") -> bool:
            for garden in manager.gardens:
                for plant in garden.plants:
                    if plant._height < 0:
                        return False
            return True

        @staticmethod
        def total_gardens(manager: "GardenManager") -> int:
            return len(manager.gardens)

        @staticmethod
        def garden_scores(manager: "GardenManager") -> str:
            parts = []
            for garden in manager.gardens:
                score = 0
                for plant in garden.plants:
                    score += plant._height
                    if isinstance(plant, PrizeFlower):
                        score += plant._prize_points
                parts.append(f"{garden.owner}: {score}")
            return "Garden scores - " + ", ".join(parts)


def main():
    print("=== Garden Managment System ===")
    manager = GardenManager.create_garden_network()
    garden1 = Garden("Alice")
    garden2 = Garden("Bob")
    manager.add_garden(garden1)
    manager.add_garden(garden2)

    plant1 = Plant("Oak Tree", 30.0, 10)
    plant2 = FloweringPlant("Tulip", 25.0, 5, "Red")
    plant3 = PrizeFlower("Orchid", 40.0, 15, "Purple", 50)

    garden1.add_plant(plant1)
    garden1.add_plant(plant2)
    garden1.add_plant(plant3)

    print(f"{garden1.owner}'s is helping all plants grow...")
    manager.grow_all_gardens(1)

    print(garden1.garden_info())

    print(f"Plants added: {GardenManager.GardenStats.plants_added(garden1)}")
    print("Total growth:",
          f"{GardenManager.GardenStats.total_growth(garden1)} cm")
    print(GardenManager.GardenStats.plant_types(garden1))

    valid_h = GardenManager.GardenStats.validate_heights(manager)
    scores = GardenManager.GardenStats.garden_scores(manager)
    total_gardens = GardenManager.GardenStats.total_gardens(manager)

    print(f"Height validation test: {valid_h}")
    print(f"Garden scores: {scores}")
    print(f"Total gardens managed: {total_gardens}")


if __name__ == "__main__":
    main()
