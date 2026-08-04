
# Set Methods: Sets have various built-in methods that allow you to perform operations on them. Some common set methods include:

# 1. add(): Adds an element to the set.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# 2. remove(): Removes the specified element from the set. Raises a KeyError if the element is not found.
my_set.remove(4)
print(my_set)  # Output: {1, 2, 3}

# 3. discard(): Removes the specified element from the set if it is present. Does not raise an error if the element is not found.
my_set.discard(3)
print(my_set)  # Output: {1, 2}

# 4. pop(): Removes and returns an arbitrary element from the set (removes a random value). Raises a KeyError if the set is empty.
element = my_set.pop()
print(element)  # Output: 1 (or 2, since it's arbitrary)
print(my_set)  # Output: {2} (or {1}, depending on what was popped)

# 5. clear(): Removes all elements from the set.
my_set.clear()
print(my_set)  # Output: set()

# sets are mutable
# Set elements are immutable
# meaning you cannot change the value of an existing element in the set. However, you can add or remove elements from the set.
# Tuples can be used as elements in a set, but lists & dictionaries cannot be used as elements in a set because they are mutable.
