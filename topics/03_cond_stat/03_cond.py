
# Simple examples of nested if statements in Python.

age = 25

# Nesting Example 1
if(age >= 18):
    print("You are an adult.")
    if(age >= 65):
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are not an adult.") 
    
# Nesting Example 2
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")