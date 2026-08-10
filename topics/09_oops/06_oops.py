
# Static Methods: Methods that do not use self parameter (work at class level).
"""
class Student:
    @staticmethod # Decorator to define a static method
    def college():
        print("ABC College")

Note: Decorators allow us to wrap another function in order to
extend the behavior of the wrapped function, without permanently modifying it.
"""
class Student:
    @staticmethod
    def hello():
        print("hello")

s1 = Student()  # creating an object of class Student
s1.hello()  # calling the static method hello() using the object s1

#-------------------
class Student:
    def __init__(self, name, marks):
        self.name = name  # instance attribute
        self.marks = marks  # instance attribute (list of marks)
    @staticmethod
    def hello():
        print("hello world")

s1 = Student("Ram", [90, 85, 95])  # creating an object of class Student
s1.hello()  # calling the static method hello() using the object s1

# Static Methods: 
# Static methods are methods that belong to a class rather than an instance of the class.
# They do not have access to the instance (self) or class (cls) variables.
# They are defined using the @staticmethod decorator.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Usage:
print(MathUtils.add(5, 3))       # Output: 8
print(MathUtils.subtract(5, 3))  # Output: 2

# Class Methods:
# Class methods are methods that belong to a class rather than an instance of the class.
# They have access to the class (cls) but not the instance (self) variables.
# They are defined using the @classmethod decorator.

class MyClass:
    class_variable = 0

    @classmethod # Decorator to define a class method
    def increment_class_variable(cls): # class method to increment the class variable
        cls.class_variable += 1

# Usage:
print(MyClass.class_variable)  # Output: 0
MyClass.increment_class_variable()
print(MyClass.class_variable)  # Output: 1

