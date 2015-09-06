# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 22:00:55 2015

@author: Graham
"""


import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Load Lending Data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#print loansData

#Remove rows with null values
loansData.dropna(inplace=True)

#Generate a Box Plot
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

#Generate a Histogram     WHY DO PLOTS REMAIN WHEN PLT.SHOW() IS REMOVED?
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

#Generate a QQ Plot
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

