# Write a script that takes in a string from the user.
# Using the 
# and print back the most common word in the text.
#lets have coffee every morning in the morning



user = input("give me a string?")
mysplit = user.split()
print(mysplit)
#dictionary is a good data type for counting
dict = {i: mysplit.count(i) for i in mysplit}
# find the key with the highest value
max_key = max(dict, key=dict.get)
print(max_key)

#for element in mysplit:
#   print(element)
