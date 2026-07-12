
# String Functions in Python

str = "I am studying python from ApnaCollege"
print(str.endswith("ege")) # returns True if the string ends with "ege"
print(str.endswith("Apna")) # returns False

print(str.startswith("I am")) # returns True if the string starts with "I am"

str1 = "i am a good student"
print(str1.capitalize()) # returns a copy of the string with the first character capitalized
print(str1) # original string remains unchanged

str2 = str1.capitalize() # returns a copy of the string with the first character capitalized
print(str2) # prints the capitalized string

print(str1.upper()) # returns a copy of the string with all characters in uppercase
print(str1.lower()) # returns a copy of the string with all characters in lowercase

str3 = str1.title() # returns a copy of the string with the first character of each word capitalized
print(str3) # prints the title-cased string

print(str.replace("o", "a")) # returns a copy of the string with all occurrences of "o" replaced with "a"
print(str.replace("o", "a", 1)) # returns a copy of the string with the first occurrence of "o" replaced with "a"
print(str.replace("python", "java")) # returns a copy of the string with "python" replaced with "java"

print(str.find("o")) # returns the index of the first occurrence of "o" in the string
print(str.find("o", 10)) # returns the index of the first occurrence of "o" in the string starting from index 10
print(str.find("python")) # returns the index of the first occurrence of "python" in the string
print(str.find("q")) # returns -1 if the substring is not found in the string

print(str.count("o")) # returns the number of occurrences of "o" in the string
print(str.count("o", 10)) # returns the number of occurrences of "o" in the string starting from index 10
print(str.count("am")) # returns the number of occurrences of "am" in the string

