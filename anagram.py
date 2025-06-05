def anagram(str1, str2) -> bool:
    if sorted(str1.lower()) == sorted(str2.lower()):
        return True
    else:
        return False


print(anagram("anagram", "MANARAG"))

## Logic: -----
# Sorting both the input word means the word will be generated with the sorted arrangement of it's alphabets,
# Also converting every word in it's lower format 
# Then checking if the sorted words for both the input strings are same, if same returning True