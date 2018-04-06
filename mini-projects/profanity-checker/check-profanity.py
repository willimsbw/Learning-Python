def readText(file):
    quotes = open(file)
    contents = quotes.read()
    print(contents)

readText("C:/version-control/learning-python/mini-projects/profanity-checker/movie_quotes.txt")
