# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:01:18 2015

@author: Graham
"""

with open('C:/Users/Graham/Documents/Thinkful Data Science/\
lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    line = next(inputFile)
    for header in inputFile:
        header = header.rstrip().split(',')
        print header