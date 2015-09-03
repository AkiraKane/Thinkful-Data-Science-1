# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:16:58 2015

@author: Graham
"""

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.split('\n')
# why didn't data.splitlines work?

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
                        # what do the colons do?

df = pd.DataFrame(data_rows, columns = column_names)

#print df

#############################

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

Alc_Mean = df['Alcohol'].mean()
Alc_Median = df['Alcohol'].median()
Alc_Mode = stats.mode(df['Alcohol'])
Alc_Range = max(df['Alcohol']) - min(df['Alcohol'])
Alc_Std = df['Alcohol'].std() 
Alc_Var = df['Alcohol'].var()

Tob_Mean = df['Tobacco'].mean() 
Tob_Median = df['Tobacco'].median() 
Tob_Mode = stats.mode(df['Tobacco']) 
Tob_Range = max(df['Tobacco']) - min(df['Tobacco'])
Tob_Std = df['Tobacco'].std()
Tob_Var = df['Tobacco'].var() 

print '\n'
print 'The mean for the Alcohol dataset is: %s' % Alc_Mean
print 'The median is: %s' %  Alc_Median
print Alc_Mode
print 'The range is: %s' % Alc_Range
print 'The standard deviation is: %s' % Alc_Std
print 'The variance is: %s' %  Alc_Var

print '\n' 
print 'The mean for the Tobacco dataset is: %s' % Tob_Mean
print 'The median is: %s' %  Tob_Median
print Tob_Mode
print 'The range is: %s' % Tob_Range
print 'The standard deviation is: %s' % Tob_Std
print 'The variance is: %s' %  Tob_Var