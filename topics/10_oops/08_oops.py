
# Polymorphism: Operator Overloading
# When the same operator is allowed to have different meaning according to the context.

"""
# ==========================================
# Operators & Dunder (Magic) Functions
# ==========================================

# a + b       # addition        ->  a.__add__(b)
# a - b       # subtraction     ->  a.__sub__(b)
# a * b       # multiplication  ->  a.__mul__(b)
# a / b       # division        ->  a.__truediv__(b)
# a % b       # modulo          ->  a.__mod__(b)

Other than lecture-------------------------------
# a ** b      # exponentiation      ->  a.__pow__(b)
# a == b     # equality             ->  a.__eq__(b)
# a != b     # inequality           ->  a.__ne__(b)
# a < b      # less than            ->  a.__lt__(b)
# a <= b     # less than or equal   ->  a.__le__(b)
# a > b      # greater than         ->  a.__gt__(b)
# a >= b     # greater than or equal ->  a.__ge__(b)


"""
print(1 + 2)  # This will print 3 because + operator is overloaded for int class to perform addition operation.
print("Hello" + "World")  # This will print HelloWorld because + operator is overloaded for str class to perform concatenation operation.
print([1, 2] + [3, 4])  # This will print [1, 2, 3, 4] because + operator is overloaded for list class to perform concatenation operation (merge two lists).
print((1, 2) + (3, 4))  # This will print (1, 2, 3, 4) because + operator is overloaded for tuple class to perform concatenation operation (merge two tuples).

print(type(1))  # This will print <class 'int'> because 1 is an integer.
print(type("Hello"))  # This will print <class 'str'> because "Hello" is a string.
print(type([1, 2]))  # This will print <class 'list'> because [1, 2] is a list.
print(type((1, 2)))  # This will print <class 'tuple'> because (1, 2) is a tuple.

# Other than lecture-------------------------------

# Polymorphism:
# Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
# It allows us to use a unified interface for different data types.
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage:

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

"""
Operators & Dunder functions:
# Operator overloading is a feature in Python that allows us to define the behavior of operators for user-defined classes. 
# This is done by implementing special methods, also known as "dunder" methods (short for "double underscore"), in the class. 
# These methods allow us to customize how operators work with instances of our class.

Operator	    Function
    +	        __pos__(self)
    -	        __neg__(self)
    *	        __mul__(self, other)
    /            __truediv__(self, other)
    //	        __floordiv__(self, other)
    %	        __mod__(self, other)
    **	        __pow__(self, other)
    ==	        __eq__(self, other)
    !=	        __ne__(self, other)
    <	        __lt__(self, other)
    <=	        __le__(self, other)
    >	        __gt__(self, other)
    >=	        __ge__(self, other)


"""

# Polymorphism:
# Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. 
# It allows methods to do different things based on the object it is acting upon.
    
class Bird:
    def speak(self):
        return "Chirp!"

# Usage:
bird = Bird()
print(bird.speak())  # Output: Chirp!


