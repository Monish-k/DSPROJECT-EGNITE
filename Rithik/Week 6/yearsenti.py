# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:38:18 2021

@author: Rithik
"""
import nltk

from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
from rake_nltk import Rake
header_list = ["year","month","day", "title", "link","description"]
df = pd.read_csv("newfeed1.csv",index_col=None, sep=',', error_bad_lines=False, dtype='unicode')
df[["year", "month","day"]] = df[["year", "month","day"]].apply(pd.to_numeric)
title=[]
des=[]
data=[]
mon=[]

word="data scientist"
for k in range(2005,2022):
 title=[]
 data=[]
 des=[]
 s=0
 for i in df.index:
    if int(df["year"][i])==k:
        title.append(df["title"][i])
        des.append(df["description"][i])
 data=data+title+des
 c=[]
 keyphrase={}
 for j in data:
    if(type(j)==str):
        
        
        if word in j:
           sid = SentimentIntensityAnalyzer()
           s=s+(sid.polarity_scores(j)["pos"])
 mon.append(int(s*1000))
print(mon)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
tick_label = [2005, 2006, 2007, 2008, 2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
  
# plotting a bar chart
plt.plot(tick_label,mon)  
# naming the x-axis
plt.xlabel('year')
# naming the y-axis
plt.ylabel('popularity')
# plot title
plt.title(word)
  
# function to show the plot
plt.show()