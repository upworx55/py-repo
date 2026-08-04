
# Q: Print the elements of the given list using for loop.
nums = [10, 20, 30, 40, 50]
for el in nums:
    print(el)  # Output: 10, 20, 30, 40, 50

# Q: Search for a no x in the given tuple using for loop.
tup = (1, 5, 3, 8, 12)
x = 8
found = False
for el in tup:
    if el == x:
        found = True
        break
if found:
    print(f"{x} found in the tuple") # here f is used for string formatting
else:
    print(f"{x} not found in the tuple")

# Second method:

tup = (1, 5, 3, 8, 12, 8)
x = 8
idx = 0
for el in tup:
    if el == x:
        print(f"{x} found at index {idx}") 
        print("number found at index", idx) # another way of printing
        # break, apply here if you want to find only the first occurrence of the number in the tuple.
    idx += 1
else:
    print(f"End")



