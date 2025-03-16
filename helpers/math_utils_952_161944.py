import math

def calculate_area_952(radius):
    return math.pi * radius ** 2

def fibonacci_952(n):
    if n <= 1:
        return n
    return fibonacci_952(n-1) + fibonacci_952(n-2)

def prime_check_952(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
