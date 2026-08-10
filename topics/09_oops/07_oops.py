
# Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.
class Car:
    def __init__(self):
        self.acc = False  # private attribute to track if the car is accelerated
        self.brk = False  # private attribute to track if the car is braking
        self.clutch = False  # private attribute to track if the clutch is engaged

    def start(self):
        self.clutch = True  # engaging the clutch
        self.acc = True  # accelerating the car
        print("Car started and accelerating.")

car1 = Car()  # creating an object of class Car
car1.start()  # calling the start method to start the car

# Here, the user does not need to know the internal workings of the Car class such as how the clutch and accelerator are engaged, 
# they just need to know that calling the start() method will start the car and accelerate it.
# This is an example of abstraction, as the implementation details are hidden from the user.


# Encapsulation: Wrapping the data (attributes) and methods (functions) into a single unit (object).

# Other then lecture:------------------------------------------------------------------

# 1. Abstraction: 
# Abstraction is the concept of hiding the internal implementation details and showing only the essential features of an object.
# In Python, abstraction can be achieved using abstract classes and abstract methods.

from abc import ABC, abstractmethod 
# importing ABC and abstractmethod from the abc module. Here ABC stands for Abstract Base Class, which is a class 
# that cannot be instantiated and is meant to be subclassed. The abstractmethod decorator is used to declare methods 
# that must be implemented by any subclass.

class Shape(ABC): # defining an abstract class Shape that inherits from ABC.
    @abstractmethod
    def area(self): # defining an abstract method area() that must be implemented by any subclass of Shape.
        pass        # The pass statement is used here as a placeholder for the method body, indicating that it does not have any implementation in the abstract class.

class Rectangle(Shape): # defining a concrete class Rectangle that inherits from the abstract class Shape.
    def __init__(self, width, height): # defining the constructor for the Rectangle class that takes width and height as parameters.
        self.width = width
        self.height = height

    def area(self): # implementing the abstract method area() from the Shape class. This method calculates and returns the area of the rectangle by multiplying its width and height.
        return self.width * self.height

# Usage:
rect = Rectangle(5, 3)
print(rect.area())  # Output: 15

# 2. Encapsulation:
# Encapsulation is the concept of wrapping data (attributes) and methods (functions) that operate on the data into a single unit (class).
# It restricts direct access to some of the object's components, which can prevent the accidental modification of data.
class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")
# Usage:
person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30




