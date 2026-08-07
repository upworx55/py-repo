
# Default Parameters: are parameters that assume a default value if a value is not provided in the function call.
# (Assigning a default value to a parameter, which is used when no argument is passed to the function)
# Example1: A function that greets a user with a default name if no name is provided.

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet("Alice"))  # prints "Hello, Alice!"
print(greet())  # prints "Hello, Guest!"

# Example2:
def cal_prod(a=4, b=2):
    print(a * b)
    return a * b

cal_prod()  # prints 8
cal_prod(5)  # prints 10
cal_prod(3, 3)  # prints 9

# Example3:
def cal_prod(a, b=2): # only b has a default value. First parameter cannot have a default value, if the second parameter does not have a default value.
    print(a * b)
    return a * b

cal_prod(4)  # prints 8
cal_prod(5)  # prints 10
cal_prod(3, 3)  # prints 9
