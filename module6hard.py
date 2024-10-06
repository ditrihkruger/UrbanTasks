import math


class Figure:
    sides_count: int = 0
    __sides: list[float]
    __color: tuple[int, int, int]
    is_filled: bool

    def __init__(self, color: tuple[int, int, int], *sides: float, is_filled: bool = False):
        self.__sides = list(sides)
        self.__color = color
        self.is_filled = is_filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color: tuple[int, int, int]):
        for component in color:
            if not 0 < component < 255:
                return False
        return True

    def set_color(self, *color: int):
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_sides(self, *sides: float):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides.copy()

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides: float):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    __radius: int

    def __init__(self, color: list[int, int, int],  *sides: float):
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(color, *sides)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list[int, int, int], *sides: float):
        if len(sides) != self.sides_count:
            sides = [1, 1, 1]
        super().__init__(color, *sides)

    def get_square(self):
        return math.sqrt(
            len(self) / 2 *
            (len(self) / 2-self.get_sides()[0]) *
            (len(self) / 2 - self.get_sides()[1]) *
            (len(self) / 2 - self.get_sides()[2])
        )


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list[int, int, int], *sides: float):
        if len(sides) != 1:
            sides = [1]*12
        else:
            sides = sides*12
        super().__init__(color, *sides)

    def set_sides(self, *new_side: float):
        if len(new_side) == 1:
            super().set_sides(*([new_side]*12))

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
