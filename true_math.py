import math

def devide(first: float, second: float) -> float:
    if second == 0:
        return math.inf
    return first / second
