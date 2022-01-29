# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:57:13 2022

@author: Satya
"""
"""

Chapter 2 content

Creating a candlestick chart
Backtesting a strategy based on simple moving average
Calculating Bollinger Bands and testing a buy/sell strategy
Calculating the relative strength index and testing a long/short strategy
Building an interactive dashboard for TA


"""
pip install cufflinks
pip install chart_studio

import pandas as pd
import yfinance as yf

import cufflinks as cf
from plotly.offline import iplot, init_notebook_mode

init_notebook_mode()

df_twtr = yf.download('TWTR',
                       start='2018-01-01',
                       end='2018-12-31',
                       progress=False,
                       auto_adjust=True)

qf = cf.QuantFig(df_twtr, title="Twitter's Stock Price",
                 legend='top', name='TWTR')

qf.add_volume()
qf.add_sma(periods=20, column='Close', color='red')
qf.add_ema(periods=20, color='green')
qf.iplot()
