
# Class & Instance Attributes: 
# Class attributes are shared across all instances of the class, while instance attributes are unique to each instance.
# class attributes are defined within the class but outside any instance methods, while instance attributes are defined within instance methods (usually in the constructor) and are prefixed with self.

class Student:
    college_name = "ABC College"  # class attribute
    def __init__(self, name, marks):
        self.name = name  # instance attribute
        self.marks = marks  # instance attribute
        print("new info printed")

s1 = Student("Ram", 90)  # creating an object of class Student with name and marks
print(s1.name, s1.marks)  # accessing instance attribute using object
print(s1.college_name)  # accessing class attribute using object
print(Student.college_name) # accessing class attribute using class name

s2 = Student("Lakhan", 85)  # creating another object of class Student with name and marks
print(s2.name, s2.marks)  # accessing instance attribute using object
print(s2.college_name)  # accessing class attribute using object
print(Student.college_name) # accessing class attribute using class name

# obj attr > class attr:
# If an instance attribute has the same name as a class attribute, the instance attribute will take precedence over the class attribute when accessed through an instance of the class.

class Student1:
    college_name = "New College"  # class attribute
    name = "anonymous"  # class attribute
    def __init__(self, name, marks):
        self.name = name  # instance or object attribute
        self.marks = marks  # instance or object attribute
        print("new info printed")

s1 = Student1("Ram", 90)  # creating an object of class Student1 with name and marks
print(s1.name)


