# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:23:32 2021

@author: Rithik
"""
import pandas as pd
import numpy as np

df = pd.read_csv("feeds.csv",index_col=None, sep=',', error_bad_lines=False, dtype='unicode')
df=df.drop_duplicates()#remove duplicates

df['title'].replace('', np.nan, inplace=True)#remove missing values
df.dropna(subset=['title'], inplace=True)
df[["year", "month","day"]] = df[["year", "month","day"]].apply(pd.to_numeric)
df=df.sort_values(['year', 'month','day'],ascending=False)#sorting date
df.to_csv("newfeed1.csv",index=False)
