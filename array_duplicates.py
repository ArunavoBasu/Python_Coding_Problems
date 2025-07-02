# Given an array arr[] of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.

# Examples:

# Input: arr[] = [2, 3, 1, 2, 3]
# Output: [2, 3] 
# Explanation: 2 and 3 occur more than once in the given array.
# Input: arr[] = [0, 3, 1, 2] 
# Output: []
# Explanation: There is no repeating element in the array, so the output is empty.
# Input: arr[] = [2]
# Output: []
# Explanation: There is single element in the array. Therefore output is empty.

from typing import List

### Method 1
def array_duplicate(arr: List) -> List:
    seen = {}
    res_arr = []
    for num in arr:
        if num in seen.keys():
            seen[num] += 1
        else:
            seen[num] = 1

    for key,val in seen.items():
        if val > 1:
            res_arr.append(key)
    return res_arr

print(array_duplicate([2, 3, 1, 2, 3]))

########################################################
# Method 2
from collections import Counter
def array_dup_counter(arr:List) -> List:
    freq = Counter(arr)
    return [num for num, count in freq.items() if count > 1]

print(array_dup_counter([2, 3, 1, 2, 3]))

