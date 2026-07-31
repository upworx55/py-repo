
# Tuples: A built-in data type that lets us create immutable sequences of values.
# Identifiers: Tuples are defined by parentheses ().

tup = (2, 1, 3, 1) # Tuple
print(type(tup))
print(tup[0])
print(tup[1])

# tup[0] = 5 -> this type of assignment not allowed in Tuples.

tup1 = () # Tuple
print(tup1)
print(type(tup1))

tup2 = (1,) # Tuple
print(tup2)
print(type(tup2))

tup3 = (1) # Python will treat it as integer.
print(tup3)
print(type(tup3))

tup3 = (1.4) # Python will treat it as float.
print(tup3)
print(type(tup3))

tup3 = ("hello") # Python will treat it as string.
print(tup3)
print(type(tup3))

tup3 = ("hello",) # Tuple
print(tup3)
print(type(tup3))
