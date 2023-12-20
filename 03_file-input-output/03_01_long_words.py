# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


with open('words.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if len(word.replace(" ", "")) > 20:
                print(word)