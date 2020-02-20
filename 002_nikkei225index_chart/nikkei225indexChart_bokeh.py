# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:07:07 2020

@author: tfx746
"""

import pandas as pd
# import requests
# import io
import numpy as np
from bokeh.plotting import figure, show #, output_file

def datetime(x):
    return np.array(x, dtype=np.datetime64)

path = 'nikkei-225-index-historical-chart-data.csv'

df = pd.read_csv(path)

df['new-date'] = pd.to_datetime(df['date'])
df1 = df.loc[:, ['new-date', ' value']]

df1['date'] = pd.to_datetime(df1['new-date'])

p1 = figure(x_axis_type="datetime", title='Nikkei 225 index historical chart')
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Value'
p1.ygrid.band_fill_color = "olive"
p1.ygrid.band_fill_alpha = 0.1
p1.line(df1['new-date'], df1[' value'], color='#8000ff', legend_label='USDJP')


show(p1)  # open a browser
