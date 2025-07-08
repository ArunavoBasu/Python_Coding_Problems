# You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

# Examples:

# Input: arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
# Input: arr = [10, 4, 2, 4, 1]
# Output: [10, 4, 4, 1]
# Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
# Input: arr = [5, 10, 20, 40]
# Output: [40]
# Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
# Input: arr = [30, 10, 10, 5]
# Output: [30, 10, 10, 5]
# Explanation: When an array is sorted in non-increasing order, all elements are leaders.

##################################################################################################################
# Logic-
## 1. iterating the loop from right to left and storing the right most element always in the result array.
## 2. max_from_right is set to -infinity , and comparing if the left element is greater than or equal to the max_from_right then storing the left element in the result array and that number will be assigned to max_from_right variable.
## 3. lastly reversing the whole array as the loop is iterating from right to left so by reversing it will give the left to right order.

from typing import List
def leader_array(arr: List) -> List:
    result_arr = []
    max_from_right = float('-inf')
    ## Loop will go from last element to -1 in decreasing order
    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= max_from_right:
            result_arr.append(arr[i])
            max_from_right = arr[i]

    return result_arr[::-1]

print(leader_array([5, 10, 20, 40]))