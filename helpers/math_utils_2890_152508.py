import math

def calculate_area_2890(radius):
    return math.pi * radius ** 2

def fibonacci_2890(n):
    if n <= 1:
        return n
    return fibonacci_2890(n-1) + fibonacci_2890(n-2)

def prime_check_2890(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
