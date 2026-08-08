
# write() method writes a string to the file. If we want to write multiple lines, we can call write() multiple times or use writelines() method to write a list of strings to the file.
f = open("demo1.txt", "w")  # Open the file in write mode
f.write("Hello, World!\n")  # Write a string to the file
f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])  # Write a list of strings to the file
f.close()

# append() method opens the file in append mode and writes the string to the end of the file.
f = open("demo1.txt", "a")  # Open the file in append mode
f.write("This line is appended to the file.\n")  # Append a string to the file
f.writelines(["This line is also appended to the file.\n", "This is the last line.\n"])  # Append a list of strings to the file
f.close()



