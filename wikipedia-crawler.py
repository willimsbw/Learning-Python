import requests
from bs4 import BeautifulSoup

def continue_crawl(search_history, target_url):
    """
    Returns False if target_url is in search_history, search_history contains
    more than 25 values, or target_url doesn't contain an anchor element
    search_history: list. Pages already visited
    target_url: string. A url
    """

    html = requests.get(target_url).text #html from target_url as string
    soup = BeautifulSoup(html, "html.parser") #soup object version of html for easy parsing

    #if more than 25 pages checked
    if len(search_history) > 25:
        return False
    #if we've seen this url before
    elif target_url in search_history:
        return False
    #if there are no links on the page
    elif len(soup.find_all('a')) == 0:
        return False
    elif target_url == "https://en.wikipedia.org/wiki/Philosophy":
        return False
    else:
        return True

print(continue_crawl(["https://en.wikipedia.org/wiki/Main_Page", "https://en.wikipedia.org/wiki/taxon"], "https://en.wikipedia.org/wiki/Main_Page"))
print(continue_crawl(["https://en.wikipedia.org/wiki/Main_Page", "https://en.wikipedia.org/wiki/taxon"], "https://en.wikipedia.org/wiki/Cladistics"))
print(continue_crawl(["https://en.wikipedia.org/wiki/Main_Page", "https://en.wikipedia.org/wiki/taxon"], "https://en.wikipedia.org/wiki/Philosophy"))
