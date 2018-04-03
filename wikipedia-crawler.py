import requests
from bs4 import BeautifulSoup
import time

def find_first_link(url):
    """
    Returns the first anchor element for a given url
    """
    html = requests.get(url).text #html from target_url as string
    soup = BeautifulSoup(html, "html.parser") #soup object version of html for easy parsing
    #The first div with class mw-parser-ouput that"s under the first div with mw-content-text
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    first_link = None #if no link found, we want to return None
    a_href = None #initializing a_href
    #for each of the direct-child <p> elements in content_div
    for element in content_div.find_all("p", recursive=False):
        #for each of the direct-child <a> elements in a given <p> element in content_div
        for link in element.find_all("a", recursive=False):
            a_href = link.get("href")
            if a_href.startswith("/wiki"):
                if a_href.startswith("/wiki/Help"):
                    continue
                else:
                    #make first_link the current element"s first <a>"s href
                    #stop looking
                    first_link = a_href
                    break
        #don't go to the next element, now that we have a first_link or have looked
        #at every link option
        break

    #return the first link
    return first_link

def continue_crawl(search_history, target_url, max_searches=25):
    """
    Returns False if target_url is in search_history, search_history contains
    more than 25 values, or target_url doesn"t contain an anchor element
    search_history: list. Pages already visited
    target_url: string. A url
    max_searches: int. The maximum number of times you want a loop to be able to run. Defaults to 25
    """

    html = requests.get(target_url).text #html from target_url as string
    soup = BeautifulSoup(html, "html.parser") #soup object version of html for easy parsing

    #if more than 25 pages checked
    if len(search_history) > max_searches:
        print("We've looked too many times!")
        return False
    #if we"ve seen this url before
    elif target_url in search_history:
        print("We've already been to this page!")
        return False
    #if we hit the Philosophy page
    elif search_history[-1] == "https://en.wikipedia.org/wiki/Philosophy":
        print("We've hit the Philosophy page!")
        return False
    else:
        return True

while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
