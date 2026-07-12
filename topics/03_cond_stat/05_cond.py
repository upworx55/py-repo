
# Program to find the largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a >=b and a >= c):
    print("first number is the largest", a)
elif(b >= c):
    print("second number is the largest", b)
else:
    print("third number is the largest", c)