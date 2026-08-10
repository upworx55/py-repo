
# Question 1
# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2

    def Perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(5)
print("Area of Circle:", c1.Area())
print("Perimeter of Circle:", c1.Perimeter())

# Question 2
# Define an Employee class with attributes role, department & salary. This class should have a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)
 
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "70,000")

e1 = Employee("Accountant", "Finance", "50,000")
e1.showDetails()

eng1 = Engineer("Alice", 30)
eng1.showDetails()

