# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:58:47 2015

@author: Graham
"""

def F(n):
    if n < 2:
        return n
    else:
        x = F(n-2) + F(n-1)       
        print x         
        return x
        
F(7)