from typing import Collection


def personal_sum(numbers: Collection):
    result = 0
    incorrect_data = 0
    for value in numbers:
        try:
            result += value
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {value}')
    return result, incorrect_data


def calculate_average(numbers: Collection) -> float | None:
    try:
        sum, incorrect_data_amount = personal_sum(numbers)
        return sum/(len(numbers) - incorrect_data_amount)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных({type(numbers).__name__})')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать