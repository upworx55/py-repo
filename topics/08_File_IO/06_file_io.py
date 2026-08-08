
"""
Deleting a File: 
1.  using the os (operating system) module, you can delete a file using the os.remove() function. 
    This function takes the path of the file you want to delete as an argument.
2.  Module (like a code library) is a file written by another programmer that generally has functions we can use.
3.  Module is a file containing Python definitions and statements. 
    The file name is the module name with the suffix .py added. 
    A module can define functions, classes, and variables. 
    A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. 
    It also makes the code logically organized.
4. Syntax
import os
os.remove(filename) # if the file exists in the current working directory
or
os.remove("path/to/file.txt") # if the file exists in a different directory

"""
# pip stands for "Pip Installs Packages" or "Pip Installs Python". It is a recursive acronym, meaning the acronym itself is part of the full name.
# Alternatively, it is sometimes referred to as the "preferred installer program". 
# It is a package management system used to install and manage software packages written in Python. 
# Many packages can be found in the Python Package Index (PyPI).

import os

os.remove("sample.txt") # removes the file sample.txt from the current working directory



