# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:20:01 2020

@author: satake
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as npf

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from pandas_datareader import DataReader
from datetime import datetime

tech_list = ['AAPL', 'GOOG', 'MSFT']

end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

for stock in tech_list:
    globals()[stock] = DataReader(stock, 'yahoo', start, end)
    
AAPL['Adj Close'].plot(legend=True, figsize=(10,4))