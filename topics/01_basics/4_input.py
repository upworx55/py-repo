
# This program demonstrates how to take input from the user in Python using the input() function.
# The input() function always returns the input as a string. 
# If you want to take numerical input, you need to convert it to the appropriate type (e.g., int or float) using type casting.

name = input("What is your name? ") # here name data type is string
age = input("How old are you? ") # here age data type is string
print(type(name)) # prints <class 'str'>
print(type(age)) # prints <class 'str'>
print("Hello, " + name + "! You are " + age + " years old.")

age = int(age) # converting age to integer
next_year_age = age + 1
print("Next year, you will be " + str(next_year_age) + " years old.")

cgpa = float(input("What is your CGPA? ")) # here cgpa data type is float
print("Your CGPA is: " + str(cgpa))

qty = int(input("Enter quantity: ")) # here qty data type is integer
price = float(input("Enter price: ")) # here price data type is float
total = qty * price
print("Total cost: " + str(total)) # print using string concatenation
print("Total cost: ", total) # print using comma separation
print(f"Total cost: {total}") # print using f-string formatting