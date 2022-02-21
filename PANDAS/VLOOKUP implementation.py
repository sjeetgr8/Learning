# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:30:56 2022

@author: Satya
"""

""" Functions used
        merge
        join
        map
        apply
        lamda       """

import pandas as pd

# creating two datframes 

data1= [[122,61,True],
      [123,61,True],
      [113,62,True],
      [122,62,True],
      [123,62,False],
      [122,63,False],
      [301,63,True]]

df1= pd.DataFrame(data1,columns=['sku','loc','flag'])
df1

data2=[[113,'a'],
       [122,'b'],
       [123,'b'],
       [301,'c']]

df2= pd.DataFrame(data2,columns=['sku','dept'])
df2 

#merge function

df1.merge(df2, on='sku', how='left')
df1.merge(df2, on='sku', how='right')

#map function---Understanding how map function works
df1['dept']=df1.sku.map(df2.dept)
df1

# Get column index from column name in python pandas
# Purpose is there are many times where you need to lookup and paste the column at a fixed index number
# https://stackoverflow.com/questions/13021654/get-column-index-from-column-name-in-python-pandas



#apply function




#lambda function







