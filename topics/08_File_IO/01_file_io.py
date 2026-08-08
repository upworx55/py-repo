
# File I/O: Python can be used to perform operations on a file such as reading, writing, and appending data. 
# The built-in `open()` function is used to open a file, and it returns a file object that can be used to read or write data.

f = open("demo.txt", "r")  # Open the file in read mode
data = f.read()  # Read the contents of the file
print(data)  # Print the contents of the file
print(type(data))  # Print the type of the data read from the file
f.close()  # Close the file

"""
Python File Modes:
'r': Opens a file for reading. The file must exist, or an error occurs.
'w': Opens a file for writing. It empties (truncates) the file if it exists or creates a new one.
'x': Creates a new file and opens it for writing. It fails if the file already exists.
'a': Opens a file for appending data to the end without overwriting existing content.
'b': Binary mode. Used for non-text files like images or executables.
't': Text mode. This is the standard default mode for text strings.
'+': Opens a disk file for updating, allowing both reading and writing simultaneously.

Common Combinations:
'r+': Opens for both reading and writing without truncating the file. (truncating means removing all existing data)
'w+': Opens for both reading and writing (overwrites existing data).
'x+': Creates a new file for reading and writing. Fails if the file exists.
'a+': Opens for both reading and appending data.
'rb': Reads a file in binary format.
'wb': Writes a file in binary format.
'ab': Appends to a file in binary format.

"""
# "r" and "rt" are the same, as are "w" and "wt", "a" and "at", etc. The default mode is "rt" (read text).
# If we want to read a file in binary mode, we can use "rb" instead of "r".

f = open("demo.txt", "r")
data = f.read(5)  # Read the first 5 characters of the file
print(data)
line1 = f.readline()  # Read the next line of the file
print(line1)  
f.close()



