# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:40:58 2022

@author: Satya
"""
## Sources
# * https://www.datasciencelearner.com/how-to-merge-two-columns-in-pandas/


import pandas as pd
import numpy as np
import os

x=np.NaN
x

data1= [[7,x,x,x,x,x],
        [x,x,x,8,x,x],
        [x,6,x,x,x,x],
        [x,x,5,x,x,x],
        [x,x,x,x,4,x],
        [x,x,x,x,x,1]]


df1=pd.DataFrame(data1,columns=['RSID1','RSID2','RSID3','RSID4','RSID5','RSID6'])

df1         

## As you can see every columns has one value but all the columns are same. I need to combine 
## all the rows into one 


# df1['RSID']=df1.RSID1 + df1.RSID2 + df1.RSID3 + df1.RSID4 + df1.RSID5 + df1.RSID6
# df1.RSID

# df1['RSID']=df1.merge(df1.RSID1, df1.RSID2, df1.RSID3,df1.RSID4,df1.RSID5,df1.RSID6).astype(int)

?pd.merge 

##### ###################               2nd

missing = np.nan
actors_name = ["Tom Cruise","Hugh Jackman","Brad Pitt","Johnny Depp","Leonardo DiCaprio"]
actor_age = [57,missing,51,missing,44]
actor_age_revised =[missing,55,missing,56,missing]
df = pd.DataFrame({"name":actors_name,"age1":actor_age,"revised_age":actor_age_revised})

df = df.fillna(0)
df["age"] = (df["age1"] + df["revised_age"]).astype("int")
df = df[["name","age"]]
df



