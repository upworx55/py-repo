
# Inheritance
# Types: Single Inheritance, Multi-level Inheritance, Multiple Inheritance.

# 1. Single Inheritance: When a child class inherits from a single parent class.
# Example: Refer example in file topics/10_oops/03_oops.py

# 2. Multi-level Inheritance: When a child class inherits from a parent class, and then another child class inherits from that child class.

class Car: # Parent/Base class
    
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car): # Child/Derived class
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start() # This will print "Car started" because the start method is inherited from the Car class through ToyotaCar class.

# 3. Multiple Inheritance: When a child class inherits from more than one parent class.

class A:
    varA = "welcome to class A"
    
class B:
    varB = "welcome to class B"

class C(A, B): # Child class inheriting from both A and B
    varC = "welcome to class C"

c1 = C()
print(c1.varA)  # This will print "welcome to class A"
print(c1.varB)  # This will print "welcome to class B"
print(c1.varC)  # This will print "welcome to class C"


