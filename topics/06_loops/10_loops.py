
# For Loops: Used for sequential traversal. For traversing list, string, tuples etc.
# For loops: Used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# For loops: Used to iterate over a sequence of numbers or items.
# Here's an example of a simple `for` loop that prints numbers from 1 to 5:

for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5

nums = [1, 2, 3, 4, 5] # List
for val in nums:
    print(val)  # Output: 1, 2, 3, 4, 5

veggies = ["carrot", "broccoli", "spinach"]
for veg in veggies:
    print(veg)  # Output: carrot, broccoli, spinach

tup = (1, 5, 3, 8, 12) # Tuple
for el in tup:
    print(el)  # Output: 1, 5, 3, 8, 12

str = "Hello" # String
for ch in str:
    print(ch)  # Output: H, e, l, l, o
else:
    print("End")

# else is optional with "for loop" and "while loop".

str1 ="apnacollege"
for char1 in str1:
    if(char1 == 'o'):
        print("o found")
        break
    print(char1)
else:
    print("End of the loop")

