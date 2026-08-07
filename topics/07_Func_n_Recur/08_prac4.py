
# Q: Write a recursive function to calculate the sum of first n natural numbers.

from operator import index


def sum_nat_nums (n):
    if n == 1: # Base case: If n is 1, we return 1 as the sum of first 1 natural number is 1.
        return 1
    else:
        return n + sum_nat_nums(n-1) # Recursive case: We add n to the sum of first (n-1) natural numbers.

print(sum_nat_nums(5))

# Method 2:
def cal_sum(n):
    if n == 0:
        return 0
    return n + cal_sum(n-1)

sum = cal_sum(5)
print(sum)

# Q: Write a recursive function to print all elements of a list.
# (Hint: Use list & index as parameters)

nums = [1, 2, 3, 4, 5]

def print_list_els(list, index):
    if index == len(list): # Base case: If index is equal to the length of the list, we stop the recursion.
        return
    else:
        print(list[index]) # Print the current element at the given index.
        print_list_els(list, index + 1) # Recursive case: Call the function with the next index.

print_list_els(nums, 0)

# Method 2:
def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx + 1)

fruits = ['apple', 'banana', 'cherry']
print_list(fruits)





