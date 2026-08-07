
# Practice Qs:

# WAF to print the length of a list. (list is the parameter)
cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore']
heroes = ['Ironman', 'Thor', 'Hulk', 'Captain America', 'Black Widow']

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

# WAF to print the elements of a list in a single line. ( list is the parameter)
print(heroes[0], end=" ")
print(heroes[1], end=" ")

print() # or print("\n") to print a new line

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()

# WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

# WAF to convert USD to INR.
def converter(usd_value):
    inr_value = usd_value * 83
    print(usd_value, "USD =", inr_value, "INR")

converter(10)
