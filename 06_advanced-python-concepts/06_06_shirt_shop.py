# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

#colors = ["neon orange", "spring green"]
#sizes = ["S", "M", "L"]


from itertools import product
def solve(colors, sizes):
   return list(product(colors, sizes))

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]
print(solve(colors, sizes))