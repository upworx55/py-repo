
# Q: Search for a specific element in a list using while loop.
my_list = [1, 4, 9, 16, 25]
element_to_search = int(input("Enter the element to search: "))
i = 0
found = False
while i < len(my_list):
    if my_list[i] == element_to_search:
        found = True
        break
    i += 1

if found:
    print(f"Element {element_to_search} found in the list.")
else:
    print(f"Element {element_to_search} not found in the list.")


    