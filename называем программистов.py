# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:04:42 2021

@author: Роман
"""



n = int(input())
if n % 10 == 1 and n not in (11, 111, 211, 311, 411, 511, 611, 711, 811, 911):
    print(str(n) + ' программист')
elif n % 10 ==1 and n in (11, 111, 211, 311, 411, 511, 611, 711, 811, 911):
    print(str(n) + ' программистов')
elif n % 10 in (2, 3, 4) and n // 10 not in (1, 11, 21, 31, 41, 51, 61, 71, 81, 91):
    print(str(n) + ' программиста')
else:
    print(str(n) + ' программистов')