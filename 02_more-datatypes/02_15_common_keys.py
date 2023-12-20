# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

#merge dictionaries
#mergedic = {**dict_1, **dict_2}
#print(mergedic)

#find duplicates and add those
#dict_3 ={}
##HELP  
#iterate thorough a dictionary & print its keys and values
#for element in dict_1:
   # print (element, '->', dict_1 [element])

    
    ##HELP  -----  
result = {}
    # Iterate over the keys of dict1
for key in dict_1.keys():
    # Check if the key is present in dict2
    if key in dict_2:
        # Add the values of the common keys together
        result[key] = dict_1[key] + dict_2[key]

# Iterate over the keys of dict2
for key in dict_2.keys():
    # Check if the key is not already in the result dictionary
    if key not in result:
        # Add the key-value pair to the result dictionary
        result[key] = dict_2[key]

print(result)