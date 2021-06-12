# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:23:32 2021

@author: Rithik
"""
import pandas as pd
import numpy as np
header_list = ["year","month","day", "title", "link"]
df = pd.read_csv("feeds.csv", names=header_list,index_col=None, sep=',', error_bad_lines=False, dtype='unicode')
df=df.drop_duplicates()

df['title'].replace('', np.nan, inplace=True)
df.dropna(subset=['title'], inplace=True)
df[["year", "month","day"]] = df[["year", "month","day"]].apply(pd.to_numeric)
df=df.sort_values(['year', 'month','day'],ascending=False)
df.to_csv("newfeed1.csv",index=False)
