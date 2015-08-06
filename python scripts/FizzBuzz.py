# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:46:33 2015

@author: Graham
"""

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0 :
        print "FizzBuzz"
    elif x % 3 == 0:
        print "Fizz"
    elif x % 5 == 0:
        print "Buzz"
    else: 
        print x 