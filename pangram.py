# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

# Example - "The quick brown fox jumps over the lazy dog"

# The string contains all letters in the English alphabet, so return pangram.

import string
def pangram_check(s: str) -> str:
    # string.ascii_lowercase gives you all lowercase letters: 'abcdefghijklmnopqrstuvwxyz'
    # s.lower() ensures the check is case-insensitive.
    # set(...).issubset(...) verifies that every letter of the alphabet is present in the string.
    if set(string.ascii_lowercase).issubset(set(s.lower())):
        return "pangram"
    else:
        return "not pangram"
    

print(pangram_check("The quick brown fox jumps over the lazy dog"))