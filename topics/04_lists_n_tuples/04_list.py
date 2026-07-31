
# List Methods - Functions to perform certain actions on Lists.

list = [2, 1, 3]
list.append(4) # adds one element at the end
print(list)

list1 = [2, 1, 3]
print(list1.append(4)) # append functions returns "None" value.
print(list1.sort()) # sort functions returns "None" value.
print(list1) # sort function arranges elements of the lists in ascending order.

list2 = [2, 1, 3]
list2.append(4)
list2.sort(reverse = True) # Now sort function will arrange elements of the list2 in descending order.
print(list2) 

list3 = ["banana", "litchi", "apple"]
list3.sort(reverse = True) # sorting in descending order.
print(list3) 

list4 = ["m", "b", "f", "a"]
list4.sort()
print(list4)

list4.reverse()
print(list4)

list5 = [2, 1, 3]
list5.insert(1, 5) # Inserts 5 before index 1.
print(list5)

# list.remove(1) -> removes first occurence of the element
list6 = [2, 1, 3]
list6.remove(1) # removes first occurence of element 1 from the list6
print(list6)

# list.pop(idx)  -> removes element at index
list7 = [2, 1, 3]
list7.pop(2) # removes element at index 2 from the list7
print(list7)

