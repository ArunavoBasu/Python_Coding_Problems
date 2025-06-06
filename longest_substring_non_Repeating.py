# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



def longest_substring(s: str) -> int:
    char_set = set()
    start = 0
    max_len = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        
        char_set.add(s[end])
        max_len = max(max_len, end-start+1)

    return max_len


print(longest_substring("pwwkew"))


### Explanation-
# 🔹 Iteration 1: end = 0, s[end] = 'p'
# 'p' not in set → skip while loop

# Add 'p' to set → char_set = {'p'}

# max_len = max(0, 0 - 0 + 1) = 1

# 🪟 Window: "p"
# ✅ Valid, all characters unique.

# 🔹 Iteration 2: end = 1, s[end] = 'w'
# 'w' not in set → skip while

# Add 'w' → char_set = {'p', 'w'}

# max_len = max(1, 1 - 0 + 1) = 2

# 🪟 Window: "pw"
# ✅ Valid

# 🔹 Iteration 3: end = 2, s[end] = 'w'
# 'w' in set → enter while

# Remove 'p' → char_set = {'w'} → start = 1

# 'w' still in set → remove 'w' → char_set = {} → start = 2

# Now 'w' not in set → add it → char_set = {'w'}

# max_len = max(2, 2 - 2 + 1) = 2 → no change

# 🪟 Window: "w"
# ✅ Valid again after shrinking

# 🔹 Iteration 4: end = 3, s[end] = 'k'
# 'k' not in set → add → char_set = {'w', 'k'}

# max_len = max(2, 3 - 2 + 1) = 2 → becomes 2

# 🪟 Window: "wk"
# ✅ Valid

# 🔹 Iteration 5: end = 4, s[end] = 'e'
# 'e' not in set → add → char_set = {'w', 'k', 'e'}

# max_len = max(2, 4 - 2 + 1) = 3 ✅ update!

# 🪟 Window: "wke"
# ✅ Longest so far

# 🔹 Iteration 6: end = 5, s[end] = 'w'
# 'w' is in set → enter while

# Remove 'w' → char_set = {'k', 'e'} → start = 3

# Now 'w' not in set → add → char_set = {'w', 'k', 'e'}

# max_len = max(3, 5 - 3 + 1) = 3 → no change

# 🪟 Window: "kew"
# ✅ Valid

# ✅ Final Result:
# max_len = 3

# Longest substrings without duplicates are "wke" and "kew"

