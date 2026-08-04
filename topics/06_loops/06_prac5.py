
# Q: Search for a number x in the tuple using loop.

my_tuple = (1, 4, 9, 16, 25, 16, 45)
x = 16
i = 0
while i < len(my_tuple):
    if my_tuple[i] == x:
        print("Found at index", i)
    else:
        print("finding..")
    i += 1