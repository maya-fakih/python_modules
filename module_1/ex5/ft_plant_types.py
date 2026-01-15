class Plant:
    def __init__(self, name: str, height: float, age: int):
        if (self.validate_plant(height, age) is True):
            self._name = name
            self._height = height     # in centimeters
            self._age = age           # in days

    def validate_plant(self, height: float, age: int):
        if (height < 0 or age < 0):
            if (height < 0):
                h = height
                print(f"Invalid operation attempted: height {h}cm [REJECTED]")
                print("Security: Negative height rejected")
            if (age < 0):
                a = age
                print(f"Invalid operation attempted: age {a} days [REJECTED]")
                print("Security: Negative age rejected")

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
        self._height += height

    def age_plant(self, days):
        self._age += days

    def get_info(self):
        return (f"{self._name}: {self._height} cm, {self._age} days old")

    def set_height(self, height):
        if (height < 0):
            print("Invalid hight. Setting height to 0.")
            self._height = 0
        else:
            self._height = height

    def set_age(self, age):
        if (age < 0):
            print("Invalid age. Setting age to 0.")
            self._age = 0
        else:
            self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def plant_factory(nb_of_plants: int):
        plants = []
        for i in range(nb_of_plants):
            name, height, age = Plant.plant_data[i % len(Plant.plant_data)]
            plants.append(Plant(name, height, age))
        return plants


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def bloom(self):
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, diameter: float):
        super().__init__(name, height, age)
        self._diameter = diameter

    def get_info(self):
        super().get_info()
        n = self._name
        h = self._height
        a = self._age
        d = self._diameter
        return f"{n} (Tree): {h}cm, {a} days, {d}cm diameter"

    def produce_shade(self):
        canopy_diameter = 2 * (self._height / 100)
        shade_area = 3.14 * (canopy_diameter / 2) ** 2
        print(f"{self._name} provides {shade_area} square meters of shade.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest: str):
        super().__init__(name, height, age)
        self._harvest = harvest

    def get_info(self):
        super().get_info()
        n = self._name
        h = self._height
        a = self._age
        hs = self._harvest
        return f"{n} (Vegetable): {h}cm, {a} days, {hs} harvest"

    def nutritional_value(self):
        print(f"{self._name} is rich in vitamin C")


def main():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 30, 60, "Red")
    oak = Tree("Oak", 300, 1000, 50)
    carrot = Vegetable("Carrot", 20, 90, "Fall")
    print(rose.get_info())
    rose.bloom()
    print("\n")
    print(oak.get_info())
    oak.produce_shade()
    print("\n")
    print(carrot.get_info())
    carrot.nutritional_value()


if __name__ == "__main__":
    main()
