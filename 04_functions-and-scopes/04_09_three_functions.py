# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.


def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def square_sum(a, b):
    sum_result = add_numbers(a, b)
    return multiply_numbers(sum_result, sum_result)

a = 2
b = 3
result = square_sum(a, b)
print(result)