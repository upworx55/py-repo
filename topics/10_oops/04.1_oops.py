
# Types of inheritance: 
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# 1. Single Inheritance: When a child class inherits from a single parent class.
# Example:
class Parent:
    def skills(self):
        print("Gardening, Programming")

class Child(Parent):
    def skills(self):
        super().skills()
        print("Cooking, Art")

c = Child()
c.skills()

# 2. Multiple Inheritance: When a child class inherits from multiple parent classes.
# Example:
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

c = Child()
c.skills()

# 3. Multilevel Inheritance: When a child class inherits from a parent class, and then another child class inherits from that child class.
# Example:
class Grandfather:
    def skills(self):
        print("Gardening, Programming")

class Father(Grandfather):
    def skills(self):
        super().skills()
        print("Cooking, Art")

class Child(Father):
    def skills(self):
        super().skills()
        print("Sports")

c = Child()
c.skills()

# 4. Hierarchical Inheritance: When multiple child classes inherit from a single parent class.
# Example:
class Parent:
    def skills(self):
        print("Gardening, Programming")

class Child1(Parent):
    def skills(self):
        super().skills()
        print("Cooking, Art")

class Child2(Parent):
    def skills(self):
        super().skills()
        print("Sports")

c1 = Child1()
c1.skills()

c2 = Child2()
c2.skills()


# 5. Hybrid Inheritance: When a combination of two or more types of inheritance is used.
# Example:
class Grandfather:
    def skills(self):
        print("Gardening, Programming")

class Father(Grandfather):
    def skills(self):
        super().skills()
        print("Cooking, Art")

class Mother:
    def skills(self):
        print("Art, Music")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

c = Child()
c.skills()


