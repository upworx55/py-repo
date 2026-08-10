
# Inheritance: When one class (child/derived) derives the properties & methods of another class (parent/base).

"""
class Car: # Parent/Base class

    ......


class ToyotaCar(Car): # Child/Derived class
        
    ......


"""

class Car: # Parent/Base class
    color = "red" # Class attribute
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car): # Child/Derived class
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Toyota Camry")
car2 = ToyotaCar("Toyota Corolla")

print(car1.name)    # This will print "Toyota Camry"
print(car1.start()) # This will print "Car started" because the start method is inherited from the Car class.
print(car1.color) # This will print "red" because the color attribute is inherited from the Car class.


