# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:51:51 2021
@author: Rithik
"""

import feedparser
import csv
import re
import pandas as pd
with open("feeds.csv", 'a',newline='',encoding="utf-8") as f:
 cvs_out = csv.writer(f) #file open 
#open the Feedurl file and read the links
 feedurl=open("FEEDUrl.txt","r")
 line=feedurl.read()
 line=line.split("\n")
#opening each link and parsing it
 for i in line:
    try:
        feed = feedparser.parse(i)
    except:
        continue
    
    dates1=[]
    dates2=[]
    dates3=[]
    titles = []
    links = []
    des=[]
    try:
     for i in feed.entries:
        #extracting date and title of each rss feed
        
        date1= int(i.published_parsed.tm_year)
        date2=int(i.published_parsed.tm_mon)
        date3=int(i.published_parsed.tm_mday)
        dates1.append(date1)
        dates2.append(date2)
        dates3.append(date3)
        titles.append(i.title)
        
        links.append(i.link)
        try:
         summary = re.sub(r",","",i.summary)
         summary = re.sub(r"<[^>]*>","",summary)     
         Summary = re.sub(r"\n"," ",summary)
         des.append(summary)
        except:
            des.append=""
        #storing the details in csv file
     for d1,d2,d3,t,l,d in zip(dates1,dates2,dates3,titles,links,des):
         
         cvs_out.writerow((d1,d2,d3,t,l,d))
    except:
        continue
f.close()
#update by removing the duplicates

df = pd.read_csv("feeds.csv",index_col=None, sep=',', error_bad_lines=False, dtype='unicode')
df=df.drop_duplicates()#remove duplicates

df.to_csv("feeds.csv",index=False)
