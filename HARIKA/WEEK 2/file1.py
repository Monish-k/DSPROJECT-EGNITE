from rake_nltk import Rake
import feedparser
import pandas as p
import urllib



try:
   a = p.read_csv('file1.csv', header=0)
except:
   a = p.DataFrame()
finally:
 f=urllib.request.urlopen("https://towardsdatascience.com/feed")
 feed = feedparser.parse(f)
 c={}

 for i in feed.entries:
   rake_nltk_var = Rake()
   rake_nltk_var.extract_keywords_from_text(i.title)
   keyword_extracted = rake_nltk_var.get_ranked_phrases()

   for k in keyword_extracted:
     s=k.split(" ")
     for h in s :
      if h.isnumeric():
          continue
      c[h]=c.get(h,0)+1
 a=p.DataFrame(c.items())
 a.to_csv("file1.csv",index=False)
 print(a)