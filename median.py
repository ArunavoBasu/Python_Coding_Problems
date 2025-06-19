# Find the median of any given array as input
from typing import List
def find_median(arr: List) -> int:
    arr.sort()
    arr_len = len(arr)
    # If the elements count is even then the average of two middle element will be the median
    # If the elements count is odd then the middle element will be median
    # arr_len // 2 returns the index
    if arr_len % 2 == 0:
        first_ele = arr[arr_len //2 -1]
        second_ele = arr[arr_len // 2]
        return f"The median is : {(first_ele + second_ele)/2}"
    else:
        ele_index = arr_len // 2
        return f"The median is : {arr[ele_index]}"
    

print(find_median([7,1,2,3,4,5]))