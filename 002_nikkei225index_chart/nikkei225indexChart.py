# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:37:35 2020

Refered the Nikkei 225 index from the following site
<a href='https://www.macrotrends.net/2593/nikkei-225-index-historical-chart-data'>Nikkei 225 Index - 67 Year Historical Chart</a>
"""
# import modules
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

path = 'nikkei-225-index-historical-chart-data.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)

data = []
for row in reader:
    # row = [date, value]
    date = datetime.strptime(row[0], '%Y-%m-%d')
    price = float(row[1]) # Nikkei 225 price
    data.append([date, price])

#print(data[-1])

returns_path = 'Nikkei-225-index-return.csv'
file = open(returns_path, 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Date","Price"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[1]
    
    formatted_date = todays_date.strftime('%Y/%m/%d')
    writer.writerow([formatted_date, todays_price])

# Drowing chart
plt.grid(True)
plt.title('Nikkei 225 index per daily')
plt.xlabel('Date')
plt.ylabel('Price')

# for i in range(len(data) - 1):
#     todays_line = data[i]
#     plt.plot(todays_line[0], todays_line[1])


# """
# Retrieve data from CSV file[1,2,3] + [4*i for i in range(1,32)]
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
