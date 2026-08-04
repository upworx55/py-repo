
# Loops: used to repeat a block of code multiple times until a certain condition is met.
# Loops: used to repeat instructions.
# There are two main types of loops in Python: for loops and while loops.

while True:  # Infinite loop, will run until a break statement is encountered
    print("hello")  # Output: hello, will be printed infinitely until the loop is broken
    break  # Break statement, will exit the loop when encountered

count = 1
while count <= 5:  # While loop, will run until the condition is False
    print(count)  # Output: 1, 2, 3, 4, 5, will print the value of count until the condition is False
    count += 1  # Incrementing the value of count by 1 in each iteration
print(count)  # Output: 6, will print the value of count after the loop has ended

i = 1
while i <= 5:
    print("hello", i)
    i = i + 1

j = 5
while j >= 1:
    print(j)
    j -= 1
print ("Loop ended")

# Avoid infinite loops
# such as in above case, if j<6 condition is applied on while loop, it will run infinitely and will not end.