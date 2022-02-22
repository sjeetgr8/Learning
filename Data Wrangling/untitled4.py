# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:20:23 2022

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


## Task is to find those serial No which is missing from 1 to 10 

