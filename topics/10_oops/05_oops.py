
# Super method: super() method is used to access methods of the parent class from the child class.
# super() method is used to call the parent class methods from the child class. 
# It is commonly used in inheritance to access methods and properties of a parent class.

class Car: # Parent/Base class
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type) # This will call the __init__ method of the parent class Car and initialize the type attribute.
        self.name = name
        super().start() # This will call the start method of the parent class Car.

car1 = ToyotaCar("Toyota", "Diesel")
print(car1.type) # This will print "Diesel" because the type attribute is initialized in the parent class Car using super() method.


