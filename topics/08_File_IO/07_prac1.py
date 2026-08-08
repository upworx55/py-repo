
"""
Q: Create a new file "practice.txt" using Python. Add the following data in it"

Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

"""

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.\n")

# Q: WAP that replaces all occurrences of "Java" with "python" in above file.
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# Q: Search if the word "learning" exists in the file or not.
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if word in data:
        print(f"The word '{word}' exists in the file.")
    else:
        print(f"The word '{word}' does not exist in the file.")

# Method2
def check_for_word():
    word1 = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word1) != -1): # find() returns -1 if the word is not found. If the word is found, it returns the index of the first occurrence of the word.
            print("Found")
        else:
            print("Not Found")

check_for_word()

# Q: WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.
def check_for_line():
    word2 = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word2 in data:
                print(f"The word '{word2}' found in line {line_no}.") # here "f" is used for string formatting. It allows you to embed expressions inside string literals, using curly braces {}.
                return
            line_no += 1

    return -1

print(check_for_line())

