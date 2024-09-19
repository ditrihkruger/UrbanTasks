def get_muliplied_digits(number: int):
    if number == 0:
        return 1
    if number % 10 == 0:
        return 1 * get_muliplied_digits(number // 10)
    return number % 10 * get_muliplied_digits(number // 10)

print(get_muliplied_digits(40203))
