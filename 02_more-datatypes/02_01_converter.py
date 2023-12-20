# Convert a string to a tuple and print out the result.
# What do you see? it added parenthesis before and after the values
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

stringv = "codingnomads"

#s = 'c','o','d','i','n','g','n'',o','m','a','d','s'
#print(s)
#print("original string: ", str(stringv))

convert = tuple(stringv)
print('the tuple is: ', convert) 

#use for loop to iterate with each elemnet in the tuple.
for element in convert:
    print(element)          