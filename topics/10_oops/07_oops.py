
# Property Decorator:
# We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(90, 80, 70)
print(stu1.percentage)  # This will print percentage of marks of student 1

stu1.phy = 86
print(stu1.phy)  # This will print updated marks of physics of student 1
print(stu1.percentage)  # This will print old percentage of marks of student 1 because we have not updated the percentage after changing the marks of physics.

# Solution 1:

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def cal_percentage(self):
            self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(90, 80, 70)
print(stu1.percentage)  # This will print percentage of marks of student 1

stu1.phy = 86
print(stu1.phy)  # This will print updated marks of physics of student 1
print(stu1.percentage)  # This will print old percentage of marks of student 1 because we have not updated the percentage after changing the marks of physics.
stu1.cal_percentage()
print(stu1.percentage)  # This will print updated percentage of marks of student 1

# Solution 2: We can use @property decorator to make percentage a property of the class.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(90, 80, 70)
print(stu1.percentage)  # This will print percentage of marks of student 1

stu1.phy = 86
print(stu1.percentage)  # This will print updated percentage of marks of student 1


# Other than lecture-------------------------------

# Property Decorators:
# Property decorators are used to define methods in a class that act like attributes.
# They are commonly used to create getter, setter, and deleter methods for class attributes.

class Person:
    def __init__(self, name):
        self._name = name  # private attribute

    @property
    def name(self):
        """Getter method for name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter method for name"""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @name.deleter
    def name(self):
        """Deleter method for name"""
        del self._name

# use:
p = Person("John Doe")
print(p.name)  # Getter method
p.name = "Jane Doe"  # Setter method
print(p.name)
del p.name  # Deleter method




