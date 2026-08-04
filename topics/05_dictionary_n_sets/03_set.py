
# Set: A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from them.
# Sets are defined using curly braces {} or the set() function.
# Each element in the set must be uniques & immutable (cannot be changed). Sets do not allow duplicate elements.

# Example:
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>

# Creating a set using the set() function
another_set = set([1, 2, 3, 4, 5])
print(another_set)  # Output: {1, 2, 3, 4, 5}

collection = {1, 2, 3, "hello", "world"}
print(collection)  # Output: {1, 2, 3, 'hello', 'world'}

# Repeated words stored in a set will be removed automatically, as sets do not allow duplicate elements.
collection_1 = {1, 2, 2, 2, "hello", "world", "world",4}
print(collection_1)
print(len(collection_1))  # Output: 5, which is the number of unique elements in the set.

# Empty set:
empty_set = set()  # Creating an empty set using the set() function
empty = {}  # This creates an empty dictionary, not a set
print(type(empty_set))  # Output: <class 'set'>
print(type(empty))  # Output: <class 'dict'>
