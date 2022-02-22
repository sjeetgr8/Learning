# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:34:28 2022

@author: Satya
"""

import numpy as np
import pandas as pd

x=np.NaN
x

data1= [[1,7,x,x,x,x,x],
        [4,x,x,x,8,x,x],
        [6,x,6,x,x,x,x],
        [7,x,x,5,x,x,x],
        [9,x,x,x,x,4,x],
        [10,x,x,x,x,x,1]]


df1=pd.DataFrame(data1,columns=['SlNo','RSID1','RSID2','RSID3','RSID4','RSID5','RSID6'])

df1     


## task is to insert one column after RSID2 column 

index_no = df1.columns.get_loc('RSID2')
index_no

data2=[['hello'],
       ['My'],
       ['Name'],
       ['is'],
       ['Satya'],
       ['jeet']]

data3=['hello',
       'My',
       'Name',
       'is',
       'Satya',
       ]


df1.insert (3, "Sold in Bulk",data3)
df1 


df1.drop(["Sold in Bulk"], axis = 1, inplace = True)
df1.drop("Sold in Bulk", axis = 1, inplace = True)
