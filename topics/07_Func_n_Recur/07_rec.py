
# Recursion: (When a function calls itself repeatedly)
# is a programming technique where a function calls itself to solve a problem. 
# It is often used to solve problems that can be broken down into smaller, similar subproblems. 
# Recursion can be a powerful tool for solving complex problems, but it can 
# also be less efficient than iterative solutions in some cases.

# Q: print n to 1 backwards using recursion
def show(n):
    if n == 0: # Base case: If n is 0, we stop the recursion and return from the function.
        return
    print(n)
    show(n-1)

show (5)

# Q: Calculate n factorial using recursion
def fact(n):
    if (n == 0 or n == 1): # Base case: If n is 0 or 1, we return 1 as the factorial of 0 and 1 is defined to be 1.
        return 1
    else:
        return n * fact(n-1) # Recursive case: We multiply n by the factorial of (n-1).

print(fact(5))

# Method2
def fact1(n):
    if (n == 0 or n == 1): 
        return 1
    return n * fact1(n-1)

print(fact1(5))



