from enum import StrEnum, auto


class Vehicle:
    class __ColorVariants(StrEnum):
        BLUE = auto()
        RED = auto()
        GREEN = auto()
        BLACK = auto()
        WHITE = auto()
        NO_SUCH_COLOR = auto()

        @classmethod
        def _missing_(cls, value):
            value = value.lower()
            for member in cls:
                if member.value == value:
                    return member
            return cls.NO_SUCH_COLOR

    owner: str
    __model: str
    __engine_power: int
    __color: __ColorVariants

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = self.__ColorVariants(color)

    def get_owner(self):
        return  f"Владелец: {self.owner}"

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color.value}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(self.get_owner())

    def set_color(self, color: str):
        if self.__ColorVariants(color) == self.__ColorVariants.NO_SUCH_COLOR:
            raise Exception(f"Нельзя сменить цвет на {color}")
        self.__color = self.__ColorVariants(color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT: int = 5

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
try:
    vehicle1.set_color('Pink')
except Exception as e:
    print(e)
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
