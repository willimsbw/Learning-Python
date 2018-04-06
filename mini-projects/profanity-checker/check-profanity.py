import re

def readText(file):
    quotes = open(file)
    contents = quotes.read()
    return contents

def censorProfanity(profanity):

    def censor(matchedString):
        listChars = list(matchedString.group())
        listChars[1] = "*"
        censored = "".join(listChars)
        return censored

    regex = re.compile(r"fuck|shit|ass|dick|piss|cunt|damn|bastard|bitch|hell", re.IGNORECASE)
    return regex.sub(censor, profanity)

text = readText("C:/version-control/learning-python/mini-projects/profanity-checker/movie_quotes.txt")
censoredText = censorProfanity(text)
print(censoredText)
