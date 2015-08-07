# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:49:14 2015

@author: Graham
"""

from collections import defaultdict
population_dict = defaultdict(int)

with open('C:/Users/Graham/Documents/Thinkful Data Science/\
lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line [5]
inputFile.close()

print population_dict