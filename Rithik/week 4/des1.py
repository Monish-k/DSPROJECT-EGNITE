# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:37:43 2021

@author: Rithik
"""

import bs4 as bs
import urllib.request

import csv

des=[]
count=0
f=open("FEEDUrl.txt","r")#opening links file
l=f.read()
l=l.split("\n")
file=""
for i in l:
 file=str(count)+".csv" #creating file names with link number
 cvs_out = csv.writer(open(file, 'w',newline='',encoding="utf-8"))  #open file write mode
 count=count+1
 try:
  source = urllib.request.urlopen(i).read()
  soup = bs.BeautifulSoup(source,'lxml')
  
  for i in soup.find_all('p'):#finding paragraph
   
    if(i.string!=None):
     des.append(i.string)
  cvs_out.writerow(des)#write the data
  des=[]
   
 except:
     continue
print(des)