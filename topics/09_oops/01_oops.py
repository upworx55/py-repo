
# OOPS: Object-Oriented Programming System
# To map with real word scenarios, we started using objects in code.
# This is called object-oriented programming (OOP). 
# OOP is a programming paradigm that uses objects and classes to structure code in a way that models real-world entities and their interactions.

# Class: A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.
# Object: An object is an instance (a concrete realization) of a class. It represents a specific entity with its own unique state and behavior, based on the class definition.

"""
creating a class:
class Student:
    name = "Karan Kumar"  # class attribute

creating object (instance) of class:
s1 = Student()  # creating an object of class Student
print(s1.name)  # accessing class attribute using object

"""

# Example 1:
class Student:      # class name should be in PascalCase
    name = "Karan"  # class attribute


s1 = Student()  # creating an object of class Student
print(s1)       # printing the object itself
print(s1.name)  # accessing class attribute using object

s2 = Student()
print(s2.name)

# Example 2:
class Car:
    color = "Red"  # class attribute
    model = "Sedan"  # class attribute

car1 = Car()  # creating an object of class Car
print(car1.color)  # accessing class attribute using object
print(car1.model)  # accessing class attribute using object




