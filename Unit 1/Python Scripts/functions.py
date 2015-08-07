# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:06:01 2015

@author: Graham
"""

number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
count_dict = collections.defaultdict(int)
for i in number_list:
    count_dict[i] += 1

print count_dict

number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
count = collections.Counter(number_list)


print count