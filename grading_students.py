
# Question:
# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range 0 to 100.

# Any grade less than 40 is a failing grade.

# Professor Sam is following a special rounding policy for student grades:

# If the difference between the grade and the next multiple of 5 is less than 3, the grade is rounded up to that multiple of 5.

# If the grade is less than 38, no rounding occurs because the result would still be a failing grade.

# Write a function to apply this grading policy and return the list of adjusted grades.

# Example 1:
# Input:
# grades = [73, 67, 38, 33]

# Output:
# [75, 67, 40, 33]

##########################################################################################################################
# NOTE
# Next divisible by 5 :
# formula = (num // multiple_of_that_number (here 5) + 1) * multiple_of_that_number(here 5)

# Suppose num = 73.

# Step by step:

# Integer division:
# num // 5 → 73 // 5 = 14
# (This gives you how many complete 5s fit into 73)

# Add 1:
# 14 + 1 = 15
# (We're moving to the next multiple of 5)

# Multiply by 5:
# 15 * 5 = 75
# (This gives you the actual number that is the next multiple of 5)

# 🧪 Examples:
# num	num // 5	+1	* 5 (next multiple)
# 73	14	15	75
# 67	13	14	70
# 38	7	8	40
# 84	16	17	85

def gradingStudents(grades):
    result_arr = []
    for num in grades:
        if num >= 38 and num > 10:
            next_multiple_of_five = ((num // 5) + 1 ) * 5
            if next_multiple_of_five - num < 3:
                result_arr.append(next_multiple_of_five)
            else:
                result_arr.append(num)
        else:
            result_arr.append(num)
        
    return result_arr

print(gradingStudents([4, 73, 67, 38, 33]))