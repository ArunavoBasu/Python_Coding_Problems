# In a given array, locate which integer is not repeated 

from typing import List
def lonelyinteger(a : List) -> int:
    seen = {}
    for num in a:
        if num in seen.keys():
            seen[num] += 1
        else:
            seen[num] = 1
 
    for key in seen:
        if seen[key] == 1:
            return key



print(lonelyinteger([1,2,3,4,3,2,1]))