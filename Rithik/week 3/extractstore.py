# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:51:51 2021
@author: Rithik
"""
import urllib
import feedparser
import csv
cvs_out = csv.writer(open("feeds.csv", 'w',newline='',encoding="utf-8"))

f=open("FEEDUrl.txt","r")
l=f.read()
l=l.split("\n")
for i in l:
    try:
        f=urllib.request.urlopen(i)
    except:
        continue
    feed = feedparser.parse(f)
    dates1=[]
    dates2=[]
    dates3=[]
    titles = []
    links = []
    try:
     for i in feed.entries:
        date1= int(i.published_parsed.tm_year)
        date2=int(i.published_parsed.tm_mon)
        date3=int(i.published_parsed.tm_mday)
        dates1.append(date1)
        dates2.append(date2)
        dates3.append(date3)
        titles.append(i.title)
        
        links.append(i.link)
        for d1,d2,d3,t,l in zip(dates1,dates2,dates3,titles,links):
           cvs_out.writerow((d1,d2,d3,t,l))
    except:
        continue
