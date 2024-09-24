class House:
    name: str
    number_of_floors: int
    def __init__(self, name : str, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors
    
    def go_to(self, new_floor: int) -> None:
        if not 1 <= new_floor <= self.number_of_floors:
            print("Такого этажа не существует")
            return
        for floor in range(1, new_floor + 1):
            print(floor)

if __name__ == "__main__":
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)
