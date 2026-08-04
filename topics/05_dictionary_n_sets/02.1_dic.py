
# Dictionary methods are built-in functions that allow you to perform various operations on dictionaries. 
# Here are some commonly used dictionary methods:

# 1. Keys(): Returns a view object that displays a list of all the keys in the dictionary.
from typing import List


student = {
    "name": "Rahul",
    "subjects": {            # Nested Dictionary
        "Math": 90,
        "Science": 85,
        "English": 92,
    }
}

print(student.keys())  # Output: dict_keys(['name', 'subjects'])

print(list(student.keys()))  # Output: ['name', 'subjects'], which is a list of all the keys in the dictionary, typecasted to a list.

print(len(student))  # Output: 2, which is the number of key-value pairs in the dictionary.

print(len(list(student.keys())))  # Output: 2, which is the number of keys in the dictionary, typecasted to a list.

# 2. values(): Returns a view object that displays a list of all the values in the dictionary.
print(student.values())  # Output: dict_values(['Rahul', {'Math': 90, 'Science': 85, 'English': 92}])

print(list(student.values()))  # Output: ['Rahul', {'Math': 90, 'Science': 85, 'English': 92}], which is a list of all the values in the dictionary, typecasted to a list.

# 3. items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(student.items())  # Output: dict_items([('name', 'Rahul'), ('subjects', {'Math': 90, 'Science': 85, 'English': 92})])
print(list(student.items()))  # Output: [('name', 'Rahul'), ('subjects', {'Math': 90, 'Science': 85, 'English': 92})], which is a list of all the key-value pairs in the dictionary.
pairs = list(student.items()) # Storing the key-value pairs in a list
print(pairs[0]) # Output: ('name', 'Rahul'), which is the first key-value pair in the dictionary.

# 4. get(): Returns the value for the specified key if the key is in the dictionary. If not, it returns None (or a specified default value).
print(student.get("name"))  # Output: Rahul, which is the value for the key
print(student["name2"])  # Output: KeyError, since the key "name2" does not exist in the dictionary.
print(student.get("name2"))  # Output: None, since the key "name2" does not exist in the dictionary.
print(student.get("name2", "Default Value"))  # Output: Default Value, since the key "name2" does not exist in the dictionary and a default value is provided.

# 5. update(): Updates the dictionary with the specified key-value pairs. If the key already exists, its value will be updated; if the key does not exist, a new key-value pair will be added.
student.update({"name": "Rahul Sharma", "age": 20})  # Updating the value of the existing key "name" and adding a new key-value pair "age": 20
print(student)  # Output: {'name': 'Rahul Sharma', 'subjects': {'Math': 90, 'Science': 85, 'English': 92}, 'age': 20}

new_dict = {"gender": "Male", "city": "Delhi"}
student.update(new_dict)  # Updating the dictionary with the key-value pairs from new_dict
print(student)  # Output: {'name': 'Rahul Sharma', 'subjects': {'Math': 90, 'Science': 85, 'English': 92}, 'age': 20, 'gender': 'Male', 'city': 'Delhi'}




