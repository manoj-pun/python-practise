#Write a function is_anagram(s1, s2) that checks if two strings are anagrams without using sorted() or Counter.

def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # If lengths differ, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    count = {}

    # Count characters in first string
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Subtract counts using second string
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True

print(is_anagram("listen", "silent"))   # True
print(is_anagram("triangle", "integral"))  # True
print(is_anagram("apple", "pale"))  # False