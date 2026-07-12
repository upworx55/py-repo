
# Conditional Statements

#Example 1
age = 21
if (age >= 18):
    print("can vote and apply for license") 
    print("can drive")
    # Indentation is important in python. 
    # Here, the print statement is indented (by 4 spaces or 1 tab) to indicate that it is part of the if block.
else:
    print("not eligible")

#Example 2
if (True):
    print("This is always true")

#Example 3
light = "green"

if (light == "red"):
    print("stop")
elif (light == "green"):
    print("go")
elif (light == "yellow"):
    print("wait")
else:
    print("Light is broken")

print("End of code")