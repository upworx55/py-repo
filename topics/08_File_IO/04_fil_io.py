
# "w+"  Open a file for writing and reading. Creates a new file if it does not exist or truncates the file if it exists.

f = open("demo4.txt", "w+")
print(f.read())  # Read the content of the file (will be empty since we just opened it in write mode)
f.write("This is a test file.") # Write "This is a test file." to the file
f.close()

# "a+" Open a file for appending and reading. Creates a new file if it does not exist.
f = open("demo4.txt", "a+")
print(f.read()) # Read the content of the file (will be empty since we are at the end of the file after opening in append mode)
f.write("abc") # Append "abc" to the end of the file
f.close()




