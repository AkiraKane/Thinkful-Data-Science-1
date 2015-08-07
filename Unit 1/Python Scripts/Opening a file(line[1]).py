# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:59:48 2015

@author: Graham
"""

with open('C:/Users/Graham/Documents/Thinkful Data Science/\
lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population': 
            print line