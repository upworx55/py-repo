
# Functions: Block of statements that perform a specific task.
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

"""
Syntax:

Function definition:
 def func_name(param1, param2, ...):
     code block (to do some work)
     return Value

 Function call:
 func_name(arg1, arg2, ...)

 """

def calc_sum (a, b):
    sum = a + b
    print (sum)
    return sum

calc_sum (5, 10)

# some lines of code

calc_sum (2, 10)

# some lines of code

calc_sum (12, 17)

# some lines of code

# Method 2: Function with return value
def calc_sum (a, b):
    return a + b

sum = calc_sum (5, 10)
print (sum)

# Another function to print hello
def print_hello():
    print ("Hello")

print_hello()  # calling the function

output = print_hello()  # calling the function and storing the return value in output
print(output)  # this will print 'None' because print_hello() does not return anything


