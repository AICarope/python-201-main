# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def say_hello (name):
    return (f"Hello {name}!")


def writeletter (name, bye, text):
    greeting = say_hello (name) #f"Hello {name}!"
    bye = f"Goodbye {bye}!"
    mixed = f"{greeting} {text} {bye}"

    return mixed

name = 'Cagdas'
text = 'you are fired'
bye = 'Pluto'
print (writeletter (name, bye, text))

