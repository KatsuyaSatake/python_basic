# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:38:59 2020

@author:
Refered URL
https://qiita.com/trami/items/bd54f22ee4449421f2bc
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as npf
import datetime

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
path = 'nikkei-225-index-historical-chart-data.csv'

# add_subplot()でグラフを描画する領域を追加。
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
# ax3 = fig.add_subplot(2,1,3)
# ax4 = fig.add_subplot(2,1,4)

# グラフのスタイル設定
c1,c2,c3,c4 = "bule","green","red","black"
l1,l2,l3,l4 = "label1","label2","label3","label4"


'''
CSVファイル(セパレータ=’,’)をDataFrameとして取り込む
'''
df = pd.read_csv(path)

df['new-date'] = pd.to_datetime(df['date'])
df1 = df.loc[:, ['new-date', ' value']]

ax.plot(df1['new-date'], df1[' value'])
ax.grid(True)
# ax1.plot(df1['new-date'], df1[' value'])
# ax2.plot(df1['new-date'], df1[' value'])
# ax1.grid(True)
# ax2.grid(True)
