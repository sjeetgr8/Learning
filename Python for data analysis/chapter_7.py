# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:59:08 2022

@author: Satya
"""

import pandas as pd
import numpy as np

from numpy import nan as NA

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data


string_data.isnull()

type(string_data)

string_data[0] = None

string_data.isnull()

"""

NA handling methods

dropna     Filter axis labels based on whether values for each label have missing data, with varying thresholds for how
           much missing data to tolerate.
fillna    Fill in missing data with some value or using an interpolation method such as 'ffill' or 'bfill'.
isnull    Return boolean values indicating which values are missing/NA.
notnull   Negation of isnull.

"""
data = pd.Series([1, NA, 3.5, NA, 7])
data1=data.dropna()
data1
data2=data[data.notnull()]
data2=data


data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                    [NA, NA, NA], [NA, 6.5, 3.]])

cleaned = data.dropna()

data
cleaned

data.dropna(how='all')    # passing how='all' will only drop rows that are all NA:

data[4] = NA
data

data.dropna(axis=1, how='all')

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df.dropna()
df.dropna(thresh=2)   # to keep only rows containing a certain number of observations



## Filling In Missing Data
df.fillna(0)
df.fillna({1: 0.5, 2: 0})


data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())

"""

value Scalar value or dict-like object to use to fill missing values
method    Interpolation; by default 'ffill' if function called with no other arguments
axis      Axis to fill on; default axis=0
inplace   Modify the calling object without producing a copy
limit For forward and backward filling, maximum number of consecutive periods to fill

"""


data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})

data
data.duplicated()
data.drop_duplicates()












