# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:37:35 2020

Refered the Nikkei 225 index from the following site
<a href='https://www.macrotrends.net/2593/nikkei-225-index-historical-chart-data'>Nikkei 225 Index - 67 Year Historical Chart</a>
"""
import csv
from datetime import datetime

path = 'nikkei-225-index-historical-chart-data.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)  # The first line is the hearder

data = []
for row in reader:
    #

# """
# Retrieve data from CSV file
# """
# # with open(csvFile, mode='r', encoding='utf_8', newline='') as f_in:
# # with open(csvFile, mode='r', encoding='shift_jis', newline='') as f_in:
# #     reader = csv.reader(f_in)
# #     data_array = [row for row in reader]
# col_names = [ 'c{0:02d}'.format(i) for i in range(30)] # c00-c29までのカラムを作る
# df = pd.read_csv(csvFile, names=col_names)
# # df2 = df.iloc[i : i + 20] for i in range(16, len(df.index))

# df2 = df.loc[:, ['c00', 'c01']].rename(columns={'c00' : 'date', 'c01' : 'price'})
# df3 = df2[9:len(df2.index)]


# """
# Change culumn type from string to datetime
# """
# df4 = pd.to_datetime(df3['date'])


# plot_x = []
# plot_y = []

# # df2 = pd.concat([df.iloc[i : i + 40] for i in range(0, len(df.index), 200)])
