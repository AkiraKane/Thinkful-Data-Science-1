# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:23:20 2015

@author: geckel02
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#### Check column names
#print list(loansData)

#### the underlying Lambda function
#y = lambda x: round(float(x.rstrip('%')) / 100, 4)

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
loansData['FICO.Range'] = cleanFICORange

#### Loop to pull out bottem end of FICORange and store in new list
cleanFICOScore = []
for x, y in loansData['FICO.Range']:
    cleanFICOScore.append(x)

loansData['FICO.Score'] = cleanFICOScore
loansData['Interest.Rate'] = cleanInterestRate
loansData['Loan.Length'] = cleanLoanLength
loansData['Loan.Range'] = cleanFICORange

##### check to see if data is clean and prints
#print loansData

#### Histogram of FICOScore
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

#### Scatterplot Matrix of loansData
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

#### Pulling out data to regress
intrate = cleanInterestRate
loanamt = loansData['Amount.Requested']
fico = cleanFICOScore

#############################
# What am I doing with this linear equation and why didn't I derive the actual equation?
#############################
#InterestRate = b + a1(FICOScore) + a2(LoanAmount)

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

#### Linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

###############
# what's the difference between our linear model and our linear equation?
##############

#### OLS Regression Results
print f.summary()

###################################
#How do I recreate that graph of the linear regression analysis?
###################################