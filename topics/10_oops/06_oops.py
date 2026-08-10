
# class method:
# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can not access or modify class state & generally used for utility.

""" 
Class Student:
    @classmethod # decorator to define a class method
    def college(cls):
        pass
"""
class Person:
    name = "anonymous"  # class attribute

    def change_name(self, new_name):
        self.name = new_name  # instance attribute

p1 = Person()
p1.change_name("Rahul Kumar")
print(p1.name)  # This will print "Rahul Kumar"
print(Person.name)  # This will print "anonymous" because class attribute is not changed

# Now we will change the class attribute:

class Person1:
    name = "anonymous"  # class attribute

    def change_name(self, new_name):
        Person1.name = new_name  # class attribute

p1 = Person1()
p1.change_name("Rahul Kumar")
print(p1.name)  # This will print "Rahul Kumar"
print(Person1.name)  # This will print "Rahul Kumar" because class attribute is changed

# method 2:

class Person2:
    name = "anonymous"  # class attribute

    def change_name(self, new_name):
        self.__class__.name = new_name  # class attribute

p1 = Person2()
p1.change_name("Rakesh Kumar")
print(p1.name)  # This will print "Rakesh Kumar"
print(Person2.name)  # This will print "Rakesh Kumar" because class attribute is changed

# method 3:

class Person3:
    name = "anonymous"  # class attribute

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name  # class attribute

p1 = Person3()
p1.change_name("Ramesh Kumar")
print(p1.name)  # This will print "Rakesh Kumar"
print(Person3.name)  # This will print "Rakesh Kumar" because class attribute is changed

# methods:
# static methods
# class methods (cls)
# instance methods (self)

# Other then lecture-------------------------------

# Class Method:
# A class method is a method that is bound to the class and not the instance of the class.
# It can access and modify class state that applies across all instances of the class.

class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def number_of_wheels(cls):
        return cls.wheels

car1 = Car("Toyota")
print(Car.number_of_wheels())  # This will print 4
print(car1.number_of_wheels())  # This will also print 4




