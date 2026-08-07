
# Q: Write a recursive function to calculate the sum of first n natural numbers.

def sum_nat_nums (n):
    if n == 1: # Base case: If n is 1, we return 1 as the sum of first 1 natural number is 1.
        return 1
    else:
        return n + sum_nat_nums(n-1) # Recursive case: We add n to the sum of first (n-1) natural numbers.

print(sum_nat_nums(5))


# Q: Write a recursive function to print all elements of a list.
# (Hint: Use list & index as parameters)








