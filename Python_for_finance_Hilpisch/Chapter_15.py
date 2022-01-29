# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:32:22 2022

@author: Satya
"""

import os
import numpy as np
import pandas as pd
import datetime as dt
from pylab import mpl, plt

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
## jupyter %matplotlib inline

os.chdir("D:\Learning\Python for finance- Hilpisch\source")
raw = pd.read_csv('tr_eikon_eod_data.csv', index_col=0, parse_dates=True)

raw.info()

symbol = 'AAPL.O'

data = ( pd.DataFrame(raw[symbol]).dropna() )

SMA1 = 42
SMA2 = 252

data['SMA1'] = data[symbol].rolling(SMA1).mean()
data['SMA2'] = data[symbol].rolling(SMA2).mean()

data.plot(figsize=(10, 6));

data.dropna(inplace=True)
data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
data.tail()

ax = data.plot(secondary_y='Position', figsize=(10, 6))
ax.get_legend().set_bbox_to_anchor((0.25, 0.85));

###   Vectorized Backtesting


###   Optimization
















































""""            *************   Working notes   **********

IPython has a set of predefined ‘magic functions’ that you can call with a command line style syntax.
There are two kinds of magics, line-oriented and cell-oriented. 
Line magics are prefixed with the % character and work much like OS command-line calls: 
    they get as an argument the rest of the line, where arguments are passed without parentheses or quotes. 
    Lines magics can return results and can be used in the right hand side of an assignment. 


Cell magics are prefixed with a double %%, and they are functions that get as an argument not only the rest of the line, but also the lines below it in a separate argument.



























