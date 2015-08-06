# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


with open('C:/Users/Graham/Documents/Thinkful Data Science/\
lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    count = sum(1 for line in inputFile)
    print count