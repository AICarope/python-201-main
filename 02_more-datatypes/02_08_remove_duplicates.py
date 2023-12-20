# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list = [1, 2, 3, 4, 3, 4, 5]
print('original list: ', (list))
remove = list(set(list))
print('new list without duplicates: ', (list))
##HELP


my_list = [1, 2, 3, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)

my_list = [1, 2, 3, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)