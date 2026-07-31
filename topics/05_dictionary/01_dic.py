
# Dictionary: Used to store data in key-value pairs. 
# Dictionaries are mutable, unordered, and do not allow duplicate keys.
# Identifiers: Dictionaries are defined by curly braces {}.

info = {
    "name": "John",
    "age": 30,
    "cities": ("New York", "Los Angeles", "Chicago"), # Tuple
    "married": True,
    "marks": [90, 85, 92], # List
    "subjects": {"Math": 95, "Science": 88, "English": 92}, # Nested Dictionary
    "percentage": 88.5,
}

print(info)
print(type(info))  # Output: <class 'dict'>
print(info["name"])  # Output: John
print(info["age"])  # Output: 30
print(info["cities"])  # Output: ('New York', 'Los Angeles', 'Chicago')
print(info["married"])  # Output: True
print(info["marks"])  # Output: [90, 85, 92]
print(info["subjects"])  # Output: {'Math': 95, 'Science': 88, 'English': 92}
print(info["percentage"])  # Output: 88.5

# Assigning a new key-value pair
info["country"] = "USA"
print(info["country"])  # Output: USA

# Updating an existing key-value pair
info["age"] = 31
print(info["age"])  # Output: 31

info["name"] = "Snow"  # Updating the name  
print(info["name"])  # Output: Snow

info["name"] = 23  # Updating the name to an integer value
print(info["name"])  # Output: 23

# Null Dictionary can also be created
null_dict = {}
print(null_dict)  # Output: {}
print(type(null_dict))  # Output: <class 'dict'>

null_dict["name"] = "Alice"
null_dict["age"] = 25

print(null_dict)  # Output: {'name': 'Alice', 'age': 25}

# Nested Dictionary: A dictionary within a dictionary.
nested_dict = {
    "person1": {"name": "Alice", "age": 25}, # Nested Dictionary
    "person2": {"name": "Bob", "age": 30}, # Nested Dictionary
}

print(nested_dict)
print(nested_dict["person1"])  # Output: {'name': 'Alice', 'age': 25}
print(nested_dict["person2"]["name"])  # Output: Bob

student = {
    "name": "Rahul",
    "Subjects": {            # Nested Dictionary
        "Math": 90,
        "Science": 88,
        "English": 92
    }
}

print(student)
print(student["Subjects"])  # Output: {'Math': 90, 'Science': 88, 'English': 92}
print(student["Subjects"]["Math"])  # Output: 90

