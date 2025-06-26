# Problem Summary:
# The expected message is a repetition of "SOS" for the full length of the received string.
# Some characters may get altered during transmission.
# Goal: Count how many characters in the received string s differ from the expected "SOS" pattern.

## Output and Input structure--
# Expected signal: SOSSOSSOSSOS
# Recieved signal: SOSSPSSQSSOR

# We print the number of changed letters, which is 3.
# S = SOSSPSSQSSOR, and signal length |S| = 12 . Sami sent = 4 SOS messages (i.e.: 12/3 = 4).

##################################################################################################
# NOTE
# 1. The zip() function in Python pairs up elements from two (or more) iterables (like lists, tuples, strings) element-wise. It returns an iterator of tuples.
# E.g -> a = [a,b,c], b = [1,2,3] -> zip(a, b) gives -> a 1, 
                                                      # b 2
                                                      # c 3 - this way


# 2. It does integer (floor) division, meaning:
    # It divides two numbers
    # Then removes any decimal/fractional part
    # Returns the largest whole number less than or equal to the result
# E.g -> (10 divided by 4 is 2.5, 10//4 =2.5 -> floor division gives 2)

##################################################################################################

def mars_sos_solution(s: str) -> int:
    expected_str = "SOS" * (len(s) // 3)
    count = 0

    for recieved_char, expected_char in zip(s, expected_str):
        if recieved_char != expected_char:
            count += 1

    return count

print(mars_sos_solution("SOSSPSSQSSOR"))