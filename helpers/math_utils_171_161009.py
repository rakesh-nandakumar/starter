import math

def calculate_area_171(radius):
    return math.pi * radius ** 2

def fibonacci_171(n):
    if n <= 1:
        return n
    return fibonacci_171(n-1) + fibonacci_171(n-2)

def prime_check_171(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
