import re

def readText(file):
    quotes = open(file)
    contents = quotes.read()
    print(contents)
    regex = re.compile(r"fuck|shit|ass|dick|piss|cunt|damn|bastard|bitch|hell", re.IGNORECASE)
    list = regex.findall(contents)
    print(list)




readText("C:/version-control/learning-python/mini-projects/profanity-checker/movie_quotes.txt")
