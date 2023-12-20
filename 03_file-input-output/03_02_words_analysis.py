# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.


def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()

        return len(words)

filename = 'words.txt'
word_count = count_words(filename)
print(f"Total number of words: {word_count}")
