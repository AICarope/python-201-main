# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.



def print_real_estate_ad(**kwargs):
    print("Real Estate Advertisement:")
    print("-------------------------")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    print("-------------------------")

# Example usage:
print_real_estate_ad(
    location="Toronto",
    price="$1,000,000",
    bedrooms=4,
    bathrooms=2,
    square_feet=1500,
    amenities=["Dog house", "Garden", "Garage"],
)