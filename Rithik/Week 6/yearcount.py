# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:54:21 2021

@author: Rithik
"""


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

word="ai"
for j in range(2005,2022):
 title=[]
 data=[]
 des=[]
 for i in df.index:
    if int(df["year"][i])==j:
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
  

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
tick_label = [2005, 2006, 2007, 2008, 2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
  
# plotting a bar chart
plt.plot(tick_label,mon)  
# naming the x-axis
plt.xlabel('year')
# naming the y-axis
plt.ylabel('count')
# plot title
plt.title(word)
  
# function to show the plot
plt.show()