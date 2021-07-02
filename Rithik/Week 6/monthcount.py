# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:45:19 2021

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
  

a=[1,2,3,4,5,6,7,8,9,10,11,12]
  
# labels for bars
tick_label = ['jan', 'feb', 'mar', 'apr', 'may','jun','jul','aug','sep','oct','nov','dec']
  
# plotting a bar chart
plt.bar(a,mon, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('month')
# naming the y-axis
plt.ylabel('count')
# plot title
plt.title(word+" 2021")
  
# function to show the plot
plt.show()