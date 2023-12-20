# The following function definition has a whole lot of bugs in it!
# Run the script and follow Python's error hints to fix them all.
# After your fixes, the function should allow you to take a name as an input
# and return a greeting message that you can save to a variable.

def say_hello (name):
                return print(f"Hello {name}!")
# if name iss under function it  must never change. If moving me outside the function then it can be reused.
name = ('carmen')

greeting = say_hello (name)
#say_hello = hello(name)
print(greeting)
