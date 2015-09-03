# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:41:27 2015

@author: Graham
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

mean = 0
variance = 1
sigma = np.sqrt(variance) # this is the standard deviation
x = np.linspace(-3,3,100)
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()