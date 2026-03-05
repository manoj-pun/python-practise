#Given two lists, write a program using sets to find their union, intersection, difference, and symmetric
#difference, displaying results clearly.

num1 = [1, 4, 2, 6, 7, 8, 3, 5]
num2 = [3, 1, 5, 6, 3, 7]

# Convert lists to sets
set1 = set(num1)
set2 = set(num2)

# Union
union = set1 | set2  # or set1.union(set2)
print("Union:", union)

# Intersection
intersection = set1 & set2  # or set1.intersection(set2)
print("Intersection:", intersection)

# Difference (elements in set1 not in set2)
difference = set1 - set2  # or set1.difference(set2)
print("Difference (set1 - set2):", difference)

# Symmetric Difference (elements in either set1 or set2 but not both)
sym_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)