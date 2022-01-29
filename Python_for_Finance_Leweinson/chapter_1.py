# -*- coding: utf-8 -*-
"""
Spyder Editor

@Satya -the editor 
This is a temporary script file.
"""


"""
Chapter-1 contents

    * Getting data from Yahoo Finance
    * Getting data from Quandl
    * Getting data from Intrinio
    * Converting prices to returns
    * Changing frequency
    * Visualizing time series data
    * Identifying outliers
    * Investigating stylized facts of asset returns
    
"""



import quandl
QUANDL_KEY = '{key}'         ## You need to replace {key} with your own API key.
quandl.ApiConfig.api_key = QUANDL_KEY
df_quandl = quandl.get(dataset='WIKI/AAPL',
                       start_date='2000-01-01',
                       end_date='2010-12-31')

import intrinio_sdk

import pandas as pd
import yfinance as yf

yf.download?


df_yahoo = yf.download('AAPL',
                       period='max',
                       progress=False)




df = df.loc[:, ['Adj Close']]
df.rename(columns={'Adj Close':'adj_close'}, inplace=True)

df['simple_rtn'] = df.adj_close.pct_change()
df['log_rtn'] = np.log(df.adj_close/df.adj_close.shift(1)


























