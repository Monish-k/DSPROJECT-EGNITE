# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:21:29 2021

@author: Rithik
"""
import pandas as pd
import numpy as np
from rake_nltk import Rake

df = pd.read_csv("newfeed1.csv",index_col=None, sep=',', error_bad_lines=False, dtype='unicode')
df[["year", "month","day"]] = df[["year", "month","day"]].apply(pd.to_numeric)
c={}
for i in list(np.where(df["year"]==2020)[0]):
   rake_nltk_var = Rake()
   rake_nltk_var.extract_keywords_from_text(df.iat[i,3])
   keyword_extracted = rake_nltk_var.get_ranked_phrases()
   for k in keyword_extracted:
     s=k.split(" ")
     for h in s :
      if h.isnumeric() or len(h)<2:
          continue
      c[h]=c.get(h,0)+1
a = sorted(c.items(), key=lambda x: x[1])   
print(a[-20:])