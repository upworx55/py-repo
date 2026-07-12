
# Program to check whether a number is even or odd

num = int(input("Enter number: "))

# way 1
if(num % 2 == 0):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# way 2
rem = num % 2
if(rem == 0):
    print("even number")
else:
    print("odd number")