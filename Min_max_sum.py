# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example: arr = [1,5,3,7,9]

# The minimum sum is - 1+3+5+7 = 16 and the maximum sum is - 3+5+7+9 = 24 . The function prints - 16 24

## WORKING-------------
# def miniMaxSum(arr: list):
#     min_sum = 0
#     max_sum = 0
#     arr = sorted(arr)
#     for num in arr[:-1]:
#         min_sum += num
    
#     for i in arr[1:]:
#        max_sum += i

#     return f"{min_sum} {max_sum}"

# print(miniMaxSum([1,2,3,4,5]))

## Optimizer version-------
def optimized_sol(arr):
    total = sum(arr)
    max_sum = total - min(arr)
    min_sum = total - max(arr)
    return f"{min_sum} {max_sum}"

print(optimized_sol([7,69,2,221,8974]))