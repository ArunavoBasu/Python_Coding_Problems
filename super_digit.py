### If a number is - 1234 then it's super digit is = 1+2+3+4 = 10
def super_digit_old(n):
    converted_str = str(n)
    sum = 0
    for i in converted_str:
        int_val = int(i)
        sum = sum + int_val

    return sum


# ---------------   How map() Works: -------------------------------
# It takes two arguments:

    # 1. A function (the transformation to be applied).

    # 2. An iterable (the collection of items to be processed).

# **It applies the function to each item in the iterable and returns a map object, which can be converted into a list, tuple, etc.**

## Another way
def super_digit_new(n):
    converted_str = str(n)
    super_digit = sum(map(int, converted_str))
    return super_digit

print(super_digit_new(1234))