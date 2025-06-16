# You are given an array ar of n integers, and a number k. You need to count the number of pairs (i, j) where i < j and the sum ar[i] + ar[j] is divisible by k.
# n = 6
# k = 3
# ar = [1, 3, 2, 6, 1, 2]

# print(divisibleSumPairs(n, k, ar))
# Output: 5 ( Because - Valid pairs: [(1, 2), (1, 2), (3, 6), (3, 0), (6, 0)] )

from typing import List
def divisible_sum_pairs(n, k, arr) -> int:
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i]+arr[j]) % k == 0:
                count += 1

    return count


print(divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2]))