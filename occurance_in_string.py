# In a given string calculate the number of occurance of each character of the input string. Take your name as the input string

def char_counter(my_str: str):
    my_str = my_str.lower().strip()
    new_obj = {}
    for char in my_str:
        if char in new_obj:
            new_obj[char] += 1
        else:
            new_obj[char] = 1
    print(f"The result is ---> \n {new_obj}")

char_counter("Arunavo Basu")