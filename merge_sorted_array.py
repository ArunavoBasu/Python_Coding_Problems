# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
## -------------   Do not return anything, modify nums1 in-place instead.    -----------------

#Method - 1
from typing import List
def merge_sort_array(nums1: List[int], m: int, nums2: List[int], n: int):
    updated_nums1 = []
    updated_nums2 = []
    new_list = []

    for i in range(m):
        updated_nums1.append(nums1[i])

    for j in range(n):
        updated_nums2.append(nums2[j])

    new_list = updated_nums1 + updated_nums2   
    return  sorted(new_list)


print(merge_sort_array(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

#Method -2 -short and editing the nums1 array in-place
def second_meth(nums1: List[int], m: int, nums2: List[int], n: int):
    ## After the m number of element nums2 array will be replaced
    nums1[m:] = nums2
    return sorted(nums1)


print(second_meth(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))