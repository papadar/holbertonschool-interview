import math


def factfunc(n):
    """factor the value"""
    result = 0
    limit = math.ceil(math.sqrt(n))
    print(f"limt for value {n} is {limit}")
    for i in range(2, limit + 1):
        if n % i == 0:
            return i


def minOperations(n):
    """minimum operations calculator"""
    if not isinstance(n, int):
        # print("not integer")
        return 0
    if n <= 1:
        return 0
    else:
        result = factfunc(n)
        return result
