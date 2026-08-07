
# Average of 3 numbers using function

def calc_avg(a, b, c):
    avg = (a + b + c) / 3
    print(avg)  # printing the average inside the function
    return avg

calc_avg(1, 2, 3)  # calling the function but not storing or printing the result
result = calc_avg(1, 2, 3)  # calling the function and storing the result
print(result)  # printing the result