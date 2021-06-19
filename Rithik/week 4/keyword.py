# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:21:29 2021

@author: Rithik
"""
import pandas as pd

from rake_nltk import Rake

df = pd.read_csv("newfeed1.csv",index_col=None, sep=',', error_bad_lines=False, dtype='unicode')
df[["year", "month","day"]] = df[["year", "month","day"]].apply(pd.to_numeric)
c=[]
keyphrase={}
#extract keyphrases from title and keep count of its occurance
for i in range(len(df.index)):
   rake_nltk_var = Rake(max_length=2)# intializing the max no of words of keyphrase as 2
   rake_nltk_var.extract_keywords_from_text(df.iat[i,3])#rake keyword extract function
   keyword_extracted = rake_nltk_var.get_ranked_phrases()
   for i in keyword_extracted:
    c.append(i)
    if len(i)>=2:
      if i.isnumeric():
          continue
      
      keyphrase[i]=keyphrase.get(i,0)+1
#printing the keyphrases in a sorted manner of occurance

sortedkey = sorted(keyphrase.items(), key=lambda x: x[1])   
for i in sortedkey:
 print(i)
print("\n machine learning  ",keyphrase["machine learning"])