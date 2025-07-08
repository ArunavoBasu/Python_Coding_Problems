# Given an array of integers arr[], the task is to find the first equilibrium point in the array.

# The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

# Examples:

# Input: arr[] = [1, 2, 0, 3]
# Output: 2 
# Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
# Input: arr[] = [1, 1, 1, 1]
# Output: -1
# Explanation: There is no equilibrium index in the array.
# Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
# Output: 3
# Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.

##############################################################################################################
# Logic-
# We're comparing left_sum and right_sum after subtracting arr[i] — which mistakenly skips the element from both sides correctly — but due to the flow of total -= arr[i] before comparison, the logic passes in cases where it shouldn't. If no index satisfied then return -1 (for scenario like - [1,1,1,1])


from typing import List
def equilibrium_arr_index(arr: List) -> int:
    left_sum = 0
    total = sum(arr)
    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]

    return -1

print(equilibrium_arr_index([1,1,1,1]))