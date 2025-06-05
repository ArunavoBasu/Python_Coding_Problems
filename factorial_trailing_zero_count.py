def factorial_trailing_zero_count(n):
    fact = 1
    for first_num in range(n, 0, -1):
        fact = fact*first_num

    print(f"The factorial is -> {fact}")

    fact_in_str = str(fact)    
    count = 0
    for i in fact_in_str:
        if i == "0":
            count += 1

    return count

print(f"The count of the count of zeros of the factorial value is -> {factorial_trailing_zero_count(10)}")