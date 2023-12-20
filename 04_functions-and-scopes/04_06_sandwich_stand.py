# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

#the *toppings is an *args argument that used grouping

def make_sandwich(bread, *toppings):
    sandwich = (f"{bread} on top and bottom")
    for element in toppings:
        sandwich += (f", {element}")
    return sandwich

# Example usage
sandwich = make_sandwich("Wheat", "Turkey", "Lettuce", "Tomato", "Mayonnaise")
print(sandwich)