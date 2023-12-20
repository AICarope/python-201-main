# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.

#A lambda expression is a short block of code which takes in parameters and returns a value. 
#Lambda expressions are similar to methods, but they do not need a name and they can be implemented right in the body of a method."""

sum_of_numbers = lambda x, y, z: x + y + z
print(sum_of_numbers(10, 22, 43))