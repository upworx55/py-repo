
# Ckeck if a list contains a palindrome of elements.

# Palindrome list
list1 = [1, 2, 1]
copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

# Non Palindrome list
list2 = [1, 2, 3]
copy_list2 = list2.copy()
copy_list2.reverse()

if (copy_list2 == list2):
    print("Palindrome")
else:
    print("Not Palindrome")


# Palindrome list
list1 = ["m", "a", "a", "m"]
copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")
