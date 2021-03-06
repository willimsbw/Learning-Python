headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
def create_news_ticker(headlines):
    """
    Takes an array of headlines and joins them into a string that's exactly 140
    characters long, containing as many headlines as possible with a space
    between each one.
    """
    #ticker = ""
    #for headline in headlines:
        #if len(ticker) + len(headline)+1 > 140:
            #if headline and a space would put ticker over the line, truncate
            #the headline, add it, and break
            #letters_to_keep = 140 - len(ticker)
            #truncated_headline = headline[:letters_to_keep]
            #ticker += truncated_headline
            #print("final ticker is: " + ticker)
            #break
        #else:
            #ticker += headline + " "
            #print("ticker is now: " + ticker)

    #return ticker
    ticker = ""
    for headline in headlines:
        ticker += headline + " "
        if len(ticker) >= 140:
            ticker = ticker[:140]
            break

    return ticker

print(create_news_ticker(headlines))
