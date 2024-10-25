from typing import Callable, Any


def is_prime(func: Callable[[Any], int]):
    def new_func(*args, **kwargs):
        number = func(*args, **kwargs)
        is_prime = True
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime")
        else:
            print("Not prime")
        return number
    return new_func

@is_prime
def sum_three(x,y,z):
    return x+y+z

result = sum_three(2, 3, 6)
print(result)