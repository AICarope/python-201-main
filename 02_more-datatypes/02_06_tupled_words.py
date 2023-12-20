# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user = "It is better to do a certificatation or a master in AI?"
#tup = (["It", "is", "better", "to", "do", "a", "certificatation", "or", "a", "master", "in", "AI?"])
#print(tup)

#Question
#when creating a tupple do you need to sdo the " and comas manually? or euser can be created automatically using aconversiont to a tupple?"

convert = tuple (user)
print(convert)