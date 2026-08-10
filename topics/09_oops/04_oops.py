
# Methods: are the functions that belong to objects of a class. 
# are the functions defined inside the class. They are used to define the behavior of the objects created from the class. 
# Methods can access and modify the attributes of the class and can also perform operations related to the class.

"""
# creating class:
class Student:
    def __init__(self, fullname):
        self.name = fullname  # instance attribute
    
    def hello(self):  # instance method
        print("Hello", self.name)

# creating object:
s1 = Student("Ram")  # creating an object of class Student with name
s1.hello()  # calling the instance method hello() using the object s1

"""

class Student:
    def __init__(self, name, marks):
        self.name = name  # instance attribute
        self.marks = marks  # instance attribute

    def welcome(self):  # instance method
        print("Welcome student,", self.name)

    def get_marks(self):  # instance method
        return self.marks
    
s1 = Student("Ram", 90)  # creating an object of class Student with name and marks
s1.welcome()  # calling the instance method welcome() using the object s1
print("Marks:", s1.get_marks())  # calling the instance method get_marks() using the object s1

