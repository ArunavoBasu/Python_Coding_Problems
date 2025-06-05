def sum_of_five_digits(num):

    digit_sum = 0
    for i in str(num):
        digit_sum += int(i)
    print(digit_sum)
    return digit_sum
    
sum_of_five_digits(12345)