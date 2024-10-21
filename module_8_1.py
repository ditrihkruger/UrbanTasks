from typing import Any


def add_everything_up(a: Any, b: Any) -> Any | str:
    try:
        return a + b
    except TypeError as e:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))