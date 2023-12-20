
# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """One kilometer is equivalent to 0.6214 miles. History/origin: The prefix kilo- is a metric prefix indicating one thousand."""
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
