
# Open the input file in read mode
with open('words.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()

# Reverse the content
reversed_content = content[::-1]

# Open the output file in write mode
with open('words_reverse.txt', 'w') as file:
    # Write the reversed content to the output file
    file.write(reversed_content)