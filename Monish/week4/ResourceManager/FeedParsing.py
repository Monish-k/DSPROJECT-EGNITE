import feedparser
'''
feed = feedparser.parse("http://themainstreamseer.blogspot.com/feeds/posts/default?alt=rss")

result = re.findall(r"<p>(.*?)</p>", str(feed.entries[0].summary))
print(result)

result = re.sub('<[^<]+>', repl="", string=str(result[0]))
time.struct_time(tm_year=2021, tm_mon=1, tm_mday=17, tm_hour=1, tm_min=57, tm_sec=0, tm_wday=6, tm_yday=17, tm_isdst=0)
print(result)
'''

Entire = open("total_data.txt", "a")

feedurl = open("/Users/monish/code/Data-Science/DSWP-Egnite/Monish/week4/UrlManager/FeedUrl.txt", "r")
Urls = feedurl.read().split("\n")

for i, url in enumerate(Urls):

    f = open("{}.txt".format(i+1), "r+")
    title_list = f.read().split("\n")
    feed = feedparser.parse(url)

    for entry in feed.entries:

        if entry.title.lower() in title_list:
            continue

        Entire.write((entry.title.replace(","," ")+ "," + str(entry.published_parsed.tm_year).replace(","," ") + "," + str(entry.published_parsed.tm_mon).replace(","," ")+ "," +
                     str(entry.published_parsed.tm_mday).replace(","," ")+ "," + str(entry.published_parsed.tm_hour).replace(","," ")).lower()+"\n")
        f.write(entry.title.lower()+"\n")

    f.close()

Entire.close()
feedurl.close()