from feedsearch import search
import feedparser

try:
    url = "https://towardsdatascience.com/"

    fptr = open("FeedUrl.txt", "r")

    FeedUrl = search(url)

    list_url = fptr.read().split("\n")

    if str(FeedUrl[0].url) in list_url:
        quit(1)

    Feed = feedparser.parse(str(FeedUrl[0].url))

    for entry in Feed.entries:
        print(entry.title, entry.published)

finally:
    if fptr:
        fptr.close()
