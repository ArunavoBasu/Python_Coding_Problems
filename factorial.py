def factorial(n) -> int:
    fact = 1
    for first_num in range(n, 0, -1):   ## -1 -> indicating negetive incremen wise loop, because by default it takes +1
        fact = fact*first_num  # storing the factorial value
    return fact
print(factorial(3))