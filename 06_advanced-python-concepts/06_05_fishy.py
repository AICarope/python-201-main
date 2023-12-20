# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
mylist = list(fish_tuple)
#print (mylist)

for x in mylist:
    
    if (x.endswith('fish')):
        print(x)


#list comprehension
myset = [x for x in mylist if x.endswith('fish')] 
print(myset)
