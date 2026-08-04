
#Set methods

# 1. add(): Adds an element to the set.
collection = set()
collection.add(1)
collection.add(2)
collection.add(2) # Adding a duplicate element to the set will not raise an error, but it will not be added to the set since sets do not allow duplicate elements.

print(collection)  # Output: {1, 2}

# 2. remove(): Removes the specified element from the set. Raises a KeyError if the element is not found.
collection.remove(1) # Removes the specified element from the set. Raises a KeyError if the element is not found.
print(collection)  # Output: {2}

# collection.remove(3) # Raises a KeyError since the element 3 is not found in the set.
# print(collection)  

# add()
collection.add("apnacollege")
collection.add((1, 2, 3)) # Adding a tuple to the set. Tuples are immutable and can be used as elements in a set.
print(collection)  # Output: {2, 'apnacollege', (1, 2, 3)}

print(len(collection))  # Output: 3, which is the number of unique elements in the set.

# 3. clear(): Removes all elements from the set.
collection.clear()
print(len(collection))  # Output: 0, which is the number of unique elements in the set after clearing it.

# 4. pop(): Removes and returns an arbitrary element from the set (removes a random value). Raises a KeyError if the set is empty.
new_collection = {"hello", "apnacollege", "world", "coding", "python"}
print(new_collection.pop())  # Output: 'hello' (or any other element, since it's arbitrary)
print(new_collection.pop()) # Output: 'apnacollege' (or any other element, since it's arbitrary)

