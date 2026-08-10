
# Private(like) attributes and methods:
# Conceptual implementations in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# Example 1
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no        # Public attribute
        self.__acc_pass = acc_pass  # Private attribute

    def reset_pass(self):
        print(self.__acc_pass) # This method can access the private attribute __acc_pass because it is defined within the class.

acc1 = Account("123456789", "password123")

print(acc1.acc_no)  # This will print "123456789"
# print(acc1.__acc_pass)  # This will raise an AttributeError becuause __acc_pass is a private attribute and cannot be accessed from outside the class.
print(acc1.reset_pass())  # This will print "password123" because the reset_pass method can access the private attribute __acc_pass.

# Example 2
class Person:
    __name = "anonymous"  # Private class attribute

    def __hello(self): # Private class method
        print("hello person!") 

p1 = Person()
# print(p1.__name)  # This will raise an AttributeError because __name is a private class attribute.
# print(p1.__hello())  # This will raise an AttributeError because __hello is a private class method.

# Example 3
class Person1:
    __name = "anonymous"  # Private class attribute

    def __hello(self): # Private class method
        print("hello person!") 

    def welcome(self):
        self.__hello() # This method can access the private method __hello because it is defined within the class.

p1 = Person1()

print(p1.welcome())  # This will print "hello person!" because the welcome method can access the private method __hello.





