# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

def swap(s:str) -> str:
    new_chars = []
    for char in s:
        if char.isupper():
            new_chars.append(char.lower())

        elif char.islower():
            new_chars.append(char.upper())

        else:
            new_chars.append(char)

    final_char = ''.join(new_chars)
    print (final_char)

swap("pYTHOn 2")