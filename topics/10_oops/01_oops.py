
# del keyword: used to delete object properties or object itself.
# is used to delete the reference of an object. It can be used to delete variables, lists, dictionaries, etc.
"""
del s1.name
del s1

"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ram", 20)

print(s1.name)  # This will print "Ram"
del s1.name
print(s1.name) # This will raise an error because the name attribute has been deleted

# Run following program after commenting the above code.

print(s1) # This will print the memory address of the s1 object
del s1
print(s1)  # This will raise an error because s1 has been deleted



