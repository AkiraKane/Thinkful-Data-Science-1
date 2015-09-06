# -*- coding: utf-8 -*-
"""
Created on Sun Sep 06 12:50:36 2015

@author: Graham
"""


from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Prints column names to a list
#print loansData.columns.values.tolist()

# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Monthly.Income'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(freq.values())

print chi
print p