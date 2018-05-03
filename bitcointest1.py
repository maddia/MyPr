# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 12:56:09 2017

@author: Magda
"""

import os, sys
import pandas as pd
import datetime
#change directory
os.chdir('C:/Users/Magda/Desktop/Data An/PfBD/Project')
#get current working directory
os.getcwd()
from pandas import read_csv
data = read_csv('bitcoin.csv')
# check how data looks like
print(data.head())
print(data.shape)
print(data.describe())
print(data.dtypes)
#CLEANING
# First I make copy of data
df= data.copy()
# check for column with date to make sure that it only contains Dates, no names or anything other
print(df.Date.value_counts().sort_index())
#check for leading space
print(df.columns)
# find any Nan values
print(df.isnull().any())
# find duplicates in dates column if any
import collections
print [item for item, count in collections.Counter(data).items() if count > 1]
print(df.head(10))
# first colum Date, change for format of Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
# creating new column with year and month
df['mnth_yr'] = df['Date'].apply(lambda x: x.strftime('%B-%Y'))
df['YEAR'] = pd.DatetimeIndex(df['Date']).year
df['MONTH'] = pd.DatetimeIndex(df['Date']).month
print(df.head())
print(df.tail())

#  Filtering Pandas data frame
x = data['Volume']>200000    
data[x]

#save clean data
df.to_csv('bitcoin_clean_data.csv', encoding='utf8')

# Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

df.Ask.plot(kind = 'line', color = 'g',label = 'Asking Price',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Bid.plot(color = 'r',label = 'Bid Price',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('Time')              # label = name of label
plt.ylabel('Price')
plt.title('Line Plot of Price over Time')  

df.Volume.plot(kind = 'line', color = 'g',label = 'Asking Price',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('Time')              # label = name of label
plt.ylabel('Volume')
plt.title('Line Plot of Volume over Time')  

df.plot(kind='scatter', x='Volume', y='Ask',alpha = 0.5,color = 'red')
plt.xlabel('Volume')              # label = name of label
plt.ylabel('Asking price')
plt.title('Volume - Asking price Correlation')

