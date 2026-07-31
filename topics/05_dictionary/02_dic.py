
# Dictionary Methods

# 1. clear(): Removes all items from the dictionary.
my_dict = {"name": "John", "age": 30}
print(my_dict)  # Output: {'name': 'John', 'age': 30}
my_dict.clear()
print(my_dict)  # Output: {}

# 2. copy(): Returns a shallow copy of the dictionary.
my_dict = {"name": "John", "age": 30}
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'John', 'age': 30}

# 3. keys(): Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {"name": "John", "age": 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# 4. values(): Returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values())  # Output: dict_values(['John', 30])

# 5. items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30)])

# 6. get(): Returns the value of the specified key. If the key does not exist, it returns None (or a default value if provided).
print(my_dict.get("name"))  # Output: John
print(my_dict.get("address"))  # Output: None
print(my_dict.get("address", "Not Available"))  # Output: Not Available

# 7. update(): Updates the dictionary with the specified key-value pairs. If the key already exists, its value will be updated; if the key does not exist, it will be added.
my_dict.update({"age": 31, "city": "New York"})
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}


