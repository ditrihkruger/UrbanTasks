class IncorrectVinNumber(Exception):
    message: str
    def __init__(self, *args):
        if len(args) != 0:
            self.message = args[0]
        super().__init__(*args)


class IncorrectCarNumbers(Exception):
    message: str
    def __init__(self, *args):
        if len(args) != 0:
            self.message = args[0]
        super().__init__(*args)


class Car:
    model: str
    __vin: int
    __numbers: str

    def __init__(self, model: str, vin_number: int, numbers: str):
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        self.model = model

    def __is_valid_vin(self, vin_number: int) -> bool:
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers: str) -> bool:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if not len(numbers) == 6:
            raise IncorrectCarNumbers ('Неверная длина номера')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')