
# 3. Inheritance:
# Inheritance is the mechanism by which one class can inherit the attributes and methods of another class. 
# It allows for code reusability and establishes a relationship between classes.
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage:
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!