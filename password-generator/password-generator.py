# Use an import statement at the top
import random
word_file = "C:/version-control/learning-python/password-generator/words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if len(word) > 3 and len(word) < 8:
            word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    """Takes word_list and returns three random strings from it concatenated.
    """
    password = ""
    for i in range(3):
        password += random.choice(word_list)

    return password

print(generate_password())
