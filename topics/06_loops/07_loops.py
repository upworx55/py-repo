
# Break: Used to exit a loop prematurely when a certain condition is met.
# (Used to terminate the loop when encountered.)

i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
print("end of the loop")
