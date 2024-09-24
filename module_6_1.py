class Nameable:
    name: str = None

    def __init__(self, name: str):
        self.name = name

class Plant(Nameable):
    is_edible: bool = False

    def __init__(self, name: str):
        super().__init__(name)

class Animal(Nameable):
    is_alive: bool = True
    is_fed: bool = False
    name: str = None

    def __init__(self, name: str):
        super().__init__(name)

    def eat(self, food: Plant) -> None:
        if not isinstance(food, Plant):
            return
        if food.is_edible:
            print(f"{self.name} съел {food.name}")
            self.is_fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.is_alive = False


class Mammal(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class Predator(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class Flower(Plant):
    def __init__(self, name: str):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.is_alive)
print(a2.is_fed)
a1.eat(p1)
a2.eat(p2)
print(a1.is_alive)
print(a2.is_fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.