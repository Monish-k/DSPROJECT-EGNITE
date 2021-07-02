# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:23:06 2021

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
print(df['day'][1])
title=[]
des=[]
word="data"
from datetime import date, timedelta
mon=[]
label=[]
current_date = date.today()
prev=current_date - timedelta(2)
curr=str(current_date).split("-")
past=str(prev).split("-")
print(curr[1],curr[2],past[1],past[2])
for i in range(0,7):
 current_date = date.today()
 prev=current_date - timedelta(i)
 curr=str(current_date).split("-")
 past=str(prev).split("-")
 label.append(past[1]+"-"+past[2])
 title=[]
 data=[]
 des=[]
 for j in df.index:
     if df['day'][j]==int(past[2]) and df['month'][j]==int(past[1]) and df['year'][j]==int(past[0]):
        title.append(df["title"][i])
        des.append(df["description"][i])
        
 data=data+title+des
 c=[]
 keyphrase={}
 for i in data:
    if(type(i)==str):
     rake_nltk_var = Rake(max_length=2)# intializing the max no of words of keyphrase as 2
     rake_nltk_var.extract_keywords_from_text(i)#rake keyword extract function
     keyword_extracted1 = rake_nltk_var.get_ranked_phrases()

     for i in keyword_extracted1:
         c.append(i)
         if len(i)>=2:
          if i.isnumeric():
           continue
      
          keyphrase[i]=keyphrase.get(i,0)+1
    else:
         continue
 try:
   mon.append(keyphrase[word])
 except:
     mon.append(0)
print(mon)
  

a=[1,2,3,4,5,6,7]
  
print(label)
  
# plotting a bar chart
plt.bar(a,mon,tick_label=label,
        width = 0.8, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('week')
# naming the y-axis
plt.ylabel('count')
# plot title
plt.title(word+" 2021")
  
# function to show the plot
plt.show()