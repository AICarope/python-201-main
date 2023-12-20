# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def writeletter (name, bye, text):
    greeting =(f"Hello {name}!")
    bye = (f"Goodbye {bye}!")

    return print (greeting, text, bye)
name = ('Cagdas')
text = ('you are fired')
bye = ('Pluto')

writeletter(name, bye, text)

