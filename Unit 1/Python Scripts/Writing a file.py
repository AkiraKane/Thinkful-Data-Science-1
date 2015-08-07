# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:29:55 2015

@author: Graham
"""


with open('national_population.csv', 'w') as outputFile: # how do I write to any directory?
    outputFile.write('continent,2010_population\n') # \n indicates a new line
    for k,v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
