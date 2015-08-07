# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:34:22 2015

@author: Graham
"""


phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

try:
    phone_book["Jamie Theakston"]
except:
    print "Name not found in phone book" 
    