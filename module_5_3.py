from module_5_2 import House2
from typing import Self


class House3(House2):
    def __eq__(self, other: House2 | int) -> bool:
        if isinstance(other, House2):
            return self.number_of_floors == other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors == other
        return False

    def __ne__(self, other: House2 | int) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: House2 | int) -> bool:
        if isinstance(other, House2):
            return self.number_of_floors < other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors < other
        return False

    def __gt__(self, other: House2 | int) -> bool:
        if not isinstance(other, House2) or not isinstance(other, int):
            return False
        return not self.__lt__(other)

    def __le__(self, other: House2 | int) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: House2 | int) -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __add__(self, other: House2 | int) -> Self:
        if isinstance(other, House2):
            self.number_of_floors += other.number_of_floors
            return self
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        raise Exception(f"Operand + with type {type(other)} is not emplemented")

    def __iadd__(self, other: House2 | int) -> Self:
        return self.__add__(other)

    def __radd__(self, other: House2 | int) -> Self:
        return self.__add__(other)

if __name__ == "__main__":
    h1 = House3('ЖК Эльбрус', 10)
    h2 = House3('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2) # __eq__

    h1 = h1 + 10 # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10 # __iadd__
    print(h1)

    h2 = 10 + h2 # __radd__
    print(h2)

    print(h1 > h2) # __gt__
    print(h1 >= h2) # __ge__
    print(h1 < h2) # __lt__
    print(h1 <= h2) # __le__
    print(h1 != h2) # __ne__