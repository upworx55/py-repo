# __init__ Function (constructor): All classes have a function called __init__(), which is always executed when the class is being initiated. This function is used to initialize the attributes of the class. It is also known as a constructor in Python.
# __init__ method is a constructor in Python. It is called when an object is created from a class and allows the class to initialize the attributes of the class.
# __init__ Function is used to initialize the object’s state. It is called automatically when a new object of the class is created.

"""
Creating class:
class Student:
    def __init__(self, name, age):  # constructor with parameters
        self.name = name  # instance attribute
        self.age = age    # instance attribute

Creating object (instance) of class:
s1 = Student("Karan", 20)  # creating an object of class Student with name and age
print(s1.name)  # accessing instance attribute using object
print(s1.age)   # accessing instance attribute using object

Note: The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class. It must be the first parameter of any function in the class, including __init__.
"""

class Student:
    name = "Karan"  # class attribute
    def __init__(self):
        print(self) # printing the object itself
        print("Constructor called: Object is being created")

s1 = Student()  # creating an object of class Student
print(s1) # printing the object itself

# -------------------------------

class Student1:
    def __init__(self, fullname):  # constructor with parameter
        self.name = fullname  # instance attribute
        print("adding new student in database")

s1 = Student1("Karan")  # creating an object of class Student1 with fullname
print(s1.name)  # accessing instance attribute using object

s2 = Student1("Rohit Sharma")  # creating another object of class Student1 with fullname
print(s2.name)  # accessing instance attribute using object

# Self not necessarily needs to be named self, but it is a strong convention in Python. 
# It is used to refer to the instance of the class and allows access to the attributes and methods of the class.
# The self parameter is a reference to the current instance of the class, and is used toaccess variables that belongs to the class.
class Student1:
    def __init__(abc, fullname):  
        abc.name = fullname
        print("adding new student in database")

s1 = Student1("Karan Kumar")
print(s1.name)

# change of syntax in constructor
class Student2:
    def __init__(self, name, marks):  # constructor with parameters
        self.name = name  # instance attribute
        self.marks = marks  # instance attribute
s1 = Student2("Karan", 90)  # creating an object of class Student2 with name and marks
print(s1.name, s1.marks)  # accessing instance attribute using object

s2 = Student2("Rohit", 85)  # creating another object of class Student2 with name and marks
print(s2.name, s2.marks)  # accessing instance attribute using object

#-------------------------

class Student3:

    # default constructor: 
    # automatically called if no constructor is defined in the class
    # default constructor is a constructor that takes no parameters and initializes the object with default values. 
    # If no constructor is defined in the class, Python provides a default constructor that does nothing.
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name  # instance attribute
        self.marks = marks  # instance attribute
        print("new info printed")

s1 = Student3("Ram", 90)  # creating an object of class Student3 with name and marks
print(s1.name, s1.marks)  # accessing instance attribute using object

s2 = Student3("Lakhan", 85)  # creating another object of class Student3 with name and marks
print(s2.name, s2.marks)  # accessing instance attribute using object


