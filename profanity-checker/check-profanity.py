def readText(file):
    quotes = open(file)
    contents = quotes.read()
    print(contents)

readText("C:/version-control/learning-python/profanity-checker/movie_quotes.txt")
