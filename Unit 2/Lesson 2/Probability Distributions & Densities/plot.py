# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 21:53:45 2015

@author: Graham
"""

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

testlist = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(testlist)

print "\n"
print c

count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)
  
plt.boxplot(testlist)
plt.show()

plt.hist(testlist, histtype='bar')
plt.show()

plt.figure()
test_data = testlist   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()
plt.figure()

# does the for loop create a dictionary?
# how do I label my graphs?