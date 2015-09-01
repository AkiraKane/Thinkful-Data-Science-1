# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:40:31 2015

@author: Graham
"""


"""Write a script called "stats.py" that prints the mean, median, mode, 
range, variance, and standard deviation for the Alcohol and Tobacco 
dataset with full text (ex. "The range for the Alcohol and 
Tobacco dataset is ..."). Push the code to Github and enter the link below.
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

print df

