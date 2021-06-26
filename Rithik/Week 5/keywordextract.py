# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:22:02 2021

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
   if(type(df.iat[i,5])==str):
       rake_nltk_var = Rake(max_length=2)# intializing the max no of words of keyphrase as 2
       rake_nltk_var.extract_keywords_from_text(df.iat[i,5])#rake keyword extract function
       rake_nltk_var2 = Rake(max_length=2)# intializing the max no of words of keyphrase as 2
       rake_nltk_var2.extract_keywords_from_text(df.iat[i,3])
       keyword_extracted1 = rake_nltk_var.get_ranked_phrases()
       keyword_extracted2 = rake_nltk_var2.get_ranked_phrases()
       for i in keyword_extracted1:
         c.append(i)
         if len(i)>=2:
          if i.isnumeric():
           continue
      
          keyphrase[i]=keyphrase.get(i,0)+1
       for i in keyword_extracted2:
         c.append(i)
         if len(i)>=2:
          if i.isnumeric():
           continue
      
          keyphrase[i]=keyphrase.get(i,0)+1
#printing the keyphrases in a sorted manner of occurance

sortedkey = sorted(keyphrase.items(), key=lambda x: x[1])   
for i in sortedkey:
 print(i)
