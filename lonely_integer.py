# In a given array, locate which integer is not repeated 

from typing import List
def lonelyinteger(a : List) -> int:
    seen = {}
    for num in a:
        if num in seen.keys():
            seen[num] += 1
        else:
            seen[num] = 1
 
    for key, value in seen.items():
        if value == 1:
            return key



print(lonelyinteger([1,2,3,4,3,2,1]))