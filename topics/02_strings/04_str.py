
# Slicing in Python Strings

str = "apna college"

print(str[5:8]) # accessing a substring from index 5 to 7 (8 is exclusive)
print(str[:4]) # accessing a substring from start to 3 (4 is exclusive)
print(str[4:]) # accessing a substring from index 4 to the end of the string
print(str[0:4]) # accessing a substring from index 0 to 3 (4 is exclusive)
print(str[:]) # accessing the entire string
print(str[::2]) # accessing every second character of the string
print(str[1:10:2]) # accessing every second character from index 1 to 9 (10 is exclusive)
print(str[::3]) # accessing every third character of the string

print(str[5:12]) # accessing a substring from index 5 to 11 (12 is exclusive)
print(str[5:len(str)]) # accessing a substring from index 5 to the end of the string using len() function

# Slicing and Negative Indexing in Python Strings
str1 = "Apple"
print(str1[-1]) # accessing the last character of the string using negative indexing
print(str1[-2]) # accessing the second last character of the string using negative indexing
print(str1[-3:-1]) # accessing a substring from index -3 to -1 (not including -1) using negative indexing
print(str1[::-1]) # accessing the string in reverse order using negative indexing

