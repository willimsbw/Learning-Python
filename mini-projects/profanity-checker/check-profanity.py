import re

def readText(filePath):
    """
    Opens a txt file from filePath and returns its contents as a string

    filePath: string. Filepath to a txt file
    """
    quotes = open(filePath)
    contents = quotes.read()
    return contents

def censorProfanity(str):
    """
    Finds instances of profanity in a string and returns a version of the string
    with the second letter of each profane word replaced with a *.
    """

    def censor(profanity):
        """
        Takes in a string and replaces its second value with a *.
        """
        #break matched profanity into a list of characters
        listChars = list(profanity.group())
        #replace the second character with *
        listChars[1] = "*"
        #return the list of characters rejoined into a single string
        censored = "".join(listChars)
        return censored

    #regex that identifies curse words
    regex = re.compile(r"fuck|shit|ass|dick|piss|cunt|damn|bastard|bitch|hell", re.IGNORECASE)

    if bool(regex.search(str)):
        print("We think we've found profanity! Here's a censored version")
        #for each curse word found in str, replace it with a censored version. Then
        #return str with each curse word censored.
        return regex.sub(censor, str)
    else:
        return "No profanity found here!"

text = readText("C:/version-control/learning-python/mini-projects/profanity-checker/movie_quotes.txt")
censoredText = censorProfanity(text)
print(censoredText)
