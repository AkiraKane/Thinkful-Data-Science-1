# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 22:05:43 2015

@author: Graham
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Load Lending Data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Prints column names to a list
#print loansData.columns.values.tolist()
#print list(loansData)

#Remove rows with null values
loansData.dropna(inplace=True)

#Generate a Box Plot
loansData.boxplot(column='Amount.Requested')
plt.show()

#Generate a Histogram     WHY DO PLOTS VISUALS REMAIN WHEN PLT.SHOW() IS REMOVED?
loansData.hist(column='Amount.Requested')
plt.show()

#Generate a QQ Plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()