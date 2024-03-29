# -*- coding: utf-8 -*-
"""
Created on Sun Sep 06 16:07:56 2015

@author: Graham
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#print list(loansData)
#print loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate
#print loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length
#print loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range

# Attempting to remove the % sign
# Experimenting with 1 of the first 5 values
x = loansData['Interest.Rate'][0:5].values[1]  # .values[1] grabs the first the value at index 1

# x = x.rstrip('%') ###### Removes the % from the end
# x = float(x)      ###### Converts x to a number
# x = x / 100       ###### Because this is a percentage
# x = round(x, 4)   ###### We don't need more precision than 4 digits

# Combine all of the above into a single Lambda function 
y = lambda x: round(float(x.rstrip('%')) / 100, 4)

# print y(x)

# now we need to map this lambda function
# over all of the values in loansData['Interest.Rate']. For this, Python has
# a method called .map()

# map(...)
   #  map(function, sequence[, sequence, ...]) -> list
    
   # Return a list of the results of applying the function to the items of
   # the argument sequence(s).  If more than one sequence is given, the
   # function is called with an argument list consisting of the corresponding
   # item of each sequence, substituting None for missing values when not all
   # sequences have the same length.  If the function is None, return a list of
   # the items of the sequence (or a list of tuples if more than one sequence).
    
# Store the result in a variable so we don't overwrite our data right away,
# in case something goes wrong
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

# For this one, we'll split the numbers and replace it with a list of
# two numbers in the form of [start, end]. Unfortunately, we'll need to
# use multiple passes - we can't just do it all in one .map(lambda...)
# First we'll use the .split() method.

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))

# print cleanFICORange[0:5].values[0]       ####### why does ths only return 1 number?
# print type(cleanFICORange[0:5].values[0])
# print cleanFICORange[0:5].values[0][0]    ####### why does this return the 1st # and not the 2nd, or not both?
# print type(cleanFICORange[0:5].values[0][0])

# This is a start. As you can see, we have only a list of strings. Now,
# for each string inside of each list, we need to convert it to an integer.
# But, we'll have to get inside each list. To do that, we can use a list
# comphrehension. The list comp starts here...| and ends here...|
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
# print cleanFICORange[0:5]                 ####### where did the commas come from?

# Now we can replace the column in our data frame with the cleaned data
loansData['FICO.Range'] = cleanFICORange

# print '\n'
# print cleanInterestRate
# print '\n'
# print cleanLoanLength
# print '\n'
# print cleanFICORange
# print '\n'
# print loansData['FICO.Range']

#### Loop to pull out bottem end of FICORange and store in new list
cleanFICOScore = []
for x, y in loansData['FICO.Range']:
    cleanFICOScore.append(x)


#################################
#Why do these variables not store/replace the dataframe values?
#################################

loansData['FICO.Score'] = cleanFICOScore
loansData['Interest.Rate'] = cleanInterestRate
loansData['Loan.Length'] = cleanLoanLength
loansData['Loan.Range'] = cleanFICORange


# print loansData['FICO.Score']    
    
# plot a histogram of FICO scores
#plt.figure()
#p = loansData['FICO.Score'].hist()
#plt.show()

# create a scatterplot matrix 
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')


#############################
#Deriving our linear model
#############################

intrate = cleanInterestRate
loanamt = loansData['Amount.Requested']
fico = cleanFICOScore

#When we extract a column from a DataFrame, it's returned as a #######Series datatype?######
#You want to reshape the data like this:
 
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

###############
#What is all this matrix stuff?
################

#Now you want to put the two columns together to create an input matrix
#(with one column for each independent variable):

x = np.column_stack([x1,x2])

#our linear model

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()
