
# Continue: Used to skip the current iteration of the loop and move to the next iteration.
# (terminates execution in the current iteration & continues execution of the loop with the next iteration)

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue # Skips the current iteration when i is equal to 5 and moves to the next iteration of the loop.
    print(i)

# Q: Print odd numbers only

j = 1
while j<= 10:
    if(j%2 == 0): # j%2 != 0 (use this condition to print even numbers) means j is odd, j%2 == 0 means j is even
        j += 1
        continue
    print(j)
    j += 1
