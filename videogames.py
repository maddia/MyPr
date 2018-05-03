# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:22:15 2017

@author: MagdaData An/PfBD/Project')

"""

import pandas as pd
import numpy as np
import os
#change directory
os.chdir('C:/Users/Magda/Desktop//Data An/PfBD/Project')
#get current working directory
os.getcwd()
from pandas import read_csv
data = read_csv('vgsales.csv')
# check how data looks like
data.info()
print(data.head())
print(data.shape)
print(data.describe())
print(data.dtypes)
#CLEANING
# First I make copy of data
df= data.copy()
#check for leading space
print(df.columns)
# find any Nan values
print(df.isnull().any())
print(df.isnull().sum())
# find duplicates in columns if any
import collections
print [item for item, count in collections.Counter(df).items() if count > 1]
print(df.head(10))
#  Filtering Pandas data frame
x = df['Year']>2016   
data[x]

#another dataframe without crazy value in Year column
df1 = df[df.Year<2018]
y = df1['Year']>2016   
print(df1.describe)


#save clean data
df1.to_csv('video_clean_data.csv', encoding='utf8')
#data visiualisation
import matplotlib.pyplot as plt
import seaborn as sns
#correlation map
plat = df.groupby('Platform', sort = True)
f,ax = plt.subplots(figsize=(22, 22))
# heatmap
sns.heatmap(df.corr(), annot=True, linewidths=.11, fmt= '.1f',ax=ax)

