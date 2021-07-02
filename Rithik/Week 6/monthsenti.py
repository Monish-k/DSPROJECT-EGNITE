# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:03:46 2021

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

word="data science"
for j in range(1,13):
 title=[]
 data=[]
 des=[]
 for i in df.index:
    if int(df["year"][i])==2021 and int(df["month"][i])==j:
        title.append(df["title"][i])
        des.append(df["description"][i])
 data=data+title+des
 c=[]
 s=0
 keyphrase={}
 for j in data:
    if(type(j)==str):
        
        
        if word in j:

         
           sid = SentimentIntensityAnalyzer()
           s=s+(sid.polarity_scores(j)["pos"])
          
 mon.append(int(s*1000))
print(mon)

a=[1,2,3,4,5,6,7,8,9,10,11,12]
  
# labels for bars
tick_label = ['jan', 'feb', 'mar', 'apr', 'may','jun','jul','aug','sep','oct','nov','dec']
  
# plotting a bar chart
plt.bar(a,mon, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('month')
# naming the y-axis
plt.ylabel('popularity')
# plot title
plt.title(word+" 2021")
  
# function to show the plot
plt.show()