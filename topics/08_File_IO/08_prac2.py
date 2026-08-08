
# Q: From a file containing numbers separated by comma, print the count of even numbers.
# parse means to analyze a string and convert it into a more usable format, such as a list of numbers.
# casting means to convert a variable from one type to another, such as converting a string to an integer.
# Type casting is the process of converting a variable from one data type to another. In Python, this can be done using built-in functions like int(), float(), str(), etc.


"""
We can extract the numbers and then check if they are even or odd.

with open("demo6.txt", "r") as f:
    data = f.read()
    print(data)

num = ""
for i in range(len(data)):
    if(data[i] == "," or data[i] == "."):
        print(int(num))
        num = ""
    else:
        num += data[i]

now we can check if the number is even or odd by using the modulus operator (%).

"""
count = 0
with open("demo6.txt", "r") as f:
    data = f.read()
    nums = data.split(",")  # Split the string into a list of numbers separated by commas
    for val in nums:
        if (int(val) % 2 == 0):  # Check if the number is even
            count += 1

print("Count of even numbers:", count)

