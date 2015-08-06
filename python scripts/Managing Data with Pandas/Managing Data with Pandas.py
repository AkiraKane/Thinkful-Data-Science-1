# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:41:59 2015

@author: Graham
"""


import pandas as pd

with open('C:\Users\Graham\Documents\Thinkful Data Science\
/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print len(line)