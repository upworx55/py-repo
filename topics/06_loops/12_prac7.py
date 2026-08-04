
# range(): returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.
# range(start?, stop, step?) - start is optional, step is optional

print(range(5))  # Output: range(0, 5)
print("\n")
#-----------------

seq = range(5)
for i in seq:
    print(i)  # Output: 0, 1, 2, 3, 4
print("\n")
#-----------------

for i in range(10): # range(stop) - here start is 0 and step is 1 by default
    print(i) 
print("\n")
#-----------------

for i in range(2, 10): # range(start, stop) - here step is 1 by default
    print(i)
print("\n")
#-----------------

for i in range(2, 10, 2): # range(start, stop, step) - here step is 2
    print(i)
print("\n")
#-----------------

# Q: print all even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)
print("\n")
#-----------------

# Q: print all odd numbers from 1 to 20
for i in range(1, 20, 2):
    print(i)
print("\n")
#-----------------

# Q: print numbers from 100 to 1 in reverse order
for i in range(100, 0, -1):
    print(i)
print("\n")
#-----------------

# Q: print the multiplication table of a number n
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    # or print(n*i)
print("\n")




