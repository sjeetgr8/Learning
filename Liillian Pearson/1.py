# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:15:05 2022

@author: Satya
"""


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series_obj=Series(np.arange(8), index=['row1','row2','row3','row4','row5','row6','row7','row8'])

series_obj

# ?np.arange()
# ?arange()

series_obj['row5']
series_obj[0]
series_obj[6]
series_obj[[0,6]]
series_obj['row3':'row7']

np.random.seed(25)
Df_obj=DataFrame(np.random.rand(36).reshape((6,6)),
                 index=['row1','row2','row3','row4','row5','row6'],
                 columns=['column1','column2','column3','column4','column5','column6']
                 )

Df_obj

Df_obj.loc[['row2','row5'],
           ['coulmn5','column2']]

Df_obj <0.2     # Comparing with scalar 

# Treating missing values 
# When to us emissing values and when to replace with the approximate values

missing=np.nan
series_obj2=Series(['row1','row2','row3',missing,'row5','row6',missing,'row8'])
series_obj2.isnull()


np.random.seed(25)
Df_obj2=DataFrame(np.random.rand(36).reshape(6,6))
Df_obj2

Df_obj2.loc[3:5,0]=missing
Df_obj2.loc[1:4,5]=missing
Df_obj2

filled_df=Df_obj2.fillna(0)
filled_df

filled_df=Df_obj2.fillna({0:0.1,
                          5:1.25}
                         )
filled_df

fill_Df=Df_obj2.fillna(method='ffill')
fill_Df

missing=np.nan
series_obj2=Series(['row1','row2','row3',missing,'row5','row6',missing,'row8'])
series_obj2.isnull()

Df_obj2.isna()
Df_obj2.isna().sum()

# Filtering ouyt missing values


## Three different data visualization types
#   Data story telling
#   Data showcasing
#   Data art


"""
#basic maths and statistics
"""


import numpy as np
from numpy.random import randn

np.set_printoptions(precision=2)

#creating an arrays using a list 
a=np.array([1,2,3,4,5,6,76,78])
a

b=np.array([[10,20,20],
           [40,50,60]])
b

# TypeError: Field elements must be 2- or 3-tuples, got '40'


c=np.array([5,6,4,9,4,90,23,45])
c

np.random.seed(25)
d=36*np.random.randn(6)
d

e=np.arange(1,35)
e

#performing arithmetics on arrays 

a*10

c+a
c-999

#basic linear algebra 

a*c

#generating summary statistics 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips);





































































































































