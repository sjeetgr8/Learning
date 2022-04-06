# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:09:36 2022

@author: Satya
"""
import pandas as pd 
import numpy as np 


data=[[5,10],
      [10,10],
      [9,7]]

data
df1=pd.DataFrame(data)
df1 

np.cov(df1)
