# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

#from resources import randlist

#print(randlist)

user = [3,7,5,7]
print('the max number is: ', max(user))

import math
user = [3,7,5,7]
product = math.prod(user)

print('the product is: ', product)


