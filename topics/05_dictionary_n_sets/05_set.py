
# Set Methods
# Union: Returns a new set that contains all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
#OR
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

print(set1) # no change in set1
print(set2) # no change in set2

# Intersection: Returns a new set that contains only the elements that are common to both sets.
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
#OR
print(set1.intersection(set2))  # Output: {3}

