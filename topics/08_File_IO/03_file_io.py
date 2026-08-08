
# "r+" mode allows you to read and write to a file. The file pointer is placed at the beginning of the file. If the file does not exist, it raises a FileNotFoundError.
f = open("demo2.txt", "r+")  # Open the file in read and write mode (File (demo2.txt) original content: This is a sample file.)
f.write("abc")
print(f.read())  # Reads the contents of the file from the current file pointer position (which is at the end of the file after writing "abc")
f.close()

# seek() method is used to change the file pointer position. In this case, we move the file pointer to the beginning of the file before reading its contents.
f = open("demo3.txt", "r+")  
f.write("This line is written to the file.\n")  # Write a string to the file
f.seek(0)  # Move the file pointer to the beginning of the file
print(f.read())  
f.close()


