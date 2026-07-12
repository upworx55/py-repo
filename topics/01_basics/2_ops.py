
# This Program demonstrates the use of basic arithmetic operations in Python.

a = 5
b = 2

# Performing arithmetic operations
print("Arithmetic Operations:")
print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication
print(a/b)  # Division
print(a%b)  # Modulus (remainder of a divided by b)
print(a**b) # Exponentiation (a^b)

# Performing relational operations
print("\nRelational Operations:")
print(a>b)  # Greater than
print(a>=b) # Greater than or equal to
print(a<b)  # Less than
print(a<=b) # Less than or equal to
print(a==b) # Equal to
print(a!=b) # Not equal to

# Performing Assignment operations
print("\nAssignment Operations:")
c = 10  # Initialize c with 10 (value 10 is assigned to c)
c += 5  # c = c + 5
print(c)
c -= 3  # c = c - 3
print(c)
c *= 2  # c = c * 2
print(c)
c /= 4  # c = c / 4
print(c)
c %= 4  # c = c % 4
print(c)
c **= 2  # c = c ** 2
print(c)

d = 8
e = 3
# Performing Logical operations
print("\nLogical Operations:")
print(True and False)   # Logical AND
print(True or False)    # Logical OR
print(not True)         # Logical NOT
print(d > 5 and e < 5)  # Logical AND with relational expressions
print(d > 5 or e < 5)   # Logical OR with relational expressions
print(not (d > 5))      # Logical NOT with relational expression
print(not (d>e))        # Logical NOT with relational expression

val1 = True
val2 = False
print("and operator:", val1 and val2)  # Logical AND
print("or operator:", val1 or val2)    # Logical OR
print("not operator:", not val1)       # Logical NOT

f = 6
g = 4
# Performing Bitwise operations (Not tought in the course, hence optional)
print("\nBitwise Operations:")
print(f & g)  # Bitwise AND
print(f | g)  # Bitwise OR
print(f ^ g)  # Bitwise XOR
print(~f)     # Bitwise NOT
print(f << 1) # Left shift
print(f >> 1) # Right shift