
#  Q: WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary and add one by one. Use subject name as key & marks as value.

marks = {}  # Empty dictionary to store subject names and marks

x = int(input("Enter marks of phy:\n"))
marks.update({"phy": x})

x = int(input("Enter marks of meth:\n"))
marks.update({"meth": x})

x = int(input("Enter marks of chem:\n"))
marks.update({"chem": x})

print(marks)  