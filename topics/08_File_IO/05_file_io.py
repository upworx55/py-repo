
"""
'with' syntax:
with open("demo5.txt", "a") as f:
    data = f.read()

"""

with open("demo5.txt", "r") as f:
    data = f.read()
    print(data)
    # close()  # Not needed when using 'with' syntax

with open("demo5.txt", "w") as f:
    f.write("newd data")

