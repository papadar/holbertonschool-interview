import math


def is_prime(n: int) -> bool:
    """Numbers less than or equal to 1 are not prime"""
    if n <= 1:
        return False
    """2 is the only even prime number"""
    if n == 2:
        return True
    """Exclude all other even numbers"""
    if n % 2 == 0:
        return False

    """Check odd divisors up to the square root of n"""
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def factfunc(n) -> int:
    """factor the value"""
    result = 0
    check = 0
    limit = math.ceil(n/2)
    factor = False
    print(f" - - - - - - - - - - - limit for value {n} is {limit}")
    for i in range(2, limit + 1):
        check = int(n/i)
        print(f"check {i} for {n} = {n/i}")
        if n % i == 0:
            factor = True
            result += i
            print(f" - - - found a factor in {check} result for {n} is now {result}")
            if is_prime(check):
                result += check
                print(f" - - - found a PRIME factor in {check} result for {n} is now {result}")
            else:
                result += factfunc(check)
                print(f" - - - result for {n} is now {result}")
        if factor:
            print(f"factor was found escape the loop")
            break
    if result == 0:
        print(f"limit reached, adding {n} itself")
        return n
    else:
        return result


def minOperations(n):
    """minimum operations calculator"""
    if not isinstance(n, int):
        print("not integer")
        return 0
    if n <= 1:
        return 0
    else:
        print(f"checking value {n}")
        result = factfunc(n)
        return result
