# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:37:43 2021

@author: Rithik
"""

import bs4 as bs
import urllib.request

import csv

c=[]
count=0
f=open("FEEDUrl.txt","r")
l=f.read()
l=l.split("\n")
file=""
for i in l:
 file=str(count)+".csv"
 cvs_out = csv.writer(open(file, 'w',newline='',encoding="utf-8"))  #open file write mode
 count=count+1
 try:
  source = urllib.request.urlopen(i).read()
  soup = bs.BeautifulSoup(source,'lxml')
  
  for paragraph in soup.find_all('p'):
    #print(paragraph.string)
    if(paragraph.string!=None):
     c.append(paragraph.string)
  cvs_out.writerow(c)
  c=[]
   # print(str(paragraph.text))
 except:
     continue
print(c)