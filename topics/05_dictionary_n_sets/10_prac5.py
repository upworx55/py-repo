
# Q: Figure out a way to store 9 & 9.0 as separate values in the set.

values = {9, 9.0, 8, 8.25}
print(values)  # Output: {9, 8, 8.25}, which shows that 9 and 9.0 are considered the same value in a set, so only one of them is stored.

# using string
values_1 = {9, "9.0"} # here 9 is an integer and "9.0" is a string, so they are considered different values in a set.
print(values_1 ) # output: {9, '9.0'}

# using tuple
values_2 = {9, (9.0,)} # here 9 is an integer and (9.0,) is a tuple, so they are considered different values in a set.
print(values_2) # output: {9, (9.0,)}

# using tuple
values_3 = {
    ("float", 9.0), # here ("float", 9.0) is a tuple, so it is considered a different value in a set.
    ("int", 9), # here ("int", 9) is a tuple, so it is considered a different value in a set.
}
print(values_3)  # output: {('float', 9.0), ('int', 9)}, which shows that 9 and 9.0 are considered different values in a set when stored as tuples.

